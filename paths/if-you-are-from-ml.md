---
title: For machine learning researchers
description: >-
  The ML implementation depth of the Triad structural prediction lives in
  the mnsm spinoff. This page is the path entry that orients ML readers
  toward both repositories.
hide:
  - navigation
---

<div class="path-hero path--ml" markdown>

<div class="path-breadcrumb" markdown>
[← Pick another path](../#read-it-your-way)
</div>

<span class="path-eyebrow">For ML researchers</span>

# Triad = SSM + structural nonlinearity

You know S4, Mamba, RWKV. The linear-state diagonal SSM update sits at the centre of every modern sub-quadratic sequence architecture. The Triad equation is the same update, extended structurally — with anti-collapse, cubic self-interaction, and FDT-locked stochastic regularization derived from physical first principles rather than fit empirically.

<div class="path-eq" markdown>
$$
\partial_t y_j = \nu_j(\rho - y_j)
\quad\Longleftrightarrow\quad
\partial_t \mathbf{h} = \mathbf{A}\,\mathbf{h} + \mathbf{B}\,u
$$
</div>

with $\mathbf{A}$ diagonal, eigenvalues $-\nu_j$, $b_j = \nu_j$. The auxiliary-field memory update is exactly the diagonal-state SSM update — no calibration required.

</div>

<div class="path-body" markdown>

## What this maps to in your area

The exact equivalence between Triad's auxiliary-field memory and the diagonal SSM update (S4, Mamba, RWKV) means the two were derived independently by communities that did not coordinate. The full equation embeds this P2 subsystem inside a P1 wave-equation kinetic and a P3 FDT-locked dissipation–noise pair. An optimization-collapse experiment at 70M parameters shows the memory-hierarchical model descending monotonically through 50 000 training steps while the matched-shape attention-only baseline spikes catastrophically at step 28 000, with perplexity jumping from 3.10 to 27.17. The work evaluates this as structural evidence, not benchmark competition — see [`methodology/04-the-six-criteria.md`](../methodology/04-the-six-criteria.md).

## Reading sequence

<div class="path-reading" markdown>
<div class="path-reading-card" markdown>
<span class="step">01 · Methodology</span>
<p class="title">[The six criteria](../methodology/04-the-six-criteria.md)</p>
<p class="blurb">The evaluation framework the work uses — six structural criteria, not benchmark perplexity.</p>
</div>

<div class="path-reading-card" markdown>
<span class="step">02 · Conceptual</span>
<p class="title">[The three principles](../principles/README.md)</p>
<p class="blurb">P1, P2, P3 — the structural axioms from which the equation and the SSM equivalence are derived.</p>
</div>

<div class="path-reading-card" markdown>
<span class="step">03 · Equation</span>
<p class="title">[Markovian embedding](../equation/02-markovian-embedding.md)</p>
<p class="blurb">The auxiliary-field reduction that is structurally equivalent to the diagonal SSM update — the mathematical identity.</p>
</div>

<div class="path-reading-card" markdown>
<span class="step">04 · Interface</span>
<p class="title">[SSM equivalence](https://github.com/qrv0/mnsm/blob/main/interfaces/01-state-space-models.md)</p>
<p class="blurb">The exact mathematical correspondence with S4/Mamba/RWKV, with the equation side by side.</p>
</div>

<div class="path-reading-card" markdown>
<span class="step">05 · Empirical</span>
<p class="title">[Optimization-collapse experiment](https://github.com/qrv0/mnsm/blob/main/results/01-optimization-collapse-empirical.md)</p>
<p class="blurb">The 70M-parameter training run — anti-collapse in the MNSM model, catastrophic spike in the matched Transformer.</p>
</div>

<div class="path-reading-card" markdown>
<span class="step">06 · Cross-substrate</span>
<p class="title">[3D anti-collapse](../results/04-anti-collapse-3d.md)</p>
<p class="blurb">The same mechanism in the physics field equation — the structural-realist prediction that links the two substrates.</p>
</div>

<div class="path-reading-card" markdown>
<span class="step">07 · Synthesis</span>
<p class="title">[Full manuscript](../paper/manuscript.md)</p>
<p class="blurb">The complete synthesized argument, covering both the field-theoretic and ML-substrate findings.</p>
</div>
</div>

## Switch path

<div class="path-switch" markdown>
[Physics](if-you-are-from-physics.md) &nbsp;·&nbsp; [Neuroscience](if-you-are-from-neuroscience.md) &nbsp;·&nbsp; [Philosophy](if-you-are-from-philosophy.md) &nbsp;·&nbsp; [Newcomer](if-you-are-new.md)
</div>

</div>
