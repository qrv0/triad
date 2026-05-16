# P1, Persistent extended entities oscillate

## Statement

Every spatially extended entity that persists in time exhibits intrinsic oscillation at one or more characteristic scales.

## Motivation

A literally static extended structure, free of internal oscillation, is unstable. Any perturbation either decays, in which case the structure was not persistent except as an external constraint imposed upon it, or grows, in which case the structure undergoes phase transition and is replaced by something else. Permanence of form requires permanent internal motion.

This is not a metaphysical claim; it is a structural observation. The atoms of any solid are in continuous thermal motion. The electrons in any atom occupy states that are stationary only in the time-averaged probability density and not in the underlying quantum amplitude. The galaxies of any cluster orbit each other under gravity; even a virialized cluster has nonzero internal velocity dispersion. The cells of any tissue exchange ions across membranes continuously; absolute electrochemical stasis is death. At every scale at which we observe persistent extended structure, we observe oscillation. We do not observe persistent extended structure without oscillation.

The principle generalizes this observation to a structural axiom: in any mathematical model that aspires to describe a class of persistent extended entities, the state object must support intrinsic oscillation, and the absence of oscillation must correspond to absence of the entity rather than to a special case of its presence.

## Mathematical consequence

The most economical state object that supports intrinsic oscillation without external forcing is a complex field $\Psi(t, \mathbf{x}) \in \mathbb{C}$ carrying a phase $\varphi = \arg\Psi$. The phase admits rotation at any frequency without modifying the modulus $|\Psi|$; the modulus admits modulation at any frequency without affecting the phase. The two degrees of freedom suffice to encode both amplitude oscillations and phase oscillations independently.

Real scalar fields fail this requirement. A real scalar field can oscillate only by driving its amplitude through zero, which couples amplitude and phase non-trivially and which requires external forcing to sustain. A complex field does not have this constraint: the phase rotates freely, and oscillation is intrinsic rather than externally maintained.

This is why the equation in [`../equation/`](../equation/) is built on a complex field rather than a real field. The choice is forced by P1.

## Optional internal structure

For systems with internal degrees of freedom, spin, polarization, two-band electronic structure, or any other binary internal label, the field generalizes from a scalar to a two-component spinor:

$$
\Psi(t, \mathbf{x}) = \begin{pmatrix} \psi_\uparrow(t, \mathbf{x}) \\ \psi_\downarrow(t, \mathbf{x}) \end{pmatrix},
$$

and the Hamiltonian acquires Pauli-matrix structure as detailed in [`../equation/01-derivation.md`](../equation/01-derivation.md). The choice between scalar and spinor representation depends on the specific physical system being modeled, but does not affect the structural content of P1 itself.

## What P1 does not assert

P1 does not assert that all motion is oscillatory. Translation, diffusion, ballistic propagation, and turbulence are all real and important kinds of motion. P1 asserts that the *intrinsic* dynamics of a persistent extended entity, abstracted from its translation through space and from its decay under dissipation, contains oscillation. Translation and dissipation are added as separate ingredients in the equation; they are not denied by P1, only distinguished from it.

P1 does not assert that the oscillation frequency is universal or fundamental. Different persistent entities oscillate at different frequencies. The principle is structural, not numerical.

## Cross-domain reading

Under P1, the relevant cross-domain question is not "do these systems share a specific oscillation frequency?" but "do these systems share the structural property that their persistence requires intrinsic oscillation?" The answer in the cases documented in [`../interfaces/`](../interfaces/) is yes: Bose–Einstein condensates oscillate at their condensate frequency, optical solitons oscillate at their carrier frequency modulated by their envelope, vibrated membranes oscillate at their normal modes, neural circuits oscillate at their gamma, beta, alpha, and theta bands, primordial plasma oscillated at its acoustic frequencies, and structured state space models maintain their hidden state through eigenvalue-controlled oscillation. The shared structural feature is oscillation as the substrate of persistence. The specific frequencies are calibrations of that substrate to particular physical instantiations.
