"""WAVE 1 RETRACTED 2026-05-16: this script has the MNSM portion in the
isolated regime (gamma_0=0, T=0); the perturbations are ad-hoc rather than
FDT-coupled drive. Per methodology/02-limits-of-falsification.md, isolation
is the abstraction the work argues against. DO NOT RUN.
See ../../results/13-soc-vs-mnsm-avalanches.md retraction note for context.
A wave-2 redesigned version with both substrates having explicit
drive-and-dissipation (FDT-locked for MNSM, matched in structure to BTW)
is required for any methodologically valid test of P14.2.

Test prediction P14.2 (interface 14 SOC).

Prediction: the equation's release transition, when simulated with appropriate
parameters, should produce avalanche-size distributions statistically
indistinguishable from BTW sandpile distributions at matching substrate
parameters.

Method: simulate BTW sandpile on a 2D grid (standard reference SOC model)
and the MNSM equation in 2D in its released regime under periodic
perturbation; measure avalanche-size distributions in both; compare
exponents.

Both substrates are simulated at small scale (2D 64x64) on CPU using numpy.

Backend: numpy (CPU). Wall time: ~5-10 minutes.

Output: outputs/soc_vs_mnsm_avalanches/

This test does not duplicate any existing experiment.
"""

from __future__ import annotations
import json
import sys
import time
from pathlib import Path

import numpy as np


REPO_ROOT = Path(__file__).parent.parent.parent
OUTPUT_DIR = REPO_ROOT / "outputs" / "soc_vs_mnsm_avalanches"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


# === BTW SANDPILE ===

def btw_sandpile(N: int, n_drives: int, threshold: int = 4, seed: int = 42) -> dict:
    """Bak-Tang-Wiesenfeld sandpile on N x N grid.

    Boundary: dissipative (grains falling off the edge are lost).

    Drive: at each event, add 1 grain to a random cell.
    Relax: if any cell has H_i >= threshold, topple (subtract threshold,
    distribute 1 to each of 4 neighbors). Continue until no cell is unstable.
    Avalanche size = number of toppling events during one relaxation cycle.
    """
    rng = np.random.default_rng(seed)
    H = np.zeros((N, N), dtype=np.int32)
    sizes = []

    print(f"  BTW: N = {N}, drives = {n_drives}, threshold = {threshold}")
    t0 = time.time()
    for drive in range(n_drives):
        # Random drive
        i, j = rng.integers(0, N, size=2)
        H[i, j] += 1
        # Relax
        size = 0
        while True:
            unstable = np.argwhere(H >= threshold)
            if len(unstable) == 0:
                break
            for (ui, uj) in unstable:
                H[ui, uj] -= threshold
                # Distribute to 4 neighbors (with dissipative boundary)
                if ui > 0:
                    H[ui - 1, uj] += 1
                if ui < N - 1:
                    H[ui + 1, uj] += 1
                if uj > 0:
                    H[ui, uj - 1] += 1
                if uj < N - 1:
                    H[ui, uj + 1] += 1
                size += 1
        if size > 0:
            sizes.append(size)
        if (drive + 1) % 2000 == 0:
            print(f"    {drive+1}/{n_drives} drives, {len(sizes)} avalanches so far")
    wall = time.time() - t0
    print(f"  BTW done: {len(sizes)} avalanches in {wall:.1f}s")
    return {"sizes": sizes, "N": N, "n_drives": n_drives, "threshold": threshold, "wall_time": wall}


# === MNSM 2D ===

def mnsm_2d_with_perturbations(N: int, L: float, Lambda: float, Sigma_lambda: float,
                                 nu_fast: float = 10.0, nu_slow: float = 0.5,
                                 sigma_init: float = 0.4, dt: float = 0.005,
                                 n_steps_warmup: int = 2000, n_steps_record: int = 8000,
                                 perturbation_period: int = 200,
                                 perturbation_amplitude: float = 0.01,
                                 avalanche_threshold: float = 0.05,
                                 seed: int = 42) -> dict:
    """MNSM 2D released regime with periodic perturbations.

    Steps:
    1. Initialize with a concentrated Gaussian, evolve under collapse+memory
       until released-crystalline regime is established (warmup).
    2. Record peak density trace.
    3. Periodically add small Gaussian perturbations at random locations.
    4. Identify "avalanche" events: continuous excursions of peak density
       above threshold (defined as fraction above the median peak).
    5. Compute avalanche size = total above-threshold area during the event.
    """
    rng = np.random.default_rng(seed)

    # Initial Gaussian
    coord = np.linspace(-L / 2, L / 2, N, endpoint=False)
    xs, ys = np.meshgrid(coord, coord, indexing="ij")
    psi = (1.0 / (sigma_init * np.sqrt(2 * np.pi))) * np.exp(-(xs ** 2 + ys ** 2) / (2 * sigma_init ** 2))
    psi = psi.astype(np.complex64)

    # FFT kinetic kernel
    k_axis = 2 * np.pi * np.fft.fftfreq(N, d=L / N)
    kx, ky = np.meshgrid(k_axis, k_axis, indexing="ij")
    kinetic_phase = -1j * 0.5 * (kx ** 2 + ky ** 2)
    propagator = np.exp(kinetic_phase * dt)

    # Memory fields
    lambda_fast = Sigma_lambda * 0.75
    lambda_slow = Sigma_lambda * 0.25
    y_fast = np.zeros_like(psi.real, dtype=np.float32)
    y_slow = np.zeros_like(psi.real, dtype=np.float32)
    decay_fast = np.exp(-nu_fast * dt)
    decay_slow = np.exp(-nu_slow * dt)
    accum_fast = 1.0 - decay_fast
    accum_slow = 1.0 - decay_slow

    # Warmup: let the field reach released-crystalline regime
    print(f"  MNSM: N = {N}, Lambda = {Lambda}, Sigma_lambda = {Sigma_lambda}")
    print(f"  Warmup {n_steps_warmup} steps...")
    t0 = time.time()
    for step in range(n_steps_warmup):
        rho = (psi.real ** 2 + psi.imag ** 2).astype(np.float32)
        V_mem = lambda_fast * y_fast + lambda_slow * y_slow
        V_total = Lambda * rho + V_mem
        psi = psi * np.exp(-1j * V_total * dt / 2)
        psi_k = np.fft.fftn(psi)
        psi_k = psi_k * propagator
        psi = np.fft.ifftn(psi_k)
        rho = (psi.real ** 2 + psi.imag ** 2).astype(np.float32)
        V_mem = lambda_fast * y_fast + lambda_slow * y_slow
        V_total = Lambda * rho + V_mem
        psi = psi * np.exp(-1j * V_total * dt / 2)
        y_fast = decay_fast * y_fast + accum_fast * rho
        y_slow = decay_slow * y_slow + accum_slow * rho

    # Record + perturbation phase
    print(f"  Recording {n_steps_record} steps with perturbations every {perturbation_period}...")
    peak_trace = np.zeros(n_steps_record, dtype=np.float32)
    for step in range(n_steps_record):
        rho = (psi.real ** 2 + psi.imag ** 2).astype(np.float32)
        peak_trace[step] = float(np.max(rho))

        # Apply perturbation periodically
        if step % perturbation_period == 0 and step > 0:
            # Add small Gaussian perturbation at random location
            ci, cj = rng.integers(0, N, size=2)
            i_idx, j_idx = np.meshgrid(np.arange(N), np.arange(N), indexing="ij")
            di = np.minimum(np.abs(i_idx - ci), N - np.abs(i_idx - ci))
            dj = np.minimum(np.abs(j_idx - cj), N - np.abs(j_idx - cj))
            r2 = (di ** 2 + dj ** 2).astype(np.float32)
            pert = perturbation_amplitude * np.exp(-r2 / 8.0)
            psi = psi + pert.astype(np.complex64)

        V_mem = lambda_fast * y_fast + lambda_slow * y_slow
        V_total = Lambda * rho + V_mem
        psi = psi * np.exp(-1j * V_total * dt / 2)
        psi_k = np.fft.fftn(psi)
        psi_k = psi_k * propagator
        psi = np.fft.ifftn(psi_k)
        rho = (psi.real ** 2 + psi.imag ** 2).astype(np.float32)
        V_mem = lambda_fast * y_fast + lambda_slow * y_slow
        V_total = Lambda * rho + V_mem
        psi = psi * np.exp(-1j * V_total * dt / 2)
        y_fast = decay_fast * y_fast + accum_fast * rho
        y_slow = decay_slow * y_slow + accum_slow * rho

    wall = time.time() - t0

    # Avalanche detection: excursions above threshold
    median_peak = float(np.median(peak_trace))
    threshold_level = median_peak * (1 + avalanche_threshold)
    above = peak_trace > threshold_level

    # Identify contiguous runs above threshold
    sizes = []
    in_event = False
    event_size = 0.0
    for i in range(len(above)):
        if above[i]:
            if not in_event:
                in_event = True
                event_size = 0.0
            event_size += (peak_trace[i] - threshold_level)
        else:
            if in_event:
                if event_size > 0:
                    sizes.append(event_size)
                in_event = False
    if in_event and event_size > 0:
        sizes.append(event_size)

    print(f"  MNSM done: {len(sizes)} avalanches in {wall:.1f}s")
    print(f"  median peak = {median_peak:.4f}, threshold = {threshold_level:.4f}")

    return {
        "sizes": sizes,
        "median_peak": median_peak,
        "threshold_level": threshold_level,
        "peak_trace": peak_trace,
        "N": N,
        "Lambda": Lambda,
        "Sigma_lambda": Sigma_lambda,
        "wall_time": wall,
    }


# === STATISTICAL ANALYSIS ===

def fit_power_law_exponent(sizes: list, x_min: float = None) -> dict:
    """Maximum-likelihood estimator for power-law exponent (Clauset-Shalizi-Newman 2009).

    P(x) ~ x^{-tau} for x >= x_min.
    MLE: tau = 1 + n / (sum log(x_i / x_min))
    """
    sizes = np.asarray(sizes, dtype=np.float64)
    if x_min is None:
        x_min = max(np.min(sizes), 1.0)
    above = sizes[sizes >= x_min]
    if len(above) < 10:
        return {"tau": None, "n": int(len(above)), "x_min": float(x_min), "reason": "too few samples"}
    log_ratios = np.log(above / x_min)
    tau = 1.0 + len(above) / log_ratios.sum()
    return {"tau": float(tau), "n": int(len(above)), "x_min": float(x_min)}


def main():
    print(f"Phase 9 Test E: SOC vs MNSM avalanche statistics (P14.2)")
    print(f"Output: {OUTPUT_DIR}")

    t_total = time.time()

    # BTW sandpile
    btw_result = btw_sandpile(N=64, n_drives=15000, threshold=4, seed=42)
    btw_sizes = btw_result["sizes"]
    btw_fit = fit_power_law_exponent(btw_sizes, x_min=4)

    # MNSM 2D
    mnsm_result = mnsm_2d_with_perturbations(
        N=64, L=10.0, Lambda=-8.0, Sigma_lambda=2.0,
        n_steps_warmup=2000, n_steps_record=8000,
        seed=42,
    )
    mnsm_sizes = mnsm_result["sizes"]
    mnsm_fit = fit_power_law_exponent(mnsm_sizes, x_min=0.001)

    t_total = time.time() - t_total
    print(f"\nTotal wall time: {t_total:.1f}s")

    print("\n=== Avalanche statistics comparison ===")
    print(f"  BTW: {len(btw_sizes)} avalanches; tau = {btw_fit.get('tau', 'NA')} "
          f"(n_above_xmin = {btw_fit['n']}, x_min = {btw_fit['x_min']})")
    print(f"  MNSM: {len(mnsm_sizes)} avalanches; tau = {mnsm_fit.get('tau', 'NA')} "
          f"(n_above_xmin = {mnsm_fit['n']}, x_min = {mnsm_fit['x_min']})")
    print()
    print("Reference: BTW 2D sandpile critical exponent literature value tau ~ 1.0 to 1.2")
    print("           (Manna 1991; Clauset-Shalizi-Newman 2009 statistical caveats apply)")
    print()
    print("Prediction P14.2 check: equation's release-regime avalanches should be")
    print(f"  statistically indistinguishable from BTW. Numerical comparison above.")

    # Save outputs
    summary = {
        "prediction": "P14.2 (interface 14)",
        "btw": {
            "n_avalanches": len(btw_sizes),
            "fit": btw_fit,
            "size_stats": {
                "min": float(min(btw_sizes)) if btw_sizes else None,
                "median": float(np.median(btw_sizes)) if btw_sizes else None,
                "max": float(max(btw_sizes)) if btw_sizes else None,
                "mean": float(np.mean(btw_sizes)) if btw_sizes else None,
            },
            "wall_time": btw_result["wall_time"],
        },
        "mnsm": {
            "n_avalanches": len(mnsm_sizes),
            "fit": mnsm_fit,
            "median_peak": mnsm_result["median_peak"],
            "threshold_level": mnsm_result["threshold_level"],
            "size_stats": {
                "min": float(min(mnsm_sizes)) if mnsm_sizes else None,
                "median": float(np.median(mnsm_sizes)) if mnsm_sizes else None,
                "max": float(max(mnsm_sizes)) if mnsm_sizes else None,
                "mean": float(np.mean(mnsm_sizes)) if mnsm_sizes else None,
            },
            "wall_time": mnsm_result["wall_time"],
        },
        "wall_time_total_s": t_total,
    }
    with open(OUTPUT_DIR / "summary.json", "w") as f:
        json.dump(summary, f, indent=2)

    np.savez(
        OUTPUT_DIR / "trajectories.npz",
        btw_sizes=np.asarray(btw_sizes),
        mnsm_sizes=np.asarray(mnsm_sizes),
        mnsm_peak_trace=mnsm_result["peak_trace"],
    )
    print(f"\nFull data written to {OUTPUT_DIR}/")


if __name__ == "__main__":
    main()
