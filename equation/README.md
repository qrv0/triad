# Equation

This folder contains the formal mathematical content. It is downstream of [`../principles/`](../principles/) and upstream of [`../results/`](../results/) and [`../interfaces/`](../interfaces/).

| File | Content |
|---|---|
| [`01-derivation.md`](01-derivation.md) | From P1, P2, P3 to the equation. Each principle yields a specific structural term. |
| [`02-markovian-embedding.md`](02-markovian-embedding.md) | The Mori–Zwanzig projection that reduces the integro-differential memory potential to a finite system of local ordinary differential equations via auxiliary fields. |
| [`03-two-dimensional.md`](03-two-dimensional.md) | The equation in two spatial dimensions. The L²-critical regime. |
| [`04-three-dimensional.md`](04-three-dimensional.md) | The equation in three spatial dimensions. The L²-supercritical regime. Dimensional rescaling of the memory coupling. |
| [`05-reductions.md`](05-reductions.md) | The classical equations that appear as limits when specific terms are neutralized. |

The full equation, with all terms active:

$$
\boxed{\;
i\hbar\, \partial_t \Psi = \left[\,-\frac{\hbar^2}{2m} D^2 + V_{\text{ext}} + \Lambda |\Psi|^2 + V_{\text{mem}} + \alpha (-\Delta)^{\sigma/2} - i\Gamma\,\right]\Psi + \eta\;
}
$$

with auxiliary fields $y_j$ evolving by $\partial_t y_j = \nu_j(\rho - y_j)$ and $V_{\text{mem}} = \sum_j \lambda_j y_j$, and noise $\eta$ satisfying the fluctuation-dissipation correlator.

The mathematical content of this folder is what [`../implementation/`](../implementation/) computes and what [`../paper/manuscript.md`](../paper/manuscript.md) reports.
