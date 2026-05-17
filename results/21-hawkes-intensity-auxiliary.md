# Result 21: Hawkes exponential-kernel intensity matches auxiliary-field equation

## Prediction tested

Interface: [`../interfaces/21-hawkes-intensity.md`](../interfaces/21-hawkes-intensity.md), prediction **P21.1**.

Predicted observable: for a self-exciting Hawkes process with exponential memory kernel $\phi(\tau) = \alpha\beta e^{-\beta\tau}$, the Markov-representation SDE $d\lambda_t = -\beta(\lambda_t - \mu)\,dt + \alpha\beta\,dN_t$ (Errais-Giesecke-Goldberg) is structurally identical to the auxiliary-field equation of the present work. Closed-form intensity, simulated via Ogata thinning, and auxiliary-ODE intensity should match to within numerical precision.

## Method

The script [`../experiments/physics/test_hawkes_intensity_auxiliary.py`](../experiments/physics/test_hawkes_intensity_auxiliary.py) simulates an exponential-kernel Hawkes process via Ogata thinning, then verifies the Markov representation by comparing:

- Closed-form intensity from event history: $\lambda(t) = \mu + \sum_{t_k \le t} \alpha\beta e^{-\beta(t - t_k)}$
- Auxiliary-ODE intensity: forward Euler integration with exponential decay between events and jumps of $\alpha\beta$ at each event

**Hawkes parameters:**
- Baseline: $\mu = 1.0$
- Branching ratio: $\alpha = 0.6$ (subcritical, $n < 1$)
- Decay rate: $\beta = 2.0$
- Simulation horizon: $t_{\max} = 2000$
- Time grid: 10001 points

Statistical properties verified:
- Mean intensity (theoretical: $\mu/(1-\alpha) = 2.5$)
- Event rate (theoretical: $\mu/(1-\alpha) = 2.5$)

Backend: numpy on CPU. Wall time: 0.26 seconds.

## Results

| Quantity | Empirical | Theoretical | Relative error |
|---|---:|---:|---:|
| Intensity equivalence (closed-form vs ODE) | machine precision | exact | 5.5e-16 |
| Mean intensity | 2.499 | 2.500 | 3.0e-4 |
| Event rate | 2.49 | 2.50 | 3.4e-3 |

Events simulated: 4983 over $t_{\max} = 2000$.

The closed-form intensity (constructed from event history) and the auxiliary-ODE intensity (constructed by forward integration with jumps at event times) agree to machine precision ($5.5 \times 10^{-16}$ maximum relative error). This is the exact Markov representation in operation: the auxiliary-ODE intensity IS the closed-form intensity for the exponential-kernel Hawkes process.

Statistical convergence to theoretical mean intensity is at the level expected for ~5000 events: mean intensity within 0.03% of theoretical, event rate within 0.34%.

## Statistical analysis

The intensity equivalence at machine precision verifies the Errais-Giesecke-Goldberg Markov representation operationally: $\lambda_t$ for an exponential-kernel Hawkes process IS the auxiliary-field of the present work, with $\nu = \beta$ and stochastic forcing $\alpha\beta\,dN_t$ replacing the deterministic $\nu\rho$. The deterministic-to-stochastic substitution is exactly what makes the Hawkes correspondence Class B/C rather than Class A: the structural form of the memory equation is preserved, but the driving is a point-process counting measure rather than a continuous density field.

## Status assignment

Status: **tested, consistent**.

Rationale: the Markov representation of exponential-kernel Hawkes intensity is identical to the auxiliary-field equation in mathematical structure, verified numerically at machine precision. The statistical properties of the simulated process match theoretical predictions within stochastic uncertainty for the event count. The result contributes evidence consistent with P21.1 under criterion 4 (cross-domain coherence) and criterion 2 (reproducibility).

## What this result establishes structurally

The exponential-kernel Hawkes intensity equation, deployed across seismology (Ogata 1988 ETAS), finance (Bacry-Mastromatteo-Muzy 2015), social contagion (Crane-Sornette 2008), and neural spike modeling (Truccolo-Eden 2010), is mathematically identical to the auxiliary-field equation of the present work in the Markovian limit. The structural correspondence between interface 21 and the equation's memory subsystem is operationally established.

The result does not establish that Hawkes processes are governed by the field equation of the present work; the substrate (point process vs continuous field) differs. The correspondence is at the memory subsystem level, with the field types and driving structures distinct, as documented in [`../interfaces/21-hawkes-intensity.md`](../interfaces/21-hawkes-intensity.md).

## Honest caveats

- Single-exponential kernel only; multi-exponential kernels (the next step toward power-law / rough-kernel Hawkes) are open follow-up. Prediction P21.3 (rough-volatility kernel reproduction via Prony lift) requires explicit power-law approximation.
- Subcritical regime ($\alpha = 0.6$) only; near-critical regime ($\alpha \to 1$) probing scale-free clustering is P21.2 and remains open.
- Single seed for the Ogata thinning; multi-seed analysis would give variance bounds on the statistical convergence.

## Reproducibility

```bash
python experiments/physics/test_hawkes_intensity_auxiliary.py
```

Wall time: ~0.3 seconds on CPU. Output: `outputs/hawkes_intensity_auxiliary/summary.json`. Seed: 42.

## Related documents

- Interface: [`../interfaces/21-hawkes-intensity.md`](../interfaces/21-hawkes-intensity.md), prediction P21.1.
- Methodology grounding: [`../methodology/08-mori-zwanzig-foundation.md`](../methodology/08-mori-zwanzig-foundation.md).
- Equation: [`../equation/02-markovian-embedding.md`](../equation/02-markovian-embedding.md).
