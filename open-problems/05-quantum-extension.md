# Open problem 05: Quantum field-theoretic extension

**Status:** Open. The equation is currently semi-classical (complex field plus classical stochastic forcing); the full quantum-field formulation is not developed.

## Precise statement

Formulate the equation as a quantum field theory: identify the action $S[\Psi, \Psi^*, y_j]$ from which the equation follows as the saddle-point (Euler-Lagrange) condition; derive the path integral $Z = \int \mathcal{D}\Psi \mathcal{D}\Psi^* \mathcal{D}y_j \, e^{iS/\hbar}$; compute one-loop corrections to the classical anti-collapse mechanism; identify which features of the classical analysis survive quantization and which acquire quantum corrections.

## What is known

- The equation has a semi-classical form: $\Psi$ is treated as a c-number field, the auxiliary fields $y_j$ are classical relaxation modes, the noise $\eta$ is classical stochastic forcing satisfying the FDT correlator.
- The reductions in [`../equation/05-reductions.md`](../equation/05-reductions.md) include the free Schrödinger equation (which has a well-known quantum-field formulation as a non-relativistic field theory) and the Gross-Pitaevskii equation (which is the mean-field limit of the Bose-Hubbard model in the dilute limit). The full equation includes additional structure (memory, FDT noise) whose quantum formulation has not been developed.
- The Mori-Zwanzig projection in [`../equation/02-markovian-embedding.md`](../equation/02-markovian-embedding.md) is classical; a quantum version of the projection-operator method exists (Nakajima-Zwanzig equation) and would provide the natural starting point.
- Non-equilibrium quantum field theory (Schwinger-Keldysh closed-time-path formalism) is the standard framework for stochastic quantum systems coupled to baths; this would be the natural setting for the full quantum extension.

## What is missing

- The action $S[\Psi, \Psi^*, y_j]$ from which the equation follows is not written down.
- The path integral has not been formulated.
- One-loop corrections to the classical anti-collapse mechanism (does quantum tunneling allow collapse where the classical analysis says it does not?) have not been computed.
- The connection to the Schwinger-Keldysh formalism has not been worked out.

## What would constitute progress

- Identification of the action whose variation gives the equation. (This is likely a Martin-Siggia-Rose-Janssen-De Dominicis action incorporating the noise, with auxiliary "response" fields.)
- Path-integral formulation of the partition function (or generating functional) in the Schwinger-Keldysh closed-time-path framework.
- Computation of the one-loop correction to the anti-collapse separation ratio; comparison to the classical numerical result.
- Identification of quantum-only phenomena: do the auxiliary fields $y_j$ acquire quantum fluctuations of their own that modify the classical relaxation dynamics?
- Connection to existing quantum-bath formalisms (Caldeira-Leggett 1981, 1983) which provide the quantum extension of classical Brownian motion with arbitrary memory kernels.

## Suggested approaches

- **Martin-Siggia-Rose-Janssen-De Dominicis (MSRJD) action.** Start from the classical equation; introduce response fields $\tilde{\Psi}$, $\tilde{y}_j$; write the action that produces the equation as a saddle point and the noise correlator from a Gaussian integration over $\eta$. Then quantize by replacing classical noise integrals with quantum path integrals.
- **Caldeira-Leggett extension.** Treat the bath (the source of the FDT-locked noise and dissipation) as an explicit collection of quantum oscillators; integrate them out to obtain an effective action for $\Psi$ alone with memory and noise. The memory kernel and noise correlator should match the classical FDT-locked pair.
- **Schwinger-Keldysh contour.** Formulate the equation on the closed-time-path contour; the action lives on the forward and backward branches; physical (Keldysh) and quantum (advanced/retarded) components separate.
- **Path integral for OU process.** The auxiliary fields $y_j$ satisfy an Ornstein-Uhlenbeck-like equation; the path integral for OU is well-known and provides the starting point for incorporating $y_j$ into the full path integral.

## Connections to existing repo content

- [`../equation/02-markovian-embedding.md`](../equation/02-markovian-embedding.md): the classical Markovian embedding; the quantum version uses the Nakajima-Zwanzig equation.
- [`../principles/03-coupling.md`](../principles/03-coupling.md): the FDT lock; the quantum FDT (Callen-Welton 1951) relates the quantum response and correlation functions.
- [`04-continuum-rg.md`](04-continuum-rg.md): the RG analysis would be done in the path-integral framework; the quantum extension is a prerequisite for proper field-theoretic RG.
- [`../equation/05-reductions.md`](../equation/05-reductions.md): the Lindblad limit is already a quantum master equation; the full quantum extension generalizes from Lindblad (Markovian) to non-Markovian.
- [`../methodology/04-the-six-criteria.md`](../methodology/04-the-six-criteria.md) criterion 6: bringing the equation into contact with quantum field theory as such extends comprehensiveness.
