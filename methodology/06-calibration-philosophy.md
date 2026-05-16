# Calibration philosophy

Cross-domain interfaces in this work range from mathematical equivalence (no calibration required; same equation in two notations) to structural-but-calibrated correspondence (the form is the same; specific numerical values require a choice of dimensional units). This document develops a procedure for evaluating calibrations: when they are defensible, when they are post-hoc, how they must be consistent across interfaces, and how calibration sensitivity affects evidentiary weight under the structural-realist criterion.

## The two-level structure

The methodology in [`01-structural-realism.md`](01-structural-realism.md) and [`02-limits-of-falsification.md`](02-limits-of-falsification.md) commits to a two-level evaluation:

- **Global structural claim:** evaluated by the six criteria in [`04-the-six-criteria.md`](04-the-six-criteria.md). Not subject to single-experiment refutation; tested by cross-domain coherence across multiple substrates.
- **Local predictions:** specific numerical quantities (separation ratios, frequency overlaps, peak positions) testable by standard experimental methods in the substrate-specific way. Locally falsifiable in the standard sense.

Calibration sits between these two levels. A calibration is the choice of dimensional units that lets a specific numerical quantity in the equation be compared to a measurement in a specific substrate. Without calibration, the equation's $\omega \in [3, 30]$ broadband absorption regime is dimensionless; with calibration (1 unit of computational time = 25 ms), the regime maps onto 20-200 Hz, comparable to the neural gamma band.

The calibration is a methodological choice, not a discovery. It is also not arbitrary: defensible calibrations are constrained by the substrate physics, by self-consistency across multiple measurements in the same substrate, and by consistency with calibrations chosen for other interfaces.

## Decision procedure

Given a cross-domain mapping with the form "the equation's quantity $X$ (computational units) maps to substrate quantity $Y$ (physical units) under calibration $C$," the following procedure evaluates whether $C$ is principled.

**Step 1: Is the calibration motivated by substrate physics independent of the desired match?**

A calibration motivated by substrate physics is one that is fixed by a measurement or by a physical scale that exists in the substrate independent of the structural-realist mapping. The 9 ms unit time used in [`../interfaces/05-archaeoacoustic-resonance.md`](../interfaces/05-archaeoacoustic-resonance.md) is motivated by the dimensional analysis of resonant cavities of physical size $L = 20$ m (the typical dimension of the chambers in question); the speed of sound in stone fixes the unit time once $L$ is fixed. The calibration is not chosen to produce the 110 Hz match; it is forced by the chamber dimensions and the medium.

A calibration chosen to produce a desired match is post-hoc and has low evidentiary weight under structural realism.

**Step 2: Does the calibration produce internally consistent predictions within the substrate?**

A defensible calibration produces multiple predictions about the substrate, not just the one used to motivate the calibration. The 25 ms unit time in [`../interfaces/04-gamma-entrainment.md`](../interfaces/04-gamma-entrainment.md) predicts the broadband absorption regime spans 20-200 Hz; this includes the gamma band (where the GENUS literature operates) but also the beta and high-gamma bands. The calibration is testable by examining absorption signatures across the full predicted range, not only at 40 Hz.

A calibration that produces only the one match used to motivate it has weaker evidentiary weight than a calibration that survives multiple substrate-specific tests.

**Step 3: Is the calibration consistent with calibrations used in other interfaces?**

Cross-interface consistency is the constraint at the heart of cross-domain coherence (criterion 4). If interface A is calibrated with $C_A$ and interface B with $C_B$, the calibrations must be self-consistent in the sense that the physical scales of the two substrates, measured independently, must stand in the ratio $C_A / C_B$. A calibration that violates cross-interface consistency is evidence that one of the calibrations is post-hoc.

In the current set of interfaces, the calibrations are: gamma uses 25 ms unit time; archaeoacoustic uses 9 ms unit time. These are different by a factor of approximately 2.8. The substrates differ: neural-tissue dynamics versus chamber acoustics. The 2.8 factor must be checkable against the physical scales of the two substrates (neural firing timescale vs sound-wave timescale in stone chambers); if the ratio matches the physical-scale ratio, the calibrations are consistent.

This check has not been performed quantitatively in the current repo; it is documented as part of [`../open-problems/08-calibration-philosophy.md`](../open-problems/08-calibration-philosophy.md) for future work.

**Step 4: Does the structural form survive variation of the calibration within the defensible range?**

A robust cross-domain correspondence is one where the structural form (the existence of the broadband absorption regime, the existence of two principal vibrational modes in a specific ratio, the existence of anti-collapse separation) survives any defensible calibration within the substrate's natural range. The specific numerical match shifts with the calibration; the structural feature does not.

A correspondence that requires one specific calibration to survive is fragile. A correspondence that survives all defensible calibrations is robust.

## Worked examples

### Example 1: Gamma entrainment (interface 04)

The calibration is "1 unit of computational time corresponds to 25 ms." This is motivated by the natural timescale of neural circuits, where 25 ms is roughly the period of 40 Hz oscillations and the membrane time constant of cortical pyramidal neurons.

**Step 1 (motivated):** The 25 ms scale is fixed by neuronal biophysics, not by the desired match. Cortical neurons have membrane time constants in this range; gamma oscillations have periods near this; the choice is grounded in substrate measurement.

**Step 2 (multiple predictions):** The calibration predicts broadband absorption spans 20-200 Hz, which includes gamma (where the empirical match is documented) but also beta and high-gamma. Predictions about absorption signatures at non-gamma frequencies are testable but not yet tested; this is named in [`../open-problems/`](../open-problems/) under the "Locally testable predictions" framework.

**Step 3 (cross-interface consistency):** Differs from archaeoacoustic calibration by factor 2.8. The factor needs comparison to physical-scale ratios; not yet done.

**Step 4 (robustness):** The structural feature (broadband absorption over multiple decades) survives any calibration that places the equation's $\omega \in [3, 30]$ regime in the audible-to-low-MHz range. The specific overlap with the gamma band shifts with the calibration; the existence of a broadband regime overlapping with a biologically active frequency band is the structural feature.

Evidentiary weight: moderate. The calibration is principled, the structural feature is robust, the cross-interface consistency is not yet verified.

### Example 2: Archaeoacoustic resonance (interface 05)

The calibration is "$L = 20$ m, $dt = 9$ ms." This is motivated by the physical dimensions of megalithic stone chambers (Newgrange, Hypogeum, others have dimensions on this scale) and the speed of sound in air within stone enclosures.

**Step 1 (motivated):** The 20 m scale is the typical chamber dimension; the 9 ms unit time follows from the sound-speed-in-air divided by the chamber dimension. Both are substrate measurements, not match-driven.

**Step 2 (multiple predictions):** The calibration predicts two principal frequency modes in 0.6:1.0 ratio; this matches the 66 Hz and 111 Hz measurements at Newgrange and Hypogeum. Additional predictions about resonances at other ratios (higher harmonics, weaker secondary peaks) are testable but not yet exhaustively tested.

**Step 3 (cross-interface consistency):** Differs from gamma calibration by factor 2.8. Same status as for gamma: needs comparison against substrate physical-scale ratios.

**Step 4 (robustness):** The structural feature (two principal vibrational modes in a specific ratio) is dimension-independent: the ratio 0.6:1.0 is a property of the equation's spectrum, not of the calibration. The specific Hz values (66 and 111) require the calibration; the ratio does not.

Evidentiary weight: low-moderate. The calibration is principled but the cross-substrate convergence of 110 Hz (with EEG response, multiple chambers, the equation's second mode) is the load-bearing observation. The careful framing of the interface document already acknowledges this.

### Example 3: Cosmological expansion (interface 07)

The calibration is implicit and operates at scales separated by approximately 60 orders of magnitude in length and 17 orders of magnitude in time from the laboratory equation.

**Step 1 (motivated):** No specific calibration is committed to because the cross-substrate claim is at the level of dynamical shape rather than absolute values. The trajectory shape (singular initial state, lag, overshoot, release, structure formation, sustained expansion) is the same; the absolute timescales are vastly different.

**Step 2 (multiple predictions):** The unified trajectory reading predicts the BAO scale, the inflation duration, the reheating energy, the dark-energy density. None of these are calibrated quantitatively; the interface document is explicit that this is open work.

**Step 3 (cross-interface consistency):** Not applicable in the current form because no specific calibration is committed to.

**Step 4 (robustness):** The structural feature (the trajectory shape) is the load-bearing claim and is calibration-independent.

Evidentiary weight: structural identification only; quantitative cosmology would require committing to a calibration and is open work.

## Constraints from cross-substrate consistency

When multiple interfaces operate, the calibrations must be jointly defensible. The cross-substrate consistency constraint is operationally:

> For interfaces A and B with calibrations $C_A$ and $C_B$, if both substrates exhibit the same structural feature of the equation (e.g., the broadband absorption regime), then under $C_A$ and $C_B$ the absorption regimes must coincide with the empirically active frequency bands of substrates A and B respectively. The ratio $C_A / C_B$ must equal the ratio of physical scales between substrates A and B, measured independently.

For the existing interfaces, this constraint produces specific tests not yet performed; see [`../open-problems/08-calibration-philosophy.md`](../open-problems/08-calibration-philosophy.md).

A calibration that satisfies cross-substrate consistency is jointly defensible. A calibration that violates it is evidence either that the cross-substrate claim is wrong at that pair of substrates, or that one of the calibrations is post-hoc.

## What this does not commit to

This document does not commit to a single universal calibration of the equation. The structural-realist position is explicitly that the equation is substrate-independent; the calibrations are how the substrate-independent form is compared to substrate-dependent measurements. Different substrates legitimately have different calibrations.

This document does not commit to the principled-vs-post-hoc distinction being binary. Calibrations exist on a spectrum: some are tightly forced by substrate physics, some are loosely motivated, some are chosen specifically for the match. The procedure here is intended to characterize where on the spectrum a given calibration sits, not to produce a binary verdict.

This document does not relieve interfaces of the responsibility to acknowledge their calibration sensitivity explicitly. The current interfaces with calibration handling ([`../interfaces/04-gamma-entrainment.md`](../interfaces/04-gamma-entrainment.md), [`../interfaces/05-archaeoacoustic-resonance.md`](../interfaces/05-archaeoacoustic-resonance.md), [`../interfaces/07-cosmological-expansion.md`](../interfaces/07-cosmological-expansion.md)) do this in their own documents; this methodology document provides the centralized framework, not a substitute for the per-interface acknowledgement.

## References

- [`01-structural-realism.md`](01-structural-realism.md): the two-level structure (global structural claim vs local predictions) the calibration philosophy operates within.
- [`02-limits-of-falsification.md`](02-limits-of-falsification.md): local falsifiability of specific numerical predictions, including calibration-dependent ones.
- [`04-the-six-criteria.md`](04-the-six-criteria.md) criterion 4 (cross-domain coherence): the evaluation criterion whose operational test the calibration philosophy refines.
- [`../open-problems/08-calibration-philosophy.md`](../open-problems/08-calibration-philosophy.md): the open work this document partially addresses; the cross-substrate consistency check across all current interfaces is named there as work to do.
- [`../interfaces/04-gamma-entrainment.md`](../interfaces/04-gamma-entrainment.md), [`../interfaces/05-archaeoacoustic-resonance.md`](../interfaces/05-archaeoacoustic-resonance.md), [`../interfaces/07-cosmological-expansion.md`](../interfaces/07-cosmological-expansion.md): the worked examples.
