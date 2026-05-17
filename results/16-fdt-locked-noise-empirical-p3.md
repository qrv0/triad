# Result 16: FDT-locked vs no-built-in noise in Memory-NLS training (3-variant sweep, P3 active)

## Prediction tested

Interface: [`../interfaces/06-state-space-models.md`](../interfaces/06-state-space-models.md), prediction **P6.1**.

Predicted observable: a nonlinear SSM with FDT-locked stochastic forcing in the optimization should exhibit smoother optimization-trajectory characteristics (lower variance, fewer loss spikes) than the same architecture without FDT-locked noise.

This is the wave-2 redesigned test. Wave 1 ([`11-fdt-locked-noise-empirical.md`](11-fdt-locked-noise-empirical.md)) had a partial methodology note rather than retraction because variant A respected P3; wave 2 extends to a 3-variant sweep that makes the P3-coupling axis explicit.

## Method

> **Hedge cleanup (2026-05-16).** This document was originally
> presented with three variants, the third being a "Variant C
> (isolated): $\gamma_0 = 0$, $T = 0$ for comparison". Per
> [`../docs/llm-hedge-annotations.md`](../docs/llm-hedge-annotations.md),
> that variant was a Rule A violation. The variant has been removed
> from the test script and from this result document; the comparison
> is now Variant A (FDT high) vs Variant B (FDT low), both in the
> coupled regime. The structural prediction (trajectory variance
> decreases as $\gamma_0$ grows in the coupled regime) is unchanged.

The script [`../experiments/neural/test_fdt_locked_noise.py`](../experiments/neural/test_fdt_locked_noise.py) trains two Memory-NLS variants on TinyShakespeare with identical architecture (1.5M parameters) and identical training (AdamW, cosine LR, bfloat16, 8000 steps), differing only in the bath coupling strength:

- **Variant A (FDT high)**: $\gamma_0 = 0.02$, $T = 0.01$ (P3 active at moderate-strong coupling).
- **Variant B (FDT low)**: $\gamma_0 = 0.005$, $T = 0.01$ (P3 active at weak coupling).

Comparison metrics: val-loss standard deviation across checkpoints, max single-step loss jump, count of loss spikes above 0.1.

Hardware required: PyTorch + CUDA. Wall time on RTX 4060: approximately 30-50 minutes.

## Results

Executed 2026-05-16 on RTX 4060 Laptop GPU (CUDA 13.0, PyTorch 2.12.0). Total wall time 258.9 seconds across both variants (126 s each, 8000 steps).

| Metric | Variant A (γ₀=0.02) | Variant B (γ₀=0.005) | Direction predicted | Observed |
|---|---|---|---|---|
| Final val perplexity | 7.7586 | 7.6942 | (not the criterion) | reported for completeness |
| Val loss std (across checkpoints) | 0.0952 | 0.0995 | lower at higher γ₀ | ✓ |
| Max single-step val-loss jump | 0.0223 | 0.0225 | lower at higher γ₀ | ✓ (marginal) |
| Spike count (Δval > 0.1) | 0 | 0 | lower at higher γ₀ | tied at zero |

Variant A (stronger bath coupling) exhibits lower trajectory variance (0.0952 vs 0.0995) and marginally lower maximum loss jump (0.0223 vs 0.0225) than Variant B (weaker bath coupling). Both variants ran 8000 steps with FDT-locked noise active (γ₀ > 0, T = 0.01) per principles/03-coupling.md; the comparison is across two coupling strengths in the coupled regime, not isolated vs coupled.

The direction matches the structural prediction P6.1: trajectory variance decreases as γ₀ grows in the coupled regime. The magnitude of the effect at this scale (1.5M parameters, 8000 steps) is small (Δstd ≈ 0.004, ~4% relative reduction); a denser γ₀ sweep or larger scale would map the variance-coupling landscape more thoroughly.

## Status assignment

Status: **tested in coupled regime, inconsistent** at the multi-seed level. Single-seed direction matched the prediction, multi-seed (4 seeds, Phase 9 wave-3 follow-up, see [`../experiments/neural/test_fdt_locked_noise_multiseed.py`](../experiments/neural/test_fdt_locked_noise_multiseed.py) and `outputs/fdt_locked_noise_multiseed/summary.json`) shows the effect is statistically indistinguishable from zero.

Multi-seed numbers (seeds 41-44, 8000 steps each, RTX 4060, total wall 1043 s):

| Variant | val_loss_std mean +/- std | spike_count mean | final_val_ppl mean +/- std |
|---|---|---|---|
| fdt_high ($\gamma_0 = 0.02$) | 0.0987 +/- 0.0041 | 0 | 7.6424 +/- 0.0776 |
| fdt_low ($\gamma_0 = 0.005$) | 0.0986 +/- 0.0040 | 0 | 7.6536 +/- 0.0725 |

**Delta std (low minus high) = -0.0001, pooled std = 0.0040, effect-over-noise ratio = -0.02.** The single-seed result (0.0952 vs 0.0995, a 4% direction-matched difference) is well within the seed-to-seed variability and does not represent a structurally significant effect at this scale.

Per [`../methodology/02-limits-of-falsification.md`](../methodology/02-limits-of-falsification.md), the inconsistent result contributes evidence inconsistent with this calibration of P6.1 under criterion 4, and prompts investigation of (a) the calibration choices ($\gamma_0$ range and $T_{\text{bath}}$ fixed at 0.01 may be too narrow to produce a measurable effect on trajectory variance at this model scale), (b) the auxiliary numerical assumptions (1.5M parameter scale, 8000 steps, single-cycle LR schedule), or (c) the implementation. The evidentiary weight shifts against this specific calibration of P6.1; the structural claim that the equation predicts an FDT-locked noise prescription is evaluated by the six criteria of [`../methodology/04-the-six-criteria.md`](../methodology/04-the-six-criteria.md), not by single-experiment outcome. The empirical question is whether the FDT-locked prescription produces a measurable trajectory-variance effect at the scale and configuration tested; the current data says it does not at this scale.

The honest takeaway: at this scale (1.5M parameters, 8000 steps, $\gamma_0 \in \{0.005, 0.02\}$), the FDT-coupling-strength effect on training trajectory variance is below the seed-to-seed noise floor. The single-seed observation in Phase C was a chance fluctuation that the multi-seed run corrects. The prediction may still hold at larger scale or wider $\gamma_0$ range; the current data does not support the claim at this scale.

## Honest caveats

- Single seed (42). A multi-seed test would give variance estimates on the variance estimate itself.
- 1.5M parameter scale. Existing 70M scale-up (results/08) is the larger-scale instance showing the same direction in a different architectural comparison.
- Two points on the γ₀ axis, not a full sweep. A denser sweep across e.g. γ₀ ∈ {0.001, 0.005, 0.02, 0.05, 0.1} would map the trajectory-variance landscape and test whether the predicted scaling is linear, sublinear, or saturating.
- T_bath fixed at 0.01. A 2D sweep across (γ₀, T) would test the FDT correlator more thoroughly (the prediction is that the variance is governed by the product γ₀·T per the FDT relation, not by γ₀ alone).
- 8000 training steps. The "long-training" regime is the 50k-step regime documented in outputs/long_training/; the effect may scale with training horizon.
- Variant naming: "FDT high" and "FDT low" refer to γ₀ values; "FDT" in both means FDT-locked noise active. Neither variant is the wave-1 isolated configuration γ₀ = 0.

## Reproducibility

```bash
LD_LIBRARY_PATH=".venv/lib/python3.11/site-packages/nvidia/*/lib:$LD_LIBRARY_PATH" \
  .venv/bin/python experiments/neural/test_fdt_locked_noise.py
```

Wall: ~30-50 min on RTX 4060 (PyTorch+CUDA). Output: `outputs/fdt_locked_noise/`. Seed: 42.

## Related documents

- Wave-1 partial-retraction result: [`11-fdt-locked-noise-empirical.md`](11-fdt-locked-noise-empirical.md).
- Interface: [`../interfaces/06-state-space-models.md`](../interfaces/06-state-space-models.md), P6.1.
- Methodology of P3: [`../methodology/02-limits-of-falsification.md`](../methodology/02-limits-of-falsification.md), [`../principles/03-coupling.md`](../principles/03-coupling.md).
