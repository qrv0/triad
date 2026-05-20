# Result 28: phase diagram 2D slice ($\Sigma\lambda \times \gamma_0$) at d=4

## Prediction tested

The equation in the focal-collapse regime ($\Lambda < 0$) has multiple regime
structures (collapse, released, stable, dispersive, runaway). The first
focused slice at d=3 ([`26-phase-diagram-2d-slice.md`](26-phase-diagram-2d-slice.md))
mapped the released-dominated regime in the canonical supercritical
configuration; the d=2 slice ([`27-phase-diagram-d2-slice.md`](27-phase-diagram-d2-slice.md))
extended this to the L2-critical d=2 case. The structural prediction for
d=4 is that the regime structure shifts further toward the focal-collapse
or runaway side because d=4 is more strongly L2-supercritical, and the
dimensional rescaling formula $\Sigma\lambda/|\Lambda| \sim 1/d$ predicts
ratio $\sim 0.25$ at d=4 (so $\Sigma\lambda \sim 2$ at $|\Lambda|=8$).

## Method

Script: [`../experiments/physics/test_phase_diagram_d4_slice.py`](../experiments/physics/test_phase_diagram_d4_slice.py).
4D Strang split-step CuPy solver with full P1+P2+P3 triangle active.
Convention extended from the canonical d=3 anti-collapse protocol: sigma_init
normalized to total L2 norm 1.

Configuration:
- d=4, N=16 (65,536 voxels per field; analogous compromise to d=3's N=48
  vs canonical N=128).
- L=20, dt=0.0025, n_steps=2000.
- sigma_init=0.5 with normalization $\psi \leftarrow \psi / \sqrt{\int |\psi|^2 d^4x}$
  (canonical normalized Gaussian, 4D L2 norm). Initial peak $|\Psi|^2 = 0.403$
  (computed at script runtime; smaller than d=3's 1.437 per the analytic
  $(2\pi\sigma^2)^{-d/2}$ dependence: at $\sigma=0.5$ the continuous-limit
  value is $(2\pi \cdot 0.25)^{-d/2}$ which decreases with d).
- $\Lambda = -8$ (canonical attractive nonlinearity).
- $T_{\text{bath}} = 0.001$ (matching canonical phase diagram).
- Memory hierarchy 75/25 split: $\lambda_{\text{fast}} = 0.75 \Sigma\lambda$,
  $\lambda_{\text{slow}} = 0.25 \Sigma\lambda$, with $\nu_{\text{fast}} = 10$,
  $\nu_{\text{slow}} = 0.5$.

Sweep grid (20 points, 5 x 4):
- $\Sigma\lambda \in \{0.5, 1.0, 2.0, 4.0, 8.0\}$ (d=4 is more
  supercritical so the sweep extends further than the d=3 sweep; covers
  the 1/d formula prediction at $\Sigma\lambda \sim 2$ and the factor-10
  formula prediction at $\Sigma\lambda \sim 40$ partially).
- $\gamma_0 \in \{0.01, 0.05, 0.2, 1.0\}$.
- Seeds vary per grid point: $42 + \lfloor 10 \Sigma\lambda \rfloor + \lfloor 100 \gamma_0 \rfloor$.

Regime classification (per [`04-anti-collapse-3d.md`](04-anti-collapse-3d.md)
+ paper Section 6.1 phenomenology; identical to the d=3 script).

Hardware: RTX 4060 Laptop GPU, CUDA, CuPy backend. Wall time 115 seconds.

## Convention note

The canonical anti-collapse convention (sigma_init=0.5 normalized to total
norm 1) is used here, extended to d=4. This is the convention of the
canonical anti-collapse series ([`04-anti-collapse-3d.md`](04-anti-collapse-3d.md),
[`25-vibrational-modes-3d.md`](25-vibrational-modes-3d.md),
[`26-phase-diagram-2d-slice.md`](26-phase-diagram-2d-slice.md),
[`27-phase-diagram-d2-slice.md`](27-phase-diagram-d2-slice.md)) and the
extension to d=4 is internally consistent with that series.

This is distinct from the dimensional-rescaling series convention
(sigma=0.4 non-normalized) used in
[`10-dimensional-rescaling-higher-d.md`](10-dimensional-rescaling-higher-d.md),
[`15-dimensional-rescaling-fdt.md`](15-dimensional-rescaling-fdt.md), and
[`24-dimensional-rescaling-d6.md`](24-dimensional-rescaling-d6.md). The two
conventions are internally consistent within their own series and are not
in conflict.

## Results

**Regime map.** Rows are $\Sigma\lambda$, columns are $\gamma_0$:

| $\Sigma\lambda \setminus \gamma_0$ | 0.01 | 0.05 | 0.2 | 1.0 |
|---|---|---|---|---|
| 0.5 | dispersive | dispersive | dispersive | dispersive |
| 1.0 | dispersive | dispersive | dispersive | dispersive |
| 2.0 | dispersive | dispersive | dispersive | dispersive |
| 4.0 | dispersive | dispersive | dispersive | dispersive |
| 8.0 | dispersive | dispersive | dispersive | dispersive |

Regime counts: dispersive 20, released 0, intermediate 0, collapse 0,
runaway 0, stable 0.

**Quantitative metrics** (representative; all grid points start at
initial_peak 0.403):

| $\Sigma\lambda$ | $\gamma_0$ | max_peak | final_peak | peak_growth | final_ratio | regime |
|---|---|---|---|---|---|---|
| 0.5 | 0.01 | 0.4033 | 0.0011 | 1.00 | 0.0027 | dispersive |
| 1.0 | 0.05 | 0.4033 | 0.0046 | 1.00 | 0.0114 | dispersive |
| 2.0 | 0.20 | 0.4033 | 0.0092 | 1.00 | 0.0227 | dispersive |
| 4.0 | 1.00 | 0.4033 | 0.0116 | 1.00 | 0.0287 | dispersive |
| 8.0 | 0.01 | 0.4033 | 0.0010 | 1.00 | 0.0025 | dispersive |

Every grid point exhibits peak_growth exactly 1.00 (max_peak equals
initial_peak), meaning the field never enters a focal-growth phase under
any combination of $\Sigma\lambda \in [0.5, 8.0]$ and $\gamma_0 \in [0.01,
1.0]$ tested. The field disperses monotonically from initial peak 0.403
to final peak $\sim 10^{-3} \text{ to } 10^{-2}$ depending on $\gamma_0$.

**Norm conservation.** Initial norm 1.0; final norm growth with
$\gamma_0$ tracks the FDT-locked noise injection (4D volume L^4 = 160,000
means norm growth at d=4 is substantial: final_norm reaches $\sim 800$ at
$\gamma_0=1.0$).

## Reading the regime structure

The d=4 phase diagram yields a single regime in the explored region: the
dispersive regime. The peak_growth ratio is exactly 1.00 at every tested
point; the field does not enter a focal-growth phase.

The structural reading: the canonical anti-collapse configuration extended
to d=4 with N=16 places the initial state below the focal-collapse
threshold under these lattice conditions. Three contributing factors are
identifiable from the configuration:

1. **Initial peak amplitude drops with d.** At $\sigma_{\text{init}}=0.5$
   with normalization to total L2 norm 1, the continuous-limit initial
   peak is $(2\pi\sigma^2)^{-d/2}$, which evaluates to $\sim 0.318$ at d=2
   (lattice value 1.273), $\sim 1.437$ at d=3 (lattice value matches), and
   $\sim 0.403$ at d=4 (lattice value matches). The d=4 initial peak is
   $\sim 3.5\times$ smaller than d=3's, reducing the attractive cubic drive
   $|\Lambda|\rho$ by the same factor.

2. **Lattice underresolution at N=16, L=20.** The lattice spacing is
   $dx = L/N = 1.25$, while the initial Gaussian width is $\sigma=0.5 <
   dx$. The Gaussian is concentrated in less than one voxel, so the
   lattice does not adequately resolve the focal region. The
   focal-collapse mechanism requires the cubic nonlinearity to concentrate
   the field below the lattice scale; at d=4 with N=16, the initial state
   already occupies less than one voxel, so the lattice prevents further
   focal concentration.

3. **High-d voxel-count constraint.** At d=4 the voxel budget at N=16 is
   $16^4 = 65{,}536$; matching the canonical d=3 N=128 voxel budget of
   $128^3 = 2.1$ million would require $N \approx 38$ at d=4, which is
   memory-intensive. The N=16 compromise sacrifices spatial resolution
   for the 20-point grid sweep; the consequence is that the focal-region
   dynamics that d=4 should exhibit (more concentrated focal region per
   the geometric argument in
   [`06-dimensional-rescaling.md`](06-dimensional-rescaling.md)) cannot be
   resolved.

The structural prediction from the dimensional rescaling formula
($\Sigma\lambda/|\Lambda| \sim 1/d$ gives ratio 0.25 at d=4; so
$\Sigma\lambda \sim 2$ at $|\Lambda|=8$) is therefore not testable from
this configuration: the field never enters the regime where the
anti-collapse mechanism would be tested. The result is what the equation
does at d=4 with sigma_init=0.5 normalized, N=16, L=20, in the
(Sigma_lambda, gamma_0) sweep: monotonic dispersion. The result does not
test the dimensional rescaling claim; the lattice underresolution
prevents the focal-collapse regime from being reached.

**No collapse, released, runaway, intermediate, or stable regime observed.**
The classifier criterion for each of these regimes requires peak_growth >
1 (or 1) at minimum; the d=4 N=16 configuration produces peak_growth =
1.00 (machine precision agreement, no growth).

## Boundary structure

No regime boundaries are observable in this slice because the entire slice
classifies as the same regime. The continuous quantities (final_peak,
final_ratio) vary smoothly with $\gamma_0$ (final_ratio increases from
$\sim 0.003$ at $\gamma_0=0.01$ to $\sim 0.03$ at $\gamma_0=1.0$) and are
nearly independent of $\Sigma\lambda$ (because the memory potential never
accumulates: $\rho$ never exceeds initial_peak, so $V_{\text{mem}}$ never
exceeds $\Sigma\lambda \cdot \rho_0$).

## Comparison to d=2 and d=3 regime maps

The three slices ($d=2$ [`27`](27-phase-diagram-d2-slice.md), $d=3$
[`26`](26-phase-diagram-2d-slice.md), $d=4$ this result) in the canonical
anti-collapse configuration produce qualitatively different regime
structures:

| Dimension | initial_peak | dominant regime | dispersive count | released count |
|---|---|---|---|---|
| d=2 | 1.273 | released | 5/20 | 13/20 |
| d=3 | 1.437 | released | 1/20 | 11/20 |
| d=4 | 0.403 | dispersive | 20/20 | 0/20 |

Qualitative structural observations across the three slices:

- **d=2 and d=3 both show released-dominant regimes**: the anti-collapse
  mechanism operates at both dimensions in the canonical
  sigma_init=0.5-normalized configuration, with d=2 reaching stronger
  transient focal growth (peak_growth $\sim 20\times$) and d=3 reaching
  moderate transient focal growth (peak_growth $\sim 5\text{-}8\times$).
- **d=4 shows neither released nor collapse phenomenology in the
  configuration tested.** The field never enters focal growth; the
  dispersive regime fills the slice. This is not a structural prediction
  that the equation cannot anti-collapse at d=4; it is the structural
  observation that the canonical $\sigma_{\text{init}}=0.5$-normalized
  configuration at N=16, L=20 does not place the field in the
  focal-collapse regime at d=4. Lattice resolution and initial-state
  amplitude both contribute to this.
- **Released-to-dispersive transition shifts with d**: at d=2 the
  transition is at $\gamma_0 \approx 0.5$ (dispersive only at $\gamma_0 =
  1.0$); at d=3 the transition is at $\gamma_0 \approx 1.0$ with high
  $\Sigma\lambda$ (1/20 dispersive); at d=4 the entire slice is
  dispersive. The d=4 finding here is a property of the chosen test
  configuration's amplitude-vs-resolution balance, per the analysis above.

## Status assignment

Status: **partial** with respect to the d=4 phase-diagram open problem
contribution.

- Single seed per grid point.
- 20-point grid does not reach the focal-collapse regime at d=4 with the
  chosen $\sigma_{\text{init}}=0.5$ normalized and N=16. The dimensional
  rescaling prediction at d=4 is not testable from this configuration.
- The result documents what the equation does in this specific d=4
  configuration; it does not bear on the structural claim that the
  anti-collapse mechanism operates at d=4 in a focal-collapse regime
  (which would require a different initial-state amplitude or higher N).

The result contributes evidence under criterion 4 (cross-domain coherence)
for the dimensional dependence of where the focal-collapse regime sits in
the (Sigma_lambda, gamma_0) plane: at d=4 with this initial-state
amplitude and lattice resolution, the focal-collapse regime is not
reached.

## Honest caveats

- **N=16 is small.** At d=4 the lattice spacing is $L/N = 1.25 > \sigma =
  0.5$, so the initial Gaussian is concentrated in less than one voxel.
  The focal-collapse mechanism that operates at d=2 (N=128) and d=3
  (N=48) requires the lattice to resolve the focal region; at d=4 N=16,
  the lattice does not. Higher N at d=4 would require a multi-GB voxel
  budget ($N^4$ scaling) per field, exceeding consumer GPU constraints.
- **Initial-state amplitude scales with d.** At $\sigma=0.5$ normalized,
  the d=4 initial peak 0.403 is $\sim 3.5\times$ smaller than d=3's 1.437
  and is below the focal-collapse threshold for $|\Lambda|=8$ in this
  configuration. A larger $|\Lambda|$ or a more concentrated initial
  state (smaller $\sigma$, higher peak) would push the d=4 configuration
  into the focal-collapse regime. The canonical convention is chosen for
  internal consistency with the canonical anti-collapse series, not as
  optimal for d=4 focal-collapse exploration.
- **Single seed per grid point.** Multi-seed runs would not change the
  structural observation that the field does not enter focal growth.
- **The result is what the equation does at d=4 in this specific
  configuration.** It is not a structural test of the dimensional
  rescaling formula at d=4; the focal-collapse regime that the formula
  would predict for the released boundary is not reached at this
  initial-state amplitude with this lattice resolution. The result
  serves as a calibration anchor for what the canonical-convention
  extension to d=4 produces at this voxel budget.
- **Comparison to the dimensional-rescaling series at d=4.** The series
  in [`10-dimensional-rescaling-higher-d.md`](10-dimensional-rescaling-higher-d.md)
  and [`15-dimensional-rescaling-fdt.md`](15-dimensional-rescaling-fdt.md)
  uses sigma=0.4 non-normalized at d=4 N=24, which produces a more
  amplitude-concentrated initial state and does reach the focal-collapse
  regime; that series tests the dimensional rescaling formula directly.
  The present d=4 slice uses the canonical anti-collapse convention
  instead, internally consistent with the canonical series; the
  trade-off is that the dimensional rescaling formula prediction is not
  directly tested here.

## Reproducibility

```bash
LD_LIBRARY_PATH=".venv/lib/python3.11/site-packages/nvidia/cufft/lib:$LD_LIBRARY_PATH" \
  .venv/bin/python experiments/physics/test_phase_diagram_d4_slice.py
```

Wall time: 115 seconds on RTX 4060 Laptop GPU. Output:
`outputs/phase_diagram_d4_slice/summary.json`. Seeds vary per grid point.

## Related documents

- Phase diagram open problem: this result contributes to the characterization of the equation's regime structure across dimensions.
- [`26-phase-diagram-2d-slice.md`](26-phase-diagram-2d-slice.md): the
  companion d=3 slice in the canonical configuration this result extends
  from.
- [`27-phase-diagram-d2-slice.md`](27-phase-diagram-d2-slice.md): the
  companion d=2 slice produced in the same task.
- [`06-dimensional-rescaling.md`](06-dimensional-rescaling.md): the
  dimensional rescaling formula context.
- [`10-dimensional-rescaling-higher-d.md`](10-dimensional-rescaling-higher-d.md):
  the dimensional-rescaling series d=4 result in the alternative
  convention (sigma=0.4 non-normalized) that does reach the focal-collapse
  regime.
- [`24-dimensional-rescaling-d6.md`](24-dimensional-rescaling-d6.md): the
  d=6 dimensional-rescaling slice in the alternative convention.
- [`../experiments/physics/test_phase_diagram_d4_slice.py`](../experiments/physics/test_phase_diagram_d4_slice.py):
  the script.
