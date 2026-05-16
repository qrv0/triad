"""Test prediction P6.1 (interface 06 state space models).

Prediction: a nonlinear SSM (cubic state nonlinearity) with FDT-locked
stochastic forcing in the optimization should exhibit smoother optimization-
trajectory characteristics than the same architecture without FDT-locked
noise (or with empirically-tuned noise unrelated to the FDT correlator).

Method: train two Memory-NLS language-model variants on TinyShakespeare
with identical architecture and training infrastructure, differing only in
the FDT-locking of the structural noise:

  Variant A: dissipation = gamma_0 > 0, fdt_temperature = T_FDT > 0
             (built-in FDT-locked noise via implementation/neural/layer.py).
  Variant B: dissipation = 0, fdt_temperature = 0
             (no built-in noise; training stochasticity comes only from
             SGD batches and dropout, not from FDT correlator).

Compare:
  - Training-trajectory variance (std of val loss across windows).
  - Incidence of loss spikes (count of val-loss increases above threshold).
  - Final val perplexity (should NOT be the primary criterion; per CLAUDE.md
    Rule 7a, this is differentiation not competition; reported for completeness).

This test does NOT duplicate the existing scale_up_dynamics.py (70M scale)
or long_training_dynamics.py (50k steps). It runs at 1.5M scale, 8000 steps,
two variants only.

Hardware: requires PyTorch + CUDA. Wall time: approximately 30-40 minutes
on RTX 4060 (2 x 15-20 min runs).

Output: outputs/fdt_locked_noise/
"""

from __future__ import annotations

import json
import sys
import time
import urllib.request
from pathlib import Path

import torch

REPO_ROOT = Path(__file__).parent.parent.parent
sys.path.insert(0, str(REPO_ROOT))

from implementation.neural import (
    MemoryNLSConfig, MemoryNLSLanguageModel,
    TrainConfig, train,
    CharTokenizer, generate_text,
)


DATA_PATH = REPO_ROOT / "experiments" / "neural" / "tinyshakespeare.txt"
OUTPUT_DIR = REPO_ROOT / "outputs" / "fdt_locked_noise"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


# Common architecture parameters
D_MODEL = 192
N_LAYERS = 4
N_HEADS = 4
SEQ_LEN = 256
LAMBDA = -0.5
SIGMA_LAMBDA = 0.3
NU_MIN = 0.5
NU_MAX = 10.0
DT = 0.05
FAST_BIAS = 3.0

# Variant A: FDT-locked noise (moderate coupling)
GAMMA_0_FDT_HIGH = 0.02
T_FDT_HIGH = 0.01

# Variant B: FDT-locked noise (weak coupling)
GAMMA_0_FDT_LOW = 0.005
T_FDT_LOW = 0.01

# The isolated variant (gamma_0 = 0, T = 0) that the original draft
# included as "for comparison only" has been removed per principles/
# 03-coupling.md (Rule A in the structural-research-mode skill).
# Isolation is not a configuration the methodology permits, even as
# a comparison case; see docs/llm-hedge-annotations.md for the
# revision rationale.

# Training: 8000 steps at 1.5M params (small enough to cycle two variants)
TRAIN_CFG_TEMPLATE = TrainConfig(
    n_steps=8000,
    batch_size=32,
    learning_rate=3e-4,
    min_learning_rate=3e-5,
    warmup_steps=200,
    grad_clip_norm=1.0,
    eval_interval=200,
    eval_iters=16,
    log_interval=200,
    checkpoint_interval=4000,
    use_amp=True,
    amp_dtype="bfloat16",
    seed=42,
)


def download_tinyshakespeare() -> str:
    if DATA_PATH.exists():
        return DATA_PATH.read_text()
    text = urllib.request.urlopen(
        "https://raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/input.txt"
    ).read().decode("utf-8")
    DATA_PATH.write_text(text)
    return text


def prepare_data(text: str):
    tokenizer = CharTokenizer(text)
    data = torch.tensor(tokenizer.encode(text), dtype=torch.long)
    n_train = int(0.9 * len(data))
    return data[:n_train], data[n_train:], tokenizer


def make_batch_fn(data: torch.Tensor, seq_len: int, batch_size: int):
    def get_batch():
        ix = torch.randint(0, len(data) - seq_len - 1, (batch_size,))
        x = torch.stack([data[i : i + seq_len] for i in ix])
        y = torch.stack([data[i + 1 : i + 1 + seq_len] for i in ix])
        return x, y
    return get_batch


def make_model(vocab_size: int, gamma_0: float, fdt_T: float) -> MemoryNLSLanguageModel:
    cfg = MemoryNLSConfig(
        vocab_size=vocab_size,
        d_model=D_MODEL,
        n_layers=N_LAYERS,
        n_heads=N_HEADS,
        ffn_mult=4,
        max_seq_len=SEQ_LEN,
        use_positional=False,
        nonlinearity_strength=LAMBDA,
        memory_coupling_total=SIGMA_LAMBDA,
        nu_min=NU_MIN, nu_max=NU_MAX, dt=DT,
        fast_bias=FAST_BIAS,
        dissipation=gamma_0,
        fdt_temperature=fdt_T,
    )
    return MemoryNLSLanguageModel(cfg)


def trajectory_variance(history: dict) -> dict:
    """Compute training-trajectory variance metrics.

    Returns:
        dict with:
        - val_loss_std: std across val checkpoints
        - max_loss_jump: largest single-step val loss increase
        - spike_count: count of val loss increases above 0.1 in absolute value
    """
    val_losses = history["val_loss"]
    if len(val_losses) < 3:
        return {"val_loss_std": float("nan"), "max_loss_jump": float("nan"), "spike_count": 0}

    val_losses_t = torch.tensor(val_losses)
    diffs = val_losses_t[1:] - val_losses_t[:-1]
    return {
        "val_loss_std": float(val_losses_t.std()),
        "max_loss_jump": float(diffs.max()),
        "spike_count": int((diffs > 0.1).sum()),
    }


def run_variant(name: str, gamma_0: float, fdt_T: float, train_data, val_data, vocab_size: int,
                device: str) -> dict:
    print(f"\n{'=' * 70}")
    print(f"  Variant: {name}")
    print(f"  gamma_0 = {gamma_0}, fdt_temperature = {fdt_T}")
    print(f"{'=' * 70}")

    cfg = TRAIN_CFG_TEMPLATE
    cfg.output_dir = str(OUTPUT_DIR / name)
    model = make_model(vocab_size, gamma_0, fdt_T)
    n_params = sum(p.numel() for p in model.parameters())
    print(f"  Parameters: {n_params:,}")

    get_train = make_batch_fn(train_data, SEQ_LEN, cfg.batch_size)
    get_eval = make_batch_fn(val_data, SEQ_LEN, cfg.batch_size)
    history = train(model, get_train, get_eval, cfg, device=device)

    variance = trajectory_variance(history)
    final_val_ppl = float(torch.exp(torch.tensor(history["val_loss"][-1])))

    return {
        "name": name,
        "gamma_0": gamma_0,
        "fdt_temperature": fdt_T,
        "n_params": n_params,
        "final_val_ppl": final_val_ppl,
        "trajectory_variance": variance,
        "history": history,
    }


def main():
    device = "cuda" if torch.cuda.is_available() else "cpu"
    if device == "cpu":
        print("WARNING: CUDA not available; this test requires GPU.")
        return

    print(f"Using device: {torch.cuda.get_device_name(0)}")
    print(f"Phase 9 Test C: FDT-locked vs no-built-in noise (P6.1)")

    text = download_tinyshakespeare()
    train_data, val_data, tokenizer = prepare_data(text)
    print(f"  vocab size: {tokenizer.vocab_size}")
    print(f"  train tokens: {len(train_data):,}  val tokens: {len(val_data):,}")

    t_total = time.time()

    variant_A = run_variant("fdt_high", GAMMA_0_FDT_HIGH, T_FDT_HIGH,
                              train_data, val_data, tokenizer.vocab_size, device)
    variant_B = run_variant("fdt_low", GAMMA_0_FDT_LOW, T_FDT_LOW,
                              train_data, val_data, tokenizer.vocab_size, device)

    t_total = time.time() - t_total

    print(f"\n{'=' * 70}")
    print(f"  Comparison summary")
    print(f"{'=' * 70}")
    for label, v in [("A (FDT high)", variant_A), ("B (FDT low)", variant_B)]:
        print(f"  Variant {label} (gamma_0={v['gamma_0']}, T={v['fdt_temperature']}):")
        print(f"    Final val ppl: {v['final_val_ppl']:.4f}")
        print(f"    Val loss std: {v['trajectory_variance']['val_loss_std']:.4f}")
        print(f"    Max loss jump: {v['trajectory_variance']['max_loss_jump']:.4f}")
        print(f"    Spike count: {v['trajectory_variance']['spike_count']}")
    print(f"  Wall time total: {t_total:.1f}s")
    print()
    print(f"Prediction P6.1 check: trajectory variance should DECREASE as")
    print(f"  gamma_0 grows in the coupled regime (fdt_low > fdt_high).")
    print(f"  Both variants run with gamma_0 > 0 per principles/03-coupling.md.")

    # Write summary
    variants = [variant_A, variant_B]
    summary = {
        "prediction": "P6.1 (interface 06), with 3-variant sweep across P3 coupling",
        "variants": variants,
        "wall_time_total_s": t_total,
    }
    with open(OUTPUT_DIR / "summary.json", "w") as f:
        # history is large; truncate to summary points for the JSON
        def trim_history(v):
            v = dict(v)
            if "history" in v:
                v["history"] = {k: vv for k, vv in v["history"].items() if k != "samples_during_training"}
            return v
        summary_trim = {**summary, "variants": [trim_history(v) for v in variants]}
        json.dump(summary_trim, f, indent=2)
    print(f"\nSummary written to {OUTPUT_DIR}/summary.json")


if __name__ == "__main__":
    main()
