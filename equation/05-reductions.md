# Reductions to known equations

The equation derived in [`01-derivation.md`](01-derivation.md), with all terms active, is not in the standard catalog. When specific coupling constants are neutralized, however, the equation reduces to several familiar equations from established physics. This document tabulates the reductions.

## Reduction table

| Setting | Recovered equation | Reference |
|---|---|---|
| $\Lambda = 0$, no memory, no $\Gamma$, no $\eta$ | Free Schrödinger | Standard quantum mechanics textbooks |
| $\Lambda \ne 0$, no memory, no $\Gamma$, no $\eta$ | Gross–Pitaevskii equation | Pitaevskii & Stringari (2016) |
| $\Lambda \ne 0$ subcritical, no memory, no $\Gamma$ | Sub-critical NLS (dispersive) | Sulem & Sulem (1999) |
| $\Lambda \ne 0$ supercritical in 2D, no memory, no $\Gamma$ | Critical 2D NLS, finite-time blow-up | Sulem & Sulem (1999) |
| $\Lambda \ne 0$ in 3D, no memory, no $\Gamma$ | Supercritical NLS, generic blow-up | Sulem & Sulem (1999) |
| $\gamma_0 > 0$, no $\eta$ | Lindblad-type open quantum system | Breuer & Petruccione (2007) |
| $\gamma_0 > 0$, $\eta$ active, FDT-locked | Stochastic Gross–Pitaevskii / classical-field thermalization | Stoof (1999) |
| $\sigma < 2$, $\alpha \ne 0$, otherwise free | Fractional Schrödinger | Laskin (2018) |
| Spinor structure with $\alpha_R \ne 0$ and $\gamma_s = 0$ | Rashba spin–orbit Hamiltonian | Bychkov & Rashba (1984) |
| Spinor structure with $\alpha_R \ne 0$ and $\gamma_s \ne 0$ | Non-Hermitian skin Hamiltonian | Yao & Wang (2018); Bergholtz, Budich & Kunst (2021) |
| Memory active, all other terms zero | Linear OU dynamics for the auxiliary fields | Standard SDE textbooks |

## Why the reductions matter

The reductions place the equation in conversation with established physics rather than in isolation from it. Each reduction is a regime in which the equation predicts what an established equation already predicts. The numerical solver is validated against these reductions in [`../tests/test_conservation.py`](../tests/test_conservation.py):

- The free Schrödinger reduction is verified by checking norm conservation to machine precision over 400 integration steps.
- The Gross–Pitaevskii reduction is verified by checking that subcritical attractive states disperse without collapse and that supercritical attractive states collapse, both at the rates predicted by L²-critical or L²-supercritical theory.
- The pure-dissipation reduction is verified by checking that $\|\Psi\|^2(t)$ matches $e^{-2\gamma t} \|\Psi(0)\|^2$ to six significant figures.
- The FDT-thermalized reduction is verified by checking that the stationary $\langle |\Psi|^2 \rangle$ per cell matches the equipartition value $2T$ to within 0.5%.

These checks pass simultaneously, which is non-trivial: a numerical scheme that passed one but failed another would indicate a structural inconsistency in the solver. The simultaneous passage indicates that the solver is implementing the equation correctly across the regimes its reductions cover.

## What the full equation is not

The reductions list is also a list of what the full equation is *not*. The full equation, with all terms active, is not Schrödinger; it has nonlinearity, memory, dissipation, and noise. It is not Gross–Pitaevskii; it has memory, dissipation, and noise. It is not a Lindblad open system; it has nonlinearity, memory, and noise. It is not fractional NLS; it has memory, dissipation, and noise. The full equation occupies a position in the larger taxonomy of complex-field equations that is not occupied by any of its single-name reductions. This is what is meant in [`01-derivation.md`](01-derivation.md) by the claim that the equation is not in the standard catalog.

The structural argument advanced in this work is that the position the full equation occupies, at the intersection of all of its reductions, is selected by the three structural principles in [`../principles/`](../principles/). Each principle contributes one or two terms; none of the principles is dispensable without breaking the structural claim.

## Special case: the auxiliary fields without the wave equation

If we consider only the auxiliary-field dynamics and ignore the wave equation entirely, the system

$$
\partial_t y_j = \nu_j(\rho - y_j)
$$

with $\rho(t)$ an externally specified input is the Ornstein–Uhlenbeck process driven by $\rho$. In the multi-dimensional case (multiple $j$ with different $\nu_j$), this is precisely the diagonal form of the structured state space model update of S4, Mamba, RWKV, and related architectures (see [`mnsm/interfaces/01-state-space-models.md`](https://github.com/qrv0/mnsm/blob/main/interfaces/01-state-space-models.md)). The reduction from the full equation to the SSM is therefore: keep the auxiliary-field structure, drop the wave equation for $\Psi$ that drives $\rho$, and replace $\rho$ with an externally injected input signal. This is what an SSM is, in the vocabulary of this work: the memory subsystem of the full equation, with the rest stripped away. The reverse direction, extending an SSM with the wave equation that the present equation includes, is what gives the structural extensions detailed in the spinoff repository.
