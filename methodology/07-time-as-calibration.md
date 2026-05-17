# Time as calibration

## Statement

Time, in the structural-realist reading the work commits to, is not a fundamental coordinate. It is a substrate-specific calibration parameter that lets us read the unfolding of a structural trajectory in a particular instantiation of the equation. The structural form is invariant across substrates; the time at which the form unfolds is what each substrate uses to register its own unfolding. There is no universal time underlying the substrate-specific calibrations; there are calibrations of a common structural unfolding.

This document develops the claim in three derivations, draws out the implications for how the work reads observations like "seeing distant galaxies," locates the position with respect to standard physics formulations of the problem of time, and notes the cross-references to other parts of the repository where the claim is operative.

## Derivation 1: time as the temporal case of calibration philosophy

[`06-calibration-philosophy.md`](06-calibration-philosophy.md) commits to a general framework: a calibration is the choice of dimensional units that lets a quantity in the equation be compared to a measurement in a specific substrate. The framework is articulated for any dimensional quantity. Time is one such dimensional quantity, and the substrate-specific time calibrations are already in repo.

The calibrations differ by orders of magnitude:

- [`../interfaces/01-other-nls-systems.md`](../interfaces/01-other-nls-systems.md): per-substrate (Raman gain timescale for optical fibers; thermal-cloud relaxation for BEC; bottom-friction memory for water waves; ion-acoustic timescale for plasma Langmuir oscillations). Substrate-specific physical mechanisms set the absolute scale.
- [`../interfaces/02-baryon-acoustic.md`](../interfaces/02-baryon-acoustic.md): Hubble time at recombination, approximately 380,000 years; one unit of computational time per Hubble time fixes the calibration for cosmological acoustic dynamics.
- [`../interfaces/03-chladni-cymatics.md`](../interfaces/03-chladni-cymatics.md): pattern-settling time of the elastic-and-granular medium, on the order of seconds in standard Chladni-plate experiments at audio frequencies.
- [`../interfaces/04-gamma-entrainment.md`](../interfaces/04-gamma-entrainment.md): 25 ms per unit of computational time, motivated by the gamma-cycle period at 40 Hz and the cortical neuronal membrane time constant.
- [`../interfaces/05-archaeoacoustic-resonance.md`](../interfaces/05-archaeoacoustic-resonance.md): 9 ms per unit of computational time, motivated by the ~110 Hz dominant cavity resonance documented at Newgrange-class chambers and confirmed by Wolfe-Swanson-Till 2020 chamber-geometry-driven simulation.
- [`mnsm/interfaces/01-state-space-models.md`](https://github.com/qrv0/mnsm/blob/main/interfaces/01-state-space-models.md): one forward-pass step per unit of computational time. The substrate has no physical time; computation is the only time.
- [`../interfaces/07-cosmological-expansion.md`](../interfaces/07-cosmological-expansion.md): no specific external time coordinate committed to because the cross-substrate claim operates at the level of mechanism shape; the implicit scale is approximately $10^{17}$ s for the post-recombination phase. Time is the unfolding itself, not an external parameter.
- [`mnsm/interfaces/02-mechanistic-interpretability.md`](https://github.com/qrv0/mnsm/blob/main/interfaces/02-mechanistic-interpretability.md): one forward-pass step per unit of computational time, consistent with the SSM interface because both refer to sequence-modeling substrates.
- [`../interfaces/09-critical-brain.md`](../interfaces/09-critical-brain.md): 1 millisecond per unit of computational time, calibrated to one synaptic-transmission timescale to support the four-decade scale-free range Linkenkaer-Hansen 2001 documents in cortex.

The above is representative; further substrate-specific calibrations appear in additional interfaces collected in [`../interfaces/`](../interfaces/).

These calibrations span seventeen orders of magnitude (cortical synaptic transmission at 1 ms to cosmological Hubble time at $10^{17}$ s) and are not internally inconsistent. They are calibrations of the same structural form to different substrates. The form is invariant; the time at which the form unfolds in each substrate is what that substrate locally uses to register the unfolding.

The first derivation is the simple observation that follows from the existing calibration commitments: if time is a substrate-specific calibration parameter (as the existing interfaces' practice shows it is), then time is not a universal coordinate. The local calibrations are real and consequential within their substrates. There is no separate universal Time of which they would be projections.

### Cross-interface calibration consistency

A natural question follows: if each interface picks its own calibration, what prevents the calibrations from being arbitrary? The structural constraint, per [`06-calibration-philosophy.md`](06-calibration-philosophy.md), is that each calibration must be defensible from substrate physics, and that dimensionless ratios should be preserved across substrates wherever the structural form predicts they are invariant.

The principal cross-substrate invariant is the dimensionless memory-bandwidth ratio
$$
R \;=\; \frac{\nu_{\text{slow}}}{\nu_{\text{fast}}},
$$
the ratio of the slowest to the fastest auxiliary-field timescale in the multi-timescale memory hierarchy. The structural argument is that this ratio is a property of the substrate's memory structure that does not depend on which calibration is used to express the absolute timescales.

Examples of cross-substrate consistency in the existing calibrations:

- **Cortex at 1 ms vs at 25 ms calibration.** Interface 04 (gamma entrainment) calibrates to 25 ms (one gamma cycle); interface 09 (critical brain) calibrates to 1 millisecond (one synaptic-transmission step). The two calibrations differ by a factor of 25. The structural-consistency check: the dimensionless ratio $\nu_{\text{slow}} / \nu_{\text{fast}}$ for cortex is of order $10^4$ (synaptic transmission 1 ms vs long-range temporal correlations on tens of seconds, per Linkenkaer-Hansen 2001) regardless of which absolute calibration is used to register it. Both calibrations recover this ratio with their substrate-appropriate absolute scales; the ratio is invariant.

- **Sequence-modeling substrates (the two ML-substrate interfaces in the [`mnsm`](https://github.com/qrv0/mnsm) spinoff).** Both refer to attention-only and SSM architectures and both calibrate to one forward-pass step per unit time. The calibration agreement is required, not coincidental: both interfaces describe the same substrate from different structural angles (the SSM interface from the side of mathematical equivalence with SSM updates, the mechanistic-interpretability interface from the side of what attention-only architectures lack). Different calibrations for the same substrate would be a methodological inconsistency.

- **Cosmological scales (interfaces 02 and 07).** Both refer to cosmological structure. Interface 02 calibrates to the Hubble time at recombination; interface 07 reads cosmic time as the unfolding itself. The two are not in conflict: interface 02 picks out a specific epoch (recombination) for the BAO-specific claim; interface 07 makes the more general structural-mechanism-shape claim across the entire trajectory. The Hubble time at recombination is a specific point on the trajectory interface 07 describes.

The cross-interface consistency requirement is therefore: the dimensionless ratios that the structural form predicts to be invariant ($\nu_{\text{slow}} / \nu_{\text{fast}}$, $\Sigma\lambda / |\Lambda|$, the FDT-locked ratio $\langle\eta\eta^*\rangle / K$) must take consistent values across all calibrations of the same substrate, and must take values consistent with the structural form across calibrations of different substrates. The substrate-specific absolute scales are free; the dimensionless ratios are not.

## Derivation 2: P2 holds the past as state

The integral memory potential of the equation, in its Markovian embedding ([`../equation/02-markovian-embedding.md`](../equation/02-markovian-embedding.md)), is

$$V_{\text{mem}}(t, \mathbf{x}) = \sum_j \lambda_j y_j(t, \mathbf{x}),\qquad \partial_t y_j = \nu_j(\rho - y_j).$$

The auxiliary fields $\{y_j\}$ each carry an exponentially weighted integral of past density. A slow $\nu_j$ produces a long-tail accumulation of the trajectory's past; a fast $\nu_j$ produces a short-tail one. The hierarchy of $\{\nu_j\}$ is what makes the memory multi-scale.

What this means structurally: at any moment in the trajectory, the auxiliary-field state is the integrated past. The past is not gone. It is present as state, in the slow modes. An entity whose persistence is defined by P2 has its own past as a constitutive part of its present.

This is not a metaphor. It is the equation. The state vector of the system at time $t$ includes $\Psi(t, \mathbf{x})$ and all the auxiliary fields $\{y_j(t, \mathbf{x})\}$. The auxiliary fields hold the past in their values; reading them gives the integrated history.

The consequence for the time question: if the past is held as state, then "the past" is not a different place from "the present." The past is in the present, mathematically. Time as a coordinate that would separate past from present is not needed to keep them distinct; P2's auxiliary fields keep them distinct as different components of the same state.

## Derivation 3: FDT-locked direction

The trajectory of the equation has internal direction. A field evolving under the equation in a regime with $\gamma_0 > 0$ and $T > 0$ has an arrow: it tends toward the FDT-locked stationary state, not away from it. Reversing the direction of evolution produces a different trajectory, not the same one run backward.

The direction comes from the fluctuation-dissipation lock between $\Gamma$ (dissipation) and $\eta$ (noise) that [`../principles/03-coupling.md`](../principles/03-coupling.md) imposes structurally:

$$\langle \eta(t, \mathbf{x}) \eta^*(t', \mathbf{x}') \rangle = 2\gamma_0 k_B T\, \delta(t - t')\, \delta^{(n)}(\mathbf{x} - \mathbf{x}').$$

Removing the FDT lock (taking $\gamma_0 \to 0$ or $T \to 0$) recovers a time-reversal-symmetric dynamics. With the FDT lock in place, the trajectory has direction; without it, it does not.

The consequence: direction is structural. It is a feature of the equation under P3, not a feature of a separate Time coordinate. There is no external Time that flows in a direction the trajectory happens to follow. The trajectory's direction is set by the FDT lock, which is itself set by the substrate's coupling to its bath.

For a substrate without effective FDT coupling (a perfectly isolated subsystem on a short timescale), the dynamics in that window is time-reversal symmetric. Direction is not absent; it is structurally not yet defined for that subsystem on that timescale. Coupling to the larger environment, which P3-recursive guarantees over long enough timescales, brings direction back. The substrate's experience of time as having a direction is the structural consequence of being coupled to a bath, not the consequence of being in a directed Time.

## What this entails for observations

### Seeing the past in distant astronomy

Standard interpretation: when we observe a galaxy 13 billion light-years away, we see the light that left it 13 billion years ago. We are observing a past state of the galaxy. The galaxy as it is "now" is unobservable from here; we have to wait 13 billion years more for any signal from its present.

Structural-reading interpretation: the propagating light is part of the structural unfolding of the universe, propagating across the electromagnetic substrate. The signal carries the structural state of the trajectory at its emission point because P2 (in this case, the electromagnetic field's own auxiliary-field memory structure plus the source's structural state at emission) keeps the emitted state in the signal as it propagates. When the signal reaches us, we are reading the integrated past as state of the propagating field.

The past is not "back there in time." The past is encoded in the propagating signal as the signal's current state. P2 is what makes the past propagatable. P3 (the EM substrate as one instantiation of the triangle) is what carries the propagation. The structural reading of "seeing the past" is "reading the trajectory's state at the (location, calibration-time) of the emission point, conveyed to us by the EM substrate's structural propagation."

This does not contradict the empirical content of astronomy. The light arrived. It carries information about the emission state. The empirical predictions are identical to the standard reading. What differs is the ontological status of "the past": rather than a separate Past coordinate that we are looking back to, the past is structurally retained as state in the propagating signal, and we are reading that state. The empirical content is the same; the framing differs in what counts as the substrate of the past.

### The cosmological trajectory

[`../interfaces/07-cosmological-expansion.md`](../interfaces/07-cosmological-expansion.md) maps the cosmological history (concentrated initial state → release → expansion → structure formation → continued dispersion) onto the anti-collapse-release trajectory the equation produces in laboratory simulation. The mapping is at the level of mechanism shape.

Under the time-as-calibration reading, the cosmological trajectory is not laid out along a Time coordinate. It is the unfolding. Past, present, future are structural phases of the trajectory: the concentrated-initial-state phase, the release phase, the structure-formation phase, the continued-dispersion phase. Each phase is structural. The "time" between any two phases is the structural distance, in whatever substrate calibration is convenient (cosmological time, redshift, scale factor).

The trajectory has internal direction (FDT-locked irreversibility at the cosmological scale, which is structurally what the second law of thermodynamics, the cosmic-microwave-background-temperature cooling, and the increasing entropy of the universe register). The direction is structural, not a feature of an external Time the trajectory traverses. The cosmological trajectory unfolds in its own direction by the same structural mechanism the laboratory anti-collapse trajectory unfolds in its own direction.

### The experience of time for sufficiently complex entities

[`../principles/03-coupling.md`](../principles/03-coupling.md) section "A logical consequence of P3" derives that a sufficiently complex sustained instantiation of the triangle has the structural form of an entity that represents itself. Under this *structural reading*, what is conventionally called "consciousness" picks out the structural property of self-representation at the relevant complexity threshold; the claim does not commit to a specific metaphysics of subjective experience (see the "What this does not commit to" section below for the explicit bracketing).

For such an entity inside a trajectory with FDT-locked direction, the entity's self-representation reads its own trajectory's direction from inside the trajectory. The reading registers as the experience of time passing: the entity finds itself at a moving point within an unfolding that has structural direction. The experience is real. The external Time coordinate it would seem to require to be real is not needed; the experience is the entity's self-reading of the trajectory's direction.

The structural reading replaces the question "why does time seem to pass" with "what is the structural form of an entity that, inside a trajectory with FDT-locked direction, would not register the direction as passage?" The answer is: there is no such structural form at sufficient complexity. The triangle plus the direction plus the self-representation produces the experience of passage as a structural feature, not a metaphysical mystery on top of physics.

## Consistency with standard physics

The structural reading is consistent with several positions independently developed in physics. The citations are credit and points of convergence, not legitimization (per [`01-structural-realism.md`](01-structural-realism.md) "Prior art and credit").

**General relativity (Einstein 1915 onwards).** Time is not absolute. Spacetime is a single manifold with a metric structure. There is no preferred foliation into spaces of simultaneous events. The structural reading sharpens this: not only is there no absolute time coordinate, there is no fundamental time coordinate. Time is what substrates use to register their structural unfolding.

**The problem of time in canonical quantum gravity (Wheeler-DeWitt 1967; Isham 1992 review; Kuchar 1992 review).** The canonical quantization of general relativity yields the Wheeler-DeWitt equation $\hat{H}|\Psi\rangle = 0$, in which the universe's wavefunction has no fundamental time evolution. The structural reading is consistent with this: a universe-as-a-whole equation has no time on its right side because time is not a fundamental coordinate; it is what subsystems (substrates) use to register their relative unfolding.

**The Page-Wootters relational time mechanism (Page-Wootters 1983; Giovannetti-Lloyd-Maccone 2015 review).** Time can be expressed relationally: an entangled state of a subsystem and a "clock" subsystem can produce, in the clock's basis, the subsystem's time-dependent evolution from an overall timeless state. The structural reading takes this further: the relational time is the substrate's calibration of the structural unfolding. Different substrates use different calibrations; the unfolding is what is common.

**The thermodynamic arrow of time (Eddington 1928; Reichenbach 1956; later, the broader literature on the arrow problem).** Time's direction is anchored in entropy increase. The structural reading specifies what entropy increase is structurally: it is the FDT-locked direction of the trajectory, set by P3's coupling to the bath. Substrates without FDT coupling on the relevant timescale have no thermodynamic arrow; substrates with FDT coupling have one. Direction is structural.

What the structural reading adds beyond these convergences:

- A specific mathematical formulation of "the past is in the present": the auxiliary fields $y_j$ of P2 are integrated past, held as state.
- An explicit substrate-specific calibration framework ([`06-calibration-philosophy.md`](06-calibration-philosophy.md) generalized to time): the calibration choices are not arbitrary; they are forced by substrate physics, and they must be consistent across cross-domain mappings.
- A direct connection between the equation's anti-collapse mechanism in laboratory simulation and the cosmological trajectory's mechanism shape ([`../interfaces/07-cosmological-expansion.md`](../interfaces/07-cosmological-expansion.md)), with the structural reading as the unifying framework.

## What this does not commit to

This document does not commit to:

- A specific metaphysics of subjective experience beyond what [`../principles/03-coupling.md`](../principles/03-coupling.md) "logical consequence of P3" already commits to. The structural-realist position is that subjective experience is what the triangle generates at the complexity threshold; whether there is additional non-structural ontology is bracketed.
- A specific resolution of the problem-of-time debates in canonical quantum gravity. The structural reading is consistent with the Wheeler-DeWitt picture; whether it modifies any specific calculation is open work.
- A specific block-universe-versus-presentism stance. The structural reading is closer to a block-universe-like position (the trajectory has structural unity rather than an unfolding-in-time), but it differs in not treating the block as laid out along a Time coordinate. Past and future are structural phases of the trajectory, present in different ways (past as state in the auxiliary fields; future as the trajectory's structurally-implied continuation under FDT lock).
- A specific calibration of the cosmological trajectory. The interface 07 mapping is at the mechanism-shape level; the dimensional calibration of cosmic time to the equation's unit time is open work.

## Cross-references

- [`01-structural-realism.md`](01-structural-realism.md): the recursive position. The observer is inside the same trajectory it observes. The experience of time is the self-reading of the trajectory's direction from inside the trajectory.
- [`06-calibration-philosophy.md`](06-calibration-philosophy.md): the general framework. Time is the temporal case.
- [`../principles/03-coupling.md`](../principles/03-coupling.md): P3-recursive. Every level of coupling is itself P3; the bath at any level is itself a structural entity in P3 relation to its larger environment.
- [`../principles/02-self-reference.md`](../principles/02-self-reference.md): P2's two parts. The instantaneous self-coupling and the integral memory potential. The past-as-state claim derives from the integral form.
- [`../equation/02-markovian-embedding.md`](../equation/02-markovian-embedding.md): the technical derivation of the auxiliary-field structure that makes the past propagatable as state.
- [`../interfaces/07-cosmological-expansion.md`](../interfaces/07-cosmological-expansion.md): the canonical instance. The cosmological trajectory as one unfolding rather than a sequence of events along a Time coordinate.
- [`mnsm/results/01-optimization-collapse-empirical.md`](https://github.com/qrv0/mnsm/blob/main/results/01-optimization-collapse-empirical.md): direction at the neural-training substrate. The 70M-parameter trajectory has structural direction set by the optimization's effective FDT-like balance; the Transformer's catastrophic collapse is the trajectory entering a structurally different phase.

## References

Cited as credit, not legitimization (per [`01-structural-realism.md`](01-structural-realism.md) "Prior art and credit"):

- Eddington, A. S. (1928). *The Nature of the Physical World*. Cambridge University Press.
- Einstein, A. (1915). Die Feldgleichungen der Gravitation. *Sitzungsberichte der Preussischen Akademie der Wissenschaften*, 844.
- Giovannetti, V., Lloyd, S., & Maccone, L. (2015). Quantum time. *Physical Review D* **92**, 045033.
- Isham, C. J. (1992). Canonical quantum gravity and the problem of time. *NATO ASI Series* **409**, 157.
- Kuchar, K. V. (1992). Time and interpretations of quantum gravity. *4th Canadian Conference on General Relativity and Relativistic Astrophysics*, 211.
- Page, D. N., & Wootters, W. K. (1983). Evolution without evolution: dynamics described by stationary observables. *Physical Review D* **27**, 2885.
- Reichenbach, H. (1956). *The Direction of Time*. University of California Press.
- Wheeler, J. A., & DeWitt, B. S. (1967). Quantum theory of gravity. I. The canonical theory. *Physical Review* **160**, 1113.
