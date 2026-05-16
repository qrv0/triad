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

**Status: pending GPU execution.** Script is ready to run.

| Metric | Variant A (γ=0.02) | Variant B (γ=0.005) |
|---|---|---|
| Final val perplexity | _pending_ | _pending_ |
| Val loss std | _pending_ | _pending_ |
| Max loss jump | _pending_ | _pending_ |
| Spike count (Δval>0.1) | _pending_ | _pending_ |

After execution, the prediction is supported if trajectory variance is LOWER in Variant A (stronger coupling) than in Variant B (weaker coupling), per the structural reading that bath coupling stabilizes training trajectories.

## Status assignment

Status: **script ready, pending GPU execution**. Both variants run in the coupled regime per principles/03-coupling.md (Rule A); the test compares trajectory variance across two coupling strengths.

## Honest caveats

- Single seed; multi-seed gives variance estimates.
- 1.5M scale; existing 70M scale-up (results/08) is the larger-scale instance.
- Three points on the $\gamma_0$ axis; a denser sweep would map the trajectory-variance landscape.
- $T_{\text{bath}}$ fixed at 0.01; sweep across $T$ would give 2D map.

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
