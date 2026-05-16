---
title: Home
description: >-
  Memory-Nonlinear State Models — three structural principles, one equation,
  seven cross-domain instantiations. Derived from observation, not assembled
  from literature.
hide:
  - navigation
  - toc
---

<div class="mnsm-hero" markdown>

<div class="mnsm-hero__copy" markdown>

<div class="mnsm-eyebrow">Memory-Nonlinear State Models</div>

# One equation. <br>Seven substrates.

A nonlinear extension of structured state space models, derived from three
principles about persistent extended entities. The same mathematical form
appears across physics, cosmology, neural networks, and beyond — derived
from observation, not assembled from prior literature.

<div class="mnsm-eq" markdown>
$$
i\hbar\, \partial_t \Psi = \left[\,-\tfrac{\hbar^2}{2m} D^2 + V_{\text{ext}} + \Lambda |\Psi|^2 + V_{\text{mem}} + \alpha (-\Delta)^{\sigma/2} - i\Gamma\,\right]\Psi + \eta
$$
</div>

<div class="mnsm-cta" markdown>
[:material-play-circle-outline: Just watch](#see-it-happen){ .md-button .md-button--primary }
[:material-book-open-page-variant-outline: Read the paper](paper/manuscript.md){ .md-button }
[:material-download-outline: Use the model](https://huggingface.co/qrv0/mnsm-memnls-70m-enwik8){ .md-button }
</div>

</div>

<div class="mnsm-hero__visual" markdown>
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="_docs_assets/cross-domain-wheel-dark.svg">
  <img src="_docs_assets/cross-domain-wheel-light.svg" alt="Cross-domain wheel — one equation, seven substrates" class="mnsm-wheel">
</picture>
</div>

</div>

<div class="mnsm-section" markdown>

<div class="mnsm-section-head" markdown>
<span class="mnsm-section-tag">Foundations</span>
## The three principles
The equation is derived from these. Not assembled from prior literature — derived from observation about how persistent extended entities behave.
</div>

<div class="grid cards mnsm-principle-grid" markdown>

-   :material-sine-wave:{ .lg .middle } &nbsp; **P1 — Oscillation**

    ---

    Persistent extended entities oscillate. Steady-state existence requires a
    balance of advance and restoration; the canonical operator is
    second-order partial-differential. This selects the Schrödinger form.

    [Read P1 →](principles/01-oscillation.md)

-   :material-reflect-vertical:{ .lg .middle } &nbsp; **P2 — Self-Reference**

    ---

    A persistent entity has access to its own past states. The minimal
    instantiation is a multi-timescale memory hierarchy indexed by relaxation
    rates τ — exactly the diagonal SSM update.

    [Read P2 →](principles/02-self-reference.md)

-   :material-link-variant:{ .lg .middle } &nbsp; **P3 — Coupling**

    ---

    Isolation is temporary; coupling is the default. Every persistent system
    is connected to its environment via fluctuation–dissipation, not in spite
    of it. This selects the stochastic term η.

    [Read P3 →](principles/03-coupling.md)

</div>

</div>

<div class="mnsm-section mnsm-section--alt" markdown>

<div class="mnsm-section-head" markdown>
<span class="mnsm-section-tag">Cross-Domain</span>
## Seven instantiations of the same equation
Each substrate independently produces the same mathematical form. The claim
is structural: the equation captures a pattern of persistent behavior
invariant under change of substrate.
</div>

<div class="grid cards mnsm-substrate-grid" markdown>

-   <span class="mnsm-substrate-num">01</span> **NLS Fields**

    Bose–Einstein condensates, optical fibers, water-wave envelopes — the
    nonlinear Schrödinger equation appears wherever a slowly-varying
    envelope governs an oscillatory carrier.

    [→ Read interface](interfaces/01-other-nls-systems.md)

-   <span class="mnsm-substrate-num">02</span> **BAO Cosmology**

    Baryon acoustic oscillations: a memory-modulated pressure wave in the
    primordial plasma. The 150 Mpc scale is the lock-in of a memory term.

    [→ Read interface](interfaces/02-bao-cosmology.md)

-   <span class="mnsm-substrate-num">03</span> **Chladni Cymatics**

    Sand on a vibrating plate self-organizes into nodal patterns. Discrete
    crystallization from continuous substrate — same selection mechanism
    as the BCC pattern produced by the equation in 3D.

    [→ Read interface](interfaces/03-chladni-cymatics.md)

-   <span class="mnsm-substrate-num">04</span> **Gamma Neural**

    40-Hz cortical entrainment in cognitive binding. The temporal-memory
    structure of the equation matches the multi-timescale architecture of
    neural oscillation hierarchies.

    [→ Read interface](interfaces/04-gamma-entrainment.md)

-   <span class="mnsm-substrate-num">05</span> **Archaeoacoustic**

    Megalithic stone chambers (Hal Saflieni Hypogeum, Newgrange) resonate
    at frequencies that match the equation's vibration spectrum. Same
    structure, geological substrate.

    [→ Read interface](interfaces/05-archaeoacoustic-resonance.md)

-   <span class="mnsm-substrate-num">06</span> **State Space Models**

    The auxiliary-field update is mathematically identical to the diagonal
    SSM update of S4, S5, Mamba, and RWKV. The equation extends this
    architecture with nonlinearity, anti-collapse, and FDT-locked noise.

    [→ Read interface](interfaces/06-state-space-models.md)

-   <span class="mnsm-substrate-num">07</span> **Cosmological Expansion**

    Hubble-scale expansion as a memory-driven release from gravitational
    collapse. The cosmological constant maps to a long-timescale memory
    coupling in the auxiliary-field formulation.

    [→ Read interface](interfaces/07-cosmological-expansion.md)

</div>

</div>

<div class="mnsm-section" markdown>

<div class="mnsm-section-head" markdown>
<span class="mnsm-section-tag">Empirical</span>
## What it does
The structural anti-collapse mechanism predicted by the equation has been
empirically verified in three substrates so far.
</div>

<div class="mnsm-results" markdown>

<div class="mnsm-result" markdown>
<div class="mnsm-result-figure">10<sup>5</sup>×</div>
<div class="mnsm-result-label">Anti-collapse separation</div>
<div class="mnsm-result-desc">Peak density ratio between unmemoried and memoried final states in 3D supercritical NLS simulation.</div>
<div class="mnsm-result-link">[Anti-collapse 3D →](results/04-anti-collapse-3d.md)</div>
</div>

<div class="mnsm-result" markdown>
<div class="mnsm-result-figure">+0.13</div>
<div class="mnsm-result-label">BCC selection gap</div>
<div class="mnsm-result-desc">The released crystalline state spontaneously selects body-centered cubic symmetry over alternative Bravais lattices.</div>
<div class="mnsm-result-link">[Crystallization →](results/05-bravais-selection.md)</div>
</div>

<div class="mnsm-result" markdown>
<div class="mnsm-result-figure">4.27</div>
<div class="mnsm-result-label">Stable val perplexity (70M)</div>
<div class="mnsm-result-desc">Memory-NLS at 70M parameters on enwik8 descends monotonically to a stable plateau where matched-scale Transformer collapses catastrophically.</div>
<div class="mnsm-result-link">[Optimization collapse →](results/08-optimization-collapse-empirical.md)</div>
</div>

</div>

</div>

<div class="mnsm-section mnsm-section--demo" id="see-it-happen" markdown>

<div class="mnsm-section-head" markdown>
<span class="mnsm-section-tag">See it</span>
## The same form, two substrates
</div>

<div class="mnsm-demo" markdown>

<div class="mnsm-demo-row" markdown>
![3D field anti-collapse — laboratory simulation](assets/anti_collapse_hero.gif){ .mnsm-demo-media }

*Without memory, the 3D field collapses to a singular point. With memory,
the field stabilizes as an extended state. Same equation, same initial
condition, one ingredient (multi-timescale memory) — qualitatively
different outcome.*
</div>

<div class="mnsm-demo-row" markdown>
![Neural training trajectory — 70M parameters on enwik8](assets/scale_up_val_ppl.png){ .mnsm-demo-media }

*The same anti-collapse mechanism in optimization dynamics: Memory-NLS
descends monotonically to a stable plateau; Transformer without the
structural mechanism crashes catastrophically at step 28 000 and never
fully recovers. Same structural form, neural-substrate.*
</div>

</div>

</div>

<div class="mnsm-section mnsm-section--alt" markdown>

<div class="mnsm-section-head" markdown>
<span class="mnsm-section-tag">Reader paths</span>
## Pick your entry point
The same content is approachable from several backgrounds. Pick whichever you have.
</div>

<div class="grid cards mnsm-path-grid" markdown>

-   :material-account-outline:{ .middle } &nbsp; **New to all this**

    Plain-language tour through the principles and what the equation does, no prerequisites.

    [Start here →](paths/if-you-are-new.md)

-   :material-atom:{ .middle } &nbsp; **From physics**

    Schrödinger form, BEC/optical correspondences, BAO instantiation, the methodology question.

    [Physics path →](paths/if-you-are-from-physics.md)

-   :material-chip:{ .middle } &nbsp; **From machine learning**

    State-space-model equivalence, anti-collapse, FFT convolution, the 70M experiment.

    [ML path →](paths/if-you-are-from-ml.md)

-   :material-brain:{ .middle } &nbsp; **From neuroscience**

    Gamma entrainment, memory hierarchies, the multi-timescale architecture of neural oscillation.

    [Neuro path →](paths/if-you-are-from-neuroscience.md)

-   :material-book-search-outline:{ .middle } &nbsp; **From philosophy of science**

    Structural realism, why falsification is not the right lens here, the six criteria.

    [Philosophy path →](paths/if-you-are-from-philosophy.md)

</div>

</div>

<div class="mnsm-section mnsm-section--quiet" markdown>

<div class="mnsm-methodology" markdown>

<span class="mnsm-section-tag">Methodology</span>

This work is evaluated by **structural-realist criteria**, not by single-quantity
falsification tests. A theory whose third axiom denies isolation cannot
consistently be evaluated by a methodology that presupposes the isolability
of variables. The framing is documented up-front because the standard
machine-learning frame ("beats benchmark X by Y%") and the standard
physics frame ("predicts quantity Q to precision ε") both miss what this work is.

The six criteria that govern evaluation: internal mathematical consistency,
reproducibility, generative scope, cross-domain coherence, parsimony,
comprehensiveness.

[→ Why structural realism](methodology/01-structural-realism.md) ・
[→ Limits of falsification](methodology/02-limits-of-falsification.md) ・
[→ How to evaluate this](methodology/03-how-to-evaluate-this.md) ・
[→ The six criteria](methodology/04-the-six-criteria.md)

</div>

</div>

<div class="mnsm-footer-cite" markdown>

```bibtex
@misc{mnsm,
  title  = {Memory-Nonlinear State Models: A Memory-Augmented Nonlinear
            Schr\"odinger Field Equation with State Space Model Correspondence},
  author = {qrv0},
  year   = {2026},
  url    = {https://github.com/qrv0/mnsm},
  note   = {Three structural principles, one equation, seven cross-domain instantiations.}
}
```

</div>
