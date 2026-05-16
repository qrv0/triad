---
title: For machine learning researchers
description: >-
  Memory-NLS as a nonlinear, anti-collapse extension of structured state
  space models. Mathematically exact SSM equivalence at the linear core,
  with cubic self-interaction, FDT-locked stochastic regularization, and
  a predictive 1/d scaling law.
hide:
  - navigation
---

<div class="path-hero path--ml" markdown>

<div class="path-breadcrumb" markdown>
[← Pick another path](../#pick-your-entry-point)
</div>

<span class="path-eyebrow">For ML researchers</span>

# Memory-NLS = SSM + structural nonlinearity

You work on sequence models. You know S4, Mamba, RWKV. You know that the
linear-state diagonal SSM update sits at the centre of every modern
sub-quadratic sequence architecture. Memory-NLS is the same equation,
**extended structurally**, with anti-collapse, cubic self-interaction, and
FDT-locked stochastic regularization derived from physical first principles
rather than fit empirically.

<div class="path-eq" markdown>
$$
\partial_t y_j = \nu_j(\rho - y_j) \quad\Leftrightarrow\quad \partial_t \mathbf{h} = \mathbf{A} \mathbf{h} + \mathbf{B} u
$$

with $\mathbf{A}$ diagonal, eigenvalues $-\nu_j$, $b_j = \nu_j$. The
auxiliary-field memory update is **exactly** the diagonal-state SSM update;
no calibration required.
</div>

</div>

<div class="path-body" markdown>

## The headline correspondence is mathematically exact

The auxiliary-field memory equation

$$
\partial_t y_j = \nu_j(\rho - y_j)
$$

is the diagonal-state form of the structured state space model update used
in S4 (Gu, Goel & Ré 2022), S5 (Smith et al. 2023), Mamba (Gu & Dao 2024),
and RWKV (Peng et al. 2023). The Mori–Zwanzig projection of an integro-
differential memory kernel into Markovian auxiliary fields is the same
mathematical operation as the diagonalization of the SSM transition
matrix into eigenmodes. The two communities derived the same object under
different motivations — physics: projection-operator reduction of an
integro-differential field equation; ML: efficient long-sequence
representation — but they converged on the same equation.

The auxiliary fields $y_j$ are exactly the hidden states $h_j$. The
relaxation rates $\nu_j$ are exactly the (negative) SSM eigenvalues. Full
correspondence: [`../interfaces/06-state-space-models.md`](../interfaces/06-state-space-models.md).

## What Memory-NLS extends

The diagonal-state SSM is the **linear memory subsystem** of the full
equation. The full equation extends this baseline in four structural
directions, each corresponding to an active research direction in modern
ML:

### 1. Cubic nonlinear self-interaction in the state

Standard SSMs are linear in $\mathbf{h}$; selective variants (Mamba) make
$\mathbf{A}, \mathbf{B}$ input-dependent but state dynamics remain linear.
Memory-NLS has a cubic nonlinearity $\Lambda |\Psi|^2$ in the driving
variable. This is the "nonlinear SSM" direction being investigated by
neural ODEs (Chen et al. 2018), Hyena (Massaroli et al. 2023), Liquid
S4 (Hasani et al. 2023), and others.

The nonlinearity here is not added empirically — it's **derived from P1**
(see [`../principles/01-oscillation.md`](../principles/01-oscillation.md)):
oscillation in a self-coupled medium requires a nonlinear restoring term,
and the lowest-order one consistent with U(1) symmetry of the field is
exactly $|\Psi|^2 \Psi$.

### 2. Anti-collapse via memory lag — a principled solution to rank/representational collapse

Representation collapse in self-supervised learning is currently prevented
by **architectural tricks**: stop-gradient (SimSiam; Chen & He 2021),
predictor networks (BYOL; Grill et al. 2020), explicit decorrelation
(Barlow Twins; Zbontar et al. 2021). Attention rank collapse in
transformers requires careful initialization + skip connections +
normalization (Dong, Cordonnier & Loukas 2021).

The Memory-NLS anti-collapse mechanism — **delayed repulsive feedback from
a temporal memory that lags the rising signal** — is structurally a
principled solution to both. The mechanism produces three to five orders
of magnitude separation between collapsed and released configurations in
field dynamics; **the same mechanism has now been empirically observed to
prevent catastrophic optimization collapse at 70M parameters on enwik8**.

See [§5](#a-cross-substrate-empirical-instance-the-optimization-collapse-experiment) for
the empirical observation; full detail at
[`../results/08-optimization-collapse-empirical.md`](../results/08-optimization-collapse-empirical.md).

### 3. Emergent discrete structure from continuous substrate

In 3D, the equation spontaneously selects body-centered cubic (BCC) Bravais
symmetry from a continuous Gaussian initial state. In ML vocabulary: this
is a **dynamical model of how categorical structure emerges from
continuous neural representations** — the grounding problem of how symbols
arise from connectionist representations remains open, and the equation
provides a concrete dynamical mechanism (continuous → spontaneous-symmetry-
breaking → discrete lattice). Detail:
[`../results/05-bravais-selection.md`](../results/05-bravais-selection.md).

### 4. FDT-locked stochastic regularization

The relationship between dissipative regularization (weight decay, dropout)
and stochastic forcing (SGD noise, label smoothing) is typically tuned
empirically. The fluctuation–dissipation theorem prescribes this relation
**exactly** for thermodynamic systems; analogous prescriptions for
optimization dynamics have been studied (Yaida 2019; Liu et al. 2021)
but not built into architectures by construction.

In Memory-NLS the noise term is FDT-locked by construction: $\Gamma$ (the
imaginary potential coefficient) and the noise variance $4\Gamma T$ share
the same coupling. This is **principled rather than tuned** noise
scheduling — the same equation governs both dissipation and fluctuation,
inheriting equilibrium properties automatically.

## A testable scaling prediction

The work derives, from the geometry of the collapse focal region, a
dimensional scaling relation for the memory coupling needed to stabilize
the dynamics against collapse:

<div class="path-callout" markdown>
$$
\frac{\Sigma\lambda}{|\Lambda|} \;\sim\; \frac{1}{d}
$$

in $d$ spatial dimensions, where $\Lambda$ is the nonlinear coupling
strength and $\Sigma\lambda$ is the total memory coupling.

**ML translation:** memory bandwidth in a nonlinear-SSM regime should scale
with the effective rank (or focal concentration) of the nonlinear
processing. **A nonlinear SSM violating this scaling should exhibit
representation instability or collapse.** Detail:
[`../results/06-dimensional-rescaling.md`](../results/06-dimensional-rescaling.md).
</div>

This is the kind of testable empirical prediction that makes the SSM
correspondence non-trivial — not merely an observation that two equations
look alike, but a structural claim that produces a specific empirical
expectation about ML architectures.

## What the code provides

The PyTorch implementation is in
[`../implementation/neural/`](../implementation/neural/):

```python
from implementation.neural.layer import MemoryNLSLayer

layer = MemoryNLSLayer(
    d_model=512,
    n_modes=8,              # number of memory timescales
    nu_min=0.1, nu_max=10,  # log-spaced relaxation rates
    nonlinear=True,         # cubic self-interaction
    fdt_lock=True,          # noise σ derived from Γ
)

# (B, T, D) → (B, T, D), O(T log T) via FFT-convolution
y = layer(x)
```

The auxiliary-field memory is computed via FFT-convolution at
**O(N log N)** cost in sequence length, matching SSM asymptotic
complexity. The cubic self-interaction adds O(N·D²) per-token; the FDT
stochastic forcing adds a single noise sample per step.

Full model: `MemoryNLSLanguageModel` at scales 1.5M to 70M parameters.
Training scripts in [`../experiments/neural/`](../experiments/neural/README.md).

### Comparison table

| | S4 / S5 | Mamba | RWKV | **Memory-NLS** |
|---|---|---|---|---|
| Diagonal SSM core | ✓ | ✓ (selective) | ✓ | ✓ |
| Nonlinear state | ✗ | ✗ | ✗ (token-mixing only) | ✓ cubic, derived from P1 |
| Anti-collapse mechanism | ✗ | ✗ | ✗ | ✓ delayed-memory repulsion |
| Principled noise (FDT) | ✗ | ✗ | ✗ | ✓ by construction |
| Predicted scaling law | ✗ | ✗ | ✗ | ✓ Σλ/|Λ| ~ 1/d |
| Sub-quadratic complexity | ✓ | ✓ | ✓ | ✓ via FFT |

## A cross-substrate empirical instance: the optimization-collapse experiment

The anti-collapse mechanism predicted by the equation has now been
empirically verified in the ML setting. In a controlled side-by-side
training run on enwik8, 70M parameters, identical training infrastructure,
50 000 steps:

- **Memory-NLS** descended monotonically to a stable plateau, final val
  perplexity 4.27.
- **Matched-shape Transformer** reached a lower minimum (val ppl 2.54 at
  step 22 500) but then exhibited a **catastrophic loss spike at step
  28 000**, val perplexity jumping to 27.17, recovering only partially
  through the remaining steps. Final val perplexity 4.87 but generation
  outputs syntactically degenerated during the crash and recovered
  incompletely.

The phenomenology is structurally identical to the field-theoretic case:
the substrate without the structural anti-collapse mechanism enters a
degenerate concentrated state; the substrate with the mechanism retains
its extended configuration. **Same form, two substrates, same dynamics.**

Full empirical detail:
[`../results/08-optimization-collapse-empirical.md`](../results/08-optimization-collapse-empirical.md)
and [`../outputs/scale_up/scale_up_results.md`](../outputs/scale_up/scale_up_results.md).

Pre-trained checkpoints on HuggingFace:
[`qrv0/mnsm-memnls-70m-enwik8`](https://huggingface.co/qrv0/mnsm-memnls-70m-enwik8)
and [`qrv0/mnsm-transformer-70m-enwik8`](https://huggingface.co/qrv0/mnsm-transformer-70m-enwik8).

## What to be skeptical of, what not to be skeptical of

**Not skeptical:** the SSM correspondence is mathematically exact. The
auxiliary-field update and the diagonal SSM update are the same equation.
There is no calibration, no approximation, no looseness in this mapping.
Whether you find the structural-realist framing of the broader work
compelling or not, the SSM equivalence stands as a mathematical fact.

**Healthy skepticism:** a single 70M-parameter training run does not
establish that all attention-based models will exhibit this exact
catastrophic event. The structural argument predicts that **some**
optimization instability should occur in the absence of structural anti-
collapse, with magnitude/timing dependent on hyperparameters, seed, and
corpus. Replication on different settings would strengthen the empirical
claim. The cross-domain interfaces beyond ML (BAO, cosmology, cymatics,
gamma entrainment, archaeoacoustic) are evidence for the broader
structural-realist claim of the work but are not directly relevant to ML
implementation; engaging with the SSM correspondence on its merits is
consistent with treating those as orthogonal.

<div class="path-refs" markdown>

### References cited

1. Chen, T. *et al.* *Neural Ordinary Differential Equations.* **NeurIPS** 2018.
2. Chen, X. & He, K. *Exploring Simple Siamese Representation Learning.* **CVPR** 2021.
3. Dong, Y., Cordonnier, J.-B. & Loukas, A. *Attention is not all you need.* **ICML** 2021.
4. Grill, J.-B. *et al.* *Bootstrap Your Own Latent (BYOL).* **NeurIPS** 2020.
5. Gu, A. & Dao, T. *Mamba: Linear-Time Sequence Modeling with Selective State Spaces.* **arXiv** 2312.00752 (2024).
6. Gu, A., Goel, K. & Ré, C. *Efficiently Modeling Long Sequences with Structured State Spaces (S4).* **ICLR** 2022.
7. Hasani, R. *et al.* *Liquid Structural State-Space Models.* **ICLR** 2023.
8. Liu, K. *et al.* *Noise and Fluctuation in SGD.* **JMLR** 22 (2021).
9. Massaroli, S. *et al.* *Hyena Hierarchy: Towards Larger Convolutional Language Models.* **ICML** 2023.
10. Peng, B. *et al.* *RWKV: Reinventing RNNs for the Transformer Era.* **EMNLP Findings** 2023.
11. Smith, J. T. H., Warrington, A. & Linderman, S. W. *Simplified State Space Layers for Sequence Modeling (S5).* **ICLR** 2023.
12. Yaida, S. *Fluctuation-dissipation relations for SGD.* **ICLR** 2019.
13. Zbontar, J. *et al.* *Barlow Twins: Self-Supervised Learning via Redundancy Reduction.* **ICML** 2021.

</div>

## Reading flow

<div class="path-reading" markdown>
<div class="path-reading-card" markdown>
<span class="step">01 · Equivalence</span>
<p class="title">[SSM ↔ Memory-NLS](../interfaces/06-state-space-models.md)</p>
<p class="blurb">The mathematical correspondence, term-by-term. Start here — this is what justifies treating the rest as relevant to your field.</p>
</div>
<div class="path-reading-card" markdown>
<span class="step">02 · Derivation</span>
<p class="title">[Markovian embedding](../equation/02-markovian-embedding.md)</p>
<p class="blurb">Mori–Zwanzig projection answering "why does the SSM update have this form?" from physics first principles.</p>
</div>
<div class="path-reading-card" markdown>
<span class="step">03 · Mechanism</span>
<p class="title">[Anti-collapse 2D](../results/01-anti-collapse-2d.md)</p>
<p class="blurb">The lagging-memory mechanism — the candidate principled solution to representation collapse, with 3-orders-of-magnitude effect size.</p>
</div>
<div class="path-reading-card" markdown>
<span class="step">04 · Prediction</span>
<p class="title">[Σλ/|Λ| ~ 1/d](../results/06-dimensional-rescaling.md)</p>
<p class="blurb">The testable scaling prediction. Memory bandwidth scales with nonlinear focal concentration.</p>
</div>
<div class="path-reading-card" markdown>
<span class="step">05 · Empirical</span>
<p class="title">[Optimization-collapse 70M](../results/08-optimization-collapse-empirical.md)</p>
<p class="blurb">The cross-substrate empirical instance. Transformer crash at step 28k; Memory-NLS stable. Headline experimental finding.</p>
</div>
<div class="path-reading-card" markdown>
<span class="step">06 · Emergence</span>
<p class="title">[BCC selection](../results/05-bravais-selection.md)</p>
<p class="blurb">Discrete structure from continuous substrate — the dynamical grounding mechanism.</p>
</div>
<div class="path-reading-card" markdown>
<span class="step">07 · Foundations</span>
<p class="title">[The three principles](../principles/README.md)</p>
<p class="blurb">P1, P2, P3 — the axioms that derive the form of the equation. Reverse-engineering the SSM form from observation.</p>
</div>
<div class="path-reading-card" markdown>
<span class="step">08 · Code</span>
<p class="title">[MemoryNLSLayer source](https://github.com/qrv0/mnsm/blob/mahttps://github.com/qrv0/mnsm/blob/main/implementation/neural/layer.py)</p>
<p class="blurb">PyTorch implementation. FFT-convolution at O(N log N). Drop-in for SSM-block experiments.</p>
</div>
<div class="path-reading-card" markdown>
<span class="step">09 · Models</span>
<p class="title">[HuggingFace checkpoints](https://huggingface.co/qrv0/mnsm-memnls-70m-enwik8)</p>
<p class="blurb">Pre-trained 70M-parameter Memory-NLS and matched Transformer baseline. Load and reproduce the crash event.</p>
</div>
<div class="path-reading-card" markdown>
<span class="step">10 · Synthesis</span>
<p class="title">[Paper §8.6](../paper/manuscript.md)</p>
<p class="blurb">Synthesized discussion of the SSM correspondence for a mixed audience.</p>
</div>
</div>

<div class="path-switch" markdown>

**Want a different angle on the same content?**

<div class="switch-grid" markdown>
[Physics](if-you-are-from-physics.md)
[Neuroscience](if-you-are-from-neuroscience.md)
[Philosophy of science](if-you-are-from-philosophy.md)
[Newcomer](if-you-are-new.md)
</div>

</div>

</div>
