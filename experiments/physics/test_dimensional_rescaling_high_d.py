"""Wave-2 test: dimensional rescaling Sigma_lambda/|Lambda| at d=4 and d=5
with FDT-locked field noise (P3 active).

Wave 1 was retracted (commit c11666b) for testing the P1+P2 degenerate
sub-system (gamma_0=0, T=0). This wave-2 redesign activates P3 via the
Strang split-step's dissipation and stochastic forcing steps (paper §4.1
sub-steps 4 and 5), respecting the FDT correlator stated in P3.

Equation simulated (full triangle):
    i d_t psi = [-1/2 D^2 + Lambda |psi|^2 + V_mem - i gamma_0] psi + eta
    d_t y_j = nu_j (rho - y_j)         (exact OU update, paper §4.1)
    <eta(t,x) eta*(t',x')> = 2 gamma_0 T delta(t-t') delta^(d)(x-x')

Each step (Strang splitting):
    1. V/2:   psi <- exp(-i V_tot dt/2) psi
    2. K:     psi <- IFFT[exp(-i k^2/2 dt) FFT[psi]]
    3. V/2:   psi <- exp(-i V_tot dt/2) psi
    4. OU:    y_j <- exp(-nu_j dt) y_j + (1 - exp(-nu_j dt)) rho
    5. Diss:  psi <- exp(-gamma_0 dt) psi
    6. Noise: psi <- psi + sqrt(2 gamma_0 T dt) xi    (xi: complex Gaussian)

Sweep: Sigma_lambda x gamma_0 at d=4 and d=5. Identifies whether the
dimensional rescaling Sigma_lambda_crit/|Lambda| (results/06) depends on
the bath coupling (it should not if the scaling is purely structural;
if it does, the result reveals a coupling-structural connection).

Backend: CuPy (GPU). Wall time: a few minutes on RTX 4060.

Output: outputs/dimensional_rescaling_high_d_p3/
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
OUTPUT_DIR = REPO_ROOT / "outputs" / "dimensional_rescaling_high_d_p3"
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
    """nD anti-collapse with full P1+P2+P3 triangle active.

    Returns dict with max_peak, final_peak, final_norm, wall_time.
    """
    rng = np.random.default_rng(seed)
    psi = initial_gaussian(N, L, d, sigma_init)
    propagator_full = fft_kinetic_propagator(N, L, dt, gamma_0, d)

    # Memory fields
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

    # P3 dissipation factor
    # FDT noise amplitude per voxel per timestep
    noise_amp = float(np.sqrt(2.0 * gamma_0 * T_bath * dt))

    initial_norm = float(xp.sum(xp.abs(psi) ** 2) * (L / N) ** d)
    initial_peak = float(xp.max(xp.abs(psi) ** 2))
    peaks = [initial_peak]
    norms = [initial_norm]

    t0 = time.time()
    for step in range(n_steps):
        # V/2
        rho = (psi.real ** 2 + psi.imag ** 2).astype(xp.float32)
        V_mem = (lambda_fast * y_fast + lambda_slow * y_slow) if memory_active else 0.0
        V_total = Lambda * rho + V_mem
        psi = psi * xp.exp(-1j * V_total * dt / 2)

        # K (full kinetic step)
        psi = xp.fft.ifftn(xp.fft.fftn(psi) * propagator_full)

        # V/2
        rho = (psi.real ** 2 + psi.imag ** 2).astype(xp.float32)
        V_mem = (lambda_fast * y_fast + lambda_slow * y_slow) if memory_active else 0.0
        V_total = Lambda * rho + V_mem
        psi = psi * xp.exp(-1j * V_total * dt / 2)

        # OU update (exact)
        if memory_active:
            y_fast = decay_fast * y_fast + accum_fast * rho
            y_slow = decay_slow * y_slow + accum_slow * rho

        # P3 dissipation

        # P3 noise (FDT-locked)
        if noise_amp > 0:
            shape = psi.shape
            # Generate complex Gaussian noise: real and imag parts each unit-variance
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
    print(f"Wave 2 Test B: nD dimensional rescaling with FDT-locked field noise (P3 active)")
    print(f"Backend: {'cupy (GPU)' if USING_GPU else 'numpy (CPU)'}")

    Lambda = -8.0
    L = 10.0
    T_bath = 0.05  # bath temperature

    # Sweep Sigma_lambda x gamma_0 at d=4 and d=5.
    # gamma_0 spans small positive (weak coupling) to moderate coupling; the
    # isolated regime (gamma_0 = 0) is excluded per principles/03-coupling.md
    # (Rule A in the structural-research-mode skill).
    GAMMA_0_VALUES = [0.05, 0.2, 1.0]  # P3 sweep
    # Sigma_lambda spans both candidate scaling predictions:
    # 1/d formula: ratio ~0.25 at d=4 (Sigma_lambda ~2); ~0.20 at d=5
    # factor-10 formula: ratio ~5 at d=4 (Sigma_lambda ~40); ~50 at d=5
    SIGMA_LAMBDA_VALUES_4D = [0.0, 1.0, 2.0, 4.0, 8.0, 16.0, 40.0]
    SIGMA_LAMBDA_VALUES_5D = [0.0, 2.0, 5.0, 10.0, 25.0, 50.0]

    configs = [
        {"d": 4, "N": 24, "sigma_lambdas": SIGMA_LAMBDA_VALUES_4D},
        {"d": 5, "N": 12, "sigma_lambdas": SIGMA_LAMBDA_VALUES_5D},
    ]

    print(f"|Lambda| = {abs(Lambda)}, T_bath = {T_bath}")
    print(f"P3 sweep: gamma_0 = {GAMMA_0_VALUES}")

    t_total = time.time()
    all_results = []
    for cfg in configs:
        d = cfg["d"]
        N = cfg["N"]
        print(f"\n--- d = {d}, N = {N}, voxels per field = {N**d:,} ---")

        d_results = []
        for gamma_0 in GAMMA_0_VALUES:
            print(f"\n  gamma_0 = {gamma_0}")
            for Sigma_lambda in cfg["sigma_lambdas"]:
                r = run_anti_collapse_p3(
                    d=d, N=N, L=L, Lambda=Lambda, Sigma_lambda=Sigma_lambda,
                    gamma_0=gamma_0, T_bath=T_bath,
                    seed=42 + d * 100 + int(Sigma_lambda * 10) + int(gamma_0 * 100),
                )
                # Anti-collapse criterion: final_peak well below initial_peak (released)
                ratio = r["final_peak"] / max(r["initial_peak"], 1e-10)
                released = ratio < 1.0
                d_results.append({
                    **r,
                    "ratio_final_initial": ratio,
                    "released": released,
                })
                print(f"    Sigma_lambda={Sigma_lambda:>6.2f}: "
                      f"max_peak={r['max_peak']:>10.4f}  "
                      f"final/initial={ratio:>8.4f}  "
                      f"released={released}  "
                      f"t={r['wall_time']:.1f}s")

        # Identify critical Sigma_lambda at each gamma_0
        for gamma_0 in GAMMA_0_VALUES:
            this_gamma = [r for r in d_results if r["gamma_0"] == gamma_0]
            released = [r for r in this_gamma if r["released"] and r["Sigma_lambda"] > 0]
            if released:
                critical = min(released, key=lambda r: r["Sigma_lambda"])
                all_results.append({
                    "d": d, "gamma_0": gamma_0,
                    "critical_Sigma_lambda": critical["Sigma_lambda"],
                    "critical_ratio": critical["Sigma_lambda"] / abs(Lambda),
                })

    t_total = time.time() - t_total
    print(f"\nTotal wall time: {t_total:.1f}s")

    print(f"\n=== Critical Sigma_lambda/|Lambda| vs (d, gamma_0) ===")
    print(f"  Known from results/06: d=2 ratio ~0.05, d=3 ratio ~0.5")
    for r in all_results:
        print(f"  d={r['d']}, gamma_0={r['gamma_0']:.2f}: "
              f"Sigma_lambda_crit/|Lambda| ~ {r['critical_ratio']:.3f}")

    summary = {
        "prediction_tested": "Extension of results/06 dimensional rescaling, P3 active, d=4, d=5",
        "parameters": {"Lambda": Lambda, "L": L, "T_bath": T_bath,
                       "gamma_0_values": GAMMA_0_VALUES, "configs": configs},
        "critical_thresholds": all_results,
        "wall_time_total_s": t_total,
        "backend": "cupy" if USING_GPU else "numpy",
    }
    with open(OUTPUT_DIR / "summary.json", "w") as f:
        json.dump(summary, f, indent=2)
    print(f"\nFull data: {OUTPUT_DIR}/summary.json")


if __name__ == "__main__":
    main()
