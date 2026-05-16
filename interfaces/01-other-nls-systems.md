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

## References

- Agrawal, G. P. (2019). *Nonlinear Fiber Optics* (6th ed.). Academic Press.
- Dysthe, K., Krogstad, H. E., & Müller, P. (2008). Oceanic rogue waves. *Annual Review of Fluid Mechanics* **40**, 287.
- Pitaevskii, L. P., & Stringari, S. (2016). *Bose–Einstein Condensation and Superfluidity*. Oxford University Press.
- Stoof, H. T. C. (1999). Coherent versus incoherent dynamics during Bose–Einstein condensation in atomic gases. *J. Low Temp. Phys.* **114**, 11.
- Sulem, C., & Sulem, P.-L. (1999). *The Nonlinear Schrödinger Equation: Self-Focusing and Wave Collapse*. Springer.
