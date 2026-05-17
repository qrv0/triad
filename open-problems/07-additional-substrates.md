# Open problem 07: Additional cross-domain substrates

**Status:** Largely resolved. The five candidate substrates originally listed here (Kuramoto, immune, Friston FEP, active matter, SOC) have been developed into full interface documents ([`../interfaces/10-kuramoto-synchronization.md`](../interfaces/10-kuramoto-synchronization.md) through [`../interfaces/14-self-organized-criticality.md`](../interfaces/14-self-organized-criticality.md)). Three additional logic-predicted substrates (cardiac dynamics, gene regulation / circadian, ecosystem dynamics) were also developed ([`../interfaces/15-cardiac-dynamics.md`](../interfaces/15-cardiac-dynamics.md), [`../interfaces/16-gene-regulation-circadian.md`](../interfaces/16-gene-regulation-circadian.md), [`../interfaces/17-ecosystem-dynamics.md`](../interfaces/17-ecosystem-dynamics.md)). The cross-domain coherence ledger now stands at the documented interfaces. The remaining open status is for further candidates beyond the current scope (plate tectonics, glassy systems, granular matter, open quantum systems beyond NLS family, market dynamics, plant signaling).

## Precise statement

The cross-domain coherence criterion (methodology/04 criterion 4) is currently operative across the documented interfaces in [`../interfaces/`](../interfaces/). The original five candidates listed in this problem (Kuramoto, immune, Friston, active matter, SOC) plus three logic-predicted additions (cardiac, gene regulation / circadian, ecosystem) are all now developed as full interfaces (10 through 17). The remaining open status of this problem is for further candidates beyond the current scope, where the structural argument predicts additional substrate-instantiations but the documentation has not yet been written.

## What was known and is now resolved

The five original candidate substrates have been developed into full interfaces:

1. **Kuramoto synchronization.** Now [`../interfaces/10-kuramoto-synchronization.md`](../interfaces/10-kuramoto-synchronization.md). Mathematical equivalence in the phase-only sector with multi-exponential memory.

2. **Immune affinity maturation.** Now [`../interfaces/11-immune-affinity-maturation.md`](../interfaces/11-immune-affinity-maturation.md). Calibration-dependent structural correspondence with explicit multi-timescale memory hierarchy.

3. **Friston Free Energy Principle / active inference.** Now [`../interfaces/12-friston-free-energy.md`](../interfaces/12-friston-free-energy.md). Convergent-program correspondence at the level of hierarchical predictive coding's multi-timescale model matching the auxiliary-field hierarchy.

4. **Active matter.** Now [`../interfaces/13-active-matter.md`](../interfaces/13-active-matter.md). Calibration-dependent structural correspondence across active-matter substrates.

5. **Self-organized criticality.** Now [`../interfaces/14-self-organized-criticality.md`](../interfaces/14-self-organized-criticality.md). Mechanism-shape correspondence; the technical SOC-vs-MNSM mechanism distinction is documented.

Three additional logic-predicted candidates were also added:

6. **Cardiac dynamics.** Now [`../interfaces/15-cardiac-dynamics.md`](../interfaces/15-cardiac-dynamics.md). Calibration-dependent structural correspondence.

7. **Gene regulation and circadian.** Now [`../interfaces/16-gene-regulation-circadian.md`](../interfaces/16-gene-regulation-circadian.md). Calibration-dependent structural correspondence spanning nine orders of magnitude in timescale.

8. **Ecosystem dynamics.** Now [`../interfaces/17-ecosystem-dynamics.md`](../interfaces/17-ecosystem-dynamics.md). Mechanism-shape correspondence with multi-generation memory hierarchy.

## What remains open

Candidate substrates the structural argument predicts but the current set does not yet include:

- **Plate tectonics and earthquake-cycle dynamics**: stress accumulation (P2) plus release events (P3 drive-and-relax) plus seismic-wave propagation (P1).
- **Glassy systems and aging**: multi-timescale relaxation with explicit memory; mode-coupling theory framework.
- **Granular matter beyond SOC**: jamming transitions, force chains; substrate where SOC was originally studied but covering wider phenomenology.
- **Open quantum systems beyond NLS family**: Lindblad-type dynamics with non-Markovian memory; pertinent to quantum-information-with-memory.
- **Market dynamics in econophysics**: prices with memory (volatility clustering), interactions among agents (P3), intrinsic oscillation (business cycles).
- **Plant signaling and vascular dynamics**: phloem signaling, root-shoot coupling, circadian and seasonal rhythms in plants.

Each requires literature review and the standard logic-led interface template. The bar is the same as for the documented interfaces: peer-reviewed primary literature for the substrate, structural mapping in the inverted (logic-led) form, three-class evidentiary categorization in [`../interfaces/README.md`](../interfaces/README.md).

## What is missing (for the remaining open candidates)

- Full interface documents for the open candidates listed above, following the logic-led template (structural prediction first, substrate identification second, citations as credit, with time-as-calibration paragraph and locally testable predictions sections).
- Term-by-term mathematical mappings (where possible) and three-class evidentiary categorization.
- Wheel SVG updates if/when the open candidates are promoted; the current 17-node design pushes visual density toward its limit, and adding more nodes may require viewBox expansion or a split into core + extension visuals.

## What would constitute progress

- Five new interface files in [`../interfaces/`](../interfaces/), each substantive (40-180 lines depending on the depth of the mapping).
- Each file with peer-reviewed primary literature citations.
- Each file with explicit evidentiary status (mathematical equivalence, calibration-dependent structural correspondence, or mechanism-shape and convergent-program correspondence per the three-class division in [`../interfaces/README.md`](../interfaces/README.md)).
- Each file with "Common dismissals" and "Locally testable predictions" sections.
- Decision on the wheel: expand from the current 9-node layout to 14 (5 new substrates added on top of the Phase 6 expansion) or keep at 9 with new interfaces listed separately.

## Suggested approaches

- **One interface at a time.** Each interface is independent; the order can be chosen for maximum impact. Friston FEP is the most consequential (active research program; potentially mathematical-equivalence tier); Kuramoto is the cleanest (well-established mathematical literature); immune is the most biologically distinct (independent confirmation of the cross-domain claim in living tissue beyond gamma entrainment); active matter is the most contemporary (recent literature explosion); SOC is the most universality-claim.
- **Literature review per candidate.** Each candidate requires a focused literature review identifying the primary sources, the canonical formulation, the connections to the MNSM equation, and the dismissals likely from the substrate community.

## Connections to existing repo content

- [`../interfaces/README.md`](../interfaces/README.md): the existing interfaces set the template and the bar; the three-class evidentiary division catalogued there is where each new substrate must be situated.
- [`../methodology/04-the-six-criteria.md`](../methodology/04-the-six-criteria.md) criterion 4: each new interface increases cross-domain coherence quantitatively.
- [`../principles/README.md`](../principles/README.md) section "Why exactly three": the triangle topology argument generalizes to predict that any substrate sustaining the triangle is an instantiation; the additional substrates here are candidates the argument predicts should exist.
- [`02-phase-diagram.md`](02-phase-diagram.md): each new substrate's calibration places it at a specific region of the phase diagram.
- [`08-calibration-philosophy.md`](08-calibration-philosophy.md): the calibration choices for each new substrate must respect cross-substrate consistency.
