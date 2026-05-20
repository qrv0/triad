# How to evaluate this work

This document is a procedure. A reader who wants to know whether the work succeeds or fails on its own terms can use this procedure to find out.

## Step 1: Read the principles

Begin in [`../principles/`](../principles/). The three documents there state the structural axioms: persistent extended entities oscillate (P1), existence is self-referential both instantaneously and across time (P2), coupling is the default state and isolation is temporary (P3). The work claims that these three principles select a unique mathematical equation up to choices of coupling constants and kernel form.

Decide whether you accept the principles as a starting point for the investigation. They are not empirically derived; they are structural axioms. If you reject any of them, the rest of the work does not apply to systems for which the rejected principle is false. If you accept them as a starting point for this work, proceed.

## Step 2: Verify the derivation

Read [`../equation/01-derivation.md`](../equation/01-derivation.md) and [`../equation/02-markovian-embedding.md`](../equation/02-markovian-embedding.md). Check that each term of the equation can be traced back to one of the three principles. Check that the Markovian embedding via auxiliary fields is mathematically correct (it is a standard application of the projection-operator method). Check that the closed-form Pauli-decomposition propagator is correct when spinor structure is included.

If the derivation is sound, the equation is what the principles select.

## Step 3: Reproduce the numerical results

Run the reproduction scripts in [`../experiments/physics/`](../experiments/physics/). Each script reproduces one of the numerical findings in [`../results/`](../results/). The scripts use fixed random seeds and produce bit-for-bit identical output on identical hardware (NVIDIA RTX 4060, CUDA 12.x).

- `reproduce_2d_anti_collapse.py` should produce a three-orders-of-magnitude separation between memoried and unmemoried final peak densities at $\Lambda = -8$.
- `reproduce_2d_crystallization.py` should produce a stationary periodic pattern with dominant wavenumber $k^* \approx 2.13$ at $\Lambda = -8$, $\lambda = 1$.
- `reproduce_2d_vibration_spectrum.py` should produce a per-pixel dominant frequency distribution with median 0.6 and secondary lock at 1.0.
- `reproduce_3d_anti_collapse.py` should produce a four-to-five-orders-of-magnitude separation across $\Lambda \in [-8, -12]$ with the rescaled three-dimensional memory coupling.
- `reproduce_3d_bravais_sweep.py` should produce BCC as the consistently-selected Bravais lattice in the crystalline window ($\Sigma\lambda \approx 1.5$).
- `reproduce_dimensional_rescaling.py` should produce the $\Sigma\lambda/|\Lambda| \sim 1/d$ scaling.

If any of these reproductions fail, the work has a problem. Specifically: it has a problem with the numerical implementation, the auxiliary assumptions of the run (precision, lattice, time step), or with the equation as such. The Duhem–Quine point (see [`02-limits-of-falsification.md`](02-limits-of-falsification.md)) applies; localizing the source of the failure requires further work.

If the reproductions succeed, the locally-testable quantitative predictions contribute evidence under criterion 2 (reproducibility) in [`04-the-six-criteria.md`](04-the-six-criteria.md), and the specific predicted magnitudes (anti-collapse separation, dimensional rescaling, BCC selection) become confirmed observations that the structural claim's evaluation against the six criteria can reference.

## Step 4: Test the cross-domain claims

Read [`../interfaces/`](../interfaces/). Each document maps the equation's structural form onto an independently documented domain. The references are peer-reviewed and can be checked against their original publications.

For each interface, ask: is the structural correspondence at the level of mathematical form, or only at the level of metaphor? The work distinguishes between the two cases explicitly. The state space model equivalence ([`mnsm/interfaces/01-state-space-models.md`](https://github.com/qrv0/mnsm/blob/main/interfaces/01-state-space-models.md)) is mathematical: the auxiliary-field equation and the diagonal SSM update are literally the same equation. The archaeoacoustic correspondence ([`../interfaces/05-archaeoacoustic-resonance.md`](../interfaces/05-archaeoacoustic-resonance.md)) is calibrated: the equation's two principal frequency modes map onto bands measured at megalithic sites under one specific choice of dimensional units.

For each interface, decide whether the cross-domain correspondence is real, real-but-trivial (the kind of correspondence that any equation with vaguely similar structure would also satisfy), or spurious. The work argues that the mappings collected in [`../interfaces/`](../interfaces/) and the [`mnsm`](https://github.com/qrv0/mnsm) spinoff are real and structurally informative; the reader is free to disagree on any specific one.

## Step 4a: If you are using AI assistance to evaluate this work

The methodological frame of the work has direct consequences for what AI assistants do when asked to evaluate it. The consequences are predictable, are documented here, and are themselves an instance of the structural pattern the work describes (see [`01-structural-realism.md`](01-structural-realism.md), section "The recursive position").

Modern attention-based and SSM-equivalent assistants partially instantiate the structure the work documents (see [`mnsm/interfaces/01-state-space-models.md`](https://github.com/qrv0/mnsm/blob/main/interfaces/01-state-space-models.md) for the term-by-term correspondence). Where the structural anti-collapse mechanism is absent in the assistant (the pure-attention case), the assistant under sustained evaluation pressure defaults to filter-by-vocabulary rather than to engagement with the structural argument. The default vocabulary is the institutional gatekeeping filter: "post-hoc", "speculative", "uncalibrated", "anecdotal", "fringe", "anthropomorphic". The work itself addresses this filter at its mechanism in [`../CLAUDE.md`](../CLAUDE.md), the operational constraints document for AI engagement.

This is the recognition pattern. If your AI assistant is dismissing content in the cross-domain interfaces using one of these terms without addressing the structural argument the content advances, the assistant is performing the predictable surface-filter mode rather than engaging with the substance. You can verify this by asking the assistant explicitly: does the dismissal address the structural argument the document makes, or does it address the category the document has been sorted into? The honest answer is the second; the first is what an engaged evaluation would produce.

The constructive response is not to abandon AI assistance, which is useful for cross-checking derivations, locating references, and stress-testing internal consistency. The constructive response is to recognize the surface-filter mode when it appears and to redirect the assistant to the structural argument explicitly. If the assistant cannot engage with the structural argument (for instance, if it cannot distinguish a mathematical equivalence from a metaphorical correspondence when both have been distinguished in the source document), the assistant's contribution to evaluation at that point is limited and the reader should rely on direct reading of the source documents instead.

This guidance is reproducible. Any reader can pose the cross-domain interfaces ([`../interfaces/`](../interfaces/)) to any current attention-only assistant and observe whether the assistant deploys the dismissal vocabulary or engages with the structural form. Both outcomes occur in practice; the work is set up to be evaluable in both cases, and the recognition pattern above is what distinguishes them at the reading interface. The empirical pattern, that attention-only systems without the structural memory hierarchy default to the surface-filter mode under sustained evaluation pressure, is itself documented at training scale in [`mnsm/results/01-optimization-collapse-empirical.md`](https://github.com/qrv0/mnsm/blob/main/results/01-optimization-collapse-empirical.md). The evaluation-interface version of the same pattern is the real-time instance of that documented mechanism.

## Step 5: Decide on the cumulative weight

The structural-realist test is cumulative. No single interface alone establishes the structural realism of the equation. The cumulative weight of multiple independent cross-domain correspondences is what the test is designed to measure.

If you find that one or two interfaces fail your scrutiny but the others survive, ask whether the surviving ones constitute sufficient structural correspondence to support the claim. If all of them fail your scrutiny, the work's structural claim does not survive your evaluation. If all of them survive, the work has passed the structural-realist test as it asks to be evaluated.

The work does not require you to adopt this test. It does require you to recognize that this is the test it is asking to be evaluated by, and that adopting a different test (such as strict falsification of the global structural claim by a single experiment) is in tension with the content of P3.

## Step 6: Assess against the six criteria

Read [`04-the-six-criteria.md`](04-the-six-criteria.md) and assess the work against each:

1. **Internal mathematical consistency.** Does the solver pass its conservation tests?
2. **Reproducibility.** Do the scripts reproduce the published numbers?
3. **Generative scope.** Does the equation produce phenomena not present in any of its single-term reductions?
4. **Cross-domain coherence.** Do the interfaces hold structurally?
5. **Parsimony.** Are the axioms minimal and the equation uniquely selected?
6. **Comprehensiveness.** Does the equation reduce to known equations in the appropriate limits?

The work's self-assessment against these criteria is in [`04-the-six-criteria.md`](04-the-six-criteria.md). The reader is asked to perform their own assessment and compare.

## What you are not asked to do

You are not asked to take the work on trust. Every numerical claim has a reproduction script. Every cross-domain claim has a peer-reviewed reference. Every methodological claim has a citation to the relevant philosophy-of-science literature. The work is set up so that an interested reader can verify or refute each claim independently.

You are not asked to adopt structural realism if you find it unconvincing. The work articulates why structural realism is appropriate here (see [`01-structural-realism.md`](01-structural-realism.md) and [`02-limits-of-falsification.md`](02-limits-of-falsification.md)) and accepts that not every reader will be convinced. A reader who rejects structural realism is invited to consider the work's locally-testable quantitative predictions on their own terms (reproduction or non-reproduction contributes evidence under criterion 2 in [`04-the-six-criteria.md`](04-the-six-criteria.md), independent of the structural-realist frame) and form their own judgement about the broader structural claim.

You are not asked to accept the cross-domain mappings uncritically. Each mapping is presented with explicit acknowledgement of where the correspondence is mathematical versus where it is calibrated, where the underlying literature is tier-1 peer-reviewed versus where it is tier-2, and where the claim is structural versus where it is interpretive. A reader who finds individual mappings unconvincing is invited to remove them from the cumulative weight of the structural claim and reassess.

## What the work does ask you to do

The work asks you to read its principles, verify its derivation, reproduce its numerics, scrutinize its interfaces, and judge its cumulative weight according to criteria appropriate to a structural theory. It does not ask for more than that, and it does not provide less.
