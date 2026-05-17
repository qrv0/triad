# Result 10: dimensional rescaling extended to 4D and 5D

---

## Prediction tested

Extension of [`06-dimensional-rescaling.md`](06-dimensional-rescaling.md) to higher spatial dimensions.

Predicted observable (from the structural argument in results/06): the critical total memory coupling $\Sigma\lambda_{\text{crit}}$ required to release supercritical collapse scales with spatial dimension. Two specific predictions are discriminated:

- **1/d scaling** (boxed formula in results/06): $\Sigma\lambda_{\text{crit}}/|\Lambda| \sim 1/d$. Predicts ratio $\sim 0.25$ at $d=4$, $\sim 0.20$ at $d=5$.
- **Factor-of-10-per-dimension scaling** (geometric argument in results/06): $\Sigma\lambda_{\text{crit}}/|\Lambda| \sim 10^{(d-1)}$. Predicts ratio $\sim 5$ at $d=4$ (so $\Sigma\lambda_{\text{crit}} \sim 40$ at $|\Lambda|=8$), and $\sim 50$ at $d=5$.

The empirical data (2D ratio 0.05, 3D ratio 0.5) supports neither formula exactly: 2D is approximately $1/20$ and 3D is approximately $1/2$, which is a factor of $\sim 10$ between dimensions but not $1/d$. The 4D and 5D measurements discriminate which extrapolation continues.

## Method

The script [`../experiments/physics/test_dimensional_rescaling_high_d.py`](../experiments/physics/test_dimensional_rescaling_high_d.py) implements a minimal $n$-dimensional anti-collapse solver from scratch (the existing [`../implementation/physics/solver_3d.py`](../implementation/physics/solver_3d.py) is dimension-specific to 3D). The solver uses:

- Strang split-step integration per [`../equation/02-markovian-embedding.md`](../equation/02-markovian-embedding.md): V/2 → K → V/2 → exact OU update of auxiliary fields.
- FFT-based kinetic step in $n$D.
- Two-mode memory $(\nu_{\text{fast}}, \nu_{\text{slow}}) = (10, 0.5)$, split as $\lambda_{\text{fast}}:\lambda_{\text{slow}} = 3:1$ within $\Sigma\lambda$.
- Exact OU update of auxiliary fields: $y_j \leftarrow e^{-\nu_j dt} y_j + (1 - e^{-\nu_j dt}) \rho$ (paper §4.1).

Parameters:
- $\Lambda = -8$ (same as 3D reference in [`results/04-anti-collapse-3d.md`](04-anti-collapse-3d.md))
- $\sigma_{\text{init}} = 0.4$ (compact concentration, supercritical regime)
- $dt = 0.0025$, $n_{\text{steps}} = 4000$ ($T_{\text{final}} = 10$)
- $L = 10$ (box length)
- $d=4$: $N = 24$ ($24^4 = 332k$ voxels per field, ~15 MB memory)
- $d=5$: $N = 16$ ($16^5 = 1M$ voxels per field, ~50 MB memory)
- Sweep $\Sigma\lambda$ across $[0, 40]$ at $d=4$ and $[0, 100]$ at $d=5$ to capture both candidate scaling predictions.

Anti-collapse criterion: $\rho_{\text{peak,final}} < 10 \cdot \rho_{\text{peak,initial}}$ (10x relaxed; full release expected to drive $\rho_{\text{peak,final}}$ below $\rho_{\text{peak,initial}}$).

Backend: numpy (CPU). Hardware: consumer CPU (the existing CuPy 3D solver is dimension-specific; an $n$D port to CuPy is wave-2 work).

Expected wall time: approximately 15-30 minutes per dimension on CPU.

## Results

**Status: execution in progress at the time of this writing.** The script is running; results will populate this section when it completes. Expected output:

| $d$ | Critical $\Sigma\lambda$ at $|\Lambda|=8$ | Ratio $\Sigma\lambda_{\text{crit}}/|\Lambda|$ |
|---:|---:|---:|
| 2 (results/06) | $\sim 0.4$ | $\sim 0.05$ |
| 3 (results/06) | $\sim 4.0$ | $\sim 0.5$ |
| 4 (this test) | _pending_ | _pending_ |
| 5 (this test) | _pending_ | _pending_ |

The full per-sweep data is written to `outputs/dimensional_rescaling_high_d/summary.json` when the test completes.

## Status assignment

Status: **execution in progress, partial / pending**.

When the test completes, the status updates to:
- **tested (consistent with factor-10 scaling)** if ratio at $d=4$ is approximately 5 (i.e., $\Sigma\lambda_{\text{crit}} \sim 40$) and at $d=5$ is approximately 50;
- **tested (consistent with 1/d scaling)** if ratio at $d=4$ is approximately 0.25 (i.e., $\Sigma\lambda_{\text{crit}} \sim 2$) and at $d=5$ is approximately 0.20;
- **tested (inconsistent with both candidates)** if neither prediction is supported.

In any of these outcomes the result is informative: it discriminates between the two scaling hypotheses in results/06, both of which were named as candidates. The data fixes the actual scaling empirically.

## Honest caveats

- **Reduced lattice sizes.** $d=4$ at $N=24$ and $d=5$ at $N=16$ are at the minimum-resolution end where lattice artifacts may affect the precise threshold. The 3D reference uses $N=128$. Higher-resolution runs would require GPU CuPy port; deferred to wave 2.

- **Minimal solver.** The test uses a scalar (non-spinor) implementation with local memory only. The full equation has spinor option and nonlocal memory; these extensions are not used here. The result speaks to the cubic + local-memory subset of the full equation.

- **Single test point per dimension.** The structural argument in results/06 reasons from geometric considerations about the focal-region voxel count $N_{\text{focal}}^{(d)}$. A more thorough test would sweep $|\Lambda|$ as well as $\Sigma\lambda$ in 4D and 5D to verify that the threshold depends linearly on $|\Lambda|$ in higher dimensions as it does in 2D and 3D.

- **CPU numpy.** Compute-marginal for $d=5$. If the test produces results that require interpretation at the boundary of statistical confidence, larger-grid validation on GPU is needed.

## Reproducibility

```bash
python experiments/physics/test_dimensional_rescaling_high_d.py
```

Wall time: approximately 15-30 minutes total on CPU (4D + 5D combined). Output: `outputs/dimensional_rescaling_high_d/`. Random seed: 42.

## Related documents

- Source 2D-3D result: [`06-dimensional-rescaling.md`](06-dimensional-rescaling.md).
- Existing 3D anti-collapse: [`04-anti-collapse-3d.md`](04-anti-collapse-3d.md).
- Equation derivation and Markovian embedding: [`../equation/01-derivation.md`](../equation/01-derivation.md), [`../equation/02-markovian-embedding.md`](../equation/02-markovian-embedding.md).
- Methodology: [`../experiments/PROTOCOLS.md`](../experiments/PROTOCOLS.md).

## What this result implies for the program

The extension of the dimensional rescaling result to $d=4, 5$ either:

- **Supports the 1/d scaling** (results in low-Σλ critical thresholds): the structural argument's boxed formula is empirically supported across four dimensions, strengthening the geometric derivation in results/06.

- **Supports the factor-10-per-dimension scaling** (results in high-Σλ critical thresholds): the geometric argument's correct interpretation is that $\rho_{\text{eff}}$ scales as $10^{(1-d)}$ rather than $1/d$. The boxed formula in results/06 needs reformulation.

- **Supports neither**: the geometric argument needs revisiting at higher dimensions; the high-d behavior is governed by additional mechanisms (e.g., dimensional reduction of the focal region, or anomalous-scaling behavior).

Either of the first two outcomes refines the scaling-relation prediction from "$\sim 1/d$ or $\sim 10^{(d-1)}$" to a specific quantitative form. The third outcome opens a new research direction.

In all cases the cross-domain coherence claim of the equation is unaffected; the dimensional rescaling is a single-substrate scaling property, not a cross-substrate test.
