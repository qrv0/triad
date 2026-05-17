# Result 20: Prony viscoelastic stress reproduction via auxiliary-variable equation

## Prediction tested

Interface: [`../interfaces/19-viscoelasticity-prony.md`](../interfaces/19-viscoelasticity-prony.md), prediction **P19.1**.

Predicted observable: given a Prony series relaxation modulus $G(t) = G_\infty + \sum_i G_i e^{-t/\tau_i}$, the auxiliary-variable ODE $dq_i/dt + q_i/\tau_i = d\varepsilon^{\text{dev}}/dt$ with stress $\sigma^{\text{dev}} = 2\mu_{\text{tot}}(\mu_0 \varepsilon^{\text{dev}} + \sum_i \mu_i q_i)$ reproduces the hereditary-integral stress response $\sigma_{\text{conv}}(t) = \int_{-\infty}^t G(t-s) \dot\varepsilon(s)\,ds$ under arbitrary strain history.

This is the structural equivalence used industrially in PyLith, COMSOL, Ansys, and Abaqus for finite-element viscoelastic simulation. The test verifies the equivalence numerically with a synthetic 3-term Prony series at polymer scale.

## Method

The script [`../experiments/physics/test_prony_viscoelastic_reproduction.py`](../experiments/physics/test_prony_viscoelastic_reproduction.py) integrates the auxiliary-variable ODE via RK4 and computes the convolution-form stress via trapezoidal quadrature, comparing per-time-step error across three strain protocols.

**Prony series (synthetic, polymer scale):**
- $\tau_i = \{0.1, 1.0, 10.0\}$ seconds
- $G_i = \{3 \times 10^8, 1 \times 10^8, 5 \times 10^7\}$ Pa
- $G_\infty = 10^7$ Pa
- $G_0 = G_\infty + \sum_i G_i = 4.6 \times 10^8$ Pa
- Fractional moduli $\mu_0 = 0.022$, $\mu_i = (0.652, 0.217, 0.109)$

**Strain protocols:**
- smooth_step: sigmoid step from 0 to 0.01 at $t = 1$, width 0.05
- double_pulse: two Gaussian pulses at $t = 2, 6$ with $\sigma = 0.3$, amplitude 0.01
- sinusoidal: $\varepsilon(t) = 0.005\sin(2t)$

Time grid: $t \in [0, 30]$, 6001 points.

Backend: numpy on CPU. Wall time: 2.2 seconds.

## Results

| Protocol | Max relative error | Stress final (ODE) | Stress final (conv) |
|---|---:|---:|---:|
| smooth_step | 2.6e-4 | 1.275e5 Pa | 1.275e5 Pa |
| double_pulse | 9.5e-5 | -5.7e3 Pa | -5.7e3 Pa |
| sinusoidal | 7.2e-5 | -7.085e5 Pa | -7.085e5 Pa |

Maximum relative error overall: **2.62e-4** (smooth_step protocol).

The agreement holds across protocols that exercise distinct memory regimes: the smooth step engages all three Prony modes with rising strain, the double-pulse engages transient memory response with two separated events, and the sinusoidal probes frequency-dependent storage and loss.

## Statistical analysis

The auxiliary-variable ODE is the differential form of the exponential-kernel hereditary integral, by Leibniz differentiation. The mathematical equivalence is exact for the Prony series form; the test verifies that the numerical implementations agree to within trapezoidal-quadrature error. The error magnitude (sub-1e-3) is small enough that the structural identity is operationally established.

## Status assignment

Status: **tested in coupled regime, consistent**.

Rationale: the auxiliary-variable equation reproduces the hereditary-integral stress response across three structurally distinct strain protocols and a 3-term Prony series at polymer scale, to within 2.6e-4 relative error (below the 1e-3 threshold). The result contributes evidence consistent with P19.1 under criterion 4 (cross-domain coherence) and under criterion 2 (reproducibility).

## What this result establishes structurally

The Maxwell-element internal-variable equation used industrially in finite-element viscoelasticity codes (PyLith, COMSOL, Ansys, Abaqus) is mathematically identical to the auxiliary-field equation of the present work. This test confirms the equivalence at synthetic polymer scale with realistic Prony series parameters. The structural correspondence between interface 19 and the equation's memory subsystem is operationally established.

The result does not establish that the full continuum-mechanics stress-strain equations reduce to the field equation of the present work; the substrate-level constitutive structure (stress tensor field in viscoelasticity vs complex scalar PDE in the equation) differs. The correspondence is at the memory subsystem level, as documented in [`../interfaces/19-viscoelasticity-prony.md`](../interfaces/19-viscoelasticity-prony.md).

## Honest caveats

- Synthetic Prony series rather than measured creep modulus from a specific polymer. The next step would fit Prony coefficients to published PMMA or PDMS relaxation data and verify reproduction against the original measurement.
- 3-term series; higher-rank fits would test the prediction P19.2 (Prony rank vs decade range) separately.
- Linear viscoelasticity regime; nonlinear extensions (Mooney-Rivlin, finite-strain) are open follow-up.

## Reproducibility

```bash
python experiments/physics/test_prony_viscoelastic_reproduction.py
```

Wall time: ~2.2 seconds on CPU. Output: `outputs/prony_viscoelastic_reproduction/summary.json`. Seed: 42.

## Related documents

- Interface: [`../interfaces/19-viscoelasticity-prony.md`](../interfaces/19-viscoelasticity-prony.md), prediction P19.1.
- Methodology grounding: [`../methodology/08-mori-zwanzig-foundation.md`](../methodology/08-mori-zwanzig-foundation.md).
- Equation: [`../equation/02-markovian-embedding.md`](../equation/02-markovian-embedding.md).
