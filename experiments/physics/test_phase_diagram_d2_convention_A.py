"""Phase diagram 2D slice at d=2 using Convention A (dimensional-rescaling series).

Convention A: sigma_init=0.4 with non-normalized Gaussian
  psi_0 = (1/(sigma*sqrt(2pi)))^(d/2) * exp(-r^2/(2 sigma^2))
The continuum L2 norm of this Gaussian is 1; on a discrete grid the
norm differs from 1 by lattice effects. This is the convention used
in results/06, 10, 15, 24 (the dimensional-rescaling series).

Companion to test_phase_diagram_d2_slice.py which uses Convention B
(sigma=0.5 normalized to discrete L2 norm 1).

Purpose: cross-convention check at d=2. Per results/30 (dimensional-
rescaling-convention audit), the two conventions probe different regions
of the same equation. This script tests whether the d=2 phase-diagram
regime structure is convention-stable or convention-dependent.

Inherits the Strang split-step solver from test_phase_diagram_d2_slice.py
via direct copy of the same loop structure; only the initial state
function differs.

Output: outputs/phase_diagram_d2_convention_A/summary.json.

Wall time estimate: ~5 min on RTX 4060 (N=128, 20 grid points, 2000 steps).
"""

from __future__ import annotations
import json
import time
from pathlib import Path

import numpy as np

try:
    import cupy as cp
    xp = cp
    USING_GPU = True
except ImportError:
    xp = np
    USING_GPU = False


REPO_ROOT = Path(__file__).parent.parent.parent
OUTPUT_DIR = REPO_ROOT / "outputs" / "phase_diagram_d2_convention_A"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def to_cpu(arr):
    return arr.get() if hasattr(arr, "get") else arr


def fft_kinetic_phase(N: int, L: float, d: int = 2):
    k_axis = 2 * xp.pi * xp.fft.fftfreq(N, d=L / N)
    grids = xp.meshgrid(*[k_axis] * d, indexing="ij")
    k_squared = sum(g ** 2 for g in grids)
    return -1j * 0.5 * k_squared


def initial_gaussian_convention_A_2d(N: int, L: float, sigma_init: float):
    """Convention A: 2D Gaussian, NON-normalized (uses dimensional-rescaling series formula).

    psi_0 = (1/(sigma*sqrt(2pi)))^(d/2) * exp(-r^2/(2 sigma^2))
    Continuum L2 norm is 1; discrete norm depends on lattice.
    """
    coord = xp.linspace(-L / 2, L / 2, N, endpoint=False)
    X, Y = xp.meshgrid(coord, coord, indexing="ij")
    r_squared = X ** 2 + Y ** 2
    prefactor = (1.0 / (sigma_init * float(np.sqrt(2 * np.pi)))) ** (2 / 2)
    psi = prefactor * xp.exp(-r_squared / (2 * sigma_init ** 2))
    return psi.astype(xp.complex64)


def run_grid_point(N: int, L: float, Lambda: float, Sigma_lambda: float,
                   gamma_0: float, T_bath: float,
                   nu_fast: float = 10.0, nu_slow: float = 0.5,
                   dt: float = 0.0025, n_steps: int = 2000,
                   sigma_init: float = 0.4, seed: int = 42) -> dict:
    """2D anti-collapse / phase-classification run with P3 active, Convention A."""
    rng = np.random.default_rng(seed)
    psi = initial_gaussian_convention_A_2d(N, L, sigma_init)
    kinetic_phase = fft_kinetic_phase(N, L, d=2)
    propagator = xp.exp(kinetic_phase * dt)

    lambda_fast = Sigma_lambda * 0.75
    lambda_slow = Sigma_lambda * 0.25
    y_fast = xp.zeros_like(psi.real, dtype=xp.float32)
    y_slow = xp.zeros_like(psi.real, dtype=xp.float32)
    decay_fast = float(np.exp(-nu_fast * dt))
    decay_slow = float(np.exp(-nu_slow * dt))
    accum_fast = 1.0 - decay_fast
    accum_slow = 1.0 - decay_slow

    dissipation_factor = float(np.exp(-gamma_0 * dt))
    noise_amp = float(np.sqrt(2.0 * gamma_0 * T_bath * dt))

    initial_norm = float(xp.sum(xp.abs(psi) ** 2) * (L / N) ** 2)
    initial_peak = float(xp.max(xp.abs(psi) ** 2))

    peaks = [initial_peak]
    max_peak = initial_peak

    t0 = time.time()
    for step in range(n_steps):
        rho = (psi.real ** 2 + psi.imag ** 2).astype(xp.float32)
        V_mem = lambda_fast * y_fast + lambda_slow * y_slow
        V_total = Lambda * rho + V_mem
        psi = psi * xp.exp(-1j * V_total * dt / 2)
        psi = xp.fft.ifftn(xp.fft.fftn(psi) * propagator)
        rho = (psi.real ** 2 + psi.imag ** 2).astype(xp.float32)
        V_mem = lambda_fast * y_fast + lambda_slow * y_slow
        V_total = Lambda * rho + V_mem
        psi = psi * xp.exp(-1j * V_total * dt / 2)
        y_fast = decay_fast * y_fast + accum_fast * rho
        y_slow = decay_slow * y_slow + accum_slow * rho
        psi = psi * dissipation_factor
        if noise_amp > 0:
            xi_re = xp.asarray(rng.standard_normal(psi.shape).astype(np.float32))
            xi_im = xp.asarray(rng.standard_normal(psi.shape).astype(np.float32))
            psi = psi + noise_amp * (xi_re + 1j * xi_im) / float(np.sqrt(2.0))

        if step % 25 == 0:
            cur_peak = float(xp.max((psi.real ** 2 + psi.imag ** 2)))
            peaks.append(cur_peak)
            if cur_peak > max_peak:
                max_peak = cur_peak

    wall = time.time() - t0
    final_peak = peaks[-1]
    final_norm = float(xp.sum(xp.abs(psi) ** 2) * (L / N) ** 2)

    peak_growth = max_peak / max(initial_peak, 1e-12)
    final_ratio = final_peak / max(initial_peak, 1e-12)

    if peak_growth > 50 and final_ratio > 10:
        regime = "collapse"
    elif peak_growth > 5 and final_ratio < 0.5:
        regime = "released"
    elif peak_growth > 50:
        regime = "runaway"
    elif 0.5 <= final_ratio <= 2.0:
        regime = "stable"
    elif final_ratio < 0.5 and peak_growth < 2:
        regime = "dispersive"
    else:
        regime = "intermediate"

    return {
        "Sigma_lambda": Sigma_lambda, "gamma_0": gamma_0,
        "initial_peak": initial_peak, "initial_norm": initial_norm,
        "max_peak": max_peak,
        "final_peak": final_peak, "final_norm": final_norm,
        "peak_growth_ratio": peak_growth,
        "final_ratio": final_ratio,
        "regime": regime,
        "wall_time": wall,
    }


def main():
    print(f"Phase diagram d=2 Convention A (sigma=0.4 non-normalized)")
    print(f"Backend: {'cupy (GPU)' if USING_GPU else 'numpy (CPU)'}")
    print(f"Companion to Convention B test_phase_diagram_d2_slice.py")

    d = 2
    N = 128
    L = 20.0
    Lambda = -8.0
    T_bath = 0.001
    n_steps = 2000

    SIGMA_LAMBDA_VALUES = [0.05, 0.1, 0.5, 1.0, 2.0]
    GAMMA_0_VALUES = [0.01, 0.05, 0.2, 1.0]

    psi_init = initial_gaussian_convention_A_2d(N, L, 0.4)
    dx = L / N
    print(f"\nInitial state (d=2, sigma=0.4, Convention A):")
    print(f"  Peak |Psi|^2: {float(xp.max(xp.abs(psi_init) ** 2)):.4f}")
    print(f"  Discrete L2 norm: {float(xp.sum(xp.abs(psi_init) ** 2) * dx ** 2):.4f}")
    print(f"\nConfiguration:")
    print(f"  N = {N} ({N**d:,} voxels), L = {L}, Lambda = {Lambda}, T_bath = {T_bath}")
    print(f"  n_steps = {n_steps}, dt = 0.0025")
    print(f"  Sigma_lambda: {SIGMA_LAMBDA_VALUES}")
    print(f"  gamma_0: {GAMMA_0_VALUES}")

    t_total = time.time()
    grid = []
    for sl in SIGMA_LAMBDA_VALUES:
        for g0 in GAMMA_0_VALUES:
            seed = 42 + int(sl * 10) + int(g0 * 100)
            r = run_grid_point(N=N, L=L, Lambda=Lambda, Sigma_lambda=sl,
                               gamma_0=g0, T_bath=T_bath, n_steps=n_steps, seed=seed)
            grid.append(r)
            print(f"  Sl={sl:>5.2f}, g0={g0:>5.2f}: regime={r['regime']:>14s}  "
                  f"peak_growth={r['peak_growth_ratio']:>8.2f}  "
                  f"final_ratio={r['final_ratio']:>10.4f}  "
                  f"t={r['wall_time']:.1f}s")

    t_total = time.time() - t_total
    print(f"\nTotal wall: {t_total:.1f}s")

    regime_counts = {}
    for r in grid:
        regime_counts[r["regime"]] = regime_counts.get(r["regime"], 0) + 1
    print(f"\nRegime counts:")
    for regime, count in sorted(regime_counts.items()):
        print(f"  {regime:>14s}: {count}")

    summary = {
        "prediction_tested": "Phase diagram d=2 slice, Convention A (sigma=0.4 non-normalized)",
        "convention": "A",
        "config": {
            "d": d, "N": N, "L": L, "Lambda": Lambda, "T_bath": T_bath,
            "n_steps": n_steps, "dt": 0.0025,
            "nu_fast": 10.0, "nu_slow": 0.5,
            "sigma_init": 0.4, "normalized": False,
            "initial_peak": float(xp.max(xp.abs(psi_init) ** 2)),
            "initial_norm": float(xp.sum(xp.abs(psi_init) ** 2) * dx ** 2),
        },
        "sigma_lambda_values": SIGMA_LAMBDA_VALUES,
        "gamma_0_values": GAMMA_0_VALUES,
        "grid": grid,
        "regime_counts": regime_counts,
        "wall_time_total_s": t_total,
        "backend": "cupy" if USING_GPU else "numpy",
    }
    with open(OUTPUT_DIR / "summary.json", "w") as f:
        json.dump(summary, f, indent=2)
    print(f"\nSummary written to {OUTPUT_DIR}/summary.json")


if __name__ == "__main__":
    main()
