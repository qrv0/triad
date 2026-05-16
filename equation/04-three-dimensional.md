# The equation in three spatial dimensions

In three spatial dimensions ($n = 3$), the cubic nonlinear Schrödinger equation is L²-supercritical. Finite-time blow-up occurs for any sufficiently concentrated initial state, with no critical-norm threshold below which collapse is forbidden (Sulem & Sulem 1999). The anti-collapse mechanism of the memory regularization is therefore a stronger structural claim in three dimensions than in two: there is no kinematic-pressure regime in which the field is protected from collapse without the memory acting.

## The equation

$$
i\hbar\, \partial_t \Psi = \left[\,-\frac{\hbar^2}{2m} D^2 + V_{\text{ext}} + \Lambda |\Psi|^2 + V_{\text{mem}} + \alpha (-\Delta)^{\sigma/2} - i\Gamma\,\right]\Psi + \eta
$$

with $\mathbf{x} = (x, y, z) \in \mathbb{R}^3$, periodic boundary conditions on a cube of side $L$, and the standard auxiliary-field memory potential. The form of the equation is identical to the two-dimensional case; only the spatial dimension changes.

## Three-dimensional supercriticality

The L² norm in three dimensions does not provide a critical threshold below which the field is protected. For any nonzero attractive coupling $\Lambda < 0$ and any initial state with sufficient peak density, the unmemoried equation drives finite-time blow-up. The collapse rate and the prefactors depend on the specific initial conditions, but the structural fact, that collapse is generic, is dimension-independent.

This has the practical consequence that the choice of initial Gaussian width $\sigma_0$ for three-dimensional anti-collapse experiments must place the initial peak density above the dimensional collapse threshold. For $\Lambda = -8$ and box length $L = 20$ in standard units, the collapse threshold is approximately $\sigma_0 \approx 0.68$ (derived from the dimensional analysis of the virial-like kinetic–nonlinear energy balance). Initial widths $\sigma_0 \le 0.6$ collapse; widths $\sigma_0 \ge 0.7$ disperse without collapsing. The headline 3D results use $\sigma_0 = 0.5$ to ensure a clean collapse signal.

## Dimensional rescaling of the memory coupling

The most consequential structural finding of the three-dimensional investigation is that the memory coupling required to release the supercritical collapse is not the same as in two dimensions. In two dimensions, total memory coupling $\Sigma\lambda \sim 0.4$ at $\Lambda = -8$ suffices to release the collapse. In three dimensions, $\Sigma\lambda \sim 0.4$ at $\Lambda = -8$ does not release the collapse at all; the field remains lattice-trapped at peak density $\sim 60$. The total memory coupling must scale up by approximately an order of magnitude to recover the anti-collapse phenomenology.

The scaling is structural and derivable. At the lattice-clipped peak, the memory potential at the focal region is $V_{\text{mem}} \sim \Sigma\lambda \cdot \rho_{\text{eff}}$, where $\rho_{\text{eff}}$ is the density averaged over the spatial region in which the memory has accumulated. In two dimensions, the collapse focal region covers approximately $10^2$ lattice cells, and $\rho_{\text{eff}} \approx \rho_{\text{max}}$. In three dimensions, the collapse focal region covers approximately $10$ lattice cells; the density gradient is steeper in higher dimension, and the focal region is correspondingly smaller in voxel count. Consequently, $\rho_{\text{eff}} \approx \rho_{\text{max}}/10$ in three dimensions, and to produce the same ratio $V_{\text{mem}} / |\Lambda \rho|$ at the peak, $\Sigma\lambda$ must scale up by approximately one order of magnitude.

The empirical regime that recovers anti-collapse in three dimensions at $\Lambda = -8$ is $\Sigma\lambda \sim 4$, distributed as a fast mode ($\nu_1 = 10, \lambda_1 = 3.0$) and a slow mode ($\nu_2 = 0.5, \lambda_2 = 1.0$). The ratio $\Sigma\lambda / |\Lambda| \sim 0.5$ characterizes the 3D regime, an order of magnitude larger than the 2D ratio of approximately 0.05.

The full derivation and the numerical evidence are in [`../results/06-dimensional-rescaling.md`](../results/06-dimensional-rescaling.md).

## Bravais symmetry selection

In three dimensions, the post-release crystalline configuration must choose among more lattice options than in two dimensions. The four canonical Bravais lattices, simple cubic (SC), body-centered cubic (BCC), face-centered cubic (FCC), and hexagonal close-packed (HCP), provide structurally distinct candidates. The equation, integrated from an unstructured Gaussian initial state, consistently selects **body-centered cubic (BCC)** symmetry. The selection is robust across the swept range of memory couplings $\Sigma\lambda \in [0.5, 1.5]$ at $\Lambda = -8$.

The detection algorithm, implemented in [`../implementation/physics/observables.py`](../implementation/physics/observables.py), computes the angular distribution of power on a thin spherical shell in $k$-space at the dominant radial wavenumber $k^*$, and scores the shell-integrated power against the canonical Bravais signatures. The full results are in [`../results/05-bravais-selection.md`](../results/05-bravais-selection.md).

## The crystalline window

The three-dimensional crystalline regime is narrower than the two-dimensional one. At $\Lambda = -8$, the parameter window in which the field is both released (peak density below lattice scale) and crystalline (Bravais signature above disorder threshold) is approximately $\Sigma\lambda \in [1.2, 1.8]$. Below this window the field remains lattice-trapped; above it the field disperses completely, losing the Bravais signature.

The narrower window is consistent with the structural argument: the three-dimensional supercritical collapse is more aggressive than the two-dimensional critical collapse, so the parameter range over which the memory regularization holds the field in a stable extended configuration is correspondingly smaller.

## Numerical specification

For the headline three-dimensional results (anti-collapse, Bravais selection, vibration window):

| Parameter | Value |
|---|---|
| Lattice | $128^3$ |
| Box length | $L = 20$ |
| Time step | $dt = 0.0025$ |
| Initial state | Gaussian with width $\sigma_0 = 0.5$, momentum $\mathbf{k}_0 = (0, 0, 0)$ |
| Nonlinearity | $\Lambda = -8$ (varied for sweeps) |
| Memory (anti-collapse demo) | $(\nu_1, \lambda_1) = (10, 3.0)$, $(\nu_2, \lambda_2) = (0.5, 1.0)$ |
| Memory (crystalline regime) | $\Sigma\lambda = 1.5$, split 3:1 fast:slow |
| Dissipation, noise | $\gamma_0 = 0$, $T = 0$ (conservative regime) |
| Integration | $n_{\text{steps}} = 4000$ |
| Precision | fp32 |

The reproduction scripts are in [`../experiments/physics/`](../experiments/physics/).
