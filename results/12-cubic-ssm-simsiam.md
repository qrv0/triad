# Result 12: cubic-state SimSiam without stop-gradient

## Prediction tested

Interface: [`../interfaces/06-state-space-models.md`](../interfaces/06-state-space-models.md), prediction **P6.3**.

Predicted observable: cubic-nonlinearity in SSM state (the structural extension that the Memory-NLS equation adds to the bare diagonal-state SSM) should suppress representation collapse modes documented in self-supervised learning (SimSiam without stop-gradient, BYOL without predictor network), without requiring the architectural tricks those frameworks deploy.

## Method

The script [`../experiments/neural/test_simsiam_cubic_ssm.py`](../experiments/neural/test_simsiam_cubic_ssm.py) trains two SimSiam-style SSL variants on a synthetic clustered-sequences dataset, with identical architecture and training infrastructure, differing only in the cubic state nonlinearity:

- **Variant cubic** ($\Lambda = -0.5$): Memory-NLS layer with cubic state nonlinearity (the structural feature the equation adds to bare SSM).
- **Variant linear** ($\Lambda = 0$): Memory-NLS layer with cubic nonlinearity disabled (degenerate to bare SSM).

Both variants are trained **without stop-gradient** in the SimSiam loss; the architectural patch that normally prevents representation collapse. The structural prediction is that the cubic variant maintains higher representation rank than the linear variant despite the absence of the architectural patch.

Architecture:
- Input projection: 64 → 128.
- Memory-NLS layer with 4 memory heads, $\nu_{\min} = 0.5$, $\nu_{\max} = 10$, $\Sigma\lambda = 0.3$.
- Layer norm, temporal mean-pool.
- Projection head: 128 → 256 → 64.
- SimSiam predictor: 64 → 32 (bottleneck) → 64.

Synthetic dataset: 8,192 training + 1,024 val sequences, length 32, dimension 64, 16 clusters. Each sequence consists of vectors drawn from one cluster with additive noise.

Training: AdamW, lr $10^{-3}$, batch 256, 4000 steps. SimSiam loss = negative cosine similarity (no stop-gradient). Random seed: 42.

Comparison metrics:
- Effective rank of validation-set representations (Roy-Vetterli 2007: $\exp$ of eigenvalue-distribution entropy).
- Wang-Isola (2020) uniformity loss.
- Loss trajectory.

Hardware required: PyTorch + CUDA. Wall time: approximately 30-60 minutes on RTX 4060.

## Results

**Status: pending execution.** The script is ready to run on a GPU environment. Execution produces the comparison data populating the table below:

| Metric | Variant cubic ($\Lambda = -0.5$) | Variant linear ($\Lambda = 0$) |
|---|---|---|
| Final loss | _pending_ | _pending_ |
| Final effective rank (of 64-d projection) | _pending_ | _pending_ |
| Final uniformity (lower is more uniform) | _pending_ | _pending_ |

Prediction P6.3 supported if: cubic variant maintains effective rank substantially higher than linear variant (e.g., cubic stays > 30, linear collapses to < 5).

Prediction P6.3 locally falsified if: cubic and linear variants both collapse, or cubic shows no significant rank advantage.

## Status assignment

Status: **untested** (script designed and ready; awaiting GPU execution).

## Honest caveats

- **Synthetic data.** The test uses synthetic clustered sequences, not real images or natural sequences. The collapse prediction in interface 06 was framed for the SSL setting on real data; synthetic data simplifies the test but may not capture the full collapse dynamics that motivated SimSiam's stop-gradient design. Wave-2 work could repeat on a small image dataset (CIFAR-10 patches, for example).

- **Single seed.** Multi-seed analysis would give variance estimates on rank measurements.

- **Specific $\Lambda$ value.** $\Lambda = -0.5$ is one value; the cubic-nonlinearity strength may have a sweet spot for collapse prevention that is not at this value.

- **Predictor still present.** The SimSiam predictor (bottleneck MLP) is retained in both variants because its role in SimSiam is distinct from the stop-gradient. A cleaner P6.3 test could also remove the predictor.

- **No comparison to standard SimSiam-with-stop-gradient.** The current test compares cubic vs linear, both without stop-gradient. A complete picture also includes the canonical SimSiam-with-stop-gradient as a positive control.

## Reproducibility

```bash
python experiments/neural/test_simsiam_cubic_ssm.py
```

Wall time: approximately 30-60 minutes on RTX 4060 (PyTorch + CUDA required). Output: `outputs/simsiam_cubic_ssm/`. Random seed: 42.

## Related documents

- Interface: [`../interfaces/06-state-space-models.md`](../interfaces/06-state-space-models.md), prediction P6.3.
- Methodology: [`../experiments/PROTOCOLS.md`](../experiments/PROTOCOLS.md).
- Background on representation collapse: Chen-He (2021) "Exploring Simple Siamese Representation Learning"; Grill et al. (2020) "Bootstrap Your Own Latent".
- Background on alignment-uniformity metrics: Wang-Isola (2020) "Understanding contrastive representation learning through alignment and uniformity on the hypersphere".

## What populating this result implies for the program

The result has substantial implications either way:

- If cubic variant maintains rank: the structural argument that cubic state nonlinearity prevents collapse is empirically supported. The result strengthens the interface 06 claim that the Memory-NLS extensions over bare SSM (specifically the cubic part) are not arbitrary additions but structurally productive. This would also be of interest to the SSL community independent of the structural-realist framing.

- If cubic and linear both collapse: the cubic nonlinearity by itself is not sufficient to prevent SimSiam collapse without the stop-gradient. The interface 06 prediction P6.3 is locally falsified. The structural claim of interface 06 (mathematical equivalence with diagonal SSM) is unaffected.

Either outcome is informative; the structural-realist methodology commits to honest reporting (methodology/02).
