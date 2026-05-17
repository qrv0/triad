"""Test: dimensional rescaling at d=6 with FDT-locked field noise (P3 active).

Extends results/10-dimensional-rescaling-higher-d.md (d=4, d=5) to one more
dimension. The existing data show a non-monotonic pattern: d=2 ratio ~0.05,
d=3 ratio ~0.5, d=4 ratio ~0.125, d=5 ratio that does not follow the boxed
1/d formula in results/06. Adding d=6 either continues the non-monotonic
trend or stabilizes the scaling.

Equation simulated (full triangle, identical to test_dimensional_rescaling_high_d.py):
    i d_t psi = [-1/2 D^2 + Lambda |psi|^2 + V_mem - i gamma_0] psi + eta
    d_t y_j = nu_j (rho - y_j)
    <eta(t,x) eta*(t',x')> = 2 gamma_0 T delta(t-t') delta^(d)(x-x')

Strang splitting identical to the d=4,5 test, so the comparison is clean.

Sweep: small focused gamma_0 (one value, 0.2) x Sigma_lambda at d=6.
gamma_0=0.2 was the value at which the existing tests showed clean
ratio-independence at fixed d (per results/15).

Backend: CuPy (GPU). N=8 keeps voxels per field at 8^6 = 262,144,
comparable to d=5 at N=12.

Output: outputs/dimensional_rescaling_d6_p3/
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
OUTPUT_DIR = REPO_ROOT / "outputs" / "dimensional_rescaling_d6_p3"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def to_cpu(arr):
    if hasattr(arr, "get"):
        return arr.get()
    return arr


def fft_kinetic_propagator(N: int, L: float, dt: float, gamma_0: float, d: int,
                           hbar: float = 1.0, mass: float = 1.0):
    """Canonical kinetic propagator U_k with dissipation folded in.

    Matches implementation/physics/solver_3d.py build_kinetic_propagator:
    H_complex = (hbar^2/2m) k^2 - i gamma_0, U_k = exp(-i H_complex dt).
    """
    k_axis = 2 * xp.pi * xp.fft.fftfreq(N, d=L / N)
    grids = xp.meshgrid(*[k_axis] * d, indexing="ij")
    k_squared = sum(g ** 2 for g in grids)
    H_kin = (hbar ** 2 / (2 * mass)) * k_squared
    H_complex = H_kin.astype(xp.complex64) - 1j * gamma_0
    return xp.exp(-1j * H_complex * dt).astype(xp.complex64)


def initial_gaussian(N: int, L: float, d: int, sigma_init: float):
    coord = xp.linspace(-L / 2, L / 2, N, endpoint=False)
    grids = xp.meshgrid(*[coord] * d, indexing="ij")
    r_squared = sum(g ** 2 for g in grids)
    psi = (1.0 / (sigma_init * float(np.sqrt(2 * np.pi)))) ** (d / 2)
    psi = psi * xp.exp(-r_squared / (2 * sigma_init ** 2))
    return psi.astype(xp.complex64)


def run_anti_collapse_p3(d: int, N: int, L: float, Lambda: float, Sigma_lambda: float,
                          gamma_0: float, T_bath: float,
                          nu_fast: float = 10.0, nu_slow: float = 0.5,
                          dt: float = 0.0025, n_steps: int = 4000,
                          sigma_init: float = 0.4, seed: int = 42) -> dict:
    """nD anti-collapse with full P1+P2+P3 triangle active (identical to high_d test)."""
    rng = np.random.default_rng(seed)
    psi = initial_gaussian(N, L, d, sigma_init)
    propagator_full = fft_kinetic_propagator(N, L, dt, gamma_0, d)

    if Sigma_lambda > 0:
        lambda_fast = Sigma_lambda * 0.75
        lambda_slow = Sigma_lambda * 0.25
        y_fast = xp.zeros_like(psi.real, dtype=xp.float32)
        y_slow = xp.zeros_like(psi.real, dtype=xp.float32)
        memory_active = True
        decay_fast = float(np.exp(-nu_fast * dt))
        decay_slow = float(np.exp(-nu_slow * dt))
        accum_fast = 1.0 - decay_fast
        accum_slow = 1.0 - decay_slow
    else:
        memory_active = False

    noise_amp = float(np.sqrt(2.0 * gamma_0 * T_bath * dt))

    initial_norm = float(xp.sum(xp.abs(psi) ** 2) * (L / N) ** d)
    initial_peak = float(xp.max(xp.abs(psi) ** 2))
    peaks = [initial_peak]
    norms = [initial_norm]

    t0 = time.time()
    for step in range(n_steps):
        rho = (psi.real ** 2 + psi.imag ** 2).astype(xp.float32)
        V_mem = (lambda_fast * y_fast + lambda_slow * y_slow) if memory_active else 0.0
        V_total = Lambda * rho + V_mem
        psi = psi * xp.exp(-1j * V_total * dt / 2)

        psi = xp.fft.ifftn(xp.fft.fftn(psi) * propagator_full)

        rho = (psi.real ** 2 + psi.imag ** 2).astype(xp.float32)
        V_mem = (lambda_fast * y_fast + lambda_slow * y_slow) if memory_active else 0.0
        V_total = Lambda * rho + V_mem
        psi = psi * xp.exp(-1j * V_total * dt / 2)

        if memory_active:
            y_fast = decay_fast * y_fast + accum_fast * rho
            y_slow = decay_slow * y_slow + accum_slow * rho


        if noise_amp > 0:
            shape = psi.shape
            xi_re = xp.asarray(rng.standard_normal(shape).astype(np.float32))
            xi_im = xp.asarray(rng.standard_normal(shape).astype(np.float32))
            psi = psi + noise_amp * (xi_re + 1j * xi_im) / float(np.sqrt(2.0))

        if step % 100 == 0:
            cur_peak = float(xp.max((psi.real ** 2 + psi.imag ** 2)))
            cur_norm = float(xp.sum((psi.real ** 2 + psi.imag ** 2)) * (L / N) ** d)
            peaks.append(cur_peak)
            norms.append(cur_norm)

    wall = time.time() - t0
    return {
        "d": d, "N": N, "Lambda": Lambda, "Sigma_lambda": Sigma_lambda,
        "gamma_0": gamma_0, "T_bath": T_bath,
        "max_peak": float(max(peaks)),
        "final_peak": float(peaks[-1]),
        "initial_peak": initial_peak,
        "initial_norm": initial_norm,
        "final_norm": norms[-1],
        "wall_time": wall,
    }


def main():
    print(f"Test: dimensional rescaling at d=6 (P3 active)")
    print(f"Backend: {'cupy (GPU)' if USING_GPU else 'numpy (CPU)'}")

    Lambda = -8.0
    L = 10.0
    T_bath = 0.05
    gamma_0 = 0.2  # Fixed at the value used in the d=4,5 sweep

    # d=6 voxel budget: 8^6 = 262,144 (cf. d=5 at N=12 = 248,832)
    d = 6
    N = 8

    # Coverage: span both candidate scaling predictions
    # 1/d formula: ratio ~0.167 at d=6 (Sigma_lambda ~1.33)
    # Linear extrapolation from d=2,3,4,5 data is hard given non-monotonicity
    # Sample broadly to capture the critical value
    SIGMA_LAMBDA_VALUES = [0.0, 0.5, 1.0, 2.0, 4.0, 8.0, 16.0, 32.0]

    print(f"d = {d}, N = {N}, voxels per field = {N**d:,}")
    print(f"|Lambda| = {abs(Lambda)}, gamma_0 = {gamma_0}, T_bath = {T_bath}")
    print(f"Sigma_lambda sweep: {SIGMA_LAMBDA_VALUES}")
    print()

    t_total = time.time()
    results = []
    for Sigma_lambda in SIGMA_LAMBDA_VALUES:
        r = run_anti_collapse_p3(
            d=d, N=N, L=L, Lambda=Lambda, Sigma_lambda=Sigma_lambda,
            gamma_0=gamma_0, T_bath=T_bath,
            seed=42 + d * 100 + int(Sigma_lambda * 10) + int(gamma_0 * 100),
        )
        ratio = r["final_peak"] / max(r["initial_peak"], 1e-10)
        released = ratio < 1.0
        results.append({**r, "ratio_final_initial": ratio, "released": released})
        print(f"  Sigma_lambda={Sigma_lambda:>6.2f}: "
              f"max_peak={r['max_peak']:>12.4f}  "
              f"final/initial={ratio:>10.4f}  "
              f"released={released}  "
              f"t={r['wall_time']:.1f}s")

    t_total = time.time() - t_total
    print(f"\nTotal wall time: {t_total:.1f}s")

    released = [r for r in results if r["released"] and r["Sigma_lambda"] > 0]
    critical_Sigma_lambda = None
    critical_ratio = None
    if released:
        critical = min(released, key=lambda r: r["Sigma_lambda"])
        critical_Sigma_lambda = critical["Sigma_lambda"]
        critical_ratio = critical["Sigma_lambda"] / abs(Lambda)
        print(f"\nCritical Sigma_lambda at d=6, gamma_0={gamma_0}: {critical_Sigma_lambda}")
        print(f"Critical Sigma_lambda / |Lambda|: {critical_ratio:.3f}")
    else:
        print(f"\nNo released configuration found in sweep; critical Sigma_lambda > {max(SIGMA_LAMBDA_VALUES)}")

    print(f"\nFor reference (existing data):")
    print(f"  d=2 ratio ~0.05; d=3 ratio ~0.5; d=4 ratio ~0.125; d=5 not on boxed 1/d formula")
    print(f"  1/d formula at d=6: predicts ratio ~0.167 (Sigma_lambda ~1.33)")

    summary = {
        "prediction_tested": "Extension to d=6 of dimensional rescaling per results/06,10,15",
        "config": {"d": d, "N": N, "L": L, "Lambda": Lambda, "gamma_0": gamma_0, "T_bath": T_bath},
        "sigma_lambda_sweep": SIGMA_LAMBDA_VALUES,
        "results": [{k: v for k, v in r.items() if k not in ("peaks", "norms")} for r in results],
        "critical_Sigma_lambda": critical_Sigma_lambda,
        "critical_ratio": critical_ratio,
        "wall_time_total_s": t_total,
        "backend": "cupy" if USING_GPU else "numpy",
    }
    with open(OUTPUT_DIR / "summary.json", "w") as f:
        json.dump(summary, f, indent=2)
    print(f"\nSummary written to {OUTPUT_DIR}/summary.json")


if __name__ == "__main__":
    main()
