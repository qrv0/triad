# Principles

This folder contains the three structural axioms from which the equation is derived. They are stated as axioms about physical structure rather than as testable predictions; the equation that follows from them is what is testable. The principles themselves are evaluated by the criteria documented in [`../methodology/04-the-six-criteria.md`](../methodology/04-the-six-criteria.md): internal mathematical consistency, reproducibility, generative scope, cross-domain coherence, parsimony, and comprehensiveness.

| File | Principle |
|---|---|
| [`01-oscillation.md`](01-oscillation.md) | **P1.** Every persistent extended entity oscillates. |
| [`02-self-reference.md`](02-self-reference.md) | **P2.** Existence is self-referential, both instantaneously and across time. |
| [`03-coupling.md`](03-coupling.md) | **P3.** Isolation is temporary; coupling is the default. |

Each document states the principle plainly, then explains why it has the mathematical consequence that the [`../equation/`](../equation/) folder develops. The three principles together select a unique mathematical form: a complex field with a nonlinear self-interaction, an integral memory potential, dissipation, and fluctuation-dissipation-locked stochastic forcing. None of the three principles is novel in isolation; what is novel is the structural argument that taken together they admit no degrees of freedom in the form of the equation up to choices of coupling constants.

The principles are not derived from prior physics. They are the input from which the physics is constructed. Their justification, where justification is possible, comes from their universality across physical, biological, and information-theoretic systems, and from the parsimony of the equation they jointly select.

## Why exactly three: the triangle as minimum stable structure

The number three is not chosen for narrative symmetry. It is the minimum number of coupled elements that admits bounded non-trivial dynamics, and this is a mathematical fact about coupled dynamical systems that long predates this work.

A one-element self-interacting system either decays or diverges; there is no third option. A two-element coupled system is integrable in the generic case (Hamiltonian systems on the plane), exhibits at most periodic motion in its bounded sector, and admits no chaos. The first qualitative change of behavior appears at three coupled elements: the Poincaré–Bendixson theorem fails in dimension three; bounded aperiodic trajectories become possible; structurally stable non-trivial attractors appear (Lorenz 1963; Ruelle and Takens 1971). The triangle is the smallest topological structure on which persistent extended dynamics that is neither static nor divergent can live.

P1, P2, P3 are this triangle in axiom form. P1 (oscillation) is one element. P2 (self-reference, both instantaneous and across time) is the second element, coupled to the first via the equation's nonlinearity and memory. P3 (coupling) is the third element, the environment that completes the triangle by exchanging energy and entropy with the first two. The equation derived in [`../equation/`](../equation/) has, correspondingly, exactly three structural blocks of terms: a kinetic generator (from P1), a self-interaction-plus-memory pair (from P2), and a dissipation-plus-noise pair (from P3). Removing any one collapses the system back into the two-element regime where only trivial or divergent dynamics are available; the two-element reductions are catalogued in [`../equation/05-reductions.md`](../equation/05-reductions.md).

The triangle is therefore not a heuristic of the work. It is the topological floor below which the kind of structure the work documents cannot exist. Persistent extended entities are triangles in this technical sense: $\Psi$ couples to its own past via $y$, and both couple to the environment via $\Gamma$ and $\eta$. Two of those would be too few; the work asserts that three is the empirically observed minimum across substrates.
