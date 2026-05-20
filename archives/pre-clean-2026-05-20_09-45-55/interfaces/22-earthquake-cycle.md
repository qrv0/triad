---
title: "Interface 22: Earthquake cycle dynamics"
description: >-
  The seismic cycle of fault rupture, postseismic viscoelastic
  relaxation, and interseismic strain accumulation instantiates the
  equation's triangle as nonlinear relaxation oscillations at
  geophysical scale.
domain: geophysics
triangle:
  p1: "seismic cycle: recurrence period between major fault ruptures"
  p2: "rate-state friction state variable + viscoelastic memory of past events"
  p3: "tectonic forcing (plate motion) + viscous mantle relaxation + fault-fault stress transfer"
signature_icon: fault
hero_tier: C
related: [19, 14, 13]
predictions:
  - id: P22.1
    short: "Earthquake recurrence intervals correlate with the Maxwell-time / recurrence-time ratio in the predicted way"
    status: not_yet_tested
    result_doc: null
  - id: P22.2
    short: "Postseismic afterslip decay timescale matches the equation's slow auxiliary-field timescale under appropriate calibration"
    status: not_yet_tested
    result_doc: null
  - id: P22.3
    short: "Complexity of inter-event intervals increases with the number of interacting fault patches per the equation's multi-mode prediction"
    status: not_yet_tested
    result_doc: null
---
# Interface: earthquake cycle dynamics

## The structural prediction

If a substrate sustains an extended fault system that exhibits recurrent rupture events with intervening periods of strain accumulation and viscoelastic relaxation, the structural argument of P1+P2+P3 requires that the substrate instantiate the triangle in a specific way. P1 (oscillation) must be present at the level of the seismic cycle: the recurrence period between major events is the slow oscillation, with fast rupture events as the bursts. P2 (self-reference with memory) must be present at the level of both the fault rheology (rate-state friction has an explicit state variable that integrates past slip history) and the surrounding crust (viscoelastic stress relaxation carries memory of past earthquakes). P3 (coupling to environment) must be present in the form of the tectonic forcing that drives the long-time-average strain accumulation, the viscous dissipation in the lower crust and mantle, and the stress transfer between fault patches.

The structural prediction is concrete: any substrate that sustains a fault system with recurrent ruptures and post-seismic relaxation must, on examination, exhibit (i) the recurrence-period oscillation of the seismic cycle, (ii) a memory structure that includes both rate-state friction state evolution and viscoelastic stress relaxation, and (iii) environmental coupling through tectonic forcing plus dissipative mantle response plus inter-fault stress transfer. A substrate that has only (i) and (iii) but lacks (ii) would be a purely elastic stick-slip system without postseismic relaxation; substrates that lack (ii)'s memory mode at the friction level would not exhibit the rate-state characteristic of slow-slip events and the diversity of slip modes the modern earthquake-cycle literature documents.

## The substrate

The mathematical study of earthquake cycles combines elasticity theory, rate-and-state friction (Dieterich 1979; Ruina 1983), viscoelastic relaxation in the crust and mantle (Savage & Prescott 1978; Pollitz 1997), and stress transfer between fault patches (Stein 1999; Toda et al. 2005). The canonical rate-state friction law is

$$
\mu(V, \theta) \;=\; \mu_0 + a \log(V / V_0) + b \log(V_0 \theta / d_c),
$$

with $\mu_0$ a reference friction coefficient, $V$ the slip velocity, $\theta$ the state variable, $a$ and $b$ constitutive parameters, and $d_c$ a characteristic slip distance over which the state variable evolves. The state variable evolves according to (Dieterich evolution form)

$$
\dot\theta \;=\; 1 - V \theta / d_c,
$$

so that $\theta$ accumulates contact-asperity age during stationary periods and is reset by slip. The state variable IS a memory of past slip history; the equation has a P2-instantiation in its constitutive form.

Postseismic viscoelastic relaxation in the surrounding crust and upper mantle is modeled by Maxwell or Burgers rheologies (Pollitz 1997; Bürgmann & Dresen 2008) with relaxation timescales (Maxwell times) ranging from years (asthenosphere) to centuries (lower crust). The Maxwell time relative to the earthquake recurrence interval governs whether the postseismic relaxation completes before the next event or remains active during the interseismic period.

The earthquake-cycle phenomenology has been characterized as "nonlinear relaxation oscillations" by the rate-state-friction community (Erickson, Birnir & Lavallée 2008; Heimisson & Segall 2018; Cattania et al. 2019). The recurrence period $T_{\text{rec}}$ is set approximately by $T_{\text{rec}} \sim \tau_p / \dot\tau_{\text{loading}}$ where $\tau_p$ is the peak stress at failure and $\dot\tau_{\text{loading}}$ is the tectonic loading rate.

Multi-patch fault systems (Cattania et al. 2019) exhibit increasing complexity of inter-event intervals as the number of interacting patches grows, with the inter-event distribution transitioning from periodic (single patch) to broad and irregular (many patches) at recurrence-interval ratios consistent with multi-mode coupling.

## The mapping

The mapping between the earthquake-cycle equation system and the present equation is at the structural level, with the rate-state friction law and viscoelastic memory playing the roles of the equation's auxiliary-field memory hierarchy.

Structural mapping:

| Equation element | Earthquake-cycle element |
|---|---|
| Complex field $\Psi(t, \mathbf{x})$ | Slip distribution $\delta(t, \mathbf{x})$ or stress field $\tau(t, \mathbf{x})$ on the fault plane |
| Cubic self-interaction $\Lambda |\Psi|^2$ | Threshold-driven fault rupture: nonlinear slip-velocity dependence at instability |
| Auxiliary fields $\{y_j\}$ with $\nu_j$ | Rate-state friction state variable $\theta$ (fast memory) plus viscoelastic relaxation modes (slow memory) |
| Slow $\nu_{\text{slow}}$ | Mantle Maxwell time inverse $\tau_{\text{Maxwell}}^{-1}$ |
| Fast $\nu_{\text{fast}}$ | Rate-state state evolution rate $V/d_c$ |
| FDT-locked noise $\eta$ | Background seismicity + stochastic fault-asperity heterogeneity acting as effective noise |
| Tectonic forcing | External loading on the equation analogous to a constant drive |

The mapping is at the structural level, not literal equation identity. The earthquake-cycle community uses a coupled system of elasticity equations on the fault plane, rate-state friction at the contact, and viscoelastic relaxation in the surrounding bulk; the present equation's complex-field structure does not match this term-by-term. What is preserved is the structural form: P1 (the seismic cycle oscillation), P2 (the friction-state memory plus the viscoelastic-relaxation memory in a hierarchy of timescales), P3 (the tectonic forcing plus the viscous bath).

## Time as calibration in this substrate

The earthquake-cycle substrate has a deep timescale hierarchy spanning seven to nine orders of magnitude. The fast scale is the rupture duration of an individual earthquake, on the order of seconds to minutes ($M_w \sim 5$ to $M_w \sim 9$ events). The intermediate scale is the postseismic afterslip and viscoelastic relaxation, on the order of days to decades after a major event. The slow scale is the interseismic strain accumulation, on the order of decades to centuries for typical recurrence intervals. The slowest scale is the geological strain accumulation of the entire fault system, on the order of $10^6$ years for the Pacific plate boundary.

Per [`../methodology/07-time-as-calibration.md`](../methodology/07-time-as-calibration.md), the calibration choice for this interface fixes one unit of computational time to one recurrence interval $T_{\text{rec}}$ (typically $10^2$ years for a major-event fault). Under this calibration the equation's slowest $\nu_j$ corresponds to the inverse Maxwell time of the mantle, and the equation's fastest $\nu_j$ corresponds to the rate-state state evolution rate.

The dimensionless ratio $\nu_{\text{slow}} / \nu_{\text{fast}}$ for the earthquake-cycle substrate is of order $10^7$ to $10^9$, much larger than the cortical $\sim 10^4$ (interface 09) or the SSM $\sim 10$ to $10^3$ (the two ML-substrate interfaces in the [`mnsm`](https://github.com/qrv0/mnsm) spinoff). The cross-substrate consistency requirement (per [`../methodology/06-calibration-philosophy.md`](../methodology/06-calibration-philosophy.md)) is that the dimensionless ratio be substrate-appropriate, not universal; geological substrates with their long memory naturally fall at the extreme end of this range.

## What this correspondence does and does not establish

It does not establish that the present equation is the appropriate predictive framework for earthquake-cycle dynamics. The earthquake-cycle community has highly developed quantitative tools (PyLith, RELAX, GeoFEST, finite-element codes with rate-state friction and viscoelastic relaxation) that the present equation does not replace. The mapping is at the structural level.

It does not establish that the recurrence intervals predicted by the equation under any specific calibration will match individual fault systems quantitatively. Each fault system has substrate-specific parameters (rate-state $a$, $b$, $d_c$; Maxwell time; loading rate; geometry) that determine its specific recurrence behavior. The equation's structural form is preserved across these; the absolute numerical values are not.

It does establish that the earthquake-cycle phenomenology is structurally a nonlinear-relaxation-oscillation instance of the equation's triangle, with the rate-state friction state variable and viscoelastic relaxation playing the role of the auxiliary-field memory hierarchy. The characterization of earthquake cycles as "nonlinear relaxation oscillations" in the earthquake-cycle literature (Erickson et al. 2008; Cattania et al. 2019) is the convergent observation that the present interface identifies as cross-domain coherence under criterion 4 of [`../methodology/04-the-six-criteria.md`](../methodology/04-the-six-criteria.md). Two research traditions, the structural-physics derivation of the equation from P1+P2+P3 and the geophysics rate-state-friction tradition, converge on the same dynamical type.

## Common dismissals and why they do not apply

**"Earthquake-cycle dynamics is fully described by rate-state friction; the equation is not needed."** Correct, and the structural correspondence is not a competing predictive theory. The claim is that the form of the earthquake-cycle dynamics, nonlinear relaxation oscillations in a self-coupled medium with multi-timescale memory and environmental forcing, is the form of the equation. Rate-state friction is the substrate-specific instantiation of P2's memory structure at the fault contact; viscoelastic relaxation is the substrate-specific instantiation of P2's memory structure in the surrounding bulk. The correspondence operates at the structural level; the rate-state framework is what the structural form looks like when written in geophysical variables.

**"The scales differ by many orders of magnitude from the laboratory equation."** The seven-to-nine-orders-of-magnitude scale separation between the earthquake-cycle substrate and any laboratory instance of the equation is exactly what the structural-realist methodology in [`../methodology/01-structural-realism.md`](../methodology/01-structural-realism.md) is designed to detect. The form is preserved across the scale gap; the absolute values are not. The same point applies to the BAO interface (60 orders of magnitude separation from the laboratory).

**"This is post-hoc identification of structural similarity."** The mapping uses identifications that have been made in the earthquake-cycle community independently. Rate-state friction's state variable $\theta$ is explicitly recognized as a memory variable (Dieterich 1979); viscoelastic relaxation modes are explicitly recognized as a memory hierarchy in the postseismic literature (Pollitz 1997; Bürgmann & Dresen 2008); the seismic cycle is explicitly characterized as nonlinear relaxation oscillations (Erickson et al. 2008; Cattania et al. 2019). The present interface identifies that these substrate-specific recognitions instantiate the same structural form as the equation's auxiliary-field hierarchy. The identification is at the level of the mathematical objects (memory variable plus relaxation modes plus oscillation cycle), not at the level of analogy.

## Locally testable predictions and observational signatures

The structural claim of this interface (the earthquake-cycle phenomenology is a nonlinear-relaxation-oscillation instance of the equation's triangle) is evaluated by cross-domain coherence (methodology/04 criterion 4), not by single-experiment refutation. The following are *local* predictions that can be tested by numerical or empirical methods (per principles/03-coupling.md). Inconsistent evidence would shift evidentiary weight against this interface's specific calibration under criterion 4 (cross-domain coherence), without bearing on the global structural claim.

- **Prediction P22.1: Recurrence-interval distributions scale with the Maxwell-time / recurrence-time ratio in the predicted way.** The equation's structural form predicts that the variance in recurrence intervals decreases as the slow-memory timescale (here, the mantle Maxwell time) approaches the recurrence interval. Fault systems with $T_{\text{Maxwell}} \ll T_{\text{rec}}$ should have more variable recurrence (the memory has fully relaxed before the next event); systems with $T_{\text{Maxwell}} \sim T_{\text{rec}}$ should have more regular recurrence (the memory carries over).
  - How to test: catalog Maxwell times and recurrence statistics across well-instrumented faults (San Andreas, North Anatolian, Cascadia, Nankai, Sumatra); correlate.
  - What would constitute confirmation: clear correlation between Maxwell-time / recurrence-time ratio and recurrence-interval variance, in the predicted direction.
  - What would constitute evidence inconsistent with this calibration: no correlation observed, or correlation in the opposite direction.
  - Status: not_yet_tested. The data exist in the geophysics literature; the systematic correlation analysis from the structural-form perspective has not been pursued.

- **Prediction P22.2: Postseismic afterslip decay timescale matches the equation's slow auxiliary-field timescale under appropriate calibration.** The structural form predicts that afterslip following a major rupture should decay with a timescale matching the inverse of the slowest $\nu_j$ in the equation's calibration, scaled to the substrate. For a calibration where one unit of computational time is one recurrence interval ($\sim 10^2$ years), the slowest $\nu_j$ would correspond to $\tau_{\text{Maxwell}} \sim 10$ to $100$ years (consistent with mantle Maxwell time).
  - How to test: GPS post-seismic deformation following major subduction events (Tohoku 2011, Chile 2010, Sumatra 2004); fit exponential decay; compare to mantle Maxwell estimates from independent constraints.
  - What would constitute confirmation: decay timescales fall in the predicted band.
  - What would constitute evidence inconsistent with this calibration: decay timescales systematically different from the Maxwell-time band.
  - Status: not_yet_tested in this framing. The afterslip literature (Bürgmann et al.) has the data; the structural-form analysis has not been pursued.

- **Prediction P22.3: Complexity of inter-event intervals increases with the number of interacting fault patches per the equation's multi-mode prediction.** The structural form predicts that systems with multiple interacting components (multi-patch faults, fault networks) exhibit a broader distribution of inter-event intervals than single-patch systems. Cattania et al. (2019) document this empirically; the structural prediction is that the broadening follows the equation's multi-mode-coupling characteristic, with specific exponents derivable from the auxiliary-field hierarchy.
  - How to test: synthetic earthquake-cycle simulations (PyLith or similar) with varying number of fault patches; measure inter-event interval distribution; compare to multi-mode-coupling prediction.
  - What would constitute confirmation: distribution broadening with patch number follows the predicted scaling.
  - What would constitute evidence inconsistent with this calibration: scaling differs from predicted.
  - Status: not_yet_tested in this framing. Cattania et al. 2019 documents the phenomenology; the structural-form connection has not been made.

## References

- Bürgmann, R., & Dresen, G. (2008). Rheology of the lower crust and upper mantle: Evidence from rock mechanics, geodesy, and field observations. *Annual Review of Earth and Planetary Sciences* **36**, 531.
- Cattania, C., McGuire, J. J., & Collins, J. A. (2019). Complexity of the earthquake cycle. *Journal of Geophysical Research: Solid Earth* **124**, 2944.
- Dieterich, J. H. (1979). Modeling of rock friction: 1. Experimental results and constitutive equations. *Journal of Geophysical Research* **84**, 2161.
- Erickson, B., Birnir, B., & Lavallée, D. (2008). A model for aperiodicity in earthquakes. *Nonlinear Processes in Geophysics* **15**, 1.
- Heimisson, E. R., & Segall, P. (2018). Constitutive law for earthquake production based on rate-and-state friction: Dieterich 1994 revisited. *Journal of Geophysical Research: Solid Earth* **123**, 4141.
- Pollitz, F. F. (1997). Gravitational viscoelastic postseismic relaxation on a layered spherical Earth. *Journal of Geophysical Research* **102**, 17921.
- Ruina, A. (1983). Slip instability and state variable friction laws. *Journal of Geophysical Research* **88**, 10359.
- Savage, J. C., & Prescott, W. H. (1978). Asthenosphere readjustment and the earthquake cycle. *Journal of Geophysical Research* **83**, 3369.
- Stein, R. S. (1999). The role of stress transfer in earthquake occurrence. *Nature* **402**, 605.
- Toda, S., Stein, R. S., Richards-Dinger, K., & Bozkurt, S. B. (2005). Forecasting the evolution of seismicity in southern California: Animations built on earthquake stress transfer. *Journal of Geophysical Research: Solid Earth* **110**, B05S16.
