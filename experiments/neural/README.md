# Neural experiments

This folder contains the experiments that instantiate the Memory-NLS equation as a neural sequence model and verify what the instantiation produces.

| Script | What it does |
|---|---|
| `train_tinyshakespeare.py` | Trains Memory-NLS on TinyShakespeare (1.5M params). Primary small-scale experiment. ~45s on RTX 4060. |
| `compare_architectures.py` | Trains Memory-NLS and Transformer side by side at 1.5M on TinyShakespeare. Framed as differentiation, not competition. ~90s. |
| `long_training_dynamics.py` | Extends both architectures to 50,000 steps at 1.5M to study post-transient regime. ~17 minutes. |
| `scale_up_dynamics.py` | Scales both architectures to 70M parameters on enwik8 (100MB byte-level). The structural difference becomes empirically dramatic at this scale: Memory-NLS plateaus monotonically; Transformer exhibits catastrophic optimization collapse. ~6.3 hours on RTX 4060. |
| `verify_training_infra.py` | Trains a small Transformer in isolation to confirm the training loop infrastructure works on a model known to train. |

## Why these experiments exist

The Memory-NLS equation has six independently documented instantiations (see [`../../interfaces/`](../../interfaces/)). One of them is as a neural sequence layer ([`../../interfaces/06-state-space-models.md`](../../interfaces/06-state-space-models.md)). The mathematical equivalence between the equation's auxiliary-field memory $\partial_t y_j = \nu_j(\rho - y_j)$ and the diagonal-state SSM update is exact and does not require dimensional calibration.

`train_tinyshakespeare.py` verifies in working code that this equivalence is not merely formal. The same equation, the same parameters with the same physical meaning ($\Lambda, \Sigma\lambda, \nu_j$, FDT temperature), instantiated in a neural-network substrate, trains coherently and produces structured output.

`compare_architectures.py` places Memory-NLS next to a same-shape Transformer to make the structural differences between them legible. The Transformer is included here not as a competitor but as a contrast: the two architectures use different sequence-mixing primitives and produce different kinds of behavior. The comparison is differentiation, not benchmark contest. See [`../../CLAUDE.md`](../../CLAUDE.md), Rule 7a.

`verify_training_infra.py` exists for the narrow purpose of confirming that the training loop itself works on a model whose training behavior is well-established. It is only useful if you suspect the training infrastructure is the cause of some observed behavior in the Memory-NLS training.

## Running them

```bash
# Primary small-scale experiment: train Memory-NLS, generate report (~45s).
python experiments/neural/train_tinyshakespeare.py
# → outputs/tinyshakespeare/training_results.md

# Side-by-side differentiation at small scale (~90s).
python experiments/neural/compare_architectures.py
# → outputs/tinyshakespeare_compare/comparison_results.md

# Long-horizon dynamics at small scale (~17 minutes).
python experiments/neural/long_training_dynamics.py
# → outputs/long_training/long_training_results.md

# Scale-up to 70M parameters on enwik8 (~6.3 hours, primary structural finding).
python experiments/neural/scale_up_dynamics.py
# → outputs/scale_up/scale_up_results.md

# Infrastructure check (optional, only if debugging the training loop).
python experiments/neural/verify_training_infra.py
# → outputs/tinyshakespeare/infra_check/
```

## What you should look for

In the Memory-NLS training (`train_tinyshakespeare.py`):

1. **The model trains.** Loss decreases monotonically from random initialization (~4.17 for a 65-character vocabulary) to a substantially lower value.
2. **The model learns character-level structure.** Generation samples include character names with colons ("ROMEO:", "MERCUTIO:"), line breaks, and approximate English-like spelling — not random characters and not unchanged from initialization.
3. **The structural parameters carry the physical meaning they have in the equation.** $\Lambda < 0$ is attractive self-interaction; positive $\Sigma\lambda$ is repulsive memory feedback; $\nu_\text{min}$ and $\nu_\text{max}$ control the slow and fast memory timescales. These are not separate hyperparameters fit to the language-modeling task; they are the same parameters that appear in the physics solver.

In the side-by-side comparison (`compare_architectures.py`):

1. **Both train, both produce structured output** — but via different mechanisms.
2. **The numerical metrics differ.** At this small scale, attention reaches lower perplexity. This is the expected outcome for a primitive specifically engineered for content-based retrieval, with substantial prior research and capital invested in it. The number is not the test the work is asking to be evaluated on; see the methodology folder.
3. **The samples differ qualitatively.** Memory-NLS produces phonologically-coherent invented words; Transformer produces more real English vocabulary via copy-paste from training. These are different inductive biases producing different kinds of intelligent behavior.

What you should NOT look for in either experiment: state-of-the-art perplexity, leaderboard scores, scaling behavior, "which architecture wins." Those framings belong to a different paradigm. See [`../../CLAUDE.md`](../../CLAUDE.md), section "Intelligence-as-structure, not intelligence-as-scale".

## What you should look for at scale (`scale_up_dynamics.py`)

This is the experiment where the structural difference between Memory-NLS and Transformer becomes most empirically visible. At 70M parameters on enwik8 (4 epochs through 100MB of data), with identical training infrastructure:

1. **Memory-NLS produces a monotonic descent + plateau.** Final val perplexity 4.27, no catastrophic events, train-val gap stays small. The structural anti-collapse mechanism that the equation predicts manifests as optimization trajectory stability.

2. **Transformer exhibits catastrophic optimization collapse.** Reaches a low minimum (val perplexity 2.54) at step 22500, then crashes catastrophically at step 28000–34000 (peak val perplexity 27.17, an 8.8× degradation). Recovers partially through the remaining steps to final val perplexity 4.87 — worse than Memory-NLS's plateau, despite reaching a lower minimum mid-training.

3. **Generation samples confirm the qualitative difference.** Memory-NLS preserves Wikipedia structural grammar (XML hierarchy, infobox tables, references) throughout training; Transformer outputs degenerate to syntactically broken fragments during the crash and only partially recover.

The scale-up experiment is the structural-realist empirical test: same equation form derived from physics, manifesting the same anti-collapse phenomenology in neural training that it produces in 3D NLS field dynamics. Same form, different substrate.

See [`../../results/08-optimization-collapse-empirical.md`](../../results/08-optimization-collapse-empirical.md) for the structural finding documentation and trajectory plots.

## Related documents

- [`../../interfaces/06-state-space-models.md`](../../interfaces/06-state-space-models.md) — mathematical correspondence with state space models.
- [`../../implementation/neural/`](../../implementation/neural/) — layer and model implementations.
- [`../../methodology/03-how-to-evaluate-this.md`](../../methodology/03-how-to-evaluate-this.md) — evaluation procedure.
- [`../../results/08-optimization-collapse-empirical.md`](../../results/08-optimization-collapse-empirical.md) — structural finding from scale-up.
- [`../../outputs/tinyshakespeare/training_results.md`](../../outputs/tinyshakespeare/training_results.md) — small-scale Memory-NLS report.
- [`../../outputs/tinyshakespeare_compare/comparison_results.md`](../../outputs/tinyshakespeare_compare/comparison_results.md) — small-scale comparison report.
- [`../../outputs/long_training/long_training_results.md`](../../outputs/long_training/long_training_results.md) — 50,000-step run at 1.5M parameters.
- [`../../outputs/scale_up/scale_up_results.md`](../../outputs/scale_up/scale_up_results.md) — 50,000-step run at 70M parameters with structural collapse observation.
