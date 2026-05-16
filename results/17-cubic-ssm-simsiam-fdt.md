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

**Status: pending GPU execution.** Script is ready to run.

| Metric | cubic_p3 ($\Lambda=-0.5$, γ=0.02) | linear_p3 ($\Lambda=0$, γ=0.02) |
|---|---|---|
| Final effective rank | _pending_ | _pending_ |
| Final uniformity | _pending_ | _pending_ |
| Final loss | _pending_ | _pending_ |

P6.3 supported if: cubic_p3 effective rank substantially higher than linear_p3.

## Status assignment

Status: **script ready, pending GPU execution**. Both variants run with P3 active per principles/03-coupling.md (Rule A); the test isolates the structural role of cubic vs linear state nonlinearity within the coupled regime.

## Honest caveats

- Synthetic clustered data, not real images.
- Single seed; multi-seed gives variance.
- Fixed P3 strength ($\gamma_0=0.02$); a P3 sweep would map the noise-dependence.
- Predictor retained; cleaner test removes predictor too.
- No comparison to standard SimSiam-with-stop-gradient (positive control).

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
