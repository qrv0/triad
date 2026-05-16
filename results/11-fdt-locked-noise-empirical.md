# Result 11: FDT-locked vs no-built-in noise in Memory-NLS training dynamics

> **METHODOLOGICAL NOTE (2026-05-16, wave 1 partial retraction).** This test is the least affected by the wave-1 methodological flaw because it specifically varies the FDT lock ($\gamma_0 > 0, T > 0$ vs $\gamma_0=0, T=0$). The variant A (FDT-locked) respects P3; variant B (no built-in noise) is the isolated degenerate. As such this test is structurally coherent with the methodology. The script is still pending GPU execution; when run, the result is interpretable per the original design.

---

## Prediction tested

Interface: [`../interfaces/06-state-space-models.md`](../interfaces/06-state-space-models.md), prediction **P6.1**.

Predicted observable: a nonlinear SSM with FDT-locked stochastic forcing in the optimization should exhibit smoother optimization-trajectory characteristics (lower variance, fewer loss spikes) than the same architecture without FDT-locked noise (or with empirically-tuned noise that does not respect the FDT correlator).

## Method

The script [`../experiments/neural/test_fdt_locked_noise.py`](../experiments/neural/test_fdt_locked_noise.py) trains two Memory-NLS language-model variants on TinyShakespeare with identical architecture (1.5M parameters, $d_{\text{model}}=192$, 4 layers, 4 memory heads) and identical training infrastructure (AdamW, cosine LR schedule, bfloat16, batch 32, sequence 256, 8000 steps), differing only in the FDT-locking of the structural noise:

- **Variant A (FDT-locked)**: dissipation $\gamma_0 = 0.02$, FDT temperature $T_{\text{FDT}} = 0.01$. The built-in FDT-locked noise from [`../implementation/neural/layer.py`](../implementation/neural/layer.py) adds noise of correlator-determined amplitude at every step.

- **Variant B (no built-in noise)**: $\gamma_0 = 0$, $T_{\text{FDT}} = 0$. Training stochasticity comes only from SGD batch sampling.

Comparison metrics:
- Trajectory variance: std of val loss across 40 checkpoint intervals (every 200 steps).
- Spike count: number of val-loss increases above 0.1 between consecutive checkpoints.
- Max loss jump: largest single-step val-loss increase.

Final val perplexity is reported for completeness but is not the primary criterion (per [`../CLAUDE.md`](../CLAUDE.md) Rule 7a).

Hardware required: PyTorch + CUDA. Wall time on RTX 4060: approximately 30-40 minutes (2 × 15-20 min runs).

## Results

**Status: pending execution.** The script is ready to run on a GPU environment with PyTorch + CUDA installed. Execution produces the comparison data populating the table below:

| Metric | Variant A (FDT-locked) | Variant B (no built-in noise) |
|---|---|---|
| Final val perplexity | _pending_ | _pending_ |
| Val loss std (across checkpoints) | _pending_ | _pending_ |
| Max loss jump | _pending_ | _pending_ |
| Spike count (Δval > 0.1) | _pending_ | _pending_ |

The script writes `outputs/fdt_locked_noise/summary.json` with the full history of both variants. After execution, this result document will be updated with the headline numbers and a status assignment.

## Status assignment

Status: **untested** (script designed and ready; awaiting GPU execution).

This is honest: the test is structured to validate or falsify P6.1 in a controlled comparison, but the actual numerical answer requires running the training on a GPU. When the user runs `python experiments/neural/test_fdt_locked_noise.py` on their full venv, the result populates and the status updates to "tested (consistent)" or "tested (inconsistent)" accordingly.

## Honest caveats

The test design has known limitations that the result interpretation must acknowledge:

- **Single seed per variant.** A multi-seed study would give variance estimates on the comparison; the current design uses seed=42 for both variants. If trajectory variance differs by less than the seed-to-seed variation, the comparison is inconclusive.

- **Specific values of $\gamma_0$ and $T_{\text{FDT}}$.** The FDT-locked variant uses $\gamma_0 = 0.02$, $T = 0.01$, chosen as moderate values for the 1.5M-scale TinyShakespeare regime. Different magnitudes could change the strength of the effect. A sweep across $\gamma_0$ values is wave-2 work.

- **"No built-in noise" vs "empirically-tuned noise" framing.** The cleanest test of P6.1 would compare FDT-locked noise against empirically-tuned noise of comparable amplitude but uncorrelated with the structural dissipation. The current test compares against zero built-in noise (with training stochasticity from SGD only). The comparison is informative but not the strictest reading of P6.1.

- **1.5M parameter scale.** The existing 70M-scale experiment in [`../results/08-optimization-collapse-empirical.md`](../results/08-optimization-collapse-empirical.md) is the canonical large-scale comparison; at 1.5M, instabilities may not manifest as dramatically.

## Reproducibility

```bash
python experiments/neural/test_fdt_locked_noise.py
```

Wall time: approximately 30-40 minutes on RTX 4060 (PyTorch + CUDA required). Output: `outputs/fdt_locked_noise/`. Random seed: 42.

## Related documents

- Interface: [`../interfaces/06-state-space-models.md`](../interfaces/06-state-space-models.md), prediction P6.1.
- Existing 70M scale-up: [`08-optimization-collapse-empirical.md`](08-optimization-collapse-empirical.md) and [`../outputs/scale_up/scale_up_results.md`](../outputs/scale_up/scale_up_results.md).
- Methodology: [`../experiments/PROTOCOLS.md`](../experiments/PROTOCOLS.md).
- FDT-locked noise implementation: [`../implementation/neural/layer.py`](../implementation/neural/layer.py).

## What populating this result implies for the program

When the user executes the script, the result either:
- Supports P6.1 (FDT-locked variant lower variance + fewer spikes): the structural prediction holds; status moves to "tested (consistent)". Wave-2 work would extend to multi-seed analysis and the cleaner "FDT-locked vs empirically-tuned" comparison.
- Locally falsifies P6.1 (no difference or FDT-locked variant has higher variance): structural prediction is challenged; status moves to "tested (inconsistent)". Per methodology/02, this shifts evidentiary weight against the specific P6.1 reading without falsifying the global structural claim of interface 06 (which rests on the mathematical equivalence of the auxiliary-field equation and the diagonal SSM update).
