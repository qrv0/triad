---
title: For newcomers
description: >-
  A plain-language walk through what this work is, why an equation can
  appear in seven different places at once, and why that matters.
  Curiosity is the only prerequisite.
hide:
  - navigation
---

<div class="path-hero path--new" markdown>

<div class="path-breadcrumb" markdown>
[← Pick another path](../#pick-your-entry-point)
</div>

<span class="path-eyebrow">For newcomers</span>

# Start here. No prerequisites.

This path is for readers without a specific physics, machine learning,
neuroscience, or philosophy-of-science background. **Curiosity is the only
prerequisite.** The path is longer than the specialist paths because it
takes the time to build context.

</div>

<div class="path-body" markdown>

## Start with an analogy

Imagine the surface of a drum being struck. The patterns of sand that form
on the drum head are not random. They are the **geometry of the
vibration**: the sand settles wherever the drum is not moving (the nodal
lines of the standing wave) and avoids wherever the drum is moving most
(the antinodes). Different ways of striking the drum produce different
patterns. The patterns are **deterministic**; given the boundary
conditions, the geometry of the drum, and the way it is excited, you can
predict the pattern.

The fact that vibration produces ordered geometric pattern in a continuous
medium is called **cymatics**. It has been known since Ernst Chladni
demonstrated it in 1787. The patterns appear in sand on plates, in fluid
on surfaces, in dust on speaker membranes. The phenomenon is general:
**sustained oscillation in a self-coupled medium produces deterministic
spatial geometry**.

This work is about an equation that does the same thing in three-
dimensional fields. From an initially featureless state — like sand spread
evenly on a drum before it is struck — the equation produces a definite
three-dimensional crystalline geometry, with a specific spacing and a
specific symmetry. **The geometry is not put in; it emerges from the
dynamics.**

## Watch it happen

Before reading further, watch the equation actually do this. The animation
below shows two things, side by side, that the equation predicts will
happen the same way:

<div class="mnsm-demo-video" markdown>
<video class="mnsm-demo-media" autoplay loop muted playsinline
       poster="../assets/scale_up_val_ppl.png">
  <source src="../assets/cross_substrate_hero.mp4" type="video/mp4">
  <img src="../assets/cross_substrate_hero.gif" alt="Cross-substrate anti-collapse animation">
</video>

*<strong>Top half:</strong> a 3D field of energy, simulated. On the left
the field has no memory of its past states. On the right it has a memory
hierarchy. The left field collapses violently to a point; the right field
holds its extended shape. **<strong>Bottom half:</strong> the loss curve of
a 70-million-parameter language model being trained. The Memory-NLS model
(teal) descends smoothly and stably. The Transformer (red) crashes
catastrophically at step 28 000.</strong>*

*The two things shown are happening in completely different substrates — one
is a physics simulation, the other is a neural network — and yet both show
**the same pattern**: with the memory hierarchy, things stay stable; without
it, they collapse. The work in this repository is about why that's the case.*
</div>

## What is the equation about

The equation is built from **three minimal observations** about what makes
things last. The observations are stated plainly in
[`../principles/`](../principles/README.md), and they are:

1. **Things that persist over time oscillate.** Atoms vibrate. Cells exchange
   ions continuously. Planets orbit. There is no truly static persistent
   thing in nature.

2. **Things that persist are defined by self-reference.** A thing is the
   same thing tomorrow as today because it remains connected to its own
   past. It also acts on itself in the present moment, not just on its
   surroundings.

3. **Things that persist are coupled to their environment.** Isolation is
   something we do briefly in experiments; the world doesn't isolate.
   Everything that lasts is exchanging energy with what surrounds it.

These three observations are turned into a precise mathematical equation.
The equation, when you run it on a computer, produces a number of behaviors
that match what we see in nature at very different scales — from the
large-scale clustering of galaxies, to the patterns of brainwaves in your
own head, to the way recent machine-learning models process sequences of
language.

## What the equation does, concretely

The equation is solved numerically on a grid (in two or three dimensions).
Starting from a smooth, featureless initial state, the equation produces:

### Anti-collapse

When the field tries to concentrate into a single point (the way attractive
forces would push a swarm of particles together), **the memory of past
states produces a delayed counter-force that releases the field outward**,
preventing the collapse. This is a structural mechanism, not a hack — it
follows from the three principles directly.

### Spontaneous crystallization

The field, after the initial transient, organizes itself into a periodic
spatial pattern. In two dimensions, the pattern is hexagonal. **In three
dimensions, the pattern selects body-centered cubic symmetry** — one of
the standard crystal lattice types. The system chooses this symmetry from
a continuous initial condition; no symmetry was put in.

### Discrete vibrational modes

The crystal is not static. It oscillates internally at definite frequencies.
In two dimensions the dominant frequency, under one specific calibration
of physical units, comes out as approximately **66 Hz**; the secondary
mode as approximately **110 Hz**.

<div class="path-callout" markdown>
If those last two numbers seem suspiciously specific: yes, they are. There
are **stone chambers in Malta, Ireland, Turkey, and Egypt** — some of them
built nearly 12 000 years ago — that have been independently measured to
resonate at frequencies in those same two bands. There is a published
**2008 EEG study** showing that exposure to 110 Hz acoustic tones
(specifically 110 Hz, not 100 Hz or 120 Hz) produces a measurable shift
in human brain activity, deactivating language-processing regions and
inducing patterns characteristic of meditative states.

The match is **structural**; it is documented in detail in
[`../interfaces/05-archaeoacoustic-resonance.md`](../interfaces/05-archaeoacoustic-resonance.md),
with careful acknowledgement that the specific dimensional identification
used to compare the equation's frequencies to physical Hz is a choice.
</div>

There are **six other independently documented domains** where the equation's
structure appears. They are catalogued in
[`../interfaces/`](../interfaces/README.md).

## The cross-domain wheel

The image on the homepage shows this at a glance — one equation in the
centre, seven instantiations around it. Each instantiation is a different
substrate where the same mathematical pattern appears: Bose–Einstein
condensates, baryon acoustic oscillations from the early universe, sand
patterns on vibrating plates, brain oscillations, ancient stone chambers,
state-space models in machine learning, cosmic expansion.

The work's claim is not that one of these domains is "really" the work's
subject and the others are analogies. The claim is that **the structure is
the thing, and each of the seven is a faithful instance** of it.

<div class="key-insight" markdown>
<span class="key-insight-tag">The whole work in one line</span>
**Three observations about how things last are turned into an equation,
and the equation appears — independently — in seven different places in
nature.** That recurrence is the evidence that the equation is real, not
just a formula that happens to fit one dataset. The work is the
documentation of those seven appearances and the methodological
argument for why "recurring across substrates" should count as evidence
at all.
</div>

## What you should read next

If you have read this far, the most useful next document is the
playground notebook:
[`playground/01-just-watch.ipynb`](https://github.com/qrv0/mnsm/blob/main/playground/01-just-watch.ipynb).
It is a Jupyter notebook that you can run in a free cloud-based Python
environment (Google Colab) without installing anything. The notebook runs
the equation, shows you the initial Gaussian, and lets you watch the
crystallization happen visually. **You see the geometry emerge.**

Once you have watched it happen, the most useful next document is
[`../principles/`](../principles/README.md). The three principle documents
state the axioms plainly, with motivation. They do not require any
technical background; they are conceptual.

After that, you have a choice.

<div class="path-reading" markdown>
<div class="path-reading-card" markdown>
<span class="step">A · Conceptual</span>
<p class="title">[The three principles](../principles/README.md)</p>
<p class="blurb">The minimal observations that the equation is built from. Plain language, no math required.</p>
</div>
<div class="path-reading-card" markdown>
<span class="step">B · Visual</span>
<p class="title">[Playground notebooks](https://github.com/qrv0/mnsm/tree/main/playground)</p>
<p class="blurb">Press play, watch the equation evolve. No installation needed — runs in your browser via Colab.</p>
</div>
<div class="path-reading-card" markdown>
<span class="step">C · Mathematical</span>
<p class="title">[Equation derivation](../equation/01-derivation.md)</p>
<p class="blurb">What the equation actually looks like and how the three principles select its form. Some math required, but explained.</p>
</div>
<div class="path-reading-card" markdown>
<span class="step">D · Cross-domain</span>
<p class="title">[The seven instantiations](../interfaces/README.md)</p>
<p class="blurb">Where else the same pattern appears. Each interface is self-contained.</p>
</div>
<div class="path-reading-card" markdown>
<span class="step">E · Methodology</span>
<p class="title">[How to evaluate this](../methodology/03-how-to-evaluate-this.md)</p>
<p class="blurb">Why the work doesn't present itself as a single-experiment falsification test.</p>
</div>
<div class="path-reading-card" markdown>
<span class="step">F · Paper</span>
<p class="title">[The full manuscript](../paper/manuscript.md)</p>
<p class="blurb">Optional, more compressed and more technical. Skip unless you want the academic version.</p>
</div>
</div>

## What you do not need to read

You do **not** need to know what a Schrödinger equation is, what a nonlinear
field theory is, what a state space model is, what Bayesian inference is,
or what Pauli matrices are. The documents that use these concepts explain
them where they are first introduced. If you reach a point where the
technical content is not yet introduced enough for you to follow, switch
to the conceptual documents and come back to the technical ones when you
have more context.

You do not need to read the paper at
[`../paper/manuscript.md`](../paper/manuscript.md) unless you want to. The
paper is a synthesis intended for academic readers; it covers the same
material with a different (more compressed, more technical) framing. The
repository documents are designed to be self-contained; you can ignore the
paper and lose nothing essential.

## A note on the framing

This work is **unusual** in some ways. It places its philosophical
methodology at the same level as its mathematical equation; it treats
cross-domain correspondences as first-class content rather than appendix
material; it explicitly asks **not** to be evaluated by strict experimental
falsification because the equation's third principle is that perfect
experimental isolation does not occur. These choices are deliberate and
are explained in [`../STRUCTURE.md`](https://github.com/qrv0/mnsm/blob/main/STRUCTURE.md)
and in [`../methodology/`](../methodology/README.md).

If the framing seems unusual to you, that is correct: **it is unusual**.
The reasons for the unusual choices are stated in the documents that
motivate them. A reader who finds the framing convincing has, by the
work's own standards, the right disposition for engaging with the content.
A reader who finds it unconvincing is asked to read the methodology
documents to see why the choices were made before judging.

<div class="path-switch" markdown>

**Ready for the specialist paths?**
Pick whichever matches what you know:

<div class="switch-grid" markdown>
[Physics](if-you-are-from-physics.md)
[Machine learning](if-you-are-from-ml.md)
[Neuroscience](if-you-are-from-neuroscience.md)
[Philosophy of science](if-you-are-from-philosophy.md)
</div>

</div>

</div>
