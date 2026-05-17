"""Phase 9 wave-3 phase diagram 2D slice: Sigma_lambda x gamma_0 at d=3.

**METHODOLOGICAL FLAG (2026-05-17 audit):** this script uses sigma_init=1.2
with non-normalized Gaussian (same wrong convention as test_vibrational_3d.py),
giving peak |Psi|^2 ~ 0.037, ~40x weaker than the canonical 3D config
(sigma_init=0.5 normalized to total norm 1, peak ~1.44). At this amplitude
the field is in the noise-amplification regime rather than the focal-collapse
regime; the "regime classifications" produced are biased toward dispersive /
intermediate at low gamma and collapse / runaway at high gamma due to thermal
noise injection on a weak field, not due to the structural Sigma_lambda x
gamma_0 phase structure. The proper sweep requires sigma_init=0.5 normalized,
matching the results/04 3D anti-collapse config. See docs/llm-hedge-annotations.md.

First focused contribution to open-problems/02 (full phase diagram).
Sweeps (Sigma_lambda, gamma_0) at fixed d=3, Lambda=-8.0, T_bath=0.05,
nu_fast=10, nu_slow=0.5. Classifies each grid point by qualitative regime
(released, collapse, runaway, dispersive).

Output: outputs/phase_diagram_2d_slice/{summary.json, grid.npy}.
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
OUTPUT_DIR = REPO_ROOT / "outputs" / "phase_diagram_2d_slice"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def to_cpu(arr):
    return arr.get() if hasattr(arr, "get") else arr


def fft_kinetic_phase(N: int, L: float, d: int = 3):
    k_axis = 2 * xp.pi * xp.fft.fftfreq(N, d=L / N)
    grids = xp.meshgrid(*[k_axis] * d, indexing="ij")
    k_squared = sum(g ** 2 for g in grids)
    return -1j * 0.5 * k_squared


def initial_gaussian_3d(N: int, L: float, sigma_init: float):
    coord = xp.linspace(-L / 2, L / 2, N, endpoint=False)
    X, Y, Z = xp.meshgrid(coord, coord, coord, indexing="ij")
    r_squared = X ** 2 + Y ** 2 + Z ** 2
    psi = (1.0 / (sigma_init * float(np.sqrt(2 * np.pi)))) ** 1.5
    psi = psi * xp.exp(-r_squared / (2 * sigma_init ** 2))
    return psi.astype(xp.complex64)


def run_grid_point(N: int, L: float, Lambda: float, Sigma_lambda: float,
                   gamma_0: float, T_bath: float,
                   nu_fast: float = 10.0, nu_slow: float = 0.5,
                   dt: float = 0.005, n_steps: int = 2000,
                   sigma_init: float = 1.2, seed: int = 42) -> dict:
    """3D anti-collapse run with P3 active; return regime classification."""
    rng = np.random.default_rng(seed)
    psi = initial_gaussian_3d(N, L, sigma_init)
    kinetic_phase = fft_kinetic_phase(N, L, d=3)
    propagator = xp.exp(kinetic_phase * dt)

    if Sigma_lambda > 0:
        lambda_fast = Sigma_lambda * 0.75
        lambda_slow = Sigma_lambda * 0.25
        y_fast = xp.zeros_like(psi.real, dtype=xp.float32)
        y_slow = xp.zeros_like(psi.real, dtype=xp.float32)
        decay_fast = float(np.exp(-nu_fast * dt))
        decay_slow = float(np.exp(-nu_slow * dt))
        accum_fast = 1.0 - decay_fast
        accum_slow = 1.0 - decay_slow
        memory_active = True
    else:
        memory_active = False

    dissipation_factor = float(np.exp(-gamma_0 * dt))
    noise_amp = float(np.sqrt(2.0 * gamma_0 * T_bath * dt))

    initial_norm = float(xp.sum(xp.abs(psi) ** 2) * (L / N) ** 3)
    initial_peak = float(xp.max(xp.abs(psi) ** 2))

    peaks = [initial_peak]
    max_peak_seen = initial_peak

    t0 = time.time()
    for step in range(n_steps):
        rho = (psi.real ** 2 + psi.imag ** 2).astype(xp.float32)
        V_mem = (lambda_fast * y_fast + lambda_slow * y_slow) if memory_active else 0.0
        V_total = Lambda * rho + V_mem
        psi = psi * xp.exp(-1j * V_total * dt / 2)

        psi = xp.fft.ifftn(xp.fft.fftn(psi) * propagator)

        rho = (psi.real ** 2 + psi.imag ** 2).astype(xp.float32)
        V_mem = (lambda_fast * y_fast + lambda_slow * y_slow) if memory_active else 0.0
        V_total = Lambda * rho + V_mem
        psi = psi * xp.exp(-1j * V_total * dt / 2)

        if memory_active:
            y_fast = decay_fast * y_fast + accum_fast * rho
            y_slow = decay_slow * y_slow + accum_slow * rho

        if gamma_0 > 0:
            psi = psi * dissipation_factor

        if noise_amp > 0:
            shape = psi.shape
            xi_re = xp.asarray(rng.standard_normal(shape).astype(np.float32))
            xi_im = xp.asarray(rng.standard_normal(shape).astype(np.float32))
            psi = psi + noise_amp * (xi_re + 1j * xi_im) / float(np.sqrt(2.0))

        if step % 50 == 0:
            cur_peak = float(xp.max((psi.real ** 2 + psi.imag ** 2)))
            peaks.append(cur_peak)
            if cur_peak > max_peak_seen:
                max_peak_seen = cur_peak

    wall = time.time() - t0
    final_peak = peaks[-1]
    final_norm = float(xp.sum(xp.abs(psi) ** 2) * (L / N) ** 3)

    # Regime classification
    peak_growth_ratio = max_peak_seen / max(initial_peak, 1e-10)
    final_ratio = final_peak / max(initial_peak, 1e-10)
    norm_growth = final_norm / max(initial_norm, 1e-10)

    if peak_growth_ratio > 100:
        regime = "runaway"  # field blew up
    elif peak_growth_ratio > 10 and final_ratio > 5:
        regime = "collapse"  # focal density sustained at high value
    elif final_ratio < 0.5 and norm_growth > 3:
        regime = "dispersive_noise_dominated"  # field disperses; noise contributes much to norm
    elif final_ratio < 0.5:
        regime = "released"  # field disperses, anti-collapse-like
    elif 0.5 <= final_ratio <= 2.0:
        regime = "stable"
    else:
        regime = "intermediate"

    return {
        "Sigma_lambda": Sigma_lambda, "gamma_0": gamma_0,
        "initial_peak": initial_peak, "max_peak_seen": max_peak_seen,
        "final_peak": final_peak, "final_norm": final_norm,
        "peak_growth_ratio": peak_growth_ratio,
        "final_ratio": final_ratio,
        "norm_growth": norm_growth,
        "regime": regime,
        "wall_time": wall,
    }


def main():
    print(f"Phase 9 wave-3 phase diagram 2D slice (Sigma_lambda x gamma_0) at d=3")
    print(f"Backend: {'cupy (GPU)' if USING_GPU else 'numpy (CPU)'}")

    N = 24
    L = 10.0
    Lambda = -8.0
    T_bath = 0.05
    n_steps = 2000

    SIGMA_LAMBDA_VALUES = [0.0, 0.5, 2.0, 8.0]
    GAMMA_0_VALUES = [0.01, 0.05, 0.2, 1.0]

    print(f"\nConfiguration:")
    print(f"  N = {N}, L = {L}, Lambda = {Lambda}, T_bath = {T_bath}")
    print(f"  n_steps = {n_steps}, dt = 0.005")
    print(f"  Sigma_lambda values: {SIGMA_LAMBDA_VALUES}")
    print(f"  gamma_0 values: {GAMMA_0_VALUES}")
    print(f"  Total grid points: {len(SIGMA_LAMBDA_VALUES) * len(GAMMA_0_VALUES)}")

    t_total = time.time()
    grid = []
    for sl in SIGMA_LAMBDA_VALUES:
        for g0 in GAMMA_0_VALUES:
            r = run_grid_point(N=N, L=L, Lambda=Lambda, Sigma_lambda=sl,
                               gamma_0=g0, T_bath=T_bath, n_steps=n_steps,
                               seed=42 + int(sl * 10) + int(g0 * 100))
            grid.append(r)
            print(f"  Sigma_lambda={sl:>5.2f}, gamma_0={g0:>5.2f}: "
                  f"regime={r['regime']:>26s}  "
                  f"peak_growth={r['peak_growth_ratio']:>8.2f}  "
                  f"final_ratio={r['final_ratio']:>8.4f}  "
                  f"norm_growth={r['norm_growth']:>6.2f}  "
                  f"t={r['wall_time']:.1f}s")

    t_total = time.time() - t_total

    print(f"\nTotal wall time: {t_total:.1f}s")

    # Tabulate by regime
    regime_counts = {}
    for r in grid:
        regime_counts[r["regime"]] = regime_counts.get(r["regime"], 0) + 1
    print(f"\nRegime counts across grid:")
    for regime, count in sorted(regime_counts.items()):
        print(f"  {regime:>26s}: {count}")

    # Print regime map (Sigma_lambda rows, gamma_0 cols)
    print(f"\nRegime map (Sigma_lambda rows, gamma_0 cols):")
    print(f"  {'':>10s}  ", end="")
    for g0 in GAMMA_0_VALUES:
        print(f"{f'g={g0}':>30s}", end="")
    print()
    for sl in SIGMA_LAMBDA_VALUES:
        print(f"  Sl={sl:>5.2f}  ", end="")
        for g0 in GAMMA_0_VALUES:
            point = next(r for r in grid if r["Sigma_lambda"] == sl and r["gamma_0"] == g0)
            print(f"{point['regime']:>30s}", end="")
        print()

    summary = {
        "prediction_tested": "Phase 9 wave-3 phase diagram 2D slice for open-problems/02",
        "config": {
            "N": N, "L": L, "Lambda": Lambda, "T_bath": T_bath,
            "n_steps": n_steps, "dt": 0.005,
            "nu_fast": 10.0, "nu_slow": 0.5,
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
