# Neural sequence layer

This folder contains the instantiation of the Memory-NLS equation as a neural sequence layer. The mathematical equivalence between the equation's auxiliary-field memory and the diagonal-state structured state space model used in S4, S5, Mamba, and RWKV is documented in [`../../interfaces/06-state-space-models.md`](../../interfaces/06-state-space-models.md). The files here are the concrete realization of that equivalence in PyTorch, plus a small autoregressive language model built on top of it.

> **A note on framing.** This is one instantiation of the equation, alongside the physics solver, the cosmological correspondence (BAO), the cymatic correspondence, the neurobiological correspondence (gamma entrainment), and the archaeoacoustic correspondence. The fact that the same equation has a coherent neural-network instantiation is evidence for the structural-realist claim that the equation captures a pattern that appears across substrates. It is not a competitive benchmark project against attention-based architectures. See [`../../CLAUDE.md`](../../CLAUDE.md) for the methodological constraints.

## Files

| File | Content |
|---|---|
| `layer.py` | `MemoryNLSLayer` — the sequence layer. FFT-convolution implementation of the auxiliary-field recurrence (O(N log N) per call). |
| `model.py` | `MemoryNLSLanguageModel` — full autoregressive LM (embedding + stack of MemNLS blocks + tied output head). |
| `baselines.py` | `TransformerLanguageModel` — same-architecture-shape causal-attention LM, for verifying training infrastructure (not a competitive comparison). |
| `training.py` | Training infrastructure (AdamW + cosine schedule + gradient clipping + AMP). |
| `generation.py` | Char-level tokenizer and autoregressive sampling helpers. |

## What the layer instantiates

The Memory-NLS equation, derived in [`../../equation/01-derivation.md`](../../equation/01-derivation.md), updates a set of auxiliary memory fields $y_j$ according to

$$
\partial_t y_j = \nu_j (\rho - y_j) ,
$$

where $\rho$ is the local density of the underlying complex field. The same equation appears, written in a different notation but governing the same mathematical object, as the diagonal-state SSM update:

$$
\partial_t \mathbf{h}_j = -\nu_j \mathbf{h}_j + \nu_j u .
$$

The auxiliary fields $y_j$ of the physics formulation and the hidden state components $\mathbf{h}_j$ of an SSM are the same object. In `layer.py` they are implemented as a finite number of memory modes, with the linear recurrence evaluated via FFT-based causal convolution.

The full layer extends the linear baseline with the cubic self-interaction $\Lambda |\Psi|^2 \Psi$ (P2 instantaneous part), the multi-mode coupling $V_\text{mem} = \sum_j \lambda_j y_j$, and optional FDT-locked stochastic forcing ($\gamma_0, T$). The parameters carry physical meaning derived from the principles:

- $\Lambda$ — strength and sign of the cubic self-interaction.
- $\Sigma\lambda$ — total memory coupling.
- $\nu_\text{min}, \nu_\text{max}$ — spectrum of relaxation timescales.
- fast_bias — partition of $\lambda$ between fast and slow memory modes.
- $\gamma_0, T$ — dissipation rate and bath temperature for the FDT noise.

These are not hyperparameters tuned for benchmark scores; they are the structural parameters of the equation, the same ones that appear in the 2D and 3D physics solver.

## Usage

```python
import torch
from implementation.neural import MemoryNLSLayer

layer = MemoryNLSLayer(
    d_model=192,
    n_heads=4,                          # number of memory modes
    nonlinearity_strength=-0.5,         # Lambda
    memory_coupling_total=0.3,          # Sigma_lambda
    nu_min=0.5, nu_max=10.0, dt=0.05,
    fast_bias=3.0,
)

x = torch.randn(4, 256, 192)           # (batch, length, d_model)
y = layer(x)                            # same shape, residual-updated
```

For a full autoregressive language model:

```python
from implementation.neural import MemoryNLSConfig, MemoryNLSLanguageModel

cfg = MemoryNLSConfig(
    vocab_size=65, d_model=192, n_layers=4, n_heads=4,
    nonlinearity_strength=-0.5, memory_coupling_total=0.3,
)
model = MemoryNLSLanguageModel(cfg)
```

## What this folder is

A working PyTorch instantiation of the Memory-NLS equation as a sequence-modeling primitive. The layer trains, produces coherent output, and instantiates in code the structural correspondence documented in [`../../interfaces/06-state-space-models.md`](../../interfaces/06-state-space-models.md). The TinyShakespeare training experiment in [`../../experiments/neural/`](../../experiments/neural/) verifies this end-to-end; the report is at [`../../outputs/tinyshakespeare/training_results.md`](../../outputs/tinyshakespeare/training_results.md) after the training script runs.

## What this folder is not

A competitive benchmark project. There is no "roadmap to beat Mamba on Long Range Arena" because that framing does not belong here. The work is not optimizing toward a leaderboard metric; the work is documenting what the structure produces. See [`../../CLAUDE.md`](../../CLAUDE.md), section "Intelligence-as-structure, not intelligence-as-scale" for the reasoning.

## Dependencies

- `torch >= 2.0`

Install via the optional extra in `pyproject.toml`:

```bash
pip install -e ".[neural]"
```
