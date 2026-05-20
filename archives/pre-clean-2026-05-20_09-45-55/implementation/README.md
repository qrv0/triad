# Implementation

This folder contains the physics solver for the field equation. The neural sequence layer (PyTorch instantiation of the auxiliary-field equation) was migrated on 2026-05-17 to the [`mnsm`](https://github.com/qrv0/mnsm) spinoff repository, where the ML implementation depth lives. The two implementations are mathematically equivalent at the level of the auxiliary-field dynamics, in different computational substrates.

| Subpackage | What it does |
|---|---|
| [`physics/`](physics/) | CuPy-based GPU solver for the field equation. Reproduces the paper's physics results. |
| [`shared/`](shared/) | Code shared between the physics implementation and any external substrate-specific implementations (none required at present). |

## Mathematical equivalence with the ML instantiation

The auxiliary-field equation $\partial_t y_j = \nu_j(\rho - y_j)$ governs both substrates. In the physics solver here, $\rho = |\Psi|^2$ is the local density of the wave equation field at each lattice point. In the ML instantiation in `mnsm`, $\rho$ is the input signal to a hidden state $y_j$, where the hidden state evolution is a structured state space model update. The math is the same; the substrate differs.

The structural mapping is documented in the SSM interface, which now lives at [`mnsm/interfaces/01-state-space-models.md`](https://github.com/qrv0/mnsm/blob/main/interfaces/01-state-space-models.md). The empirical instance of the cross-substrate equivalence at 70M parameters is at [`mnsm/results/01-optimization-collapse-empirical.md`](https://github.com/qrv0/mnsm/blob/main/results/01-optimization-collapse-empirical.md).

## What runs

The physics solver is complete, validated, and produces the results documented in [`../results/`](../results/). It runs on NVIDIA GPUs via CuPy (CUDA 11 or 12) and falls back to NumPy on CPU for testing. The validation suite is in [`../tests/`](../tests/).

## Status of the test suite

The conservation tests in [`../tests/`](../tests/) cover:

- Norm conservation in unitary regimes (target: drift $< 10^{-13}$ in fp64).
- Pure dissipative decay matching the analytical exponential.
- FDT thermalization to the equipartition equilibrium.
- Bravais-detector behavior on known synthetic crystals.

The full validation runs in approximately one minute on the reference RTX 4060 hardware.

## Hardware requirements

- **Recommended:** NVIDIA GPU with CUDA 11 or 12, 4 GB VRAM minimum, 8 GB for production runs at $128^3$ lattice.
- **Minimum:** any system with NumPy 1.24+. The CPU fallback works for the playground notebooks and for the validation suite but is too slow for production research runs.
- **Memory:** the physics solver at $128^3$ fp32 uses approximately 100 MB VRAM per simulation; multiple simulations can be batched within an 8 GB card.

## Reproducibility

All random seeds in the physics solver are fixed in the configuration; runs reproduce bit-for-bit on identical hardware. Cross-hardware reproduction at the level of floating-point rounding may differ; qualitative results (orders of magnitude separations, Bravais selection, frequency ratios) are preserved across hardware.
