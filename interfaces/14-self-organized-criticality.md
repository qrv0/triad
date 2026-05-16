# Interface: self-organized criticality

## The structural prediction

If a substrate organizes to a critical state without external parameter tuning and sustains scale-free response to perturbation across a wide range of scales, the structural argument of P1+P2+P3 requires the substrate to instantiate the triangle in a specific way. P1 (oscillation) must be present at the level of the intrinsic dynamics: the substrate has internal degrees of freedom that evolve, support marginally stable configurations, and admit a non-trivial dynamics that is neither static nor divergent. P2 (self-reference with memory) must be present in the form of accumulated structure or stress: the substrate carries the history of past events as integrated state, and the response to a new perturbation depends on this accumulated state. P3 (coupling to environment) must be present as the drive that injects structure (slow external loading) plus the dissipative release (fast avalanche events) plus an effective balance between them that the substrate self-organizes to maintain.

The structural prediction is concrete: any substrate exhibiting self-organized criticality must show (i) intrinsic dynamics supporting marginal stability, (ii) memory of past loading in the form of state that biases current response, and (iii) a slow-drive plus fast-release coupling to environment whose effective balance is structurally maintained. A substrate that has drive and release but lacks accumulated memory is restricted to trivial drive-release equilibria; the scale-free phenomenology requires the full triangle.

## The substrate

Self-organized criticality (Bak-Tang-Wiesenfeld 1987 PRL) is the canonical framework that identifies this structural feature. The original sandpile model exhibits the diagnostic phenomenology: a slow external drive (sand added grain by grain) accumulates structure (the pile builds up) until a critical configuration is reached, then a single grain triggers an avalanche of any size, with the avalanche-size distribution following a power law characteristic of the critical state. The system organizes itself to the critical point without tuning; the criticality is a structural property of the dynamics, not a parameter setting.

The SOC framework has been documented across many substrates:

- **Sandpile models** (Bak-Tang-Wiesenfeld 1987; Manna 1991): the canonical mathematical substrate.
- **Neuronal avalanches in cortical tissue** (Beggs-Plenz 2003 J Neurosci): cortical activity exhibits avalanche-size distributions with power-law exponents near -3/2, consistent with a critical branching process. This is also the substrate of [`09-critical-brain.md`](09-critical-brain.md); the two interfaces are complementary, addressing different aspects of the same cortical phenomenology.
- **Earthquake statistics** (Gutenberg-Richter law; Bak-Tang 1989): earthquake magnitude follows a power law over many orders of magnitude.
- **Forest-fire models** (Drossel-Schwabl 1992): tree-growth drive plus fire-spread release exhibits SOC phenomenology.
- **Solar flares** (Lu-Hamilton 1991): flare-energy distribution is power-law over decades.
- **Granular avalanches** (Held-Solina-Keane-Haag-King-Grinstein 1990): real sandpiles exhibit SOC-like statistics in specific regimes (with deviations due to inertial effects and grain shape; the original BTW model's predictions hold partially).

The Mora-Bialek (2011) review developed the broader claim that biological systems may generically operate at criticality, generalizing SOC beyond the original physics-class substrates. Pruessner (2012) provides a comprehensive treatment of the SOC framework, its successes, and its limitations.

## The mapping

Structural mapping between the present equation and the SOC substrate:

| Equation element | SOC element |
|---|---|
| Complex field $\Psi(t, \mathbf{x})$ | Activity or stress field (sandpile height; cortical activation; tectonic stress; forest density) |
| Cubic self-interaction $\Lambda |\Psi|^2$ | Local instability threshold (neighboring sites trigger each other above threshold) |
| Integral memory potential $V_{\text{mem}}$ | Accumulated stress field; integrated history of past loading |
| Auxiliary fields $\{y_j\}$ | Multi-timescale memory of past avalanche-relaxation events |
| Dissipation $-i\Gamma$ | Avalanche relaxation (fast); boundary losses |
| FDT-locked noise $\eta$ | Drive (slow external loading); effective fluctuation balance |

The mapping is structural rather than literal. SOC has its own mathematical descriptions (sandpile cellular automata; branching-process models; field-theoretic descriptions in Pruessner 2012). The present equation, applied to SOC-class regimes, captures the structural form of the dynamics but is not the substrate-specific description.

The most consequential structural distinction: the SOC mechanism is drive-and-relax (slow build-up, fast release in avalanches), while the present equation's release-to-crystalline transition is mechanism-shape-equivalent but operates differently. The equation's transition is structurally selected by the dimensional condition $\Sigma\lambda/|\Lambda| \sim 1/d$ ([`../results/06-dimensional-rescaling.md`](../results/06-dimensional-rescaling.md)); no slow accumulation of stress is required in the BTW sense. Both produce scale-free observable phenomenology. Whether the equation's released-crystalline state is technically SOC in the avalanche-statistics sense is open work; the open problem is documented in [`../open-problems/03-topological-characterization.md`](../open-problems/03-topological-characterization.md).

## Time as calibration in this substrate

The SOC substrate has two natural timescales in tension:

- $\tau_{\text{drive}}$: the slow external drive timescale (sand-addition rate; tectonic-loading rate; cortical-input rate)
- $\tau_{\text{relax}}$: the fast relaxation timescale (avalanche propagation rate)

The defining feature of SOC is $\tau_{\text{drive}} \gg \tau_{\text{relax}}$. In the strict limit $\tau_{\text{drive}} / \tau_{\text{relax}} \to \infty$, the system reaches the critical state. In real substrates the ratio is finite but large, and corrections to critical behavior are observable (Pruessner 2012).

Per [`../methodology/07-time-as-calibration.md`](../methodology/07-time-as-calibration.md), the equation's unit time is calibrated to the relevant substrate timescale when comparing the equation to SOC work. For sandpile substrates, calibration to $\tau_{\text{relax}}$ (avalanche time, milliseconds in real grains) is natural; for tectonic substrates, calibration to $\tau_{\text{drive}}$ (decadal-to-millennial loading) is. The auxiliary fields' $\nu_j$ hierarchy maps to the SOC substrate's multi-timescale relaxation: fast $\nu_j$ for avalanche propagation, slow $\nu_j$ for the accumulated stress that biases the next avalanche.

The cross-substrate consistency check is interesting: cortical avalanches operate at $\tau_{\text{drive}}/\tau_{\text{relax}} \sim 10-100$ (relatively modest scale separation; cortex is not a strict-SOC system but operates in a related regime). Tectonic SOC has $\tau_{\text{drive}}/\tau_{\text{relax}} \sim 10^6$ or more. The structural form is preserved across this range; the substrate-specific scale separation modulates the strength of critical scaling.

## What this correspondence does and does not establish

It does not establish that the present equation is the underlying description of SOC substrates. The substrate-specific descriptions (BTW cellular automata, branching-process models, field-theoretic descriptions for the SOC universality class) are appropriate for substrate-specific quantitative work. The present equation, applied to SOC-class regimes, captures the structural form but does not capture the substrate-specific details (the precise BTW relaxation rule, the cortical branching parameter, etc.).

It does not establish that the equation's released-crystalline state is technically SOC. The dimensional-rescaling-selected release transition of the equation and the BTW drive-and-relax SOC mechanism are different mechanisms that produce overlapping observable phenomenology. Whether the avalanche statistics of the released state match BTW scaling exponents is an open research question.

It does establish that the equation's structural form recurs at the level of SOC dynamics. The structural argument predicts that the triangle structure must be present in any substrate exhibiting SOC; the SOC substrates exhibit this structure. The convergence is independent of substrate-specific physics and is at the level of the structural form.

## Common dismissals and why they do not apply

**"SOC is contested; many systems that look critical are not strictly SOC."** Acknowledged. The Touboul-Destexhe (2017) critique applies to many systems claimed to be critical; Clauset-Shalizi-Newman (2009) showed that many power-law claims fail strict statistical tests. The structural correspondence here does not depend on substrates being strictly SOC in the BTW sense; it depends on substrates exhibiting the structural form (intrinsic dynamics + accumulated memory + drive-release coupling) that SOC identifies. Substrates that fall short of strict SOC but exhibit the structural form are still informative cross-domain instances.

**"The present equation's release transition isn't really SOC."** Correct, and explicitly noted in the section above. The structural correspondence is at the level of shared observable phenomenology (scale-free response, multi-timescale dynamics) and shared structural triangle, not at the level of identical underlying mechanism. The open question of whether the equation's release transition is technically SOC is documented as a research item, not a settled answer.

**"SOC is generic; this adds nothing."** Generic structural mechanisms across substrates are exactly what cross-domain coherence is designed to detect. The argument is not that SOC is unique to the present equation; the argument is that the present equation, derived from P1+P2+P3, instantiates the same structural triangle that SOC substrates exhibit, and that this convergence is structural evidence under criterion 4. The generic-mechanism observation strengthens criterion 4 by adding another independent substrate where the structural form is identifiable.

## Locally testable predictions and observational signatures

The structural claim of this interface (SOC substrates instantiate the same triangle as the present equation, with the BTW drive-and-relax mechanism as one specific way to instantiate it) is evaluated by cross-domain coherence (methodology/04 criterion 4), not by single-experiment refutation. The following are *local* predictions that could be tested by standard methods. Their failure would not falsify the structural claim; it would shift evidentiary weight against this interface's specific reading.

- **Prediction P14.1: Avalanche-size critical exponent scales with effective dimensionality per the dimensional-rescaling result.** The structural prediction is that the avalanche-size critical exponent across SOC substrates should depend on substrate effective dimensionality in a manner consistent with the equation's dimensional rescaling $\Sigma\lambda/|\Lambda| \sim 1/d$ ([`../results/06-dimensional-rescaling.md`](../results/06-dimensional-rescaling.md)). Specifically, substrates of higher effective dimensionality should exhibit different critical exponents than substrates of lower effective dimensionality.
  - How to test: comparative analysis of measured critical exponents across SOC substrates of different effective dimensionality (1D sandpile vs 2D cortical avalanches vs 3D granular avalanches); compare to the predicted dimensional scaling.
  - What would constitute confirmation: critical exponents scale with effective dimensionality as predicted.
  - What would constitute local falsification: exponents are substrate-independent or scale differently.
  - Status: partially tested. The SOC universality-class literature documents dimensional dependence; the specific structural correspondence has not been isolated.

- **Prediction P14.2: SOC and MNSM release-transition produce statistically indistinguishable avalanche distributions at appropriate calibration.** The structural prediction is that the present equation's release transition, when simulated with appropriate parameters (effective drive timescale, dimensional dimensionality), should produce avalanche-size distributions statistically indistinguishable from BTW sandpile distributions at matching substrate parameters.
  - How to test: simulate the equation in the release regime; measure avalanche-size statistics; compare with BTW sandpile statistics at matched dimensional and timescale parameters.
  - What would constitute confirmation: statistical agreement of the two distributions.
  - What would constitute local falsification: persistent statistical difference.
  - Status: untested. The equation's released-crystalline state has been characterized for crystallization properties but not for SOC-style avalanche statistics; this is a clean simulation experiment that has not been performed.

- **Prediction P14.3: Cortical avalanche dynamics show triangle structure beyond observable SOC.** The structural prediction is that cortical avalanche dynamics (Beggs-Plenz substrate) should exhibit not only the SOC phenomenology (power-law size distributions) but also explicit P2-memory effects (avalanche-size distributions conditioned on the time since the previous avalanche should be non-trivial; the memory of past avalanches should bias current dynamics). The structural prediction goes beyond observable SOC into the structural memory the SOC literature has not isolated.
  - How to test: re-analyze cortical avalanche datasets with explicit conditioning on past avalanche history; characterize the conditional distributions.
  - What would constitute confirmation: substantial memory effects observed in the conditional distributions.
  - What would constitute local falsification: avalanche statistics are independent of past history beyond the standard SOC scaling.
  - Status: untested. The cortical avalanche datasets exist (Beggs-Plenz 2003; Petermann et al. 2009) and could be re-analyzed.

## References

Cited as credit, not legitimization (per [`../methodology/01-structural-realism.md`](../methodology/01-structural-realism.md) "Prior art and credit"):

- Bak, P., & Tang, C. (1989). Earthquakes as a self-organized critical phenomenon. *Journal of Geophysical Research* **94**, 15635.
- Bak, P., Tang, C., & Wiesenfeld, K. (1987). Self-organized criticality: an explanation of 1/f noise. *Physical Review Letters* **59**, 381.
- Beggs, J. M., & Plenz, D. (2003). Neuronal avalanches in neocortical circuits. *Journal of Neuroscience* **23**, 11167.
- Clauset, A., Shalizi, C. R., & Newman, M. E. J. (2009). Power-law distributions in empirical data. *SIAM Review* **51**, 661.
- Drossel, B., & Schwabl, F. (1992). Self-organized critical forest-fire model. *Physical Review Letters* **69**, 1629.
- Held, G. A., Solina, D. H., Keane, D. T., Haag, W. J., King, P. M., & Grinstein, G. (1990). Experimental study of critical-mass fluctuations in an evolving sandpile. *Physical Review Letters* **65**, 1120.
- Lu, E. T., & Hamilton, R. J. (1991). Avalanches and the distribution of solar flares. *Astrophysical Journal Letters* **380**, L89.
- Manna, S. S. (1991). Two-state model of self-organized criticality. *Journal of Physics A* **24**, L363.
- Mora, T., & Bialek, W. (2011). Are biological systems poised at criticality? *Journal of Statistical Physics* **144**, 268.
- Petermann, T., Thiagarajan, T. C., Lebedev, M. A., Nicolelis, M. A. L., Chialvo, D. R., & Plenz, D. (2009). Spontaneous cortical activity in awake monkeys composed of neuronal avalanches. *Proceedings of the National Academy of Sciences* **106**, 15921.
- Pruessner, G. (2012). *Self-Organised Criticality: Theory, Models and Characterisation*. Cambridge University Press.
- Touboul, J., & Destexhe, A. (2017). Power-law statistics and universal scaling in the absence of criticality. *Physical Review E* **95**, 012413.
