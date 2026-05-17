"""Phase diagram 2D slice (Sigma_lambda x gamma_0) at d=2.

Extends the canonical d=3 phase-diagram methodology (results/26,
experiments/physics/test_phase_diagram_2d_slice.py) to d=2, where the cubic
NLS is L2-critical rather than L2-supercritical. The structural prediction is
that the focal-collapse dynamics differ qualitatively from d=3 because at d=2
the collapse threshold is kinematic (Townes soliton) rather than generic, so
the released-regime basin in the (Sigma_lambda, gamma_0) plane is expected
to have a different shape.

Canonical convention extended to d=2: sigma_init=0.5 normalized to total
norm 1 (2D L2 norm). This is the convention of the canonical anti-collapse
series (results/04, 25, 26), not the convention of the dimensional-rescaling
series (results/10/15/24, which uses sigma=0.4 non-normalized). The two
conventions are internally consistent within their own series; this script
adheres to the canonical anti-collapse convention extended to d=2.

Configuration:
- d=2, N=128 (16384 voxels per field; canonical d=2 anti-collapse in
  results/01 uses N=256, this is a compromise for the 20-point sweep)
- L=20, dt=0.0025, n_steps=2000
- sigma_init=0.5 normalized; initial peak depends on d (computed and
  printed in script header output)
- Lambda=-8
- T_bath=0.001 (matching d=3 canonical phase diagram)
- Sigma_lambda swept: {0.05, 0.1, 0.5, 1.0, 2.0} (d=2 critical ratio per
  results/06 is ~0.05 so this sweep covers below threshold and into the
  released regime)
- gamma_0 swept: {0.01, 0.05, 0.2, 1.0} (all positive per Rule A)
- 75/25 memory split with nu_fast=10, nu_slow=0.5

Regime classification same as the d=3 canonical script.

Output: outputs/phase_diagram_d2_slice/{summary.json, run.log}.
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
OUTPUT_DIR = REPO_ROOT / "outputs" / "phase_diagram_d2_slice"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def to_cpu(arr):
    return arr.get() if hasattr(arr, "get") else arr


def fft_kinetic_phase(N: int, L: float, d: int = 2):
    k_axis = 2 * xp.pi * xp.fft.fftfreq(N, d=L / N)
    grids = xp.meshgrid(*[k_axis] * d, indexing="ij")
    k_squared = sum(g ** 2 for g in grids)
    return -1j * 0.5 * k_squared


def initial_gaussian_normalized_2d(N: int, L: float, sigma_init: float):
    """Canonical initial state: 2D Gaussian normalized to total norm 1."""
    coord = xp.linspace(-L / 2, L / 2, N, endpoint=False)
    X, Y = xp.meshgrid(coord, coord, indexing="ij")
    r_squared = X ** 2 + Y ** 2
    psi = xp.exp(-r_squared / (2 * sigma_init ** 2)).astype(xp.complex64)
    dx = L / N
    norm = float(xp.sqrt(xp.sum(xp.abs(psi) ** 2) * dx ** 2))
    psi = psi / norm
    return psi


def run_grid_point(N: int, L: float, Lambda: float, Sigma_lambda: float,
                   gamma_0: float, T_bath: float,
                   nu_fast: float = 10.0, nu_slow: float = 0.5,
                   dt: float = 0.0025, n_steps: int = 2000,
                   sigma_init: float = 0.5, seed: int = 42) -> dict:
    """2D anti-collapse / phase-classification run with P3 active."""
    rng = np.random.default_rng(seed)
    psi = initial_gaussian_normalized_2d(N, L, sigma_init)
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

    # Regime classification per results/04 + paper Section 6.1 (same as d=3 script)
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
        "initial_peak": initial_peak, "max_peak": max_peak,
        "final_peak": final_peak, "final_norm": final_norm,
        "peak_growth_ratio": peak_growth,
        "final_ratio": final_ratio,
        "regime": regime,
        "wall_time": wall,
    }


def main():
    print(f"Phase diagram 2D slice at d=2 (extends canonical d=3 methodology)")
    print(f"Backend: {'cupy (GPU)' if USING_GPU else 'numpy (CPU)'}")
    print(f"Canonical anti-collapse convention (sigma_init=0.5, normalized)")
    print(f"  extended to d=2; distinct from dimensional-rescaling series convention")

    d = 2
    N = 128
    L = 20.0
    Lambda = -8.0
    T_bath = 0.001
    n_steps = 2000

    SIGMA_LAMBDA_VALUES = [0.05, 0.1, 0.5, 1.0, 2.0]
    GAMMA_0_VALUES = [0.01, 0.05, 0.2, 1.0]

    # Compute and print initial peak for this d
    psi_init = initial_gaussian_normalized_2d(N, L, 0.5)
    initial_peak_d2 = float(xp.max(xp.abs(psi_init) ** 2))
    initial_norm_d2 = float(xp.sum(xp.abs(psi_init) ** 2) * (L / N) ** 2)
    print(f"\nInitial state (d={d}, sigma_init=0.5, normalized):")
    print(f"  initial_peak |Psi|^2 = {initial_peak_d2:.6f}")
    print(f"  initial_norm = {initial_norm_d2:.6f}")

    print(f"\nConfiguration:")
    print(f"  d = {d}, N = {N} ({N**d:,} voxels), L = {L}, Lambda = {Lambda}, T_bath = {T_bath}")
    print(f"  sigma_init = 0.5 normalized to total norm 1 (2D L2 norm)")
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
                               seed=42 + int(sl * 100) + int(g0 * 100))
            grid.append(r)
            print(f"  Sl={sl:>5.3f}, g0={g0:>5.2f}: regime={r['regime']:>14s}  "
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
        print(f"  Sl={sl:>5.3f}  ", end="")
        for g0 in GAMMA_0_VALUES:
            point = next(r for r in grid if r["Sigma_lambda"] == sl and r["gamma_0"] == g0)
            print(f"{point['regime']:>18s}", end="")
        print()

    summary = {
        "prediction_tested": "Phase diagram 2D slice at d=2 for open-problems/02",
        "convention_note": (
            "Canonical anti-collapse convention (sigma_init=0.5 normalized to "
            "total norm 1) extended to d=2. Distinct from the dimensional-"
            "rescaling series convention (sigma=0.4 non-normalized) used in "
            "results/10/15/24."
        ),
        "config": {
            "d": d, "N": N, "L": L, "Lambda": Lambda, "T_bath": T_bath,
            "n_steps": n_steps, "dt": 0.0025,
            "nu_fast": 10.0, "nu_slow": 0.5,
            "sigma_init": 0.5, "normalized": True,
            "initial_peak": initial_peak_d2,
            "initial_norm": initial_norm_d2,
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
