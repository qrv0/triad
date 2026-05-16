"""WAVE 1 RETRACTED 2026-05-16: this script does not inject FDT-locked
noise; the only stochasticity comes from SGD batch sampling. Per
methodology/02-limits-of-falsification.md, isolation is the abstraction the
work argues against. DO NOT RUN as a test of P6.3 in this form.
See ../../results/12-cubic-ssm-simsiam.md retraction note for context.
A wave-2 redesigned version with FDT-locked noise injection into the SSM
state is required for any methodologically valid test of P6.3.

Test prediction P6.3 (interface 06 state space models).

Prediction: cubic-nonlinearity in SSM state (the structural feature the
Memory-NLS equation adds to the bare diagonal-state SSM) should suppress
representation collapse modes documented in self-supervised learning
(SimSiam without stop-gradient, BYOL without predictor network), without
requiring the architectural tricks those frameworks deploy.

Method: SimSiam-style SSL training of two encoder variants on a synthetic
clustered dataset (small enough for consumer GPU). Both variants use the
SSM-class memory layer; one variant adds cubic state nonlinearity (the
Memory-NLS extension), the other is linear (standard diagonal SSM).
Both trained WITHOUT stop-gradient (the architectural patch that normally
prevents representation collapse in SimSiam).

Measure:
  - Representation-space rank (effective rank via eigenvalue analysis).
  - Alignment-uniformity loss (Wang-Isola 2020).
  - Standard collapse signature: how many representation dimensions collapse
    to near-zero variance.

Hardware: requires PyTorch + CUDA. Wall time: approximately 30-60 minutes
on RTX 4060.

Output: outputs/simsiam_cubic_ssm/

This test does not duplicate any existing experiment.
"""

from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import torch
import torch.nn as nn
import torch.nn.functional as F

REPO_ROOT = Path(__file__).parent.parent.parent
sys.path.insert(0, str(REPO_ROOT))

from implementation.neural.layer import MemoryNLSLayer


OUTPUT_DIR = REPO_ROOT / "outputs" / "simsiam_cubic_ssm"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


# Configuration
D_INPUT = 64           # synthetic feature dimension
D_MODEL = 128
SEQ_LEN = 32
PROJECTION_DIM = 64
PREDICTOR_DIM = 32     # bottleneck in predictor (SimSiam standard)
BATCH_SIZE = 256
N_STEPS = 4000
LR = 1e-3
SEED = 42

# Memory-NLS parameters (cubic variant)
LAMBDA_CUBIC = -0.5     # cubic state nonlinearity (the structural feature being tested)
LAMBDA_LINEAR = 0.0     # baseline: linear state (no cubic nonlinearity)
SIGMA_LAMBDA = 0.3
NU_MIN = 0.5
NU_MAX = 10.0
DT = 0.05


# ----- Synthetic dataset -----

def generate_clustered_sequences(n_samples: int, d_input: int, seq_len: int, n_clusters: int = 16,
                                  noise: float = 0.3, seed: int = SEED) -> torch.Tensor:
    """Generate synthetic clustered sequences.

    Each sample is a sequence of vectors drawn from one of n_clusters Gaussian
    clusters. Within a sequence, all vectors are from the same cluster (with
    added noise). Sequences from different clusters are well-separated.

    Returns: (n_samples, seq_len, d_input).
    """
    rng = torch.Generator().manual_seed(seed)
    # Cluster centers
    centers = torch.randn(n_clusters, d_input, generator=rng) * 3.0
    # Assign each sample to a cluster
    assignments = torch.randint(0, n_clusters, (n_samples,), generator=rng)
    # Build sequences
    seqs = torch.zeros(n_samples, seq_len, d_input)
    for i in range(n_samples):
        center = centers[assignments[i]]
        seqs[i] = center.unsqueeze(0) + noise * torch.randn(seq_len, d_input, generator=rng)
    return seqs


def augment(x: torch.Tensor, noise: float = 0.1) -> torch.Tensor:
    """Simple augmentation: additive Gaussian noise + random temporal shift."""
    B, L, D = x.shape
    x = x + noise * torch.randn_like(x)
    # Random shift by 0..L/4
    shift = torch.randint(0, max(1, L // 4), (1,)).item()
    if shift > 0:
        x = torch.cat([x[:, shift:], x[:, :shift]], dim=1)
    return x


# ----- Model -----

class SimSiamEncoder(nn.Module):
    """SimSiam encoder using Memory-NLS layer with controllable cubic nonlinearity."""

    def __init__(self, d_input: int, d_model: int, n_heads: int = 4,
                 lambda_cubic: float = -0.5, sigma_lambda: float = 0.3,
                 projection_dim: int = 64):
        super().__init__()
        self.input_proj = nn.Linear(d_input, d_model)
        # Memory-NLS layer: cubic nonlinearity controlled by lambda_cubic argument
        self.memnls = MemoryNLSLayer(
            d_model=d_model,
            n_heads=n_heads,
            nonlinearity_strength=lambda_cubic,
            memory_coupling_total=sigma_lambda,
            nu_min=NU_MIN, nu_max=NU_MAX, dt=DT,
            fast_bias=3.0, dissipation=0.0, fdt_temperature=0.0,
        )
        self.norm = nn.LayerNorm(d_model)
        self.projection_head = nn.Sequential(
            nn.Linear(d_model, d_model * 2), nn.ReLU(),
            nn.Linear(d_model * 2, projection_dim),
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """x: (B, L, d_input) -> (B, projection_dim)"""
        h = self.input_proj(x)
        h = h + self.memnls(h)
        h = self.norm(h)
        h = h.mean(dim=1)  # temporal average pool
        z = self.projection_head(h)
        return z


class Predictor(nn.Module):
    """SimSiam predictor head (bottleneck MLP)."""

    def __init__(self, dim: int, hidden: int):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(dim, hidden),
            nn.BatchNorm1d(hidden), nn.ReLU(),
            nn.Linear(hidden, dim),
        )

    def forward(self, z: torch.Tensor) -> torch.Tensor:
        return self.net(z)


def simsiam_loss(p_a: torch.Tensor, z_b: torch.Tensor) -> torch.Tensor:
    """Negative cosine similarity. NO stop-gradient (the key feature being tested).

    Standard SimSiam uses: -F.cosine_similarity(p_a, z_b.detach()).mean()
    Here: NO .detach() — this should normally lead to representation collapse
    unless the architecture has built-in structural protection (the prediction
    being tested for cubic Memory-NLS).
    """
    p_a = F.normalize(p_a, dim=-1)
    z_b = F.normalize(z_b, dim=-1)
    return -(p_a * z_b).sum(dim=-1).mean()


def effective_rank(features: torch.Tensor) -> float:
    """Effective rank (Roy-Vetterli 2007): exp(entropy of normalized eigenvalues)."""
    f = features - features.mean(dim=0, keepdim=True)
    cov = f.T @ f / max(f.shape[0] - 1, 1)
    eigvals = torch.linalg.eigvalsh(cov.float())
    eigvals = eigvals.clamp(min=1e-10)
    normalized = eigvals / eigvals.sum()
    entropy = -(normalized * normalized.log()).sum()
    return float(torch.exp(entropy))


def alignment_uniformity_loss(features: torch.Tensor) -> dict:
    """Wang-Isola (2020) alignment-uniformity decomposition (positive-pairs version).

    Uniformity: log E_{x,y} exp(-2 ||x - y||^2) (lower-is-better, more spread).
    """
    f = F.normalize(features, dim=-1)
    n = f.shape[0]
    sq_dist = torch.cdist(f, f) ** 2  # (n, n)
    mask = ~torch.eye(n, dtype=torch.bool, device=f.device)
    uniformity = torch.log(torch.exp(-2.0 * sq_dist[mask]).mean())
    return {
        "uniformity": float(uniformity),
        "effective_rank": effective_rank(features.detach().cpu()),
    }


def train_variant(name: str, lambda_cubic: float, train_data: torch.Tensor,
                   val_data: torch.Tensor, device: str) -> dict:
    print(f"\n{'=' * 70}")
    print(f"  Variant: {name} (lambda_cubic = {lambda_cubic})")
    print(f"{'=' * 70}")

    encoder = SimSiamEncoder(D_INPUT, D_MODEL, n_heads=4,
                              lambda_cubic=lambda_cubic, sigma_lambda=SIGMA_LAMBDA,
                              projection_dim=PROJECTION_DIM).to(device)
    predictor = Predictor(PROJECTION_DIM, PREDICTOR_DIM).to(device)
    n_params = sum(p.numel() for p in encoder.parameters()) + sum(p.numel() for p in predictor.parameters())
    print(f"  Parameters: {n_params:,}")

    opt = torch.optim.AdamW(list(encoder.parameters()) + list(predictor.parameters()),
                             lr=LR, weight_decay=1e-4)
    n_train = train_data.shape[0]
    history = {"steps": [], "loss": [], "effective_rank": [], "uniformity": []}

    t0 = time.time()
    for step in range(N_STEPS):
        # Random minibatch
        idx = torch.randint(0, n_train, (BATCH_SIZE,))
        x = train_data[idx].to(device)
        # Two augmented views
        x_a = augment(x, noise=0.1)
        x_b = augment(x, noise=0.1)

        z_a = encoder(x_a)
        z_b = encoder(x_b)
        p_a = predictor(z_a)
        p_b = predictor(z_b)

        # NO stop-gradient. This is the key feature being tested.
        loss = 0.5 * (simsiam_loss(p_a, z_b) + simsiam_loss(p_b, z_a))

        opt.zero_grad()
        loss.backward()
        torch.nn.utils.clip_grad_norm_(
            list(encoder.parameters()) + list(predictor.parameters()), max_norm=1.0
        )
        opt.step()

        if step % 100 == 0 or step == N_STEPS - 1:
            encoder.eval()
            with torch.no_grad():
                val_z = encoder(val_data.to(device))
                metrics = alignment_uniformity_loss(val_z)
            encoder.train()
            history["steps"].append(step)
            history["loss"].append(float(loss))
            history["effective_rank"].append(metrics["effective_rank"])
            history["uniformity"].append(metrics["uniformity"])
            print(f"  step {step:>5}: loss = {float(loss):>7.4f}, "
                  f"effective_rank = {metrics['effective_rank']:>6.2f} / {PROJECTION_DIM}, "
                  f"uniformity = {metrics['uniformity']:>7.4f}")

    wall = time.time() - t0
    print(f"  Wall time: {wall:.1f}s")

    return {
        "name": name,
        "lambda_cubic": lambda_cubic,
        "n_params": n_params,
        "history": history,
        "wall_time": wall,
    }


def main():
    device = "cuda" if torch.cuda.is_available() else "cpu"
    if device == "cpu":
        print("WARNING: CUDA not available; this test requires GPU.")
        return

    print(f"Phase 9 Test D: cubic-state SimSiam without stop-gradient (P6.3)")
    print(f"Using device: {torch.cuda.get_device_name(0)}")

    torch.manual_seed(SEED)
    print(f"\nGenerating synthetic clustered dataset...")
    train_data = generate_clustered_sequences(n_samples=8192, d_input=D_INPUT, seq_len=SEQ_LEN)
    val_data = generate_clustered_sequences(n_samples=1024, d_input=D_INPUT, seq_len=SEQ_LEN, seed=SEED + 1)
    print(f"  train shape: {train_data.shape}")
    print(f"  val shape: {val_data.shape}")

    t_total = time.time()

    variant_cubic = train_variant("cubic", LAMBDA_CUBIC, train_data, val_data, device)
    variant_linear = train_variant("linear", LAMBDA_LINEAR, train_data, val_data, device)

    t_total = time.time() - t_total

    print(f"\n{'=' * 70}")
    print(f"  Comparison summary")
    print(f"{'=' * 70}")
    print(f"  Variant cubic (Lambda = {LAMBDA_CUBIC}):")
    print(f"    Final effective rank: {variant_cubic['history']['effective_rank'][-1]:.2f}")
    print(f"    Final uniformity: {variant_cubic['history']['uniformity'][-1]:.4f}")
    print(f"  Variant linear (Lambda = {LAMBDA_LINEAR}):")
    print(f"    Final effective rank: {variant_linear['history']['effective_rank'][-1]:.2f}")
    print(f"    Final uniformity: {variant_linear['history']['uniformity'][-1]:.4f}")
    print(f"  Wall time total: {t_total:.1f}s")
    print()
    print(f"Prediction P6.3 check: cubic variant should maintain higher effective rank")
    print(f"  (less representation collapse) than linear variant when trained")
    print(f"  WITHOUT stop-gradient. Both should be compared to the standard SimSiam")
    print(f"  with stop-gradient which is known to maintain high rank.")

    summary = {
        "prediction": "P6.3 (interface 06)",
        "variants": [variant_cubic, variant_linear],
        "wall_time_total_s": t_total,
    }
    with open(OUTPUT_DIR / "summary.json", "w") as f:
        json.dump(summary, f, indent=2)
    print(f"\nSummary written to {OUTPUT_DIR}/summary.json")


if __name__ == "__main__":
    main()
