# Spontaneous crystallization

## What is observed

When the two-dimensional equation is integrated at $\Lambda = -8$ with memory coupling at $(\nu, \lambda) = (10, 1)$, starting from an unstructured Gaussian initial state, the field does not disperse uniformly after the initial collapse-and-release transient. Instead, it organizes into a stationary periodic spatial pattern: a two-dimensional lattice of high-density spots that tile the box.

## The dominant wavenumber

Fourier analysis of the late-time density profile yields a sharp peak in the radial power spectrum at:

$$
k^* \approx 2.13 \text{ in lattice units}
$$

corresponding to an intrinsic spatial wavelength:

$$
\lambda_{\text{wave}} = \frac{2\pi}{k^*} \approx 2.95 \text{ in lattice units}.
$$

This is a definite quantity, not a parameter of the equation. The equation has $\Lambda$, $\nu$, $\lambda$, and the lattice $L/N$ as inputs; none of these specifies $k^* = 2.13$ directly. The wavenumber emerges from the dynamics.

## Mesh independence

The wavenumber $k^*$ is invariant under mesh refinement. The same value is obtained at $N = 256$ and at $N = 512$ on a box of the same physical size. This rules out interpretations of $k^*$ as a lattice artefact.

## Parameter independence within the crystalline regime

The wavenumber $k^*$ is approximately invariant across an interior region of $(\Lambda, \lambda)$ parameter space. Within the regime where the field is released from collapse and forms a recognizable crystalline pattern (roughly $\Lambda \in [-12, -6]$ and $\lambda$ such that $\Sigma\lambda$ is in the right range for the dimensional regime), the same $k^* \approx 2.13$ is recovered. The wavenumber is not the result of tuning; it is the result of the equation selecting the most unstable mode of its modulational instability about the unperturbed uniform state.

## The modulational instability

The mechanism is the standard modulational instability of the attractive nonlinear Schrödinger equation under perturbation. The unperturbed uniform state $\Psi_0 = \sqrt{\rho_0} e^{-i\Lambda \rho_0 t/\hbar}$ is linearly unstable to perturbations at finite wavenumber; the growth rate as a function of perturbation wavenumber peaks at a specific wavenumber that depends on $\Lambda$, the density $\rho_0$, and the kinetic dispersion. The memory potential modifies the growth-rate dispersion relation in a way that selects a specific $k^*$ as the dominant unstable mode, and this $k^*$ is what is observed in the late-time pattern.

The structural feature is that the equation selects a specific scale from a featureless initial state. The initial Gaussian has support across all wavenumbers; the late-time crystalline state has support concentrated at $k^*$. This is a clear instance of dynamical symmetry breaking and scale selection.

## Numerical specification

| Parameter | Value |
|---|---|
| Lattice | $256 \times 256$ (refined to $512 \times 512$ for convergence) |
| Box length | $L = 20$ |
| Time step | $dt = 0.0025$ |
| Integration | 4000 steps |
| Initial state | Gaussian, $\sigma_0 = 1.2$, $\mathbf{k}_0 = (1.0, 0.5)$ |
| Nonlinearity | $\Lambda = -8$ |
| Memory | $(\nu, \lambda) = (10, 1)$, single mode, larger coupling than the anti-collapse regime |
| Conservative regime | $\gamma_0 = 0$, $T = 0$ |
| Precision | fp64 |

Note that the crystalline regime uses a larger memory coupling than the anti-collapse demo: $\lambda = 1$ here versus $\Sigma\lambda = 0.4$ in [`01-anti-collapse-2d.md`](01-anti-collapse-2d.md). The phase landscape of $(\Lambda, \lambda)$ contains distinct regimes for different qualitative behaviors.

## Reproduction

```bash
python experiments/physics/reproduce_2d_crystallization.py
```

Expected wall time: ~4 minutes on RTX 4060. Output: late-time density snapshot, radial power spectrum, time series of the FWHM.

## What this result is not

This is not an FFT artefact. The Fourier analysis is performed on the real-space density field, and the peak at $k^* = 2.13$ corresponds to a real spatial periodicity visible in the density snapshot. The crystalline pattern is observable directly without reference to spectral analysis.

This is not a special feature of the initial condition. The crystallization is robust to varying $\sigma_0$, $\mathbf{k}_0$, and the random seed (in the noisy version of the equation). The pattern emerges from any initial state that delivers the system into the crystalline regime of the parameter space.

This is not a transient. The crystalline state is stationary on average over the available integration window. Individual lattice points oscillate in time (see [`03-vibrational-modes.md`](03-vibrational-modes.md)), but the spatial pattern itself is preserved.

## Structural significance

Spontaneous scale selection from a featureless input is one of the canonical signatures of pattern-forming dynamical systems. The classical reference cases include Bénard convection, the Faraday instability, Turing reaction-diffusion patterns, and Chladni cymatic geometry. The present equation places the Triad equation in this family of pattern-forming systems with a definite intrinsic wavelength. See [`../interfaces/03-chladni-cymatics.md`](../interfaces/03-chladni-cymatics.md) for the explicit cross-domain mapping.
