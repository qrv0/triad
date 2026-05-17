"""Phase 9 wave-3 multi-seed extension of test_fdt_locked_noise.py.

Runs P6.1 (FDT-locked noise reduces training trajectory variance) across
4 seeds for each of the two variants (fdt_high, fdt_low) to get variance
estimates on the small effect observed in the single-seed Phase C run
(val_loss_std 0.0952 vs 0.0995).

Each seed runs the same fdt_high and fdt_low configuration, computes
val_loss trajectory standard deviation, and the script aggregates
mean+/-std across seeds.

Total wall: 4 seeds * 2 variants * 2 min/run = ~16 min on RTX 4060.

Output: outputs/fdt_locked_noise_multiseed/summary.json.
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

from experiments.neural.test_fdt_locked_noise import (
    download_tinyshakespeare, prepare_data, make_model, make_batch_fn,
    trajectory_variance, TRAIN_CFG_TEMPLATE, SEQ_LEN,
    GAMMA_0_FDT_HIGH, T_FDT_HIGH, GAMMA_0_FDT_LOW, T_FDT_LOW,
)
from implementation.neural.training import train


OUTPUT_DIR = REPO_ROOT / "outputs" / "fdt_locked_noise_multiseed"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def run_variant_with_seed(name: str, gamma_0: float, fdt_T: float, seed: int,
                          train_data, val_data, vocab_size: int, device: str) -> dict:
    print(f"\n--- Variant: {name}, seed: {seed} (gamma_0={gamma_0}, T={fdt_T}) ---")

    cfg = TRAIN_CFG_TEMPLATE
    cfg.output_dir = str(OUTPUT_DIR / f"{name}_seed{seed}")
    cfg.seed = seed

    torch.manual_seed(seed)
    np.random.seed(seed)
    torch.cuda.manual_seed_all(seed)

    model = make_model(vocab_size, gamma_0, fdt_T)
    n_params = sum(p.numel() for p in model.parameters())
    print(f"  Parameters: {n_params:,}")

    get_train = make_batch_fn(train_data, SEQ_LEN, cfg.batch_size)
    get_eval = make_batch_fn(val_data, SEQ_LEN, cfg.batch_size)
    history = train(model, get_train, get_eval, cfg, device=device)

    variance = trajectory_variance(history)
    final_val_ppl = float(torch.exp(torch.tensor(history["val_loss"][-1])))

    return {
        "name": name, "seed": seed,
        "gamma_0": gamma_0, "fdt_temperature": fdt_T,
        "n_params": n_params, "final_val_ppl": final_val_ppl,
        "trajectory_variance": variance,
    }


def main():
    device = "cuda" if torch.cuda.is_available() else "cpu"
    if device == "cpu":
        print("WARNING: CUDA not available; this test requires GPU.")
        return
    print(f"Using device: {torch.cuda.get_device_name(0)}")
    print(f"Phase 9 wave-3 multi-seed extension of P6.1 (FDT-locked noise)")

    text = download_tinyshakespeare()
    train_data, val_data, tokenizer = prepare_data(text)
    print(f"  vocab size: {tokenizer.vocab_size}")
    print(f"  train tokens: {len(train_data):,}  val tokens: {len(val_data):,}")

    SEEDS = [41, 42, 43, 44]
    t_total = time.time()
    all_results = []

    for seed in SEEDS:
        r_high = run_variant_with_seed("fdt_high", GAMMA_0_FDT_HIGH, T_FDT_HIGH,
                                        seed, train_data, val_data,
                                        tokenizer.vocab_size, device)
        all_results.append(r_high)
        r_low = run_variant_with_seed("fdt_low", GAMMA_0_FDT_LOW, T_FDT_LOW,
                                       seed, train_data, val_data,
                                       tokenizer.vocab_size, device)
        all_results.append(r_low)

    t_total = time.time() - t_total

    high_stds = [r["trajectory_variance"]["val_loss_std"] for r in all_results if r["name"] == "fdt_high"]
    low_stds = [r["trajectory_variance"]["val_loss_std"] for r in all_results if r["name"] == "fdt_low"]
    high_spikes = [r["trajectory_variance"]["spike_count"] for r in all_results if r["name"] == "fdt_high"]
    low_spikes = [r["trajectory_variance"]["spike_count"] for r in all_results if r["name"] == "fdt_low"]
    high_ppl = [r["final_val_ppl"] for r in all_results if r["name"] == "fdt_high"]
    low_ppl = [r["final_val_ppl"] for r in all_results if r["name"] == "fdt_low"]

    print(f"\n{'=' * 70}")
    print(f"  Multi-seed summary (N_seeds = {len(SEEDS)})")
    print(f"{'=' * 70}")
    print(f"  fdt_high (gamma_0={GAMMA_0_FDT_HIGH}):")
    print(f"    val_loss_std:    {np.mean(high_stds):.4f} +/- {np.std(high_stds):.4f}")
    print(f"    spike_count:     {np.mean(high_spikes):.2f} +/- {np.std(high_spikes):.2f}")
    print(f"    final_val_ppl:   {np.mean(high_ppl):.4f} +/- {np.std(high_ppl):.4f}")
    print(f"  fdt_low (gamma_0={GAMMA_0_FDT_LOW}):")
    print(f"    val_loss_std:    {np.mean(low_stds):.4f} +/- {np.std(low_stds):.4f}")
    print(f"    spike_count:     {np.mean(low_spikes):.2f} +/- {np.std(low_spikes):.2f}")
    print(f"    final_val_ppl:   {np.mean(low_ppl):.4f} +/- {np.std(low_ppl):.4f}")
    print(f"  Wall time total: {t_total:.1f}s")
    print(f"\nDelta std (fdt_low - fdt_high): {np.mean(low_stds) - np.mean(high_stds):.4f}")
    print(f"Pooled std of std: {np.sqrt((np.var(high_stds) + np.var(low_stds))/2):.4f}")
    print(f"Effect/noise ratio: {(np.mean(low_stds) - np.mean(high_stds)) / np.sqrt((np.var(high_stds) + np.var(low_stds))/2):.2f}")

    summary = {
        "prediction": "P6.1 multi-seed extension (Phase 9 wave-3)",
        "n_seeds": len(SEEDS),
        "seeds": SEEDS,
        "wall_time_total_s": t_total,
        "fdt_high": {
            "gamma_0": GAMMA_0_FDT_HIGH, "fdt_temperature": T_FDT_HIGH,
            "val_loss_std_mean": float(np.mean(high_stds)),
            "val_loss_std_std": float(np.std(high_stds)),
            "spike_count_mean": float(np.mean(high_spikes)),
            "final_val_ppl_mean": float(np.mean(high_ppl)),
            "final_val_ppl_std": float(np.std(high_ppl)),
            "per_seed": [{"seed": r["seed"], "val_loss_std": r["trajectory_variance"]["val_loss_std"],
                          "spike_count": r["trajectory_variance"]["spike_count"],
                          "final_val_ppl": r["final_val_ppl"]}
                         for r in all_results if r["name"] == "fdt_high"],
        },
        "fdt_low": {
            "gamma_0": GAMMA_0_FDT_LOW, "fdt_temperature": T_FDT_LOW,
            "val_loss_std_mean": float(np.mean(low_stds)),
            "val_loss_std_std": float(np.std(low_stds)),
            "spike_count_mean": float(np.mean(low_spikes)),
            "final_val_ppl_mean": float(np.mean(low_ppl)),
            "final_val_ppl_std": float(np.std(low_ppl)),
            "per_seed": [{"seed": r["seed"], "val_loss_std": r["trajectory_variance"]["val_loss_std"],
                          "spike_count": r["trajectory_variance"]["spike_count"],
                          "final_val_ppl": r["final_val_ppl"]}
                         for r in all_results if r["name"] == "fdt_low"],
        },
        "delta_std": float(np.mean(low_stds) - np.mean(high_stds)),
        "effect_over_noise": float((np.mean(low_stds) - np.mean(high_stds)) / np.sqrt((np.var(high_stds) + np.var(low_stds))/2)),
    }
    with open(OUTPUT_DIR / "summary.json", "w") as f:
        json.dump(summary, f, indent=2)
    print(f"\nSummary written to {OUTPUT_DIR}/summary.json")


if __name__ == "__main__":
    main()
