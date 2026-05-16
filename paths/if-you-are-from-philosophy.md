# If you are from philosophy of science

You are familiar with structural realism, the Duhem–Quine thesis, the limits of strict falsificationism, the literature on theory-change and the preservation of structure across paradigm shifts. This document gives you the fast route to the philosophical content of this work.

## The position

The work adopts a moderately strong version of structural realism. The mathematical structure of the equation is what we propose to be the load-bearing object of knowledge; the specific physical substrates onto which the structure maps are instantiations, not the primary referents of the theory.

The position is articulated explicitly in [`../methodology/01-structural-realism.md`](../methodology/01-structural-realism.md). The key citations are Worrall (1989), Ladyman & Ross (2007), Cartwright (1983), Duhem (1906), and Quine (1951). The position is not novel; what is potentially novel is its operationalization: the work places the methodological frame at the same level as the mathematical equation, treats cross-domain mappings as first-class content rather than appendix material, and articulates an explicit alternative to strict Popperian falsification.

## The structural tension that motivates the position

The equation is derived from three structural axioms (P1, P2, P3, articulated in [`../principles/`](../principles/)). The third axiom — coupling is the default, isolation is temporary — has direct implications for how the equation should be evaluated. A theory whose third axiom asserts that perfect dynamical isolation does not occur cannot consistently be evaluated by an experimental methodology that presupposes isolation, which is what strict Popperian falsificationism requires.

The argument is detailed in [`../methodology/02-limits-of-falsification.md`](../methodology/02-limits-of-falsification.md). The structural tension between content and methodology is not a defect of the work to be overcome; it is what motivates the methodological choice. The work argues, drawing on Cartwright's analysis, that the appropriate response is to evaluate the global structural claim by criteria appropriate to structures (the six criteria in [`../methodology/04-the-six-criteria.md`](../methodology/04-the-six-criteria.md)), while continuing to evaluate locally-falsifiable predictions in the standard way.

## What the work is doing methodologically

The work treats the cross-domain co-occurrence of a specific mathematical structure as the principal evidence for the structural-realist claim about that structure. The six cross-domain interfaces in [`../interfaces/`](../interfaces/) are presented as independent instances of the same mathematical form, drawn from physically and computationally distinct domains. The strongest of these is a mathematically exact equivalence with structured state space models in machine learning ([`../interfaces/06-state-space-models.md`](../interfaces/06-state-space-models.md)); the weakest is a calibrated mapping to archaeoacoustic resonance data ([`../interfaces/05-archaeoacoustic-resonance.md`](../interfaces/05-archaeoacoustic-resonance.md)).

The work distinguishes carefully between cross-domain correspondences that are mathematical (no calibration required) and those that are structural-but-calibrated (the form is the same but the specific numerical values require a choice of dimensional units). It does not treat all six as equally weighty evidence; the philosophical readers will find the discussion of evidentiary weight in [`../interfaces/README.md`](../interfaces/README.md) and the individual interface documents.

## The reflexive consistency of the work

A point that may interest philosophers of science specifically: the work attempts a degree of reflexive consistency between its content and its presentation. The third structural principle is that coupling is the default; the repository is organized so that the documents are coupled across folders rather than partitioned into isolated silos. The self-referential principle (P2) is instantiated in the repository's `STRUCTURE.md`, a document that explains its own organization in terms of the principles it documents.

Whether this reflexive consistency is methodologically required or stylistic is a separate question; the work makes the consistency explicit in [`../STRUCTURE.md`](../STRUCTURE.md) and the reader is free to judge.

## What may interest you specifically

Four aspects of the work may be of specific philosophical interest beyond the general structural-realist framing.

**The operationalization of "evaluation by criteria appropriate to structures."** Worrall's and Ladyman & Ross's structural realism articulates the position but does not always specify in detail what evaluation under the position looks like in practice. The six criteria in [`../methodology/04-the-six-criteria.md`](../methodology/04-the-six-criteria.md) attempt an operational version: internal consistency, reproducibility, generative scope, cross-domain coherence, parsimony, comprehensiveness. The work's self-assessment against each criterion is provided as a worked example.

**The dimensional-identification problem.** Several of the cross-domain mappings ([`../interfaces/04-gamma-entrainment.md`](../interfaces/04-gamma-entrainment.md), [`../interfaces/05-archaeoacoustic-resonance.md`](../interfaces/05-archaeoacoustic-resonance.md)) depend on a choice of dimensional units to compare the equation's frequencies to physical Hz. The work is explicit that this is a choice. The philosophical question of how much weight a calibration-dependent cross-domain correspondence carries — and whether the structural-realist position can absorb such correspondences as evidence — is a substantive issue that the work brings into the open rather than concealing.

**The recursive structure of P3.** P3 forbids the recursive postulation of any final, truly isolated system. Strictly, this entails that the bath to which a system is coupled is itself coupled to a further bath, indefinitely. The philosophical question of whether this generates a vicious regress or a productive structural feature is not resolved in the work but is articulated in [`../principles/03-coupling.md`](../principles/03-coupling.md).

**An empirical instance of the structural-realist prediction.** The structural-realist position predicts that if a mathematical form is real, the same form should appear in independently observed phenomena across substrates that were not coordinated to share it. The optimization-collapse experiment documented in [`../results/08-optimization-collapse-empirical.md`](../results/08-optimization-collapse-empirical.md) is one such empirical instance: the anti-collapse mechanism derived from the equation in 3D NLS field dynamics manifests in a categorically different substrate (gradient descent in 70M-parameter neural network), with no design coordination between the two substrates. This is the kind of cross-substrate confirmation the structural-realist methodology identifies as evidence; the philosophical question of whether one such empirical instance suffices to corroborate the position, and what additional independent instances would be required, is left open.

## Recommended path

In order:

1. [`../principles/`](../principles/) — The three structural axioms.
2. [`../methodology/01-structural-realism.md`](../methodology/01-structural-realism.md) — The position.
3. [`../methodology/02-limits-of-falsification.md`](../methodology/02-limits-of-falsification.md) — The Duhem–Quine and structural-tension arguments.
4. [`../methodology/04-the-six-criteria.md`](../methodology/04-the-six-criteria.md) — The criteria and self-assessment.
5. [`../interfaces/README.md`](../interfaces/README.md) — The cross-domain framing.
6. [`../interfaces/06-state-space-models.md`](../interfaces/06-state-space-models.md) — The mathematically exact correspondence (the strongest evidence).
7. [`../interfaces/05-archaeoacoustic-resonance.md`](../interfaces/05-archaeoacoustic-resonance.md) — The calibration-dependent correspondence (the weakest in evidentiary terms but the most philosophically interesting because of the calibration question).
8. [`../STRUCTURE.md`](../STRUCTURE.md) — The reflexive consistency of repository organization with the principles it documents.
9. [`../paper/manuscript.md`](../paper/manuscript.md), §7 and §8 — The synthesized methodological position in paper form.

The equation and its numerical results are technical content that you may or may not engage with directly. The philosophical content stands independently of the technical content in the sense that the position is consistent and the criteria are articulated regardless of whether the specific numerical findings hold; conversely, if the numerical findings fail, the philosophical position remains a position about how to evaluate work of this kind, even if this particular instance does not survive its own evaluation.

## What the work asks of you

The work asks you to consider whether structural realism, articulated and operationalized in this way, is a defensible position from which to evaluate cross-domain mathematical structures. It does not ask you to endorse this specific work; the work itself is the case study, and the philosophical position is what the work tries to instantiate. If you find the position defensible and the instantiation faithful, the work succeeds on its own terms. If you find the position defensible but the instantiation flawed, your critique is the kind of philosophical engagement the work invites. If you reject the position, the work's other content (the equation, the physics results) does not depend on the philosophical framing and can be evaluated independently.
