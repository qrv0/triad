"""Phase 9 wave-3 (corrected 2026-05-17): phase diagram 2D slice
Sigma_lambda x gamma_0 at d=3.

First focused contribution to open-problems/02 (full phase diagram). Sweeps
(Sigma_lambda, gamma_0) at fixed d=3 with the canonical 3D anti-collapse config.

This is the corrected version replacing the 2026-05-16 wrong-config test
flagged in docs/llm-hedge-annotations.md (Phase 9 wave-3 cluster, Failure 4).
The previous version used sigma_init=1.2 with non-normalized Gaussian (inherited
from the wrong vibrational test), placing the system in a noise-amplification
regime rather than the focal-collapse regime; the regime classifications were
biased by thermal noise on a weak field, not the structural phase structure.

Canonical config (this version):
- d=3, N=48 (compromise; canonical anti-collapse uses N=128)
- L=20 (canonical, matching results/04)
- sigma_init=0.5 with psi normalized to total norm = 1
- Lambda=-8 (canonical supercritical)
- Sigma_lambda swept: {0.5, 1.0, 1.5, 2.0, 4.0} (covers crystalline window
  and into anti-collapse regime; 0 excluded since the test
  is in the focal-collapse-with-memory regime)
- gamma_0 swept: {0.01, 0.05, 0.2, 1.0} (0.01 is the
  minimum permitted)
- T_bath=0.001 (small to minimize thermal contamination of regime
  classification)
- Memory: 75/25 split (lambda_fast = 0.75*Sigma_lambda, lambda_slow = 0.25*Sigma_lambda)
- n_steps=2000 sufficient for regime classification

Regime classification (per results/04 + paper Section 6.1 phenomenology):
- "collapse": peak grows to lattice scale (>~10x initial) and stays there
- "released": peak grows transiently then drops below initial (anti-collapse mechanism)
- "stable": peak stays within ~2x of initial throughout
- "runaway": peak grows unboundedly (memory over-coupling at very high Sigma_lambda)
- "dispersive": peak drops below initial without any growth phase

Output: outputs/phase_diagram_2d_slice/{summary.json, ...}.
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


def fft_kinetic_propagator(N: int, L: float, dt: float, gamma_0: float, d: int = 3):
    """Canonical kinetic propagator U_k with dissipation folded in.

    Matches implementation/physics/solver_3d.py build_kinetic_propagator
    structure: H_complex = k^2/(2m) - i gamma_0, U_k = exp(-i H_complex dt).
    The dissipation factor exp(-gamma_0 dt) appears as part of the K step
    rather than as a separate sub-step.
    """
    k_axis = 2 * xp.pi * xp.fft.fftfreq(N, d=L / N)
    grids = xp.meshgrid(*[k_axis] * d, indexing="ij")
    k_squared = sum(g ** 2 for g in grids)
    H_kin = 0.5 * k_squared
    H_complex = H_kin.astype(xp.complex64) - 1j * gamma_0
    return xp.exp(-1j * H_complex * dt).astype(xp.complex64)


def initial_gaussian_normalized_3d(N: int, L: float, sigma_init: float):
    """Canonical initial state matching solver_3d.py build_initial_state."""
    coord = xp.linspace(-L / 2, L / 2, N, endpoint=False)
    X, Y, Z = xp.meshgrid(coord, coord, coord, indexing="ij")
    r_squared = X ** 2 + Y ** 2 + Z ** 2
    psi = xp.exp(-r_squared / (2 * sigma_init ** 2)).astype(xp.complex64)
    dx = L / N
    norm = float(xp.sqrt(xp.sum(xp.abs(psi) ** 2) * dx ** 3))
    psi = psi / norm
    return psi


def run_grid_point(N: int, L: float, Lambda: float, Sigma_lambda: float,
                   gamma_0: float, T_bath: float,
                   nu_fast: float = 10.0, nu_slow: float = 0.5,
                   dt: float = 0.0025, n_steps: int = 2000,
                   sigma_init: float = 0.5, seed: int = 42) -> dict:
    """3D anti-collapse / phase-classification run with P3 active."""
    rng = np.random.default_rng(seed)
    psi = initial_gaussian_normalized_3d(N, L, sigma_init)
    propagator = fft_kinetic_propagator(N, L, dt, gamma_0, d=3)

    lambda_fast = Sigma_lambda * 0.75
    lambda_slow = Sigma_lambda * 0.25
    y_fast = xp.zeros_like(psi.real, dtype=xp.float32)
    y_slow = xp.zeros_like(psi.real, dtype=xp.float32)
    decay_fast = float(np.exp(-nu_fast * dt))
    decay_slow = float(np.exp(-nu_slow * dt))
    accum_fast = 1.0 - decay_fast
    accum_slow = 1.0 - decay_slow

    noise_amp = float(np.sqrt(2.0 * gamma_0 * T_bath * dt))

    initial_norm = float(xp.sum(xp.abs(psi) ** 2) * (L / N) ** 3)
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
    final_norm = float(xp.sum(xp.abs(psi) ** 2) * (L / N) ** 3)

    peak_growth = max_peak / max(initial_peak, 1e-12)
    final_ratio = final_peak / max(initial_peak, 1e-12)

    # Regime classification per results/04 + paper Section 6.1
    if peak_growth > 50 and final_ratio > 10:
        regime = "collapse"  # locked at lattice / very high peak throughout
    elif peak_growth > 5 and final_ratio < 0.5:
        regime = "released"  # anti-collapse mechanism: grew then released
    elif peak_growth > 50:
        regime = "runaway"  # peak grows large and stays unstable
    elif 0.5 <= final_ratio <= 2.0:
        regime = "stable"
    elif final_ratio < 0.5 and peak_growth < 2:
        regime = "dispersive"
    else:
        regime = "intermediate"

    return {
        "Sigma_lambda": Sigma_lambda, "gamma_0": gamma_0,
        "initial_peak": initial_peak, "max_peak": max_peak,
        "final_peak": final_peak, "final_norm": final_norm,
        "peak_growth_ratio": peak_growth,
        "final_ratio": final_ratio,
        "regime": regime,
        "wall_time": wall,
    }


def main():
    print(f"Phase 9 wave-3 (CORRECTED): phase diagram 2D slice at d=3")
    print(f"Backend: {'cupy (GPU)' if USING_GPU else 'numpy (CPU)'}")
    print(f"Canonical 3D anti-collapse config per results/04 + paper Section 6.1")

    N = 48
    L = 20.0
    Lambda = -8.0
    T_bath = 0.001
    n_steps = 2000

    SIGMA_LAMBDA_VALUES = [0.5, 1.0, 1.5, 2.0, 4.0]
    GAMMA_0_VALUES = [0.01, 0.05, 0.2, 1.0]

    print(f"\nConfiguration:")
    print(f"  N = {N} ({N**3:,} voxels), L = {L}, Lambda = {Lambda}, T_bath = {T_bath}")
    print(f"  sigma_init = 0.5 normalized to total norm 1")
    print(f"  n_steps = {n_steps}, dt = 0.0025")
    print(f"  Sigma_lambda: {SIGMA_LAMBDA_VALUES}")
    print(f"  gamma_0: {GAMMA_0_VALUES}")
    print(f"  Total grid points: {len(SIGMA_LAMBDA_VALUES) * len(GAMMA_0_VALUES)}")

    t_total = time.time()
    grid = []
    for sl in SIGMA_LAMBDA_VALUES:
        for g0 in GAMMA_0_VALUES:
            r = run_grid_point(N=N, L=L, Lambda=Lambda, Sigma_lambda=sl,
                               gamma_0=g0, T_bath=T_bath, n_steps=n_steps,
                               seed=42 + int(sl * 10) + int(g0 * 100))
            grid.append(r)
            print(f"  Sl={sl:>5.2f}, g0={g0:>5.2f}: regime={r['regime']:>14s}  "
                  f"peak_growth={r['peak_growth_ratio']:>10.2f}  "
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

    print(f"\nRegime map (Sigma_lambda rows, gamma_0 cols):")
    print(f"  {'':>10s}  ", end="")
    for g0 in GAMMA_0_VALUES:
        print(f"{f'g={g0}':>18s}", end="")
    print()
    for sl in SIGMA_LAMBDA_VALUES:
        print(f"  Sl={sl:>5.2f}  ", end="")
        for g0 in GAMMA_0_VALUES:
            point = next(r for r in grid if r["Sigma_lambda"] == sl and r["gamma_0"] == g0)
            print(f"{point['regime']:>18s}", end="")
        print()

    summary = {
        "prediction_tested": "Phase diagram 2D slice for open-problems/02, canonical config",
        "config": {
            "N": N, "L": L, "Lambda": Lambda, "T_bath": T_bath,
            "n_steps": n_steps, "dt": 0.0025,
            "nu_fast": 10.0, "nu_slow": 0.5,
            "sigma_init": 0.5, "normalized": True,
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
