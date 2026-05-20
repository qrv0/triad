# P2, Existence is self-referential

## Statement

A persistent entity is defined by its relation to itself, both instantaneously and across its own past.

## Motivation

Identity over time presupposes self-reference. An entity that does not relate to itself across time has no continuous identity; what would be called "the entity at time $t_1$" and "the entity at time $t_2$" would be two distinct objects with no relation between them. The persistence of the entity *is* the continuity of self-reference. Whatever it is about the entity at $t_2$ that makes it the same entity as the one at $t_1$ is a relation between the two.

This relation has two structural parts. The first is instantaneous: at every moment, the entity acts on itself through its own state. A field with nontrivial density acts on its own dynamics through that density. A neural state acts on its own subsequent dynamics through its current configuration. A particle in a self-consistent mean field acts on its own trajectory through the mean field it generates. The instantaneous part of self-reference is the nonlinearity of the entity in its own state variable.

The second part is across time: the entity's current state depends not only on its instantaneous configuration but on a weighted integral of its past configurations. This is memory. The entity is, in part, the trajectory of its own history. The same instantaneous state at two different moments can correspond to entirely different subsequent dynamics if the histories that produced those instantaneous states differ.

P2 asserts that both parts of self-reference are structurally necessary. An entity defined only by instantaneous self-coupling is Markovian: its future depends only on its present, and its identity is restricted to whatever can be encoded in a single state vector. An entity defined only by integral memory without instantaneous coupling is linear in its state: it carries information about its history but cannot act nontrivially on its current configuration. Persistent extended entities exhibit both kinds of self-reference simultaneously.

P2 is the second vertex of the three-element structure documented in [`README.md`](README.md). Self-reference without oscillation gives a fixed point; self-reference without environmental coupling gives an isolated Hamiltonian that either conserves itself trivially or runs away. Both the oscillation (P1) and the coupling (P3) are required for self-reference to produce a persistent extended entity rather than a static or runaway one.

## Mathematical consequence

The instantaneous part of P2 manifests as the cubic Gross–Pitaevskii term:

$$
\Lambda |\Psi|^2 \Psi
$$

where $\Lambda$ controls both the strength and the sign of self-interaction. Attractive coupling ($\Lambda < 0$) makes the field act on itself to concentrate; repulsive coupling ($\Lambda > 0$) makes it act on itself to disperse. The cubic form is the lowest-order nonlinearity consistent with the gauge invariance of the underlying complex field; higher-order terms ($|\Psi|^4$, $|\Psi|^6$) are possible but not required by P2 and are not included unless a specific physical motivation demands them.

The across-time part of P2 manifests as the integral memory potential:

$$
V_{\text{mem}}(t, \mathbf{x}) = \int_0^t dt' \int d^n x'\, \hat{U}(t - t', \mathbf{x}, \mathbf{x}')\, |\Psi(t', \mathbf{x}')|^2,
$$

where $\hat{U}$ is a memory kernel that weights past density values by their separation in time and (optionally) in space. A kernel that is a sum of decaying exponentials in time and a delta function in space admits an exact Markovian embedding via auxiliary fields, as derived in [`../equation/02-markovian-embedding.md`](../equation/02-markovian-embedding.md). This embedding is what makes the integral memory potential computationally tractable without sacrificing its non-Markovian character.

## A structural observation about the two parts

The instantaneous and across-time parts of self-reference act on different scales. The instantaneous part is a local algebraic operation: at each point, $\Lambda |\Psi|^2$ contributes to the local potential without reference to any other point or any other time. The across-time part is non-local in time and (optionally) non-local in space: it accumulates information from elsewhere in spacetime.

The dynamical consequence of having both is qualitatively different from having either one alone. As documented in [`../results/01-anti-collapse-2d.md`](../results/01-anti-collapse-2d.md), the integral memory potential by itself does nothing if there is no nonlinearity to amplify the signal it tracks. The cubic nonlinearity by itself, in two-dimensional supercritical or three-dimensional supercritical regimes, drives finite-time blow-up. Together they generate an anti-collapse mechanism that is absent from either limit: the memory accumulates the rising density during the collapse phase and, with lag set by the inverse relaxation rate $\nu_j$, builds a repulsive potential that overshoots the attractive nonlinearity and releases the field outward. The mechanism is neither memory alone nor nonlinearity alone; it is the coupling of the two, which P2 requires structurally.

## What P2 does not assert

P2 does not specify the form of the memory kernel. A single exponential, a sum of exponentials, a power law, or a more exotic kernel are all admissible under P2. The choice is determined by the physical system being modeled and by the requirement of computational tractability. The multi-exponential choice used in this work is the most economical kernel that admits exact Markovian embedding while still being able to represent multiple temporal scales of memory.

P2 does not assert that all the entity's past is equally weighted in its current state. The kernel weights past states by their separation from the present. P2 only asserts that the weighting is nontrivial across some range, which is to say that the kernel is not a delta function in time.

## Cross-domain reading

Under P2, the relevant cross-domain question is "does this system exhibit both instantaneous self-coupling and temporal memory?" The answer in the cases documented in [`../interfaces/`](../interfaces/) is uniformly yes. The clearest mathematical instance is the correspondence with structured state space models (see [`mnsm/interfaces/01-state-space-models.md`](https://github.com/qrv0/mnsm/blob/main/interfaces/01-state-space-models.md)): the hidden state of an SSM is, formally, the auxiliary-field embedding of an integral memory, and the nonlinearity that recent variants such as Mamba introduce through input-dependent gating is, formally, an approximation to the cubic self-interaction P2 demands. The two parts of P2 are present in both formulations; they are present in the architecture because the architecture is solving the same structural problem as the equation.
