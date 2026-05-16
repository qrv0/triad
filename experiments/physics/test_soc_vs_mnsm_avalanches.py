"""Wave-2 test: SOC sandpile vs MNSM release-regime avalanche statistics,
with both substrates having explicit drive-and-dissipation (P3 active).

Targets prediction P14.2 (interface 14 SOC), redesigned to respect P3
per the post-retraction methodology.

Wave 1 was retracted (commit c11666b) for using gamma_0=0, T=0 on the
MNSM portion and ad-hoc perturbations instead of FDT-coupled drive.
methodology/02 identifies isolation as the abstraction the work argues
against. This wave-2 redesign uses:

  - BTW sandpile: standard drive-and-dissipate (always was).
  - MNSM 2D: FDT-locked stochastic forcing (gamma_0>0, T>0) replaces the
    ad-hoc periodic perturbations. The drive is now continuous (every step)
    and structurally matched to the equation's P3 instantiation.

Both substrates now have matched drive-and-dissipate structure for a
fair comparison.

Backend: CuPy on GPU. Wall time: a few minutes.

Output: outputs/soc_vs_mnsm_avalanches_p3/
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
OUTPUT_DIR = REPO_ROOT / "outputs" / "soc_vs_mnsm_avalanches_p3"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def to_cpu(arr):
    if hasattr(arr, "get"):
        return arr.get()
    return arr


# === BTW SANDPILE (unchanged from wave 1) ===

def btw_sandpile(N: int, n_drives: int, threshold: int = 4, seed: int = 42) -> dict:
    rng = np.random.default_rng(seed)
    H = np.zeros((N, N), dtype=np.int32)
    sizes = []

    print(f"  BTW: N={N}, drives={n_drives}, threshold={threshold}")
    t0 = time.time()
    for drive in range(n_drives):
        i, j = rng.integers(0, N, size=2)
        H[i, j] += 1
        size = 0
        while True:
            unstable = np.argwhere(H >= threshold)
            if len(unstable) == 0:
                break
            for (ui, uj) in unstable:
                H[ui, uj] -= threshold
                if ui > 0: H[ui-1, uj] += 1
                if ui < N-1: H[ui+1, uj] += 1
                if uj > 0: H[ui, uj-1] += 1
                if uj < N-1: H[ui, uj+1] += 1
                size += 1
        if size > 0:
            sizes.append(size)
    wall = time.time() - t0
    print(f"  BTW done: {len(sizes)} avalanches in {wall:.1f}s")
    return {"sizes": sizes, "N": N, "n_drives": n_drives, "wall_time": wall}


# === MNSM 2D WITH FDT-LOCKED DRIVE (wave-2 redesigned) ===

def mnsm_2d_with_fdt(N: int, L: float, Lambda: float, Sigma_lambda: float,
                      gamma_0: float, T_bath: float,
                      nu_fast: float = 10.0, nu_slow: float = 0.5,
                      sigma_init: float = 0.4, dt: float = 0.005,
                      n_steps_warmup: int = 1000, n_steps_record: int = 5000,
                      avalanche_threshold: float = 0.05,
                      seed: int = 42) -> dict:
    """MNSM 2D released regime with FDT-locked stochastic forcing (P3 active).

    Replaces wave-1 ad-hoc periodic perturbations with continuous FDT-locked
    drive, matching the structure of P3 in the equation.
    """
    rng = np.random.default_rng(seed)

    coord = xp.linspace(-L / 2, L / 2, N, endpoint=False)
    xs, ys = xp.meshgrid(coord, coord, indexing="ij")
    psi = (1.0 / (sigma_init * float(np.sqrt(2 * np.pi)))) * xp.exp(-(xs**2 + ys**2) / (2 * sigma_init**2))
    psi = psi.astype(xp.complex64)

    k_axis = 2 * xp.pi * xp.fft.fftfreq(N, d=L / N)
    kx, ky = xp.meshgrid(k_axis, k_axis, indexing="ij")
    kinetic_phase = -1j * 0.5 * (kx ** 2 + ky ** 2)
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

    def step_strang(psi, y_fast, y_slow):
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
        # P3 dissipation + noise
        if gamma_0 > 0:
            psi = psi * dissipation_factor
        if noise_amp > 0:
            xi_re = xp.asarray(rng.standard_normal(psi.shape).astype(np.float32))
            xi_im = xp.asarray(rng.standard_normal(psi.shape).astype(np.float32))
            psi = psi + noise_amp * (xi_re + 1j * xi_im) / float(np.sqrt(2.0))
        return psi, y_fast, y_slow

    print(f"  MNSM: N={N}, Lambda={Lambda}, Sigma_lambda={Sigma_lambda}, gamma_0={gamma_0}, T={T_bath}")
    print(f"  Warmup {n_steps_warmup} steps...")
    t0 = time.time()
    for step in range(n_steps_warmup):
        psi, y_fast, y_slow = step_strang(psi, y_fast, y_slow)

    print(f"  Recording {n_steps_record} steps...")
    peak_trace = np.zeros(n_steps_record, dtype=np.float32)
    for step in range(n_steps_record):
        rho = (psi.real ** 2 + psi.imag ** 2)
        peak_trace[step] = float(xp.max(rho))
        psi, y_fast, y_slow = step_strang(psi, y_fast, y_slow)

    wall = time.time() - t0

    # Avalanche detection: excursions above threshold
    median_peak = float(np.median(peak_trace))
    threshold_level = median_peak * (1 + avalanche_threshold)
    above = peak_trace > threshold_level

    sizes = []
    in_event = False
    event_size = 0.0
    for i in range(len(above)):
        if above[i]:
            if not in_event:
                in_event = True
                event_size = 0.0
            event_size += peak_trace[i] - threshold_level
        else:
            if in_event:
                if event_size > 0:
                    sizes.append(event_size)
                in_event = False
    if in_event and event_size > 0:
        sizes.append(event_size)

    print(f"  MNSM done: {len(sizes)} avalanches in {wall:.1f}s")
    print(f"  median peak={median_peak:.4f}, threshold={threshold_level:.4f}")

    return {"sizes": sizes, "median_peak": median_peak, "threshold_level": threshold_level,
            "peak_trace": peak_trace, "wall_time": wall,
            "gamma_0": gamma_0, "T_bath": T_bath}


def fit_power_law_exponent(sizes: list, x_min: float = None) -> dict:
    sizes = np.asarray(sizes, dtype=np.float64)
    if x_min is None:
        x_min = max(np.min(sizes), 1.0)
    above = sizes[sizes >= x_min]
    if len(above) < 10:
        return {"tau": None, "n": int(len(above)), "x_min": float(x_min),
                "reason": "too few samples"}
    log_ratios = np.log(above / x_min)
    tau = 1.0 + len(above) / log_ratios.sum()
    return {"tau": float(tau), "n": int(len(above)), "x_min": float(x_min)}


def main():
    print(f"Wave 2 Test E: SOC vs MNSM avalanche statistics with FDT-coupled MNSM (P14.2)")
    print(f"Backend: {'cupy (GPU)' if USING_GPU else 'numpy (CPU)'}")

    t_total = time.time()

    btw_result = btw_sandpile(N=64, n_drives=15000, threshold=4, seed=42)
    btw_sizes = btw_result["sizes"]
    btw_fit = fit_power_law_exponent(btw_sizes, x_min=4)

    # MNSM with multiple gamma_0 values to compare across P3 strengths
    mnsm_results = []
    for gamma_0 in [0.0, 0.05, 0.2]:
        mr = mnsm_2d_with_fdt(N=64, L=10.0, Lambda=-8.0, Sigma_lambda=2.0,
                               gamma_0=gamma_0, T_bath=0.05, seed=42)
        mr_fit = fit_power_law_exponent(mr["sizes"], x_min=0.001)
        mnsm_results.append({**mr, "fit": mr_fit, "n_avalanches": len(mr["sizes"])})

    t_total = time.time() - t_total
    print(f"\nTotal wall time: {t_total:.1f}s")

    print("\n=== Avalanche statistics comparison ===")
    print(f"  BTW (reference): {len(btw_sizes)} avalanches; tau = {btw_fit.get('tau', 'NA'):.3f}")
    print(f"  Literature reference for BTW 2D: tau ~ 1.0 to 1.2")
    print()
    for mr in mnsm_results:
        print(f"  MNSM gamma_0={mr['gamma_0']:.2f}: {mr['n_avalanches']} avalanches; "
              f"tau = {mr['fit'].get('tau', 'NA')}")

    summary = {
        "prediction": "P14.2 (interface 14), wave 2 with FDT-coupled MNSM",
        "btw": {"n_avalanches": int(len(btw_sizes)), "fit": btw_fit,
                 "wall_time": float(btw_result["wall_time"]),
                 "size_min": int(min(btw_sizes)) if btw_sizes else None,
                 "size_max": int(max(btw_sizes)) if btw_sizes else None,
                 "size_mean": float(np.mean(btw_sizes)) if btw_sizes else None},
        "mnsm_runs": [
            {
                "gamma_0": float(mr["gamma_0"]),
                "T_bath": float(mr["T_bath"]),
                "n_avalanches": int(mr["n_avalanches"]),
                "fit": mr["fit"],
                "median_peak": float(mr["median_peak"]),
                "threshold_level": float(mr["threshold_level"]),
                "wall_time": float(mr["wall_time"]),
            }
            for mr in mnsm_results
        ],
        "wall_time_total_s": float(t_total),
        "backend": "cupy" if USING_GPU else "numpy",
    }
    with open(OUTPUT_DIR / "summary.json", "w") as f:
        json.dump(summary, f, indent=2)
    print(f"\nFull data: {OUTPUT_DIR}/summary.json")


if __name__ == "__main__":
    main()
