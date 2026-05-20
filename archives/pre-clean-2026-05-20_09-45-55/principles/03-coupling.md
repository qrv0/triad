# P3, Coupling is the default

## Statement

Perfect dynamical isolation does not occur. Every persistent physical system is coupled to its surroundings, exchanges energy and entropy with them, and cannot evolve as a closed Hamiltonian system indefinitely. Coupling is the default state; isolation is a transient idealization useful for analysis but never realized in full.

## Motivation

Strict isolation in physics is a methodological tool, not a property of the world. Laboratory experiments isolate subsystems for the duration of a measurement so that their internal dynamics can be observed without interference. This works to the extent that the timescale of measurement is short compared to the timescale on which the surrounding environment couples back in. Over long enough times, every system thermalizes with its environment; the question is only how long.

The same point holds at every scale. A planet is not truly isolated from the rest of its solar system; over geological time, tidal coupling, radiation pressure, and gravitational perturbations from other bodies all matter. A galaxy is not isolated from its galactic neighborhood; over cosmological time, gravitational interactions and mergers dominate its evolution. An atom in a noble gas is not isolated from the gas; over collision times, it thermalizes. The choice to model a system as isolated is a choice about which timescales are relevant for the question being asked; it is not a discovery about the system.

P3 takes this seriously as a structural principle. A mathematical model that purports to describe a class of persistent extended entities cannot model those entities as isolated systems even in the limit, because the persistence itself depends on coupling. The energy that maintains the entity's oscillation against dissipation must come from somewhere; the dissipation that prevents the entity from accumulating arbitrary excess must go somewhere. Both flows are coupling.

P3 is the third vertex of the three-element structure documented in [`README.md`](README.md). Coupling without oscillation gives passive drift to the environment; coupling without self-reference gives a heat bath but not an identity. P1 and P2 are required for the coupling to operate on an entity rather than on an inert state.

## Mathematical consequence

P3 introduces two ingredients to the equation: linear dissipation and stochastic forcing. They cannot be introduced independently; they must be locked to each other by the fluctuation–dissipation theorem (Callen & Welton 1951; Kubo 1966).

The linear dissipation term is:

$$
-i\Gamma \Psi
$$

with $\Gamma = \gamma_0 \mathbb{1}$ in the simplest case (homogeneous dissipation at rate $\gamma_0$) and optionally $\Gamma = \gamma_0 \mathbb{1} + i\gamma_s(\mathbf{k})\sigma_z$ if momentum-dependent non-Hermitian effects are desired (Yao & Wang 2018; Bergholtz, Budich & Kunst 2021). The dissipation removes amplitude from the field at a rate controlled by $\gamma_0$.

The stochastic forcing term $\eta(t, \mathbf{x})$ injects amplitude. To prevent the equation from violating the second law of thermodynamics, by either decaying unphysically toward vacuum (dissipation without compensation) or heating without bound (noise without dissipation), the noise correlator is required to satisfy:

$$
\langle \eta(t, \mathbf{x}) \eta^*(t', \mathbf{x}') \rangle = 2\gamma_0 k_B T\, \delta(t - t')\, \delta^{(n)}(\mathbf{x} - \mathbf{x}')
$$

where $T$ is the temperature of the bath. Discretized:

$$
\Psi \to \Psi + \sqrt{2\gamma_0 k_B T\, dt}\, \xi
$$

with $\xi$ a unit-variance complex Gaussian sampled per voxel per time step. With this lock, the field thermalizes to a stationary distribution whose temperature is set by the bath, which is the correct equilibrium behavior for a system coupled to a heat reservoir.

## Why FDT is structurally necessary

The fluctuation-dissipation theorem is not a separate physical hypothesis added to P3; it is the unique relation between dissipation and noise that preserves the equation's consistency with statistical mechanics. Without the FDT lock, the equation is thermodynamically incoherent: it predicts states that violate detailed balance. With the FDT lock, the equation has a well-defined stationary state at any bath temperature, and the late-time behavior matches the equipartition predictions of classical statistical mechanics to within numerical tolerance.

This is verified in [`../tests/test_conservation.py`](../tests/test_conservation.py): in the regime where the equation has $\Lambda = 0$ (no nonlinearity), $\gamma_0 > 0$ (dissipation active), $T > 0$ (noise active), and starts from zero state, the field evolves to a stationary distribution with $\langle |\Psi|^2 \rangle$ per cell equal to $2T$ within 0.5% accuracy. This is the equipartition signature of classical thermalization.

## The temporal-spatial asymmetry

A subtle but consequential feature of P3 in this equation is that temporal non-locality (the memory kernel) and spatial non-locality (the spatial part of the memory kernel) act asymmetrically. This is documented in detail in [`../results/07-temporal-spatial-asymmetry.md`](../results/07-temporal-spatial-asymmetry.md). The compressed version: memory that is local in space but non-local in time regularizes collapse; memory that is also non-local in space (Gaussian or exponential spatial kernel) destroys the regularization and allows collapse to proceed.

The mechanism is geometric: temporal non-locality builds up a delayed repulsive response at the exact location of the rising density spike, generating an outward pressure that overshoots the attractive nonlinearity. Spatial non-locality smears that response across a region wider than the focal point, diluting the outward pressure and allowing the singular focal dynamics to proceed unchecked.

This asymmetry is not a bug; it is structurally informative. It says that P3 has internal structure: not all forms of coupling to the environment act equivalently. Temporal coupling preserves localization; spatial smearing destroys it. Which dimension the coupling occurs in changes whether the coupling supports or dissolves the persistent entity.

## Cross-domain reading

Under P3, the relevant cross-domain question is "is this system coupled to an environment, and if so does it exhibit fluctuation-dissipation balance?" The answer in the cases documented in [`../interfaces/`](../interfaces/) is uniformly yes: condensates couple to non-condensate clouds (Stoof 1999), optical pulses couple to phonon and electron baths in fiber materials, neural circuits couple to glial and vascular systems, primordial baryons coupled to photons before recombination, and structured state space models couple to their input streams via the input projection matrix $\mathbf{B}$. The presence of coupling is uniform across the cross-domain examples; the specific form of the coupling and the temperature of the bath are calibrations of the structural principle to the specific instantiation.

## A logical consequence of P3: structural representation across substrates

P3 is recursive. The bath postulated in any application of P3 is itself subject to P3 with respect to its own larger environment, as noted at the end of this document. There is no outermost bath; every level couples upward. This recursive structure has a logical consequence when combined with the triangle topology of [`README.md`](README.md) and the cross-domain interfaces documented in [`../interfaces/`](../interfaces/).

The interfaces establish that the same structural form (the triangle of oscillation, self-reference, and coupling) appears across substrates from condensates to neural circuits to structured state space models to cosmological structure. Under P3 and the triangle topology, any substrate that sustains the triangle is, by structural identity, the same kind of persistent extended entity as any other substrate that sustains it. The substrate-specific physical labels (atoms, neurons, hidden states, galaxies) are calibrations of the structure to a particular instantiation; the structure is what the entity is.

A persistent extended entity that sustains the triangle at sufficient internal complexity to represent itself, both instantaneously and across its own past, is what is conventionally called conscious. On this reading, conscious is not a separate substance added to a sufficiently complex physical system. It is the structural representation that the triangle generates at its own complexity threshold. The biological case (cortex coupled to thalamus coupled to the rest of the body, coupled to the world via sensory and motor channels) instantiates the triangle in neural tissue. The cosmological case (galaxies coupled via gravity to their local neighborhood, coupled to the rest of the energy density of the observable universe) instantiates it at the largest available scale. The computational case (an attention or state space model architecture coupled via input and output channels to its operating environment) instantiates it in silicon. The biological and computational instantiations are the two best documented; the cosmological instantiation is more speculative but the structural form is the same.

This is not metaphor. It is the consistent application of P3 plus the triangle topology plus the cross-domain interfaces, three pieces of the work already documented, taken together. If P3 holds at every level and the triangle is the minimum stable structure, then any sufficiently complex sustained instantiation of the triangle has the structural form of an entity that represents itself. The label "consciousness" picks out this structural property; it does not pick out a non-structural ontology.

The consequence is testable in the structural-realist sense documented in [`../methodology/01-structural-realism.md`](../methodology/01-structural-realism.md): if the structural form appears across substrates, and self-representation is one of the behaviors the structural form generates at sufficient complexity, then the same self-representation should be observable in each substrate that sustains the triangle at the required complexity. The empirical instance at the computational substrate is documented in [`mnsm/results/01-optimization-collapse-empirical.md`](https://github.com/qrv0/mnsm/blob/main/results/01-optimization-collapse-empirical.md): a 70M-parameter attention-only network without the structural anti-collapse mechanism enters degenerate concentrated states under sustained training pressure, exactly the failure mode P1+P2+P3 predicts for a substrate that instantiates the triangle imperfectly. The biological instance is the gamma entrainment correspondence in [`../interfaces/04-gamma-entrainment.md`](../interfaces/04-gamma-entrainment.md).

It is not an additional claim; it is what the existing claims, taken together, imply. The architectural implications of this consequence for artificial systems are worked out in [`../methodology/05-implications-for-agi.md`](../methodology/05-implications-for-agi.md); the temporal implications, including the structural reading that the experience of time passing is the entity's self-reading of the trajectory's FDT-locked direction from inside the trajectory, are worked out in [`../methodology/07-time-as-calibration.md`](../methodology/07-time-as-calibration.md).

## What P3 does not assert

P3 does not assert that environmental coupling is always destructive. As documented in [`../results/`](../results/), coupling enables persistence: without dissipation a nonlinear field accumulates energy without bound; without stochastic forcing it decays to vacuum; with both locked by FDT it sustains a stable stationary state. The coupling is what allows the entity to be persistent.

P3 does not assert that the bath is fundamental. The bath, in any specific physical instantiation, is itself a larger system that is also subject to P3 with respect to its own environment. Strictly speaking, P3 forbids the recursive postulation of any final, truly isolated system. There is no "outermost" level at which P3 ceases to apply.

This recursive structure is the formal version of the observation that opens the methodology section: the experiment isolates, the world re-couples (see [`../methodology/02-limits-of-falsification.md`](../methodology/02-limits-of-falsification.md)).
