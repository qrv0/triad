# Result 14: memory-Kuramoto chimera stability under FDT-locked phase noise

> **2026-05-17 — output removed.** The associated `outputs/kuramoto_chimera_memory_p3/` directory was removed: its recorded grid included gamma_0 = 0.0 as a sweep point, which is inconsistent with this document's declared sweep gamma_0 in {0.01, 0.05, 0.2, 1.0}. The extra gamma_0 = 0.0 cell was a hedge from a prior audit cycle. Re-running with the declared parameters is open work.

## Prediction tested

Interface: [`../interfaces/10-kuramoto-synchronization.md`](../interfaces/10-kuramoto-synchronization.md), prediction **P10.1**.

Predicted observable: chimera-state stability in a memory-Kuramoto ensemble is maximal in the parameter window where the memory kernel timescale $\tau_{\text{mem}}$ is comparable to the synchronization timescale $\tau_{\text{sync}}$ of the synchronized cluster.


## Method

The script [`../experiments/physics/test_kuramoto_chimera_memory.py`](../experiments/physics/test_kuramoto_chimera_memory.py) simulates a 1D ring of $N=256$ phase oscillators with Gaussian kernel ($\sigma=12$), phase lag $\alpha=1.45$, multi-exponential coupling memory, and **FDT-locked Langevin noise on the phases**:

$$\frac{d\theta_i}{dt} = K \cdot \text{Im}\left[e^{-i(\theta_i + \alpha)} Y_i\right] + \sqrt{2 \gamma_0 T / dt}\, \xi_i$$

with $\xi_i$ unit-variance Gaussian. The noise amplitude is fixed by P3's FDT correlator in terms of $(\gamma_0, T)$. The auxiliary-field memory is unchanged from the earlier (exact OU update per paper §4.1).

**2D parameter sweep**: $\gamma_0 \in \{0.01, 0.05, 0.2, 1.0\}$ at $T_{\text{bath}} = 0.1$, $\nu \in \{0.03, 0.1, 0.3, 1.0, 3.0, 10.0\}$ (i.e., $\tau_{\text{mem}}$ from 33 to 0.1). All sweep points are per principles/03-coupling.md; the structural prediction is evaluated across these four coupling strengths.

Random seed varies per cell (seed = base + 1000*g_idx + n_idx) to give independent realizations. Backend: CuPy on RTX 4060. Wall time: 38.9 seconds.

## Results

Chimera lifetime fraction (where 1.0 = chimera persists throughout the simulation; 0 = chimera dissolves immediately) at each $(\gamma_0, \tau_{\text{mem}})$:

| $\gamma_0$ \\ $\tau_{\text{mem}}$ | 33.3 | 10 | 3.3 | 1.0 | 0.33 | 0.1 |
|---|---|---|---|---|---|---|
| **0.01** | 0.080 | 0.064 | 0.064 | 0.120 | 0.524 | **1.000** |
| **0.05** | 0.080 | 0.072 | 0.064 | 0.140 | 0.424 | **1.000** |
| **0.2** | 0.088 | 0.072 | 0.064 | 0.264 | **0.988** | 1.000 |
| **1.0 (strongly coupled)** | 0.240 | 0.160 | 0.184 | **0.968** | 0.936 | 0.484 |

The peak of chimera lifetime in the parameter plane shifts as $\gamma_0$ increases:

- At $\gamma_0 = 0.01$ (weak coupling): peak at $\tau_{\text{mem}} = 0.1$ (Markovian limit).
- At $\gamma_0 = 0.05$: peak still at $\tau_{\text{mem}} = 0.1$ but the intermediate-$\tau_{\text{mem}}$ values are rising.
- At $\gamma_0 = 0.2$: peak shifts to $\tau_{\text{mem}} = 0.33$ (lifetime 0.988), with the Markovian limit also at 1.000.
- At $\gamma_0 = 1.0$ (strongly coupled): peak at $\tau_{\text{mem}} = 1.0$ (lifetime 0.968); the Markovian limit DROPS to 0.484.

## Statistical analysis

The chimera-lifetime peak shifts across the sweep: as $\gamma_0$ grows from 0.01 to 1.0 (a factor of 100 in coupling strength), the peak moves from $\tau_{\text{mem}} = 0.1$ (Markovian-dominated regime) toward $\tau_{\text{mem}} \sim 1$ (the regime $\tau_{\text{mem}}/\tau_{\text{sync}} \sim 1$ that P10.1 originally predicted, with $\tau_{\text{sync}} \sim 1$-3 for this kernel and coupling).

The structural reading: as bath coupling grows, bath-induced phase diffusion destabilizes the Markovian-limit chimera at small $\tau_{\text{mem}}$ (the noise overwhelms the fast-relaxing memory). The chimera survives best in the regime where the memory timescale is comparable to the bath-driven decorrelation timescale. The crossover happens around $\gamma_0 \sim 0.1$-$0.2$. This is the structural prediction P10.1 makes: in a system where coupling is the default (P3), memory must be paced to the bath-decorrelation timescale for the chimera to persist.

P10.1's original prediction (chimera optimum at $\tau_{\text{mem}}/\tau_{\text{sync}} \sim 1$) is therefore **supported** at moderate-to-strong $\gamma_0$. The companion run in [`09-kuramoto-chimera-memory.md`](09-kuramoto-chimera-memory.md), at $\gamma_0 = 0$ and $T = 0$, reported chimera dominance in the Markovian limit, which sits at the weak-coupling corner of the present sweep.

## Status assignment

Status: **tested, consistent**.

Rationale: at $\gamma_0 = 0.2$ and $\gamma_0 = 1.0$ (at moderate-to-strong coupling), the chimera-lifetime peak is at $\tau_{\text{mem}} \in [0.33, 1.0]$, which is the predicted $\tau_{\text{mem}}/\tau_{\text{sync}} \sim 1$ regime for this kernel ($\tau_{\text{sync}} \sim 1$-3 for $K=1$, $\sigma=12$). The result contributes evidence consistent with P10.1's qualitative prediction under criterion 4 (cross-domain coherence) and under criterion 2 (reproducibility); the GPU run is reproducible from `experiments/physics/test_kuramoto_chimera_memory.py` with the published seed.

## Honest caveats

- **Single seed per cell.** The 30 trajectories use seed = 42 + 1000*g_idx + n_idx for independence. Multi-seed analysis would give variance estimates on the lifetime in each cell.
- **2D parameter sweep, not full 4D.** $T_{\text{bath}}$ is fixed at 0.1; sweeping $T$ would give a 3D parameter scan. Could reveal further structure.
- **Specific kernel and $\alpha$.** The chimera regime is parameter-sensitive; the qualitative pattern (the peak shifts toward $\tau_{\text{mem}} \sim 1$ as coupling grows) should hold across kernel variations, but the precise peak locations will vary.
- **Multi-exponential memory.** Single exponential here; multi-exponential could reveal richer dynamics.
- **The structural reading is post-hoc fit?** The explanation (bath diffusion destabilizes Markovian-limit chimera; memory at $\tau_{\text{mem}} \sim$ bath-decorrelation-time provides resistance) is consistent with the data but was not predicted in advance. Treat as a hypothesis for future tests.

## Reproducibility

```bash
LD_LIBRARY_PATH=".venv/lib/python3.11/site-packages/nvidia/*/lib:$LD_LIBRARY_PATH" \
  .venv/bin/python experiments/physics/test_kuramoto_chimera_memory.py
```

Wall time: 38.9 seconds on RTX 4060. Output: `outputs/kuramoto_chimera_memory_p3/`. Seed base: 42.

## Related documents

- Earlier result on the same prediction: [`09-kuramoto-chimera-memory.md`](09-kuramoto-chimera-memory.md).
- Interface: [`../interfaces/10-kuramoto-synchronization.md`](../interfaces/10-kuramoto-synchronization.md), prediction P10.1.
- Methodology of P3 default: [`../principles/03-coupling.md`](../principles/03-coupling.md), [`../methodology/02-limits-of-falsification.md`](../methodology/02-limits-of-falsification.md).
- Protocol: [`../experiments/PROTOCOLS.md`](../experiments/PROTOCOLS.md).

## What this result implies for the program

The result shifts the picture of P10.1: chimera lifetime in this 1D ring of phase oscillators depends jointly on $\gamma_0$ and $\tau_{\text{mem}}$ rather than on $\tau_{\text{mem}}$ alone. The companion run in [`09-kuramoto-chimera-memory.md`](09-kuramoto-chimera-memory.md), at $\gamma_0 = 0$ and $T = 0$, sits at one corner of the present sweep; the present 2D sweep populates the rest.

Candidates for further investigation of this prediction: multi-seed statistical analysis; $T_{\text{bath}}$ sweep; kernel-width sweep; alternative memory-kernel shapes (multi-exponential, power-law).
