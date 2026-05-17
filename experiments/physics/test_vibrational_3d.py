"""Phase 9 wave-3 test: vibrational mode spectrum at d=3 (P3 active).

**METHODOLOGICAL FLAG (2026-05-17 audit):** the configuration in this script
does NOT match the canonical 3D anti-collapse / crystalline-state protocol
established in results/04 and paper Section 6.3. Specifically:
  - sigma_init=1.2 with non-normalized Gaussian gives peak |Psi|^2 ~ 0.037,
    ~40x weaker than the canonical sigma_init=0.5 with total-norm=1
    normalization (peak |Psi|^2 ~ 1.44). The field never reaches the
    crystalline regime at this amplitude.
  - Sigma_lambda=4.0 is the 3D anti-collapse regime (results/04), NOT the
    crystalline window Sigma_lambda~1.5 (paper Section 6.3) appropriate
    for vibrational mode analysis.
  - gamma_0=0.02, T_bath=0.005 contradicts the canonical conservative
    regime used for vibrational spectrum extraction in results/03 (2D)
    and paper Section 6.3 (3D).
The "spectrum" produced by this script is dominated by thermal noise on a
dispersing field, not the 3D crystalline vibrational spectrum.
This script and its output (results/25, outputs/vibrational_3d_p3) are
preserved as historical record per the repository's documentation-of-errors
philosophy; the proper 3D vibrational analysis requires N=128, L=20,
sigma_init=0.5 normalized, Lambda=-8, Sigma_lambda=1.5 (or 4 for anti-collapse
regime), gamma_0=0 and T=0, 2000-step warmup. See docs/llm-hedge-annotations.md.

Extends the 2D vibrational analysis of results/03 (median 0.6 cycles/unit time,
secondary at 1.0) to d=3 using the standard 3D anti-collapse configuration.
The structural question (from results/23 audit) is whether the equation's 3D
vibrational spectrum has multi-modal structure with consecutive ratios similar
to the whole-tone scale Wolfe-Swanson-Till 2020 measured at the Hypogeum
(consecutive ratio ~1.122).

Configuration: 3D supercritical regime in the released-crystalline state.
N=32 (32^3 = 32,768 voxels per field, manageable for per-voxel FFT analysis).
Lambda=-8.0, Sigma_lambda=4.0 (the 3D-rescaled total memory coupling per
results/04 anti-collapse 3D).

P3 active: gamma_0=0.02, T_bath=0.005 (small enough not to dominate the
spectrum but consistent with principles/03-coupling.md Rule A; isolated
regime is not used). The 2D published spectrum in results/03 used the
conservative regime (gamma_0=0, T=0); the present test uses the
coupled-regime methodology adopted in wave-2 onward and identifies
whether the discrete spectral features survive small thermal noise.

Output: outputs/vibrational_3d_p3/{summary.json, spectrum.npy, histogram.npy}.
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
OUTPUT_DIR = REPO_ROOT / "outputs" / "vibrational_3d_p3"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def to_cpu(arr):
    return arr.get() if hasattr(arr, "get") else arr


def fft_kinetic_phase(N: int, L: float, d: int = 3, hbar: float = 1.0, mass: float = 1.0):
    k_axis = 2 * xp.pi * xp.fft.fftfreq(N, d=L / N)
    grids = xp.meshgrid(*[k_axis] * d, indexing="ij")
    k_squared = sum(g ** 2 for g in grids)
    return -1j * (hbar ** 2 / (2 * mass)) * k_squared


def initial_gaussian_3d(N: int, L: float, sigma_init: float):
    coord = xp.linspace(-L / 2, L / 2, N, endpoint=False)
    X, Y, Z = xp.meshgrid(coord, coord, coord, indexing="ij")
    r_squared = X ** 2 + Y ** 2 + Z ** 2
    psi = (1.0 / (sigma_init * float(np.sqrt(2 * np.pi)))) ** 1.5
    psi = psi * xp.exp(-r_squared / (2 * sigma_init ** 2))
    return psi.astype(xp.complex64)


def run_3d_vibrational(N: int = 32, L: float = 20.0,
                       Lambda: float = -8.0, Sigma_lambda: float = 4.0,
                       gamma_0: float = 0.02, T_bath: float = 0.005,
                       nu_fast: float = 10.0, nu_slow: float = 0.5,
                       dt: float = 0.005, n_steps: int = 4000,
                       sample_every: int = 4, sigma_init: float = 1.2,
                       seed: int = 42) -> dict:
    """3D crystalline regime, record per-voxel time series for FFT analysis."""
    rng = np.random.default_rng(seed)
    psi = initial_gaussian_3d(N, L, sigma_init)
    kinetic_phase = fft_kinetic_phase(N, L, d=3)
    propagator = xp.exp(kinetic_phase * dt)

    # Two-mode memory: 75% in fast, 25% in slow (matches 3D anti-collapse convention)
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

    n_samples = n_steps // sample_every
    # Storage: per-voxel time series of |psi|^2 at sampled times
    # Shape (n_samples, N, N, N), float32
    rho_history = np.zeros((n_samples, N, N, N), dtype=np.float32)

    initial_norm = float(xp.sum(xp.abs(psi) ** 2) * (L / N) ** 3)

    print(f"  Equilibration phase (first 25%): {n_steps // 4} steps")
    print(f"  Recording phase: {n_steps - n_steps // 4} steps, sampling every {sample_every}")

    t0 = time.time()
    sample_idx = 0
    record_start = n_steps // 4  # skip initial transient

    for step in range(n_steps):
        # V/2
        rho = (psi.real ** 2 + psi.imag ** 2).astype(xp.float32)
        V_mem = lambda_fast * y_fast + lambda_slow * y_slow
        V_total = Lambda * rho + V_mem
        psi = psi * xp.exp(-1j * V_total * dt / 2)

        # K
        psi = xp.fft.ifftn(xp.fft.fftn(psi) * propagator)

        # V/2
        rho = (psi.real ** 2 + psi.imag ** 2).astype(xp.float32)
        V_mem = lambda_fast * y_fast + lambda_slow * y_slow
        V_total = Lambda * rho + V_mem
        psi = psi * xp.exp(-1j * V_total * dt / 2)

        # OU
        y_fast = decay_fast * y_fast + accum_fast * rho
        y_slow = decay_slow * y_slow + accum_slow * rho

        # P3 dissipation
        psi = psi * dissipation_factor

        # P3 noise (FDT-locked)
        if noise_amp > 0:
            shape = psi.shape
            xi_re = xp.asarray(rng.standard_normal(shape).astype(np.float32))
            xi_im = xp.asarray(rng.standard_normal(shape).astype(np.float32))
            psi = psi + noise_amp * (xi_re + 1j * xi_im) / float(np.sqrt(2.0))

        # Record (after equilibration)
        if step >= record_start and (step - record_start) % sample_every == 0 and sample_idx < n_samples:
            rho_now = (psi.real ** 2 + psi.imag ** 2).astype(xp.float32)
            rho_history[sample_idx] = to_cpu(rho_now)
            sample_idx += 1

    wall = time.time() - t0
    n_recorded = sample_idx

    return {
        "psi_shape": tuple(psi.shape),
        "rho_history": rho_history[:n_recorded],  # truncate if needed
        "n_samples": n_recorded,
        "sample_dt": dt * sample_every,
        "wall_time": wall,
        "initial_norm": initial_norm,
        "final_norm": float(xp.sum(xp.abs(psi) ** 2) * (L / N) ** 3),
    }


def analyze_spectrum(rho_history: np.ndarray, sample_dt: float):
    """Per-voxel temporal FFT, extract dominant frequency per voxel."""
    n_samples, N, _, _ = rho_history.shape
    # Time axis
    freqs = np.fft.rfftfreq(n_samples, d=sample_dt)  # in cycles per unit time
    # Per-voxel FFT (subtract mean to remove DC)
    rho_centered = rho_history - rho_history.mean(axis=0, keepdims=True)
    # Reshape to (n_samples, N^3) for batched FFT
    rho_flat = rho_centered.reshape(n_samples, -1)
    # FFT along time axis
    spectrum = np.abs(np.fft.rfft(rho_flat, axis=0))
    # Find dominant frequency per voxel (excluding DC at index 0)
    dominant_idx = np.argmax(spectrum[1:], axis=0) + 1
    dominant_freqs = freqs[dominant_idx]
    # Aggregate spectrum (mean across voxels)
    aggregate_spectrum = spectrum.mean(axis=1)
    return {
        "freqs": freqs,
        "dominant_freqs_per_voxel": dominant_freqs,
        "aggregate_spectrum": aggregate_spectrum,
    }


def main():
    print(f"Phase 9 wave-3 test: 3D vibrational mode spectrum (P3 active)")
    print(f"Backend: {'cupy (GPU)' if USING_GPU else 'numpy (CPU)'}")

    print(f"\nConfiguration:")
    print(f"  N = 32, L = 20, Lambda = -8.0, Sigma_lambda = 4.0")
    print(f"  gamma_0 = 0.02 (P3 active), T_bath = 0.005")
    print(f"  nu_fast = 10, nu_slow = 0.5")
    print(f"  dt = 0.005, n_steps = 4000")
    print(f"  Sample every 4 steps (Nyquist for ~10 cycles/unit time)")

    t_total = time.time()
    r = run_3d_vibrational()
    t_total = time.time() - t_total

    print(f"\nWall time: {t_total:.1f}s")
    print(f"Recorded {r['n_samples']} samples per voxel")
    print(f"Initial norm: {r['initial_norm']:.4f}; Final norm: {r['final_norm']:.4f}")

    print(f"\nAnalyzing spectrum...")
    analysis = analyze_spectrum(r["rho_history"], r["sample_dt"])

    freqs = analysis["freqs"]
    dom = analysis["dominant_freqs_per_voxel"]
    agg = analysis["aggregate_spectrum"]

    # Per-voxel dominant frequency statistics
    dom_median = float(np.median(dom))
    dom_mean = float(np.mean(dom))
    dom_std = float(np.std(dom))
    dom_min = float(dom.min())
    dom_max = float(dom.max())

    print(f"\nDominant frequency per voxel:")
    print(f"  Range: {dom_min:.3f} to {dom_max:.3f} cycles/unit time")
    print(f"  Median: {dom_median:.3f}")
    print(f"  Mean: {dom_mean:.3f}")
    print(f"  Std: {dom_std:.3f}")

    # Histogram of dominant frequencies (bins of 0.1 cycle/unit time)
    bin_edges = np.arange(0, dom_max + 0.1, 0.1)
    hist, _ = np.histogram(dom, bins=bin_edges)

    # Identify top peaks in histogram (most-common dominant frequencies across voxels)
    top_bins = np.argsort(hist)[-10:][::-1]
    top_freqs_centers = [(bin_edges[i] + bin_edges[i+1]) / 2 for i in top_bins]
    top_counts = [int(hist[i]) for i in top_bins]
    print(f"\nTop 10 most-common dominant frequencies (bin centers):")
    for fc, c in zip(top_freqs_centers, top_counts):
        print(f"  {fc:.2f} cycles/unit time: {c} voxels")

    # Look for the predicted 0.6 and 1.0 peaks (from 2D results/03)
    print(f"\nReference (2D results/03): median 0.6, secondary peak locked at 1.0")
    print(f"3D extrapolation per dimensional rescaling: rougher prediction")

    # Aggregate spectrum: identify top peaks
    # (Exclude DC at index 0; look for local maxima)
    nonzero = agg[1:]
    nonzero_freqs = freqs[1:]
    # Top 15 peaks in aggregate spectrum
    top_agg_idx = np.argsort(nonzero)[-15:][::-1]
    top_agg_peaks = [(float(nonzero_freqs[i]), float(nonzero[i])) for i in top_agg_idx]
    print(f"\nTop 15 peaks in aggregate spectrum (cycles/unit time, amplitude):")
    for f, a in sorted(top_agg_peaks, key=lambda x: x[0])[:15]:
        print(f"  {f:6.3f} Hz_comp  amplitude {a:.2e}")

    # Compute consecutive ratios for the top peaks
    sorted_freqs = sorted([f for f, _ in top_agg_peaks])
    consec_ratios = [sorted_freqs[i+1] / sorted_freqs[i] for i in range(len(sorted_freqs) - 1)]
    print(f"\nConsecutive-peak ratios in sorted top-15 aggregate peaks:")
    for ratio in consec_ratios:
        print(f"  {ratio:.3f}")
    if consec_ratios:
        print(f"  Mean: {np.mean(consec_ratios):.3f} +/- {np.std(consec_ratios):.3f}")
        print(f"  Whole-tone reference: 2^(2/12) = 1.122")

    # Save analysis arrays
    np.save(OUTPUT_DIR / "freqs.npy", freqs)
    np.save(OUTPUT_DIR / "aggregate_spectrum.npy", agg)
    np.save(OUTPUT_DIR / "dominant_freqs_per_voxel.npy", dom)
    np.save(OUTPUT_DIR / "histogram.npy", hist)
    np.save(OUTPUT_DIR / "bin_edges.npy", bin_edges)

    summary = {
        "prediction_tested": "Phase 9 wave-3 3D vibrational extension of results/03 (2D), P3 active",
        "config": {
            "N": 32, "L": 20.0, "Lambda": -8.0, "Sigma_lambda": 4.0,
            "gamma_0": 0.02, "T_bath": 0.005,
            "nu_fast": 10.0, "nu_slow": 0.5,
            "dt": 0.005, "n_steps": 4000, "sample_every": 4,
        },
        "results": {
            "wall_time_s": t_total,
            "n_samples_per_voxel": r["n_samples"],
            "n_voxels": int(32 ** 3),
            "dominant_freq_stats": {
                "range": [dom_min, dom_max],
                "median": dom_median,
                "mean": dom_mean,
                "std": dom_std,
            },
            "top_dominant_freq_bins": list(zip(top_freqs_centers, top_counts)),
            "top_aggregate_peaks": top_agg_peaks,
            "consecutive_peak_ratios": consec_ratios,
        },
        "initial_norm": r["initial_norm"],
        "final_norm": r["final_norm"],
        "backend": "cupy" if USING_GPU else "numpy",
    }
    with open(OUTPUT_DIR / "summary.json", "w") as f:
        json.dump(summary, f, indent=2)
    print(f"\nSummary written to {OUTPUT_DIR}/summary.json")


if __name__ == "__main__":
    main()
