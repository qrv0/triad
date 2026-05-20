"""Balanced 3D solver for the Triad anti-collapse simulation.

This module keeps the original Memory-NLS lineage but makes the numerical
conventions explicit:

    i hbar d_t Psi = [ -hbar^2/(2m) D^2 + V_ext + Lambda |Psi|^2
                       + V_mem + alpha(-Delta)^(sigma/2) - i Gamma ] Psi + eta

    V_mem = sum_j lambda_j y_j,    d_t y_j = nu_j (rho - y_j)

The step is a symmetric Strang-style composition:

    memory half-step -> potential half-step -> kinetic+dissipation full-step
    -> potential half-step -> memory half-step -> FDT noise

The memory field is advanced around the conservative field step instead of only
at the end. That makes the memory coupling less lagged than the historical
reference solver while preserving the delayed-memory mechanism that produces
anti-collapse.
"""

from __future__ import annotations

import math
import time
from dataclasses import asdict, dataclass, field
from typing import Callable, Optional

from .kernels import MemoryConfig, apply_spatial_kernel, build_spatial_kernel_fft_3d
from .precision import Precision, get_backend, to_cpu


@dataclass
class BalancedSolverConfig3D:
    """Parameters for a balanced 3D Triad simulation."""

    # Lattice
    N: int = 128
    L: float = 20.0
    dt: float = 0.0025
    n_steps: int = 2400

    # Equation parameters
    hbar: float = 1.0
    m: float = 1.0
    Lambda: float = -8.0
    sigma: float = 2.0
    alpha_frac: float = 0.0
    gamma_0: float = 0.0
    T: float = 0.0

    # Memory
    memory: MemoryConfig = field(
        default_factory=lambda: MemoryConfig(
            nus=[12.0, 3.0, 0.75],
            lambdas=[0.22, 0.18, 0.10],
            spatial="local",
        )
    )

    # External potential
    V_ext_amp: float = 0.0

    # Initial state
    init_sigma: float = 1.0
    init_k0: tuple[float, float, float] = (1.0, 0.5, 0.0)

    # Numerics
    precision: str = "fp32"
    seed: int = 42
    sample_every: int = 20
    frame_every: int = 20
    noise_dx_scaling: bool = True


def build_grid(cfg: BalancedSolverConfig3D, xp, prec: Precision):
    dx = cfg.L / cfg.N
    x = (xp.arange(cfg.N, dtype=prec.real) - cfg.N / 2) * dx
    return xp.meshgrid(x, x, x, indexing="ij"), dx


def build_initial_state(cfg: BalancedSolverConfig3D, xp, prec: Precision):
    (X, Y, Z), dx = build_grid(cfg, xp, prec)
    r2 = X * X + Y * Y + Z * Z
    envelope = xp.exp(-r2 / (2.0 * cfg.init_sigma * cfg.init_sigma)).astype(prec.real)
    kx, ky, kz = cfg.init_k0
    phase = (kx * X + ky * Y + kz * Z).astype(prec.real)
    psi = (envelope * xp.exp(1j * phase)).astype(prec.complex)
    norm = xp.sqrt(xp.sum(xp.abs(psi) ** 2) * dx**3)
    return psi / norm


def build_external_potential(cfg: BalancedSolverConfig3D, xp, prec: Precision):
    if cfg.V_ext_amp == 0.0:
        return None
    (X, Y, Z), _ = build_grid(cfg, xp, prec)
    r2 = X * X + Y * Y + Z * Z
    return (cfg.V_ext_amp * xp.exp(-r2 / 8.0)).astype(prec.real)


def build_kinetic_dissipative_propagator(cfg: BalancedSolverConfig3D, xp, prec: Precision):
    kvec = xp.fft.fftfreq(cfg.N, d=cfg.L / cfg.N) * 2.0 * math.pi
    kx, ky, kz = xp.meshgrid(kvec, kvec, kvec, indexing="ij")
    k2 = (kx * kx + ky * ky + kz * kz).astype(prec.real)
    k_mag = xp.sqrt(k2)

    h_kin = (cfg.hbar**2 / (2.0 * cfg.m)) * k2
    if cfg.alpha_frac != 0.0:
        h_kin = h_kin + cfg.alpha_frac * (k_mag**cfg.sigma)

    phase = xp.exp(-1j * h_kin.astype(prec.complex) * cfg.dt / cfg.hbar)
    dissipation = math.exp(-cfg.gamma_0 * cfg.dt / cfg.hbar)
    return (phase * dissipation).astype(prec.complex)


def _density(psi, xp, prec: Precision):
    return (psi.conj() * psi).real.astype(prec.real)


def _effective_density(rho, G_k, cfg: BalancedSolverConfig3D, xp, prec: Precision):
    if cfg.memory.spatial == "local" or G_k is None:
        return rho
    return apply_spatial_kernel(rho, G_k, xp=xp).astype(prec.real)


def _advance_memory(ys, rho_eff, half_dt: float, cfg: BalancedSolverConfig3D):
    for j, nu in enumerate(cfg.memory.nus):
        decay = math.exp(-nu * half_dt)
        ys[j] = decay * ys[j] + (1.0 - decay) * rho_eff
    return ys


def _memory_potential(ys, cfg: BalancedSolverConfig3D, xp, template):
    v_mem = xp.zeros_like(template)
    for y, lam in zip(ys, cfg.memory.lambdas):
        v_mem = v_mem + lam * y
    return v_mem


def _potential_step(psi, ys, V_ext, half_dt: float, cfg: BalancedSolverConfig3D, xp, prec: Precision):
    rho = _density(psi, xp, prec)
    v_tot = cfg.Lambda * rho + _memory_potential(ys, cfg, xp, rho)
    if V_ext is not None:
        v_tot = v_tot + V_ext
    return psi * xp.exp(-1j * v_tot.astype(prec.complex) * half_dt / cfg.hbar)


def _add_fdt_noise(psi, cfg: BalancedSolverConfig3D, dx: float, xp, prec: Precision, rng):
    if cfg.gamma_0 <= 0.0 or cfg.T <= 0.0:
        return psi

    # Discrete white-noise convention: delta(x-x') becomes 1/dx^3 on a 3D grid.
    spatial = dx ** (-1.5) if cfg.noise_dx_scaling else 1.0
    amp = math.sqrt(2.0 * cfg.gamma_0 * cfg.T * cfg.dt) * spatial
    xi = (rng.standard_normal(psi.shape) + 1j * rng.standard_normal(psi.shape)).astype(prec.complex)
    return psi + (amp / math.sqrt(2.0)) * xi


def step(psi, ys, U_k, V_ext, G_k, cfg: BalancedSolverConfig3D, t: float, xp, prec: Precision, rng):
    dt = cfg.dt
    dx = cfg.L / cfg.N

    rho0 = _density(psi, xp, prec)
    ys = _advance_memory(ys, _effective_density(rho0, G_k, cfg, xp, prec), dt * 0.5, cfg)

    psi = _potential_step(psi, ys, V_ext, dt * 0.5, cfg, xp, prec)
    psi = xp.fft.ifftn(xp.fft.fftn(psi) * U_k).astype(prec.complex)
    psi = _potential_step(psi, ys, V_ext, dt * 0.5, cfg, xp, prec)

    rho1 = _density(psi, xp, prec)
    ys = _advance_memory(ys, _effective_density(rho1, G_k, cfg, xp, prec), dt * 0.5, cfg)
    psi = _add_fdt_noise(psi, cfg, dx, xp, prec, rng).astype(prec.complex)

    return psi, ys, t + dt


def default_observables(cfg: BalancedSolverConfig3D):
    dx = cfg.L / cfg.N

    def observe(psi, ys, t, step_idx, xp):
        rho = (psi.conj() * psi).real
        norm = xp.sqrt(xp.sum(rho) * dx**3)
        peak = xp.max(rho)
        participation = (xp.sum(rho) ** 2) / (xp.sum(rho * rho) + 1e-30)
        return {
            "step": int(step_idx),
            "t": float(t),
            "norm": float(to_cpu(norm)),
            "peak": float(to_cpu(peak)),
            "participation": float(to_cpu(participation)),
        }

    return observe


def run(
    cfg: BalancedSolverConfig3D,
    observables_fn: Optional[Callable] = None,
    collect_frames: bool = False,
    verbose: bool = True,
) -> dict:
    xp = get_backend()
    prec = Precision(cfg.precision)
    rng = xp.random.default_rng(cfg.seed)

    psi = build_initial_state(cfg, xp, prec)
    ys = [xp.zeros_like(psi.real).astype(prec.real) for _ in range(cfg.memory.n_modes)]
    U_k = build_kinetic_dissipative_propagator(cfg, xp, prec)
    V_ext = build_external_potential(cfg, xp, prec)

    if cfg.memory.spatial != "local":
        G_k = build_spatial_kernel_fft_3d(cfg.N, cfg.L, cfg.memory.spatial, cfg.memory.scale, xp=xp, dtype=prec.real)
    else:
        G_k = None

    if observables_fn is None:
        observables_fn = default_observables(cfg)

    samples = []
    frames = []
    t = 0.0
    start = time.time()

    for step_idx in range(cfg.n_steps + 1):
        if step_idx % cfg.sample_every == 0:
            sample = observables_fn(psi, ys, t, step_idx, xp)
            samples.append(sample)
            if verbose and step_idx % max(cfg.sample_every * 10, 1) == 0:
                print(
                    f"step {step_idx:6d}/{cfg.n_steps} t={t:7.3f} "
                    f"norm={sample['norm']:.6f} peak={sample['peak']:.5g}"
                )

        if collect_frames and step_idx % cfg.frame_every == 0:
            rho_mid = _density(psi, xp, prec)[:, :, cfg.N // 2]
            frames.append(to_cpu(rho_mid))

        if step_idx == cfg.n_steps:
            break
        psi, ys, t = step(psi, ys, U_k, V_ext, G_k, cfg, t, xp, prec, rng)

    wall = time.time() - start
    if verbose:
        print(f"completed in {wall:.1f}s")

    return {
        "psi_final": to_cpu(psi),
        "ys_final": [to_cpu(y) for y in ys],
        "samples": samples,
        "frames": frames,
        "config": _config_to_dict(cfg),
        "wall_time": wall,
        "backend": xp.__name__,
    }


def _config_to_dict(cfg: BalancedSolverConfig3D) -> dict:
    data = asdict(cfg)
    data["memory"] = asdict(cfg.memory)
    return data
