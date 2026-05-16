# Markovian embedding of the integral memory potential

The integral memory potential introduced by P2 is, in its general form, computationally intractable. This document derives the reduction that makes it tractable: the projection of the convolution onto a finite set of auxiliary fields that evolve by local ordinary differential equations.

## The intractable form

The integral memory potential, in its general form, is:

$$
V_{\text{mem}}(t, \mathbf{x}) = \int_0^t dt' \int d^n x'\, \hat{U}(t - t', \mathbf{x}, \mathbf{x}')\, \rho(t', \mathbf{x}')
$$

where $\rho = |\Psi|^2$ is the field density and $\hat{U}$ is a general memory kernel. Direct evaluation requires storing the full history of $\rho$ at every spatial point, then performing a convolution integral at every time step. Memory cost scales as $O(N_x N_t)$ where $N_x$ is the number of spatial grid points and $N_t$ is the number of time steps in the history; computational cost per step scales as $O(N_x N_t)$ for the convolution and $O(N_x^2 N_t)$ for spatially non-local kernels. Both are prohibitive beyond very small systems and short integration times.

## The factorization that admits embedding

Assume the kernel factors into a temporal part and a spatial part:

$$
\hat{U}(\tau, \mathbf{x}, \mathbf{x}') = U_t(\tau)\, U_x(\mathbf{x} - \mathbf{x}').
$$

For the temporal part, assume a multi-exponential form:

$$
U_t(\tau) = \sum_{j=1}^N \lambda_j \nu_j e^{-\nu_j \tau}.
$$

For the spatial part, assume locality (delta-function kernel):

$$
U_x(\mathbf{x} - \mathbf{x}') = \delta^{(n)}(\mathbf{x} - \mathbf{x}').
$$

Under these assumptions, the integral memory potential becomes:

$$
V_{\text{mem}}(t, \mathbf{x}) = \sum_{j=1}^N \lambda_j \nu_j \int_0^t dt' e^{-\nu_j(t - t')}\, \rho(t', \mathbf{x}).
$$

The spatial integral has collapsed because of the delta function. The temporal integral is now a sum of single-exponential convolutions, one for each mode $j$.

## The auxiliary-field reduction

Define, for each mode $j$, an auxiliary field:

$$
y_j(t, \mathbf{x}) = \nu_j \int_0^t dt' e^{-\nu_j(t - t')}\, \rho(t', \mathbf{x}).
$$

The total memory potential is then a finite sum:

$$
V_{\text{mem}}(t, \mathbf{x}) = \sum_{j=1}^N \lambda_j y_j(t, \mathbf{x}).
$$

The auxiliary field $y_j(t, \mathbf{x})$ satisfies a first-order linear ordinary differential equation in time at each spatial point, obtained by differentiating the integral expression and using the fundamental theorem of calculus:

$$
\partial_t y_j = \nu_j (\rho - y_j).
$$

This is the central reduction. The integro-differential equation for $\Psi$ coupled to its full history has been replaced by a system of local ordinary differential equations: $\Psi$ evolves under the equation of [`01-derivation.md`](01-derivation.md), and each auxiliary field $y_j$ evolves under its own local first-order equation, driven by the instantaneous density $\rho$.

The memory cost is now $O(N_x \cdot N)$ where $N$ is the number of memory modes. Typical values are $N = 1$ or $N = 2$. The computational cost per time step is reduced to $O(N_x \cdot N)$ for the auxiliary-field updates plus the cost of the field equation itself, both of which are independent of $N_t$. The non-Markovian character of the original equation is preserved — the auxiliary fields encode the memory — but the implementation is now local in time and computationally feasible.

## Derivation of the local ODE

Starting from the integral definition:

$$
y_j(t, \mathbf{x}) = \nu_j \int_0^t dt' e^{-\nu_j(t - t')}\, \rho(t', \mathbf{x}).
$$

Differentiating with respect to $t$, using Leibniz's rule:

$$
\partial_t y_j = \nu_j \rho(t, \mathbf{x}) + \nu_j \int_0^t dt' \frac{\partial}{\partial t}\left[ e^{-\nu_j(t - t')} \right] \rho(t', \mathbf{x}).
$$

The partial derivative of the exponential is:

$$
\frac{\partial}{\partial t} e^{-\nu_j(t - t')} = -\nu_j e^{-\nu_j(t - t')}.
$$

Substituting:

$$
\partial_t y_j = \nu_j \rho(t, \mathbf{x}) - \nu_j \cdot \nu_j \int_0^t dt' e^{-\nu_j(t - t')}\, \rho(t', \mathbf{x}) = \nu_j \rho(t, \mathbf{x}) - \nu_j y_j(t, \mathbf{x}).
$$

Factoring $\nu_j$:

$$
\boxed{\;\partial_t y_j = \nu_j(\rho - y_j)\;}.
$$

This is the canonical Ornstein–Uhlenbeck equation, driven by the field density $\rho$ rather than by noise.

## Interpretation of the auxiliary fields

Each auxiliary field $y_j$ is a memory reservoir. At any moment $t$, $y_j(t, \mathbf{x})$ stores a weighted integral of past values of $\rho$ at the same spatial point $\mathbf{x}$. The weighting is exponential with decay rate $\nu_j$. The relaxation time of the reservoir is $\tau_j = 1/\nu_j$.

A fast reservoir ($\nu_j \gg 1$, $\tau_j \ll 1$) tracks $\rho$ closely: in the limit $\nu_j \to \infty$, $y_j \to \rho$ instantaneously, and the memory becomes effectively local in time. A slow reservoir ($\nu_j \ll 1$, $\tau_j \gg 1$) responds slowly: it averages $\rho$ over a long window and is largely insensitive to brief fluctuations.

The choice of $N$ and the spectrum $\{\nu_j, \lambda_j\}$ determines the temporal structure of the memory. A single fast mode gives short-time memory; a single slow mode gives long-time memory; two modes (one fast, one slow) give a hierarchical memory that responds to both transient fluctuations and sustained changes.

## Connection to the Mori–Zwanzig formalism

The Markovian embedding derived here is a special case of the Mori–Zwanzig projection-operator method (Mori 1965; Zwanzig 1961) used in statistical mechanics to reduce systems with many degrees of freedom to systems with few. In the Mori–Zwanzig framework, the elimination of "fast" degrees of freedom produces an integro-differential equation for the "slow" ones with a memory kernel encoding the eliminated dynamics. When the eliminated dynamics has a multi-exponential autocorrelation structure, the memory kernel has the multi-exponential form assumed above, and the resulting integro-differential equation admits the auxiliary-field reduction.

The connection is not merely formal. The multi-exponential kernel is the most general kernel that admits exact Markovian embedding via a finite number of auxiliary fields. Other kernel forms — power laws, stretched exponentials, fractional derivatives — do not admit finite-dimensional embedding and require fundamentally different computational strategies.

## Numerical update of the auxiliary fields

In the numerical implementation, the auxiliary-field update is computed exactly per time step using the analytical solution to the OU equation:

$$
y_j(t + dt) = e^{-\nu_j dt}\, y_j(t) + (1 - e^{-\nu_j dt})\, \rho(t).
$$

This update is exact for constant $\rho$ over the time step; for the slowly varying $\rho$ that arises in the operator-split scheme used by the solver, the resulting error is part of the splitting error and is $O(dt^2)$ for the Strang-symmetric scheme. The update is unconditionally stable for any $dt$ because $0 < e^{-\nu_j dt} < 1$ for all $\nu_j > 0$ and $dt > 0$. This is why the auxiliary-field substep is the cheapest part of the numerical integration.

## Connection to state space models

The auxiliary-field equation $\partial_t y_j = \nu_j(\rho - y_j)$ is the diagonal form of the structured state space model update used in S4, S5, Mamba, and RWKV. See [`../interfaces/06-state-space-models.md`](../interfaces/06-state-space-models.md) for the term-by-term correspondence.
