# Open problem 02: Full phase diagram of the equation

**Status:** Open. Several regions of parameter space are characterized; the comprehensive map does not exist.

## Precise statement

Map the dynamical regimes of the equation
$$
i\hbar\, \partial_t \Psi = \left[-\tfrac{\hbar^2}{2m}\nabla^2 + V_{\text{ext}} + \Lambda |\Psi|^2 + V_{\text{mem}} + \alpha (-\Delta)^{\sigma/2} - i\Gamma\right]\Psi + \eta
$$
across the parameter space $(\Lambda, \Sigma\lambda, \nu_{\text{slow}}, \nu_{\text{fast}}, \sigma, \Gamma, T, d)$. For each region, identify the qualitative behavior (subcritical dispersive, supercritical-no-memory collapse, supercritical-with-memory-insufficient collapse, supercritical-with-memory-sufficient anti-collapse, crystalline, chaotic, runaway) and the critical surfaces separating regions.

## What is known

- **Anti-collapse vs collapse boundary** at 2D and 3D, partially mapped: [`../results/01-anti-collapse-2d.md`](../results/01-anti-collapse-2d.md) and [`../results/04-anti-collapse-3d.md`](../results/04-anti-collapse-3d.md) document the regime where anti-collapse operates.
- **Dimensional rescaling**: [`../results/06-dimensional-rescaling.md`](../results/06-dimensional-rescaling.md) gives $\Sigma\lambda/|\Lambda| \sim 1/d$ for the boundary.
- **BCC crystalline regime** at 3D with $\Sigma\lambda \approx 1.5$, documented in [`../results/05-bravais-selection.md`](../results/05-bravais-selection.md).
- **Vibrational mode structure** of the crystalline state in 2D and 3D, in [`../results/03-vibrational-modes.md`](../results/03-vibrational-modes.md).
- **Temporal-spatial asymmetry** of memory: [`../results/07-temporal-spatial-asymmetry.md`](../results/07-temporal-spatial-asymmetry.md) shows spatial non-locality destroys regularization.
- **Optimization-dynamics analogue**: [`mnsm/results/01-optimization-collapse-empirical.md`](https://github.com/qrv0/mnsm/blob/main/results/01-optimization-collapse-empirical.md) documents the failure mode at 70M parameters without anti-collapse.
- **Reductions to known equations**: [`../equation/05-reductions.md`](../equation/05-reductions.md) catalogues the limits where the equation reduces to standard NLS, Gross-Pitaevskii, Lindblad, stochastic GP, fractional Schrödinger, Rashba.
- **First focused 2D slice $(\Sigma\lambda, \gamma_0)$ at d=3**: [`../results/26-phase-diagram-2d-slice.md`](../results/26-phase-diagram-2d-slice.md). 5x4 grid in canonical 3D anti-collapse config (N=48, $\sigma_{\text{init}}=0.5$ normalized, $\Lambda=-8$, $T_{\text{bath}}=10^{-3}$, 75/25 memory split). Regime structure: released dominates the low-$\gamma_0$ region across all $\Sigma\lambda \in [0.5, 4.0]$; intermediate at moderate $\gamma_0$; dispersive at high $\gamma_0=1.0$ with high $\Sigma\lambda=4.0$. No collapse or runaway observed (the anti-collapse mechanism prevents focal locking).
- **2D slice $(\Sigma\lambda, \gamma_0)$ at d=2**: [`../results/27-phase-diagram-d2-slice.md`](../results/27-phase-diagram-d2-slice.md). 5x4 grid in canonical anti-collapse config extended to d=2 (N=128, $\sigma_{\text{init}}=0.5$ normalized with 2D L2 norm, $\Lambda=-8$, $T_{\text{bath}}=10^{-3}$, 75/25 memory split, initial peak 1.273). Regime structure: released dominates 13/20 across $\Sigma\lambda \in [0.05, 2.0]$ at $\gamma_0 \le 0.2$; dispersive fills the entire $\gamma_0 = 1.0$ column (5/20); intermediate at the two corners $(0.05, 0.01)$ and $(2.0, 0.2)$. No collapse or runaway. Transient peak_growth $\sim 20\times$ initial in the released regime (vs $\sim 5\text{-}8\times$ at d=3), consistent with d=2 L2-critical mechanism.
- **2D slice $(\Sigma\lambda, \gamma_0)$ at d=4**: [`../results/28-phase-diagram-d4-slice.md`](../results/28-phase-diagram-d4-slice.md). 5x4 grid in canonical anti-collapse config extended to d=4 (N=16, $\sigma_{\text{init}}=0.5$ normalized with 4D L2 norm, $\Lambda=-8$, $T_{\text{bath}}=10^{-3}$, 75/25 memory split, initial peak 0.403). Regime structure: dispersive across all 20 points. The field never enters focal growth (peak_growth=1.00 everywhere) because the d=4 initial peak is below the focal-collapse threshold at this lattice resolution (N=16 with L=20 places $dx=1.25 > \sigma=0.5$, underresolving the Gaussian). The result documents what the canonical convention produces at d=4 with this voxel budget; the dimensional-rescaling-series convention (sigma=0.4 non-normalized) tests the focal-collapse regime at d=4 separately ([`../results/10-dimensional-rescaling-higher-d.md`](../results/10-dimensional-rescaling-higher-d.md)).
- **d=6 dimensional rescaling result**: [`../results/24-dimensional-rescaling-d6.md`](../results/24-dimensional-rescaling-d6.md). At d=6, $\Sigma\lambda=0$ baseline is already dispersive (no memory needed); memory-driven runaway only at $\Sigma\lambda=32$. The "anti-collapse threshold" notion does not apply cleanly at this high d in the chosen configuration.

## What is missing

- A unified map of all regimes in a single parameter-space figure (or set of 2D slices through the higher-dimensional space).
- The complete inventory of regimes including any not yet observed (chaotic, runaway, partial release, multi-stable).
- The critical surfaces (codimension-1 manifolds in parameter space) separating regimes, characterized either analytically or numerically.
- The phase structure as a function of $\Gamma$ and $T$ (the FDT-locked dissipation/noise pair) which has been largely unexplored.
- The role of $\sigma$ (fractional Laplacian exponent) in shifting boundaries.

## What would constitute progress

- A figure (or set of figures) presenting 2D slices through the higher-dimensional parameter space, with each region color-coded by qualitative regime.
- Numerical scripts (additions to [`../experiments/physics/`](../experiments/physics/)) that reproduce the phase diagram from fixed seeds.
- Analytical bounds (if available) on the critical surfaces, from [`01-analytical-anti-collapse.md`](01-analytical-anti-collapse.md) or independent analysis.
- Identification of any new regime not previously documented (e.g., bistable, oscillatory between collapse and release, chaotic anti-collapse).
- Documentation of the phase diagram's behavior under variation of $\Gamma$ and $T$.
- A discussion of how the cross-substrate predictions (BAO regime, gamma regime, SSM training-dynamics regime, cosmological regime) are positioned on the phase diagram under their respective calibrations.

## Suggested approaches

- **Brute-force sweep.** A grid sweep over $(\Lambda, \Sigma\lambda, \nu_{\text{slow}})$ with fixed $\sigma$, $\Gamma$, $T$, classifying each grid point by the qualitative regime of the resulting trajectory. Computationally expensive but feasible on consumer GPU hardware.
- **Bifurcation analysis.** Identify the critical points where regimes change; characterize the bifurcations (saddle-node, pitchfork, Hopf, period-doubling) at each.
- **Order parameter analysis.** Define an order parameter for each regime (peak density for collapse, structure factor for crystalline, Lyapunov exponent for chaotic) and map its variation across parameter space.
- **Adiabatic continuation.** Start from a known regime (e.g., bare NLS at small $\Lambda$) and continuously vary parameters, tracking when the trajectory qualitatively changes.

## Connections to existing repo content

- [`01-analytical-anti-collapse.md`](01-analytical-anti-collapse.md): analytical derivation feeds directly into the phase-diagram boundaries.
- [`../equation/05-reductions.md`](../equation/05-reductions.md): each known reduction sits at a specific point or region in parameter space; the phase diagram contextualizes them.
- [`../experiments/physics/`](../experiments/physics/): existing reproduction scripts can be augmented with sweep scripts.
- [`../methodology/04-the-six-criteria.md`](../methodology/04-the-six-criteria.md) criterion 3 (generative scope): a comprehensive phase diagram demonstrates the equation's generative scope in concrete cartographic form.
- [`07-additional-substrates.md`](07-additional-substrates.md): new substrates considered there will need their calibration mapped to a point in the phase diagram.
