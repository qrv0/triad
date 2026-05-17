# Predictions status board

This page lists every locally-testable prediction across the cross-domain interfaces in one place, grouped by interface. Each row gives the prediction ID, the one-line claim, the current status, and a link to the result document where a test exists.

Status terms follow the methodology in [`../methodology/02-limits-of-falsification.md`](../methodology/02-limits-of-falsification.md): predictions are evaluated by numerical reproduction at the parameter values each experiment requires, and a prediction's status reflects whether such a test has run and what evidence under criterion 4 of [`../methodology/04-the-six-criteria.md`](../methodology/04-the-six-criteria.md) it contributes. There is no aggregate "passing rate" — the global structural claim is not evaluated by per-prediction accumulation; the six criteria are.

<details>
<summary><b>Status vocabulary</b></summary>

- **not yet tested** — no test has been run.
- **tested, consistent** — a test ran and the observed quantity matches the prediction. Contributes evidence under criterion 4 (cross-domain coherence) and criterion 2 (reproducibility).
- **tested, inconsistent** — a test ran and the observed quantity does not match. Prompts investigation of calibration, auxiliary numerical assumptions (Duhem–Quine), or implementation; does not falsify the structural claim.
- **partially tested** — a related experiment exists but does not directly target this prediction.

None of the terms use the word "falsified" because the methodology rejects Popperian falsificationism as the evaluation method for this work.

</details>

[Browse interfaces by domain](README.md) · [Compare two interfaces](compare.md)

---

### Interface 01: Other instances of NLS dynamics — physics

| ID | Prediction | Status | Result |
|---|---|---|---|
| P1.1 | Memory-augmented soliton stability scales with Raman timescale ratio | not yet tested | — |
| P1.2 | BEC anti-collapse threshold scales with non-condensate-cloud temperature | not yet tested | — |
| P1.3 | Surface-wave Benjamin–Feir threshold shifts with bottom-friction memory | not yet tested | — |

### Interface 02: Baryon acoustic oscillations — cosmology

| ID | Prediction | Status | Result |
|---|---|---|---|
| P2.1 | BAO peak position correction scales with memory-kernel timescale at recombination | not yet tested | — |
| P2.2 | Secondary BAO peaks show memory-modulated harmonic structure | not yet tested | — |
| P2.3 | Phase shift in BAO ringing detectable in DESI/LSST data | not yet tested | — |

### Interface 03: Chladni cymatics and Faraday waves — acoustics

| ID | Prediction | Status | Result |
|---|---|---|---|
| P3.1 | Symmetry selection probability scales with memory timescale at fixed drive | not yet tested | — |
| P3.2 | Pattern stability scales with drive amplitude in the predicted regime | not yet tested | — |
| P3.3 | Multiple symmetries coexist in the bistable regime predicted by memory hysteresis | not yet tested | — |

### Interface 04: Gamma entrainment and broadband absorption — neuroscience

| ID | Prediction | Status | Result |
|---|---|---|---|
| P4.1 | Broadband absorption bandwidth scales with memory-mode hierarchy depth | not yet tested | — |
| P4.2 | Cortical regions with multi-timescale glia show stronger GENUS response | not yet tested | — |
| P4.3 | GENUS amyloid-clearance kinetics follows the predicted memory-coupling pattern | not yet tested | — |

### Interface 05: Archaeoacoustic resonance at megalithic sites — archaeology

| ID | Prediction | Status | Result |
|---|---|---|---|
| P5.1 | Additional megalithic chambers resonate in the predicted 70–110 Hz band | not yet tested | — |
| P5.2 | EEG response outside 110 Hz predicted by the second principal mode at 66 Hz | not yet tested | — |
| P5.3 | Ratio of the two principal frequencies stays in the predicted band across chambers | not yet tested | — |

### Interface 06: State space models — engineering *(in [mnsm spinoff](https://github.com/qrv0/mnsm))*

| ID | Prediction | Status | Result |
|---|---|---|---|
| P6.1 | FDT-locked noise reduces training trajectory variance vs ad-hoc noise schedules | partially tested | [mnsm/results/04](https://github.com/qrv0/mnsm/blob/main/results/04-fdt-locked-noise-empirical-p3.md) |
| P6.2 | Optimization collapse boundary scales with model size as the cubic term predicts | tested, consistent | [mnsm/results/01](https://github.com/qrv0/mnsm/blob/main/results/01-optimization-collapse-empirical.md) |
| P6.3 | Cubic state nonlinearity prevents SimSiam collapse without stop-gradient | partially tested | [mnsm/results/05](https://github.com/qrv0/mnsm/blob/main/results/05-cubic-ssm-simsiam-fdt.md) |

### Interface 07: Cosmological expansion as mechanism-shape — cosmology

| ID | Prediction | Status | Result |
|---|---|---|---|
| P7.1 | Late-time dark-energy equation of state shows $V_{\text{mem}}$-induced deviation from cosmological constant | not yet tested | — |
| P7.2 | Small-scale BAO substructure follows the equation's memory-modulated spectrum | not yet tested | — |
| P7.3 | Inflationary-era residual signal in tensor-to-scalar ratio matches anti-collapse profile | not yet tested | — |

### Interface 08: Mechanistic interpretability — engineering *(in [mnsm spinoff](https://github.com/qrv0/mnsm))*

| ID | Prediction | Status | Result |
|---|---|---|---|
| P8.1 | Sparse autoencoder recovery rate scales with auxiliary-field count in modified architectures | not yet tested | — |
| P8.2 | Superposition density correlates inversely with explicit memory hierarchy depth | not yet tested | — |
| P8.3 | Polysemanticity decreases when auxiliary fields are added to attention layers | not yet tested | — |

### Interface 09: Critical brain dynamics — neuroscience

| ID | Prediction | Status | Result |
|---|---|---|---|
| P9.1 | Cortex shows multi-timescale memory hierarchy matching equation predictions | not yet tested | — |
| P9.2 | VIP–AQP4 cortical regions show predicted broadband absorption signature | not yet tested | — |
| P9.3 | Multi-scale 1/f spectra emerge from auxiliary-field hierarchy without parameter tuning | not yet tested | — |

### Interface 10: Kuramoto synchronization with memory — complex systems

| ID | Prediction | Status | Result |
|---|---|---|---|
| P10.1 | Chimera-state lifetime peaks at $\tau_{\text{mem}} / \tau_{\text{sync}} \sim 1$ | tested, consistent | [`results/14`](../results/14-kuramoto-chimera-fdt.md) |
| P10.2 | Cardiac arrhythmia onset corresponds to the triangle's structural breakdown | not yet tested | — |
| P10.3 | Power-grid stability correlates with effective coupling memory | not yet tested | — |

### Interface 11: Immune affinity maturation — biology

| ID | Prediction | Status | Result |
|---|---|---|---|
| P11.1 | Memory-B-cell response amplitude scales with predicted timing of antigen exposure | not yet tested | — |
| P11.2 | Autoimmune disease classification maps to the triangle's structural failure modes | not yet tested | — |
| P11.3 | Affinity maturation kinetics correlates with memory-kernel timescale predictions | not yet tested | — |

### Interface 12: Friston free-energy and active inference — complex systems

| ID | Prediction | Status | Result |
|---|---|---|---|
| P12.1 | Predictive-coding hierarchy depth correlates with structural memory-mode count | not yet tested | — |
| P12.2 | Hierarchical active-inference agent more stable than non-hierarchical equivalent | not yet tested | — |
| P12.3 | Cortical hierarchy structurally aligns with the equation's auxiliary-field hierarchy | not yet tested | — |

### Interface 13: Active matter — complex systems

| ID | Prediction | Status | Result |
|---|---|---|---|
| P13.1 | Active-crystal symmetry selection follows the equation's BCC pattern | not yet tested | — |
| P13.2 | Flock-correlation length scales with predicted memory-coupling strength | not yet tested | — |
| P13.3 | Motility-induced phase separation shows broadband-absorption response | not yet tested | — |

### Interface 14: Self-organized criticality — complex systems

| ID | Prediction | Status | Result |
|---|---|---|---|
| P14.1 | BTW-style critical exponents emerge in MNSM sweeps | tested, consistent | [`results/18`](../results/18-soc-vs-mnsm-matched-drive.md) |
| P14.2 | MNSM avalanche-size distribution matches BTW reference under matched drive | tested, consistent | [`results/18`](../results/18-soc-vs-mnsm-matched-drive.md) |
| P14.3 | Neuronal-avalanche universality class shared between cortex and MNSM critical regime | not yet tested | — |

### Interface 15: Cardiac dynamics — biology

| ID | Prediction | Status | Result |
|---|---|---|---|
| P15.1 | Cardiac alternans threshold scales with predicted memory-hierarchy depth | not yet tested | — |
| P15.2 | Clinical arrhythmia categories map to triangle structural failure modes | not yet tested | — |
| P15.3 | Heart rate variability spectrum matches the predicted multi-timescale decomposition | not yet tested | — |

### Interface 16: Gene regulation and circadian clocks — biology

| ID | Prediction | Status | Result |
|---|---|---|---|
| P16.1 | Circadian period robustness scales with regulatory hierarchy depth | not yet tested | — |
| P16.2 | Temperature compensation strength tracks the predicted memory-kernel pattern | not yet tested | — |
| P16.3 | Cell-cycle–circadian coupling follows the triangle's two-level integration | not yet tested | — |

### Interface 17: Ecosystem dynamics — biology

| ID | Prediction | Status | Result |
|---|---|---|---|
| P17.1 | Ecosystem diversity–stability tracks the predicted memory-coupling pattern | not yet tested | — |
| P17.2 | Age-structured populations show predicted memory-modulated stability vs unstructured | not yet tested | — |
| P17.3 | Regime-shift indicators correlate with the structural failure-mode predictions | not yet tested | — |

### Interfaces 18–22: more recent substrates

Predictions for pseudomode quantum ([interface 18](18-pseudomode-quantum.md)), Prony viscoelasticity ([interface 19](19-viscoelasticity-prony.md)), warm inflation ([interface 20](20-warm-inflation.md)), Hawkes intensity ([interface 21](21-hawkes-intensity.md)), and earthquake cycle ([interface 22](22-earthquake-cycle.md)) are listed in each interface document. Several have associated result documents already: [results/19](../results/19-pseudomode-auxiliary-equivalence.md), [results/20](../results/20-prony-viscoelastic-reproduction.md), [results/21](../results/21-hawkes-intensity-auxiliary.md), [results/22](../results/22-warm-inflation-langevin.md).
