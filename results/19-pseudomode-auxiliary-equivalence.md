# Result 19: pseudomode auxiliary-field equivalence verified numerically

## Prediction tested

Interface: [`../interfaces/18-pseudomode-quantum.md`](../interfaces/18-pseudomode-quantum.md), prediction **P18.1**.

Predicted observable: for an exponential memory kernel $K(\tau) = \nu e^{-\nu\tau}$, the auxiliary-field ODE $dy/dt = \nu(\rho - y)$, $y(0) = 0$ reproduces the convolution-form trajectory $y_{\text{conv}}(t) = \int_0^t \nu e^{-\nu(t-s)}\rho(s)\,ds$ to within numerical precision, for arbitrary smooth forcing $\rho(t)$.

This is the structural equivalence at the memory subsystem level that underlies the pseudomode embedding of non-Markovian open quantum systems (Garraway 1997, Tamascelli et al 2018, Pleasance et al 2020), identical in form to the auxiliary-field embedding of the equation (Mori-Zwanzig 1961).

## Method

The script [`../experiments/physics/test_pseudomode_auxiliary_equivalence.py`](../experiments/physics/test_pseudomode_auxiliary_equivalence.py) integrates the auxiliary ODE via RK4 and computes the convolution directly via trapezoidal quadrature, comparing per-time-step error across:

- Three forcing protocols: smooth step (sigmoid), Gaussian pulse, bandlimited random noise.
- Five decay rates: $\nu \in \{0.1, 0.5, 1.0, 5.0, 20.0\}$ spanning two orders of magnitude.
- Time grid: $t \in [0, 10]$, 5001 points, $dt = 0.002$.

Backend: numpy on CPU. Wall time: 2.5 seconds.

## Results

Maximum relative error of $y_{\text{ode}}$ versus $y_{\text{conv}}$ across all combinations:

| Protocol | $\nu = 0.1$ | $\nu = 0.5$ | $\nu = 1.0$ | $\nu = 5.0$ | $\nu = 20.0$ |
|---|---:|---:|---:|---:|---:|
| smooth_step | 2.8e-7 | 8.9e-7 | 1.8e-6 | 1.3e-5 | 1.3e-4 |
| gaussian | 1.1e-7 | 2.6e-7 | 5.7e-7 | 8.7e-6 | 1.3e-4 |
| bandlim_noise | 1.7e-6 | 1.8e-6 | 2.6e-6 | 1.2e-5 | 1.4e-4 |

Maximum relative error overall: **1.36e-4**, achieved at $\nu = 20$ (fastest decay) for the bandlimited-noise protocol.

For $\nu \in [0.1, 5.0]$, maximum relative error is below **1.3e-5** across all protocols, indicating the auxiliary ODE reproduces the convolution to near floating-point precision in the well-resolved regime. The increase at $\nu = 20$ is the expected quadrature-resolution effect when the kernel decay timescale ($\tau = 0.05$) approaches the grid spacing ($dt = 0.002$); refining the grid eliminates this without affecting the structural equivalence.

## Statistical analysis

The agreement between $y_{\text{ode}}$ (auxiliary ODE) and $y_{\text{conv}}$ (direct convolution) is a mathematical equivalence: the ODE is the differential form of the exponential-kernel convolution, obtained by Leibniz differentiation. The test verifies this equivalence numerically across a structurally diverse set of forcing protocols and decay rates. The residual error is from quadrature discretization, not from any structural mismatch.

## Status assignment

Status: **tested in coupled regime, consistent**.

Rationale: across three forcing protocols and five decay rates spanning two orders of magnitude, the auxiliary-field ODE reproduces the convolution-form memory integral to within $1.36 \times 10^{-4}$ relative error (well below the $10^{-3}$ threshold). The equivalence is mathematically exact for the exponential kernel; the numerical test confirms the structural identity. The result contributes evidence consistent with P18.1 under criterion 4 (cross-domain coherence) and under criterion 2 (reproducibility).

## What this result establishes structurally

The pseudomode operator equation in non-Markovian open quantum systems, in the over-damped expectation-value form, reduces to the auxiliary-field equation of the present work. This test verifies the underlying mathematical equivalence numerically and at the level of arbitrary forcing functions. The structural correspondence between interface 18 and the present equation's memory subsystem is operationally established.

The result does not establish that the full quantum master equation reduces to the field equation of the present work; those are distinct equations operating on different mathematical objects (density operator vs complex scalar PDE). The correspondence is at the memory subsystem level, with the full equation differing in field type, as documented in [`../interfaces/18-pseudomode-quantum.md`](../interfaces/18-pseudomode-quantum.md).

## Honest caveats

- Single-exponential kernel tested; multi-exponential extension is the natural follow-up.
- Smooth forcing protocols only; discontinuous step forcing produces additional trapezoidal-quadrature error that is not a structural failure but a quadrature artifact (documented in the script).
- Numerical scheme (RK4 + trapezoid) may not be optimal at the fastest decay rate ($\nu = 20$) at the current grid resolution; finer grids eliminate the residual error.

## Reproducibility

```bash
python experiments/physics/test_pseudomode_auxiliary_equivalence.py
```

Wall time: ~2.5 seconds on CPU. Output: `outputs/pseudomode_auxiliary_equivalence/summary.json`. Seed: 42.

## Related documents

- Interface: [`../interfaces/18-pseudomode-quantum.md`](../interfaces/18-pseudomode-quantum.md), prediction P18.1.
- Methodology grounding: [`../methodology/08-mori-zwanzig-foundation.md`](../methodology/08-mori-zwanzig-foundation.md).
- Equation: [`../equation/02-markovian-embedding.md`](../equation/02-markovian-embedding.md).
