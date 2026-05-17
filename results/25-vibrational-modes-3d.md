# Result 25: vibrational mode spectrum at d=3 (P3 active)

> **METHODOLOGICAL FLAG (2026-05-17, post-hoc audit).** This result was generated with a test configuration that does NOT match the canonical 3D anti-collapse / crystalline-state protocol established in [`04-anti-collapse-3d.md`](04-anti-collapse-3d.md) and paper Section 6.3. The mismatches:
>
> 1. **Initial-state amplitude is ~40x too weak.** Used `sigma_init = 1.2` with the non-normalized Gaussian `psi = (1/(sigma sqrt(2pi)))^(d/2) exp(...)` giving peak |Psi|^2 ≈ 0.037. Canonical 3D anti-collapse (results/04) uses `sigma_init = 0.5` with `psi /= sqrt(sum |psi|^2 dx^d)` normalization, giving peak |Psi|^2 ≈ 1.44. At my chosen amplitude the field is below the focal-collapse regime and never reaches the released crystalline state.
> 2. **Sigma_lambda = 4.0 (results/04 anti-collapse regime), not 1.5 (paper Section 6.3 crystalline window).** The vibrational spectrum of the released crystalline state is well-defined only in the narrow crystalline window per `05-bravais-selection.md`.
> 3. **P3 active (gamma_0 = 0.02, T_bath = 0.005) does not match the conservative regime used in the canonical results/03 (2D vibrational) and paper Section 6.3 (3D vibrational). Norm grew from 0.35 to 22 during the run because of thermal noise injection on a non-crystallizing field; the "spectrum" measured is dominated by thermal fluctuations on a dispersing field.
> 4. **Equilibration window 1000 steps vs paper's 2000-step warmup.** Insufficient for the slow memory mode ($\nu_{\text{slow}} = 0.5$) to fully establish the crystalline regime.
> 5. **N = 32** is the smallest of the issues but is below the canonical N = 128.
>
> The "spectrum" reported below is therefore NOT the 3D vibrational spectrum of the crystalline state. It is the spectrum of a low-amplitude field dispersing under thermal noise. The structural reading of this result is null: it documents what happens when test configuration mismatches the canonical protocol, not what the 3D vibrational spectrum is.
>
> The status assignment originally given was "partial / inconsistent" with respect to the Hypogeum whole-tone scale; that comparison is invalid because the configuration tested is not the crystalline-state configuration the Hypogeum comparison requires.
>
> See [`../docs/llm-hedge-annotations.md`](../docs/llm-hedge-annotations.md) for the catalog entry on this and other Phase 9 wave-3 (2026-05-17) configuration errors.
>
> The proper 3D vibrational analysis requires re-running with: N = 128, L = 20, sigma_init = 0.5 normalized to total norm 1, Lambda = -8, Sigma_lambda = 1.5 (or 4.0 depending on regime targeted), gamma_0 = 0 and T = 0 (matching canonical conservative methodology for vibrational analysis), 2000-step warmup, then record. The body below is preserved as historical record per the repository's documentation-of-errors philosophy.

---

## Prediction tested

Open item flagged in [`23-hypogeum-spectrum-audit.md`](23-hypogeum-spectrum-audit.md): the equation's published vibrational analysis ([`03-vibrational-modes.md`](03-vibrational-modes.md)) is 2D and reports median 0.6 cycles per unit time with secondary mode locked at 1.0. The Hypogeum is a 3D cavity; the structural comparison to the Hypogeum whole-tone-scale spectrum requires the 3D vibrational analysis of the equation. This result is the first 3D extension.

## Method

Script: [`../experiments/physics/test_vibrational_3d.py`](../experiments/physics/test_vibrational_3d.py). 3D Strang split-step CuPy solver with full P1+P2+P3 triangle active, in the released-crystalline regime.

Configuration:
- N=32 (32^3 = 32,768 voxels per field).
- L=20, dt=0.005, n_steps=4000 (10 units of computational time, plus equilibration).
- $\Lambda = -8.0$, $\Sigma\lambda = 4.0$ (the 3D-rescaled total memory coupling per [`04-anti-collapse-3d.md`](04-anti-collapse-3d.md)).
- Memory hierarchy: $\nu_{\text{fast}} = 10.0$, $\nu_{\text{slow}} = 0.5$, $\lambda_{\text{fast}} = 3.0$, $\lambda_{\text{slow}} = 1.0$.
- P3 active: $\gamma_0 = 0.02$, $T_{\text{bath}} = 0.005$.

Per [`../principles/03-coupling.md`](../principles/03-coupling.md) and the wave-2-onward methodology, the test runs in the coupled regime; the 2D published spectrum in results/03 used the conservative regime ($\gamma_0 = 0$, $T = 0$), which the present methodology no longer adopts. The present 3D analysis is the methodologically correct first 3D vibrational reading.

Procedure: equilibrate for the first 1000 steps (25%), then record per-voxel density $|\Psi|^2$ every 4 steps for 3000 steps (yielding 750 samples per voxel). Per-voxel temporal FFT extracts dominant frequency. Histogram aggregates across voxels.

Hardware: RTX 4060 Laptop GPU, CUDA 13.0, CuPy backend. Wall time 13.9 seconds.

## Results

Initial norm 0.3536; final norm 22.09. The norm grew substantially during the run, indicating that thermal noise contributes non-trivially to the energy of the recorded state. The recorded spectrum is therefore partly the crystalline-state dynamics and partly thermal fluctuation. This is acknowledged as a methodological caveat and motivates further runs with smaller $T_{\text{bath}}$.

**Per-voxel dominant frequency statistics:**
- Range: 0.067 to 2.733 cycles per unit time.
- Median: 0.333.
- Mean: 0.510.
- Std: 0.475.

**Histogram top-10 most common dominant frequencies (0.1-cycle bins):**

| Bin center (cycles/unit time) | Voxel count |
|---|---|
| 0.05 | 8560 |
| 0.25 | 3735 |
| 0.45 | 2827 |
| 0.15 | 2775 |
| 0.55 | 2523 |
| 0.85 | 1951 |
| 0.35 | 1522 |
| 1.05 | 1473 |
| 1.15 | 1209 |
| 0.65 | 1096 |

The 0.05 bin (largest count, 8560 voxels) corresponds to voxels with very weak oscillation amplitude (low-density regions of the crystal where the dominant frequency identification is unreliable; the FFT picks up the largest available bin which is near-DC for these voxels). The non-trivial structure is in the bins 0.25 through 1.15.

## Comparison with 2D results/03

| | 2D (results/03, conservative) | 3D (this result, P3 active) |
|---|---|---|
| Median dominant frequency | 0.6 cycles/unit time | 0.333 cycles/unit time |
| Secondary mode | locked at 1.0 | broader, peaks at 0.85, 1.05 |
| Range | 0.1 to 7.6 | 0.067 to 2.733 |
| Methodology | conservative ($\gamma_0=0, T=0$) | coupled ($\gamma_0=0.02, T=0.005$) |

The 3D spectrum has a lower median (0.333 vs 0.6) and a broader high-frequency tail rather than a sharp locked secondary mode. This is consistent with the dimensional-rescaling argument: in 3D the focal-volume geometry differs, producing different effective restoring forces and different vibrational frequencies.

## Comparison with Wolfe-Swanson-Till 2020 Hypogeum spectrum

The Hypogeum spectrum has nine prominent peaks at 37.2-92.5 Hz forming a whole-tone scale (consecutive ratio $\approx 1.122$). Under the interface 05 calibration (9 ms per unit time), this maps to 0.33-0.83 cycles per unit time in computational units.

The 3D equation's dominant-frequency histogram has substantial counts at 0.25, 0.45, 0.55, 0.85 cycles per unit time. Selected pair ratios:

| Pair | Ratio | Whole-tone (1.122)? |
|---|---|---|
| 0.45 / 0.25 | 1.80 | no (too large) |
| 0.55 / 0.45 | 1.222 | yes, close |
| 0.85 / 0.55 | 1.545 | no |
| 1.05 / 0.85 | 1.235 | yes, close |
| 0.55 / 0.35 | 1.571 | no |
| 0.35 / 0.25 | 1.40 | no |

Some pair ratios are close to the whole-tone reference (1.222 and 1.235 vs 1.122); most are not. The 3D equation in this configuration does NOT cleanly reproduce the Hypogeum's whole-tone-scale structure as a single emergent pattern.

The honest reading: the 3D equation has multi-modal vibrational structure that overlaps the Hypogeum frequency range (0.25-0.85 cycles per unit time, mapping to 28-94 Hz under the 9 ms calibration) but does not cleanly produce the regular consecutive-ratio structure that Wolfe-Swanson-Till 2020 documented.

## Status assignment

Status: **partial / informative** with respect to the 3D vs 2D comparison; **partial / inconsistent** with respect to the Hypogeum whole-tone-scale match.

The result contributes evidence under criterion 4 (cross-domain coherence) for the dimensional difference between the equation's 2D and 3D vibrational spectra (refines the structural prediction). It does not provide clean confirmation that the equation predicts the Hypogeum's whole-tone-scale structure; that match would require either (a) a different calibration, (b) a different region of parameter space, or (c) substantive analytical work to clarify whether the whole-tone-scale is a generic feature of the equation in its 3D crystalline regime or a chamber-geometry-specific artifact at the Hypogeum.

## Honest caveats

- **Thermal noise contamination.** The final norm (22.09) is much larger than the initial norm (0.35), indicating that FDT thermal noise contributes substantially to the equilibrium state. The spectrum is therefore partly thermal fluctuation, not purely the crystalline-state dynamics. A run with smaller $T_{\text{bath}}$ (e.g., $10^{-4}$) would give a cleaner crystalline spectrum at the cost of less coupling strength.
- **N=32 may be too small.** The 2D published vibrational analysis used N=256. At N=32 in 3D, the spatial resolution may be insufficient to capture the full crystalline structure. Higher N would give a denser sampling of the vibrational modes, at the cost of GPU memory.
- **Equilibration window may be too short.** 1000 steps of equilibration (25% of the run) may not allow the crystalline state to fully form. The relaxation timescale is $1/\nu_{\text{slow}} = 2$ in computational units, i.e., 400 steps; the equilibration of 1000 steps covers 2.5 such relaxation times. A longer equilibration (10+ relaxation times) would be cleaner.
- **Single seed.** Multi-seed runs would give variance estimates on the histogram bins.
- **The "top-15 aggregate spectrum peaks" reported by the script are not physical features but the lowest 15 FFT bins** (because the aggregate spectrum is approximately monotonically decreasing in this regime). The structural information is in the per-voxel dominant-frequency histogram, not the aggregate spectrum.

## Reproducibility

```bash
LD_LIBRARY_PATH=".venv/lib/python3.11/site-packages/nvidia/cufft/lib:$LD_LIBRARY_PATH" \
  .venv/bin/python experiments/physics/test_vibrational_3d.py
```

Wall time: 13.9 seconds on RTX 4060. Output: `outputs/vibrational_3d_p3/{summary.json, freqs.npy, aggregate_spectrum.npy, dominant_freqs_per_voxel.npy, histogram.npy, bin_edges.npy}`. Seed: 42.

## Related documents

- [`03-vibrational-modes.md`](03-vibrational-modes.md): the 2D published vibrational analysis (median 0.6, secondary 1.0).
- [`23-hypogeum-spectrum-audit.md`](23-hypogeum-spectrum-audit.md): the Wolfe-Swanson-Till 2020 Hypogeum spectrum that motivated this 3D extension.
- [`../interfaces/05-archaeoacoustic-resonance.md`](../interfaces/05-archaeoacoustic-resonance.md): the interface this work feeds back into.
- [`../open-problems/01-analytical-anti-collapse.md`](../open-problems/01-analytical-anti-collapse.md): the analytical-theory open problem that should clarify whether the multi-mode whole-tone-scale is predicted by the equation's 3D crystalline regime.
