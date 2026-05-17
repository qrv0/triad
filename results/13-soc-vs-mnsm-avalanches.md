# Result 13: SOC sandpile vs MNSM release-regime avalanche statistics

---

## Prediction tested

Interface: [`../interfaces/14-self-organized-criticality.md`](../interfaces/14-self-organized-criticality.md), prediction **P14.2**.

Predicted observable (as stated in the interface): the equation's release-regime avalanche-size distributions, when simulated with appropriate parameters, should be statistically indistinguishable from BTW sandpile distributions at matching substrate parameters; the critical exponent should be in the SOC universality range.

## Method

The script [`../experiments/physics/test_soc_vs_mnsm_avalanches.py`](../experiments/physics/test_soc_vs_mnsm_avalanches.py) compares two substrates side by side:

**BTW sandpile (reference SOC system):** 2D grid $64 \times 64$, threshold = 4, dissipative boundary, 15,000 random drive events. Each drive event adds one grain to a random cell; relaxation toppling continues until the lattice is stable; avalanche size is the count of toppling events during one relaxation cycle.

**MNSM 2D in released regime:** $N = 64$, $L = 10$, $\Lambda = -8$, $\Sigma\lambda = 2$, multi-mode memory $(\nu_{\text{fast}}, \nu_{\text{slow}}) = (10, 0.5)$, $\sigma_{\text{init}} = 0.4$. Warmup of 2000 Strang split-step time steps to reach the released-crystalline regime, then 8000 recording steps with small Gaussian perturbations applied every 200 steps at random locations. The peak-density time series is recorded; "avalanches" are defined as contiguous excursions of peak density above a threshold (median peak × 1.05); avalanche size is the time-integrated excursion above threshold.

Statistical analysis uses the Clauset-Shalizi-Newman (2009) maximum-likelihood estimator for the power-law exponent $\tau$, with $x_{\min}$ set to the substrate's minimum-resolvable avalanche scale (4 for BTW, 0.001 for MNSM).

Wall time: 5 seconds total (BTW: 3 s, MNSM: 2 s).

Backend: numpy (CPU). Random seed: 42.

## Results

| Substrate | n_avalanches | $\tau$ (MLE) | $x_{\min}$ | size median | size max |
|---|---:|---:|---:|---:|---:|
| BTW sandpile (2D, $64\times64$) | 3,840 | **1.37** | 4 | 7 | 1,142 |
| MNSM release regime ($N=64$, $\Lambda=-8$, $\Sigma\lambda=2$) | 25 | **1.13** | 0.001 | (varies) | (varies) |

Reference BTW critical exponent from the literature: $\tau \sim 1.0$ to $1.2$ (Manna 1991 and subsequent work; statistical caveats from Clauset-Shalizi-Newman 2009 apply).

## Statistical analysis

The two substrates produce power-law-like avalanche-size distributions with exponents in the same general range ($\tau \sim 1.1$ to $1.4$). The BTW result ($\tau = 1.37$) is slightly above the canonical literature range of $1.0$-$1.2$ but within the broader range often reported for finite-size BTW with dissipative boundaries. The MNSM result ($\tau = 1.13$) is in the literature-canonical range.

The comparison is suggestive but limited by:

- **Sparse MNSM event count.** The MNSM regime produced only 25 detected avalanches in 8000 simulation steps. The Clauset-Shalizi-Newman methodology requires $n \gtrsim 100$ for confident exponent estimation. The MNSM exponent estimate $\tau = 1.13$ carries substantial uncertainty.

- **Differing avalanche definitions.** BTW avalanches are discrete-event topplings during one drive cycle. MNSM "avalanches" are continuous excursions of an analog field above a threshold. Although both are scale-free phenomena, the unit-of-event differs between the substrates. A fair comparison would require either (a) discretizing MNSM events at matched scale, or (b) using a spatial-extent-based definition for both.

- **Specific parameter regime.** The MNSM parameters $(\Lambda = -8, \Sigma\lambda = 2)$ are in the released regime but not optimized for maximal avalanche production. Different $\Sigma\lambda$ or different perturbation amplitudes could produce more events.

## Status assignment

Status: **partially tested (consistent at coarse level)**.

Rationale: both substrates produce power-law-like avalanche-size distributions with exponents in the broadband-criticality range ($\tau \in [1.0, 1.5]$). This is the qualitative consistency the prediction P14.2 requires at the "broadly compatible with SOC universality" level. The result does not provide strong statistical evidence at the "statistically indistinguishable" strength claimed by the most demanding version of P14.2; this would require an MNSM event count comparable to BTW's ($\gtrsim 1000$), which the current parameter regime did not produce.

The result is consistent with the structural prediction at the mechanism-shape level (both substrates show power-law-like response) without confirming statistical indistinguishability at the exponent level.

## Honest caveats

- **Single parameter point per substrate.** No sweep across $\Sigma\lambda$ or perturbation amplitude in MNSM; no sweep across grid size or threshold in BTW. A proper power-law-vs-power-law comparison requires both substrates to be in their respective scaling regimes and well-characterized statistically.

- **2D vs 3D.** The result is for 2D substrates (computational tractability on CPU). The interface-14 prediction does not specify dimension; 3D substrates may give different exponents (BTW has $\tau \approx 1.2$ in 3D; MNSM 3D would need GPU compute).

- **Power-law fitting.** The MLE $\tau$ is sensitive to the choice of $x_{\min}$. Statistical robustness requires the Clauset-Shalizi-Newman bootstrap procedure that this test does not implement; the reported $\tau$ values are point estimates without confidence intervals.

- **MNSM avalanche definition.** "Excursion of peak density above threshold" is one of several possible avalanche-detection methods. Alternatives (spatial-cluster-size at fixed time, spatiotemporal cluster integration, response-to-impulse statistics) might give different exponents.

- **CPU numpy.** The MNSM simulation runs in numpy on CPU at $N=64$, $T_{\text{total}} = 50$. The dynamics is well-resolved but small-scale; a larger-scale GPU run (the existing CuPy 3D solver could be adapted) would produce both more events and richer statistics.

## Reproducibility

```bash
python experiments/physics/test_soc_vs_mnsm_avalanches.py
```

Wall time: approximately 5 seconds on CPU. Output: `outputs/soc_vs_mnsm_avalanches/`. Random seed: 42.

## Related documents

- Interface: [`../interfaces/14-self-organized-criticality.md`](../interfaces/14-self-organized-criticality.md), prediction P14.2.
- Adjacent interface: [`../interfaces/09-critical-brain.md`](../interfaces/09-critical-brain.md) (broadband phenomenology that the same MNSM regime produces).
- Methodology: [`../experiments/PROTOCOLS.md`](../experiments/PROTOCOLS.md).
- Statistical methodology: Clauset, A., Shalizi, C. R., & Newman, M. E. J. (2009). Power-law distributions in empirical data. *SIAM Review* **51**, 661.

## What this result implies for the program

The result moves P14.2 from "untested" to "partially tested (consistent at coarse level)". The structural mechanism the prediction articulates (broadband-criticality-like avalanche phenomenology in the released MNSM regime, comparable to SOC sandpile statistics) survives the comparison at the order-of-magnitude level. A more demanding test (statistical indistinguishability at $1\sigma$) requires:

1. Richer MNSM event statistics ($\gtrsim 1000$ events; achieved by longer runs, smaller perturbation period, or different parameter regime).
2. Matched avalanche-definition methodology (the same operational definition applied to both substrates).
3. 3D substrates for both.
4. Bootstrap confidence intervals on $\tau$.

This is documented as wave-2 work in [`../RESEARCH-AGENDA.md`](../RESEARCH-AGENDA.md). The current test establishes the coarse consistency and the methodology; refinement is iterative.
