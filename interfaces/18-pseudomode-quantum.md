---
title: "Interface 18: Pseudomode embedding of non-Markovian open quantum systems"
description: >-
  Non-Markovian quantum systems with rational spectral density admit an
  exact Lindblad master equation on an enlarged Hilbert space; the
  auxiliary discrete pseudomodes are the memory subsystem of the
  equation in quantum form.
domain: physics
triangle:
  p1: "primary quantum system wave function or density operator"
  p2: "auxiliary discrete pseudomodes integrating bath spectral history"
  p3: "Markovian dissipators on pseudomodes locked to bath temperature via FDT"
signature_icon: pseudomode
hero_tier: C
related: [6, 1, 12]
predictions:
  - id: P18.1
    short: "Pseudomode embedding for Lorentzian spectral density reproduces full non-Markovian system observable trajectories to within numerical precision"
    status: tested_consistent
    result_doc: results/19-pseudomode-auxiliary-equivalence.md
  - id: P18.2
    short: "Number of auxiliary pseudomodes required scales with rank of rational fit to bath spectral density"
    status: not_yet_tested
    result_doc: null
  - id: P18.3
    short: "FDT-locked Markovian dissipation on pseudomodes recovers Caldeira-Leggett thermalization at the specified bath temperature"
    status: not_yet_tested
    result_doc: null
---
# Interface: pseudomode embedding of non-Markovian open quantum systems

## The structural prediction

If a substrate sustains a quantum system strongly coupled to a structured environment whose spectral density is rational (a finite sum of Lorentzians, the generic case for any bath admitting a finite-state-machine description), the structural argument of P1+P2+P3 requires the substrate to instantiate the triangle in a specific quantum form. P1 (oscillation) must be present at the level of the primary system: its state evolves under a unitary or near-unitary generator, with intrinsic oscillation set by the system Hamiltonian. P2 (self-reference with memory) must be present as the structured bath's contribution to the system's reduced dynamics: the bath does not return to equilibrium instantaneously, so the system's current state depends on a non-local-in-time integral over its own past coupling to the bath. P3 (coupling to environment) must be present in two forms: the original system-bath coupling, and (after embedding) the residual Markovian dissipation on the auxiliary pseudomodes that captures the structured-bath's own coupling to a wider environment.

The structural prediction is concrete: any quantum substrate that sustains coherent non-Markovian dynamics under a structured bath must, on examination, admit (i) a primary state object with intrinsic Hamiltonian dynamics, (ii) a finite set of auxiliary modes integrating the bath's spectral history, and (iii) Markovian dissipators on the auxiliary modes whose rates are determined by the bath spectral density and whose noise correlators (in thermal cases) satisfy a quantum FDT-like balance with the bath temperature. A substrate that has system-bath coupling but lacks the auxiliary-mode structure is restricted to the Born-Markov limit, which fails to capture coherent revival, recoherence, photonic-bandgap stabilization, and other characteristic non-Markovian phenomena.

## The substrate

The pseudomode framework for non-Markovian open quantum systems is one of the most rigorously developed areas of open-quantum-system theory. The base statement is that the reduced dynamics of a primary quantum system coupled to a structured bath can be reproduced exactly by an enlarged Lindblad master equation on a Hilbert space comprising the primary system plus a finite number of auxiliary discrete bosonic modes (the pseudomodes), each in turn coupled to a Markovian (memoryless) sub-bath. The framework was developed by Garraway (1997) for single Lorentzian bath spectra, extended by Tamascelli, Smirne, Lim, Huelga and Plenio (2018) to a non-perturbative treatment with general rational spectra, and generalized by Pleasance, Garraway and Petruccione (2020) to a unifying theory of pseudomodes covering thermal and non-thermal baths.

The defining mathematical statement is the following. For an original system-bath Hamiltonian $H = H_S + H_B + H_{SB}$ with bath spectral density $J(\omega) = \sum_j J_j(\omega)$ a sum of Lorentzians, there exists an exact equivalent dynamics on $\mathcal{H}_S \otimes \mathcal{H}_{\text{aux}}$ governed by a Lindblad master equation of the form

$$\partial_t \rho_{S, \text{aux}} = -i[H_{S, \text{aux}}, \rho_{S, \text{aux}}] + \sum_j \kappa_j \mathcal{D}[a_j] \rho_{S, \text{aux}},$$

where $\mathcal{H}_{\text{aux}}$ is the Hilbert space of $N$ auxiliary pseudomodes $a_j$, $H_{S, \text{aux}}$ extends $H_S$ with system-pseudomode coupling terms, and $\mathcal{D}[a_j]\rho = a_j \rho a_j^\dagger - \tfrac{1}{2}\{a_j^\dagger a_j, \rho\}$ are standard Lindblad dissipators with rates $\kappa_j$ derived from the Lorentzian widths in $J(\omega)$. The reduced dynamics on the primary system is recovered by tracing out the pseudomodes. The equivalence is exact, not perturbative.

The framework has been applied across substrate-specific instantiations: single-qubit decoherence in photonic-bandgap reservoirs, vibrational-mode coupling in molecular electron transfer, atom-cavity dynamics in lossy resonators, and the ultra-strongly coupled spin-boson model where the standard Born-Markov treatment fails categorically.

## The mapping

Structural mapping between the present equation and the pseudomode quantum substrate, at the level of the memory subsystem:

| Equation element | Pseudomode quantum element |
|---|---|
| Complex field $\Psi(t, \mathbf{x})$ | Primary quantum system state $|\psi_S\rangle$ or density operator $\rho_S$ |
| Cubic self-interaction $\Lambda |\Psi|^2$ | System self-Hamiltonian $H_S$ acting on $\rho_S$ (typically nonlinear in atomic operators, linear in $\rho_S$) |
| Integral memory potential $V_{\text{mem}}$ | System-pseudomode coupling $\sum_j g_j(a_j^\dagger O + a_j O^\dagger)$ feeding back from pseudomodes to system |
| Auxiliary fields $\{y_j\}$ | Pseudomode operators $\{a_j\}$ or their expectation values $\langle a_j\rangle$ |
| Rates $\{\nu_j\}$ | Pseudomode decay rates $\{\kappa_j\}$ derived from Lorentzian widths |
| Dissipation $-i\Gamma$ | Lindblad dissipators $\mathcal{D}[a_j]$ on pseudomodes (and optionally on the primary system) |
| FDT-locked noise $\eta$ | Quantum-mechanical Langevin noise satisfying the quantum FDT correlator at the bath temperature |

The mapping is exact at the memory subsystem level (the auxiliary-mode equation is structurally identical) and structural at the field-equation level (the primary system equation is a quantum master equation in the density operator, not a complex scalar PDE in field amplitude). This places the pseudomode framework in Class B of the cross-domain ledger: the memory module of the equation appears term-by-term in a quantum substrate, but the field type and the primary-equation form differ.

The auxiliary-mode dynamics, in the Heisenberg picture for expectation values, takes the form

$$\partial_t \langle a_j\rangle = -i\omega_j \langle a_j\rangle - \tfrac{\kappa_j}{2}\langle a_j\rangle + g_j \langle O\rangle,$$

which, for $\omega_j = 0$ (memory-only sector with no internal oscillation in the pseudomode) and identifying $\langle a_j\rangle$ with $y_j$, $\kappa_j$ with $2\nu_j$, $g_j \langle O\rangle$ with $\nu_j \rho$, reduces to the equation's auxiliary-field update $\partial_t y_j = \nu_j(\rho - y_j)$. The general pseudomode includes internal oscillation; the present equation's auxiliary-field sector is the over-damped limit of this more general structure.

## Time as calibration in this substrate

The pseudomode substrate has substrate-specific timescales spanning quantum optics, condensed matter, and chemical physics. Representative scales:

- $T_{\text{system}} \sim 10^{-15}$ to $10^{-12}$ s: atomic or vibrational system periods
- $\tau_{\text{bath corr}} \sim 10^{-15}$ to $10^{-9}$ s: bath correlation time set by Lorentzian widths
- $\tau_{\text{decoh}} \sim 10^{-12}$ to $10^{-3}$ s: system decoherence time
- $\tau_{\text{thermal}} \sim \hbar/k_B T$: thermal correlation time at bath temperature

Per [`../methodology/07-time-as-calibration.md`](../methodology/07-time-as-calibration.md), the equation's unit time is calibrated to the relevant pseudomode timescale when comparing the equation to non-Markovian open-quantum-system literature. For decoherence studies, calibration to $\tau_{\text{decoh}}$ is natural; for vibrational-mode studies, calibration to $T_{\text{system}}$.

## What this correspondence does and does not establish

It does not establish that the present equation is the underlying description of non-Markovian open quantum systems. The appropriate description is the quantum master equation on the extended Hilbert space (Garraway, Tamascelli, Pleasance), with explicit density-operator dynamics and quantum statistical structure. The present equation, applied to the quantum substrate, captures the memory-subsystem structural form but not the full quantum-mechanical apparatus.

It does not establish that all open quantum systems instantiate the full triangle. Strict Born-Markov systems (weakly coupled to white-noise baths) are described by a memoryless Lindblad master equation without auxiliary modes; they are degenerate cases where the structural prediction's full content does not apply. The pseudomode framework is the regime where non-Markovian memory matters.

It does establish that the equation's memory subsystem $\partial_t y_j = \nu_j(\rho - y_j)$ is mathematically identical, in the over-damped limit, to the pseudomode operator equation in the quantum-substrate Lindblad master equation framework. The convergence is non-trivial because the two frameworks were developed independently: the present equation from physics-philosophy axioms about persistent extended entities, the pseudomode framework from quantum open-system theory targeting exact non-Markovian reproduction. The convergence on the same memory module is structural evidence under criterion 4 (cross-domain coherence).

## Common dismissals and why they do not apply

**"Pseudomode is a numerical trick, not physical."** The opposite is the case. The Garraway-Tamascelli-Pleasance pseudomode framework is a rigorous mathematical theorem about reduced dynamics: when the bath spectral density is a finite sum of Lorentzians, the system-plus-pseudomode dynamics is exact, not approximate. The pseudomodes have physical interpretation as collective excitations of the structured bath in the modes most strongly coupled to the system. The framework is widely used in production quantum-optical simulations and produces empirically correct predictions where Born-Markov fails.

**"Density matrices are different from wave functions; the mapping does not apply."** The structural correspondence is at the memory subsystem level, where the auxiliary modes satisfy operator equations whose expectation-value form is identical to the auxiliary-field equation of the present work. The full field equation differs (density operator vs complex scalar PDE), and this is acknowledged in the Class B classification. The structural fact, that the memory module is mathematically the same in both substrates, is what the correspondence captures.

**"Quantum is fundamentally different from classical."** The triangle structure P1+P2+P3 is substrate-independent by construction (per [`../methodology/01-structural-realism.md`](../methodology/01-structural-realism.md)); it asserts a relational structure that any persistent extended entity must instantiate, regardless of substrate. The pseudomode framework is one specific way the triangle is instantiated in a quantum substrate; the diagonal SSM correspondence (in the [`mnsm-ml`](https://github.com/qrv0/mnsm-ml) spinoff) is another way in a computational substrate; the auxiliary-field memory of the present equation is the way in a physical-field substrate. The structural form is preserved across these instantiations; the substrate-specific details differ.

**"This is convergence by mathematical structure alone, not physics."** Mathematical convergence is exactly what criterion 4 (cross-domain coherence) is designed to detect. The argument is not that pseudomode physics IS the physics of the equation. The argument is that two independently developed frameworks, addressing structurally similar problems (efficient finite-rank representation of fading memory in a coupled system), arrive at the same mathematical module. The convergence is structural evidence for the form, regardless of whether the physical interpretations align.

## Locally testable predictions and observational signatures

The structural claim of this interface (the auxiliary-field memory of the present equation is mathematically identical to the pseudomode operator equation of the non-Markovian open-quantum-system framework) is evaluated by cross-domain coherence (methodology/04 criterion 4), not by single-experiment refutation. The following are local predictions that can be tested by numerical or empirical methods (per principles/03-coupling.md). Inconsistent evidence would shift evidentiary weight against this interface's specific calibration under criterion 4, without bearing on the global structural claim.

- **Prediction P18.1: Numerical equivalence of memory-subsystem reproduction for Lorentzian spectral density.** The structural prediction is that for a single Lorentzian bath spectral density $J(\omega) = (\eta \gamma / \pi) / ((\omega - \omega_0)^2 + \gamma^2)$, the system observable trajectory computed via direct convolution with the bath correlation function should match the trajectory computed via pseudomode embedding (one auxiliary mode with decay rate $\kappa = 2\gamma$) to within numerical precision, and both should match the auxiliary-field embedding of the present equation when reduced to the over-damped limit.
  - How to test: numerical simulation of a two-level system coupled to a single Lorentzian bath, using (a) direct integro-differential evolution with the bath correlation, (b) pseudomode Lindblad master equation, (c) present equation's auxiliary-field embedding in over-damped limit. Compare excited-state population dynamics across the three methods.
  - What would constitute confirmation: relative error across the three methods below $10^{-8}$ in fp64 numerics over the system lifetime.
  - What would constitute evidence inconsistent with this calibration: persistent disagreement above numerical floor, indicating that the embedding equivalence breaks at some non-trivial point.
  - Status: **not yet tested**, candidate for numerical implementation in [`../experiments/physics/`](../experiments/physics/).

- **Prediction P18.2: Pseudomode count scales with rational rank of bath spectral density.** The structural prediction is that the number $N$ of auxiliary pseudomodes required to reproduce non-Markovian dynamics to a fixed accuracy scales with the rank of the rational fit to the bath spectral density (number of Lorentzian peaks plus background poles). For sub-Ohmic baths with power-law spectral density, the required $N$ scales logarithmically with the desired temporal range.
  - How to test: vary bath spectral density (single Lorentzian, sum of two, sum of three, super-Ohmic, sub-Ohmic) and measure pseudomode count required for fixed reproduction accuracy. Compare with theoretical rational-rank prediction.
  - What would constitute confirmation: pseudomode count tracks rational rank as predicted.
  - What would constitute evidence inconsistent with this calibration: count scales independently of rational rank or with different functional form.
  - Status: **not yet tested**.

- **Prediction P18.3: FDT-locked thermal noise on pseudomodes recovers Caldeira-Leggett thermalization.** The structural prediction is that adding thermal noise to the pseudomode dissipators (raising the bath from zero to finite temperature $T$, with noise correlator locked to dissipator rate by quantum FDT) drives the primary system to the canonical thermal state $\rho_S \propto e^{-H_S/k_B T}$ at long times, matching the Caldeira-Leggett prediction for system-bath thermalization in the appropriate parameter regime.
  - How to test: pseudomode simulation with thermal Lindblad dissipators at varied temperatures; measure long-time state of primary system; compare with $e^{-H_S/k_B T}$.
  - What would constitute confirmation: long-time state agreement with canonical thermal state across temperature range.
  - What would constitute evidence inconsistent with this calibration: persistent deviation from canonical thermal state, indicating that the FDT lock as implemented does not produce correct quantum thermalization.
  - Status: **not yet tested**.

## References

Cited as credit, not legitimization (per [`../methodology/01-structural-realism.md`](../methodology/01-structural-realism.md) "Prior art and credit"):

- Breuer, H.-P., & Petruccione, F. (2007). *The Theory of Open Quantum Systems*. Oxford University Press.
- Garraway, B. M. (1997). Nonperturbative decay of an atomic system in a cavity. *Physical Review A* **55**, 2290.
- Lorenzo, S., Plastina, F., & Paternostro, M. (2016). Class of exact memory-kernel master equations. arXiv:1603.00248.
- Pleasance, G., Garraway, B. M., & Petruccione, F. (2020). Generalized theory of pseudomodes for exact descriptions of non-Markovian quantum processes. *Physical Review Research* **2**, 043058.
- Tamascelli, D., Smirne, A., Lim, J., Huelga, S. F., & Plenio, M. B. (2018). Nonperturbative treatment of non-Markovian dynamics of open quantum systems. *Physical Review Letters* **120**, 030402.
