"""Phase 9 wave-3 (corrected 2026-05-17): 3D vibrational mode spectrum.

Extends results/03 (2D vibrational analysis: median 0.6 cycles/unit time,
secondary lock at 1.0) to d=3 using the canonical 3D anti-collapse / crystalline-
state protocol established in results/04-anti-collapse-3d.md and paper Section
6.3.

This is the corrected version replacing the 2026-05-16 wrong-config test
flagged in docs/llm-hedge-annotations.md (Phase 9 wave-3 cluster, Failure 3).
The previous version used sigma_init=1.2 with non-normalized Gaussian giving
peak |Psi|^2 ~ 0.037 (40x below the canonical ~1.44 with sigma_init=0.5
normalized), Sigma_lambda=4 (anti-collapse regime, not crystalline window),
gamma_0=0.02, T_bath=0.005 (against paper Section 6.3 conservative regime),
and 1000-step equilibration (vs paper's 2000-step warmup). The spectrum
produced was dominated by thermal noise on a dispersing field.

Canonical config (this version):
- N=64 (compromise between paper's N=128 and GPU memory budget for per-voxel FFT)
- L=20
- sigma_init=0.5 with psi normalized to total norm = 1 via psi /= sqrt(sum |psi|^2 dx^d)
- Lambda=-8 (matching results/04 supercritical regime)
- Memory: nu1=10, lambda1=1.125; nu2=0.5, lambda2=0.375 (total Sigma_lambda=1.5,
  the crystalline window from paper Section 6.2 Bravais sweep, with 75/25 split
  matching the 3D convention from results/04)
- gamma_0=0.01, T_bath=0.0001 (small positive per Rule A in
  ~/.claude/skills/structural-research-mode/SKILL.md, kept tiny to minimize
  thermal contamination of the vibrational spectrum; the spectrum will have a
  thermal background but the crystalline modes should dominate)
- dt=0.0025
- n_warmup=2000 (matching paper Section 6.3)
- n_record=4000 (matching paper Section 6.3)
- Record per-voxel rho on a 16^3 subgrid (every 4th voxel) for FFT analysis

Output: outputs/vibrational_3d_p3/{summary.json, freqs.npy, ...}.
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


def initial_gaussian_normalized_3d(N: int, L: float, sigma_init: float) -> "xp.ndarray":
    """Canonical initial state matching solver_3d.py build_initial_state:
    Gaussian with total integral |Psi|^2 dx^3 = 1.

    For sigma_init=0.5, L=20, N=128 this gives peak |Psi(0)|^2 ~ 1.44 matching
    paper Section 6.1 / results/04. The same formula at smaller N gives the
    same peak density to within discretization error.
    """
    coord = xp.linspace(-L / 2, L / 2, N, endpoint=False)
    X, Y, Z = xp.meshgrid(coord, coord, coord, indexing="ij")
    r_squared = X ** 2 + Y ** 2 + Z ** 2
    psi = xp.exp(-r_squared / (2 * sigma_init ** 2)).astype(xp.complex64)
    dx = L / N
    norm = float(xp.sqrt(xp.sum(xp.abs(psi) ** 2) * dx ** 3))
    psi = psi / norm
    return psi


def run_3d_vibrational(N: int = 64, L: float = 20.0,
                       Lambda: float = -8.0, Sigma_lambda: float = 1.5,
                       gamma_0: float = 0.01, T_bath: float = 0.0001,
                       nu_fast: float = 10.0, nu_slow: float = 0.5,
                       dt: float = 0.0025, n_warmup: int = 2000, n_record: int = 4000,
                       subgrid_stride: int = 4,
                       sigma_init: float = 0.5, seed: int = 42) -> dict:
    """3D crystalline regime via canonical protocol, record per-voxel rho on subgrid."""
    rng = np.random.default_rng(seed)
    psi = initial_gaussian_normalized_3d(N, L, sigma_init)
    kinetic_phase = fft_kinetic_phase(N, L, d=3)
    propagator = xp.exp(kinetic_phase * dt)

    # Two-mode memory: 75/25 split matching results/04 3D convention
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

    initial_norm = float(xp.sum(xp.abs(psi) ** 2) * (L / N) ** 3)
    initial_peak = float(xp.max(xp.abs(psi) ** 2))

    # Record on subgrid: every subgrid_stride-th voxel in each dim
    # For N=64 with stride=4: subgrid is 16^3 = 4096 voxels
    sub_N = N // subgrid_stride
    rho_history = np.zeros((n_record, sub_N, sub_N, sub_N), dtype=np.float32)

    print(f"  Canonical 3D vibrational config:")
    print(f"  N={N} (subgrid {sub_N}^3 = {sub_N**3} voxels recorded)")
    print(f"  initial_norm = {initial_norm:.6f} (should be 1.0)")
    print(f"  initial_peak = {initial_peak:.4f} (canonical ~1.44 for sigma=0.5 in d=3)")
    print(f"  warmup: {n_warmup} steps; record: {n_record} steps")
    print(f"  P3: gamma_0={gamma_0}, T_bath={T_bath}, noise_amp={noise_amp:.2e}")

    t0 = time.time()
    # Warmup phase
    for step in range(n_warmup):
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

    warmup_wall = time.time() - t0
    warmup_norm = float(xp.sum(xp.abs(psi) ** 2) * (L / N) ** 3)
    warmup_peak = float(xp.max(xp.abs(psi) ** 2))
    print(f"  Warmup complete in {warmup_wall:.1f}s")
    print(f"  Post-warmup: norm={warmup_norm:.4f}, peak={warmup_peak:.4f}")

    # Recording phase
    for step in range(n_record):
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

        # Record subgrid every step
        rho_now = (psi.real ** 2 + psi.imag ** 2).astype(xp.float32)
        rho_history[step] = to_cpu(rho_now[::subgrid_stride, ::subgrid_stride, ::subgrid_stride])

    total_wall = time.time() - t0
    final_norm = float(xp.sum(xp.abs(psi) ** 2) * (L / N) ** 3)
    final_peak = float(xp.max(xp.abs(psi) ** 2))
    print(f"  Recording complete; total wall {total_wall:.1f}s")
    print(f"  Final: norm={final_norm:.4f}, peak={final_peak:.4f}")

    return {
        "psi_shape": tuple(psi.shape),
        "rho_history": rho_history,
        "n_record": n_record,
        "subgrid_N": sub_N,
        "sample_dt": dt,
        "wall_time": total_wall,
        "initial_norm": initial_norm,
        "initial_peak": initial_peak,
        "warmup_norm": warmup_norm,
        "warmup_peak": warmup_peak,
        "final_norm": final_norm,
        "final_peak": final_peak,
    }


def analyze_spectrum(rho_history: np.ndarray, sample_dt: float):
    """Per-voxel temporal FFT, extract dominant frequency per voxel."""
    n_samples = rho_history.shape[0]
    freqs = np.fft.rfftfreq(n_samples, d=sample_dt)
    # Subtract per-voxel mean (DC)
    rho_centered = rho_history - rho_history.mean(axis=0, keepdims=True)
    rho_flat = rho_centered.reshape(n_samples, -1)
    spectrum = np.abs(np.fft.rfft(rho_flat, axis=0))
    # Dominant frequency per voxel (excluding DC bin)
    dominant_idx = np.argmax(spectrum[1:], axis=0) + 1
    dominant_freqs = freqs[dominant_idx]
    aggregate_spectrum = spectrum.mean(axis=1)
    return {
        "freqs": freqs,
        "dominant_freqs_per_voxel": dominant_freqs,
        "aggregate_spectrum": aggregate_spectrum,
    }


def main():
    print(f"Phase 9 wave-3 (CORRECTED): 3D vibrational mode spectrum")
    print(f"Backend: {'cupy (GPU)' if USING_GPU else 'numpy (CPU)'}")
    print(f"Canonical 3D crystalline-state protocol per paper Section 6.3 + results/04")

    t_total = time.time()
    r = run_3d_vibrational(
        N=64, L=20.0, Lambda=-8.0, Sigma_lambda=1.5,
        gamma_0=0.01, T_bath=0.0001,
        dt=0.0025, n_warmup=2000, n_record=4000,
        subgrid_stride=4, sigma_init=0.5, seed=42,
    )
    t_total = time.time() - t_total

    print(f"\nAnalyzing spectrum...")
    analysis = analyze_spectrum(r["rho_history"], r["sample_dt"])

    freqs = analysis["freqs"]
    dom = analysis["dominant_freqs_per_voxel"]
    agg = analysis["aggregate_spectrum"]

    dom_min = float(dom.min())
    dom_max = float(dom.max())
    dom_median = float(np.median(dom))
    dom_mean = float(np.mean(dom))
    dom_std = float(np.std(dom))

    print(f"\nPer-voxel dominant frequency statistics:")
    print(f"  Range: {dom_min:.3f} to {dom_max:.3f} cycles/unit time")
    print(f"  Median: {dom_median:.3f}  (reference: 2D results/03 = 0.6)")
    print(f"  Mean: {dom_mean:.3f}")
    print(f"  Std: {dom_std:.3f}")

    bin_edges = np.arange(0, dom_max + 0.05, 0.05)
    hist, _ = np.histogram(dom, bins=bin_edges)
    top_bins = np.argsort(hist)[-15:][::-1]
    top_freqs_centers = [float((bin_edges[i] + bin_edges[i+1]) / 2) for i in top_bins]
    top_counts = [int(hist[i]) for i in top_bins]
    print(f"\nTop 15 most-common dominant frequencies (0.05-cycle bins):")
    for fc, c in sorted(zip(top_freqs_centers, top_counts)):
        print(f"  {fc:.3f} cycles/unit time: {c} voxels")

    np.save(OUTPUT_DIR / "freqs.npy", freqs)
    np.save(OUTPUT_DIR / "aggregate_spectrum.npy", agg)
    np.save(OUTPUT_DIR / "dominant_freqs_per_voxel.npy", dom)
    np.save(OUTPUT_DIR / "histogram.npy", hist)
    np.save(OUTPUT_DIR / "bin_edges.npy", bin_edges)

    summary = {
        "prediction_tested": "3D vibrational spectrum extension of results/03 (2D), canonical config",
        "config": {
            "N": 64, "L": 20.0, "Lambda": -8.0, "Sigma_lambda": 1.5,
            "lambda_fast": 1.125, "lambda_slow": 0.375,
            "gamma_0": 0.01, "T_bath": 0.0001,
            "nu_fast": 10.0, "nu_slow": 0.5,
            "dt": 0.0025, "n_warmup": 2000, "n_record": 4000,
            "subgrid_stride": 4, "subgrid_N": r["subgrid_N"],
            "sigma_init": 0.5, "normalized": True,
        },
        "results": {
            "wall_time_s": t_total,
            "initial_norm": r["initial_norm"],
            "initial_peak": r["initial_peak"],
            "warmup_norm": r["warmup_norm"],
            "warmup_peak": r["warmup_peak"],
            "final_norm": r["final_norm"],
            "final_peak": r["final_peak"],
            "dominant_freq_stats": {
                "range": [dom_min, dom_max],
                "median": dom_median,
                "mean": dom_mean,
                "std": dom_std,
            },
            "top_15_dominant_freq_bins": list(zip(top_freqs_centers, top_counts)),
        },
        "backend": "cupy" if USING_GPU else "numpy",
    }
    with open(OUTPUT_DIR / "summary.json", "w") as f:
        json.dump(summary, f, indent=2)
    print(f"\nSummary written to {OUTPUT_DIR}/summary.json")


if __name__ == "__main__":
    main()
