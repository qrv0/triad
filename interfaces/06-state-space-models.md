---
title: "Interface 06: State space models (Mamba, RWKV, S4)"
description: >-
  The diagonal SSM update of S4 / Mamba / RWKV is term-by-term identical
  to the equation's auxiliary-field memory; the equation adds cubic +
  anti-collapse + FDT-locked noise.
domain: engineering
triangle:
  p1: "hidden-state oscillation across timesteps"
  p2: "auxiliary-field memory hierarchy (diagonal SSM update)"
  p3: "input projection + FDT-locked training noise"
signature_icon: ssm
hero_tier: A
related: [8, 10, 9]
predictions:
  - id: P6.1
    short: "FDT-locked noise reduces training trajectory variance vs ad-hoc noise schedules"
    status: tested_inconsistent
    result_doc: results/16-fdt-locked-noise-empirical-p3.md
  - id: P6.2
    short: "Optimization collapse boundary scales with model size as the cubic term predicts"
    status: not_yet_tested
    result_doc: null
  - id: P6.3
    short: "Cubic state nonlinearity prevents SimSiam collapse without stop-gradient in coupled regime"
    status: tested_consistent
    result_doc: results/17-cubic-ssm-simsiam-fdt.md
---
# Interface: structured state space models

This is the mathematically tightest of the six cross-domain mappings. The auxiliary-field memory equation derived in [`../equation/02-markovian-embedding.md`](../equation/02-markovian-embedding.md) is identical, term by term, to the hidden-state update of the structured state space model architectures that have become a leading approach to sequence modeling in machine learning since 2021.

## The equivalence

The defining update equation of structured state space models (Gu, Goel & Ré 2021; Smith, Warrington & Linderman 2023; Gu & Dao 2024; Peng et al. 2023) is:

$$
\partial_t \mathbf{h}(t) = \mathbf{A}\,\mathbf{h}(t) + \mathbf{B}\,u(t),
$$

with $\mathbf{h}(t) \in \mathbb{R}^d$ a hidden state, $u(t)$ an input signal, and $\mathbf{A}, \mathbf{B}$ structured matrices whose eigenvalues control the temporal range over which past inputs persist. For diagonal $\mathbf{A}$ with eigenvalues $-\nu_j$ (the architecture variant of S4D and the basic Mamba update), the system decouples into $d$ independent scalar equations:

$$
\partial_t h_j(t) = -\nu_j h_j(t) + b_j u(t).
$$

For $b_j = \nu_j$:

$$
\partial_t h_j = \nu_j u - \nu_j h_j = \nu_j (u - h_j).
$$

This is precisely the auxiliary-field equation of the memory-NLS, with the identification $h_j = y_j$ and $u = \rho$:

$$
\partial_t y_j = \nu_j(\rho - y_j).
$$

The auxiliary fields of the present equation and the hidden state components of a diagonal-state SSM are the same object, expressed in different physical and computational contexts.

## No calibration is required

This is the property that distinguishes this correspondence from the others in this folder. No dimensional identification, no choice of physical units, no scaling factor mediates between the two formulations. The two equations are literally the same equation. A physicist who writes the Markovian embedding of an integral memory potential and a machine learning researcher who writes the diagonal hidden-state update of a structured state space model are writing the same mathematical object.

The two communities arrived at this object by entirely different paths. Physicists arrived via Mori–Zwanzig projection-operator methods (Mori 1965; Zwanzig 1961), originally developed to reduce systems with many degrees of freedom to systems with few in classical statistical mechanics. Machine learning researchers arrived via the search for efficient alternatives to attention mechanisms in sequence models, motivated by the quadratic computational cost of attention and the difficulty of capturing very long-range dependencies. Neither community needed the other's motivation to reach the same mathematical structure.

This independent convergence on identical mathematical form is, on the structural-realist reading documented in [`../methodology/`](../methodology/), evidence that the form is recovering something invariant about the underlying class of systems. Two communities under different pressures with different goals reaching the same equation suggests the equation is the unique answer to a structural question both communities were asking, even if neither phrased it that way.

## What the present equation adds to the SSM baseline

The diagonal-state SSM update is the linear memory subsystem of the full equation. The full equation extends this baseline in four structurally distinct directions, each of which corresponds to an active research question in the machine learning literature.

### 1. Nonlinear self-interaction in the state

Standard SSMs are linear in the hidden state $\mathbf{h}$. The inputs $u$ may be projected through learned mixing matrices, and "selective" variants (Mamba; Gu & Dao 2024) make $\mathbf{A}$ and $\mathbf{B}$ input-dependent, but the state dynamics remain linear in $\mathbf{h}$ itself. The present equation introduces a cubic nonlinearity $\Lambda |\Psi|^2$ in the wave equation that drives $\rho = |\Psi|^2$ and hence the auxiliary fields. The nonlinearity acts at the level of the variable that produces the input to the SSM-like memory.

Nonlinear state space models are an active and incomplete extension within the ML literature. Work in this direction includes neural ordinary differential equations (Chen et al. 2018), Hyena (Massaroli et al. 2023), and others. The present equation provides a specific physically-motivated form of nonlinearity, the L²-norm-conserving cubic NLS interaction, that has well-studied properties from the physics literature and that produces, in particular, the anti-collapse phenomenology documented in [`../results/01-anti-collapse-2d.md`](../results/01-anti-collapse-2d.md).

### 2. Anti-collapse via temporal memory lag

Representation collapse, the convergence of distinct inputs onto degenerate output representations, is a documented failure mode of contemporary neural architectures. Self-supervised methods such as SimSiam and BYOL (Chen & He 2021; Grill et al. 2020) prevent collapse via architectural asymmetries: stop-gradient operations, predictor networks, exponential moving averages of weights. The theoretical basis of these prescriptions is incomplete; they are known to work empirically but the precise mechanism by which they avert collapse remains a subject of investigation.

A second form of collapse, attention rank collapse, occurs in transformer architectures and is characterized by the attention matrix becoming low-rank with depth. Dong, Cordonnier & Loukas (2021) showed that pure-attention networks lose rank doubly exponentially with depth, and Noci et al. (2022) developed the theoretical framework. The architectural responses to this, skip connections, normalization layers, careful initialization, are also somewhat empirical.

The anti-collapse mechanism analyzed in [`../results/01-anti-collapse-2d.md`](../results/01-anti-collapse-2d.md) is structurally a candidate solution to both classes of failure mode. The mechanism is the delayed repulsive feedback from a temporal memory potential that lags the rising signal; the memory builds up while concentration is occurring, and releases at the moment the concentration would have locked in. The same mechanism, applied to neural representation dynamics, would provide a principled rather than ad-hoc resistance to representational collapse.

The dimensional rescaling discovered in [`../results/06-dimensional-rescaling.md`](../results/06-dimensional-rescaling.md), $\Sigma\lambda \sim |\Lambda|/d$, where $d$ is the dimensional concentration of the focal region, is the testable scaling prediction this mechanism makes. The corresponding ML hypothesis: the memory bandwidth required to stabilize representations scales with the effective rank of the attention or state representation.

### 3. Spontaneous discrete structure from continuous substrate

The Bravais lattice selection documented in [`../results/05-bravais-selection.md`](../results/05-bravais-selection.md) is, in machine-learning vocabulary, a model of emergent categorical structure from a continuous representational substrate. From an unstructured Gaussian initial state, the equation selects a specific discrete spatial symmetry (BCC in three dimensions, hexagonal in two) and selects it consistently across the relevant parameter range.

The grounding problem, how discrete symbolic categories arise from continuous neural representations, remains open in deep learning theory. The equation provides a concrete mechanism: a continuous, self-interacting field with appropriate temporal coupling spontaneously selects a discrete symmetry through modulational instability about the unperturbed uniform state. The selection is dynamical, not encoded; the symmetry is emergent, not specified.

Whether this mechanism scales from the field-theoretic setting to the very high-dimensional embedding spaces of neural networks is an empirical question for follow-up work. The structural fact, that a memory-augmented continuous field equation can produce discrete symmetry, is established in this work.

### 4. Fluctuation–dissipation-locked stochastic regularization

Noise injection during training is standard in deep learning, but the relationship between the magnitude of dissipative regularization (weight decay, attention dropout, etc.) and the magnitude of stochastic forcing (SGD noise, dropout, label noise) is typically tuned empirically. The fluctuation–dissipation theorem prescribes this relation exactly for thermodynamic systems; its analogue for optimization dynamics has been investigated recently (Yaida 2019; Liu et al. 2021), with suggestive evidence that principled noise schedules outperform heuristically tuned ones in the long-training regime.

The equation's noise term is FDT-locked by construction. Translated into optimization terms, the prescription would be: the stochastic forcing applied during training should be proportional to the square root of (dissipative regularization rate × bath temperature × step size). The temperature parameter is, in this translation, an analogue of the effective stochasticity of the input distribution. The prescription is parameter-poor, only $\gamma_0$ and $T$ are free, and removes the need to separately tune noise injection and weight decay.

## Time as calibration in this substrate

The SSM substrate has no physical time; computation is the only time. The relevant timescales are computational: the discretization step $\Delta t$ in the continuous-time S4 formulation, equivalent to one token's worth of sequence advance in Mamba and RWKV; the per-step decay factor $\exp(-\nu_j \Delta t)$ for the j-th memory channel; and the slowest-decaying channel set by the smallest $\nu_j$ in the model.

The substrate's three timescales fall in a hierarchy. $\Delta t$ (one forward-pass step) is the fast scale. The medium scale is $1/\nu_j$ for channels with eigenvalues near $\Delta t^{-1}$, channels that retain memory of order one step. The slow scale is $1/\nu_{\text{slow}}$ for channels with the smallest eigenvalues, channels that retain memory across many steps and provide long-range context.

Per [`../methodology/07-time-as-calibration.md`](../methodology/07-time-as-calibration.md), the unit of computational time in the present equation is calibrated to one of these substrate timescales. The natural choice for the SSM substrate is to calibrate the equation's discretization step to one forward-pass step of the SSM. The other timescales then follow: $\nu_j \Delta t$ is dimensionless and equal to the per-step decay; the equation's slowest $\nu_j$ corresponds to the SSM's slowest hidden-state component, which sets the effective context length.

This calibration choice differs from the calibration choices for the physics substrates (interfaces 02, 03, 05, 07) where time has a substrate-specific physical meaning. The structural form is preserved across calibrations; the absolute scales are not. This is the standard pattern documented in [`../methodology/06-calibration-philosophy.md`](../methodology/06-calibration-philosophy.md): the structural form is invariant; the calibration is substrate-specific.

## What this correspondence does and does not establish

It does not establish that machine learning practitioners need to adopt the physics-side framing of these objects. The work asserts only that an equation derived from physical structural axioms (P1+P2+P3) is mathematically identical to the linear core of modern sequence models. Whether researchers in machine learning find the physics-side framing useful for their own work is for them to decide; the structural fact does not depend on adoption.

It does not establish that the four extensions Memory-NLS makes beyond the linear SSM baseline (cubic nonlinearity, anti-collapse via temporal memory lag, spontaneous discrete-symmetry selection, FDT-locked noise) constitute superior architectural choices in the comparative-benchmark sense. The structural claim is that each extension is principled, follows from one of the three axioms, and addresses a documented failure mode in current sequence-modeling architectures. Whether the extensions translate into the metrics that ML evaluation conventions privilege is a separate empirical question whose outcome does not bear on the structural claim. Per [`../CLAUDE.md`](../CLAUDE.md) Rule 7a, the comparison is differentiation, not competition.

It does establish that two communities, with no coordination and different research motivations, independently arrived at the same mathematical object. The auxiliary-field memory equation and the diagonal SSM update are term-by-term identical, and remain so whether or not either community engages with the other's framing. This convergence is the cross-domain coherence evidence under criterion 4 of [`../methodology/04-the-six-criteria.md`](../methodology/04-the-six-criteria.md). The structural form selected by P1+P2+P3, far from being arbitrary or post-hoc, is the same form the ML community arrived at independently while solving a different problem (efficient long-sequence modeling).

## Common dismissals and why they do not apply

**"Trivial mathematical coincidence."** The auxiliary-field update $\partial_t y_j = \nu_j(\rho - y_j)$ and the diagonal SSM update $\partial_t \mathbf{h} = \mathbf{A}\mathbf{h} + \mathbf{B} u$ with $\mathbf{A}$ diagonal and eigenvalues $-\nu_j$ are not similar equations; they are the same equation written with different notation. Sections `## The equivalence` and `## No calibration is required` give the term-by-term identification. Calling a term-by-term identity a "coincidence" addresses the appearance of the equations rather than their content; the content is identical.

**"Different motivations, same equation by accident."** Two communities converging on the same mathematical object from different motivations is exactly the structural-realist signature (see [`../methodology/01-structural-realism.md`](../methodology/01-structural-realism.md), criterion of cross-domain coherence). The physics community arrived at this equation by Mori–Zwanzig projection of an integro-differential field equation; the ML community arrived at it by search for efficient long-sequence representation. The convergence is informative because it is unmotivated by either community in terms of the other; if the mathematical form were arbitrary, this convergence would not have occurred.

**"ML does not need physics."** The work does not assert that ML needs physics. It asserts that an equation derived from physical structural axioms is, by mathematical identity, the same equation as the linear core of modern sequence models. Whether ML practitioners find this useful for their own work is for ML practitioners to decide. The structural fact, that the same equation arose independently, is established by the term-by-term identification and is not contingent on ML practitioners adopting the physics-side framing.

## Locally testable predictions and observational signatures

> **Hedge cleanup (2026-05-16).** Each prediction's "What would constitute evidence inconsistent with this calibration" subsection previously used Popperian falsification framing ("would constitute local falsification") inserted in Phase 2 (commit 26e96ee) and propagated by Phase 3 to interfaces 10-17. The hedge contradicted the section's own opening sentence (the structural claim is evaluated by cross-domain coherence, not by single-experiment refutation). See [`../docs/llm-hedge-annotations.md`](../docs/llm-hedge-annotations.md) for the catalog of prior wordings and the structural reason for revision.

The structural claim of this interface (the auxiliary-field equation is term-by-term identical to the diagonal SSM update) is evaluated by cross-domain coherence (methodology/04 criterion 4), not by single-experiment refutation. The equivalence at the level of the linear core is mathematical and requires no testing. The following are *local* predictions about the four extensions Memory-NLS makes to the SSM baseline, all of which are testable in standard sequence-modeling settings without scale-up or competitive benchmarking.

- **Prediction P6.1: Training-trajectory signatures in nonlinear-SSM variants with vs without FDT lock.** The equation predicts that a nonlinear SSM (cubic state nonlinearity) with FDT-locked stochastic forcing in the optimization should exhibit smooth optimization-trajectory characteristics, while the same architecture without the FDT lock should exhibit higher optimization-trajectory variance and increased likelihood of catastrophic loss spikes.
  - How to test: train two nonlinear-SSM variants on the same corpus and infrastructure, one with FDT-locked noise scheduling, one with empirically tuned noise; compare optimization-trajectory variance and incidence of loss spikes.
  - What would constitute confirmation: FDT-locked variant has lower trajectory variance and fewer spikes at matched accuracy.
  - What would constitute evidence inconsistent with this calibration: no difference, or the FDT-locked variant has higher variance / more spikes.
  - Status: **tested in coupled regime, inconsistent** at the multi-seed level (see [`../results/16-fdt-locked-noise-empirical-p3.md`](../results/16-fdt-locked-noise-empirical-p3.md)). Phase C single-seed run showed val-loss trajectory std 0.0952 vs 0.0995 (direction matched, 4% effect). Phase 9 wave-3 follow-up with 4 seeds at each variant (RTX 4060, total wall 1043 s) gave val_loss_std 0.0987 +/- 0.0041 (fdt_high) vs 0.0986 +/- 0.0040 (fdt_low); the effect is statistically indistinguishable from zero (effect-over-noise ratio -0.02). The single-seed observation was within the seed-to-seed noise floor. Per the Duhem-Quine principle, the inconsistent result prompts investigation of calibration ($\gamma_0$ range and $T_{\text{bath}}$ may be too narrow), auxiliary assumptions (model scale, training length), or implementation. The cross-architecture instance at [`../results/08-optimization-collapse-empirical.md`](../results/08-optimization-collapse-empirical.md) remains the principal evidence for the broader anti-collapse phenomenology; the specific P6.1 within-architecture FDT-coupling-strength prediction is not supported at this scale.

- **Prediction P6.2: Scaling of the optimization-collapse boundary with model size.** The equation predicts that the boundary at which optimization-collapse becomes likely (in an attention-only architecture without anti-collapse) scales with model size in a specific way derivable from the focal-region geometry argument (analogous to the dimensional rescaling $\Sigma\lambda / |\Lambda| \sim 1/d$ in the field-theoretic case). Specifically, the parameter-space dimension of the optimization landscape acts as the effective dimension; collapse-boundary parameters should scale accordingly.
  - How to test: repeat the optimization-collapse experiment at a range of model scales (1.5M, 7M, 30M, 70M, 140M, 700M); identify the parameter regime at which the spike becomes likely vs unlikely; compare scaling to the predicted form.
  - What would constitute confirmation: collapse-boundary parameters scale with model size in the predicted way.
  - What would constitute evidence inconsistent with this calibration: collapse-boundary parameters do not scale with size, or scale in a different functional form.
  - Status: untested. The 70M run in results/08 is one data point; the scaling prediction requires multiple scales. (Note: this is not "scaling to test if it beats baselines"; it is "scaling to test a specific structural prediction about the boundary location.")

- **Prediction P6.3: Cubic-nonlinearity in SSM state suppresses representation collapse.** The equation predicts that adding cubic nonlinearity ($\Lambda |\Psi|^2 \Psi$) to the SSM state update suppresses representation collapse modes documented in self-supervised learning (SimSiam without stop-gradient, BYOL without predictor network) without requiring the architectural tricks those frameworks deploy.
  - How to test: implement a nonlinear-SSM-state variant of SimSiam without stop-gradient; train on standard SSL benchmarks; measure representation collapse signatures (representation-space rank, alignment-uniformity loss).
  - What would constitute confirmation: nonlinear-SSM SSL without stop-gradient does not collapse; rank and uniformity remain healthy.
  - What would constitute evidence inconsistent with this calibration: nonlinear-SSM SSL still collapses without stop-gradient; the cubic nonlinearity does not provide the protection.
  - Status: **tested in coupled regime, consistent** (see [`../results/17-cubic-ssm-simsiam-fdt.md`](../results/17-cubic-ssm-simsiam-fdt.md)). Cubic vs linear SSM-state variants of SimSiam without stop-gradient, both with FDT noise active (γ₀ = 0.02, T = 0.01), 4000 steps on RTX 4060: cubic_p3 final effective rank = 4.60/64 vs linear_p3 final effective rank = 2.88/64. Cubic maintains ~60% higher rank than linear, matching the predicted direction. Both variants partially collapse (rank below full 64), so the result establishes the comparative claim (cubic > linear) rather than absolute anti-collapse. Wave-1 isolated variant at [`../results/12-cubic-ssm-simsiam.md`](../results/12-cubic-ssm-simsiam.md) retracted.

## Recommended further reading

The state space model literature relevant to this correspondence:

- Gu, A., Goel, K., & Ré, C. (2021). Efficiently modeling long sequences with structured state spaces. *NeurIPS*.
- Smith, J. T. H., Warrington, A., & Linderman, S. W. (2023). Simplified state space layers for sequence modeling. *ICLR*.
- Gu, A., & Dao, T. (2024). Mamba: Linear-time sequence modeling with selective state spaces. *COLM*.
- Peng, B., et al. (2023). RWKV: Reinventing RNNs for the transformer era. *EMNLP Findings*.

The representation-collapse literature relevant to the anti-collapse mechanism:

- Chen, X., & He, K. (2021). Exploring simple Siamese representation learning. *CVPR*.
- Grill, J.-B., et al. (2020). Bootstrap your own latent. *NeurIPS*.
- Dong, Y., Cordonnier, J.-B., & Loukas, A. (2021). Attention is not all you need: pure attention loses rank doubly exponentially with depth. *ICML*.
- Noci, L., et al. (2022). Signal propagation in transformers: theoretical perspectives and the role of rank collapse. *NeurIPS*.

The optimization-dynamics literature relevant to the FDT-locked noise discussion:

- Yaida, S. (2019). Fluctuation–dissipation relations for stochastic gradient descent. *ICLR*.
- Liu, K., et al. (2021). Noise and fluctuation of finite learning rate stochastic gradient descent. *ICML*.

The original Mori–Zwanzig projection-operator references:

- Mori, H. (1965). Transport, collective motion, and Brownian motion. *Prog. Theor. Phys.* **33**, 423.
- Zwanzig, R. (1961). Memory effects in irreversible thermodynamics. *Phys. Rev.* **124**, 983.
