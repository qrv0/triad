---
title: "Interface 12: Friston free-energy and active inference"
description: >-
  Predictive coding / free-energy minimization instantiates the triangle
  in a variational-dynamics substrate; the hierarchical generative model
  is P2's memory hierarchy.
domain: complex-systems
triangle:
  p1: "internal-state inferential dynamics"
  p2: "hierarchical generative model + precision weights memory"
  p3: "sensory observation + motor action coupling"
signature_icon: nested
hero_tier: C
related: [4, 8, 10]
predictions:
  - id: P12.1
    short: "Predictive-coding hierarchy depth correlates with structural memory-mode count"
    status: not_yet_tested
    result_doc: null
  - id: P12.2
    short: "Hierarchical active-inference agent more stable than non-hierarchical equivalent"
    status: not_yet_tested
    result_doc: null
  - id: P12.3
    short: "Cortical hierarchy structurally aligns with the equation's auxiliary-field hierarchy"
    status: not_yet_tested
    result_doc: null
---
# Interface: free-energy minimization and active inference

## The structural prediction

If a substrate sustains operation by minimizing prediction error about its sensory inputs, the structural argument of P1+P2+P3 requires the substrate to instantiate the triangle in a specific way. P1 (oscillation) must be present at the level of internal dynamics: the system has intrinsic state evolution driven by the gradient of a variational free-energy functional, and that dynamics is not static but oscillatory in the sense that the system continuously updates its internal estimate against incoming signals. P2 (self-reference with memory) must be present as the generative model the system holds about its environment: the model is itself state, persisting and updating across time, and a hierarchical version of the model has multi-timescale components corresponding to different prediction horizons. P3 (coupling to environment) must be present in two forms: sensory coupling (signals arriving from the environment that the model attempts to predict) and active coupling (motor outputs that modify the environment in ways that reduce future prediction error). The FDT-locked aspect of P3 is operative in a particular form: the system's effective free-energy minimization is structurally similar to thermalization against a bath at a specific temperature, where the temperature parameterizes the precision-weighting of prediction errors.

The structural prediction is concrete: any substrate that sustains adaptive behavior under sensory uncertainty must exhibit (i) intrinsic internal-state dynamics whose evolution is driven by a free-energy-like functional, (ii) a multi-timescale model of the environment held across time as state, and (iii) sensory and motor coupling to the environment in a balance that is FDT-locked in structure. The substrate-specific implementation differs across cases (cortex, robot controller, immune system, gene regulatory network all instantiate this differently), but the structural form is preserved.

## The substrate

The Free Energy Principle, developed by Karl Friston and collaborators across two decades of work, is the canonical theoretical framework that explicitly identifies this triangle structure in adaptive systems. The principle states that any self-organizing system that maintains its identity over time must, by mathematical necessity, minimize variational free energy with respect to a model of its environment (Friston 2010 Nat Rev Neurosci; Parr-Pezzulo-Friston 2022). Active inference extends the principle to action: the system selects actions that minimize expected free energy, equivalently, actions that maximize information gain or that bring future sensory inputs into alignment with the model's predictions.

The hierarchical predictive coding formulation (Friston 2008; Bastos-Usrey-Adams-Mangun-Fries-Friston 2012) makes the multi-timescale memory structure explicit. The cortical hierarchy is modeled as a stack of layers, each making predictions about the layer below at its own characteristic timescale; higher cortical levels predict slower-varying features (object identity, scene grammar) while lower levels predict faster-varying features (edge orientation, local motion). The timescale hierarchy is not merely descriptive; it is mathematically required for the free-energy minimization to be tractable across scales.

The framework has been applied across substrates: cortical microcircuits (Friston-Buzsaki-Kiebel 2017 on neuronal message passing under predictive coding), immune systems (the discontinuity-theory-of-immunity work of Pradeu, Jaeger, & Vivier 2013, which treats antigen recognition as a discrimination problem amenable to inference framings), gene-regulatory networks (Friston-Levin-Sengupta-Pezzulo 2015), and artificial systems (Buckley-Kim-McGregor-Seth 2017 on active-inference robots). The convergence across substrates is itself the structural-realist signature.

## The mapping

The mapping between the present equation and the FEP / active-inference framework is mathematical at the level of the variational dynamics, with substrate-specific calibration of the timescales.

| Equation element | FEP / active-inference element |
|---|---|
| Complex field $\Psi(t, \mathbf{x})$ | Internal-state representation (probabilistic posterior over external causes) |
| Cubic self-interaction $\Lambda |\Psi|^2$ | Self-information of the internal state (KL-divergence-like coupling of the model to its own predictions) |
| Integral memory potential $V_{\text{mem}}$ | Generative model held as integrated history; predictions inherited from past inference |
| Auxiliary fields $\{y_j\}$ | Hierarchical layers of the predictive-coding stack, each at characteristic timescale $1/\nu_j$ |
| Dissipation $-i\Gamma$ | Free-energy descent rate (the system relaxes toward the free-energy minimum) |
| FDT-locked noise $\eta$ | Sensory noise + intrinsic stochasticity, balanced to maintain a stationary precision (FDT-equivalent for the perception-action loop) |

The mathematical correspondence is tightest at the hierarchical level: the cortical predictive-coding stack with multi-timescale layers $\{\nu_j\}$ is structurally the same object as the present equation's auxiliary-field hierarchy $\{(\nu_j, \lambda_j)\}$. The diagonal-state SSM correspondence ([`06-state-space-models.md`](06-state-space-models.md)) makes this mathematical at the level of the linear update; the FEP correspondence extends it to the variational-inference setting where the SSM state is interpreted as the posterior over latent causes.

The active-inference extension introduces the action-selection component: the system chooses actions that reduce expected free energy. In the present equation's language, this is the system modifying its environmental coupling to reduce the future surprise of sensory inputs. The structural form is preserved: an agent that selects actions to optimize a variational objective, with hierarchical internal model and stochastic sensorimotor coupling, instantiates the triangle in the active-inference substrate.

## Time as calibration in this substrate

The FEP / active-inference substrate has a clear hierarchy of timescales operating in parallel:

- $T_{\text{perceptual}} \sim 10-100$ ms: perceptual updating at the lowest cortical levels
- $T_{\text{working}} \sim 1-10$ s: working memory and short-term inference
- $T_{\text{deliberation}} \sim 10-100$ s: deliberative action selection
- $T_{\text{learning}} \sim$ days to lifetime: model learning, parameter updates, hierarchical refinement

Per [`../methodology/07-time-as-calibration.md`](../methodology/07-time-as-calibration.md), the equation's unit time is calibrated to the relevant substrate timescale when comparing the equation to FEP work. For perceptual-level modeling, calibration to $T_{\text{perceptual}}$ is natural; for developmental modeling of long-term model acquisition, calibration to $T_{\text{learning}}$ is. The auxiliary fields with different $\nu_j$ correspond directly to the predictive-coding hierarchy levels; the cortical instantiation of the hierarchy has each level operating at its own characteristic timescale.

The calibration-philosophy commitment (methodology/06) requires cross-substrate consistency: the FEP-substrate calibration must be consistent with the gamma-entrainment calibration (interface 04) since both operate at cortical scales. The two calibrations should differ in their target timescale (gamma is the cortical-microcircuit-fast scale; FEP perceptual is roughly the same scale; FEP deliberation is the working-memory scale), but they should not contradict each other. This consistency is verifiable.

## What this correspondence does and does not establish

It does not establish that the present equation is the underlying mathematical description of free-energy minimization. The appropriate description is the variational-inference framework as developed by Friston and collaborators, with its own machinery of generalized coordinates, precision-weighting, and hierarchical message passing. The present equation, applied to the cortical substrate with hierarchical predictive coding, captures the structural form of the dynamics; the specific functional form of the free-energy gradient may differ from the present equation's specific terms.

It does not establish that all adaptive systems must be exactly described by the FEP. The principle has been advanced as a normative claim about self-organizing systems; whether every adaptive system in nature literally minimizes a variational free energy in the mathematical sense remains an open empirical question (Andrews 2021; Aguilera et al. 2021). The structural correspondence here is at the level of the triangle's instantiation: whatever the precise functional form of the free energy in a given substrate, the substrate must have the triangle structure to support adaptive behavior under uncertainty.

It does establish that the equation's structural form recurs at the level of FEP-style adaptive dynamics. This is a particularly strong entry in the cross-domain ledger because the FEP itself is a structural framework that identifies the same triangle structure across substrates (cortex, immune system, gene regulation, artificial agents). The present equation and the FEP converge on the same structural form from different starting points: the present equation from physics-philosophy axioms about persistent extended entities, the FEP from variational-Bayesian information theory applied to self-organization. The convergence is informative because the two frameworks are unmotivated by each other; they reach the same triangle structure.

## Common dismissals and why they do not apply

**"The Free Energy Principle is controversial; not all adaptive systems literally minimize free energy."** The controversy is acknowledged. Andrews (2021) and others have raised methodological concerns about the FEP's status as a normative claim versus a descriptive one. The structural correspondence here does not depend on the strong-FEP claim being correct in all cases. It depends on the weaker claim: substrates that sustain adaptive behavior under sensory uncertainty exhibit the triangle structure, which is what the FEP identifies (whether or not the system literally minimizes a variational free energy in the mathematical sense). The structural form is robust across the controversial-strong-FEP-claim vs descriptive-FEP-claim distinction.

**"Friston's framework is too general to be testable."** A common critique. The structural-realist methodology (methodology/01) explicitly addresses this: theories of structural form are evaluated by cross-domain coherence (criterion 4), not by single-experiment refutation of the global claim. Local predictions of the FEP within specific substrates (specific cortical-circuit predictions, specific behavioral predictions) remain locally testable in the standard way. The global structural claim of the FEP and the present equation is evaluated by the cross-domain coherence the two frameworks together establish.

**"This is mapping mathematics to mathematics; it adds nothing."** The mapping is at the level of mathematical form (the predictive-coding hierarchy as auxiliary-field hierarchy), and this is what the structural-realist methodology requires for criterion 4 to be satisfied. The convergence is informative: two mathematical frameworks developed from different starting points produce the same structural form. The convergence does add something beyond either framework alone: it strengthens the structural-realist claim that the form captures something invariant about persistent adaptive systems, regardless of the specific framework that derives it.

## Locally testable predictions and observational signatures

The structural claim of this interface (free-energy minimization and active inference instantiate the same triangle as the present equation in a variational-dynamics substrate) is evaluated by cross-domain coherence (methodology/04 criterion 4), not by single-experiment refutation. The following are *local* predictions that can be tested by coupled-regime numerical or empirical methods (per principles/03-coupling.md). Inconsistent evidence would shift evidentiary weight against this interface's specific calibration under criterion 4 (cross-domain coherence), without bearing on the global structural claim.

- **Prediction P12.1: Predictive-coding timescale separation matches the dimensional rescaling.** The structural prediction is that the cortical predictive-coding hierarchy's timescale separation across levels follows the same scaling as the dimensional rescaling result $\Sigma\lambda/|\Lambda| \sim 1/d$ ([`../results/06-dimensional-rescaling.md`](../results/06-dimensional-rescaling.md)), where $d$ is the effective dimensionality of the perceptual feature being integrated. Higher-level cortical areas integrating over more abstract features (higher effective $d$) should have proportionally slower timescales.
  - How to test: comparative analysis of cortical timescales across regions (existing electrophysiology and fMRI data); correlate with the effective dimensionality of the features each region encodes.
  - What would constitute confirmation: timescale and effective dimensionality correlate as predicted.
  - What would constitute evidence inconsistent with this calibration: no correlation, or anti-correlation.
  - Status: partially tested. The intrinsic-timescale-hierarchy literature (Murray et al. 2014; Honey et al. 2012) documents cortical timescale heterogeneity; the specific structural correlation has not been isolated.

- **Prediction P12.2: Active-inference agents with multi-timescale memory exhibit anti-collapse in optimization.** The structural prediction is that active-inference agents implemented with explicit hierarchical predictive-coding memory will exhibit the same anti-collapse property in their internal-model optimization dynamics that Memory-NLS exhibits in neural-network training ([`../results/08-optimization-collapse-empirical.md`](../results/08-optimization-collapse-empirical.md)). Active-inference agents with only flat (single-timescale) models should be susceptible to catastrophic-failure modes during sustained training, while hierarchical agents should not.
  - How to test: train two active-inference agents on the same task, one with flat model and one with hierarchical multi-timescale model; compare training-trajectory stability and incidence of model collapse.
  - What would constitute confirmation: hierarchical agent shows monotonic descent and stability; flat agent exhibits catastrophic events.
  - What would constitute evidence inconsistent with this calibration: no difference, or hierarchical agent is less stable.
  - Status: untested. The active-inference robotics literature (Lanillos-Cheng 2020; Pio-Lopez et al. 2016) provides the experimental infrastructure; the specific anti-collapse prediction has not been isolated.

- **Prediction P12.3: Psychiatric-disorder categories partition by triangle-element dysregulation.** The structural prediction is that psychiatric disorders (schizophrenia, depression, OCD, autism spectrum) can be mapped to dysregulation of specific triangle elements: P1 dysregulation (intrinsic dynamics aberrant; tracking abnormalities, hallucination), P2 dysregulation (memory and model integrity compromised; rumination, fixed false beliefs), P3 dysregulation (sensory or active coupling abnormal; sensory hypersensitivity, action paralysis). Each disorder should align with predominant dysregulation of one or two triangle elements.
  - How to test: comparison of disorder taxonomies (DSM-5 or RDoC categories) with the predicted partition.
  - What would constitute confirmation: substantial alignment of disorder categories with triangle-element dysregulation patterns.
  - What would constitute evidence inconsistent with this calibration: no systematic alignment.
  - Status: partially anticipated. Friston's computational-psychiatry program (Friston-Stephan-Montague-Dolan 2014) has compatible framing; the specific structural-element partition has not been formalized.

## References

Cited as credit, not legitimization (per [`../methodology/01-structural-realism.md`](../methodology/01-structural-realism.md) "Prior art and credit"):

- Aguilera, M., Millidge, B., Tschantz, A., & Buckley, C. L. (2021). How particular is the physics of the free energy principle? *Physics of Life Reviews* **40**, 24.
- Andrews, M. (2021). The math is not the territory: navigating the free energy principle. *Biology & Philosophy* **36**, 30.
- Bastos, A. M., Usrey, W. M., Adams, R. A., Mangun, G. R., Fries, P., & Friston, K. J. (2012). Canonical microcircuits for predictive coding. *Neuron* **76**, 695.
- Buckley, C. L., Kim, C. S., McGregor, S., & Seth, A. K. (2017). The free energy principle for action and perception: a mathematical review. *Journal of Mathematical Psychology* **81**, 55.
- Friston, K. (2008). Hierarchical models in the brain. *PLoS Computational Biology* **4**, e1000211.
- Friston, K. (2010). The free-energy principle: a unified brain theory? *Nature Reviews Neuroscience* **11**, 127.
- Friston, K., Buzsaki, G., & Kiebel, S. (2017). The intrinsic active brain. *Trends in Cognitive Sciences* **22**, 165.
- Friston, K. J., Levin, M., Sengupta, B., & Pezzulo, G. (2015). Knowing one's place: a free-energy approach to pattern regulation. *Journal of the Royal Society Interface* **12**, 20141383.
- Friston, K. J., Stephan, K. E., Montague, R., & Dolan, R. J. (2014). Computational psychiatry: the brain as a phantastic organ. *The Lancet Psychiatry* **1**, 148.
- Honey, C. J., Thesen, T., Donner, T. H., Silbert, L. J., Carlson, C. E., Devinsky, O., Doyle, W. K., Rubin, N., Heeger, D. J., & Hasson, U. (2012). Slow cortical dynamics and the accumulation of information over long timescales. *Neuron* **76**, 423.
- Lanillos, P., & Cheng, G. (2020). Active inference with function learning for robot body perception. *International Workshop on Continual Unsupervised Sensorimotor Learning*.
- Murray, J. D., Bernacchia, A., Freedman, D. J., Romo, R., Wallis, J. D., Cai, X., Padoa-Schioppa, C., Pasternak, T., Seo, H., Lee, D., & Wang, X.-J. (2014). A hierarchy of intrinsic timescales across primate cortex. *Nature Neuroscience* **17**, 1661.
- Parr, T., Pezzulo, G., & Friston, K. J. (2022). *Active Inference: The Free Energy Principle in Mind, Brain, and Behavior*. MIT Press.
- Pio-Lopez, L., Nizard, A., Friston, K., & Pezzulo, G. (2016). Active inference and robot control: a case study. *Journal of the Royal Society Interface* **13**, 20160616.
- Pradeu, T., Jaeger, S., & Vivier, E. (2013). The speed of change: towards a discontinuity theory of immunity? *Nature Reviews Immunology* **13**, 764.
