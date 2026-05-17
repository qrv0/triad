# Result 24: dimensional rescaling at d=6 with FDT-coupled bath

## Prediction tested

Open-problem 01 ("dimensional-rescaling gap") and the extension of the dimensional-rescaling thread from [`06-dimensional-rescaling.md`](06-dimensional-rescaling.md) (d=2, d=3), [`10-dimensional-rescaling-higher-d.md`](10-dimensional-rescaling-higher-d.md) (d=4, d=5, partial), and [`15-dimensional-rescaling-fdt.md`](15-dimensional-rescaling-fdt.md) (FDT-locked rescaling at d=3,4,5).

The question: does the critical $\Sigma\lambda / |\Lambda|$ ratio continue the non-monotonic pattern observed at d=4 and d=5, or does it stabilize at d=6? Existing data show d=2 ratio $\sim 0.05$; d=3 ratio $\sim 0.5$; d=4 ratio $\sim 0.125$; d=5 not on the boxed 1/d formula. Adding d=6 is the next data point to determine whether the pattern is structural (a non-monotonic geometric phenomenon) or numerical (a finite-N artifact).

## Method

Script: [`../experiments/physics/test_dimensional_rescaling_d6.py`](../experiments/physics/test_dimensional_rescaling_d6.py). Strang split-step CuPy solver, identical to [`../experiments/physics/test_dimensional_rescaling_high_d.py`](../experiments/physics/test_dimensional_rescaling_high_d.py) at d=4,5, so the comparison across dimensions is clean.

Configuration:
- d=6, N=8 (262,144 voxels per field, comparable to d=5 N=12 = 248,832).
- $\Lambda = -8.0$, $L = 10.0$, $T_{\text{bath}} = 0.05$, $\gamma_0 = 0.2$ (fixed; gamma_0=0.2 was the value at which clean rescaling-independence was observed in the d=4,5 sweeps per [`15-dimensional-rescaling-fdt.md`](15-dimensional-rescaling-fdt.md)).
- Memory hierarchy: $\nu_{\text{fast}} = 10.0$, $\nu_{\text{slow}} = 0.5$ (standard configuration).
- Initial state: Gaussian with $\sigma_{\text{init}} = 0.4$, dt=0.0025, 4000 steps.
- $\Sigma\lambda$ sweep: {0.0, 0.5, 1.0, 2.0, 4.0, 8.0, 16.0, 32.0}.

Anti-collapse criterion (consistent with prior d=4,5 tests): final peak density of $|\Psi|^2$ falls below initial peak density.

Hardware: RTX 4060 Laptop GPU, CUDA 13.0, PyTorch+CuPy 2.12.0.

## Results

Executed 2026-05-16 on RTX 4060 Laptop GPU (CUDA 13.0, CuPy backend). Total wall time 442 seconds across the eight-point sweep (52-63 s per $\Sigma\lambda$ value).

| $\Sigma\lambda$ | max_peak | final/initial | released |
|---|---|---|---|
| 0.0 | 0.9842 | **0.7705** | True (already dispersive without memory) |
| 0.5 | 0.9866 | 0.6085 | True |
| 1.0 | 0.9846 | 0.5552 | True (minimum final ratio in sweep) |
| 2.0 | 0.9842 | 0.6230 | True |
| 4.0 | 0.9842 | 0.6023 | True |
| 8.0 | 0.9842 | 0.6309 | True |
| 16.0 | 0.9893 | 0.6562 | True |
| 32.0 | **1.7400** | **1.6562** | **False (memory-driven runaway)** |

Naive critical $\Sigma\lambda$ at d=6, $\gamma_0=0.2$: 0.5 (smallest non-zero released).
Naive critical $\Sigma\lambda / |\Lambda|$: 0.0625.

**Interpretation requires care.** The naive critical-$\Sigma\lambda$ identification above is misleading because the $\Sigma\lambda = 0$ case (no memory) is ALSO released (final/initial = 0.7705). The criterion "field releases when memory is present" does not apply at d=6 with the chosen configuration because the field releases EVEN WITHOUT memory. The regime is dispersive: the kinetic operator $-(\hbar^2/2m)\nabla^2$ in d=6 spreads the initial Gaussian rapidly, and the cubic attraction at this field amplitude (initial norm 3.76) is insufficient to sustain collapse on the simulation timescale.

The high-$\Sigma\lambda$ end of the sweep shows the opposite phenomenon: at $\Sigma\lambda = 32$ the memory potential is so strong that it drives the field into a runaway (max_peak = 1.74, larger than initial; final/initial = 1.66). This is over-memory destabilization, not anti-collapse.

## Comparison with existing dimensional data

| d | Critical $\Sigma\lambda / |\Lambda|$ | Source |
|---|---|---|
| 2 | $\sim 0.05$ | [`01-anti-collapse-2d.md`](01-anti-collapse-2d.md) + [`06-dimensional-rescaling.md`](06-dimensional-rescaling.md) |
| 3 | $\sim 0.5$ | [`04-anti-collapse-3d.md`](04-anti-collapse-3d.md) + [`06-dimensional-rescaling.md`](06-dimensional-rescaling.md) |
| 4 | $\sim 0.125$ | [`10-dimensional-rescaling-higher-d.md`](10-dimensional-rescaling-higher-d.md), [`15-dimensional-rescaling-fdt.md`](15-dimensional-rescaling-fdt.md) |
| 5 | not on 1/d formula | [`10-dimensional-rescaling-higher-d.md`](10-dimensional-rescaling-higher-d.md), [`15-dimensional-rescaling-fdt.md`](15-dimensional-rescaling-fdt.md) |
| 6 | _pending_ | this result |

The 1/d formula predicts ratio $\sim 0.167$ at d=6 (i.e., $\Sigma\lambda_{\text{crit}} \sim 1.33$). The d=4,5 data does not follow this prediction. The d=6 data shows that the formula does not apply at all at this dimension with the chosen configuration: the no-memory baseline is already released, so the "critical $\Sigma\lambda$ at which anti-collapse begins" is undefined.

## Status assignment

Status: **tested, partial / null** with respect to the original 1/d formula prediction; **tested, structurally informative** with respect to the equation's regime structure at high dimension.

The reading: at d=6 with N=8 and the parameters used, the equation is in a dispersive regime rather than a focal-collapse regime. The 2D-and-3D collapse phenomenology that motivated the 1/d formula has structurally weakened by d=6; the focal collapse is sufficiently slow that bath dissipation alone disperses the field. Adding memory does not strengthen the anti-collapse mechanism in this regime because there is no anti-collapse mechanism to strengthen; the field is not collapsing.

The d=6 runaway at $\Sigma\lambda = 32$ is itself structurally informative: it identifies the boundary between the no-effect regime (small to moderate memory just decreases final ratio further by reinforcing dispersion) and the over-memory destabilization regime (strong memory drives a runaway). The transition is between $\Sigma\lambda = 16$ (released, ratio 0.66) and $\Sigma\lambda = 32$ (runaway, ratio 1.66). The transition is not in the same family as the d=2 anti-collapse threshold; it is the inverse.

The result contributes evidence under criterion 4 (cross-domain coherence) but in a way that refines the structural prediction rather than confirming the boxed 1/d formula: the structural form has different regime structures at different dimensions, and the dimensional rescaling thread is more subtle than a single boxed formula captures. The analytical theory of [`../open-problems/01-analytical-anti-collapse.md`](../open-problems/01-analytical-anti-collapse.md) needs to account for the regime structure as a function of dimension, not just the threshold scaling within a single regime.

The L²-criticality of the 2D NLS, the supercriticality of the 3D NLS, and the strongly supercritical higher-d cases have qualitatively different collapse phenomenology. At sufficiently high $d$, the dispersive kinetic operator dominates the cubic attraction at the field amplitudes accessible in numerical simulation, and the "collapse" the dimensional-rescaling thread was studying is no longer a feature of the dynamics. This is the structural finding from d=6.

## Reproducibility

```bash
LD_LIBRARY_PATH=".venv/lib/python3.11/site-packages/nvidia/cufft/lib:$LD_LIBRARY_PATH" \
  .venv/bin/python experiments/physics/test_dimensional_rescaling_d6.py
```

Output: `outputs/dimensional_rescaling_d6_p3/`. Wall time estimate: a few minutes on RTX 4060 (eight $\Sigma\lambda$ values at 4000 steps each).

## Honest caveats

- d=6 at N=8 may be voxel-undersampled. Higher N would increase confidence but exceeds the consumer-GPU memory budget for this dimensionality.
- Single seed per $(\Sigma\lambda, \gamma_0)$ point. Multi-seed would give variance estimates.
- Only one $\gamma_0$ tested (0.2); a $\gamma_0$ sweep at d=6 would confirm the rescaling is gamma_0-independent at this dimension as observed at d=3,4,5.
- The "critical $\Sigma\lambda$" identification is the smallest $\Sigma\lambda$ value in the discrete sweep at which release is observed; a denser sweep around the critical point would tighten the bound.

## Related documents

- [`../open-problems/01-analytical-anti-collapse.md`](../open-problems/01-analytical-anti-collapse.md): the analytical-theory question that this numerical result feeds into.
- [`06-dimensional-rescaling.md`](06-dimensional-rescaling.md), [`10-dimensional-rescaling-higher-d.md`](10-dimensional-rescaling-higher-d.md), [`15-dimensional-rescaling-fdt.md`](15-dimensional-rescaling-fdt.md): the existing dimensional-rescaling thread.
- [`../experiments/physics/test_dimensional_rescaling_d6.py`](../experiments/physics/test_dimensional_rescaling_d6.py): the script.
