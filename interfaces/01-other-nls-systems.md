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

## What this set of correspondences establishes

The cross-domain status of the bare cubic NLS, its appearance across optical, atomic, hydrodynamic, and plasma systems, is not a coincidence and not a metaphor. It is a structural fact about the leading-order behavior of weakly nonlinear, weakly dispersive wave systems. The equation derived in this work places the memory-augmented NLS in the same family. Each of the four substrates above (optical, atomic, hydrodynamic, plasma) admits the memory term as a natural extension corresponding to the coupling between the primary wave dynamics and a slower-relaxing environmental field (the medium's polarization for optical; the non-condensate cloud for BEC; the wind or bottom for water; the ions for plasma).

The structural fact, again on the structural-realist reading, is that all four substrates exhibit oscillation (P1), self-interaction with memory (P2), and environmental coupling (P3). They differ only in the physical interpretation of the field $\Psi$ and the values of the coupling constants. The mathematical form is the same.

## Common dismissals and why they do not apply

**"NLS is well known; this is not new."** The claim here is not novelty of NLS. The claim is that the equation derived from P1+P2+P3 reduces to NLS in the appropriate limit, that NLS in turn appears across the listed substrates, and that the appearance is structural rather than coincidental. The well-known status of NLS is the evidence supporting cross-domain coherence (criterion 4 in [`../methodology/04-the-six-criteria.md`](../methodology/04-the-six-criteria.md)), not the counterargument; NLS is one substrate-specific calibration of the structural form the equation derives.

**"Memory effects are domain-specific."** The point of the multi-exponential memory and its Markovian embedding (see [`../equation/02-markovian-embedding.md`](../equation/02-markovian-embedding.md)) is precisely that the structural form of the memory is invariant across substrates while the substrate-specific kernel parameters vary. The Raman scattering kernel for optics and the non-condensate-cloud kernel for BEC have different numerical parameters; they are the same mathematical object up to those parameters. The structural form is preserved across the calibration choices; that is what the cross-domain claim asserts.

## Locally testable predictions and observational signatures

> **Hedge cleanup (2026-05-16).** Each prediction's "What would constitute evidence inconsistent with this calibration" subsection previously used Popperian falsification framing ("would constitute local falsification") inserted in Phase 2 (commit 26e96ee) and propagated by Phase 3 to interfaces 10-17. The hedge contradicted the section's own opening sentence (the structural claim is evaluated by cross-domain coherence, not by single-experiment refutation). See [`../docs/llm-hedge-annotations.md`](../docs/llm-hedge-annotations.md) for the catalog of prior wordings and the structural reason for revision.

The structural claim of this interface (the memory-augmented NLS form is shared with optical, atomic, hydrodynamic, plasma instances of NLS) is evaluated by cross-domain coherence (methodology/04 criterion 4), not by single-experiment refutation. The following are *local* predictions that can be tested by coupled-regime numerical or empirical methods (per principles/03-coupling.md). Inconsistent evidence would shift evidentiary weight against this interface's specific calibration under criterion 4 (cross-domain coherence), without bearing on the global structural claim.

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
