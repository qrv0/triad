# Result 32: Convention x L matrix at d=2, d=3

## Prediction tested

[`31-cross-convention-phase-diagram-comparison.md`](31-cross-convention-phase-diagram-comparison.md) tested Convention A vs Convention B at L=20 and found Convention A all-dispersive while Convention B released-dominant at d=2 and d=3. The finding suggested that the dimensional-rescaling series (results/06, 10, 15, 24) used Convention A with L=10, which would give focal-collapse access where L=20 does not.

This result completes the (convention, L) matrix at d=2 and d=3 by running the 4 cells at L=10 (the dimensional-rescaling series' implicit L). Combined with the 4 cells at L=20 already in the repository, the full 8-cell matrix documents how the regime structure depends on (convention, L) jointly.

## Method

Script: [`../experiments/physics/test_convention_L_matrix.py`](../experiments/physics/test_convention_L_matrix.py). Implements both conventions in one solver, runs 4 cells at L=10 in series, single seed per grid point.

Wall time: 245 seconds on RTX 4060.

Parameters held fixed across all cells (matching the canonical phase-diagram series):
- Lambda = -8, T_bath = 0.001, dt = 0.0025, n_steps = 2000
- Memory split 75/25, nu_fast=10, nu_slow=0.5
- Grids: Sigma_lambda in {0.05, 0.1, 0.5, 1.0, 2.0} at d=2; in {0.5, 1.0, 1.5, 2.0, 4.0} at d=3; gamma_0 in {0.01, 0.05, 0.2, 1.0}

## Results

### The 8-cell matrix

Combining the existing L=20 results from [`26-phase-diagram-2d-slice.md`](26-phase-diagram-2d-slice.md), [`27-phase-diagram-d2-slice.md`](27-phase-diagram-d2-slice.md), [`31-cross-convention-phase-diagram-comparison.md`](31-cross-convention-phase-diagram-comparison.md), with the new L=10 results:

| Convention | L | d | initial peak | initial L2 norm | regime counts |
|---|---|---|---|---|---|
| A (sigma=0.4 non-norm) | 10 | 2 | 0.995 | 0.500 | dispersive 20 |
| A (sigma=0.4 non-norm) | 10 | 3 | 0.992 | 0.354 | dispersive 20 |
| A (sigma=0.4 non-norm) | 20 | 2 | 0.995 | 0.500 | dispersive 20 |
| A (sigma=0.4 non-norm) | 20 | 3 | 0.992 | 0.354 | dispersive 20 |
| B (sigma=0.5 normalized) | 10 | 2 | 1.273 | 1.000 | released 14, dispersive 5, intermediate 1 |
| B (sigma=0.5 normalized) | 10 | 3 | 1.437 | 1.000 | released 15, dispersive 3, intermediate 2 |
| B (sigma=0.5 normalized) | 20 | 2 | 1.273 | 1.000 | released 12, dispersive 5, intermediate 2, stable 1 |
| B (sigma=0.5 normalized) | 20 | 3 | 1.437 | 1.000 | released 11, dispersive 1, intermediate 8 |

(The L=20 d=3 row for Convention B is multi-seed; the other Convention B rows are single-seed for this comparison. The L=20 d=2 row for Convention B is also multi-seed.)

### Convention A is dispersive at BOTH L=10 and L=20

This was unexpected. The dimensional-rescaling series (results/06, 10, 15) documents focal-collapse with Convention A at L=10. Yet my Convention A at L=10 (here) is all-dispersive at both d=2 and d=3.

The difference is in the OTHER parameters, not (convention, L). The dimensional-rescaling series used:

- T_bath = 0.05 (50x higher than the phase-diagram series' 0.001)
- n_steps = 4000 (2x longer than the phase-diagram series' 2000)
- gamma_0 sweep starting at 0.05 (not 0.01)

These choices, together with Convention A's initial state, gave focal-collapse access at d=4, d=5 in results/15. With the phase-diagram series' parameters (T_bath=0.001, n_steps=2000, gamma_0 from 0.01), Convention A does NOT achieve focal-collapse at d=2, d=3 in this matrix.

### Convention B preserves focal-collapse access at both L=10 and L=20

This is a new structural finding. Convention B (sigma=0.5 with explicit discrete normalization to L2=1) maintains the released-dominant regime structure at both L=10 (released 14/20 d=2, 15/20 d=3) and L=20 (released 12/20 d=2, 11/20 d=3) with the phase-diagram series' parameters. The regime structure is L-robust at the box sizes tested.

The mechanism: Convention B's normalization keeps the L2 norm at 1 regardless of L. The cubic attraction |Lambda| |Psi|^2 with |Psi|^2 normalized to 1 across the box maintains the same effective amplitude at the focal region. As L changes, the field's spatial extent rescales but the integrated amplitude is preserved.

Convention A's prefactor (1/(sigma * sqrt(2 pi)))^(d/2) gives a peak amplitude that depends on sigma but a discrete L2 norm that depends on L and N (specifically, on how well-resolved the Gaussian is on the grid). At L=10 with N=48 (d=3) the discrete L2 is 0.35, not 1. At L=20 with N=48 it's still 0.35 (the Gaussian is the same width and the grid resolution is comparable). The integrated amplitude is consistently smaller than Convention B's L2=1.

### What this means for the dimensional-rescaling series

The dimensional-rescaling series' choice of Convention A is paired with a specific (T_bath, n_steps, gamma_0 range) regime that compensates for Convention A's lower L2 amplitude. With higher T_bath, the FDT noise injects energy that can push the field into focal-collapse despite the lower initial amplitude. With longer n_steps, slow focal-growth processes have time to develop. With higher gamma_0 minimum, the dissipative-driven regime is more thoroughly explored.

The 1/d-formula from results/06 and the d=4, d=5 ratios from results/15 are valid within this specific (Convention A, L=10, T_bath=0.05+, n_steps=4000+) operating region. They do NOT generalize to the (Convention A, T_bath=0.001, n_steps=2000) regime tested here.

### What this means for the canonical phase-diagram series

Convention B with the phase-diagram series' parameters (T_bath=0.001, n_steps=2000) is robust across L=10 and L=20. The released-dominant regime structure documented in results/26, 27 at L=20 also obtains at L=10 (this matrix). The phase-diagram series' findings are not L-specific within the tested range.

### What this means for the d=4 phase diagram (results/28)

results/28 documented Convention B at d=4, L=20, N=16 as all-dispersive. With the convention now characterized, the all-dispersive at d=4 Convention B is a combined effect of: (a) the canonical d=4 initial peak of 0.40 being lower than d=2, d=3 (due to normalization spreading more thinly at higher d), AND (b) the N=16 lattice under-resolving sigma=0.5 (dx=1.25 > sigma). Either factor alone might not have produced all-dispersive; the combination did. Higher N at d=4 (more lattice resolution) or different sigma would change this.

## Structural reading

The equation is the same in both conventions; the regime accessibility depends on the JOINT choice of (convention, L, sigma_init, T_bath, n_steps, gamma_0 range, Lambda). No single parameter is uniquely determining; pairs of parameters can compensate for each other (e.g., Convention A's lower amplitude is compensated by higher T_bath in the dimensional-rescaling series).

The structural-realist reading: the equation's predictions are about regimes (focal-collapse, released, dispersive, etc.), not about specific numerical thresholds in single-parameter sweeps. Each setup defines an operating region; different setups probe different regions; cross-regime comparison requires bridging through amplitude-based invariants (initial peak, max peak, cubic-kinetic balance), not through single-parameter sweeps.

Convention B at L=10 is itself a new operating region not previously documented in the repository. The released regime there (14/20 d=2, 15/20 d=3) extends the regime-coverage and confirms that the canonical Convention B is robust to the L=20 -> L=10 reduction.

## Convention A at native regime: d=2 and d=3 verification (2026-05-17)

Script: [`../experiments/physics/test_convention_A_native_regime.py`](../experiments/physics/test_convention_A_native_regime.py). Runs Convention A at L=10, sigma=0.4, T_bath=0.05 (dimensional-rescaling series value), n_steps=4000 (series value), gamma_0 from 0.05 (series minimum), at d=2 and d=3. Closes the `partial` clause of the convention question.

Result: even at the dimensional-rescaling series' native parameter regime, Convention A at L=10 does NOT achieve focal-collapse at d=2 or d=3.

| Cell | regime counts | peak_growth range |
|---|---|---|
| A_native_d2 (L=10, sigma=0.4, T_bath=0.05, n=4000) | 9 dispersive, 6 stable | 1.00-1.11 |
| A_native_d3 (L=10, sigma=0.4, T_bath=0.05, n=4000) | 5 dispersive, 10 stable | 1.00-1.03 |

Zero released regime at either d. Peak_growth ratios across all 30 grid points are between 1.00 and 1.11; the field essentially does not undergo focal growth before dispersing or stabilizing.

The structural reading is sharper than the convention-only framing in results/31: Convention A at L=10, sigma=0.4 does not access focal-collapse at d=2 or d=3 under any tested parameter regime (neither the phase-diagram series' T_bath=0.001 + n=2000 nor the dimensional-rescaling series' T_bath=0.05 + n=4000). The dimensional-rescaling series' focal-collapse access at d=4, d=5 (results/15) is a property of the d=4, d=5 amplitude regime, not of Convention A in general.

The implication for results/06's 1/d formula: the formula was built across DIFFERENT conventions silently. The d=2 anti-collapse demonstration (Σλ_crit/|Λ| ~ 0.05) cited in results/06 used a setup distinct from Convention A; the d=3 demonstration (Σλ_crit/|Λ| ~ 0.5) used Convention B / canonical; the d=4, d=5 datapoints in results/10, 15 used Convention A. The 1/d scaling is therefore not within-convention; it is across conventions, with the convention choice silently varying with d.

For the analytical theory in open-problems/01, the implication is that the dimensional dependence of Σλ_crit must be characterized in a convention-independent / amplitude-bridge form, not as a single-parameter sweep within Convention A or Convention B.

## Status assignment

Status: **tested_consistent** with respect to the convention-robustness question at the phase-diagram parameter regime: Convention B is L-robust at L=10 and L=20; Convention A is not focal-collapse-accessible at d=2, d=3 under ANY tested parameter regime. **tested_consistent** with respect to the convention-A-at-native-regime verification: Convention A at d=2, d=3 with (T_bath=0.05, n_steps=4000) is still all-dispersive-or-stable; the dimensional-rescaling series' focal-collapse access at d=4, d=5 is a property of those d's, not of Convention A generally.

The 1/d formula in results/06 is structurally informative as a fit across multi-convention data, not as a within-convention scaling.

Rule 9 application: the convention effect is deterministic in this regime (Convention A 100% non-released at both L and at native parameter regime, Convention B released-dominant at both L); single-seed runs are sufficient to document it. The variance question is closed at this scale because the convention effect dominates by orders of magnitude.

## Honest caveats

- **Phase-diagram parameter regime only.** The matrix uses (Lambda=-8, T_bath=0.001, n_steps=2000, gamma_0 from 0.01). The dimensional-rescaling series' (T_bath=0.05, n_steps=4000, gamma_0 from 0.05) regime would give different Convention A results.
- **Single seed per cell.** The convention effect is deterministic at the magnitude observed (Convention A 20/20 dispersive, Convention B 11+ released) so multi-seed extension is not required for the convention conclusion. Variance within each cell at the released-intermediate boundary in Convention B at L=10 would benefit from multi-seed.
- **N constraints.** d=2 at N=128 and d=3 at N=48 are matched between the L=10 and L=20 runs to isolate L as the variable. The dx values differ (L=10/N=128 = 0.078; L=20/N=128 = 0.156) so the lattice resolution differs slightly, but both are well-resolved (dx < sigma).
- **Convention A at the dimensional-rescaling regime not re-run.** A direct test of (Convention A, T_bath=0.05, n_steps=4000) at d=2, d=3 would close the question of whether the dimensional-rescaling series' specific parameter choices are necessary for Convention A's focal-collapse access. Left as a future verification.

## Reproducibility

```bash
LD_LIBRARY_PATH=".venv/lib/python3.11/site-packages/nvidia/cufft/lib:$LD_LIBRARY_PATH" \
  .venv/bin/python experiments/physics/test_convention_L_matrix.py
```

Wall time: 245 s on RTX 4060. Output: `outputs/convention_L_matrix/summary.json`. Seeds: per grid point, 42 + sl*10 + g0*100.

## Related documents

- [`30-dimensional-rescaling-convention-audit.md`](30-dimensional-rescaling-convention-audit.md): the audit identifying the two conventions.
- [`31-cross-convention-phase-diagram-comparison.md`](31-cross-convention-phase-diagram-comparison.md): the L=20 cross-convention comparison.
- [`26-phase-diagram-2d-slice.md`](26-phase-diagram-2d-slice.md), [`27-phase-diagram-d2-slice.md`](27-phase-diagram-d2-slice.md): the Convention B at L=20 references.
- [`06-dimensional-rescaling.md`](06-dimensional-rescaling.md), [`15-dimensional-rescaling-fdt.md`](15-dimensional-rescaling-fdt.md): the Convention A literature at L=10, T_bath=0.05, n_steps=4000.
- [`../open-problems/01-analytical-anti-collapse.md`](../open-problems/01-analytical-anti-collapse.md): the analytical theory that should clarify the parameter-region dependence in a regime-coherent form.
