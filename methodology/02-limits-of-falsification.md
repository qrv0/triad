# The limits of falsification

## The Popperian criterion

Strict Popperian falsificationism (Popper 1959) holds that a scientific theory must make predictions that can in principle be falsified by experiment, and that the appropriate test is to attempt such falsification. The criterion is methodologically powerful: it distinguishes scientific from non-scientific claims, it forces theories to be specific, and it provides a clear procedure for evaluation.

The criterion has, however, well-documented limitations. This document articulates the two that are most consequential for the present work: the Duhem–Quine underdetermination of theory by experiment, and the structural tension between the falsification criterion and the content of P3.

## The Duhem–Quine point

Pierre Duhem (1906) observed that no scientific hypothesis is tested in isolation. Every experimental test invokes a network of auxiliary assumptions: assumptions about the instruments, about the theory of measurement, about the environmental conditions, about the statistical inferences used to interpret the data, and about the broader theoretical framework that gives the experiment its meaning. W. V. O. Quine (1951) extended this analysis: an apparent disconfirmation of a hypothesis never refutes the hypothesis alone; it places stress somewhere in the network of beliefs that the test invoked, and which proposition absorbs the stress is itself a choice.

This is a standard, widely accepted result in philosophy of science. It does not abolish experimental testing — experiments still produce information — but it qualifies what testing accomplishes. The strict falsificationist picture, in which a single experiment can definitively falsify a single hypothesis, is incompatible with the Duhem–Quine analysis.

Within the present work, the Duhem–Quine point operates concretely. Each numerical run invokes assumptions: the floating-point precision of the GPU, the correctness of the cuFFT library, the validity of the Strang splitting at the chosen time step, the reasonableness of the lattice resolution, the appropriateness of the boundary conditions. A surprising numerical result could be attributed to any of these auxiliary assumptions before being attributed to the equation itself. Conversely, an expected numerical result confirms the equation only to the extent that the auxiliary assumptions are themselves trusted.

This is not a defect of the work; it is the standard epistemic situation of any computational investigation. The work mitigates the Duhem–Quine pressure by validating the auxiliary assumptions explicitly: norm conservation in unitary regimes verifies the splitting and the precision; comparison to analytical solutions in dissipative regimes verifies the boundary conditions and the dissipation implementation; the FDT thermalization test verifies the noise correlator. The auxiliary assumptions are tested as separately as the technology permits.

## The structural tension with P3

A second, more specific limitation of the falsificationist criterion arises from the content of P3 (see [`../principles/03-coupling.md`](../principles/03-coupling.md)). P3 asserts that perfect dynamical isolation does not occur. The standard falsificationist test, however, requires the experimental isolation of variables: a hypothesis is tested by setting up an experiment in which one variable is varied, all others held fixed, and a specific predicted outcome is checked.

A theory whose third axiom is "isolation does not occur" cannot be evaluated by experimental methodology that presupposes isolation. The methodology contradicts the content of the theory before any experiment is performed. This is not a quirk of how the present work is framed; it is a structural consequence of the content of P3.

The alternative is not to abandon experimental testing. The alternative is to recognize that the global content of a theory whose principles deny isolation is not the kind of thing that admits single-experiment refutation. The theory's predictions in regimes where isolation is a good approximation — short time, controlled environment, well-screened bath — remain testable in the standard way. Cartwright's (1983) analysis is the appropriate reference: the laws of physics, she argues, are true in their models (which are isolated abstractions) but not in the world (which is not). The model isolates; the world re-couples.

This applies to the present work as follows. The numerical experiments in [`../experiments/physics/`](../experiments/physics/) test specific local predictions of the equation within isolated computational models. Each individual test admits falsification: the anti-collapse separation should be approximately five orders of magnitude in three dimensions; if it were not, the prediction would be false. But the *global content* of the work — the structural claim that the equation captures the form of persistent extended entities in coupled environments — is not the kind of claim that can be falsified by any single test. It is evaluated by the criteria in [`04-the-six-criteria.md`](04-the-six-criteria.md): internal consistency, reproducibility, generative scope, cross-domain coherence, parsimony, comprehensiveness.

## The self-referential failure of the falsificationist criterion

A further point, raised originally by Popper's critics: the falsificationist criterion itself fails its own test. There is no observation that could disconfirm the proposition "only falsifiable claims are scientific." It is a methodological convention, not an empirical claim about reality. Treating it as the universal test of scientific status is a category error.

This does not mean the criterion is wrong. It means the criterion is not in the same category as the empirical hypotheses it is used to evaluate. Foundational propositions in mathematics, conservation principles in physics, and structural-realist positions in metaphysics all fail the falsification criterion and are accepted because they pass other criteria — typically: they are internally consistent, productively generative, parsimonious, and consistent with the network of accepted theories that depends on them. The present work is accepted or rejected by the same standards.

## The cost of not adopting strict falsification

We have not adopted strict Popperian falsificationism as the methodological frame. There is a cost to this choice that we acknowledge.

The cost is that the work does not produce a single decisive experiment whose outcome would refute it. A reader committed to strict falsificationism may therefore find the work unsatisfying: there is no "if this experiment fails the theory dies" moment. The reasons we have not provided such a moment are structural — P3 forbids it — and not stylistic.

What the work provides instead is a body of locally-falsifiable predictions (the anti-collapse separation magnitudes, the BCC selection, the dimensional rescaling) embedded in a larger structural claim evaluated by cross-domain coherence. The locally-falsifiable predictions can be tested in the standard way; they pass or fail on the numerics. The larger structural claim is evaluated by whether the same form appears in independently documented domains, which is the structural-realist test.

## What this entails for engagement with the work

A reader committed to strict falsificationism is invited to test the locally-falsifiable predictions. The reproduction scripts in [`../experiments/`](../experiments/) execute the relevant numerical tests. If the predictions fail to reproduce, the work has a problem. If they reproduce, the local predictions are confirmed in the standard sense.

A reader committed to structural realism is invited to test the cross-domain coherence claim. The mappings in [`../interfaces/`](../interfaces/) are the principal evidence. The state space model equivalence is the strongest (mathematically exact); the archaeoacoustic correspondence is the weakest (calibration-dependent). The cumulative weight of the six mappings is the test.

The work does not require its reader to adopt one or the other position. It does require the reader to recognize that the global content is evaluated structurally and that this is a deliberate methodological choice, not an evasion of accountability.

## References

- Cartwright, N. (1983). *How the Laws of Physics Lie*. Oxford University Press.
- Duhem, P. (1906). *La Théorie Physique: son objet et sa structure*. Chevalier et Rivière, Paris.
- Popper, K. (1959). *The Logic of Scientific Discovery*. Hutchinson, London.
- Quine, W. V. O. (1951). Two dogmas of empiricism. *The Philosophical Review* **60**, 20.
