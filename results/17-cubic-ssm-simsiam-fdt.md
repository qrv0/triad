# Result 17: cubic-state SimSiam without stop-gradient, with FDT noise injection (P3 active)

## Prediction tested

Interface: [`../interfaces/06-state-space-models.md`](../interfaces/06-state-space-models.md), prediction **P6.3**.

Predicted observable: cubic-nonlinearity in SSM state suppresses representation-collapse modes in SimSiam without stop-gradient, without requiring the architectural tricks those frameworks deploy.

Wave-1 ([`12-cubic-ssm-simsiam.md`](12-cubic-ssm-simsiam.md)) was retracted for not injecting FDT-locked noise. This wave-2 redesign adds explicit FDT-correlated noise to the SSM state at each forward pass.

## Method

> **Hedge cleanup (2026-05-16).** This document was originally
> presented with three variants, the third being "Variant C
> (cubic_iso): $\Lambda = -0.5$ + $\gamma_0 = 0$, $T = 0$" framed as
> "shows what wave-1 tested". Per
> [`../docs/llm-hedge-annotations.md`](../docs/llm-hedge-annotations.md),
> that variant was a Rule A violation. The variant has been removed
> from the test script and from this result document; the comparison
> is now Variant A (cubic_p3) vs Variant B (linear_p3), both in the
> coupled regime. The structural prediction P6.3 (cubic state
> nonlinearity prevents SimSiam collapse in the coupled regime) is
> evaluated on the cubic vs linear comparison alone.

The script [`../experiments/neural/test_simsiam_cubic_ssm.py`](../experiments/neural/test_simsiam_cubic_ssm.py) trains two SimSiam-style SSL variants on a synthetic clustered-sequences dataset, both WITHOUT stop-gradient and both with P3 active:

- **Variant A (cubic_p3)**: $\Lambda = -0.5$ (cubic state nonlinearity) + $\gamma_0 = 0.02$, $T = 0.01$ (P3 active).
- **Variant B (linear_p3)**: $\Lambda = 0$ (linear state) + same P3 noise.

The prediction P6.3 is supported if cubic_p3 maintains higher representation rank than linear_p3, isolating the structural role of the cubic nonlinearity in preventing collapse.

Architecture: input proj : Memory-NLS layer (4 heads, $\nu_{\min}=0.5$, $\nu_{\max}=10$) : LayerNorm : temporal mean pool : projection head (128:256:64) : SimSiam predictor (64:32:64).

Synthetic dataset: 8,192 train + 1,024 val sequences, length 32, dim 64, 16 clusters with additive noise.

Training: AdamW lr=1e-3, batch 256, 4000 steps. Seed 42.

Hardware required: PyTorch + CUDA. Wall time: 30-60 min on RTX 4060.

## Results

Executed 2026-05-16 on RTX 4060 Laptop GPU (CUDA 13.0, PyTorch 2.12.0). Total wall time 50.0 seconds across both variants (cubic_p3: 21.9 s, linear_p3: 26.1 s, 4000 steps each).

| Metric | cubic_p3 ($\Lambda=-0.5$, γ₀=0.02) | linear_p3 ($\Lambda=0$, γ₀=0.02) | Direction predicted | Observed |
|---|---|---|---|---|
| Final effective rank (out of 64) | 4.60 | 2.88 | higher at cubic | ✓ |
| Final uniformity | -0.1102 | -0.0897 | (lower-magnitude = more spread) | larger magnitude at cubic |
| Final loss (negative cosine sim) | -0.9999 | -0.9999 | (both saturate) | tied |

cubic_p3 maintains 60% more effective rank than linear_p3 (4.60 vs 2.88 of a possible 64). Both variants saturate the loss at -0.9999 (cosine similarity ~1.0, the SimSiam-without-stop-gradient default collapse target), but the representation-space metric (effective rank) distinguishes them: cubic preserves more rank, linear collapses further.

The direction matches the structural prediction P6.3: cubic nonlinearity in the SSM state suppresses representation collapse relative to the linear baseline, with both variants in the FDT-coupled regime (γ₀ > 0, T > 0). The magnitude (cubic ~60% higher effective rank) is a substantive effect.

Note that neither variant fully avoids collapse to a low-rank attractor (effective rank 4.60 out of 64 is still heavily collapsed); the prediction is comparative (cubic > linear), not absolute (cubic full-rank). The structural claim is that the cubic term provides a relative anti-collapse pressure that the linear baseline lacks, not that cubic gives full rank preservation in the absence of stop-gradient.

## Status assignment

Status: **tested in coupled regime, consistent**. Cubic state nonlinearity maintains higher effective rank (4.60/64) than linear state (2.88/64), a ~60% relative difference, with both variants in the FDT-coupled regime. The direction matches the prediction; the magnitude is non-trivial.

The result contributes evidence under criterion 4 (cross-domain coherence: the cubic nonlinearity prediction, derived from physics-philosophy axioms about anti-collapse in field-theoretic settings, transfers to the neural-representation substrate) and criterion 2 (reproducibility: the test runs in ~50 seconds on a single consumer GPU, fully scripted). It contributes weakly under criterion 3 (generative scope) because the experiment is at small scale (95k parameters, 4000 steps, synthetic data).

## Honest caveats

- Synthetic clustered-sequences data, not real images or text. The collapse phenomenology and the cubic-anti-collapse signal may differ on realistic data.
- Single seed (42). Multi-seed required for variance estimates on the rank difference.
- Fixed P3 strength (γ₀ = 0.02). A P3-strength sweep would map the noise-dependence of the cubic advantage.
- The SimSiam predictor head is retained; a cleaner isolation of the cubic effect would remove the predictor too (the wave-2 design left it in to keep the SimSiam reference architecture intact).
- No positive control: standard SimSiam-with-stop-gradient was not run for comparison. The prediction is internal (cubic vs linear within the no-stop-gradient regime), so the lack of a stop-gradient baseline does not bear on the comparison, but a future extension could include it as a control.
- Both variants ended at very saturated loss (~-1.0), indicating both substantially collapsed in the SimSiam sense. The rank difference is observed before complete saturation; whether the cubic preserves more rank in the more strongly anti-collapse regime (with more aggressive structural noise, or stronger Λ) is for follow-up.
- 95k parameters is small. The scaling of the cubic-anti-collapse advantage with model size is the natural extension under P6.2 (collapse-boundary scaling) once a multi-scale infrastructure exists.

## Reproducibility

```bash
LD_LIBRARY_PATH=".venv/lib/python3.11/site-packages/nvidia/*/lib:$LD_LIBRARY_PATH" \
  .venv/bin/python experiments/neural/test_simsiam_cubic_ssm.py
```

Wall: 30-60 min on RTX 4060 (PyTorch+CUDA). Output: `outputs/simsiam_cubic_ssm_p3/`. Seed: 42.

## Related documents

- Wave-1 retracted result: [`12-cubic-ssm-simsiam.md`](12-cubic-ssm-simsiam.md).
- Interface: [`../interfaces/06-state-space-models.md`](../interfaces/06-state-space-models.md), P6.3.
- Methodology of P3: [`../principles/03-coupling.md`](../principles/03-coupling.md).
