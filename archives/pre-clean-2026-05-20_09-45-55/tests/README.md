# Tests

The validation tests for the physics solver. These tests are the basis for the "internal mathematical consistency" criterion of the structural-realist evaluation (see [`../methodology/04-the-six-criteria.md`](../methodology/04-the-six-criteria.md), Criterion 1).

| File | What it tests |
|---|---|
| `test_conservation.py` | Norm conservation in unitary regimes, pure dissipative decay, FDT thermalization, supercritical-collapse signature. |

## Running the tests

```bash
pytest tests/
```

Or invoke the underlying sanity module directly:

```bash
python -m implementation.physics.sanity
```

The full validation runs in approximately one minute on the reference RTX 4060 hardware. The tests use the GPU if CuPy is available; otherwise they fall back to NumPy on CPU and run more slowly.

## What the tests verify

The five conservation diagnostics correspond to the five reductions of the equation (see [`../equation/05-reductions.md`](../equation/05-reductions.md)) plus the cross-validation that the anti-collapse mechanism is operating:

1. **Free Schrödinger (norm conservation)**: With $\Lambda = 0$, no memory, no dissipation, no noise, the L²-norm should be conserved to machine precision. The test runs 200 steps of a free Gaussian wavepacket and checks that the norm drift is below the precision-mode tolerance ($10^{-13}$ for fp64, $10^{-6}$ for fp32).

2. **Pure dissipation**: With $\gamma_0 > 0$, no noise, no nonlinearity, the L²-norm should decay as $e^{-2\gamma_0 t}$. The test compares the numerical decay to the analytical prediction; relative error below $10^{-3}$ is the pass criterion.

3. **Sub-critical attractive NLS**: With $\Lambda < 0$ but below the collapse threshold, the field should disperse without collapse. The test verifies that the peak density stays bounded throughout the integration.

4. **Supercritical attractive NLS without memory**: With $\Lambda$ in the supercritical range, the bare equation should collapse to lattice scale. The test verifies that the peak density grows above the initial value.

5. **Supercritical attractive NLS with memory**: With $\Lambda$ in the supercritical range and the memory potential active, the field should release after the initial spike. The test verifies that the final-to-maximum peak ratio is small.

6. **FDT thermalization**: With $\Lambda = 0$, $\gamma_0 > 0$, $T > 0$, the field should thermalize to the equipartition value $\langle |\Psi|^2 \rangle = 2T$ per cell. The test checks the late-time mean density and confirms plateau behavior.

## Tolerances

The tolerances are documented in `implementation/physics/precision.py`. For the reference fp32 mode:

- Norm conservation: $10^{-6}$ over hundreds of steps.
- Dissipative decay: $10^{-3}$ relative error vs. analytical.
- FDT thermalization: 0.5% deviation from equipartition.

The fp64 mode achieves $10^{-13}$ on norm conservation and 6-significant-figure agreement on dissipative decay; this is the standard for validation runs.

## What passing tests establish

The validation tests establish that the solver implements the equation correctly across the regimes covered by the reductions. They do not, by themselves, establish that the equation is correct for any specific physical system. The relationship between the equation and physical reality is the subject of the cross-domain interfaces in [`../interfaces/`](../interfaces/).
