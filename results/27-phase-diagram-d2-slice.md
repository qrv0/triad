# Result 27: phase diagram 2D slice ($\Sigma\lambda \times \gamma_0$) at d=2

## Prediction tested

Open problem [`02-phase-diagram.md`](../open-problems/02-phase-diagram.md):
the equation in the focal-collapse regime ($\Lambda < 0$) has multiple regime
structures (collapse, released, stable, dispersive, runaway). The first
focused slice at d=3 ([`26-phase-diagram-2d-slice.md`](26-phase-diagram-2d-slice.md))
mapped the released-dominated regime in the canonical 3D supercritical
configuration. The structural prediction for d=2 is that the regime
structure differs from d=3 because the d=2 cubic NLS is L2-critical rather
than L2-supercritical: collapse is kinematic (above the Townes-soliton
threshold) rather than generic. The (Sigma_lambda, gamma_0) plane should
therefore admit released phenomenology at lower Sigma_lambda than d=3, in
accordance with the dimensional rescaling $\Sigma\lambda/|\Lambda| \sim 1/d$
([`06-dimensional-rescaling.md`](06-dimensional-rescaling.md)).

## Method

Script: [`../experiments/physics/test_phase_diagram_d2_slice.py`](../experiments/physics/test_phase_diagram_d2_slice.py).
2D Strang split-step CuPy solver with full P1+P2+P3 triangle active.
Convention extended from the canonical d=3 anti-collapse protocol: sigma_init
normalized to total L2 norm 1.

Configuration:
- d=2, N=128 (16,384 voxels per field; canonical d=2 anti-collapse in
  [`01-anti-collapse-2d.md`](01-anti-collapse-2d.md) uses N=256, this is a
  compromise for the 20-point grid sweep).
- L=20, dt=0.0025, n_steps=2000.
- sigma_init=0.5 with normalization $\psi \leftarrow \psi / \sqrt{\int |\psi|^2 d^2x}$
  (canonical normalized Gaussian, 2D L2 norm). Initial peak $|\Psi|^2 = 1.273$
  (computed at script runtime; differs from d=3's 1.437 per the analytic
  $(2\pi\sigma^2)^{-d/2}$ dependence and lattice discretization at N=128).
- $\Lambda = -8$ (canonical attractive nonlinearity).
- $T_{\text{bath}} = 0.001$ (matching the d=3 canonical phase diagram).
- Memory hierarchy 75/25 split: $\lambda_{\text{fast}} = 0.75 \Sigma\lambda$,
  $\lambda_{\text{slow}} = 0.25 \Sigma\lambda$, with $\nu_{\text{fast}} = 10$,
  $\nu_{\text{slow}} = 0.5$.

Sweep grid (20 points, 5 x 4):
- $\Sigma\lambda \in \{0.05, 0.1, 0.5, 1.0, 2.0\}$ (d=2 critical ratio per
  [`06-dimensional-rescaling.md`](06-dimensional-rescaling.md) is $\sim 0.05$
  so this sweep covers below the threshold and into the released regime).
- $\gamma_0 \in \{0.01, 0.05, 0.2, 1.0\}$.
- Seeds vary per grid point: $42 + \lfloor 100 \Sigma\lambda \rfloor + \lfloor 100 \gamma_0 \rfloor$.

Regime classification (per [`04-anti-collapse-3d.md`](04-anti-collapse-3d.md)
+ paper Section 6.1 phenomenology; identical to the d=3 script):
- "collapse": peak_growth > 50 AND final_ratio > 10.
- "released": peak_growth > 5 AND final_ratio < 0.5.
- "runaway": peak_growth > 50.
- "stable": 0.5 <= final_ratio <= 2.0.
- "dispersive": final_ratio < 0.5 AND peak_growth < 2.
- "intermediate": none of the above.

Hardware: RTX 4060 Laptop GPU, CUDA, CuPy backend. Wall time 40 seconds.

## Convention note

The canonical anti-collapse convention (sigma_init=0.5 normalized to total
norm 1) is used here, extended to d=2. This is the convention of the
canonical anti-collapse series ([`04-anti-collapse-3d.md`](04-anti-collapse-3d.md),
[`25-vibrational-modes-3d.md`](25-vibrational-modes-3d.md),
[`26-phase-diagram-2d-slice.md`](26-phase-diagram-2d-slice.md)) and the
extension to d=2 is internally consistent with that series.

This is distinct from the dimensional-rescaling series convention
(sigma=0.4 non-normalized) used in
[`10-dimensional-rescaling-higher-d.md`](10-dimensional-rescaling-higher-d.md),
[`15-dimensional-rescaling-fdt.md`](15-dimensional-rescaling-fdt.md), and
[`24-dimensional-rescaling-d6.md`](24-dimensional-rescaling-d6.md). The two
conventions are internally consistent within their own series and are not
in conflict; they answer different cross-dimensional questions (the
canonical anti-collapse series asks how the canonical d=3 protocol behaves
at adjacent d, the dimensional-rescaling series asks how a uniform
amplitude profile evolves at varying d).

## Results

**Regime map.** Rows are $\Sigma\lambda$, columns are $\gamma_0$:

| $\Sigma\lambda \setminus \gamma_0$ | 0.01 | 0.05 | 0.2 | 1.0 |
|---|---|---|---|---|
| 0.05 | intermediate | released | released | dispersive |
| 0.1 | released | released | released | dispersive |
| 0.5 | released | released | released | dispersive |
| 1.0 | released | released | released | dispersive |
| 2.0 | released | released | intermediate | dispersive |

Regime counts: released 13, dispersive 5, intermediate 2, collapse 0,
runaway 0, stable 0.

**Quantitative metrics** (selected, illustrative; all grid points start at
initial_peak 1.273):

| $\Sigma\lambda$ | $\gamma_0$ | max_peak | final_peak | peak_growth | final_ratio | regime |
|---|---|---|---|---|---|---|
| 0.05 | 0.01 | 28.48 | 26.79 | 22.37 | 21.05 | intermediate |
| 0.05 | 0.05 | 21.81 | 0.0247 | 17.13 | 0.0194 | released |
| 0.10 | 0.01 | 27.05 | 0.5076 | 21.26 | 0.3988 | released |
| 0.50 | 0.05 | 26.29 | 0.0162 | 20.65 | 0.0127 | released |
| 1.00 | 0.05 | 29.10 | 0.0158 | 22.86 | 0.0124 | released |
| 2.00 | 0.20 | 4.10 | 0.0121 | 3.22 | 0.0095 | intermediate |
| 2.00 | 1.00 | 1.62 | 0.0098 | 1.27 | 0.0077 | dispersive |

The peak_growth ratios at d=2 reach $\sim 20\times$ initial across most
grid points (vs $\sim 5\text{-}8\times$ at d=3), indicating a stronger
transient focal phase. After the focal growth, the field releases to final
peak $\sim 10^{-2}$ in the released regime.

**Norm conservation.** Initial norm is 1.0 (normalized). Final norm grows
with $\gamma_0$ due to FDT noise injection. At $\gamma_0 = 0.01$,
final_norm $\approx$ 1.05; at $\gamma_0 = 0.05$, $\approx$ 1.27; at
$\gamma_0 = 0.2$, $\approx$ 2.05; at $\gamma_0 = 1.0$, $\approx$ 6.07. The
norm growth is consistent with FDT-locked noise injection rate $2\gamma_0
T_{\text{bath}} N_{\text{steps}} V$ where V is the field volume (smaller
at d=2 than d=3, hence smaller absolute norm growth than d=3 at matched
$\gamma_0$).

## Reading the regime structure

The d=2 phase diagram yields three regimes occupying the explored region:

1. **Released regime** (13/20 points): the bulk. Occurs across $\gamma_0
   \in [0.01, 0.2]$ for $\Sigma\lambda \in [0.05, 2.0]$. The anti-collapse
   mechanism per paper Section 5.1 (the d=2 version of the mechanism)
   operates: focal growth phase reaches max_peak $\sim 20\times$ initial,
   then the cubic attraction is balanced by the memory potential and the
   field releases. Final peak is $\sim 10^{-2}$, a factor 50-100 below
   initial.

2. **Dispersive regime** (5/20 points): the entire $\gamma_0 = 1.0$
   column. Strong dissipation suppresses the focal growth phase
   (peak_growth $\le 1.5$); the field decays to dispersion without entering
   the focal regime.

3. **Intermediate regime** (2/20 points): the boundary at the corners.
   - $(\Sigma\lambda, \gamma_0) = (0.05, 0.01)$: low memory and low
     dissipation; the field grows to max_peak $\approx 28$ but stays
     elevated (final_ratio 21), failing the released criterion of
     final_ratio < 0.5. The mechanism is that at the lowest tested
     $\Sigma\lambda$ and the lowest $\gamma_0$, the memory is insufficient
     to release and the dissipation is too weak to disperse, so the field
     stays in an elevated post-growth state.
   - $(\Sigma\lambda, \gamma_0) = (2.0, 0.2)$: moderate memory and moderate
     dissipation; the dissipation already prevents the focal growth
     (peak_growth 3.22) so the released criterion (peak_growth > 5) is
     not met, but final_ratio is low (0.0095) so dispersive is also not
     met.

**No collapse regime observed in this grid.** Even at $\Sigma\lambda =
0.05$ (which the 1/d formula identifies as the d=2 critical ratio) the
released regime is reached at moderate $\gamma_0$. The collapse classifier
(peak_growth > 50) is not met by any tested point. The $(0.05, 0.01)$
intermediate point comes closest: peak_growth 22 with final_ratio 21
indicates the field is in an elevated quasi-stationary state, not a true
locked collapse.

**No runaway regime observed.** Memory pumping at $\Sigma\lambda = 2.0$
does not destabilize at any of the tested $\gamma_0$ values.

## Boundary structure

The released-to-dispersive boundary is approximately at $\gamma_0 \approx
0.5\text{-}1.0$ across all tested $\Sigma\lambda$ at d=2; the entire $\gamma_0
= 1.0$ column tips dispersive while all $\gamma_0 \le 0.2$ entries (except
the corners) are released. The boundary is sharper at d=2 than at d=3,
where the dispersive regime occupies only the single high-$\Sigma\lambda$,
high-$\gamma_0$ corner.

The structural reading: the d=2 critical L2-norm structure means even small
memory coupling ($\Sigma\lambda = 0.05$, near the 1/d formula threshold)
suffices to release the field at moderate $\gamma_0$. The mechanism is
that at d=2 the field is on the kinematic boundary between dispersive (norm
below Townes) and collapsing (norm above Townes), so a small repulsive
memory potential moves the released-collapsing balance significantly. At
d=3 (supercritical) the field is generically collapsing, so larger memory
coupling is required to overcome the attractive collapse drive.

## Comparison to d=3 regime map

The d=3 slice ([`26-phase-diagram-2d-slice.md`](26-phase-diagram-2d-slice.md))
in the canonical configuration uses
$\Sigma\lambda \in \{0.5, 1.0, 1.5, 2.0, 4.0\}$ and the same $\gamma_0$
sweep. Regime counts at d=3: released 11, intermediate 8, dispersive 1.
The d=2 slice produces a different distribution: released 13, dispersive
5, intermediate 2.

Qualitative structural observations across the two slices:

- **Released-regime dominance**: both d=2 and d=3 show released dominating
  the low-$\gamma_0$ region across all tested $\Sigma\lambda$. The
  anti-collapse mechanism is active at both dimensions.
- **Dispersive-regime extent**: at d=2 the dispersive regime fills the
  entire $\gamma_0 = 1.0$ column (5/20); at d=3 only the single
  $(\Sigma\lambda, \gamma_0) = (4.0, 1.0)$ corner is dispersive (1/20).
  The d=2 field is more easily dispersed by dissipation, consistent with
  its L2-critical nature (the field's marginal kinematic-pressure
  protection is more sensitive to dissipation removing amplitude).
- **Intermediate-regime extent**: at d=2 only 2 corner points are
  intermediate; at d=3 the intermediate regime occupies the entire upper-left
  portion (8/20) where moderate $\gamma_0$ and lower $\Sigma\lambda$ combine.
  The structural reading: at d=2 the released mechanism is more sharply
  on-or-off; at d=3 there is a wider transition band where the released
  mechanism partially operates but thermal contamination prevents the full
  released signature.
- **No collapse, no runaway at either dimension**: the canonical
  anti-collapse configuration with P3 active suppresses both indefinite
  focal locking and memory-driven runaway at d=2 and d=3.
- **Transient focal-growth magnitude**: d=2 reaches peak_growth $\sim 20\times$
  initial in the released regime; d=3 reaches only $\sim 5\text{-}8\times$ initial.
  The d=2 critical NLS produces stronger transient focal concentration
  before the memory releases, consistent with the d=2 mechanism
  documented in [`01-anti-collapse-2d.md`](01-anti-collapse-2d.md) (peak
  transient $\sim 80$ at supercritical norm in the unmemoried baseline; the
  memoried version retains a significant transient before release).

## Multi-seed extension (2026-05-17)

Script: [`../experiments/physics/test_phase_diagram_d2_slice_multiseed.py`](../experiments/physics/test_phase_diagram_d2_slice_multiseed.py). 4 seeds {42, 43, 44, 45} per grid point. Wall time 277 seconds on RTX 4060. Output: `outputs/phase_diagram_d2_slice_multiseed/summary.json`.

**Regime stability: all 20 grid points stable across all 4 seeds.** Every grid point yields the same regime classification across all 4 seeds. Stability counts: stable 20, boundary 0, ambiguous 0.

Multi-seed regime map:

| $\Sigma\lambda \setminus \gamma_0$ | 0.01 | 0.05 | 0.2 | 1.0 |
|---|---|---|---|---|
| 0.05 | intermediate | released | released | dispersive |
| 0.10 | stable | released | released | dispersive |
| 0.50 | released | released | released | dispersive |
| 1.00 | released | released | released | dispersive |
| 2.00 | released | released | intermediate | dispersive |

Regime counts: released 12, dispersive 5, intermediate 2, stable 1, collapse 0, runaway 0.

Quantitative variance per grid point (selected):

| $\Sigma\lambda$ | $\gamma_0$ | Regime | peak_growth (mean ± std) | final_ratio (mean ± std) |
|---|---|---|---|---|
| 0.05 | 0.01 | intermediate | 22.88 ± 0.21 | 8.09 ± 3.17 |
| 0.05 | 0.05 | released | 16.45 ± 0.97 | 0.022 ± 0.003 |
| 0.10 | 0.01 | stable | 22.13 ± 0.03 | 0.690 ± 0.175 |
| 0.50 | 0.20 | released | 10.55 ± 0.50 | 0.0101 ± 0.0011 |
| 1.00 | 0.05 | released | 22.64 ± 0.15 | 0.0123 ± 0.0014 |
| 2.00 | 0.05 | released | 23.19 ± 0.34 | 0.0240 ± 0.0017 |
| 2.00 | 1.00 | dispersive | 1.27 ± 0.02 | 0.0085 ± 0.0011 |

The peak_growth_ratio relative variance ranges from < 1% (most grid points) to ~10% (low-Σλ corner where the field is at the L²-critical boundary and dynamics are most variance-sensitive). The effect (the regime structure across the grid) exceeds the seed-to-seed variance at every grid point. The strong transient growth signature of L²-critical dynamics (peak_growth ~10-23 across most of the grid, compared to ~5-8 at d=3) is reproducible.

**Comparison with d=3 multi-seed (results/26):** both d=2 and d=3 yield regime-map seed-stability (all 20 grid points stable in each). The d=2 transient peak_growth is consistently 2-4x larger than d=3 (~22 vs ~5), confirming the L²-critical mechanism's stronger transient focal growth before release. The dispersive corner is wider at d=2 (entire $\gamma_0=1.0$ column dispersive) than d=3 (only $\Sigma\lambda=4, \gamma_0=1.0$ dispersive).

## Status assignment

Status: **tested_consistent** with respect to the regime-structure reproducibility at d=2 under criterion 4 (promoted from `partial` by the 2026-05-17 multi-seed extension); **partial** with respect to the full phase-diagram open problem at d=2 (the 20-point grid is too coarse to identify boundaries precisely, and the slice does not exhaust the higher-dimensional parameter space).

Statistical-power note: effect (the regime classification across 20 grid points) exceeds test-bed variance (all 20 grid points stable across 4 seeds; peak_growth relative variance < 10% at every grid point). The d=2 regime structure is reproducible, not a seed artifact. The qualitative finding (released-dominant low-$\gamma_0$ region, dispersive at high $\gamma_0$, intermediate / stable at low-$\Sigma\lambda$ corners; no collapse or runaway) is consistent with the structural expectation that the anti-collapse mechanism operates at d=2 as at d=3, with the L²-critical-specific signature of stronger transient peak_growth before release.

The result contributes evidence under criterion 4 (cross-domain coherence) for the regime structure of the equation extended to d=2.

## Honest caveats

- **N=128 is below canonical N=256** of the d=2 anti-collapse reference
  ([`01-anti-collapse-2d.md`](01-anti-collapse-2d.md)). Memory budget
  compromise for the 20-point sweep. The qualitative regime structure is
  expected to be N-robust, but precise locations of regime boundaries may
  shift with higher N.
- **Single seed per grid point.** Multi-seed runs would give variance
  estimates on the regime classification, particularly near the
  released-to-dispersive transition at $\gamma_0 = 0.2 \text{-} 1.0$.
- **No collapse regime observed.** The classifier criterion (peak_growth >
  50 AND final_ratio > 10) is not met by any tested point. Whether this
  reflects the structural prediction that the canonical anti-collapse
  configuration with P3 active suppresses collapse at d=2, or whether the
  tested $\Sigma\lambda$ range did not include values low enough to fail
  the anti-collapse mechanism, is a remaining question. The intermediate
  point at $(0.05, 0.01)$ is the closest to a collapse signature in this
  grid; lower $\Sigma\lambda$ at low $\gamma_0$ might cross into collapse.
- **2D slice, not full phase diagram.** $T_{\text{bath}}$ is fixed at
  0.001; varying $T_{\text{bath}}$ would shift the released-dispersive
  boundary along the $\gamma_0$ axis. The memory hierarchy and initial
  state are fixed.
- **Regime classifier thresholds are heuristic.** The cutoffs (peak_growth
  5 for released, 50 for collapse, etc.) are inherited from the d=3
  script. Whether the cutoffs should rescale with d for the released
  criterion (since d=2 produces peak_growth $\sim 20\times$ vs d=3's $\sim
  5\text{-}8\times$) is a calibration choice; the underlying continuous
  quantities (max_peak, final_ratio, norm_growth) are the structural
  information.

## Reproducibility

```bash
LD_LIBRARY_PATH=".venv/lib/python3.11/site-packages/nvidia/cufft/lib:$LD_LIBRARY_PATH" \
  .venv/bin/python experiments/physics/test_phase_diagram_d2_slice.py
```

Wall time: 40 seconds on RTX 4060 Laptop GPU. Output:
`outputs/phase_diagram_d2_slice/summary.json`. Seeds vary per grid point.

## Related documents

- [`../open-problems/02-phase-diagram.md`](../open-problems/02-phase-diagram.md):
  the open problem this result contributes to.
- [`26-phase-diagram-2d-slice.md`](26-phase-diagram-2d-slice.md): the
  companion d=3 slice this result extends from.
- [`28-phase-diagram-d4-slice.md`](28-phase-diagram-d4-slice.md): the
  companion d=4 slice produced in the same task.
- [`01-anti-collapse-2d.md`](01-anti-collapse-2d.md): the canonical d=2
  anti-collapse reference.
- [`06-dimensional-rescaling.md`](06-dimensional-rescaling.md): the
  dimensional rescaling formula context.
- [`../experiments/physics/test_phase_diagram_d2_slice.py`](../experiments/physics/test_phase_diagram_d2_slice.py):
  the script.
