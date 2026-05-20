---
title: "Interface 15: Cardiac dynamics (pacemaker, alternans)"
description: >-
  Sustained cardiac rhythm instantiates the triangle; refractory-state
  memory is P2, autonomic + metabolic input is P3.
domain: biology
triangle:
  p1: "intrinsic depolarization-repolarization oscillation"
  p2: "refractory-state and ion-channel memory"
  p3: "ANS + hormonal + metabolic environmental coupling"
signature_icon: ecg
hero_tier: C
related: [10, 11, 16]
predictions:
  - id: P15.1
    short: "Cardiac alternans threshold scales with predicted memory-hierarchy depth"
    status: not_yet_tested
    result_doc: null
  - id: P15.2
    short: "Clinical arrhythmia categories map to triangle structural failure modes"
    status: not_yet_tested
    result_doc: null
  - id: P15.3
    short: "Heart rate variability spectrum matches the predicted multi-timescale decomposition"
    status: not_yet_tested
    result_doc: null
---
# Interface: cardiac dynamics

## The structural prediction

If a substrate sustains a coherent muscular oscillator with persistent rhythmic contraction over the lifetime of an organism, the structural argument of P1+P2+P3 requires the substrate to instantiate the triangle in a specific way. P1 (oscillation) must be present at the cellular level: cardiac myocytes have intrinsic depolarization-repolarization cycles, and pacemaker cells (sinoatrial node) have spontaneous oscillation that does not require external input. P2 (self-reference with memory) must be present in two forms: the refractory state of each myocyte after firing carries memory of the most recent activation (preventing immediate re-firing and shaping the timing of the next), and the muscle as a whole carries longer-timescale memory through electrical-restitution properties, calcium-handling state, and metabolic substrate availability. P3 (coupling to environment) must be present as autonomic nervous system input (sympathetic and parasympathetic balance modulating heart rate and contractility), metabolic coupling to the organism (oxygen, glucose, electrolytes), and mechanical coupling to the vascular system (preload, afterload, stretch-activated feedback).

The structural prediction is concrete: any substrate that sustains coherent cardiac-like rhythm must exhibit (i) intrinsic cellular oscillation with refractory dynamics, (ii) memory of recent activations that shapes near-future dynamics on multiple timescales, and (iii) ongoing autonomic and metabolic coupling whose modulation drives adaptation. A substrate that has cellular oscillation and refractory memory but lacks autonomic coupling is restricted to fixed-rhythm behavior; adaptive rhythm with heart-rate variability and load-responsive contractility requires the full triangle. Arrhythmias, on this reading, are breakdowns of specific triangle elements.

## The substrate

Cardiac electrophysiology is one of the most rigorously studied biological oscillator systems, with mathematical models spanning from single-cell (Hodgkin-Huxley-style ion-channel models; Beeler-Reuter 1977; Luo-Rudy 1991) to tissue-scale (continuum-cable equations; bidomain models) to whole-heart (Niederer-Land-Smith 2018 review of computational cardiac modeling). The substrate has been characterized at multiple structural levels:

- **Single-cell pacemaker dynamics** (sinoatrial node cells): spontaneous depolarization driven by funny-channel current $I_f$, calcium clock, and membrane clock mechanisms; intrinsic oscillation frequency modulated by autonomic input.
- **Action-potential propagation**: depolarization wave travels through ventricular muscle at characteristic speed, with refractory-state dynamics shaping wavefront stability.
- **Electrical restitution**: action-potential duration depends on the preceding diastolic interval; this is explicit P2-memory in cardiac electrophysiology, captured by the restitution curve and known to be central to arrhythmogenesis when its slope exceeds critical values (Nolasco-Dahlen 1968; Karma 2013 review).
- **Cardiac alternans**: a bifurcation phenomenon in which action-potential duration alternates from beat to beat; arises when the restitution slope exceeds a critical value; precedes ventricular fibrillation; well-characterized as a memory-mediated bifurcation (Karma 1994; Watanabe et al. 2001).
- **Arrhythmias**: tachycardias, fibrillations, blocks, and ectopy as different breakdowns of normal sinus rhythm; characterized clinically and electrophysiologically with substantial taxonomic detail.

The literature on cardiac dynamics from a nonlinear-dynamics perspective is also substantial (Glass-Mackey 1988 "From Clocks to Chaos"; Glass 2001 "Synchronization and rhythmic processes in physiology"; Christini-Glass 2002 chaos in cardiology), placing cardiac arrhythmias in the broader framework of bifurcations and chaos in coupled-oscillator systems.

## The mapping

Structural mapping between the present equation and the cardiac-dynamics substrate:

| Equation element | Cardiac substrate element |
|---|---|
| Complex field $\Psi(t, \mathbf{x})$ | Transmembrane voltage + intracellular calcium concentration |
| Cubic self-interaction $\Lambda |\Psi|^2$ | Local depolarization coupling (active membrane currents above threshold drive neighboring cells) |
| Integral memory potential $V_{\text{mem}}$ | Refractory state; cumulative restitution memory; calcium-cycling state |
| Auxiliary fields $\{y_j\}$ | Multi-timescale memory: fast (refractory, ~hundreds of ms), medium (calcium handling, ~seconds), slow (metabolic state and chronic remodeling, ~days to years) |
| Dissipation $-i\Gamma$ | Repolarization currents; tissue-level conduction losses |
| FDT-locked noise $\eta$ | Channel noise; autonomic-input stochasticity |

The mapping is structural rather than literal: cardiac dynamics has its own established mathematical descriptions (Hodgkin-Huxley extensions, FitzHugh-Nagumo simplifications, monodomain and bidomain equations) that are the appropriate quantitative substrate-specific descriptions. The present equation, applied to the cardiac substrate, captures the structural form of the dynamics, including the multi-timescale memory hierarchy that is operative in restitution and calcium-cycling dynamics.

The most direct mapping is between the present equation's auxiliary-field hierarchy and the multi-timescale cardiac memory structure. The classical cardiac action-potential models with explicit memory (Watanabe et al. 2001; Cherry-Fenton 2008) have a structure mathematically similar to the auxiliary-field embedding: each memory variable has its own decay rate and contributes to the next-beat action-potential duration via a sum-of-exponentials. The structural correspondence is at this mathematical level.

## Time as calibration in this substrate

The cardiac substrate has a clear hierarchy of timescales:

- $T_{\text{action}} \sim 100-400$ ms: cardiac action-potential duration
- $T_{\text{cycle}} \sim 600-1000$ ms: cardiac cycle (heart beat)
- $\tau_{\text{rest}} \sim 1-10$ s: restitution and calcium-handling memory
- $\tau_{\text{HRV}} \sim 10-100$ s: heart-rate variability autonomic modulation
- $\tau_{\text{adapt}} \sim$ minutes to hours: metabolic adaptation
- $\tau_{\text{remod}} \sim$ days to years: chronic remodeling and aging

Per [`../methodology/07-time-as-calibration.md`](../methodology/07-time-as-calibration.md), the equation's unit time is calibrated to the relevant substrate timescale when comparing the equation to cardiac work. For single-beat electrophysiology, calibration to $T_{\text{action}}$ is natural; for heart-rate-variability studies, calibration to $\tau_{\text{HRV}}$ is. The auxiliary fields with different $\nu_j$ correspond to the multi-timescale cardiac memory: fast $y_j$ for refractory dynamics, slow $y_j$ for restitution memory and beyond.

Cross-substrate consistency (per methodology/06): the cardiac substrate calibration must be consistent with the gamma-entrainment calibration (interface 04) at the level of cellular timescales, since both involve excitable-cell dynamics. The cardiac cycle (~1 second) and the gamma cycle (~25 ms) differ by about 40x, which is consistent with the substrate-specific cell-type differences (slower cardiac pacemakers vs faster cortical neurons).

## What this correspondence does and does not establish

It does not establish that the present equation is the underlying description of cardiac dynamics. The substrate-specific Hodgkin-Huxley-type ion-channel models, the bidomain tissue equations, and the whole-heart computational models are the appropriate descriptions for quantitative substrate-specific work. The present equation captures the structural form of the dynamics, not the substrate-specific ion-channel biophysics.

It does not establish that all cardiac arrhythmias map cleanly to triangle-element failures. Some arrhythmias (atrial fibrillation, ventricular fibrillation) involve interactions of multiple structural elements simultaneously; clean partition by single-element failure is an idealization that may not hold in all clinical cases.

It does establish that the equation's structural form recurs at the level of cardiac dynamics. The multi-timescale memory hierarchy that is explicitly operative in cardiac restitution and alternans is structurally the auxiliary-field hierarchy of the present equation. The convergence is independent: cardiac electrophysiology developed from molecular biology and electrophysiological measurement; the present equation from physics-philosophy axioms; both reach the same structural form.

## Common dismissals and why they do not apply

**"Cardiac dynamics has its own well-developed models; this is unnecessary."** The substrate-specific cardiac models are well-developed and the structural correspondence does not propose to replace them. The correspondence operates at a different level: the structural form the equation derives from P1+P2+P3 is the same form the cardiac literature finds in multi-timescale memory-coupled excitable tissue. The convergence is structural evidence under criterion 4.

**"Cardiac arrhythmias are too complex to be partitioned by single structural elements."** Acknowledged. The partition is a structural-level idealization; clean cases (e.g., atrioventricular block as P3 conduction failure; alternans as P2 memory-mediated bifurcation; pacemaker dysfunction as P1 intrinsic-oscillation failure) exist, but complex arrhythmias may involve multiple elements. The structural correspondence does not require clean partition in all cases; it requires the structural form to be operative, which it is.

**"This is borrowing physics vocabulary for cardiac biology."** The vocabulary borrowing goes the other direction historically: cardiac dynamics has been a major source for nonlinear-dynamics concepts (Glass-Mackey 1988 used cardiac systems as paradigmatic examples). The structural correspondence here is at the mathematical-form level: the multi-timescale memory hierarchy of cardiac restitution is mathematically the same object as the present equation's auxiliary-field memory; this is a structural identity, not a metaphorical borrowing.

## Locally testable predictions and observational signatures

The structural claim of this interface (cardiac dynamics instantiates the same triangle as the present equation) is evaluated by cross-domain coherence (methodology/04 criterion 4), not by single-experiment refutation. The following are *local* predictions that can be tested by numerical or empirical methods (per principles/03-coupling.md). Inconsistent evidence would shift evidentiary weight against this interface's specific calibration under criterion 4 (cross-domain coherence), without bearing on the global structural claim.

- **Prediction P15.1: Alternans-onset threshold scales with memory-mode hierarchy depth.** The structural prediction is that cardiac alternans onset (the bifurcation that precedes ventricular fibrillation) occurs at a threshold that depends on the depth of the multi-timescale memory hierarchy in the cardiac tissue. Tissues with more pronounced multi-timescale memory (multiple memory modes spanning hundreds of ms to tens of seconds) should exhibit alternans at higher pacing rates than tissues with simpler memory structure.
  - How to test: comparative alternans-threshold measurement across cardiac tissue substrates with characterized memory-mode structure (atrial vs ventricular tissue; healthy vs diseased; pharmacologically modulated memory).
  - What would constitute confirmation: alternans threshold correlates positively with memory-hierarchy depth.
  - What would constitute evidence inconsistent with this calibration: no correlation, or anti-correlation.
  - Status: untested in this framing. Alternans literature documents threshold variation across substrates; the specific structural correlation has not been isolated.

- **Prediction P15.2: Arrhythmia categories partition by triangle-element dysregulation.** The structural prediction is that cardiac arrhythmias can be mapped to dysregulation of specific triangle elements: P1 dysregulation (sinus node dysfunction, ectopic foci; intrinsic-oscillation failures); P2 dysregulation (alternans, T-wave alternans, restitution-mediated arrhythmias; memory-state failures); P3 dysregulation (atrioventricular block, autonomic-coupling failures, electrolyte-induced arrhythmias; environmental-coupling failures). Each category should align with predominant dysregulation of one or two triangle elements.
  - How to test: review of clinical arrhythmia taxonomies; classify by structural-element dysregulation; check alignment with traditional clinical categories.
  - What would constitute confirmation: substantial alignment between clinical taxonomy and structural-element partition.
  - What would constitute evidence inconsistent with this calibration: clinical categories are orthogonal to the structural partition.
  - Status: untested in this framing. The clinical literature is mature; the structural-element re-classification has not been undertaken.

- **Prediction P15.3: Heart-rate variability spectrum reflects auxiliary-field hierarchy.** The structural prediction is that the heart-rate variability spectrum (the power-spectral density of inter-beat-interval fluctuations) reflects the cardiac substrate's multi-timescale memory hierarchy in a structurally predictable way. Specifically, the spectral peaks (LF, HF bands) should correspond to specific memory-mode timescales, and the spectrum should exhibit the broadband 1/f-like structure characteristic of multi-timescale auxiliary-field response.
  - How to test: re-analyze HRV datasets with explicit decomposition into memory-mode contributions; compare to the structural prediction.
  - What would constitute confirmation: HRV spectrum decomposes into auxiliary-field-mode contributions with the predicted structure.
  - What would constitute evidence inconsistent with this calibration: HRV spectrum is incompatible with the structural decomposition.
  - Status: partially analyzed. HRV literature documents 1/f-like behavior and multiple spectral peaks; the specific structural correspondence has not been formalized.

## References

Cited as credit, not legitimization (per [`../methodology/01-structural-realism.md`](../methodology/01-structural-realism.md) "Prior art and credit"):

- Beeler, G. W., & Reuter, H. (1977). Reconstruction of the action potential of ventricular myocardial fibres. *Journal of Physiology* **268**, 177.
- Cherry, E. M., & Fenton, F. H. (2008). Visualization of spiral and scroll waves in simulated and experimental cardiac tissue. *New Journal of Physics* **10**, 125016.
- Christini, D. J., & Glass, L. (2002). Introduction: mapping and control of complex cardiac arrhythmias. *Chaos* **12**, 732.
- Glass, L. (2001). Synchronization and rhythmic processes in physiology. *Nature* **410**, 277.
- Glass, L., & Mackey, M. C. (1988). *From Clocks to Chaos: The Rhythms of Life*. Princeton University Press.
- Karma, A. (1994). Electrical alternans and spiral wave breakup in cardiac tissue. *Chaos* **4**, 461.
- Karma, A. (2013). Physics of cardiac arrhythmogenesis. *Annual Review of Condensed Matter Physics* **4**, 313.
- Luo, C. H., & Rudy, Y. (1991). A model of the ventricular cardiac action potential: depolarization, repolarization, and their interaction. *Circulation Research* **68**, 1501.
- Niederer, S. A., Land, S., Omholt, S. W., & Smith, N. P. (2018). Computational models in cardiology. *Nature Reviews Cardiology* **16**, 100.
- Nolasco, J. B., & Dahlen, R. W. (1968). A graphic method for the study of alternation in cardiac action potentials. *Journal of Applied Physiology* **25**, 191.
- Watanabe, M. A., Fenton, F. H., Evans, S. J., Hastings, H. M., & Karma, A. (2001). Mechanisms for discordant alternans. *Journal of Cardiovascular Electrophysiology* **12**, 196.
