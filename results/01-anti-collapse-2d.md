# Anti-collapse in two dimensions

## What is observed

Under identical initial conditions and identical attractive coupling $\Lambda = -8$, the equation with memory active produces a final peak density approximately three orders of magnitude below the equation with memory inactive. The unmemoried equation locks into a lattice-clipped collapsed state at peak $\sim 100$; the memoried equation produces a transient spike of comparable magnitude that subsequently decays to peak $\sim 0.03$ by the end of the integration window.

## Specific run

| Parameter | Value |
|---|---|
| Lattice | $256 \times 256$ |
| Box length | $L = 20$ |
| Time step | $dt = 0.0025$ |
| Integration | 4000 steps (10 units of time) |
| Initial state | Gaussian, width $\sigma_0 = 1.2$, momentum $\mathbf{k}_0 = (1.0, 0.5)$ |
| Nonlinearity | $\Lambda = -8$ |
| Memory (active case) | $(\nu_1, \lambda_1) = (10, 0.3)$, $(\nu_2, \lambda_2) = (0.5, 0.1)$ |
| Memory (control case) | none |
| Dissipation, noise | $\gamma_0 = 0$, $T = 0$ |
| Precision | fp64 |
| Seed | 1234 |

The initial L² norm is 1, which exceeds the Townes-soliton threshold at $\sigma_0 = 1.2$; both runs are in the supercritical regime.

## Time series

| Time | No-memory run | With-memory run |
|---|---|---|
| $t = 0$ | peak 0.221, fwhm 2.5 | peak 0.221, fwhm 2.5 |
| $t \approx 2$ | peak $\sim 100$ (spike) | peak $\sim 80$ (spike) |
| $t \approx 5$ | peak $\sim 50$ (locked) | peak $\sim 0.5$ (decaying) |
| $t = 10$ | peak $\sim 50$ (locked) | peak $\sim 0.03$ (delocalized) |

The two runs share an essentially identical initial spike. They diverge after the peak: the unmemoried run remains locked at lattice scale, while the memoried run releases and the peak declines by three orders of magnitude.

## The mechanism

The memory potential $V_{\text{mem}} = \sum_j \lambda_j y_j$ tracks the density $\rho = |\Psi|^2$ with lag $\tau_j = 1/\nu_j$. When $\rho$ rises sharply during the initial collapse phase, the auxiliary fields $y_j$ rise with delay. By the time $V_{\text{mem}}$ has caught up to its equilibrium value $\sum_j \lambda_j \rho \approx 0.4 \rho_{\text{peak}}$, the density has already begun to decline (or, in the no-memory baseline, has already locked at lattice scale). The lag means that $V_{\text{mem}}$ transiently exceeds its instantaneous-equilibrium value: the slow mode at $\nu_2 = 0.5$ holds memory of the high density even after the peak passes.

In the high-density region, the total potential is

$$
V_{\text{tot}} = \Lambda \rho + V_{\text{mem}}.
$$

When $V_{\text{mem}}$ overshoots, this total switches sign locally: the field, which had been concentrating under the attractive $\Lambda \rho < 0$ term, now experiences a net repulsion $V_{\text{tot}} > 0$ and flows outward. The repulsion is geometrically focused at the same region where the collapse had been concentrating, because the memory is local in space.

The slow mode is essential. Without it, the fast memory mode would track $\rho$ too closely to overshoot. With the slow mode at $\tau_2 = 2$ units of time, the memory holds high after the peak has passed and the explosive outward dynamics is sustained long enough to actually release the field from the lattice configuration.

## What is not observed

The unmemoried run does not exhibit true singular blow-up. It exhibits lattice-clipped collapse: the field concentrates onto a single grid cell and remains there. The "peak density $\sim 100$" is the value at the single bright pixel; the rest of the lattice contains essentially zero density. True singular blow-up — peak density diverging continuously to infinity — would require a continuum limit and lattice refinement; what is observed at finite lattice is the regularized version of this singular behavior, where the lattice itself imposes a cutoff.

This caveat is important for interpretation. The structural claim is not that the memory prevents a mathematically singular blow-up; the structural claim is that the memory prevents the field from locking into the lattice-cell concentration that is the numerical signature of supercritical collapse. The two are consistent but not identical.

## Reproduction

```bash
python experiments/physics/reproduce_2d_anti_collapse.py
```

Expected wall time: ~3 minutes on RTX 4060. Output: trajectory `.npz` files for both runs, plus a comparison plot.

## Robustness

The finding has been replicated at $N = 512$ to confirm mesh-independence (the qualitative result is identical; the absolute peak values in the locked phase scale slightly with lattice resolution as expected). The finding has been replicated across $\Lambda \in [-6, -12]$; the separation between memoried and unmemoried final states is preserved across this range, with the absolute final peak values varying.

The finding is sensitive to the slow-mode coupling $\lambda_2$. Reducing $\lambda_2$ to zero (single-mode memory at $\nu_1 = 10$) substantially weakens the anti-collapse effect: the unmemoried-memoried separation drops to approximately one order of magnitude. Increasing $\lambda_2$ above $\sim 0.5$ shifts the regime into one where the field disperses more uniformly without forming the post-release crystalline pattern documented in [`02-spontaneous-crystallization.md`](02-spontaneous-crystallization.md).

## Structural significance

The anti-collapse mechanism is absent from any of the equation's single-term reductions (see [`../equation/05-reductions.md`](../equation/05-reductions.md)). The bare cubic NLS produces only the collapse; the bare memory equation has no nonlinearity to amplify; the bare dissipation equation simply decays. The mechanism emerges only when the cubic nonlinearity and the multi-mode memory potential are both active simultaneously, and it is the delayed response between them that produces the regularization. This is a concrete instance of the structural claim made in [`../principles/02-self-reference.md`](../principles/02-self-reference.md): the two parts of self-reference (instantaneous and across-time) are jointly necessary, and the dynamics produced by their coupling is qualitatively different from the dynamics of either part alone.
