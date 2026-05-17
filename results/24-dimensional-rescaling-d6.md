# Result 24: dimensional rescaling at d=6 with P3 active

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

Executed 2026-05-16. Results to be populated from `outputs/dimensional_rescaling_d6_p3/summary.json` once the GPU run completes.

| $\Sigma\lambda$ | max_peak | final/initial | released |
|---|---|---|---|
| 0.0 | _pending_ | _pending_ | _pending_ |
| 0.5 | _pending_ | _pending_ | _pending_ |
| 1.0 | _pending_ | _pending_ | _pending_ |
| 2.0 | _pending_ | _pending_ | _pending_ |
| 4.0 | _pending_ | _pending_ | _pending_ |
| 8.0 | _pending_ | _pending_ | _pending_ |
| 16.0 | _pending_ | _pending_ | _pending_ |
| 32.0 | _pending_ | _pending_ | _pending_ |

Critical $\Sigma\lambda$ at d=6, $\gamma_0=0.2$: _pending_.
Critical $\Sigma\lambda / |\Lambda|$: _pending_.

## Comparison with existing dimensional data

| d | Critical $\Sigma\lambda / |\Lambda|$ | Source |
|---|---|---|
| 2 | $\sim 0.05$ | [`01-anti-collapse-2d.md`](01-anti-collapse-2d.md) + [`06-dimensional-rescaling.md`](06-dimensional-rescaling.md) |
| 3 | $\sim 0.5$ | [`04-anti-collapse-3d.md`](04-anti-collapse-3d.md) + [`06-dimensional-rescaling.md`](06-dimensional-rescaling.md) |
| 4 | $\sim 0.125$ | [`10-dimensional-rescaling-higher-d.md`](10-dimensional-rescaling-higher-d.md), [`15-dimensional-rescaling-fdt.md`](15-dimensional-rescaling-fdt.md) |
| 5 | not on 1/d formula | [`10-dimensional-rescaling-higher-d.md`](10-dimensional-rescaling-higher-d.md), [`15-dimensional-rescaling-fdt.md`](15-dimensional-rescaling-fdt.md) |
| 6 | _pending_ | this result |

The 1/d formula predicts ratio $\sim 0.167$ at d=6 (i.e., $\Sigma\lambda_{\text{crit}} \sim 1.33$). The d=4,5 data does not follow this prediction. The d=6 data clarifies whether the formula breaks down further or stabilizes.

## Status assignment

Status: _pending GPU execution_. Will be assigned (tested_consistent, tested_inconsistent, or partial) once `outputs/dimensional_rescaling_d6_p3/summary.json` is populated. The structural reading is independent of the specific ratio value; the ratio's d-dependence is the open question for [`../open-problems/01-analytical-anti-collapse.md`](../open-problems/01-analytical-anti-collapse.md) (Townes-profile volume averaging is the suggested analytical path to recover the d-dependence from the equation).

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
