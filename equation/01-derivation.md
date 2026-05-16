# Derivation of the equation from the three principles

This document traces the path from the structural axioms in [`../principles/`](../principles/) to the full equation. Each principle is responsible for a specific structural term; the combination of terms is the equation.

## From P1 — the kinetic generator

[P1](../principles/01-oscillation.md) requires a complex field with a norm-preserving generator. The most economical such generator on a flat continuum is the negative Laplacian:

$$
\hat{H}_{\text{kin}} = -\frac{\hbar^2}{2m}\nabla^2.
$$

For systems that exhibit anomalous transport — sub-diffusive or super-diffusive propagation deviating from Gaussian — a fractional generalization is admitted:

$$
\hat{H}_{\text{frac}} = \alpha\, (-\Delta)^{\sigma/2}, \qquad \sigma \in (1, 2].
$$

The fractional Laplacian reduces to the standard Laplacian for $\sigma = 2$. For internal degrees of freedom such as spin or polarization, the field generalizes to a two-component spinor and the Hamiltonian acquires Pauli-matrix structure:

$$
H(\mathbf{k}) = a(\mathbf{k})\mathbb{1} + n_x(\mathbf{k})\sigma_x + n_y(\mathbf{k})\sigma_y + n_z(\mathbf{k})\sigma_z,
$$

with $a(\mathbf{k}) = \tfrac{\hbar^2 k^2}{2m} + \alpha|\mathbf{k}|^\sigma - i\gamma_0$ collecting the scalar dispersion and the homogeneous part of the dissipation, $n_x = -\alpha_R k_y$ and $n_y = \alpha_R k_x$ encoding Rashba spin–orbit coupling, and $n_z = -i\gamma_s(\mathbf{k})$ a momentum-dependent dissipative term. The propagator over a time step admits a closed form via the Pauli identity:

$$
U(\mathbf{k}) = e^{-iH(\mathbf{k})\,dt} = e^{-ia\,dt}\!\left[\cos(\omega\,dt)\mathbb{1} - i\frac{\sin(\omega\,dt)}{\omega}\bigl(n_x \sigma_x + n_y \sigma_y + n_z \sigma_z\bigr)\right],
$$

where $\omega^2 = n_x^2 + n_y^2 + n_z^2$. This form remains exact when $\omega$ is complex, as it is when $\gamma_s \neq 0$. The closed form makes the kinetic step of the numerical solver an algebraic pointwise operation in momentum space, which is what permits the Strang split-step scheme described in [`../implementation/physics/README.md`](../implementation/physics/README.md).

When the gauge potential $\hat{A}$ is included, the spatial derivative is promoted to the gauge-covariant derivative $D = \nabla - iq\hat{A}/\hbar$. In the absence of external gauge fields, $\hat{A} = 0$ and $D = \nabla$.

## From P2 — local nonlinearity and integral memory

[P2](../principles/02-self-reference.md) has two parts.

The instantaneous part contributes the cubic Gross–Pitaevskii term:

$$
\Lambda |\Psi|^2 \Psi
$$

with $\Lambda$ controlling both the strength and the sign of the self-interaction. The cubic form is the lowest-order nonlinearity consistent with the gauge invariance of the underlying complex field. Higher-order terms are admissible but not required by P2.

The across-time part contributes the integral memory potential:

$$
V_{\text{mem}}(t, \mathbf{x}) = \int_0^t dt' \int d^n x'\, \hat{U}(t - t', \mathbf{x}, \mathbf{x}')\, |\Psi(t', \mathbf{x}')|^2.
$$

For a kernel that factors as a sum of decaying exponentials in time and a delta function in space,

$$
\hat{U}(\tau, \mathbf{x}, \mathbf{x}') = \sum_{j=1}^N \lambda_j \nu_j e^{-\nu_j \tau}\, \delta^{(n)}(\mathbf{x} - \mathbf{x}'),
$$

this convolution reduces exactly to a system of local ordinary differential equations via the Markovian embedding derived in [`02-markovian-embedding.md`](02-markovian-embedding.md). The auxiliary fields $y_j$ defined by $\partial_t y_j = \nu_j(\rho - y_j)$ are the memory reservoirs, each with its own relaxation time $\tau_j = 1/\nu_j$ and coupling strength $\lambda_j$. The total memory potential is

$$
V_{\text{mem}}(t, \mathbf{x}) = \sum_{j=1}^N \lambda_j y_j(t, \mathbf{x}).
$$

## From P3 — dissipation and fluctuation-dissipation-locked noise

[P3](../principles/03-coupling.md) contributes the linear dissipation term

$$
-i\Gamma \Psi
$$

with $\Gamma \ge 0$ removing amplitude at a rate controlled by $\Gamma$. P3 simultaneously requires a compensating stochastic forcing term $\eta(t, \mathbf{x})$ whose correlator is locked to $\Gamma$ by the classical fluctuation–dissipation theorem:

$$
\langle \eta(t, \mathbf{x}) \eta^*(t', \mathbf{x}') \rangle = 2\gamma_0 k_B T\, \delta(t - t')\, \delta^{(n)}(\mathbf{x} - \mathbf{x}').
$$

Without this lock, the equation either decays toward vacuum (dissipation without compensation) or heats without bound (noise without dissipation). With the lock, the field thermalizes to a stationary distribution whose temperature is set by the bath.

## The combined equation

Combining the three contributions:

$$
\boxed{\;
i\hbar\, \partial_t \Psi = \left[\,-\frac{\hbar^2}{2m} D^2 + V_{\text{ext}} + \Lambda |\Psi|^2 + V_{\text{mem}} + \alpha (-\Delta)^{\sigma/2} - i\Gamma\,\right]\Psi + \eta\;
}
$$

with $V_{\text{mem}} = \sum_j \lambda_j y_j$, $\partial_t y_j = \nu_j(\rho - y_j)$, and $\eta$ satisfying the FDT correlator. An optional external potential $V_{\text{ext}}$ admits the introduction of trap geometries or external drives.

## What the equation is and is not

The equation is a single composite field equation. Each term is forced by one of the principles. The structural claim of the work is that the combination of principles admits no degrees of freedom in the form of the equation up to choices of coupling constants and choices of kernel form within the constraints stated.

The equation is not derived from a more fundamental theory. It is derived from structural axioms about the behavior of persistent extended entities. The relationship of the equation to fundamental physics — quantum field theory, statistical mechanics, general relativity — is established case by case via the reductions in [`05-reductions.md`](05-reductions.md), each of which corresponds to a regime where the equation reduces to a known established equation.

The equation does not claim to be the unique correct equation for any specific physical system. The claim is that the equation captures the structural form that several physical systems share, and that the cross-domain co-occurrence of this form is itself the criterion by which the work is evaluated. See [`../methodology/01-structural-realism.md`](../methodology/01-structural-realism.md) for the methodological position.
