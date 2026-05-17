---
title: For neuroscientists
description: >-
  Gamma-frequency entrainment, broadband absorption by a self-organized
  oscillating medium with hierarchical temporal memory. Cross-correspondence
  with 40 Hz GENUS, 110 Hz EEG response, and archaeoacoustic resonance.
hide:
  - navigation
---

<div class="path-hero path--neuro" markdown>

<div class="path-breadcrumb" markdown>
[← Pick another path](../#pick-your-entry-point)
</div>

<span class="path-eyebrow">For neuroscientists</span>

# Broadband absorption, hierarchical memory, gamma response

You work on neural oscillations, gamma rhythms, EEG, glymphatic clearance,
or stress-mediated dysregulation. The equation derived in this work
produces a crystalline regime that, under a defensible dimensional
calibration, exhibits broadband absorption across the **20–200 Hz** range
,  covering the neural gamma, beta, and lower high-gamma bands.

<div class="path-eq" markdown>
$$
i\hbar\, \partial_t \Psi
=
\left[\,-\tfrac{\hbar^{2}}{2m}\nabla^{2} + V_{\text{ext}} + \Lambda|\Psi|^{2} + V_{\text{mem}} + \alpha(-\Delta)^{\sigma/2} - i\Gamma\,\right]\Psi + \eta
$$
</div>

<div class="eq-breakdown" markdown>
<div class="eq-term eq-term--p1" markdown>
<span class="eq-term-tag">P1 · Oscillation</span>
<span class="eq-term-math">$-\tfrac{\hbar^{2}}{2m}\nabla^{2}$ ・ $\alpha(-\Delta)^{\sigma/2}$</span>
<span class="eq-term-desc">wave dynamics</span>
</div>
<div class="eq-term eq-term--p2" markdown>
<span class="eq-term-tag">P2 · Self-reference</span>
<span class="eq-term-math">$\Lambda|\Psi|^{2}$ ・ $V_{\text{mem}}$</span>
<span class="eq-term-desc">multi-timescale memory hierarchy (working / short-term / long-term)</span>
</div>
<div class="eq-term eq-term--p3" markdown>
<span class="eq-term-tag">P3 · Coupling</span>
<span class="eq-term-math">$V_{\text{ext}}$ ・ $-i\Gamma$ ・ $\eta$</span>
<span class="eq-term-desc">environmental coupling, dissipation, FDT-locked noise</span>
</div>
</div>

with $V_{\text{mem}} = \sum_j \lambda_j y_j$ from auxiliary fields $y_j$
relaxing at rates $\nu_j$, a **multi-timescale memory hierarchy**
structurally equivalent to the working / short-term / long-term integration
pipeline of the hippocampal–cortical system.

</div>

<div class="path-body" markdown>

## The 40 Hz correspondence, gamma entrainment

Under a dimensional identification where one unit of computational time
maps to 25 milliseconds, the equation's broadband absorption band ($\omega
\in [3, 30]$ computational units) lies at approximately **20–200 Hz** in
physical frequency. This band encompasses the neural gamma band (25–80 Hz),
the beta band, and the lower high-gamma band.

The **40 Hz** frequency at which Iaccarino et al. (2016) document amyloid-β
clearance and glymphatic acceleration via the parvalbumin–VIP–AQP4 pathway
falls within this band. The clinical translation in the OVERTURE Phase II
trial (Hajós et al. 2024) reports significant slowing of cognitive decline
in mild-to-moderate Alzheimer's disease patients exposed to 40 Hz GENUS
stimulation. The same band also encompasses 40 Hz "binding" oscillations
in cortical microcircuits (Fries 2009; Tallon-Baudry & Bertrand 1999).

The work's **structural claim** is that the equation's broadband absorption
mechanism and the neural gamma response are instances of the **same
underlying structural pattern**: broadband absorption by a self-organized
oscillating medium with hierarchical temporal memory. The mechanism is
dimension-independent and substrate-independent; specific frequencies
depend on substrate-specific calibration.

<div class="inline-diagram" markdown>
<p class="inline-diagram-caption">
<strong>Where the equation's modes fall on the EEG frequency map.</strong>
The four teal markers are the equation's principal modes under three
different but each independently defensible dimensional calibrations.
They land on (or near) frequencies that the clinical and experimental
literature has independently identified as physiologically active.
</p>
</div>

Full interface: [`../interfaces/04-gamma-entrainment.md`](../interfaces/04-gamma-entrainment.md).

## The 110 Hz correspondence, vibrational modes

A separate dimensional identification ($L = 20$ m, $dt = 9$ ms) places the
equation's two principal vibrational modes at approximately **66 Hz and
111 Hz**.

<div class="path-callout" markdown>
**Cook, Pajot & Leuchter (2008)**, using quantitative electroencephalography,
report that acoustic stimulation at **110 Hz**, but not at 90, 100, 120, or
130 Hz, produces:

- measurable left-temporal lobe deactivation,
- a shift of prefrontal cortex laterality from baseline left-dominance to
  right-dominance,
- patterns characteristic of meditative and trance-like states.

The 110 Hz value is also the dominant low-frequency resonance reported for
the **inner chamber of Newgrange** (Jahn, Devereux & Ibison 1996) and one of
the two dual resonances reported for the **Hypogeum of Ħal-Saflieni**
(Debertolis et al. 2015). **Three independent measurement traditions
converge on the same frequency.**
</div>

Whether the equation's 110 Hz mode under this calibration is causally
connected to the EEG response and the archaeoacoustic measurements, or
whether the three are independently structured by the same underlying
mechanism, is left **open**. The structural fact: the equation produces this
frequency under one defensible calibration; how to interpret the cross-
domain co-occurrence is for the reader to weigh.

Full interface: [`../interfaces/05-archaeoacoustic-resonance.md`](../interfaces/05-archaeoacoustic-resonance.md).

## The hierarchical memory structure

The equation uses a **multi-mode memory potential** with two characteristic
timescales:

| Mode | Rate ν | Timescale τ | Biological analogue |
|---|---|---|---|
| Fast | 10 | 0.1 | Working memory, hippocampal CA3 |
| Slow | 0.5 | 2 | Cortical consolidation, neocortical LTM |

The two modes serve structurally distinct functions: the **fast mode**
tracks instantaneous density changes; the **slow mode** holds information
about the recent trajectory. This is the **same structural pattern** as the
hippocampal–cortical consolidation pipeline (Squire & Alvarez 1995;
McClelland, McNaughton & O'Reilly 1995): rapid encoding in hippocampus
(fast mode) followed by gradual transfer to neocortical long-term storage
(slow mode).

<div class="inline-diagram" markdown>
<p class="inline-diagram-caption">
<strong>The two structural memory modes mapped onto the biological pipeline.</strong>
The equation's fast and slow relaxation rates fall in exactly the bands
where the brain's working-memory / long-term-consolidation systems
operate. This is a structural correspondence, not a fit, neither set of
timescales was chosen with the other in mind.
</p>
</div>

The equation does not model neural microcircuit biophysics. It models the
**structural pattern** of hierarchical memory that biological memory
systems instantiate. The structural form is invariant; the specific
substrate (cortical tissue vs. computational field) is not.

## The vibrational spectrum

In the **two-dimensional** crystalline regime, the equation produces a
distribution of per-pixel dominant frequencies with median **0.6 c/u.t.**
and a sharp secondary mode at **1.0 c/u.t.**. Under the 9-ms-unit-time
calibration, these map to 66 Hz and 111 Hz.

In the **three-dimensional** crystalline regime, the median dominant
frequency drops to **0.20 c/u.t.**, corresponding to 22 Hz (high beta)
under the same calibration. The factor-of-three shift is consistent with
the dimensional rescaling of the memory coupling discussed in
[`../results/06-dimensional-rescaling.md`](../results/06-dimensional-rescaling.md):
absolute frequencies depend on the underlying timescale of the slow
memory mode against spatial dispersion, which changes with dimensionality.

Full result: [`../results/03-vibrational-modes.md`](../results/03-vibrational-modes.md).

## A connection to mental breakdown, what the cross-substrate experiment shows

A recent empirical observation in this work may interest neuroscientists
working on stress-related disorders, dissociative phenomena, and acute
psychological breakdown.

The optimization-collapse experiment
([`mnsm/results/01-optimization-collapse-empirical.md`](https://github.com/qrv0/mnsm/blob/main/results/01-optimization-collapse-empirical.md))
compared two 70M-parameter neural sequence models, one with the multi-
timescale memory hierarchy that the equation requires, one without, under
identical training conditions on enwik8. The model **without** the
structural memory mechanism exhibited a catastrophic collapse event
mid-training:

- representational coherence broke down at step 28 000,
- generation outputs degenerated to syntactically broken fragments,
- val perplexity spiked from 3.10 to 27.17,
- recovery did not restore pre-collapse capability.

<div class="path-callout" markdown>
**The structural form of this failure mode parallels phenomena documented
in clinical neuroscience.** Acute psychological breakdown often follows
disruption of memory consolidation processes (van der Kolk 2014); dissociative
disorders involve fragmentation across timescales of memory (Putnam 1997);
recovery from severe traumatic episodes is frequently incomplete in ways
that retain "scars" of the disruption.

The MNSM architecture instantiates the canonical biological memory
hierarchy (working / short-term / long-term integration) explicitly via
auxiliary fields with relaxation rates spanning the relevant timescales;
the matched-Transformer's failure mode is structurally **what occurs when
this hierarchy is absent or disrupted**.

This is a structural correspondence, not a clinical claim. But the formal
mechanism by which a system loses representational coherence under
sustained pressure when its memory hierarchy is insufficient is **the same
mechanism**, and it is dimension-independent and substrate-independent.
</div>

The neuroscience reader interested in mechanism-level accounts of mental
disorders may find the cross-substrate observation suggestive as a model
for what hierarchical memory failure looks like as a dynamical signature.

<div class="key-insight" markdown>
<span class="key-insight-tag">Why the multi-Hz convergence is interesting</span>
**Four predicted modes of the equation, 22 Hz, 40 Hz, 66 Hz, 110 Hz , 
fall on or near frequencies that the literature has independently
identified as physiologically active**: 40 Hz (clinical GENUS protocol),
110 Hz (Cook-Pajot-Leuchter EEG response, Newgrange resonance), 22 Hz
(high beta), 66 Hz (mid-gamma). None of those clinical/experimental
frequencies was used to set the equation's parameters. The convergence
is what the structural-realist methodology calls **independent cross-domain
recurrence of the same form**.
</div>

## What the equation does not do

**It does not describe neural dynamics directly.** The appropriate
description of cortical microcircuits is biophysical neural modeling , 
Hodgkin–Huxley, neural mass models, mean-field cortical models, conductance-
based simulations. The equation here is a different mathematical object;
its connection to the neuroscience case is **structural**, at the level of
the absorbing-mechanism mathematics, not the cellular biophysics.

**It does not predict that 40 Hz is special.** Within the broadband
absorption regime, many frequencies should produce responses. The
experimental finding that 40 Hz produces the strongest in-vivo effect is
set by **additional biological factors** downstream of the structural
mechanism the equation describes. The equation predicts the structural
mechanism; the specific frequency at which the response is maximized is
set by the biology.

**It does not establish a causal connection** between megalithic acoustic
engineering, the 110 Hz EEG response, and the equation's intrinsic modes.
The structural correspondence is documented; the deeper interpretation is
left as an open question.

<div class="path-refs" markdown>

### References cited

1. Cook, I. A., Pajot, S. K. & Leuchter, A. F. *Ancient architectural acoustic resonance patterns and regional brain activity.* **Time & Mind** 1, 95–104 (2008).
2. Debertolis, P. *et al.* *Archaeoacoustic analysis of the Hypogeum of Ħal Saflieni in Malta.* **Sociology Study** 5, 451–462 (2015).
3. Fries, P. *Neuronal gamma-band synchronization as a fundamental process in cortical computation.* **Annu. Rev. Neurosci.** 32, 209–224 (2009).
4. Hajós, M. *et al.* *Safety, tolerability, and efficacy of GENUS 40 Hz stimulation in Alzheimer's disease (OVERTURE Phase II).* **Alzheimer's & Dementia** 20, e093442 (2024).
5. Iaccarino, H. F. *et al.* *Gamma frequency entrainment attenuates amyloid load and modifies microglia.* **Nature** 540, 230–235 (2016).
6. Jahn, R. G., Devereux, P. & Ibison, M. *Acoustical resonances of assorted ancient structures.* **JASA** 99, 649–658 (1996).
7. McClelland, J. L., McNaughton, B. L. & O'Reilly, R. C. *Why there are complementary learning systems.* **Psychological Review** 102, 419–457 (1995).
8. Murdock, M. H. *et al.* *Multisensory gamma stimulation promotes glymphatic clearance.* **Nature** 627, 149–156 (2024).
9. Putnam, F. W. <cite>Dissociation in Children and Adolescents</cite>. Guilford Press, 1997.
10. Squire, L. R. & Alvarez, P. *Retrograde amnesia and memory consolidation.* **Curr. Opin. Neurobiol.** 5, 169–177 (1995).
11. Tallon-Baudry, C. & Bertrand, O. *Oscillatory gamma activity in humans and its role in object representation.* **Trends Cogn. Sci.** 3, 151–162 (1999).
12. van der Kolk, B. <cite>The Body Keeps the Score</cite>. Viking, 2014.

</div>

## Reading flow

<div class="path-reading" markdown>
<div class="path-reading-card" markdown>
<span class="step">01 · Interface</span>
<p class="title">[Gamma entrainment](../interfaces/04-gamma-entrainment.md)</p>
<p class="blurb">The 40 Hz correspondence and the broadband absorption mechanism, with explicit caveats about the dimensional identification.</p>
</div>
<div class="path-reading-card" markdown>
<span class="step">02 · Interface</span>
<p class="title">[Archaeoacoustic resonance](../interfaces/05-archaeoacoustic-resonance.md)</p>
<p class="blurb">The 110 Hz correspondence treated carefully, three independent measurement traditions converging on one number.</p>
</div>
<div class="path-reading-card" markdown>
<span class="step">03 · Result</span>
<p class="title">[Vibrational modes](../results/03-vibrational-modes.md)</p>
<p class="blurb">The actual frequency spectrum of the equation's crystalline regime, 66 Hz, 111 Hz, 22 Hz across dimensions.</p>
</div>
<div class="path-reading-card" markdown>
<span class="step">04 · Result</span>
<p class="title">[Dimensional rescaling](../results/06-dimensional-rescaling.md)</p>
<p class="blurb">Why 2D and 3D frequencies differ, the structural argument for the factor-of-three shift.</p>
</div>
<div class="path-reading-card" markdown>
<span class="step">05 · Principle</span>
<p class="title">[Self-reference (P2)](../principles/02-self-reference.md)</p>
<p class="blurb">Hierarchical memory as a structural principle, why multi-timescale relaxation is structurally required.</p>
</div>
<div class="path-reading-card" markdown>
<span class="step">06 · Cross-substrate</span>
<p class="title">[Optimization-collapse experiment](https://github.com/qrv0/mnsm/blob/main/results/01-optimization-collapse-empirical.md)</p>
<p class="blurb">Cross-substrate analogue of memory-hierarchy failure under sustained pressure. The mental-breakdown structural parallel.</p>
</div>
<div class="path-reading-card" markdown>
<span class="step">07 · Methodology</span>
<p class="title">[Why structural rather than predictive](../methodology/README.md)</p>
<p class="blurb">The framing: the work is presented as structural correspondence, not as a clinical or experimental prediction.</p>
</div>
</div>

## What the work asks of you

The work asks you to consider whether the broadband absorption mechanism it
documents in a deterministic field equation is a **structurally analogous
process** to the gamma-frequency entrainment your field studies in
biological tissue. If you find the structural analogy interesting, the
cross-domain mappings in [`../interfaces/`](../interfaces/README.md) provide
additional context. If you find it forced or insufficient, the work's other
content (the equation, the physics results, the methodology) stands
independently of the gamma-entrainment correspondence; you can engage with
those parts without endorsing the neuroscience interface.

<div class="path-switch" markdown>

**Want the same content framed differently?**

<div class="switch-grid" markdown>
[Physics](if-you-are-from-physics.md)
[Machine learning](if-you-are-from-ml.md)
[Philosophy of science](if-you-are-from-philosophy.md)
[Newcomer](if-you-are-new.md)
</div>

</div>

</div>
