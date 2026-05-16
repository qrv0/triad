# Open problem 01: Analytical derivation of the anti-collapse mechanism

**Status:** Open. Numerical evidence exists; analytical derivation does not.

## Precise statement

For the equation
$$
i\hbar\, \partial_t \Psi = \left[-\tfrac{\hbar^2}{2m}\nabla^2 + \Lambda |\Psi|^2 + V_{\text{mem}}\right]\Psi
$$
with $V_{\text{mem}} = \sum_j \lambda_j y_j$ and $\partial_t y_j = \nu_j(\rho - y_j)$, $\rho = |\Psi|^2$, derive the condition under which the memory potential overshoot $V_{\text{mem}}$ exceeds the cubic attraction $|\Lambda| \rho$ at the collapse focal region, releasing the field outward.

The derivation should yield: (a) an analytical bound on the peak density separation ratio between memoried and unmemoried runs as a function of $(\Lambda, \Sigma\lambda, \nu_{\text{slow}}, d)$; (b) the dimensional rescaling relation $\Sigma\lambda / |\Lambda| \sim 1/d$ as a derived consequence rather than a numerical observation; (c) the boundary in parameter space between regimes where anti-collapse operates and where it does not.

## What is known

- Numerical evidence at 2D ([`../results/01-anti-collapse-2d.md`](../results/01-anti-collapse-2d.md)) shows three-orders-of-magnitude peak-density separation between memoried and unmemoried runs at $\Lambda = -8$, $\Sigma\lambda \sim 0.4$.
- Numerical evidence at 3D ([`../results/04-anti-collapse-3d.md`](../results/04-anti-collapse-3d.md)) shows $10^5\times$ separation at $\Lambda = -8$, $\Sigma\lambda \sim 4$.
- The dimensional rescaling $\Sigma\lambda / |\Lambda| \sim 1/d$ is documented numerically in [`../results/06-dimensional-rescaling.md`](../results/06-dimensional-rescaling.md), with the structural argument that 2D focal volume scales as $\xi^2$ and 3D as $\xi^3$.
- The mechanism is qualitatively understood: $y_j$ relaxes toward $\rho$ at rate $\nu_j$, so $V_{\text{mem}}$ peaks after the focal density does; in the overshoot window $V_{\text{mem}} > |\Lambda|\rho$ and the field is released. The slow mode ($\nu = 0.5$, $\tau = 2$) is structurally essential; the fast mode alone cannot produce the lag.

## What is missing

- A derivation that starts from the equation and ends with a closed-form expression for the separation ratio (or a rigorous bound on it) as a function of the parameters.
- A characterization of the boundary between the anti-collapse and collapse regimes in $(\Lambda, \Sigma\lambda, \nu_j, d)$ space that does not depend on numerical sweeps.
- An analytical version of the dimensional rescaling relation.

## What would constitute progress

- A perturbative derivation linearizing around the collapse focal region that yields the leading-order overshoot magnitude as a function of $(\Lambda, \Sigma\lambda, \nu_{\text{slow}}, d)$.
- A rigorous (non-perturbative) bound on the separation ratio, even if the bound is loose.
- A clear identification of the small parameter that the perturbative expansion is in (most likely $\nu_{\text{slow}} / |\Lambda \rho_{\text{peak}}|$, the ratio of the memory relaxation rate to the focal nonlinear timescale).
- Numerical validation of the analytical prediction against the existing results at 2D and 3D, with stated tolerance.
- A reformulation showing the dimensional rescaling $\Sigma\lambda / |\Lambda| \sim 1/d$ as a corollary of the analytical derivation.

## Suggested approaches

- **Townes profile linearization.** The 2D L²-critical collapse is well-studied (Sulem & Sulem 1999); near the Townes profile the radial concentration $\rho(r, t) \approx |\Psi_T(\xi)|^2 / L(t)^2$ where $L(t) \to 0$ at finite time and $\xi = r/L$ is the rescaled radial coordinate. Compute $V_{\text{mem}}$ at the focal region using this approximation and the OU dynamics of $y_j$. The overshoot condition then becomes a relation between $L(t)$ and $\nu_{\text{slow}}$.
- **WKB-type analysis.** Treat the memory dynamics in the WKB regime where the field evolution is rapid compared to $\nu_{\text{slow}}$ but slow compared to $\nu_{\text{fast}}$. Expand around the moment of maximum density.
- **Variational ansatz.** Parameterize the field with a Gaussian-of-Gaussians ansatz of varying width; derive ODEs for the width parameters; analyze the fixed-point structure of the augmented system including the auxiliary fields.
- **Multiple-scale analysis.** Separate timescales: the fast (collapse) dynamics from the slow (memory equilibration) dynamics; apply method of multiple scales to derive an effective equation for the slow envelope.

## Connections to existing repo content

- [`../principles/02-self-reference.md`](../principles/02-self-reference.md) section "A structural observation about the two parts": the qualitative argument is here; the open problem is to make it quantitative.
- [`../equation/02-markovian-embedding.md`](../equation/02-markovian-embedding.md): the auxiliary-field embedding gives the form of the memory dynamics; the open problem uses this form.
- [`../results/01-anti-collapse-2d.md`](../results/01-anti-collapse-2d.md), [`../results/04-anti-collapse-3d.md`](../results/04-anti-collapse-3d.md), [`../results/06-dimensional-rescaling.md`](../results/06-dimensional-rescaling.md): numerical results the derivation must reproduce.
- [`../methodology/04-the-six-criteria.md`](../methodology/04-the-six-criteria.md) criterion 1 (internal mathematical consistency): a successful analytical derivation strengthens criterion 1 substantially.
- [`02-phase-diagram.md`](02-phase-diagram.md): the boundary characterized analytically here would feed directly into the phase-diagram open problem.
