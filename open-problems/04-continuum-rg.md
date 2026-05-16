# Open problem 04: Renormalization-group flow of the equation

**Status:** Open. No RG analysis exists.

## Precise statement

Compute the renormalization-group flow of the equation
$$
i\hbar\, \partial_t \Psi = \left[-\tfrac{\hbar^2}{2m}\nabla^2 + V_{\text{ext}} + \Lambda |\Psi|^2 + V_{\text{mem}} + \alpha (-\Delta)^{\sigma/2} - i\Gamma\right]\Psi + \eta
$$
under coarse-graining. Identify which couplings are relevant, marginal, or irrelevant in the RG sense. Look for fixed points. Determine which features of the equation are universal (survive coarse-graining) and which are non-universal (UV-sensitive and depend on microscopic details).

## What is known

- The equation reduces in various limits to known equations (Free Schrödinger, Gross-Pitaevskii, sub/supercritical NLS, Lindblad, stochastic Gross-Pitaevskii, fractional Schrödinger, Rashba) as catalogued in [`../equation/05-reductions.md`](../equation/05-reductions.md). Each reduction is a known field theory with its own RG behavior.
- The cubic nonlinearity $\Lambda |\Psi|^2$ has dimension $4-d$ in standard counting (where $d$ is spatial dimension). It is relevant for $d<4$, marginal at $d=4$, irrelevant for $d>4$. The equation operates in $d=2, 3$ where it is relevant.
- The memory potential $V_{\text{mem}}$ is non-local in time; its RG behavior under spatial coarse-graining is subtle because of the auxiliary-field structure.
- The FDT-locked noise/dissipation pair has a well-studied analogue in stochastic field theory (Hohenberg-Halperin 1977; Tauber 2014), where the noise is irrelevant for $d>2$ and marginal at $d=2$.

## What is missing

- The beta functions for $\Lambda$, $\{\lambda_j\}$, $\{\nu_j\}$, $\Gamma$, $\alpha$, $\sigma$ have not been computed.
- The fixed-point structure of the flow has not been characterized.
- The cross-over scales between the different reductions (when does the equation behave like bare NLS vs Gross-Pitaevskii vs stochastic GP?) have not been derived from RG.
- The universality class of the BCC-selecting crystalline state has not been identified.

## What would constitute progress

- One-loop beta functions for the principal couplings.
- Identification of relevant, marginal, irrelevant operators at the Gaussian fixed point.
- Identification of any non-trivial fixed points (Wilson-Fisher type at $d = 4 - \epsilon$, for instance).
- A statement about which features of the released crystalline state are universal vs non-universal.
- Connection to the universality classes catalogued in Hohenberg-Halperin (Model A, B, C, ..., H): which class does the equation belong to in the absence of memory? With memory?

## Suggested approaches

- **Wilsonian RG.** Standard momentum-shell integration; compute the change in effective couplings as high-momentum modes are integrated out. The memory kernel introduces non-trivial frequency dependence that may require Wilsonian analysis in $(\omega, k)$ space.
- **Functional RG (Wetterich equation).** Particularly suitable for the auxiliary-field structure; computes the effective action as a function of an infrared cutoff.
- **Field-theoretic perturbation theory.** Standard diagrammatic expansion around the Gaussian theory; compute one-loop corrections to all couplings.
- **Connection to dynamic critical phenomena.** The Hohenberg-Halperin classification (Models A through J) for stochastic systems is the natural starting point; the equation has Model A (relaxational, non-conserved order parameter) character with memory added.

## Connections to existing repo content

- [`../equation/05-reductions.md`](../equation/05-reductions.md): the reductions are different fixed points or RG-flow endpoints; the RG analysis explains why each reduction is the appropriate description at its scale.
- [`../principles/03-coupling.md`](../principles/03-coupling.md) section "Why FDT is structurally necessary": the FDT lock is the only condition under which the stationary distribution is well-defined; RG must respect this.
- [`02-phase-diagram.md`](02-phase-diagram.md): RG provides the scale at which different phase-diagram regions become controlling.
- [`03-topological-characterization.md`](03-topological-characterization.md): if BCC selection has topological character, RG tells us whether it is protected against perturbations.
- [`../methodology/04-the-six-criteria.md`](../methodology/04-the-six-criteria.md) criterion 6 (comprehensiveness): RG analysis brings the equation into contact with the standard machinery of statistical field theory.
