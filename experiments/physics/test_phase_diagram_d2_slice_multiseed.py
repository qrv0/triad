"""Multi-seed extension of test_phase_diagram_d2_slice.py (2026-05-17).

Wrapper around the canonical d=2 phase-diagram slice that runs the full
5 x 4 Sigma_lambda x gamma_0 grid across 4 seeds {42, 43, 44, 45} and
aggregates per-grid-point metrics across seeds.

Inherits the canonical config from the parent script: d=2, N=128, L=20,
sigma_init=0.5 normalized to total norm 1 with initial peak |Psi|^2 ~ 1.273
in d=2, Lambda=-8, T_bath=0.001, 75/25 memory split with nu_fast=10,
nu_slow=0.5, n_steps=2000, dt=0.0025. Sweep arrays match parent:
  Sigma_lambda in {0.05, 0.1, 0.5, 1.0, 2.0}
  gamma_0      in {0.01, 0.05, 0.2, 1.0}

For each grid point, the seed formula is
seed = base + int(sl * 10) + int(g0 * 100); base varies across the 4 runs
(42, 43, 44, 45) so the 4 seeds at each grid point are distinct streams
while remaining deterministic.

Output: outputs/phase_diagram_d2_slice_multiseed/summary.json.

Wall time estimate: 4 seeds * 20 grid points * ~6 s = ~8 min on RTX 4060.
"""

from __future__ import annotations
import json
import sys
import time
from collections import Counter
from pathlib import Path

import numpy as np

REPO_ROOT = Path(__file__).parent.parent.parent
sys.path.insert(0, str(REPO_ROOT))

from experiments.physics.test_phase_diagram_d2_slice import (
    run_grid_point, USING_GPU,
)


OUTPUT_DIR = REPO_ROOT / "outputs" / "phase_diagram_d2_slice_multiseed"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


SEEDS = [42, 43, 44, 45]
N = 128
L = 20.0
Lambda = -8.0
T_bath = 0.001
n_steps = 2000

SIGMA_LAMBDA_VALUES = [0.05, 0.1, 0.5, 1.0, 2.0]
GAMMA_0_VALUES = [0.01, 0.05, 0.2, 1.0]


def stability_label(regimes: list) -> str:
    """Classify regime stability across seeds."""
    counts = Counter(regimes)
    n_distinct = len(counts)
    if n_distinct == 1:
        return "stable"
    if n_distinct >= 4:
        return "ambiguous"
    return "boundary"


def main():
    print(f"Multi-seed extension: phase diagram 2D slice at d=2")
    print(f"Backend: {'cupy (GPU)' if USING_GPU else 'numpy (CPU)'}")
    print(f"Canonical anti-collapse config extended to d=2")
    print(f"Seeds (base offsets): {SEEDS}")

    t_total = time.time()
    grid_data = {(sl, g0): [] for sl in SIGMA_LAMBDA_VALUES for g0 in GAMMA_0_VALUES}

    for seed_base in SEEDS:
        print(f"\n--- Seed base {seed_base} ---")
        for sl in SIGMA_LAMBDA_VALUES:
            for g0 in GAMMA_0_VALUES:
                seed = seed_base + int(sl * 10) + int(g0 * 100)
                r = run_grid_point(
                    N=N, L=L, Lambda=Lambda, Sigma_lambda=sl,
                    gamma_0=g0, T_bath=T_bath, n_steps=n_steps,
                    seed=seed,
                )
                r["seed_base"] = seed_base
                r["seed_actual"] = seed
                grid_data[(sl, g0)].append(r)
                print(f"  Sl={sl:>5.2f}, g0={g0:>5.2f}, base={seed_base}: "
                      f"regime={r['regime']:>14s}  "
                      f"peak_growth={r['peak_growth_ratio']:>8.2f}  "
                      f"final_ratio={r['final_ratio']:>10.4f}  "
                      f"t={r['wall_time']:.1f}s")

    t_total = time.time() - t_total

    aggregated = []
    for sl in SIGMA_LAMBDA_VALUES:
        for g0 in GAMMA_0_VALUES:
            seeds_data = grid_data[(sl, g0)]
            peak_growths = [d["peak_growth_ratio"] for d in seeds_data]
            final_ratios = [d["final_ratio"] for d in seeds_data]
            max_peaks = [d["max_peak"] for d in seeds_data]
            final_peaks = [d["final_peak"] for d in seeds_data]
            final_norms = [d["final_norm"] for d in seeds_data]
            regimes = [d["regime"] for d in seeds_data]

            stability = stability_label(regimes)
            regime_counts = dict(Counter(regimes))
            majority_regime = Counter(regimes).most_common(1)[0][0]

            aggregated.append({
                "Sigma_lambda": sl,
                "gamma_0": g0,
                "seeds_used": [d["seed_actual"] for d in seeds_data],
                "per_seed_regime": regimes,
                "per_seed_peak_growth": peak_growths,
                "per_seed_final_ratio": final_ratios,
                "regime_counts": regime_counts,
                "majority_regime": majority_regime,
                "stability": stability,
                "peak_growth_mean": float(np.mean(peak_growths)),
                "peak_growth_std": float(np.std(peak_growths)),
                "final_ratio_mean": float(np.mean(final_ratios)),
                "final_ratio_std": float(np.std(final_ratios)),
                "max_peak_mean": float(np.mean(max_peaks)),
                "max_peak_std": float(np.std(max_peaks)),
                "final_peak_mean": float(np.mean(final_peaks)),
                "final_peak_std": float(np.std(final_peaks)),
                "final_norm_mean": float(np.mean(final_norms)),
                "final_norm_std": float(np.std(final_norms)),
            })

    stability_counts = Counter([a["stability"] for a in aggregated])

    print(f"\n{'=' * 70}")
    print(f"  Multi-seed aggregate at d=2 (N_seeds = {len(SEEDS)})")
    print(f"{'=' * 70}")

    print(f"\nRegime stability counts (across {len(aggregated)} grid points):")
    for lab, c in sorted(stability_counts.items()):
        print(f"  {lab:>12s}: {c}")

    print(f"\nPer-grid-point summary:")
    print(f"  {'sl':>5s}  {'g0':>5s}  {'majority':>14s}  {'stability':>10s}  "
          f"{'peak_growth (m+/-s)':>22s}  {'final_ratio (m+/-s)':>22s}")
    for a in aggregated:
        pg_mean = a["peak_growth_mean"]
        pg_std = a["peak_growth_std"]
        fr_mean = a["final_ratio_mean"]
        fr_std = a["final_ratio_std"]
        print(f"  {a['Sigma_lambda']:>5.2f}  {a['gamma_0']:>5.2f}  "
              f"{a['majority_regime']:>14s}  {a['stability']:>10s}  "
              f"{pg_mean:>10.3f} +/- {pg_std:>7.3f}  "
              f"{fr_mean:>10.5f} +/- {fr_std:>8.5f}")

    print(f"\n  Wall time total: {t_total:.1f}s")

    summary = {
        "prediction_tested": "Phase diagram 2D slice at d=2 multi-seed extension of results/27",
        "config": {
            "d": 2, "N": N, "L": L, "Lambda": Lambda, "T_bath": T_bath,
            "n_steps": n_steps, "dt": 0.0025,
            "nu_fast": 10.0, "nu_slow": 0.5,
            "sigma_init": 0.5, "normalized": True,
        },
        "seeds": SEEDS,
        "n_seeds": len(SEEDS),
        "sigma_lambda_values": SIGMA_LAMBDA_VALUES,
        "gamma_0_values": GAMMA_0_VALUES,
        "aggregated_grid": aggregated,
        "stability_counts": dict(stability_counts),
        "wall_time_total_s": t_total,
        "backend": "cupy" if USING_GPU else "numpy",
    }
    with open(OUTPUT_DIR / "summary.json", "w") as f:
        json.dump(summary, f, indent=2)
    print(f"\nSummary written to {OUTPUT_DIR}/summary.json")


if __name__ == "__main__":
    main()
