# If you are from physics

You are familiar with nonlinear Schrödinger dynamics, with the Gross–Pitaevskii equation in BEC, with stochastic field theory and FDT, with Mori–Zwanzig projection-operator methods. The work in this repository sits in the intersection of these. This document gives you a fast route through it.

## What the equation is

The equation is the cubic nonlinear Schrödinger equation with three structural additions: an integral memory potential reducible to auxiliary fields via Markovian embedding; FDT-locked dissipation and noise; and optional fractional spatial dispersion and Rashba spinor structure. The Markovian embedding is the standard projection-operator reduction of an integro-differential memory kernel; the FDT lock is the standard stochastic-field-theory prescription for thermalization in open systems; the fractional and spinor structures are optional and recover well-studied special cases.

What is new is not the addition of any one of these terms individually — each is established in its respective sub-field — but the structural claim that the three terms (cubic nonlinearity, integral memory, FDT-locked coupling) are jointly required by a minimal set of axioms about persistent extended entities, and that the equation produced by including all three exhibits qualitative behavior absent from any of its single-term reductions.

The full equation, in compact form:

$$
i\hbar\, \partial_t \Psi = \left[\,-\frac{\hbar^2}{2m} D^2 + V_{\text{ext}} + \Lambda |\Psi|^2 + V_{\text{mem}} + \alpha (-\Delta)^{\sigma/2} - i\Gamma\,\right]\Psi + \eta,
$$

with $V_{\text{mem}} = \sum_j \lambda_j y_j$, $\partial_t y_j = \nu_j(\rho - y_j)$, and $\eta$ obeying the classical FDT correlator.

Detail: [`../equation/01-derivation.md`](../equation/01-derivation.md).

## What the equation does that bare cubic NLS does not

Three results stand out as inaccessible from the bare cubic NLS:

**Anti-collapse via memory.** In 2D L²-critical NLS with $\Lambda = -8$ and initial norm above the Townes threshold, the bare equation produces lattice-clipped collapse. The memory-augmented equation produces a three-orders-of-magnitude separation between memoried and unmemoried final peak densities. The mechanism is delayed repulsion: the auxiliary fields lag the rising density, generate a transiently larger memory potential than the steady-state equilibrium, and this overshoot exceeds the attractive cubic interaction at the focal point, releasing the field outward. The slow memory mode ($\nu = 0.5$, $\tau = 2$) is structurally essential — the fast mode alone cannot produce the lag. Detail: [`../results/01-anti-collapse-2d.md`](../results/01-anti-collapse-2d.md).

**Three-dimensional supercritical anti-collapse with dimensional rescaling.** In 3D, the cubic NLS is L²-supercritical and collapse is generic. The same anti-collapse mechanism operates, but the total memory coupling required scales geometrically: $\Sigma\lambda/|\Lambda| \sim 0.5$ in 3D versus $\sim 0.05$ in 2D. The factor-of-10 rescaling is derivable from the dimensional concentration of the collapse focal region. Detail: [`../results/06-dimensional-rescaling.md`](../results/06-dimensional-rescaling.md).

**Spontaneous Bravais lattice selection.** The released crystalline state in 3D consistently selects body-centered cubic (BCC) symmetry across the swept memory coupling range, with score 0.44 and gap +0.13 over the next-best Bravais option (FCC). The selection emerges from a continuous Gaussian initial state; no symmetry is input. The detection algorithm is documented in [`../implementation/physics/observables.py`](../implementation/physics/observables.py). Detail: [`../results/05-bravais-selection.md`](../results/05-bravais-selection.md).

## Validation

The Strang split-step solver is implemented in CuPy on consumer GPU hardware. The validation suite ([`../tests/test_conservation.py`](../tests/test_conservation.py)) covers:

- Norm conservation in unitary regimes ($< 10^{-13}$ in fp64).
- Pure dissipative decay matching $e^{-2\gamma t}$ to six significant figures.
- FDT thermalization to $\langle |\Psi|^2 \rangle = 2T$ per cell within 0.5%.
- Rashba spinor unitarity drift $< 10^{-13}$.
- Memory auxiliary field stability over the integration window.

The validation is comparable to the standards of the stochastic-field-theory and BEC simulation literature.

## What may be unfamiliar

Three aspects of the work may be unfamiliar to readers from physics.

**The structural-realist methodology.** The work places the methodological position (structural realism, in the sense of Worrall 1989 and Ladyman & Ross 2007) at the same level as the equation derivation. The position is articulated in [`../methodology/`](../methodology/). The reason for elevating methodology is the structural tension between strict Popperian falsificationism and the content of P3 (coupling is the default; isolation is temporary). A theory whose third axiom denies isolation cannot consistently be evaluated by a methodology that presupposes isolation.

**Cross-domain interfaces as first-class content.** The work elevates cross-domain mappings to a first-order folder ([`../interfaces/`](../interfaces/)). The strongest of these is the exact mathematical equivalence between the auxiliary-field memory equation and the diagonal-state structured state space model used in machine learning (S4, Mamba, RWKV). Detail: [`../interfaces/06-state-space-models.md`](../interfaces/06-state-space-models.md). The weakest is the calibrated mapping to archaeoacoustic resonance data, with explicit caveats about the dimensional identification.

**The temporal–spatial asymmetry.** The memory kernel can be non-local in time (the standard form) or also non-local in space (a Gaussian or exponential spatial smoothing). The two non-localities act asymmetrically: temporal non-locality regularizes collapse; spatial non-locality destroys the regularization. This is documented numerically and has a geometric explanation. Detail: [`../results/07-temporal-spatial-asymmetry.md`](../results/07-temporal-spatial-asymmetry.md).

## A cross-substrate empirical instance

A recent observation extends the field-theoretic anti-collapse result into a categorically different substrate: the same anti-collapse mechanism that prevents singular concentration in 3D supercritical NLS field dynamics has been observed to prevent catastrophic optimization collapse in the training of a 70M-parameter neural network ([`../results/08-optimization-collapse-empirical.md`](../results/08-optimization-collapse-empirical.md)).

In a controlled side-by-side training run on enwik8, Memory-NLS (with the structural multi-timescale memory hierarchy) descended monotonically through 50,000 steps to a stable plateau. A matched-shape Transformer (without the structural mechanism) reached a lower minimum mid-training but then exhibited a catastrophic loss spike at step 28,000 (val perplexity jumping from 3.10 to 27.17), recovering only partially through the remaining steps.

The phenomenology is structurally identical to the field-theoretic case: the substrate without anti-collapse mechanism enters a degenerate concentrated state and either remains there or recovers incompletely; the substrate with the mechanism retains its extended, distributed configuration throughout. The cross-substrate observation is the kind of empirical instance the structural-realist methodology in [`../methodology/`](../methodology/) identifies as definitive evidence: same form, two physically and ontologically distinct substrates, same observable dynamics, no design coordination.

For the physicist this provides an additional empirical testbed for the anti-collapse mechanism that operates in a regime (gradient flow on a high-dimensional non-convex loss landscape) very different from the field-theoretic regime where the mechanism was originally derived.

## Recommended path

In order:

1. [`../equation/01-derivation.md`](../equation/01-derivation.md) — Derivation of the full equation.
2. [`../equation/02-markovian-embedding.md`](../equation/02-markovian-embedding.md) — Auxiliary-field reduction.
3. [`../results/01-anti-collapse-2d.md`](../results/01-anti-collapse-2d.md) and [`../results/04-anti-collapse-3d.md`](../results/04-anti-collapse-3d.md) — The headline numerical findings.
4. [`../results/06-dimensional-rescaling.md`](../results/06-dimensional-rescaling.md) — The structural scaling argument.
5. [`../results/05-bravais-selection.md`](../results/05-bravais-selection.md) — The spontaneous symmetry result.
6. [`../results/08-optimization-collapse-empirical.md`](../results/08-optimization-collapse-empirical.md) — The cross-substrate empirical instance in neural training dynamics.
7. [`../interfaces/01-other-nls-systems.md`](../interfaces/01-other-nls-systems.md) — The bare-NLS instances.
8. [`../interfaces/06-state-space-models.md`](../interfaces/06-state-space-models.md) — The state space model equivalence.
9. [`../interfaces/07-cosmological-expansion.md`](../interfaces/07-cosmological-expansion.md) — The cosmological correspondence (anti-collapse at cosmic scale).
10. [`../methodology/01-structural-realism.md`](../methodology/01-structural-realism.md) and [`../methodology/02-limits-of-falsification.md`](../methodology/02-limits-of-falsification.md) — Why this position.
11. [`../paper/manuscript.md`](../paper/manuscript.md) — The synthesized full paper.

To reproduce the numerical results, the scripts in [`../experiments/physics/`](../experiments/physics/) execute the relevant computations. Wall times on RTX 4060 are on the order of minutes per experiment. The neural-substrate empirical instance reproduces in [`../experiments/neural/scale_up_dynamics.py`](../experiments/neural/scale_up_dynamics.py) (~6.3 hours).
