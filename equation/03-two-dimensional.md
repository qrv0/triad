# The equation in two spatial dimensions

In two spatial dimensions ($n = 2$), the cubic nonlinear Schrödinger equation is L²-critical: finite-time blow-up occurs when the initial L² norm exceeds the Townes-soliton threshold (Sulem & Sulem 1999), and the field disperses freely below threshold. This document specializes the general equation to the two-dimensional case and notes the consequences for the memory regularization.

## The equation

$$
i\hbar\, \partial_t \Psi = \left[\,-\frac{\hbar^2}{2m} D^2 + V_{\text{ext}} + \Lambda |\Psi|^2 + V_{\text{mem}} + \alpha (-\Delta)^{\sigma/2} - i\Gamma\,\right]\Psi + \eta
$$

with $\mathbf{x} = (x, y) \in \mathbb{R}^2$, periodic boundary conditions on a square of side $L$, and the standard auxiliary-field memory potential $V_{\text{mem}} = \sum_j \lambda_j y_j$, $\partial_t y_j = \nu_j(\rho - y_j)$. The covariant derivative reduces to $D = \nabla$ unless an external gauge potential is included.

## L²-criticality in two dimensions

The bare cubic NLS in two dimensions admits a one-parameter family of self-similar collapsing solutions whose L² norm is exactly the Townes-soliton norm $\|\Psi_T\|_{L^2}^2 \approx 1.86$ in standard units. Solutions with initial norm strictly below this threshold disperse to zero; solutions with norm exactly at threshold are marginally stable in the linearization but unstable under any infinitesimal perturbation in the direction of further concentration; solutions with norm strictly above threshold undergo finite-time blow-up.

This places strong constraints on the equation's two-dimensional phenomenology. The supercritical regime, initial conditions whose L² norm exceeds the Townes threshold, is the regime in which the unmemoried equation produces dramatic blow-up. It is also the regime in which the memory regularization (see [`../results/01-anti-collapse-2d.md`](../results/01-anti-collapse-2d.md)) produces its most striking phenomenology. The contrast is sharp because the unmemoried baseline is sharp: without memory, the field hits the lattice cutoff; with memory, the field is released back to dispersed.

## The memory coupling regime

The two-dimensional anti-collapse regime is achieved with relatively modest memory couplings. Total memory coupling $\Sigma\lambda \sim 0.4$, distributed as a fast mode at $\nu_1 = 10, \lambda_1 = 0.3$ and a slow mode at $\nu_2 = 0.5, \lambda_2 = 0.1$, is sufficient to release the supercritical collapse at $\Lambda = -8$. The ratio $\Sigma\lambda / |\Lambda| \sim 0.05$ characterizes the 2D regime.

This ratio is, as documented in [`../results/06-dimensional-rescaling.md`](../results/06-dimensional-rescaling.md), specific to two dimensions. The three-dimensional case requires a substantially larger ratio.

## The crystalline regime

For $\Lambda \sim -8$ and total memory coupling near $\Sigma\lambda \sim 1$, the post-collapse-release state organizes into a periodic two-dimensional spatial pattern. The pattern has a definite dominant wavenumber $k^* \approx 2.13$ in lattice units of the box of side $L$, corresponding to wavelength $\lambda_{\text{wave}} \approx 2.95$ lattice units. The wavelength is invariant under mesh refinement and across an interior region of $(\Lambda, \Sigma\lambda)$ parameter space.

The pattern is hexagonal in symmetry; in two dimensions the spontaneous lattice options are restricted (square or hexagonal at most), and the hexagonal is selected in the regimes studied. The selection is documented in [`../results/02-spontaneous-crystallization.md`](../results/02-spontaneous-crystallization.md).

## The vibrational regime

The crystalline state in two dimensions is not static. Each lattice point oscillates in time, and the spatial average of these oscillations exhibits structure: a median dominant frequency of approximately 0.6 cycles per unit time, with a secondary mode locked at exactly 1.0 cycles per unit time, both detected through per-pixel temporal Fourier analysis of densely sampled trajectories. See [`../results/03-vibrational-modes.md`](../results/03-vibrational-modes.md).

## Numerical specification

For the headline two-dimensional results (anti-collapse, crystallization, vibration spectrum):

| Parameter | Value |
|---|---|
| Lattice | $256^2$ (refined to $512^2$ for convergence checks) |
| Box length | $L = 20$ |
| Time step | $dt = 0.0025$ |
| Initial state | Gaussian with width $\sigma_0 = 1.2$, momentum $\mathbf{k}_0 = (1.0, 0.5)$ |
| Nonlinearity | $\Lambda = -8$ |
| Memory | $(\nu_1, \lambda_1) = (10, 0.3)$, $(\nu_2, \lambda_2) = (0.5, 0.1)$ |
| Dissipation, noise | $\gamma_0 = 0$, $T = 0$ (conservative regime) |
| Integration | $n_{\text{steps}} = 4000$ |
| Precision | fp64 for conservation runs, fp32 for production |

The reproduction script is [`../experiments/physics/reproduce_2d_anti_collapse.py`](../experiments/physics/reproduce_2d_anti_collapse.py).

## Two-dimensional reductions

When the equation's parameters are set to neutralize various terms, the two-dimensional case reduces to:

- $\Lambda = 0$, no memory, no $\Gamma$, no $\eta$: free 2D Schrödinger.
- $\Lambda \ne 0$, no memory, no $\Gamma$, no $\eta$: 2D Gross–Pitaevskii.
- $\Lambda < 0$, no memory, supercritical norm: standard 2D NLS, finite-time blow-up.
- All terms active: the equation studied here.

The presence of any single term alone, or any pair, fails to produce anti-collapse. The mechanism requires the simultaneous presence of nonlinearity, memory, and (in the dissipative case) FDT-locked noise. See [`05-reductions.md`](05-reductions.md) for the full reduction table.
