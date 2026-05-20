"""Multi-seed extension of test_vibrational_3d.py (2026-05-17).

Wrapper around the canonical test_vibrational_3d.py that runs the same
crystalline-window configuration across 4 seeds {42, 43, 44, 45} and aggregates
per-seed metrics. Inherits the canonical config from the parent script
(N=64, L=20, Lambda=-8, Sigma_lambda=1.5 crystalline window per paper Section
6.2, 75/25 memory split with nu_fast=10, nu_slow=0.5, gamma_0=0.01,
T_bath=0.0001, 2000-step warmup + 4000-step recording on 16^3 subgrid stride 4,
sigma_init=0.5 normalized to total norm 1, initial peak |Psi|^2 ~ 1.44).

Per-seed metrics collected:
- median, mean, std of dominant frequency across 4,096 subgrid voxels
- top-5 frequency bins with voxel counts (0.05-cycle bins)
- initial_peak, final_norm

Aggregated across seeds:
- mean and std of each scalar metric
- mean and std of voxel counts in each top-5 bin

Output: outputs/vibrational_3d_p3_multiseed/summary.json.

Wall time estimate: 4 seeds * 106 s per seed = ~7 min on RTX 4060.
"""

from __future__ import annotations
import json
import sys
import time
from pathlib import Path

import numpy as np

REPO_ROOT = Path(__file__).parent.parent.parent
sys.path.insert(0, str(REPO_ROOT))

from experiments.physics.test_vibrational_3d import (
    run_3d_vibrational, analyze_spectrum, USING_GPU,
)


OUTPUT_DIR = REPO_ROOT / "outputs" / "vibrational_3d_p3_multiseed"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

SEEDS = [42, 43, 44, 45]

CANONICAL_BINS = [0.125, 0.225, 0.325, 0.425, 0.525]
BIN_TOLERANCE = 0.0125  # half of 0.05/2


def per_seed_metrics(seed: int) -> dict:
    print(f"\n{'=' * 70}")
    print(f"  Seed {seed}")
    print(f"{'=' * 70}")

    r = run_3d_vibrational(
        N=64, L=20.0, Lambda=-8.0, Sigma_lambda=1.5,
        gamma_0=0.01, T_bath=0.0001,
        nu_fast=10.0, nu_slow=0.5,
        dt=0.0025, n_warmup=2000, n_record=4000,
        subgrid_stride=4, sigma_init=0.5, seed=seed,
    )

    analysis = analyze_spectrum(r["rho_history"], r["sample_dt"])
    dom = analysis["dominant_freqs_per_voxel"]

    dom_min = float(dom.min())
    dom_max = float(dom.max())
    dom_median = float(np.median(dom))
    dom_mean = float(np.mean(dom))
    dom_std = float(np.std(dom))

    # 0.05-cycle bins from 0 to max
    bin_edges = np.arange(0, dom_max + 0.05, 0.05)
    hist, _ = np.histogram(dom, bins=bin_edges)
    centers = [float((bin_edges[i] + bin_edges[i + 1]) / 2) for i in range(len(hist))]

    top5_indices = np.argsort(hist)[-5:][::-1]
    top5 = sorted([(centers[i], int(hist[i])) for i in top5_indices])

    # Voxel counts at the canonical bin centers (0.125 .. 0.525) for cross-seed comparison
    canonical_counts = {}
    for cb in CANONICAL_BINS:
        # Find the bin center closest to cb within tolerance
        idx_in_centers = None
        for i, c in enumerate(centers):
            if abs(c - cb) < BIN_TOLERANCE:
                idx_in_centers = i
                break
        canonical_counts[f"{cb:.3f}"] = int(hist[idx_in_centers]) if idx_in_centers is not None else 0

    print(f"  median={dom_median:.4f}, mean={dom_mean:.4f}, std={dom_std:.4f}")
    print(f"  initial_peak={r['initial_peak']:.4f}, final_norm={r['final_norm']:.4f}")
    print(f"  canonical_bin_counts: {canonical_counts}")

    return {
        "seed": seed,
        "median_dominant_freq": dom_median,
        "mean_dominant_freq": dom_mean,
        "std_dominant_freq": dom_std,
        "range_min": dom_min,
        "range_max": dom_max,
        "top5_bins": top5,
        "canonical_bin_counts": canonical_counts,
        "initial_peak": r["initial_peak"],
        "warmup_norm": r["warmup_norm"],
        "warmup_peak": r["warmup_peak"],
        "final_norm": r["final_norm"],
        "final_peak": r["final_peak"],
        "wall_time": r["wall_time"],
    }


def aggregate(per_seed_results: list) -> dict:
    """Compute mean and std across seeds for each scalar metric and per-bin count."""
    def mean_std(vals):
        arr = np.asarray(vals, dtype=np.float64)
        return float(np.mean(arr)), float(np.std(arr))

    medians = [r["median_dominant_freq"] for r in per_seed_results]
    means = [r["mean_dominant_freq"] for r in per_seed_results]
    stds = [r["std_dominant_freq"] for r in per_seed_results]
    initial_peaks = [r["initial_peak"] for r in per_seed_results]
    final_norms = [r["final_norm"] for r in per_seed_results]
    final_peaks = [r["final_peak"] for r in per_seed_results]

    canonical_bin_stats = {}
    for cb in CANONICAL_BINS:
        key = f"{cb:.3f}"
        counts = [r["canonical_bin_counts"].get(key, 0) for r in per_seed_results]
        m, s = mean_std(counts)
        canonical_bin_stats[key] = {
            "per_seed": counts,
            "mean": m,
            "std": s,
        }

    median_mean, median_std = mean_std(medians)
    mean_mean, mean_std_val = mean_std(means)
    std_mean, std_std = mean_std(stds)
    initial_peak_mean, initial_peak_std = mean_std(initial_peaks)
    final_norm_mean, final_norm_std = mean_std(final_norms)
    final_peak_mean, final_peak_std = mean_std(final_peaks)

    return {
        "n_seeds": len(per_seed_results),
        "median_dominant_freq": {
            "per_seed": medians, "mean": median_mean, "std": median_std,
        },
        "mean_dominant_freq": {
            "per_seed": means, "mean": mean_mean, "std": mean_std_val,
        },
        "std_dominant_freq": {
            "per_seed": stds, "mean": std_mean, "std": std_std,
        },
        "initial_peak": {
            "per_seed": initial_peaks, "mean": initial_peak_mean, "std": initial_peak_std,
        },
        "final_norm": {
            "per_seed": final_norms, "mean": final_norm_mean, "std": final_norm_std,
        },
        "final_peak": {
            "per_seed": final_peaks, "mean": final_peak_mean, "std": final_peak_std,
        },
        "canonical_bin_counts": canonical_bin_stats,
    }


def main():
    print(f"Multi-seed extension: 3D vibrational mode spectrum")
    print(f"Backend: {'cupy (GPU)' if USING_GPU else 'numpy (CPU)'}")
    print(f"Canonical 3D crystalline-state protocol per paper Section 6.3 + results/04")
    print(f"Seeds: {SEEDS}")

    t_total = time.time()
    per_seed = [per_seed_metrics(s) for s in SEEDS]
    t_total = time.time() - t_total

    agg = aggregate(per_seed)

    print(f"\n{'=' * 70}")
    print(f"  Multi-seed aggregate (N_seeds = {len(SEEDS)})")
    print(f"{'=' * 70}")
    print(f"  median dominant freq:  {agg['median_dominant_freq']['mean']:.4f} +/- {agg['median_dominant_freq']['std']:.4f}")
    print(f"  mean dominant freq:    {agg['mean_dominant_freq']['mean']:.4f} +/- {agg['mean_dominant_freq']['std']:.4f}")
    print(f"  std dominant freq:     {agg['std_dominant_freq']['mean']:.4f} +/- {agg['std_dominant_freq']['std']:.4f}")
    print(f"  initial_peak:          {agg['initial_peak']['mean']:.4f} +/- {agg['initial_peak']['std']:.4f}")
    print(f"  final_norm:            {agg['final_norm']['mean']:.4f} +/- {agg['final_norm']['std']:.4f}")
    print(f"  final_peak:            {agg['final_peak']['mean']:.6f} +/- {agg['final_peak']['std']:.6f}")
    print(f"\n  Canonical-bin voxel counts (mean +/- std across seeds):")
    for cb in CANONICAL_BINS:
        key = f"{cb:.3f}"
        st = agg['canonical_bin_counts'][key]
        print(f"    bin {key}: {st['mean']:8.1f} +/- {st['std']:7.1f}   (per-seed: {st['per_seed']})")

    print(f"\n  Wall time total: {t_total:.1f}s")

    summary = {
        "prediction_tested": "3D vibrational spectrum multi-seed extension of results/25",
        "config": {
            "N": 64, "L": 20.0, "Lambda": -8.0, "Sigma_lambda": 1.5,
            "lambda_fast": 1.125, "lambda_slow": 0.375,
            "gamma_0": 0.01, "T_bath": 0.0001,
            "nu_fast": 10.0, "nu_slow": 0.5,
            "dt": 0.0025, "n_warmup": 2000, "n_record": 4000,
            "subgrid_stride": 4, "subgrid_N": 16,
            "sigma_init": 0.5, "normalized": True,
        },
        "seeds": SEEDS,
        "n_seeds": len(SEEDS),
        "per_seed": per_seed,
        "aggregate": agg,
        "wall_time_total_s": t_total,
        "backend": "cupy" if USING_GPU else "numpy",
    }
    with open(OUTPUT_DIR / "summary.json", "w") as f:
        json.dump(summary, f, indent=2)
    print(f"\nSummary written to {OUTPUT_DIR}/summary.json")


if __name__ == "__main__":
    main()
