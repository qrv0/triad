# Implementation

This folder contains the code that integrates the equation. It is divided into two subpackages, reflecting the dual nature of the work documented in [`../interfaces/06-state-space-models.md`](../interfaces/06-state-space-models.md): the physics solver and the neural sequence layer use mathematically equivalent auxiliary-field dynamics but operate in different computational regimes.

| Subpackage | What it does |
|---|---|
| [`physics/`](physics/) | CuPy-based GPU solver for the field equation. Reproduces the paper's physics results. |
| [`neural/`](neural/) | PyTorch reference implementation of the equation as a neural sequence layer. Currently a skeleton; benchmark work pending. |
| [`shared/`](shared/) | Code shared between the physics and neural implementations (none required at present). |

## Mathematical equivalence between the two implementations

The auxiliary-field equation $\partial_t y_j = \nu_j(\rho - y_j)$ governs both implementations. In the physics solver, $\rho = |\Psi|^2$ is the local density of the wave equation field at each lattice point. In the neural layer, $\rho$ is the input signal to a hidden state $y_j$, where the hidden state evolution is a structured state space model update. The math is the same; the substrate differs.

The state space model correspondence is what allows the same auxiliary-field code, with different driver $\rho$, to function in both contexts. This is the mathematical content of [`../interfaces/06-state-space-models.md`](../interfaces/06-state-space-models.md).

## What runs and what doesn't

The physics solver is complete, validated, and produces the results documented in [`../results/`](../results/). It runs on NVIDIA GPUs via CuPy (CUDA 11 or 12) and falls back to NumPy on CPU for testing. The validation suite is in [`../tests/`](../tests/).

The neural layer is a reference implementation, intended to demonstrate the architectural translation. It has not been benchmarked against standard sequence-modeling baselines (S4, Mamba, RWKV, Transformer). The benchmark work is the natural next direction and is outlined in [`neural/README.md`](neural/README.md).

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
