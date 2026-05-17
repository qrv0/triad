"""Phase 9 wave-3 multi-seed extension of test_simsiam_cubic_ssm.py.

Runs P6.3 (cubic state nonlinearity prevents SimSiam collapse) across 4
seeds for each of the two variants (cubic_p3, linear_p3) to get variance
estimates on the effective-rank effect observed in the single-seed Phase
C run (cubic 4.60/64 vs linear 2.88/64).

Total wall: 4 seeds * 2 variants * ~25s = ~3 min on RTX 4060.

Output: outputs/simsiam_cubic_ssm_multiseed/summary.json.
"""

from __future__ import annotations
import json
import sys
import time
from pathlib import Path

import numpy as np
import torch

REPO_ROOT = Path(__file__).parent.parent.parent
sys.path.insert(0, str(REPO_ROOT))

from experiments.neural.test_simsiam_cubic_ssm import (
    train_variant, generate_clustered_sequences,
    LAMBDA_CUBIC, LAMBDA_LINEAR, GAMMA_0_FDT, T_FDT,
    D_INPUT, SEQ_LEN,
)


OUTPUT_DIR = REPO_ROOT / "outputs" / "simsiam_cubic_ssm_multiseed"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def run_variant_with_seed(name: str, lambda_cubic: float, seed: int,
                          train_data: torch.Tensor, val_data: torch.Tensor,
                          device: str) -> dict:
    print(f"\n--- Variant: {name}, seed: {seed} ---")
    torch.manual_seed(seed)
    np.random.seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)

    r = train_variant(
        name=name + f"_seed{seed}",
        lambda_cubic=lambda_cubic,
        gamma_0=GAMMA_0_FDT,
        fdt_T=T_FDT,
        train_data=train_data,
        val_data=val_data,
        device=device,
    )
    r["seed"] = seed
    r["final_eff_rank"] = float(r["history"]["effective_rank"][-1])
    r["final_uniformity"] = float(r["history"]["uniformity"][-1])
    # Don't carry the full history into summary
    del r["history"]
    return r


def main():
    device = "cuda" if torch.cuda.is_available() else "cpu"
    if device == "cpu":
        print("WARNING: CUDA not available; this test requires GPU.")
        return
    print(f"Using device: {torch.cuda.get_device_name(0)}")
    print(f"Phase 9 wave-3 multi-seed extension of P6.3 (cubic SSM SimSiam)")

    SEEDS = [41, 42, 43, 44]
    t_total = time.time()
    all_results = []

    # Shared train_data and val_data across seeds (variation is in
    # model training trajectory, not in the data).
    train_data = generate_clustered_sequences(8192, D_INPUT, SEQ_LEN, seed=999)
    val_data = generate_clustered_sequences(1024, D_INPUT, SEQ_LEN, seed=1000)

    for seed in SEEDS:
        r_cubic = run_variant_with_seed("cubic_p3", LAMBDA_CUBIC, seed,
                                         train_data, val_data, device)
        all_results.append(r_cubic)
        r_linear = run_variant_with_seed("linear_p3", LAMBDA_LINEAR, seed,
                                          train_data, val_data, device)
        all_results.append(r_linear)

    t_total = time.time() - t_total

    cubic_ranks = [r["final_eff_rank"] for r in all_results if r["name"].startswith("cubic_p3")]
    linear_ranks = [r["final_eff_rank"] for r in all_results if r["name"].startswith("linear_p3")]
    cubic_unif = [r["final_uniformity"] for r in all_results if r["name"].startswith("cubic_p3")]
    linear_unif = [r["final_uniformity"] for r in all_results if r["name"].startswith("linear_p3")]

    print(f"\n{'=' * 70}")
    print(f"  Multi-seed summary (N_seeds = {len(SEEDS)})")
    print(f"{'=' * 70}")
    print(f"  cubic_p3 (Lambda={LAMBDA_CUBIC}):")
    print(f"    final_eff_rank: {np.mean(cubic_ranks):.3f} +/- {np.std(cubic_ranks):.3f}")
    print(f"    final_uniformity: {np.mean(cubic_unif):.4f} +/- {np.std(cubic_unif):.4f}")
    print(f"  linear_p3 (Lambda={LAMBDA_LINEAR}):")
    print(f"    final_eff_rank: {np.mean(linear_ranks):.3f} +/- {np.std(linear_ranks):.3f}")
    print(f"    final_uniformity: {np.mean(linear_unif):.4f} +/- {np.std(linear_unif):.4f}")
    print(f"  Wall time total: {t_total:.1f}s")

    delta_rank = np.mean(cubic_ranks) - np.mean(linear_ranks)
    pooled_std_rank = np.sqrt((np.var(cubic_ranks) + np.var(linear_ranks)) / 2)
    effect_over_noise = delta_rank / pooled_std_rank if pooled_std_rank > 0 else float("inf")
    print(f"\nDelta rank (cubic - linear): {delta_rank:.3f}")
    print(f"Pooled std of rank: {pooled_std_rank:.3f}")
    print(f"Effect / noise: {effect_over_noise:.2f}")

    summary = {
        "prediction": "P6.3 multi-seed extension (Phase 9 wave-3)",
        "n_seeds": len(SEEDS),
        "seeds": SEEDS,
        "wall_time_total_s": t_total,
        "cubic_p3": {
            "Lambda": LAMBDA_CUBIC,
            "final_eff_rank_mean": float(np.mean(cubic_ranks)),
            "final_eff_rank_std": float(np.std(cubic_ranks)),
            "final_uniformity_mean": float(np.mean(cubic_unif)),
            "final_uniformity_std": float(np.std(cubic_unif)),
            "per_seed": [{"seed": r["seed"], "final_eff_rank": r["final_eff_rank"],
                          "final_uniformity": r["final_uniformity"]}
                         for r in all_results if r["name"].startswith("cubic_p3")],
        },
        "linear_p3": {
            "Lambda": LAMBDA_LINEAR,
            "final_eff_rank_mean": float(np.mean(linear_ranks)),
            "final_eff_rank_std": float(np.std(linear_ranks)),
            "final_uniformity_mean": float(np.mean(linear_unif)),
            "final_uniformity_std": float(np.std(linear_unif)),
            "per_seed": [{"seed": r["seed"], "final_eff_rank": r["final_eff_rank"],
                          "final_uniformity": r["final_uniformity"]}
                         for r in all_results if r["name"].startswith("linear_p3")],
        },
        "delta_rank": float(delta_rank),
        "effect_over_noise": float(effect_over_noise),
    }
    with open(OUTPUT_DIR / "summary.json", "w") as f:
        json.dump(summary, f, indent=2)
    print(f"\nSummary written to {OUTPUT_DIR}/summary.json")


if __name__ == "__main__":
    main()
