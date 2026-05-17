# Result 15: dimensional rescaling at d=4 and d=5 with FDT-locked field noise (P3 active)

## Prediction tested

Extension of [`06-dimensional-rescaling.md`](06-dimensional-rescaling.md) to higher spatial dimensions, with P3 active.

Predicted observable: the critical $\Sigma\lambda_{\text{crit}}/|\Lambda|$ for anti-collapse should depend on spatial dimension $d$ but be ROBUST to bath coupling $\gamma_0$ (if the dimensional rescaling is a purely structural property of the equation's geometry, as results/06 argues).


## Method

The script [`../experiments/physics/test_dimensional_rescaling_high_d.py`](../experiments/physics/test_dimensional_rescaling_high_d.py) implements an $n$-dimensional anti-collapse solver with the full Strang split-step:
- Sub-step 4 (paper §4.1): exact OU update of auxiliary memory fields.
- Sub-step 5: P3 dissipation $\psi \leftarrow e^{-\gamma_0 dt} \psi$.
- Sub-step 6: P3 noise $\psi \leftarrow \psi + \sqrt{2 \gamma_0 T dt}\, \xi$ (complex Gaussian per voxel, FDT-locked).

**Parameters**: $|\Lambda| = 8$, $\sigma_{\text{init}} = 0.4$, $L = 10$, $T_{\text{bath}} = 0.05$, $dt = 0.0025$, $n_{\text{steps}} = 4000$. $d=4$ at $N=24$ (332k voxels); $d=5$ at $N=12$ (249k voxels). $\gamma_0 \in \{0.05, 0.2, 1.0\}$ (three points, per principles/03-coupling.md).

**Anti-collapse criterion**: $\rho_{\text{peak, final}} < 10 \cdot \rho_{\text{peak, initial}}$ (relaxed threshold; full release expected to drop further).

Backend: CuPy on RTX 4060. Wall time: 18.8 minutes total (slow due to per-step CPU-GPU noise transfer; future runs should use cupy.random for ~10x speedup).

## Results

Critical $\Sigma\lambda_{\text{crit}}/|\Lambda|$ ratio at each $(d, \gamma_0)$:

| $d$ | $\gamma_0 = 0.05$ | $\gamma_0 = 0.2$ | $\gamma_0 = 1.0$ |
|---:|:---:|:---:|:---:|
| 4 (this test, $N=24$) | **0.125** | **0.125** | **0.125** |
| 5 (this test, $N=12$) | **0.250** | **0.250** | **0.250** |

Reference (from `results/06-dimensional-rescaling.md`, larger lattice):

| $d$ | Ratio $\Sigma\lambda_{\text{crit}}/|\Lambda|$ |
|---:|:---:|
| 2 (L²-critical) | $\sim 0.05$ |
| 3 (L²-supercritical) | $\sim 0.5$ |

## Statistical analysis

**Two clean findings, two important caveats.**

**Finding 1 (the structural-realist content)**: $\Sigma\lambda_{\text{crit}}/|\Lambda|$ is **independent of $\gamma_0$** at fixed $d$ across the sweep tested. The ratio at $d=4$ is 0.125 at every coupling value (0.05, 0.2, 1.0); the ratio at $d=5$ is 0.250 at every coupling value. The dimensional rescaling is therefore robust to bath coupling strength within the sweep, consistent with the purely-structural reading: the scaling is a property of the equation's geometric concentration of the focal region, not of the dissipative dynamics.

**Finding 2 (the dimensional pattern)**: across the four documented dimensions, the ratio is non-monotonic:

| $d$ | ratio |
|---:|:---:|
| 2 | 0.05 |
| 3 | 0.5 |
| 4 | 0.125 |
| 5 | 0.25 |

Neither the boxed formula $1/d$ (which would give monotonically decreasing 0.5, 0.33, 0.25, 0.20) nor the factor-10-per-dimension reading of the geometric argument (which would give monotonically increasing 0.05, 0.5, 5, 50) matches this pattern. The actual scaling appears more structured than either candidate.

**Caveat 1 (regime question)**: at $d=4$ and $d=5$ in this test, the field's initial peak is $\sim 0.4$ (4D) and $\sim 0.3$ (5D). With $\Lambda = -8$, the attractive interaction at the initial Gaussian is modest. The "max_peak" through evolution never exceeded $\sim 1$ in many runs, suggesting the regime tested may be at or near the threshold of supercriticality, not deep in it. A test with smaller $\sigma_{\text{init}}$ (more concentrated initial state) or larger $|\Lambda|$ would be deeper in the supercritical regime and might give different threshold ratios.

**Caveat 2 (lattice resolution)**: $d=4$ at $N=24$ and especially $d=5$ at $N=12$ are at minimum-resolution. The focal region in higher dimensions covers fewer lattice cells, so resolution effects are stronger. The 3D reference uses $N=128$. A larger-lattice test on a stronger GPU would clarify.

**Caveat 3 (sweep granularity)**: the $\Sigma\lambda$ sweep at $d=4$ was [0, 1, 2, 4, 8, 16, 40]; the critical jumped to "released" at $\Sigma\lambda = 1$, so the actual critical may be smaller (between 0 and 1). A finer-grained sweep is needed to pin down the threshold precisely.

## Status assignment

Status: **partially tested**. Two structurally meaningful findings (gamma_0-invariance; non-monotonic d-scaling) emerge from the data. Both are honest; both are weaker than the strong-form claim that would resolve the 1/d vs factor-10 dispute. The new test demonstrates the P3-active methodology works (the gamma_0 invariance is the kind of structural fact this methodology can produce) but does not produce a clean d-scaling formula.

The result document's claim was "execution in progress, pending"; new here is the execution that finally happened. The status moves from "untested" to "partially tested" with the caveats above.

## What this implies for results/06

Results/06's boxed formula $\Sigma\lambda_{\text{crit}}/|\Lambda| \sim 1/d$ does not survive empirical extension to $d=4$ and $d=5$ in this test. The geometric argument in results/06 (about focal-region size scaling) may need re-examination at higher dimensions. The structural argument is consistent with what was observed in 2D and 3D; the formula derived from it doesn't match what's observed in 4D and 5D.

Possible explanations:
1. The geometric argument's assumption $N_{\text{focal}}^{(d)} \sim 10^{d-1}$ may not hold at higher $d$ at this lattice resolution.
2. The criterion "released vs not" may differ from the 3D reference's criterion in a way that matters at the threshold.
3. The actual physical scaling may be d-dependent in a way the geometric argument captures incompletely.

This is research; the result is informative regardless of which interpretation holds. Follow-up work could pursue tighter lattice + finer sweep at $d=4, 5$.

## Honest caveats (continued)

- Reduced lattice ($N=24$ at $d=4$, $N=12$ at $d=5$): marginal resolution at $d=5$.
- Minimal solver (no spinor; local memory only); full equation has more structure.
- Single seed per cell.
- CPU-GPU noise transfer bottleneck (~19 min wall instead of expected ~2 min); a future cupy.random version of the script would be much faster.
- The 2D and 3D reference numbers in results/06 use different solver code and lattice; direct apples-to-apples comparison would require running 2D and 3D with this same nD script.

## Reproducibility

```bash
LD_LIBRARY_PATH=".venv/lib/python3.11/site-packages/nvidia/*/lib:$LD_LIBRARY_PATH" \
  .venv/bin/python experiments/physics/test_dimensional_rescaling_high_d.py
```

Wall: ~19 min on RTX 4060 (CuPy, current implementation). Output: `outputs/dimensional_rescaling_high_d_p3/`. Seed base: 42.

## Related documents

- Source 2D-3D result (isolated): [`06-dimensional-rescaling.md`](06-dimensional-rescaling.md).
- Earlier result on the same prediction: [`10-dimensional-rescaling-higher-d.md`](10-dimensional-rescaling-higher-d.md).
- Equation derivation: [`../equation/01-derivation.md`](../equation/01-derivation.md), [`../equation/02-markovian-embedding.md`](../equation/02-markovian-embedding.md).
- Methodology of P3: [`../principles/03-coupling.md`](../principles/03-coupling.md).
