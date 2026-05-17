# Result 30: Methodological audit of the dimensional-rescaling series conventions

## Purpose

The dimensional-rescaling literature in this repository ([`06-dimensional-rescaling.md`](06-dimensional-rescaling.md), [`10-dimensional-rescaling-higher-d.md`](10-dimensional-rescaling-higher-d.md), [`15-dimensional-rescaling-fdt.md`](15-dimensional-rescaling-fdt.md), [`24-dimensional-rescaling-d6.md`](24-dimensional-rescaling-d6.md)) and the canonical anti-collapse literature ([`04-anti-collapse-3d.md`](04-anti-collapse-3d.md), [`26-phase-diagram-2d-slice.md`](26-phase-diagram-2d-slice.md), [`27-phase-diagram-d2-slice.md`](27-phase-diagram-d2-slice.md), [`28-phase-diagram-d4-slice.md`](28-phase-diagram-d4-slice.md)) use two different initial-state conventions. This audit documents that fact explicitly, identifies the structural relationship between the conventions, and clarifies which results compare directly to which.

## The two conventions

**Convention A: dimensional-rescaling series.** Initial state is a Gaussian with $\sigma_{\text{init}} = 0.4$, NON-NORMALIZED:
$$
\psi_0(\mathbf{r}) = \left(\frac{1}{\sigma_{\text{init}} \sqrt{2\pi}}\right)^{d/2} \exp\left(-\frac{r^2}{2 \sigma_{\text{init}}^2}\right).
$$
This prefactor normalizes the Gaussian to L² norm 1 in the continuum limit. On a discrete grid where the Gaussian is well-resolved ($dx < \sigma_{\text{init}}$), the discrete L² norm is approximately 1; on under-resolved grids ($dx > \sigma_{\text{init}}$, common at high $d$ with constrained voxel budget), the discrete norm differs from 1.

Used in [`10-dimensional-rescaling-higher-d.md`](10-dimensional-rescaling-higher-d.md) (d=4, d=5), [`15-dimensional-rescaling-fdt.md`](15-dimensional-rescaling-fdt.md) (d=4, d=5 with P3), [`24-dimensional-rescaling-d6.md`](24-dimensional-rescaling-d6.md) (d=6).

Discrete initial peak values from the existing data:
- d=4, N=24, L=10: initial peak |Psi|^2 approximately 0.4 (under-resolution mild)
- d=5, N=12, L=10: initial peak approximately 0.3 (under-resolution moderate)
- d=6, N=8, L=10: initial peak 0.984 with initial_norm 3.76 (severe under-resolution; the Gaussian concentrates in one voxel)

The d=6 norm of 3.76 indicates that the discrete L² norm is NOT approximately 1 at this resolution; the field amplitude is much higher per voxel than the continuum-normalized convention would suggest. The "non-normalized" convention is a misnomer at this resolution because the field is concentrated in fewer voxels than the continuum integral assumes.

**Convention B: canonical anti-collapse.** Initial state is a Gaussian with $\sigma_{\text{init}} = 0.5$, EXPLICITLY DISCRETELY NORMALIZED to total norm 1:
$$
\psi_0(\mathbf{r}) = \exp\left(-\frac{r^2}{2 \sigma_{\text{init}}^2}\right) \big/ \sqrt{\sum_{\mathbf{r}} |\psi_0(\mathbf{r})|^2 dx^d}.
$$
The discrete L² norm is exactly 1 by construction.

Used in [`04-anti-collapse-3d.md`](04-anti-collapse-3d.md) (d=3 canonical, N=128, peak |Psi|^2 = 1.437), [`26-phase-diagram-2d-slice.md`](26-phase-diagram-2d-slice.md) (d=3 slice, N=48, peak 1.437), [`27-phase-diagram-d2-slice.md`](27-phase-diagram-d2-slice.md) (d=2 slice, N=128, peak 1.273), [`28-phase-diagram-d4-slice.md`](28-phase-diagram-d4-slice.md) (d=4 slice, N=16, peak 0.403), [`25-vibrational-modes-3d.md`](25-vibrational-modes-3d.md) (d=3 vibrational, N=64, peak 1.437), [`29-cross-chamber-spectrum-audit.md`](29-cross-chamber-spectrum-audit.md) (literature audit consolidation).

Initial peak |Psi|^2 under canonical normalization scales as:
- d=2: peak 1.273
- d=3: peak 1.437
- d=4: peak 0.403
- (d=5, d=6 not run in canonical convention; budget makes lattice resolution inadequate)

The canonical peak DECREASES at d=4 (and would decrease further at higher d) because the normalization spreads the unit-norm Gaussian over an increasing d-dimensional volume.

## Structural reading: why the conventions differ

The two conventions are NOT a matter of right-vs-wrong methodology. They probe different regions of the same equation's parameter space.

Convention A (sigma=0.4 non-normalized) keeps the local field amplitude high enough that the cubic attraction $\Lambda|\Psi|^2 \Psi$ dominates the kinetic operator at the focal region across all tested $d$. This gives access to the focal-collapse regime at d=4, 5, 6 where Convention B's normalized state has too low peak amplitude for the cubic to dominate.

Convention B (sigma=0.5 normalized) maintains the canonical d=3 anti-collapse field with peak ~1.44, matched to the paper Section 6.1 reference configuration. Extending this convention to other $d$ preserves the L² norm but does not preserve the regime: at d=2 the field is at L²-critical with focal collapse accessible, at d=3 supercritical focal collapse accessible (the canonical setup), at d=4 the canonical peak drops to 0.4 and the cubic does not dominate the kinetic operator at the chosen N.

The two conventions are therefore complementary: Convention A probes focal-collapse phenomenology across $d$ at the cost of dimension-dependent field amplitude; Convention B probes a fixed normalization across $d$ at the cost of regime-changing behavior.

## What this means for the 1/d formula

The boxed formula $\Sigma\lambda_{\text{crit}}/|\Lambda| \sim 1/d$ in [`06-dimensional-rescaling.md`](06-dimensional-rescaling.md) was derived from 2D and 3D data using what amounts to Convention A (the 2D paper used $\Sigma\lambda = 0.4$ and the 3D paper used $\Sigma\lambda = 4$ with their respective focal-collapse initial states). The formula is an empirical fit within Convention A's focal-collapse regime.

The d=4 and d=5 extension in [`15-dimensional-rescaling-fdt.md`](15-dimensional-rescaling-fdt.md) found the ratio to be NON-monotonic across $d$ in Convention A:

| $d$ | Ratio $\Sigma\lambda_{\text{crit}}/|\Lambda|$ (Convention A) |
|---|---|
| 2 | 0.05 |
| 3 | 0.5 |
| 4 | 0.125 |
| 5 | 0.25 |

The 1/d formula's monotonic prediction (0.5, 0.33, 0.25, 0.20 across d=2,3,4,5) is not matched by the data. The d=6 result ([`24-dimensional-rescaling-d6.md`](24-dimensional-rescaling-d6.md)) shows the focal-collapse regime is not accessible at all in Convention A at d=6 with the available lattice resolution; the "anti-collapse threshold" notion does not apply cleanly.

The structural reading: the 1/d formula is a useful empirical fit at d=2, 3 within Convention A's focal-collapse regime; it does not extend cleanly to higher $d$ even within Convention A; the dimensional rescaling is more structured than the formula captures. This is consistent with the analytical sketch in [`../open-problems/01-analytical-anti-collapse.md`](../open-problems/01-analytical-anti-collapse.md), which identifies the dimensional dependence as entering via the lag-dynamics correction to the equilibrium-tracking sufficiency, not as a simple geometric factor.

## What this means for the canonical phase diagram series

The phase diagram series ([`26-phase-diagram-2d-slice.md`](26-phase-diagram-2d-slice.md), [`27-phase-diagram-d2-slice.md`](27-phase-diagram-d2-slice.md), [`28-phase-diagram-d4-slice.md`](28-phase-diagram-d4-slice.md)) uses Convention B. The d=3 slice (results/26) probes the canonical anti-collapse regime; the d=2 slice (results/27) probes the L²-critical regime; the d=4 slice (results/28) is dispersive throughout because Convention B at d=4 with N=16 places the field below focal-collapse onset.

The d=4 dispersive-throughout result in results/28 is therefore not a structural finding about d=4 dynamics. It is a structural finding about Convention B's behavior at d=4 with the chosen budget: the canonical-normalized convention with practical lattice resolution does not access focal-collapse at d=4. To probe d=4 focal-collapse, Convention A is the relevant convention; the results/15 d=4 data ($\Sigma\lambda_{\text{crit}}/|\Lambda| = 0.125$) gives the answer.

## Recommended cross-convention bridge

For comparing results across conventions, the relevant invariant is the field amplitude at the focal region, not the L² norm. Specifically:

- Initial peak $|\Psi(0)|^2$ at $t=0$
- Maximum peak $|\Psi(0)|^2_{\text{max}}$ during evolution
- The ratio of these to the cubic-kinetic balance $|\Lambda|^{-1}$

A future tabulation across all dimensional-rescaling and phase-diagram results, listing each in terms of these amplitude-based quantities rather than the L² norm, would make cross-convention comparison direct.

## Status

This audit is a **methodological consolidation**, not a new result. It does not change the status of any existing result; it documents the relationship between the two conventions so that the existing results can be read in their appropriate scope. The 1/d formula's status remains as documented in [`15-dimensional-rescaling-fdt.md`](15-dimensional-rescaling-fdt.md) (does not extend cleanly past d=3 even in Convention A). The phase diagram series' status remains as documented in each result doc (tested_consistent at the regime-reproducibility level for d=3 multi-seed; partial for d=2 and d=4 single-seed).

The audit does suggest two productive next steps:

1. **Convention A multi-seed extension at d=2 and d=3.** The current Convention B phase diagrams have multi-seed extension (results/26 tested_consistent); the older Convention A 2D and 3D references (paper anti-collapse demonstrations) are single-seed. A multi-seed extension within Convention A would close the same statistical-power question for that series.

2. **Cross-convention amplitude tabulation.** Listing all existing results in terms of $|\Psi(0)|^2$, max peak, and the cubic-kinetic balance ratio would enable direct comparison across conventions and make the "regime" of each result explicit in a convention-independent way.

## Related documents

- [`06-dimensional-rescaling.md`](06-dimensional-rescaling.md): the source 2D-3D rescaling result; Convention A.
- [`10-dimensional-rescaling-higher-d.md`](10-dimensional-rescaling-higher-d.md), [`15-dimensional-rescaling-fdt.md`](15-dimensional-rescaling-fdt.md): the d=4, d=5 extensions; Convention A.
- [`24-dimensional-rescaling-d6.md`](24-dimensional-rescaling-d6.md): the d=6 result; Convention A.
- [`04-anti-collapse-3d.md`](04-anti-collapse-3d.md): the canonical 3D anti-collapse; Convention B.
- [`26-phase-diagram-2d-slice.md`](26-phase-diagram-2d-slice.md), [`27-phase-diagram-d2-slice.md`](27-phase-diagram-d2-slice.md), [`28-phase-diagram-d4-slice.md`](28-phase-diagram-d4-slice.md): the phase diagram slices; Convention B.
- [`../open-problems/01-analytical-anti-collapse.md`](../open-problems/01-analytical-anti-collapse.md): the analytical theory that should resolve the dimensional dependence in a convention-independent form.
