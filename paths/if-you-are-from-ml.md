---
title: For machine learning researchers
description: >-
  The ML implementation depth of the Memory-NLS structural prediction lives in
  the mnsm-ml spinoff. This page is the path entry that orients ML readers
  toward both repositories.
hide:
  - navigation
---

<div class="path-hero path--ml" markdown>

<div class="path-breadcrumb" markdown>
[← Pick another path](../#pick-your-entry-point)
</div>

<span class="path-eyebrow">For ML researchers</span>

# Memory-NLS = SSM + structural nonlinearity

You work on sequence models. You know S4, Mamba, RWKV. You know that the linear-state diagonal SSM update sits at the centre of every modern sub-quadratic sequence architecture. Memory-NLS is the same equation, extended structurally, with anti-collapse, cubic self-interaction, and FDT-locked stochastic regularization derived from physical first principles rather than fit empirically.

<div class="path-eq" markdown>
$$
\partial_t y_j = \nu_j(\rho - y_j)
\quad\Longleftrightarrow\quad
\partial_t \mathbf{h} = \mathbf{A}\,\mathbf{h} + \mathbf{B}\,u
$$
</div>

with $\mathbf{A}$ diagonal, eigenvalues $-\nu_j$, $b_j = \nu_j$. The auxiliary-field memory update is exactly the diagonal-state SSM update; no calibration required. The full equation embeds this P2 subsystem inside a P1 wave-equation kinetic and a P3 FDT-locked dissipation-noise pair.

</div>

<div class="path-body" markdown>

## Two repositories, advancing in parallel

The work splits across two repositories. The structural argument and the cross-substrate interfaces (other NLS instantiations, BAO cosmology, gamma entrainment, archaeoacoustic resonance, critical brain, Kuramoto, immune affinity maturation, Friston FEP, active matter, SOC, cardiac, gene regulation, ecosystem, pseudomode quantum, Maxwell viscoelasticity, warm inflation, Hawkes, earthquake cycle) live in this repository, [`mnsm`](https://github.com/qrv0/mnsm).

The ML implementation depth lives in the spinoff repository [`mnsm-ml`](https://github.com/qrv0/mnsm-ml). The spinoff contains:

- The PyTorch Memory-NLS sequence layer (`src/`) and the matched Transformer baseline used for structural differentiation per `mnsm/CLAUDE.md` Rule 7a.
- The training infrastructure that produced the 70M-parameter optimization-collapse empirical finding (`experiments/`).
- The two ML-substrate interfaces: state space model equivalence (`interfaces/01-state-space-models.md`) and mechanistic-interpretability convergent prediction (`interfaces/02-mechanistic-interpretability.md`).
- The headline result document `results/01-optimization-collapse-empirical.md`, where Memory-NLS exhibits monotonic plateau under sustained training and the matched-shape Transformer exhibits catastrophic loss spike at step 28,000 of a 50,000-step run.
- Pre-trained 70M-parameter checkpoints on HuggingFace.

## Read order for ML readers

1. The methodology of this repository: [`../methodology/01-structural-realism.md`](../methodology/01-structural-realism.md), [`../methodology/02-limits-of-falsification.md`](../methodology/02-limits-of-falsification.md), [`../methodology/04-the-six-criteria.md`](../methodology/04-the-six-criteria.md). The work is evaluated by six structural criteria, not by benchmark perplexity.
2. The structural principles: [`../principles/`](../principles/).
3. The equation derivation and Markovian embedding: [`../equation/02-markovian-embedding.md`](../equation/02-markovian-embedding.md) (the auxiliary-field equation, structurally equivalent to the diagonal SSM update).
4. The state space model interface and the mechanistic-interpretability interface in [`mnsm-ml`](https://github.com/qrv0/mnsm-ml). These are the ML-substrate cross-domain mappings.
5. The optimization-collapse empirical finding at [`mnsm-ml/results/01-optimization-collapse-empirical.md`](https://github.com/qrv0/mnsm-ml/blob/main/results/01-optimization-collapse-empirical.md).
6. The 3D field-equation anti-collapse finding here at [`../results/04-anti-collapse-3d.md`](../results/04-anti-collapse-3d.md). The cross-substrate match between the field-equation transient-peak signature and the neural-network trajectory-shape signature is the criterion-4 evidence the structural-realist methodology calls for.

## What this is not

This is not a benchmark project. The structural anti-collapse finding at 70M parameters is criterion-4 evidence for the structural claim that the equation captures a form invariant across substrates; it is not a benchmark victory over Transformer. The constraints in `CLAUDE.md` (Rules 1, 2, 7a, 7b) apply: no competitive ML vocabulary, no "needs to scale" framing, no leaderboard chasing. The work documents what the structure produces at the scale we run, not hypothetical larger-scale outcomes.

If you arrive at this work expecting a head-to-head benchmark, the methodology folder explains why the work answers a different question. If you arrive expecting structural depth, the two repositories together cover both the cross-substrate breadth (mnsm) and the implementation depth (mnsm-ml).

</div>
