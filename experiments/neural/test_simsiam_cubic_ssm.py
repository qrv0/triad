"""Wave-2 test: cubic-state SimSiam without stop-gradient, with FDT-locked
noise injection (P3 active).

Targets prediction P6.3 (interface 06 state space models), redesigned to
respect P3 per the post-retraction methodology.

Wave 1 was retracted (commit c11666b) for not injecting FDT-locked noise
(only SGD stochasticity, which is not the same as the equation's P3 bath).
This wave-2 redesign adds explicit FDT-correlated noise to the SSM state
at each forward pass, structurally matching the equation's P3 instantiation.

Three variants compared, all trained WITHOUT stop-gradient in SimSiam loss:
  A. cubic_p3:    Lambda<0 (cubic state nonlinearity) + FDT-locked noise
  B. linear_p3:   Lambda=0 (linear state) + FDT-locked noise
  C. cubic_iso:   Lambda<0 + no FDT noise (degenerate isolated, for comparison)

The structural prediction P6.3 is that cubic-state SSM with P3 active
maintains higher representation rank than linear-state SSM with P3
active. The isolated variant C is included as the degenerate limit
to make explicit what the wave-1 (incorrect) test was testing.

Hardware: requires PyTorch + CUDA. Wall time: ~30-60 min on RTX 4060.

Output: outputs/simsiam_cubic_ssm_p3/
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


OUTPUT_DIR = REPO_ROOT / "outputs" / "simsiam_cubic_ssm_p3"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


# Config
D_INPUT = 64
D_MODEL = 128
SEQ_LEN = 32
PROJECTION_DIM = 64
PREDICTOR_DIM = 32
BATCH_SIZE = 256
N_STEPS = 4000
LR = 1e-3
SEED = 42

# Memory-NLS structural parameters
LAMBDA_CUBIC = -0.5
LAMBDA_LINEAR = 0.0
SIGMA_LAMBDA = 0.3
NU_MIN = 0.5
NU_MAX = 10.0
DT = 0.05

# P3 parameters
GAMMA_0_FDT = 0.02
T_FDT = 0.01
GAMMA_0_ISO = 0.0
T_ISO = 0.0


def generate_clustered_sequences(n_samples: int, d_input: int, seq_len: int,
                                  n_clusters: int = 16, noise: float = 0.3, seed: int = SEED) -> torch.Tensor:
    rng = torch.Generator().manual_seed(seed)
    centers = torch.randn(n_clusters, d_input, generator=rng) * 3.0
    assignments = torch.randint(0, n_clusters, (n_samples,), generator=rng)
    seqs = torch.zeros(n_samples, seq_len, d_input)
    for i in range(n_samples):
        center = centers[assignments[i]]
        seqs[i] = center.unsqueeze(0) + noise * torch.randn(seq_len, d_input, generator=rng)
    return seqs


def augment(x: torch.Tensor, noise: float = 0.1) -> torch.Tensor:
    B, L, D = x.shape
    x = x + noise * torch.randn_like(x)
    shift = torch.randint(0, max(1, L // 4), (1,)).item()
    if shift > 0:
        x = torch.cat([x[:, shift:], x[:, :shift]], dim=1)
    return x


class SimSiamEncoder(nn.Module):
    def __init__(self, d_input: int, d_model: int, n_heads: int = 4,
                 lambda_cubic: float = -0.5, sigma_lambda: float = 0.3,
                 gamma_0: float = 0.0, fdt_T: float = 0.0,
                 projection_dim: int = 64):
        super().__init__()
        self.input_proj = nn.Linear(d_input, d_model)
        self.memnls = MemoryNLSLayer(
            d_model=d_model, n_heads=n_heads,
            nonlinearity_strength=lambda_cubic,
            memory_coupling_total=sigma_lambda,
            nu_min=NU_MIN, nu_max=NU_MAX, dt=DT, fast_bias=3.0,
            dissipation=gamma_0, fdt_temperature=fdt_T,
        )
        self.norm = nn.LayerNorm(d_model)
        self.projection_head = nn.Sequential(
            nn.Linear(d_model, d_model * 2), nn.ReLU(),
            nn.Linear(d_model * 2, projection_dim),
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        h = self.input_proj(x)
        h = h + self.memnls(h)
        h = self.norm(h)
        h = h.mean(dim=1)
        z = self.projection_head(h)
        return z


class Predictor(nn.Module):
    def __init__(self, dim: int, hidden: int):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(dim, hidden), nn.BatchNorm1d(hidden), nn.ReLU(),
            nn.Linear(hidden, dim),
        )

    def forward(self, z):
        return self.net(z)


def simsiam_loss(p_a, z_b):
    """Negative cosine similarity. NO stop-gradient (key feature)."""
    p_a = F.normalize(p_a, dim=-1)
    z_b = F.normalize(z_b, dim=-1)
    return -(p_a * z_b).sum(dim=-1).mean()


def effective_rank(features: torch.Tensor) -> float:
    f = features - features.mean(dim=0, keepdim=True)
    cov = f.T @ f / max(f.shape[0] - 1, 1)
    eigvals = torch.linalg.eigvalsh(cov.float())
    eigvals = eigvals.clamp(min=1e-10)
    normalized = eigvals / eigvals.sum()
    entropy = -(normalized * normalized.log()).sum()
    return float(torch.exp(entropy))


def alignment_uniformity(features: torch.Tensor) -> dict:
    f = F.normalize(features, dim=-1)
    n = f.shape[0]
    sq_dist = torch.cdist(f, f) ** 2
    mask = ~torch.eye(n, dtype=torch.bool, device=f.device)
    uniformity = torch.log(torch.exp(-2.0 * sq_dist[mask]).mean())
    return {"uniformity": float(uniformity),
            "effective_rank": effective_rank(features.detach().cpu())}


def train_variant(name: str, lambda_cubic: float, gamma_0: float, fdt_T: float,
                   train_data: torch.Tensor, val_data: torch.Tensor, device: str) -> dict:
    print(f"\n{'='*70}")
    print(f"  Variant: {name} (Lambda={lambda_cubic}, gamma_0={gamma_0}, T={fdt_T})")
    print(f"{'='*70}")

    encoder = SimSiamEncoder(D_INPUT, D_MODEL, n_heads=4,
                              lambda_cubic=lambda_cubic, sigma_lambda=SIGMA_LAMBDA,
                              gamma_0=gamma_0, fdt_T=fdt_T,
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
        idx = torch.randint(0, n_train, (BATCH_SIZE,))
        x = train_data[idx].to(device)
        x_a = augment(x, noise=0.1)
        x_b = augment(x, noise=0.1)

        z_a = encoder(x_a)
        z_b = encoder(x_b)
        p_a = predictor(z_a)
        p_b = predictor(z_b)
        loss = 0.5 * (simsiam_loss(p_a, z_b) + simsiam_loss(p_b, z_a))

        opt.zero_grad()
        loss.backward()
        torch.nn.utils.clip_grad_norm_(
            list(encoder.parameters()) + list(predictor.parameters()), max_norm=1.0)
        opt.step()

        if step % 100 == 0 or step == N_STEPS - 1:
            encoder.eval()
            with torch.no_grad():
                val_z = encoder(val_data.to(device))
                metrics = alignment_uniformity(val_z)
            encoder.train()
            history["steps"].append(step)
            history["loss"].append(float(loss))
            history["effective_rank"].append(metrics["effective_rank"])
            history["uniformity"].append(metrics["uniformity"])
            print(f"  step {step:>5}: loss={float(loss):>7.4f}  "
                  f"eff_rank={metrics['effective_rank']:>6.2f}/{PROJECTION_DIM}  "
                  f"uniformity={metrics['uniformity']:>7.4f}")

    wall = time.time() - t0
    print(f"  Wall: {wall:.1f}s")
    return {"name": name, "lambda_cubic": lambda_cubic, "gamma_0": gamma_0,
            "fdt_T": fdt_T, "n_params": n_params, "history": history, "wall_time": wall}


def main():
    device = "cuda" if torch.cuda.is_available() else "cpu"
    if device == "cpu":
        print("WARNING: CUDA not available; this test requires GPU.")
        return
    print(f"Wave 2 Test D: cubic-state SimSiam without stop-gradient, with FDT noise (P6.3)")
    print(f"Using device: {torch.cuda.get_device_name(0)}")

    torch.manual_seed(SEED)
    train_data = generate_clustered_sequences(8192, D_INPUT, SEQ_LEN)
    val_data = generate_clustered_sequences(1024, D_INPUT, SEQ_LEN, seed=SEED+1)

    t_total = time.time()
    variants = []
    # A: cubic + P3 active
    variants.append(train_variant("cubic_p3", LAMBDA_CUBIC, GAMMA_0_FDT, T_FDT,
                                   train_data, val_data, device))
    # B: linear + P3 active
    variants.append(train_variant("linear_p3", LAMBDA_LINEAR, GAMMA_0_FDT, T_FDT,
                                   train_data, val_data, device))
    # C: cubic + isolated (degenerate; for comparison)
    variants.append(train_variant("cubic_iso", LAMBDA_CUBIC, GAMMA_0_ISO, T_ISO,
                                   train_data, val_data, device))
    t_total = time.time() - t_total

    print(f"\n{'='*70}\n  Comparison summary\n{'='*70}")
    for v in variants:
        print(f"  {v['name']:>10}: final eff_rank = {v['history']['effective_rank'][-1]:.2f}, "
              f"final uniformity = {v['history']['uniformity'][-1]:.4f}, "
              f"wall = {v['wall_time']:.1f}s")
    print(f"  Total wall: {t_total:.1f}s")

    print(f"\nPrediction P6.3 (with P3 active) check: cubic_p3 should maintain higher")
    print(f"  effective rank than linear_p3. cubic_iso shows what the wave-1 (degenerate) ran.")

    summary = {
        "prediction": "P6.3 (interface 06), wave 2 with FDT noise injection",
        "variants": variants,
        "wall_time_total_s": t_total,
    }
    with open(OUTPUT_DIR / "summary.json", "w") as f:
        json.dump(summary, f, indent=2)
    print(f"\nSummary: {OUTPUT_DIR}/summary.json")


if __name__ == "__main__":
    main()
