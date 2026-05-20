---
title: "Interface 02: Baryon acoustic oscillations"
description: >-
  Pre-recombination plasma acoustic waves froze a 150 Mpc characteristic
  scale into matter distribution; the equation's memory-modulated wave
  dynamics predicts specific corrections.
domain: cosmology
triangle:
  p1: "photon-baryon plasma sound waves"
  p2: "baryon inertia plus radiation pressure memory"
  p3: "photon-baryon Thomson scattering coupling"
signature_icon: horizon
hero_tier: B
related: [7, 1, 3]
predictions:
  - id: P2.1
    short: "BAO peak position correction scales with memory-kernel timescale at recombination"
    status: not_yet_tested
    result_doc: null
  - id: P2.2
    short: "Secondary BAO peaks show memory-modulated harmonic structure"
    status: not_yet_tested
    result_doc: null
  - id: P2.3
    short: "Phase shift in BAO ringing detectable in DESI/LSST data"
    status: not_yet_tested
    result_doc: null
---
# Interface: baryon acoustic oscillations

The largest-scale documented instance of acoustic structuring of matter under self-interaction and environmental coupling occurred in the early universe. The mathematical structure that governed this period, wave propagation in a self-interacting medium coupled to a relaxing background, is the same structural form that the present equation describes at vastly smaller scales.

## The physical setup

Prior to the recombination epoch, approximately 380,000 years after the Big Bang, the universe was a hot, dense plasma of photons and baryons. The plasma was tightly coupled by Thomson scattering: photons could not propagate freely; baryons could not move without dragging photons. The outward radiation pressure from the photon component engaged in tension with the inward gravitational attraction from the baryon component, and this tension produced acoustic waves traveling at slightly more than half the speed of light through the plasma (Hu & Dodelson 2002; Eisenstein et al. 2005).

The plasma was not isolated. It was coupled to the surrounding gravitational field (which mediated the initial perturbations seeded by inflation) and to the dark matter field (which was already decoupled from photons but still gravitationally interacting with the baryons). The dynamics is therefore structurally a memory-augmented, coupled-medium wave equation. The "baryons + photons" subsystem oscillates (P1); the self-interaction is via gravity and pressure (P2 in its instantaneous form); and the system is coupled to dark matter, radiation, and the cosmological expansion (P3, with the bath being the rest of the cosmological energy density).

## The acoustic horizon and the freezing of structure

When the universe expanded and cooled enough for atoms to form (the recombination epoch), the photon–baryon coupling broke, photons free-streamed, and the acoustic pressure that had been driving oscillation vanished suddenly. The wavefronts of the largest standing acoustic modes were frozen in place: the matter overdensities were left at the positions reached at the moment of recombination, and these positions became the seeds of subsequent gravitational structure formation.

The largest such standing-wave scale, the distance an acoustic wave could travel between the Big Bang and recombination, approximately 150 megaparsecs in comoving distance, is the **baryon acoustic oscillation scale**. It is a literal frozen sound wave from the early universe, preserved as a characteristic length in the matter distribution. It has been directly measured in the two-point correlation function of galaxies (Eisenstein et al. 2005; Anderson et al. 2014) and in the temperature power spectrum of the cosmic microwave background (Hinshaw et al. 2013).

## The structural correspondence

The mathematical structure of the early-universe acoustic dynamics is:

$$
\text{(wave operator in a coupled medium)} + \text{(self-coupling via gravity)} + \text{(coupling to background)} = 0,
$$

with the additional feature that the coupling to background changes (recombination), at which point the wave dynamics freezes. This is, term by term, the structural content of the present equation, with the substitutions:

- The complex field $\Psi$ → the baryon density perturbation
- The wave operator $-\hbar^2/(2m) D^2$ → the acoustic dispersion of the photon–baryon fluid
- The cubic self-interaction $\Lambda |\Psi|^2$ → the gravitational self-coupling (in the linearized regime, this enters perturbatively)
- The memory potential $V_{\text{mem}}$ → the coupling to dark matter and to the long-wavelength tail of previous-epoch perturbations
- The dissipation $-i\Gamma$ → the photon diffusion (Silk damping) that suppresses small-scale acoustic modes
- The stochastic forcing $\eta$ → the primordial inflationary perturbations

The match is structural rather than literal: the early-universe acoustic dynamics is described by a different specific equation (the coupled Boltzmann–Einstein equations for photons, baryons, and dark matter in a Friedmann–Robertson–Walker background), not by the present equation. But the structural form, wave propagation in a self-interacting medium coupled to a background that itself relaxes, is the same.

## Time as calibration in this substrate

The cosmological substrate has three natural timescales separating the acoustic dynamics of the photon-baryon plasma. The fast scale is the plasma oscillation period for the largest standing mode, on the order of $\tau_{\text{osc}} \sim 1/(c_s k)$ where $c_s \approx c/\sqrt{3}$ is the sound speed in the photon-baryon fluid and $k$ is the wave number; for the BAO mode this is about $10^5$ years at recombination. The medium scale is the photon-baryon coupling timescale set by the Thomson scattering optical depth, $\tau_{\text{coupling}} \sim 1/(n_e \sigma_T c)$, which sets the memory kernel of the plasma dynamics. The slow scale is the Hubble time at recombination, $H^{-1}(z_{\text{rec}}) \approx 380{,}000$ years, which determines when the acoustic dynamics freezes as recombination breaks the photon-baryon coupling.

The three scales fall in a hierarchy: $\tau_{\text{osc}} < \tau_{\text{coupling}} < H^{-1}$ for the BAO mode at recombination, with the ratios determining (a) the number of acoustic oscillations the plasma completes before freezing, (b) the Silk-damping suppression of small-scale modes, and (c) the phase at which the BAO mode is frozen into the matter distribution.

Per [`../methodology/07-time-as-calibration.md`](../methodology/07-time-as-calibration.md), the unit of time in the present equation, when applied to the cosmological substrate, is calibrated to the slow scale $H^{-1}$ at recombination. The equation's slowest $\nu_j$ then corresponds to the photon-baryon decoupling rate $\tau_{\text{coupling}}^{-1}$, and the equation's $|\Lambda|$ corresponds to the gravitational self-coupling at the BAO scale. The structural form is preserved across this calibration; the absolute scales (separated by about 60 orders of magnitude in length and 17 orders of magnitude in time from any laboratory instance of the equation) are not.

The dimensionless ratio that the structural argument predicts to be invariant across substrates is $\nu_{\text{slow}} / |\Lambda|$. For the BAO substrate this becomes (decoupling rate) / (gravitational self-coupling at BAO scale), a ratio that the standard cosmological framework computes but does not motivate from a cross-substrate structural argument. The structural reading provides the motivation: this ratio is the same dimensionless quantity that, in other substrates (optical fibers, BEC, water waves, plasma Langmuir), sets the regime in which memory shifts the dynamical thresholds. Its specific cosmological value emerges from substrate-specific physics; its structural role is shared.

## What this correspondence does and does not establish

It does not establish that the present equation is the appropriate predictive framework for the cosmological substrate. The standard ΛCDM cosmological framework is the appropriate description for predictive cosmology: the Boltzmann-Einstein system for photons, baryons, neutrinos, and dark matter in an FRW background gives quantitative predictions, and the present equation does not replicate or replace that framework. The dimensional identification under which the equation would map onto the cosmological case quantitatively is highly nontrivial and is not attempted here.

It does not establish that the BAO scale and the laboratory parameters of the equation are numerically related. The BAO scale (~150 megaparsecs in comoving distance) and the laboratory scales for the equation's other instantiations live at vastly different absolute magnitudes. What the structural correspondence preserves is not the numerical values; it is the dimensionless structural form and the dimensionless ratio $\nu_{\text{slow}} / |\Lambda|$.

It does establish that the structural form of the present equation, oscillation in a self-interacting medium coupled to a relaxing background, recurs at the cosmological scale. The early-universe acoustic dynamics is, mathematically, the same kind of object as the laboratory instances of the Triad equation. The BAO peak in the matter correlation function is the macroscopic frozen acoustic structure of exactly the kind of dynamics the equation describes. This is one of the strongest cross-domain structural correspondences available, precisely because of the scale separation: a structural form that recurs across 60 orders of magnitude is evidence that the form is recovering an invariant feature of the underlying class of systems, not a substrate-specific accident.

## Common dismissals and why they do not apply

**"The standard ΛCDM already explains BAO."** Correct; the structural correspondence is not a competing predictive cosmology. The claim is that the form of the early-universe dynamics, oscillation in a self-interacting medium coupled to a relaxing background, is the form of the equation, and that this co-occurrence is structurally informative even where ΛCDM is the appropriate predictive framework for the cosmological substrate. The two frameworks operate at different levels: ΛCDM gives quantitative predictions in the cosmological substrate, the structural reading identifies the mechanism shape that the cosmological substrate shares with other substrates.

**"The scales are not comparable."** The 60-orders-of-magnitude scale gap between the laboratory equation and the cosmological BAO is the point, not the objection. The structural-realist methodology (see [`../methodology/01-structural-realism.md`](../methodology/01-structural-realism.md)) asserts that the form is what persists across substrates; the absolute scale is a calibration. The structural correspondence requires that the form be preserved across the scale gap; the absolute numerical values are not expected to match.

**"This is metaphor."** The term-by-term mapping in section `## The structural correspondence` is mathematical, not metaphorical: the wave operator of the photon-baryon plasma maps to the kinetic operator of the equation, the gravitational self-coupling maps to the nonlinearity, the dark-matter coupling maps to the memory, the Silk damping maps to the dissipation, and the inflationary perturbations map to the stochastic forcing. The mapping is at the level of the mathematical objects, not at the level of analogy.

## Locally testable predictions and observational signatures

The structural claim of this interface (the form of early-universe acoustic dynamics matches the equation form) is evaluated by cross-domain coherence (methodology/04 criterion 4), not by single-experiment refutation. The following are *local* predictions that can be tested by numerical or empirical methods (per principles/03-coupling.md). Inconsistent evidence would shift evidentiary weight against this interface's specific calibration under criterion 4 (cross-domain coherence), without bearing on the global structural claim.

- **Prediction P2.1: Memory-modulated correction to the BAO peak position.** The standard linear-perturbation analysis of the photon-baryon plasma predicts the BAO scale via the sound horizon integral. The memory-augmented form of the equation predicts a small correction to the peak position arising from the lag between the photon-pressure response and the baryon density. The correction is small (suppressed by the ratio of the relaxation timescale to the Hubble time at recombination) but may be detectable in next-generation surveys.
  - How to test: precision galaxy-survey measurements of the BAO peak (DESI, Euclid, Roman) compared to the linear-perturbation prediction. The discrepancy, if it matches the predicted memory correction, supports the interface.
  - What would constitute confirmation: measured peak position shifted by the predicted memory correction amount.
  - What would constitute evidence inconsistent with this calibration: measured peak position consistent with the linear-perturbation prediction to within the predicted memory-correction magnitude; the discrepancy is in the opposite direction; or the magnitude is wrong.
  - Status: untested. Requires development of the analytical correction plus the calibration philosophy from methodology/06.

- **Prediction P2.2: Higher-order BAO substructure.** The memory-augmented dynamics predicts secondary peaks in the matter correlation function beyond the principal 150 Mpc peak, arising from harmonics of the acoustic oscillation that the memory term modulates. Standard analysis predicts harmonic peaks; the memory-modulated form predicts a specific amplitude and phase relation between harmonics that differs from the standard prediction.
  - How to test: precision measurements of the matter correlation function at scales 30-150 Mpc; compare detected secondary peaks to predictions.
  - What would constitute confirmation: secondary peaks consistent with the memory-modulated harmonic structure.
  - What would constitute evidence inconsistent with this calibration: secondary peaks consistent with the standard harmonic structure but not the memory-modulated one.
  - Status: untested. Same calibration and analytical-theory prerequisites as P2.1.

- **Prediction P2.3: Temperature-shift cross-correlation in the CMB.** The memory term in the equation, applied to the photon-baryon plasma, predicts a specific phase relationship between density fluctuations and temperature fluctuations at the moment of decoupling. Standard analysis predicts the relationship; the memory-modulated form predicts a small phase shift.
  - How to test: cross-correlation of CMB temperature with galaxy survey density at the BAO scale.
  - What would constitute confirmation: phase shift measured at the predicted magnitude.
  - What would constitute evidence inconsistent with this calibration: no phase shift detected or opposite-sign shift detected.
  - Status: untested. Same prerequisites.

## References

- Anderson, L., Aubourg, É., Bailey, S., et al. (2014). The clustering of galaxies in the SDSS-III Baryon Oscillation Spectroscopic Survey. *Monthly Notices of the Royal Astronomical Society* **441**, 24.
- Eisenstein, D. J., Zehavi, I., Hogg, D. W., et al. (2005). Detection of the baryon acoustic peak in the large-scale correlation function of SDSS luminous red galaxies. *The Astrophysical Journal* **633**, 560.
- Hinshaw, G., Larson, D., Komatsu, E., et al. (2013). Nine-Year WMAP observations: cosmological parameter results. *The Astrophysical Journal Supplement Series* **208**, 19.
- Hu, W., & Dodelson, S. (2002). Cosmic microwave background anisotropies. *Annual Review of Astronomy and Astrophysics* **40**, 171.
