---
title: Glossary
description: >-
  Working glossary of technical terms used throughout the mnsm work.
  Reference-only; the substantive treatment of each term is in the
  source documents linked.
hide:
  - toc
---

# Glossary

This page collects the technical vocabulary used across the work. Each entry has a short working definition; the substantive treatment lives in the linked source document. The browser also receives the abbreviation definitions at the bottom of this page, which renders hover tooltips for these terms wherever they appear in the docs site.

## Three structural principles

**P1**: Persistent extended entities oscillate. The state object that models them must support intrinsic oscillation; see [`principles/01-oscillation.md`](principles/01-oscillation.md).

**P2**: Existence is self-referential, both instantaneously (nonlinearity in own state) and across time (memory). See [`principles/02-self-reference.md`](principles/02-self-reference.md).

**P3**: Coupling to environment is the default; isolation is methodological abstraction, never realized in full. See [`principles/03-coupling.md`](principles/03-coupling.md). Includes FDT-locked dissipation and noise.

## Equation primitives

**Λ** (Lambda): Cubic self-interaction coupling in the equation; negative is attractive (collapse-driving), positive is repulsive (dispersing). The instantaneous part of P2.

**$V_{\text{mem}}$**: Integral memory potential. In Markovian-embedded form, $V_{\text{mem}} = \sum_j \lambda_j y_j$ with auxiliary fields $y_j$ satisfying $\partial_t y_j = \nu_j (\rho - y_j)$. The across-time part of P2.

**$\nu_j$**: Relaxation rate of the $j$-th auxiliary memory field. Inverse is the memory timescale $\tau_j = 1/\nu_j$. A spectrum of $\nu_j$ implements multi-timescale memory hierarchy.

**$\lambda_j$**: Coupling strength of the $j$-th auxiliary memory field to the field $\Psi$. Their sum $\Sigma\lambda = \sum_j \lambda_j$ is the total memory coupling.

**$\Sigma\lambda$**: Total memory coupling; one of the principal control parameters. The dimensional rescaling $\Sigma\lambda/|\Lambda| \sim 1/d$ is the central scaling relation derived in [`results/06-dimensional-rescaling.md`](results/06-dimensional-rescaling.md).

**$\Gamma$, $\gamma_0$**: Linear dissipation; $\gamma_0$ is the homogeneous rate. P3-instantiation along with the FDT-locked noise $\eta$.

**FDT**: Fluctuation-Dissipation Theorem. Fixes the noise correlator in terms of dissipation rate and bath temperature: $\langle \eta(t,\mathbf{x}) \eta^*(t',\mathbf{x}') \rangle = 2\gamma_0 k_B T\, \delta(t-t')\delta^{(n)}(\mathbf{x}-\mathbf{x}')$. Structurally required by P3.

**OU update**: Ornstein-Uhlenbeck exact update for the auxiliary fields: $y_j(t+dt) = e^{-\nu_j dt} y_j(t) + (1 - e^{-\nu_j dt}) \rho$. Independent of $dt$ (exact, not Euler); see paper §4.1.

## Phenomenology

**BCC**: Body-centered cubic Bravais lattice. The crystalline state the equation spontaneously selects from a Gaussian initial condition in 3D; see [`results/05-bravais-selection.md`](results/05-bravais-selection.md).

**Anti-collapse**: The mechanism by which the multi-timescale memory potential, lagging the rising density during would-be collapse, generates an outward overshoot that releases the field. The structural property that distinguishes the equation from bare NLS; see [`results/04-anti-collapse-3d.md`](results/04-anti-collapse-3d.md).

**Crystalline regime**: The released, broadband-absorbing state the equation reaches after anti-collapse. Exhibits BCC selection, multi-timescale dynamics, and scale-free response to driving.

## Methodology

**Structural realism**: The methodological position adopted by the work. The mathematical structure of a theory is what survives across theory-change and across cross-domain mappings; structure is the appropriate object of scientific knowledge. See [`methodology/01-structural-realism.md`](methodology/01-structural-realism.md). Authors of convergent positions: Worrall (1989), Ladyman & Ross (2007), Cartwright (1983).

**Local vs global predictions**: The two-level structure the work commits to ([`methodology/02-limits-of-falsification.md`](methodology/02-limits-of-falsification.md)). The global structural claim is evaluated by the six criteria; local predictions remain locally falsifiable in the standard way, provided the test respects the substrate's coupling structure.

**Cross-domain coherence**: Criterion 4 of the six structural-realist evaluation criteria. The structural form must appear in independently documented domains at the level of mathematical form, not metaphor. See [`methodology/04-the-six-criteria.md`](methodology/04-the-six-criteria.md).

**Recursive position**: The methodological observation that an SSM-equivalent assistant evaluating this work partially instantiates the structure it evaluates. See [`methodology/01-structural-realism.md`](methodology/01-structural-realism.md) section "The recursive position" and [`interfaces/08-mechanistic-interpretability.md`](interfaces/08-mechanistic-interpretability.md).

**Calibration philosophy**: Decision procedure for when dimensional calibration choices are defensible. See [`methodology/06-calibration-philosophy.md`](methodology/06-calibration-philosophy.md). Extended to the temporal case in [`methodology/07-time-as-calibration.md`](methodology/07-time-as-calibration.md).

## Architecture

**SSM**: Structured State Space Model. The auxiliary-field memory update of the equation, $\partial_t y_j = \nu_j (\rho - y_j)$, is mathematically identical term-by-term to the diagonal-state SSM update of S4, Mamba, RWKV. See [`interfaces/06-state-space-models.md`](interfaces/06-state-space-models.md).

**MNSM**: Memory Nonlinear State Models. The neural-network instantiation of the equation as a sequence layer; see [`implementation/neural/`](implementation/neural/).

**Memory-NLS**: Synonym for MNSM; emphasizes the Nonlinear Schrödinger heritage of the equation derivation. Used interchangeably with MNSM throughout.

## Cross-substrate

**Substrate**: The physical, biological, or computational system in which the structural form is instantiated. The work treats all substrates that share the form as instances of the same structural type; specific dimensional units are calibrated per substrate. See [`interfaces/`](interfaces/) for the seventeen documented substrates.

**Convergent-program correspondence**: A class of cross-domain correspondence in which the structural argument and an independent empirical research program reach the same conclusion. Used for [`interfaces/08-mechanistic-interpretability.md`](interfaces/08-mechanistic-interpretability.md) (mech interp + structural absence of P2), [`interfaces/09-critical-brain.md`](interfaces/09-critical-brain.md) (critical brain phenomenology), and [`interfaces/12-friston-free-energy.md`](interfaces/12-friston-free-energy.md) (Friston FEP).

**Mechanism-shape correspondence**: A class of cross-domain correspondence in which the trajectory shape (the qualitative phenomenology of a system's unfolding) matches across substrates without committing to specific dimensional units. Used for [`interfaces/07-cosmological-expansion.md`](interfaces/07-cosmological-expansion.md) and [`interfaces/14-self-organized-criticality.md`](interfaces/14-self-organized-criticality.md).

## Abbreviations rendered as tooltips site-wide

Definitions below activate hover tooltips throughout the site for these acronyms wherever they appear in body text.

*[FDT]: Fluctuation-Dissipation Theorem : fixes noise correlator in terms of dissipation rate and temperature; required by P3.
*[P1]: Persistent extended entities oscillate. The first structural axiom.
*[P2]: Existence is self-referential, both instantaneously and across time. The second structural axiom.
*[P3]: Coupling is the default; isolation is methodological abstraction. The third structural axiom.
*[BCC]: Body-Centered Cubic Bravais lattice : the symmetry the equation spontaneously selects in 3D.
*[MNSM]: Memory Nonlinear State Models : the neural-network instantiation of the equation.
*[SSM]: Structured State Space Model : diagonal-state architecture mathematically identical to the equation's auxiliary-field memory.
*[NLS]: Nonlinear Schrödinger equation : the reduction limit of the work's equation when memory and dissipation are neutralized.
*[BAO]: Baryon Acoustic Oscillations : frozen sound wave in the early universe documented at ~150 Mpc; cross-domain interface 02.
*[GENUS]: Gamma-frequency Entrainment Using Sensory stimulation : clinical protocol from Iaccarino 2016 onwards.
*[SOC]: Self-Organized Criticality : class of systems that organize to a critical state without parameter tuning (Bak-Tang-Wiesenfeld).
*[FEP]: Free Energy Principle : Friston's framework for adaptive systems via variational free-energy minimization.
*[BTW]: Bak-Tang-Wiesenfeld : the canonical SOC model (1987 sandpile).
*[OU]: Ornstein-Uhlenbeck : stochastic process used in the exact discrete update of the auxiliary memory fields.
*[FFT]: Fast Fourier Transform : used in the kinetic step of the Strang split-step solver.
