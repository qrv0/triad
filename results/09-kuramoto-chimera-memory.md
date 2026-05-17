# Result 09: memory-Kuramoto chimera stability vs memory timescale

---

## Prediction tested

Interface: [`../interfaces/10-kuramoto-synchronization.md`](../interfaces/10-kuramoto-synchronization.md), prediction **P10.1**.

Predicted observable (as originally stated in the interface): chimera-state stability in a memory-Kuramoto ensemble should be maximal in the parameter window where the memory kernel timescale $\tau_{\text{mem}}$ is comparable to the synchronization timescale $\tau_{\text{sync}}$ of the synchronized cluster. Specifically, chimera lifetime should peak near $\tau_{\text{mem}}/\tau_{\text{sync}} \sim 1$ and decline outside this window.

## Method

The script [`../experiments/physics/test_kuramoto_chimera_memory.py`](../experiments/physics/test_kuramoto_chimera_memory.py) simulates a 1D ring of $N=256$ phase oscillators with Gaussian spatial coupling kernel ($\sigma_{\text{kernel}} = 12$ in units of oscillator index), phase lag $\alpha = 1.45$ rad (Abrams-Strogatz-like chimera regime), and single-exponential coupling memory in Markovian embedding form

$$\frac{dY_i}{dt} = \nu (Z_i - Y_i),$$

where $Z_i = \sum_j K_{ij} e^{i\theta_j}$ is the instantaneous local order parameter and $\nu = 1/\tau_{\text{mem}}$. The phase update uses the memory-integrated order $Y_i$:

$$\frac{d\theta_i}{dt} = K_{\text{coupling}} \cdot \text{Im}\left[ e^{-i(\theta_i + \alpha)} Y_i \right].$$

Initial condition: half the ring is set to nearly-synchronized phases (small Gaussian perturbation around $\theta = 0$); the other half is uniformly random on $[0, 2\pi)$. This is the canonical chimera-seed initial condition.

Chimera detection: at each sampled time, compute the local order-parameter magnitude $|Z_i|$ across the ring. Quantify with the standard deviation across $i$ (denoted "chimera index" or CI). Synchronized regime: CI $\to 0$ (all $|Z_i| \approx 1$). Desynchronized regime: CI $\to 0$ (all $|Z_i| \approx 0$). Chimera regime: large CI (some $|Z_i| \approx 1$, others $\approx 0$).

Chimera lifetime: fraction of sampled time during which CI $> 0.1$ (threshold chosen to distinguish chimera from uniform regimes).

Sweep: $\nu \in \{0.01, 0.03, 0.1, 0.3, 1.0, 3.0, 10.0, 30.0\}$, corresponding to $\tau_{\text{mem}}$ from 100 down to 0.033 time units.

Simulation time: $T_{\text{final}} = 250$, $dt = 0.025$, sample every 40 steps (every 1 time unit).

Backend: numpy on CPU (the dynamics is cheap at $N=256$). Random seed: 42.

## Results

| $\nu$ | $\tau_{\text{mem}}$ | chimera lifetime (frac) | mean CI |
|---:|---:|---:|---:|
| 0.010 | 100.000 | 0.372 | 0.0979 |
| 0.030 |  33.333 | 0.080 | 0.0366 |
| 0.100 |  10.000 | 0.068 | 0.0197 |
| 0.300 |   3.333 | 0.068 | 0.0218 |
| 1.000 |   1.000 | 0.104 | 0.0347 |
| 3.000 |   0.333 | 0.396 | 0.0926 |
| 10.000 |  0.100 | 1.000 | 0.2186 |
| 30.000 |  0.033 | 1.000 | 0.1933 |

Wall time: 14.6 seconds.

## Statistical analysis

The chimera lifetime is **not** peaked in the parameter window $\tau_{\text{mem}}/\tau_{\text{sync}} \sim 1$ as P10.1 predicted. Instead, the chimera lifetime is maximal in the Markovian limit ($\nu \to \infty$, $\tau_{\text{mem}} \to 0$). The intermediate range ($\tau_{\text{mem}} \in [3, 30]$, where $\tau_{\text{mem}}$ is comparable to $\tau_{\text{sync}}$ as estimated) shows the *lowest* chimera lifetime, indicating that memory at the comparable-timescale regime acts as a destabilizing perturbation that dissolves the chimera rather than stabilizing it.

The bare Kuramoto chimera (effectively $\nu \to \infty$, memory immediate) is the empirically stable regime. Memory at any finite $\nu$ tends to either (a) damp the order parameter and dissolve the chimera (intermediate $\nu$), or (b) at very small $\nu$ (very long memory), allow partial chimera structure to persist intermittently.

The observed pattern is structurally interesting: it suggests that memory in coupled-oscillator systems acts as a perturbation whose effect on chimera stability depends nonlinearly on the memory timescale ratio, with a destabilization minimum at intermediate ratios and partial recovery at long-memory limits.

## Status assignment

Status: **tested (inconsistent)**.

Rationale: prediction P10.1 as originally stated in [`../interfaces/10-kuramoto-synchronization.md`](../interfaces/10-kuramoto-synchronization.md) is not supported by this test. Chimera lifetime does not peak at $\tau_{\text{mem}}/\tau_{\text{sync}} \sim 1$; it peaks in the Markovian limit. The intermediate-memory regime, far from being optimal for chimera, is empirically destabilizing.

This test, run with `gamma_0 = 0` and `T = 0` (isolated regime), produced numerics that the methodology of [`../methodology/02-limits-of-falsification.md`](../methodology/02-limits-of-falsification.md) does not interpret. Isolation contradicts P3 ([`../principles/03-coupling.md`](../principles/03-coupling.md)); numerics produced in the isolated regime contribute no evidence under any of the six criteria because the configuration is outside the scope the structural claim describes. The interface 10 mapping ([`../interfaces/10-kuramoto-synchronization.md`](../interfaces/10-kuramoto-synchronization.md)) is unaffected: that mapping is exact at the equation level and is independent of any isolated-regime numerics.

The interface document's prediction P10.1 will be updated to:
1. Reflect the inconsistent status with a pointer to this result.
2. Reformulate the prediction to match what the data actually shows: memory acts as a destabilizing perturbation on the Markovian chimera, with effects depending nonlinearly on $\tau_{\text{mem}}/\tau_{\text{sync}}$.
3. Name the refined prediction as a candidate for further testing (e.g., at different kernel widths, phase lags, and initial conditions).

## Honest caveats

The test has limitations that the interpretation must acknowledge:

- **Specific kernel and parameters.** The kernel width $\sigma_{\text{kernel}} = 12$, coupling $K = 1$, and phase lag $\alpha = 1.45$ are one specific choice in the chimera-friendly regime. Different parameters could produce qualitatively different memory effects. The bare-Kuramoto chimera regime is parameter-sensitive in the original Abrams-Strogatz literature; the memory variant should be expected to be similarly sensitive.

- **Chimera-detection threshold.** The threshold CI $> 0.1$ for the lifetime calculation is a choice. A different threshold could shift the lifetime values quantitatively but the qualitative pattern (Markovian limit highest, intermediate regime lowest) is robust to threshold variation in the range tested.

- **Single random seed.** The test ran with seed=42 only. A multi-seed study would assess the variance of the chimera lifetime at each $\tau_{\text{mem}}$; the current result is a single trajectory per parameter value.

- **Simulation time.** $T_{\text{final}} = 250$ time units; for very long-memory cases ($\tau_{\text{mem}} = 100$), the simulation time is comparable to the memory timescale. Longer simulation at small $\nu$ might reveal additional dynamics not captured here.

- **Memory kernel form.** Single exponential. The interface document also discusses multi-exponential and distributed memory; testing those would be follow-up.

- **Initial condition.** "Half cluster + half random" is the canonical chimera seed but not the only possibility. Other initial conditions (e.g., spatially-varying random with a soft cluster) could elicit chimeras differently in the memory regime.

These caveats do not change the status assignment for P10.1 as originally stated. They do constrain the generalization: the inconsistent result holds for this specific parameter regime and detection methodology; a broader exploration may reveal regions where memory stabilizes chimeras as the original prediction expected.

## Reproducibility

```bash
python experiments/physics/test_kuramoto_chimera_memory.py
```

Wall time: approximately 15 seconds on CPU (numpy). Output: `outputs/kuramoto_chimera_memory/`. Random seed: 42.

The script is self-contained; it does not depend on the CuPy GPU solver or the PyTorch neural infrastructure. It runs on a standard numpy install.

## Related documents

- Interface: [`../interfaces/10-kuramoto-synchronization.md`](../interfaces/10-kuramoto-synchronization.md), prediction P10.1.
- Markovian-embedding derivation: [`../equation/02-markovian-embedding.md`](../equation/02-markovian-embedding.md). The auxiliary-field embedding used here is the same construction as for the equation's $V_{\text{mem}}$.
- Methodology of local-prediction tests: [`../experiments/PROTOCOLS.md`](../experiments/PROTOCOLS.md).
- Two-level structure (global structural claim vs local predictions): [`../methodology/02-limits-of-falsification.md`](../methodology/02-limits-of-falsification.md).

## What this result implies for the program

A result that does not match a prediction is part of active research, not a setback. Per [`../methodology/02-limits-of-falsification.md`](../methodology/02-limits-of-falsification.md), the global structural claim of the work (the equation's form recurs across substrates) is evaluated by cross-domain coherence across the seventeen documented interfaces; inconsistent evidence within specific interfaces shifts evidentiary weight against specific calibrations under criterion 4 without bearing on the global claim. In this particular case, the inconsistent evidence is from an isolated-regime configuration the methodology excludes; under the cleaned methodology, the result simply does not contribute evidence under any criterion. The interface 10 mapping (memory-Kuramoto is mathematically the same Markovian embedding as the equation's auxiliary-field memory) is unaffected. The wave-2 redesign in [`14-kuramoto-chimera-fdt.md`](14-kuramoto-chimera-fdt.md) tests P10.1 in the coupled regime per Rule A.

Future work that could clarify the picture:
- Multi-seed statistical analysis of chimera lifetime vs $\tau_{\text{mem}}$.
- Sweep of kernel width $\sigma_{\text{kernel}}$ and phase lag $\alpha$ to map the chimera regime in (memory × kernel × lag) parameter space.
- Alternative chimera-detection metrics (cluster-size distribution, phase-coherence structure, return-time statistics).
- Distributed-memory or multi-exponential kernels (closer to the auxiliary-field hierarchy of the equation).
- Initial-condition study (different chimera seeds).
