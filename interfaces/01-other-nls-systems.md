---
title: "Interface 01: Other instances of NLS dynamics"
description: >-
  Optical solitons, BECs, surface gravity waves, plasma Langmuir
  oscillations all instantiate the triadic form.
domain: physics
triangle:
  p1: "envelope oscillation of the underlying carrier wave"
  p2: "nonlinear self-interaction plus dispersive / memory kernel"
  p3: "loss + gain (Raman, thermal cloud, bottom friction, electron-ion collisions)"
signature_icon: wave
hero_tier: B
related: [2, 3, 7]
predictions:
  - id: P1.1
    short: "Memory-augmented soliton stability scales with Raman timescale ratio"
    status: not_yet_tested
    result_doc: null
  - id: P1.2
    short: "BEC anti-collapse threshold scales with non-condensate-cloud temperature"
    status: not_yet_tested
    result_doc: null
  - id: P1.3
    short: "Surface-wave Benjamin-Feir threshold shifts with bottom-friction memory"
    status: not_yet_tested
    result_doc: null
---
# Interface: other nonlinear Schrödinger systems

The cubic nonlinear Schrödinger equation, in its bare form (no memory, no dissipation, no noise), is the leading-order envelope equation for a wide class of weakly nonlinear, weakly dispersive wave systems. Its appearance across physical substrates that are otherwise unrelated is the historical paradigm case of cross-domain mathematical structure in physics. The equation derived in this work, the bare NLS extended with memory, dissipation, and FDT-locked noise, places this paradigm case in the company of the other cross-domain mappings documented in this folder.

## Nonlinear optical fibers

In optical fiber propagation, the slowly-varying envelope of a light pulse in a Kerr nonlinear medium satisfies the cubic NLS (Agrawal 2019):

$$
i \partial_z A + \frac{1}{2}\beta_2 \partial_T^2 A + \gamma |A|^2 A = 0,
$$

where $A(z, T)$ is the envelope, $z$ the propagation distance, $T$ the retarded time, $\beta_2$ the group-velocity dispersion, and $\gamma$ the Kerr nonlinearity. Soliton propagation, modulational instability, and optical wave collapse are all well-documented experimentally and match NLS predictions. Stimulated Raman scattering and other delayed-response effects introduce memory terms whose structure is closely analogous to the multi-exponential memory of the present equation; these are usually handled via auxiliary-field embeddings of the type derived in [`../equation/02-markovian-embedding.md`](../equation/02-markovian-embedding.md).

## Bose–Einstein condensates

In trapped-atom Bose–Einstein condensates, the macroscopic wavefunction of the condensed atoms satisfies the Gross–Pitaevskii equation (Pitaevskii & Stringari 2016):

$$
i\hbar \partial_t \Psi = \left[-\frac{\hbar^2}{2m}\nabla^2 + V_{\text{trap}} + g|\Psi|^2\right]\Psi,
$$

which is the form to which the present equation reduces when memory, dissipation, and noise are neutralized. Coupling to the non-condensate thermal cloud, the dissipative environment for the condensate, naturally introduces both linear dissipation (atom loss to the cloud) and stochastic forcing (atom gain from the cloud), with FDT-locked noise correlator (Stoof 1999). The structural form of the present equation, with all four ingredients active, is the form of stochastic Gross–Pitaevskii used in finite-temperature BEC theory.

## Deep-water surface gravity waves

In deep water, the slow modulation of the envelope of surface gravity waves satisfies the cubic NLS as well, with appropriate identification of dispersion and nonlinearity (Dysthe, Krogstad & Müller 2008). The two-dimensional supercritical regime, in the spatial sense, not the temporal, corresponds to focusing of surface waves into rogue-wave events. Memory effects in deep-water NLS arise from wind-wave coupling and bottom friction; their incorporation into the NLS framework is structurally identical to the memory potential of the present equation.

## Plasma Langmuir oscillations

In plasma physics, the slowly varying envelope of Langmuir oscillations satisfies a Zakharov-system variant of cubic NLS coupled to ion-acoustic waves. The coupling to ions introduces effective memory in the Langmuir dynamics, the ions respond on slower timescales than the electrons, and this memory has the multi-exponential structure that admits Markovian embedding. The resulting equation is structurally identical to the present equation in the regime where Zakharov reduces to NLS-with-memory.

## Time as calibration in this substrate

Each of the four NLS-class substrates has its own physical time. In nonlinear optics the slowly-varying envelope's "time" is the retarded time $T$ in a frame co-moving with the pulse, and the "evolution direction" is the propagation distance $z$ along the fiber; physical time enters via $z = vt$ where $v$ is the group velocity. In Bose-Einstein condensates the time is laboratory time $t$ measured by the experimental clock. In surface gravity waves the time is laboratory or oceanographic time. In plasma physics the time is laboratory time on the order of the plasma period $\omega_p^{-1}$ for the fast scale, and the ion-acoustic timescale for the slow scale of the Zakharov system.

Each substrate has three natural timescales. The fast scale is the carrier oscillation period (one optical cycle, one quantum-mechanical phase rotation, one wave period, one plasma period). The medium scale is the envelope evolution timescale set by the nonlinearity (soliton period in optics; nonlinear oscillation period in BEC; Benjamin-Feir instability time in water waves; Langmuir collapse time in plasma). The slow scale is the memory or relaxation timescale (Raman response time in optics; non-condensate cloud thermalization in BEC; bottom-friction relaxation in water; ion-acoustic period in plasma).

Per [`../methodology/07-time-as-calibration.md`](../methodology/07-time-as-calibration.md), the unit of time in the present equation is calibrated to one of these substrate timescales. The natural choice is to calibrate the equation's slowest $\nu_j$ to the substrate's slow scale (Raman, thermal cloud, friction, ion-acoustic), which fixes the dimensionless memory ratio. The carrier-oscillation scale becomes the equation's fast variable, the envelope-evolution scale becomes the equation's $|\Lambda|^{-1}$, and the memory-relaxation scale becomes $\nu_{\text{slow}}^{-1}$.

The cross-substrate ratio that the structural argument predicts to be invariant is $\nu_{\text{slow}} / |\Lambda|$: this dimensionless number sets the regime in which memory effects shift soliton stability, modulational-instability thresholds, and condensate anti-collapse. Substrate-specific physics determines absolute scales; the structural form preserves the dimensionless ratio. This is the standard pattern of [`../methodology/06-calibration-philosophy.md`](../methodology/06-calibration-philosophy.md).

## What this correspondence does and does not establish

It does not establish that the four substrates above are physically the same system. They are obviously distinct: optical photons in glass, ultracold atomic ensembles, deep-water waves, plasma electron oscillations. The claim is that they share a mathematical form at the envelope-equation level, with substrate-specific physics fixing the constants.

It does not establish that the present equation is the only valid framework for any of these substrates. Each substrate has its own well-developed literature with substrate-specific formulations (the Gross-Pitaevskii equation for BEC; the Zakharov system for plasma Langmuir; the cubic NLS for optics; the Dysthe equation for water waves). The structural claim is that the memory-augmented form derived in this work places these substrate-specific equations in a single family, related by calibration choices on the coupling constants and the memory kernel parameters.

It does establish that the bare cubic NLS, in its appearance across optical, atomic, hydrodynamic, and plasma systems, is a structural fact about the leading-order behavior of weakly nonlinear, weakly dispersive wave systems with environmental coupling. The equation derived in this work shows that the memory-augmented extension fits this same family: each of the four substrates admits the memory term as a natural extension corresponding to the coupling between the primary wave dynamics and a slower-relaxing environmental field (medium polarization for optics, non-condensate cloud for BEC, wind or bottom for water waves, ions for plasma). All four substrates exhibit oscillation (P1), self-interaction with memory (P2), and environmental coupling (P3); they differ only in physical interpretation and coupling constants, not in mathematical form.

## Common dismissals and why they do not apply

**"NLS is well known; this is not new."** The claim here is not novelty of NLS. The claim is that the equation derived from P1+P2+P3 reduces to NLS in the appropriate limit, that NLS in turn appears across the listed substrates, and that the appearance is structural rather than coincidental. The well-known status of NLS is the evidence supporting cross-domain coherence (criterion 4 in [`../methodology/04-the-six-criteria.md`](../methodology/04-the-six-criteria.md)), not the counterargument; NLS is one substrate-specific calibration of the structural form the equation derives.

**"Memory effects are domain-specific."** The point of the multi-exponential memory and its Markovian embedding (see [`../equation/02-markovian-embedding.md`](../equation/02-markovian-embedding.md)) is precisely that the structural form of the memory is invariant across substrates while the substrate-specific kernel parameters vary. The Raman scattering kernel for optics and the non-condensate-cloud kernel for BEC have different numerical parameters; they are the same mathematical object up to those parameters. The structural form is preserved across the calibration choices; that is what the cross-domain claim asserts.

## Locally testable predictions and observational signatures

The structural claim of this interface (the triadic form is shared with optical, atomic, hydrodynamic, plasma instances of NLS) is evaluated by cross-domain coherence (methodology/04 criterion 4), not by single-experiment refutation. The following are *local* predictions that can be tested by numerical or empirical methods (per principles/03-coupling.md). Inconsistent evidence would shift evidentiary weight against this interface's specific calibration under criterion 4 (cross-domain coherence), without bearing on the global structural claim.

- **Prediction P1.1: Memory-augmented soliton stability in optical fiber experiments.** In dispersion-managed optical fiber with controllable Raman gain timescale (which acts as the memory kernel), the equation predicts that the soliton instability threshold shifts as the Raman timescale traverses the slow-mode regime. Specifically, solitons with peak power above the standard NLS modulational-instability threshold should remain stable when the Raman timescale satisfies $\tau_R \sim |\Lambda|^{-1}$ where $|\Lambda|$ is the effective cubic coupling.
  - How to test: dispersion-managed fiber with adjustable Raman gain (achievable via fiber composition or co-propagating pump); measure soliton stability vs Raman timescale.
  - What would constitute confirmation: observed stability threshold for solitons follows the predicted scaling with $\tau_R$.
  - What would constitute evidence inconsistent with this calibration: stability threshold is insensitive to $\tau_R$ in the predicted regime, or follows a different scaling.
  - Status: untested in this framing. Adjacent observations exist in the dispersion-managed soliton literature (Agrawal 2019); the specific scaling has not been isolated as a prediction.

- **Prediction P1.2: BEC non-condensate-cloud coupling vs temperature.** In a Bose-Einstein condensate at finite temperature, the non-condensate cloud acts as the memory bath (Stoof 1999). The memory coupling $\Sigma\lambda$ should scale with temperature in a specific way derivable from the equilibrium between the condensate and the thermal cloud. The anti-collapse threshold (at which the condensate resists self-focusing under attractive interaction) should shift with temperature in the predicted way.
  - How to test: trapped BEC with attractive interaction tunable via Feshbach resonance; vary temperature; measure the critical attractive interaction strength at which the condensate becomes self-focusing.
  - What would constitute confirmation: critical interaction strength follows the predicted temperature dependence.
  - What would constitute evidence inconsistent with this calibration: critical interaction is temperature-independent or follows a different scaling.
  - Status: untested in this specific framing. Adjacent observations exist in attractive-BEC experiments (Bradley et al. 1995; Donley et al. 2001 "Bose-Nova"); the temperature dependence has not been isolated as a prediction of memory-mediated anti-collapse.

- **Prediction P1.3: Surface-gravity-wave envelope stability with bottom-friction memory.** In deep-water wave tanks, the modulational instability of envelope solitons is affected by bottom friction (which provides a memory effect at the air-water interface via wind-water coupling). The predicted shift in the Benjamin-Feir instability threshold with controlled bottom-friction strength should follow the structural form.
  - How to test: wave tank experiments with controlled bottom roughness; measure modulational-instability onset.
  - What would constitute confirmation: instability onset shifts with friction strength in the predicted direction and magnitude.
  - What would constitute evidence inconsistent with this calibration: instability is unaffected by bottom friction or shifts in the opposite direction.
  - Status: untested in this framing. Adjacent observations in the rogue-wave literature (Dysthe et al. 2008) suggest bottom-friction effects are non-trivial; the specific structural prediction has not been formulated.

## References

- Agrawal, G. P. (2019). *Nonlinear Fiber Optics* (6th ed.). Academic Press.
- Dysthe, K., Krogstad, H. E., & Müller, P. (2008). Oceanic rogue waves. *Annual Review of Fluid Mechanics* **40**, 287.
- Pitaevskii, L. P., & Stringari, S. (2016). *Bose–Einstein Condensation and Superfluidity*. Oxford University Press.
- Stoof, H. T. C. (1999). Coherent versus incoherent dynamics during Bose–Einstein condensation in atomic gases. *J. Low Temp. Phys.* **114**, 11.
- Sulem, C., & Sulem, P.-L. (1999). *The Nonlinear Schrödinger Equation: Self-Focusing and Wave Collapse*. Springer.
