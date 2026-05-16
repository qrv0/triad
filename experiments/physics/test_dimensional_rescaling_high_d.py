"""Test the dimensional-rescaling scaling Sigma_lambda/|Lambda| in d=4 and d=5.

Extends results/06-dimensional-rescaling.md from 2D and 3D to 4D and 5D.

The 2D/3D result established that the total memory coupling Sigma_lambda
required to release supercritical collapse scales with spatial dimension:

    Sigma_lambda / |Lambda| ~ factor that grows by ~10 per dimension

Empirically:
    d = 2:  Sigma_lambda / |Lambda| ~ 0.05  (i.e., Sigma_lambda ~ 0.4 at |Lambda|=8)
    d = 3:  Sigma_lambda / |Lambda| ~ 0.5   (Sigma_lambda ~ 4 at |Lambda|=8)

For d = 4 and d = 5, the structural argument predicts continuing growth of
the required coupling, with the next-power scaling either:
    1/d:        Sigma_lambda / |Lambda| ~ 1/d (boxed formula in results/06)
    factor-10:  Sigma_lambda / |Lambda| ~ 10^(d-1) (geometric argument)

These differ at d=4: 1/d predicts ratio ~0.25 (Sigma_lambda ~ 2), while
factor-10 predicts ratio ~5 (Sigma_lambda ~ 40). The test discriminates
between them by finding the critical Sigma_lambda at d=4 and d=5.

Method: minimal nD anti-collapse solver (Strang split-step, FFT-based
kinetic, local cubic + memory potential, no spinor for simplicity).
Reduced grid sizes to fit on consumer CPU memory:
    d=4:  N = 32^4 = 1.05M voxels per complex field
    d=5:  N = 16^5 = 1.05M voxels per complex field

Backend: numpy (CPU). Wall time: ~5-15 minutes total.

This test does not duplicate any existing experiment; the existing solver
in implementation/physics/solver_3d.py is hardcoded for 3D.
"""

from __future__ import annotations
import json
import time
from pathlib import Path

import numpy as np

# GPU acceleration: use CuPy if available; fall back to NumPy.
try:
    import cupy as cp
    xp = cp
    USING_GPU = True
    print("Backend: cupy (GPU)")
except ImportError:
    xp = np
    USING_GPU = False
    print("Backend: numpy (CPU) — install cupy-cuda12x for GPU acceleration")


REPO_ROOT = Path(__file__).parent.parent.parent
OUTPUT_DIR = REPO_ROOT / "outputs" / "dimensional_rescaling_high_d"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def to_cpu(arr):
    """Move array to CPU regardless of backend."""
    if hasattr(arr, "get"):
        return arr.get()
    return arr


def fft_kinetic_kernel(N: int, L: float, d: int, hbar: float = 1.0, mass: float = 1.0):
    """Return the FFT-space kinetic kernel -i * hbar^2/(2m) * k^2 (exp applied with dt)."""
    k_axis = 2 * xp.pi * xp.fft.fftfreq(N, d=L / N)
    grids = xp.meshgrid(*[k_axis] * d, indexing="ij")
    k_squared = sum(g ** 2 for g in grids)
    return -1j * (hbar ** 2 / (2 * mass)) * k_squared


def initial_gaussian(N: int, L: float, d: int, sigma_init: float):
    """Concentrated Gaussian initial condition centered at the box center."""
    coord = xp.linspace(-L / 2, L / 2, N, endpoint=False)
    grids = xp.meshgrid(*[coord] * d, indexing="ij")
    r_squared = sum(g ** 2 for g in grids)
    psi = (1.0 / (sigma_init * float(xp.sqrt(xp.asarray(2 * xp.pi))))) ** (d / 2)
    psi = psi * xp.exp(-r_squared / (2 * sigma_init ** 2))
    return psi.astype(xp.complex64)


def run_anti_collapse(d: int, N: int, L: float, Lambda: float, Sigma_lambda: float,
                       nu_fast: float = 10.0, nu_slow: float = 0.5,
                       dt: float = 0.0025, n_steps: int = 4000,
                       sigma_init: float = 0.4) -> dict:
    """Run the anti-collapse experiment in d dimensions.

    Two-mode memory: lambda_fast = Sigma_lambda * 0.75, lambda_slow = Sigma_lambda * 0.25.

    Returns dict with max_peak, final_peak, final_norm, wall_time.
    """
    psi = initial_gaussian(N, L, d, sigma_init)
    kinetic_phase = fft_kinetic_kernel(N, L, d)
    propagator_half_step = xp.exp(kinetic_phase * dt / 2)

    # Memory auxiliary fields (two modes)
    if Sigma_lambda > 0:
        lambda_fast = Sigma_lambda * 0.75
        lambda_slow = Sigma_lambda * 0.25
        y_fast = xp.zeros_like(psi.real, dtype=xp.float32)
        y_slow = xp.zeros_like(psi.real, dtype=xp.float32)
        memory_active = True
        # Exact OU decay factors (paper §4.1: "exact, independent of dt")
        decay_fast = float(xp.exp(xp.asarray(-nu_fast * dt)))
        decay_slow = float(xp.exp(xp.asarray(-nu_slow * dt)))
        accum_fast = 1.0 - decay_fast
        accum_slow = 1.0 - decay_slow
    else:
        memory_active = False

    initial_norm = float(xp.sum(xp.abs(psi) ** 2) * (L / N) ** d)
    initial_peak = float(xp.max(xp.abs(psi) ** 2))

    peaks = [initial_peak]
    norms = [initial_norm]

    t0 = time.time()
    for step in range(n_steps):
        # V/2: nonlinear + memory potential half-step
        rho = (psi.real ** 2 + psi.imag ** 2).astype(xp.float32)
        if memory_active:
            V_mem = lambda_fast * y_fast + lambda_slow * y_slow
        else:
            V_mem = 0.0
        V_total = Lambda * rho + V_mem
        psi = psi * xp.exp(-1j * V_total * dt / 2)

        # K: kinetic full-step (FFT)
        psi_k = xp.fft.fftn(psi)
        psi_k = psi_k * propagator_half_step * propagator_half_step
        psi = xp.fft.ifftn(psi_k)

        # V/2: nonlinear + memory potential half-step
        rho = (psi.real ** 2 + psi.imag ** 2).astype(xp.float32)
        if memory_active:
            V_mem = lambda_fast * y_fast + lambda_slow * y_slow
        else:
            V_mem = 0.0
        V_total = Lambda * rho + V_mem
        psi = psi * xp.exp(-1j * V_total * dt / 2)

        # OU update for memory fields (Markovian embedding; exact per paper §4.1)
        if memory_active:
            y_fast = decay_fast * y_fast + accum_fast * rho
            y_slow = decay_slow * y_slow + accum_slow * rho

        # Sample peak occasionally
        if step % 50 == 0:
            cur_peak = float(xp.max(rho))
            cur_norm = float(xp.sum(rho) * (L / N) ** d)
            peaks.append(cur_peak)
            norms.append(cur_norm)

    wall = time.time() - t0
    return {
        "d": d,
        "N": N,
        "Lambda": Lambda,
        "Sigma_lambda": Sigma_lambda,
        "max_peak": float(max(peaks)),
        "final_peak": float(peaks[-1]),
        "initial_peak": initial_peak,
        "initial_norm": initial_norm,
        "final_norm": norms[-1],
        "norm_drift": abs(norms[-1] - initial_norm) / initial_norm,
        "wall_time": wall,
    }


def find_critical_sigma_lambda(d: int, N: int, L: float, Lambda: float,
                                sigma_lambda_values: list) -> dict:
    """Sweep Sigma_lambda and identify the threshold for anti-collapse.

    Anti-collapse criterion: final_peak < initial_peak * 10 (relaxed threshold;
    full release expected to lower final_peak below initial_peak).
    """
    sweep_results = []
    print(f"  d = {d}, N = {N}, |Lambda| = {abs(Lambda)}")
    print(f"  Sweep Sigma_lambda in {sigma_lambda_values}")

    for Sigma_lambda in sigma_lambda_values:
        result = run_anti_collapse(d, N, L, Lambda, Sigma_lambda)
        anti_collapse = result["final_peak"] < result["initial_peak"] * 10
        sweep_results.append({
            **result,
            "anti_collapse": anti_collapse,
        })
        print(f"    Sigma_lambda = {Sigma_lambda:>7.2f}: "
              f"max_peak = {result['max_peak']:>10.4f}, "
              f"final_peak = {result['final_peak']:>10.4f}, "
              f"anti_collapse = {anti_collapse}, "
              f"t = {result['wall_time']:.1f}s")

    # Critical Sigma_lambda: smallest value at which anti_collapse=True
    collapsed = [r for r in sweep_results if not r["anti_collapse"]]
    released = [r for r in sweep_results if r["anti_collapse"]]
    if released:
        critical = min(released, key=lambda r: r["Sigma_lambda"])
        ratio = critical["Sigma_lambda"] / abs(Lambda)
        return {
            "d": d,
            "Lambda": Lambda,
            "critical_Sigma_lambda": critical["Sigma_lambda"],
            "critical_ratio": ratio,
            "sweep_results": sweep_results,
        }
    return {
        "d": d,
        "Lambda": Lambda,
        "critical_Sigma_lambda": None,
        "critical_ratio": None,
        "sweep_results": sweep_results,
    }


def main():
    print("Phase 9 Test B: dimensional rescaling Sigma_lambda/|Lambda| at d=4 and d=5")
    print(f"Output: {OUTPUT_DIR}")

    # Parameters: matched to the 3D reference (|Lambda|=8, sigma_init=0.4 for higher concentration)
    Lambda = -8.0  # same magnitude as 3D reference (results/04)
    L = 10.0

    # Sweep specifications per dimension
    # d=4: predicted ratio range 0.25 (1/d formula) to ~5 (factor-10 from 3D's 0.5)
    # d=5: predicted ratio range 0.20 (1/d) to ~50 (factor-10)
    # Range chosen to discriminate between the two scaling hypotheses

    # GPU enables larger grids — closer to the 3D reference resolution
    configs = [
        # d=4 at N=32 (1M voxels per field; ~50 MB total on GPU)
        {"d": 4, "N": 32, "Lambda": Lambda, "sigma_lambdas": [0.0, 0.5, 1.0, 2.0, 4.0, 8.0, 16.0, 40.0]},
        # d=5 at N=20 (3.2M voxels per field; ~150 MB total)
        {"d": 5, "N": 20, "Lambda": Lambda, "sigma_lambdas": [0.0, 1.0, 2.0, 5.0, 10.0, 25.0, 50.0, 100.0]},
    ]

    t_total = time.time()
    all_results = []
    for cfg in configs:
        print(f"\n--- Dimensional rescaling: d = {cfg['d']} ---")
        result = find_critical_sigma_lambda(
            d=cfg["d"],
            N=cfg["N"],
            L=L,
            Lambda=cfg["Lambda"],
            sigma_lambda_values=cfg["sigma_lambdas"],
        )
        all_results.append(result)
    t_total = time.time() - t_total

    print(f"\nTotal wall time: {t_total:.1f}s")

    print("\n=== Critical Sigma_lambda/|Lambda| by dimension ===")
    # Known values from results/06
    known = {
        2: {"critical_ratio": 0.05},
        3: {"critical_ratio": 0.5},
    }
    print(f"  d = 2 (results/06):  Sigma_lambda/|Lambda| ~ {known[2]['critical_ratio']}")
    print(f"  d = 3 (results/06):  Sigma_lambda/|Lambda| ~ {known[3]['critical_ratio']}")
    for r in all_results:
        if r["critical_ratio"] is not None:
            print(f"  d = {r['d']} (this test): Sigma_lambda/|Lambda| ~ {r['critical_ratio']:.3f}")
        else:
            print(f"  d = {r['d']} (this test): no anti-collapse threshold found in sweep range")

    # Save full summary
    summary = {
        "prediction_tested": "Extension of results/06 dimensional rescaling to d=4, d=5",
        "test_parameters": {
            "Lambda": Lambda,
            "L": L,
            "configs": configs,
        },
        "known_from_results_06": known,
        "results": all_results,
        "wall_time_total_s": t_total,
    }
    with open(OUTPUT_DIR / "summary.json", "w") as f:
        json.dump(summary, f, indent=2)
    print(f"\nFull summary written to {OUTPUT_DIR}/summary.json")


if __name__ == "__main__":
    main()
