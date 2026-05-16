# Open problem 08: Calibration philosophy

**Status:** Open. Treated case-by-case in interfaces 04, 05, 07; not yet formalized as a methodological framework.

## Precise statement

Develop a decision procedure for when dimensional calibration choices matter in cross-domain interfaces, what makes a calibration defensible vs not, and how calibrations across interfaces must be consistent with each other to support the global structural-realism claim.

The procedure should address: given a cross-domain mapping with the form "the equation's quantity $X$ (computational units) maps to substrate quantity $Y$ (physical units) under calibration $C$," how do we evaluate whether $C$ is principled or post-hoc; how do we check that calibrations across multiple interfaces are mutually consistent; what role calibration plays in evidentiary weight under the structural-realist criterion.

## What is known

- The methodology already distinguishes mathematical equivalence (no calibration: interfaces 01, 06 in part) from structural-but-calibrated correspondence (interfaces 04, 05, 07).
- [`../methodology/04-the-six-criteria.md`](../methodology/04-the-six-criteria.md) criterion 4 (cross-domain coherence) treats both as evidence, with the calibrated correspondences contributing less individual weight but more cumulatively.
- The most heavily caveated interface ([`../interfaces/05-archaeoacoustic-resonance.md`](../interfaces/05-archaeoacoustic-resonance.md)) has a "Careful framing" section explicitly handling calibration sensitivity.
- The gamma entrainment interface ([`../interfaces/04-gamma-entrainment.md`](../interfaces/04-gamma-entrainment.md)) uses the calibration "1 unit of computational time corresponds to 25 ms" to map the equation's broadband absorption to the neural gamma band.
- The archaeoacoustic interface uses the calibration "$L = 20$ m, $dt = 9$ ms" to map the two principal vibrational modes to 66 Hz and 111 Hz.
- The cosmological interface ([`../interfaces/07-cosmological-expansion.md`](../interfaces/07-cosmological-expansion.md)) operates at scales separated by approximately 60 orders of magnitude in length and 17 orders of magnitude in time from the laboratory equation; the calibration is not made explicit because the cross-substrate claim is at the level of dynamical shape rather than absolute values.

## What is missing

- A formal decision procedure: given a calibration $C$ for an interface, what tests determine whether $C$ is principled (motivated by substrate physics independent of the desired match) or post-hoc (chosen specifically to produce a desired numerical coincidence)?
- A consistency check across interfaces: the calibrations chosen for interfaces 04 and 05 differ; the gamma calibration places 1 computational time unit = 25 ms, the archaeoacoustic uses 9 ms. These are different choices; under what conditions are different calibrations across substrates legitimate vs evidence of cherry-picking?
- A framework for combining evidence from multiple calibrated correspondences: if interface 04 supports the structural claim under calibration $C_4$ and interface 05 supports it under calibration $C_5$, what does the combined weight look like?

## What would constitute progress

- Documentation of a formal decision procedure for evaluating calibrations, applicable to existing interfaces and to any future cross-domain mapping.
- Explicit cross-interface consistency check: the calibrations across all current interfaces enumerated, and the constraints they impose on each other examined.
- A treatment of the limit case: when does a sequence of calibration choices add up to "the structural claim is supported across all calibrations one can defensibly choose" vs "the claim only survives one specific calibration choice and is therefore fragile"?
- Promotion of the result to [`../methodology/`](../methodology/) as a new document (`methodology/06-calibration-philosophy.md`) replacing the case-by-case treatment in individual interfaces with a centralized methodological resource.

## Suggested approaches

- **Bayesian framing.** Treat each calibration as a hypothesis; compute the prior over plausible calibrations from substrate physics; the posterior weight of a cross-domain match is the prior weight of the calibration multiplied by the likelihood of the match given the calibration. Calibrations chosen post-hoc have low prior weight; calibrations forced by substrate physics have high prior weight.
- **Invariance argument.** The structural form is dimensionless; the calibration is the choice of units that compares the dimensionless structure to a dimensional substrate. Calibrations that change the structural form (rather than just the units) are illegitimate; calibrations that only change the units are legitimate.
- **Cross-substrate consistency theorem.** If two substrates A and B share the structural form, and substrate A is calibrated by $C_A$ and substrate B by $C_B$, then the ratio $C_A / C_B$ must equal the ratio of physical scales between A and B. Test whether the existing calibrations satisfy this.
- **Counterfactual robustness.** For each calibration, ask: what would the cross-domain match look like under alternative defensible calibrations? If the match survives all defensible alternatives, it is robust; if it requires the specific calibration chosen, it is fragile.

## Connections to existing repo content

- [`../methodology/04-the-six-criteria.md`](../methodology/04-the-six-criteria.md) criterion 4: this open problem refines the operational test for criterion 4 in the calibrated-correspondence cases.
- [`../interfaces/04-gamma-entrainment.md`](../interfaces/04-gamma-entrainment.md): section "The dimensional identification" is the case study for calibration; the philosophy formalizes what this section does informally.
- [`../interfaces/05-archaeoacoustic-resonance.md`](../interfaces/05-archaeoacoustic-resonance.md): the most heavily caveated interface; its "Careful framing" section is the most extensive informal calibration handling.
- [`../interfaces/07-cosmological-expansion.md`](../interfaces/07-cosmological-expansion.md): the calibration is implicit (60 orders of magnitude scale gap); the formalization makes the implicit explicit.
- [`02-phase-diagram.md`](02-phase-diagram.md): each substrate's calibration places it at a specific point in the equation's phase diagram; cross-interface calibration consistency translates to "the substrates do not contradict each other on which region of the phase diagram is operative."
