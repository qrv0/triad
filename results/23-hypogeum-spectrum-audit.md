# Result 23: Hypogeum frequency spectrum audit and partial-evidence on P5.3

## Prediction tested (partially)

Interface: [`../interfaces/05-archaeoacoustic-resonance.md`](../interfaces/05-archaeoacoustic-resonance.md), prediction **P5.3** (frequency-ratio invariance across chamber sizes).

The P5.3 prediction is that the 0.6:1.0 ratio between the equation's two principal modes is structural and should be preserved across chambers of different physical dimensions under appropriate dimensional rescaling.

## Method

This result is a literature audit, not a numerical simulation. The most recent and highest-resolution rigorous-floor data on megalithic chamber acoustic spectra is Wolfe, Swanson and Till (2020), *Journal of Archaeological Science: Reports* 34: 102623 (arXiv:2010.13697), which extends the Till (2017) *Antiquity* swept-sine impulse-response measurements at the Ħal Saflieni Hypogeum middle level with 3D wave-equation simulation of the laser-scanned chamber geometry.

The frequency peaks reported in Wolfe-Swanson-Till 2020 for the Hypogeum middle level (averaged across chambers 18, 20, 24, 25, 26, 27 in the mean Hypogeum-wide spectrum) were extracted directly from the published Table 1 and Section 3 results. Pair ratios within the spectrum were computed and compared against the P5.3 structural prediction.

The Jahn-Devereux-Ibison 1996 *Journal of the Acoustical Society of America* survey of six British/Irish chambered tombs reports one dominant peak per chamber in the 95-120 Hz band, with no within-chamber pair data. Cross-chamber pair-ratio testing therefore cannot draw on that source.

## Results

Wolfe-Swanson-Till 2020 report nine prominent low-frequency peaks in the Hypogeum-wide mean spectrum (low-frequency band, below 100 Hz):

| Peak # | Frequency (Hz) | Cumulative ratio from 37.2 |
|---|---|---|
| 1 | 37.2 | 1.000 |
| 2 | 41.0 | 1.102 |
| 3 | 46.1 | 1.239 |
| 4 | 50.4 | 1.355 |
| 5 | 57.1 | 1.535 |
| 6 | 64.3 | 1.728 |
| 7 | 72.7 | 1.954 |
| 8 | 81.8 | 2.199 |
| 9 | 92.5 | 2.486 |

The consecutive-peak ratio is approximately **1.122** at every step:

| Consecutive pair | Ratio |
|---|---|
| 37.2 → 41.0 | 1.102 |
| 41.0 → 46.1 | 1.124 |
| 46.1 → 50.4 | 1.093 |
| 50.4 → 57.1 | 1.133 |
| 57.1 → 64.3 | 1.126 |
| 64.3 → 72.7 | 1.131 |
| 72.7 → 81.8 | 1.125 |
| 81.8 → 92.5 | 1.131 |
| **Mean** | **1.123 ± 0.014** |

A whole-tone musical interval has frequency ratio $2^{2/12} \approx 1.122$. The Hypogeum peaks form a near-perfect whole-tone scale across two octaves, which is the central empirical finding of Wolfe-Swanson-Till 2020 (their Section 3 and Figure 4).

## Bearing on P5.3

The P5.3 prediction states a 0.6:1.0 ratio between two principal modes. The Hypogeum has nine modes, not two, with a constant consecutive ratio of 1.122 (whole-tone), not a 0.6:1.0 split. The match is not exact.

However, several non-consecutive pair ratios in the Hypogeum spectrum do cluster near 0.6:

| Pair | Ratio | Distance from 0.6 |
|---|---|---|
| 37.2 / 64.3 | 0.578 | 0.022 |
| 41.0 / 64.3 | 0.638 | 0.038 |
| 41.0 / 72.7 | 0.564 | 0.036 |
| 50.4 / 92.5 | 0.545 | 0.055 |
| 57.1 / 92.5 | 0.617 | 0.017 |

The pairs with ratios closest to 0.6 are those separated by four consecutive whole-tone steps (ratio $1.122^4 \approx 1.587$, inverse $\approx 0.630$) and five steps (ratio $1.122^5 \approx 1.782$, inverse $\approx 0.561$). The structural prediction's 0.6 ratio corresponds approximately to a four-to-five whole-tone interval in the Hypogeum spectrum.

The structural prediction was derived from the 2D crystalline regime of the equation, which produces two principal modes at 0.6 and 1.0 cycles per unit time per [`../results/03-vibrational-modes.md`](03-vibrational-modes.md). The Hypogeum is a 3D cavity; its spectrum being richer than the 2D two-mode prediction is consistent with the dimensional difference. The dimensional rescaling at higher d documented in [`../results/06-dimensional-rescaling.md`](06-dimensional-rescaling.md) and [`../results/10-dimensional-rescaling-higher-d.md`](10-dimensional-rescaling-higher-d.md) suggests the spectrum structure is not preserved across dimensions; higher dimensions are expected to produce richer spectra.

## Status assignment

Status: **partial**. The empirical pattern at the Hypogeum (nine-peak whole-tone scale) is richer than the equation's 2D two-mode prediction. Pair ratios near 0.6 do appear within the Hypogeum spectrum but are not the only pattern. The cross-chamber ratio invariance part of P5.3 cannot be tested with current rigorous-floor data: the Jahn 1996 chambers have only single dominant peaks per chamber reported, and the Wolfe-Swanson-Till 2020 high-resolution methodology has been applied only to the Hypogeum.

The result contributes evidence under criterion 4 (cross-domain coherence: a multi-mode broadband-resonance phenomenology with regular interval structure is consistent with the equation's broadband-absorbing crystalline regime) and contributes a refinement target for the analytical theory of [`../open-problems/01-analytical-anti-collapse.md`](../open-problems/01-analytical-anti-collapse.md): the 3D vibrational spectrum of the equation, beyond the 2D two-mode result, should be derived analytically to clarify whether the equation predicts the whole-tone-scale structure or whether the structural prediction needs revision.

## Honest caveats

- Only one chamber complex has been measured at the high resolution of Wolfe-Swanson-Till 2020. Cross-chamber pair-ratio testing requires the same methodology applied to additional sites; the Jahn 1996 single-peak reports do not suffice.
- The amplitude weights of the nine Hypogeum peaks were not extracted in this audit. If amplitudes weight some peaks heavily over others, the "two principal modes" interpretation in P5.3 may apply if the spectrum has two amplitude-dominant peaks among the nine.
- The whole-tone scale finding is itself a substantive observation that may indicate a more sophisticated structural prediction is available from the equation than the two-mode prediction currently in interface 05. This is flagged as analytical work for [`../open-problems/01-analytical-anti-collapse.md`](../open-problems/01-analytical-anti-collapse.md).
- The 2D vs 3D dimensional difference between the equation's published vibrational analysis ([`03-vibrational-modes.md`](03-vibrational-modes.md), 2D) and the Hypogeum substrate (3D cavity) may explain part of the structural mismatch. A 3D vibrational analysis of the equation would be needed for direct comparison.

## Implications for interface 05

The Wolfe-Swanson-Till 2020 whole-tone scale finding strengthens the structural correspondence at the level of "broadband regular-interval spectrum" but weakens the specific "two-mode 0.6:1.0" prediction P5.3. Interface 05's structural claim should be updated to acknowledge:

1. The Hypogeum spectrum is multi-modal (nine peaks), not two-modal.
2. The consecutive-peak ratio is the whole-tone $\approx 1.122$, a constant ratio across the spectrum, not a 0.6:1.0 single split.
3. Pair ratios near 0.6 do appear within the spectrum (four-to-five whole-tone intervals); the structural prediction is therefore not absent, but the framing as "two principal modes" needs refinement to a "multi-mode constant-ratio" framing.
4. The analytical task is to derive the 3D vibrational spectrum of the equation and check whether it predicts the whole-tone or a different multi-mode pattern.

This update is best done as a future analytical-theory pass once the 3D vibrational analysis is available; the current interface text is preserved as the calibration-dependent reading consistent with what was published at the time it was written.

## Reproducibility

The data extraction in this audit is from Wolfe, Swanson and Till (2020) *Journal of Archaeological Science: Reports* 34: 102623, Section 3 and Table 1. The arXiv version is 2010.13697 (October 2020), accessible at https://arxiv.org/abs/2010.13697. Page 3 of the preprint lists the prominent frequency peaks as quoted above.

Ratio computations are arithmetic from the listed peak frequencies; no separate code was needed.

## Related documents

- Interface: [`../interfaces/05-archaeoacoustic-resonance.md`](../interfaces/05-archaeoacoustic-resonance.md), P5.3.
- Source: Wolfe, K., Swanson, D., & Till, R. (2020). The frequency spectrum and geometry of the Ħal Saflieni Hypogeum appear tuned. *Journal of Archaeological Science: Reports* **34**, 102623. arXiv:2010.13697.
- Adjacent: [`../results/03-vibrational-modes.md`](03-vibrational-modes.md) (the equation's 2D two-mode prediction), [`../open-problems/01-analytical-anti-collapse.md`](../open-problems/01-analytical-anti-collapse.md) (the analytical-theory open problem that would extend the vibrational analysis to 3D).
