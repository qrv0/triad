---
title: For physicists
description: >-
  Memory-augmented nonlinear Schrödinger field with FDT-locked dissipation.
  L²-supercritical anti-collapse via auxiliary-field Mori–Zwanzig embedding.
hide:
  - navigation
---

<div class="path-hero path--physics" markdown>

<div class="path-breadcrumb" markdown>
[← Pick another path](../#read-it-your-way)
</div>

<span class="path-eyebrow">For physicists</span>

# The Triad equation, in the notation you already use

You know Gross–Pitaevskii, Mori–Zwanzig projection, FDT in open systems, L²-critical/supercritical NLS collapse, and fractional Laplacians. This work sits at their intersection: three structural axioms about persistent extended entities jointly select the form below, and that form produces phenomena — anti-collapse, BCC lattice selection, broadband absorption — that no single-term reduction captures.

<div class="path-eq" markdown>
$$
i\hbar\, \partial_t \Psi
\;=\;
\left[\,-\tfrac{\hbar^{2}}{2m}\nabla^{2} + V_{\text{ext}} + \Lambda |\Psi|^{2} + V_{\text{mem}} + \alpha\,(-\Delta)^{\sigma/2} - i\Gamma\,\right]\Psi \;+\; \eta
$$
</div>

with $V_{\text{mem}} = \sum_j \lambda_j y_j$, $\partial_t y_j = \nu_j(\rho - y_j)$, $\rho = |\Psi|^2$, and $\eta$ Gaussian-white satisfying the classical FDT correlator $\langle \eta(\mathbf{x},t)\,\eta^*(\mathbf{x}',t')\rangle = 4\Gamma T\,\delta(\mathbf{x}-\mathbf{x}')\,\delta(t-t')$.

</div>

<div class="path-body" markdown>

## What this maps to in your area

The cubic NLS is augmented with three structural additions: (i) an auxiliary-field Mori–Zwanzig memory $V_{\text{mem}}$ — a Markovian embedding of an integro-differential kernel, standard in projection-operator reduction but here treated as structurally required by P2; (ii) an FDT-locked dissipation–noise pair $(-i\Gamma, \eta)$ as in stochastic field theory for open systems; and (iii) an optional fractional Laplacian for anomalous dispersion. In 2D at the L²-critical threshold the memory lag prevents focal collapse by three orders of magnitude in peak density; in 3D (supercritical) the same mechanism operates with a geometrically predicted rescaling $\Sigma\lambda/|\Lambda|\big|_{3D} \sim 10\times\Sigma\lambda/|\Lambda|\big|_{2D}$. The released crystalline state spontaneously selects BCC from a continuous isotropic initial condition.

## Reading sequence

<div class="path-reading" markdown>
<div class="path-reading-card" markdown>
<span class="step">01 · Equation</span>
<p class="title">[Full derivation](../equation/01-derivation.md)</p>
<p class="blurb">P1 selects the Schrödinger kinetic, P2 selects the integral memory, P3 selects the FDT-locked noise — the derivation in full.</p>
</div>

<div class="path-reading-card" markdown>
<span class="step">02 · Reduction</span>
<p class="title">[Markovian embedding](../equation/02-markovian-embedding.md)</p>
<p class="blurb">Mori–Zwanzig projection of the integral kernel into diagonal auxiliary fields — the form physicists already use as standard practice.</p>
</div>

<div class="path-reading-card" markdown>
<span class="step">03 · Result</span>
<p class="title">[2D anti-collapse](../results/01-anti-collapse-2d.md)</p>
<p class="blurb">L²-critical NLS at Λ=−8: three orders of magnitude peak-density separation between memoried and unmemoried runs.</p>
</div>

<div class="path-reading-card" markdown>
<span class="step">04 · Result</span>
<p class="title">[3D anti-collapse](../results/04-anti-collapse-3d.md)</p>
<p class="blurb">L²-supercritical regime: 10⁵× separation; mechanism survives the harder case where bare NLS collapse is generic.</p>
</div>

<div class="path-reading-card" markdown>
<span class="step">05 · Result</span>
<p class="title">[Dimensional rescaling](../results/06-dimensional-rescaling.md)</p>
<p class="blurb">$\Sigma\lambda/|\Lambda| \sim 1/d$ derived from focal-region geometry — predicted from structure, confirmed numerically.</p>
</div>

<div class="path-reading-card" markdown>
<span class="step">06 · Result</span>
<p class="title">[Bravais selection](../results/05-bravais-selection.md)</p>
<p class="blurb">Spontaneous BCC selection from an isotropic Gaussian initial state — no symmetry input, detection score 0.44 with gap +0.13 over FCC.</p>
</div>

<div class="path-reading-card" markdown>
<span class="step">07 · Cross-substrate</span>
<p class="title">[Optimization-collapse experiment](https://github.com/qrv0/mnsm/blob/main/results/01-optimization-collapse-empirical.md)</p>
<p class="blurb">The anti-collapse mechanism in a 70M-parameter neural network — structurally identical phenomenology, categorically different substrate.</p>
</div>
</div>

## Switch path

<div class="path-switch" markdown>
[ML](if-you-are-from-ml.md) &nbsp;·&nbsp; [Neuroscience](if-you-are-from-neuroscience.md) &nbsp;·&nbsp; [Philosophy](if-you-are-from-philosophy.md) &nbsp;·&nbsp; [Newcomer](if-you-are-new.md)
</div>

</div>
