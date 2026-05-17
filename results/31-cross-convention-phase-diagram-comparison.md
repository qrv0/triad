# Result 31: Cross-convention phase diagram comparison at d=2 and d=3

## Prediction tested

[`30-dimensional-rescaling-convention-audit.md`](30-dimensional-rescaling-convention-audit.md) identified two distinct initial-state conventions in the repository's literature: Convention A (sigma_init=0.4, non-normalized Gaussian prefactor; used in the dimensional-rescaling series results/06, 10, 15, 24) and Convention B (sigma_init=0.5, normalized to discrete L2 norm 1; used in the canonical anti-collapse and phase-diagram series results/04, 25, 26-28). The audit recommended a direct cross-convention comparison: at the SAME box size L, do the two conventions yield the same regime structure, or does the convention itself shift the regime?

This result executes that comparison at d=2 and d=3 with L=20 (the canonical L of the phase-diagram series). It does NOT directly test the dimensional-rescaling series' findings at L=10; that comparison is left as a separate question identified in the discussion below.

## Method

Two new scripts implementing Convention A at d=2 and d=3:

- [`../experiments/physics/test_phase_diagram_d2_convention_A.py`](../experiments/physics/test_phase_diagram_d2_convention_A.py): Convention A at d=2. N=128, L=20, sigma=0.4 non-normalized. Other parameters identical to Convention B counterpart in [`27-phase-diagram-d2-slice.md`](27-phase-diagram-d2-slice.md): Lambda=-8, T_bath=0.001, 75/25 memory split, n_steps=2000.
- [`../experiments/physics/test_phase_diagram_d3_convention_A.py`](../experiments/physics/test_phase_diagram_d3_convention_A.py): Convention A at d=3. N=48, L=20, sigma=0.4 non-normalized. Other parameters identical to Convention B counterpart in [`26-phase-diagram-2d-slice.md`](26-phase-diagram-2d-slice.md).

Each script runs the same 5x4 (Sigma_lambda, gamma_0) grid as the Convention B counterpart. Single-seed each (multi-seed extension not needed for the convention-comparison question since the convention effect dominates the seed variance at the magnitude observed below).

Hardware: RTX 4060, CuPy backend. Wall time: ~3 min (d=2 N=128) and ~5 min (d=3 N=48) on GPU.

## Initial-state amplitudes by convention and dimension

The two conventions produce different initial states at the same sigma_init scale:

| Convention | d | sigma | initial peak |Psi|^2 | initial discrete L2 norm |
|---|---|---|---|---|
| A (non-normalized) | 2 | 0.4 | 0.995 | 0.500 |
| A (non-normalized) | 3 | 0.4 | 0.992 | 0.354 |
| B (normalized to norm 1) | 2 | 0.5 | 1.273 | 1.000 |
| B (normalized to norm 1) | 3 | 0.5 | 1.437 | 1.000 |

Convention A's prefactor (1/(sigma * sqrt(2 pi)))^(d/2) is designed so that the continuum L2 integral equals 1, but on a discrete grid with L=20 and the indicated N, the discrete L2 sum differs from 1: at d=2 it is 0.5, at d=3 it is 0.35. The peak is approximately 1 in both cases but the field is spread thinner in the d=3 box than d=2, reducing the discrete L2.

Convention B's explicit discrete normalization gives initial L2 = 1 in both d. The peak depends on d via the normalization condition (larger d, more spread, higher peak at center for fixed L2 = 1).

## Results

**Convention A at d=2, L=20:** all 20 grid points classified as dispersive. Peak_growth_ratio range 1.00-1.13 across the grid. The field never enters significant focal growth.

**Convention A at d=3, L=20:** all 20 grid points classified as dispersive. Peak_growth_ratio range 1.00-1.12. Same qualitative finding as d=2.

**Convention B at d=2, L=20** (from [`27-phase-diagram-d2-slice.md`](27-phase-diagram-d2-slice.md) multi-seed): released-dominant with 12 released + 5 dispersive + 2 intermediate + 1 stable. Peak_growth_ratio range ~10-23 in released cells.

**Convention B at d=3, L=20** (from [`26-phase-diagram-2d-slice.md`](26-phase-diagram-2d-slice.md) multi-seed): released-dominant with 11 released + 8 intermediate + 1 dispersive. Peak_growth_ratio range ~5-8 in released cells.

Summary table:

| Convention | d | L | dispersive | released | intermediate | other |
|---|---|---|---|---|---|---|
| A (sigma=0.4) | 2 | 20 | 20 | 0 | 0 | 0 |
| A (sigma=0.4) | 3 | 20 | 20 | 0 | 0 | 0 |
| B (sigma=0.5) | 2 | 20 | 5 | 12 | 2 | 1 (stable) |
| B (sigma=0.5) | 3 | 20 | 1 | 11 | 8 | 0 |

At L=20, the convention choice is the regime-determining factor.

## Structural reading

Convention A at L=20 places the field in the dispersive regime regardless of d. The discrete L2 norm of Convention A's initial state at L=20 is 0.35-0.50 rather than 1; the cubic attraction Lambda|Psi|^2 with peak |Psi|^2 ~ 1 and L2 ~ 0.4 is too weak to dominate the kinetic operator in the L=20 box. The field disperses across the wider box before focal collapse can develop.

Convention B's explicit normalization to discrete L2 = 1 keeps the field amplitude consistent with the cubic-kinetic balance at L=20, preserving access to the focal-collapse regime where the anti-collapse mechanism operates.

The dimensional-rescaling series (results/06, 10, 15, 24) used L=10 (half the box size of the phase-diagram series). At L=10 with sigma=0.4 non-normalized, the field is proportionally more concentrated relative to box size, recovering focal-collapse access at the various d in that series. The 1/d formula and the d-scaling observations in that series are within Convention A at L=10, not Convention A at L=20.

The conventions are therefore not directly interchangeable at any fixed L; each is paired with its L choice. Convention A + L=10 probes focal-collapse phenomenology across d=2-5; Convention B + L=20 probes focal-collapse phenomenology at d=2-3 (and tips into under-resolution at d=4 N=16 per results/28). Both are valid for their own scope; direct comparison across conventions requires either matching the effective amplitude (e.g., re-normalizing Convention A to L2=1 on the discrete grid) or matching the L choice.

## What this means for the equation

The structural form of the equation is the same in both conventions; only the initial state amplitude and the box size differ. The "anti-collapse mechanism" the equation describes is a property of the structural form and operates whenever the cubic-kinetic balance puts the field in the focal-collapse regime and the memory hierarchy is loaded sufficiently to release it. Both convention/L pairings access this regime at appropriate (d, Sigma_lambda, gamma_0) values; neither convention is "more correct" than the other.

The dimensional rescaling Sigma_lambda_crit/|Lambda| versus d is a Convention-A-at-L=10 finding. The phase diagram regime structure (released-dominant bulk) is a Convention-B-at-L=20 finding. They are complementary windows on the same equation's parameter space, not competing predictions.

## Status assignment

Status: **tested_consistent** with respect to the cross-convention question: the regime structure of the equation at L=20 depends on the initial-state convention; the conventions are not interchangeable at fixed L. **partial / informative** with respect to the broader convention-audit question: the Convention A at L=10 and the Convention B at L=10 versions have not been run here, leaving the L-dependence of the convention behavior partially characterized.

Rule 9 application: the effect (Convention A 20/20 dispersive vs Convention B 11+ released at d=3) exceeds any test-bed variance by orders of magnitude. The convention dependence at L=20 is a deterministic property of the initial state, not a stochastic seed effect; single-seed runs are sufficient to document it.

## Honest caveats

- **L=20 only.** This comparison fixes L=20 to match the phase-diagram series. The Convention A at L=10 (the dimensional-rescaling series' canonical L) is documented in results/06, 10, 15, 24 but is not re-run here. A complete cross-convention audit would also include Convention A at L=10 and Convention B at L=10 to map the full (convention, L) plane.
- **Single seed.** The convention effect dominates the seed variance at the magnitude observed; multi-seed would not change the qualitative finding. A multi-seed extension would document the variance for completeness but is not required for the convention-comparison conclusion.
- **N constraints.** d=2 at N=128 and d=3 at N=48 are the same lattice resolutions used in the Convention B phase-diagram counterparts. The convention finding is not an N artifact (both conventions ran at the same N).
- **Other variables fixed.** T_bath=0.001, memory split 75/25, nu_fast=10 nu_slow=0.5, n_steps=2000 are all matched between the conventions. The convention difference is in initial state only.

## Reproducibility

```bash
LD_LIBRARY_PATH=".venv/lib/python3.11/site-packages/nvidia/cufft/lib:$LD_LIBRARY_PATH" \
  .venv/bin/python experiments/physics/test_phase_diagram_d2_convention_A.py
LD_LIBRARY_PATH=".venv/lib/python3.11/site-packages/nvidia/cufft/lib:$LD_LIBRARY_PATH" \
  .venv/bin/python experiments/physics/test_phase_diagram_d3_convention_A.py
```

Wall time: ~3 min (d=2) + ~5 min (d=3) on RTX 4060. Output: `outputs/phase_diagram_d2_convention_A/summary.json` and `outputs/phase_diagram_d3_convention_A/summary.json`. Seeds vary per grid point.

## Related documents

- [`30-dimensional-rescaling-convention-audit.md`](30-dimensional-rescaling-convention-audit.md): the audit that motivated this comparison.
- [`26-phase-diagram-2d-slice.md`](26-phase-diagram-2d-slice.md), [`27-phase-diagram-d2-slice.md`](27-phase-diagram-d2-slice.md): the Convention B counterparts at d=3 and d=2.
- [`06-dimensional-rescaling.md`](06-dimensional-rescaling.md), [`10-dimensional-rescaling-higher-d.md`](10-dimensional-rescaling-higher-d.md), [`15-dimensional-rescaling-fdt.md`](15-dimensional-rescaling-fdt.md), [`24-dimensional-rescaling-d6.md`](24-dimensional-rescaling-d6.md): the Convention A literature at L=10 (the relevant L for that series).
- [`04-anti-collapse-3d.md`](04-anti-collapse-3d.md): the canonical Convention B 3D anti-collapse setup.
- [`../open-problems/01-analytical-anti-collapse.md`](../open-problems/01-analytical-anti-collapse.md): the analytical theory that should clarify the (convention, L) dependence in a fully dimension-coherent form.
