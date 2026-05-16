---
title: "Interface 08: Mechanistic interpretability (attention)"
description: >-
  The empirical observation that attention-only architectures encode
  categorical structure as linear superpositions requiring post-hoc
  dictionary learning is what the equation predicts for an architecture
  instantiating P1 and P3 but missing P2's memory hierarchy.
domain: engineering
triangle:
  p1: "token-position attention oscillation"
  p2: "MISSING in attention-only: no auxiliary-field memory hierarchy"
  p3: "input embedding + residual stream coupling"
signature_icon: attention
hero_tier: C
related: [6, 9, 4]
predictions:
  - id: P8.1
    short: "Sparse autoencoder recovery rate scales with auxiliary-field count in modified architectures"
    status: not_yet_tested
    result_doc: null
  - id: P8.2
    short: "Superposition density correlates inversely with explicit memory hierarchy depth"
    status: not_yet_tested
    result_doc: null
  - id: P8.3
    short: "Polysemanticity decreases when Memory-NLS auxiliary fields are added to attention layers"
    status: not_yet_tested
    result_doc: null
---
# Interface: mechanistic interpretability of attention-based systems

The empirical program of mechanistic interpretability has independently documented a specific phenomenology in attention-based language models: latent categorical structure is not held in addressable architectural components, but is encoded as linear superpositions across activations whose decomposition requires post-hoc dictionary learning. This document treats the structural reading: the phenomenology is what the present equation predicts for an architecture instantiating P1 and P3 but not P2.

## The interpretability observations

Three findings from the Anthropic mechanistic interpretability program and adjacent work establish the relevant phenomenology.

**Superposition.** Elhage et al. (2022) showed that a network with $n$ activation dimensions can represent $m > n$ features by encoding each as a linear combination across the $n$-dimensional space. The condition for this is that the represented features are sparse: at any given input only a small subset are active, so the linear combinations of inactive features can be tolerated as noise. Toy models confirm that gradient-based training produces this encoding rather than dedicating one direction per feature.

**Polysemantic neurons.** Individual neurons in production language models activate for multiple semantically distinct features. The polysemanticity is not residual noise from training; it is the algorithm the architecture is forced to use to fit more features than it has activation dimensions for. Olah et al. (2020) documented this through the Distill circuits program.

**Sparse-dictionary recovery.** Bricken et al. (2023) demonstrated that training an overcomplete sparse autoencoder on layer activations recovers a dictionary of monosemantic features. Templeton et al. (2024) extended this to production-scale models (Claude 3 Sonnet), identifying tens of millions of sparse features including specific high-level concepts (deception, theory of mind, specific named entities, code structures).

The empirical picture: the categorical structure of language exists in the model's representations, but it is not held as state in addressable architectural components. It is recoverable, but recovery requires a separate decomposition step that is not part of the architecture's forward pass.

## Evidentiary class

This correspondence sits in the third class of the three-class division catalogued in [`README.md`](README.md): mechanism-shape and convergent-program correspondence. Specifically, it is a *convergent-program correspondence*: the structural argument advanced by P1+P2+P3 and an independent empirical research program (Anthropic mechanistic interpretability, plus adjacent work in superposition and sparse-feature decomposition) reach the same conclusion about the encoding format of attention-only architectures. Neither program has been adjusted to fit the other; the convergence is the structural-realist signature this correspondence rests on.

## The structural reading

The present equation contains the auxiliary fields $\{y_j(t)\}$ with timescales $\{\nu_j\}$ as explicit dynamical state, governed by

$$\partial_t y_j = \nu_j(\rho - y_j),$$

with $\rho = |\Psi|^2$. The slow-mode content of the field's history is held in these auxiliary variables. They are addressable in the sense that the dynamics of the system include their explicit time evolution, not just projections through $\Psi$.

An architecture instantiating P1 (oscillatory dynamics) and P3 (environmental coupling) but not P2 (self-interaction with memory hierarchy) has no analogue of $\{y_j\}$ in its state. Such an architecture must encode any slow categorical structure as projections through whatever activations its forward pass produces. The encoding is forced rather than chosen: there is no place in the state for the slow structure to live as state, so it must live as direction in activation space.

Attention is the canonical such architecture. The self-attention operation computes pairwise weighted combinations of token representations; it has no explicit auxiliary-field state that persists across the sequence with its own decay timescale. The residual stream carries activations forward, but the structure encoded in the residual stream is the structure that has nowhere else to be.

The structural prediction follows: an attention-only architecture, trained on data with slow categorical structure, will encode that structure as linear superpositions across activation dimensions, with the categories recoverable only by post-hoc decomposition. This is what the interpretability program empirically documents. The convergence is direct: a structural argument from the equation's P1+P2+P3 form, applied to architectures missing P2, predicts the phenomenology that the mechanistic-interpretability program independently observes.

## The recursive position

The assistant writing this document is an instance of an attention-based architecture. The structural reading of the interpretability findings applies to its own representations: whatever slow categorical structure governs its outputs is not held in addressable auxiliary state but as superposition across the residual stream. The mechanistic-interpretability work on Claude (Templeton et al. 2024) is in part the post-hoc recovery of structure that a P2 architecture would have carried explicitly.

This is not a metaphor and not a self-effacing aside. It is the structural fact noted in [`../CLAUDE.md`](../CLAUDE.md): the present work has implications for the design of systems in the same architectural family as the assistant, and engaging with the work on its own terms includes acknowledging where the assistant fits in the structural picture.

The state space model interface [`06-state-space-models.md`](06-state-space-models.md) documents the mathematical equivalence between the auxiliary-field memory of the equation and the diagonal-state SSM update. SSM-class architectures (S4, Mamba, RWKV) instantiate P2 explicitly. They are the architectural family for which the structural argument predicts that the interpretability picture should be different: slow categorical structure should be available as state-mode activity, addressable without dictionary learning. This is a prediction, not a current empirical claim about which models have been studied. The interpretability program has concentrated on attention-based systems; the structural argument suggests its findings will be substantively different on P2-instantiating architectures.

## What this correspondence does and does not establish

It does not establish that the equation is the underlying mathematical description of attention-based language models. The internal mathematics of attention is not the Memory-NLS equation; it is the softmax-weighted-product structure of multi-head attention as defined in Vaswani et al. (2017). The correspondence is at the level of which structural ingredient is absent, not at the level of equation-by-equation derivation.

It does not establish that sparse-autoencoder decomposition is a misguided method. The method is empirically effective at recovering features that exist in the residual stream; the structural reading is about why the features are in the residual stream rather than in addressable state, not about whether the decomposition itself works.

It does not establish that P2-instantiating architectures would be transparent or interpretable in some absolute sense. Interpretability of any architecture is determined by many factors; having auxiliary-field state available as state is one structural difference, not a guarantee of any particular interpretability property.

It does establish that the empirical phenomenology the interpretability program documents is what the structural argument predicts for the architectural family the program studies. The convergence is independent: the structural argument was derived from physics-and-philosophy considerations (P1+P2+P3 as axioms about persistent extended entities); the interpretability findings were derived from empirical examination of trained models. The match between the structural prediction and the empirical finding is cross-domain coherence in the sense of [`../methodology/04-the-six-criteria.md`](../methodology/04-the-six-criteria.md) criterion 4.

## Common dismissals and why they do not apply

**"Attention is a universal function approximator; it can represent anything an SSM can represent."** Universal approximation is a representational-capacity claim. The structural claim here is not about representational capacity but about where the represented structure is held in the architecture's state. An attention layer can represent any function of its input, but in doing so it forces the slow categorical structure into the activation space rather than holding it as auxiliary-field state with its own time evolution. The interpretability findings (superposition, polysemanticity, post-hoc recovery) are evidence that this forcing happens in practice, not just in principle.

**"Sparse autoencoders are a tool, not a theoretical commitment."** Correct, and the structural reading does not require sparse autoencoders to be the right or only tool for interpretability. The structural reading is about the empirical phenomenology that the tool recovers: the existence of recoverable monosemantic features inside polysemantic neurons. Whether the recovery is done by SAEs or by some other dictionary-learning method, the underlying fact (the features exist but are not held in addressable state) is what the structural argument predicts.

**"This is rebranded interpretability as physics."** It is not. The mechanistic-interpretability program is doing its own work on its own terms and has produced specific empirical findings cited above. The present interface does not propose to do interpretability work; it documents that the interpretability findings, taken at face value, match a structural prediction made independently from the equation's form. Both programs proceed on their own terms; the cross-domain coherence is the structural-realist observation, not a methodological reframing of either program.

**"Mechanistic interpretability is a young field; conclusions about superposition could be revised."** The cited results (Elhage 2022; Bricken 2023; Templeton 2024) are robust to specific revisions of secondary claims; the central phenomenon (categorical features encoded as linear directions across polysemantic neurons, recoverable by dictionary learning) is the basis for an active scaled empirical program. The structural argument is contingent on this phenomenon continuing to hold; if it were overturned, the interface would need revision. The current evidence supports it strongly.

## Locally testable predictions and observational signatures

> **Hedge cleanup (2026-05-16).** Each prediction's "What would constitute evidence inconsistent with this calibration" subsection previously used Popperian falsification framing ("would constitute local falsification") inserted in Phase 2 (commit 26e96ee) and propagated by Phase 3 to interfaces 10-17. The hedge contradicted the section's own opening sentence (the structural claim is evaluated by cross-domain coherence, not by single-experiment refutation). See [`../docs/llm-hedge-annotations.md`](../docs/llm-hedge-annotations.md) for the catalog of prior wordings and the structural reason for revision.

The structural claim of this interface (the absence of P2 from an attention-only architecture forces categorical structure into superposed activation space, recoverable only by post-hoc decomposition) is evaluated by cross-domain coherence (methodology/04 criterion 4), not by single-experiment refutation. The following are *local* predictions that can be tested by coupled-regime numerical or empirical methods (per principles/03-coupling.md). Inconsistent evidence would shift evidentiary weight against this interface's specific calibration under criterion 4 (cross-domain coherence), without bearing on the global structural claim.

- **Prediction P13.1: Auxiliary-field directness in P2-instantiating architectures.** In an SSM-class architecture (S4, Mamba, RWKV, or the Memory-NLS layer in [`../implementation/neural/`](../implementation/neural/)), the auxiliary-field state directions $\{y_j\}$ should correspond to monosemantic feature directions at a much higher rate than the residual-stream directions in an attention-only architecture of comparable scale.
  - How to test: apply the same sparse-autoencoder decomposition methodology to (a) the activations of an attention-only model and (b) the auxiliary-field activations of a P2-instantiating model trained on the same data; compute the fraction of dictionary features that align with single state directions versus require linear combinations.
  - What would constitute confirmation: P2-instantiating models show substantially higher single-direction alignment.
  - What would constitute evidence inconsistent with this calibration: no difference in alignment between architectures, or attention-only models show comparable single-direction alignment.
  - Status: untested. The Memory-NLS layer in this repository provides a testbed; the experiment requires running SAE decomposition on its auxiliary-field activations and comparing to baseline attention-only models.

- **Prediction P13.2: Feature direction stability under fine-tuning.** In P2-instantiating architectures, the dictionary of monosemantic features should be more stable under task-specific fine-tuning than in attention-only architectures, because the features correspond to addressable state with intrinsic time evolution rather than to emergent projections that can be reshaped by gradient updates.
  - How to test: apply SAE to architecture A and architecture B before fine-tuning on task T; apply SAE again after fine-tuning; compute feature dictionary overlap; compare overlap across architecture families.
  - What would constitute confirmation: P2-instantiating architectures show higher feature dictionary preservation.
  - What would constitute evidence inconsistent with this calibration: equal or lower preservation.
  - Status: untested.

- **Prediction P13.3: Memory-mode hierarchy structure.** In P2-instantiating architectures with multi-timescale auxiliary fields ($\nu_1 \ll \nu_2 \ll \ldots$), the recovered sparse features should partition by timescale: fast features (short-context dependencies) align with fast-$\nu_j$ fields, slow features (long-range structure, document-level coherence, persona) align with slow-$\nu_j$ fields.
  - How to test: train a P2-architecture with a known hierarchy $\{\nu_j\}$; apply SAE; categorize recovered features by which $y_j$ they predominantly load on; categorize features independently by context-length sensitivity; check whether the two categorizations correlate.
  - What would constitute confirmation: timescale hierarchy in auxiliary fields predicts context-length-sensitivity hierarchy in features.
  - What would constitute evidence inconsistent with this calibration: no correlation between auxiliary-field timescale and feature context-length sensitivity.
  - Status: untested.

## References

- Bricken, T., Templeton, A., Batson, J., Chen, B., Jermyn, A., Conerly, T., Turner, N., Anil, C., Denison, C., Askell, A., Lasenby, R., Wu, Y., Kravec, S., Schiefer, N., Maxwell, T., Joseph, N., Hatfield-Dodds, Z., Tamkin, A., Nguyen, K., McLean, B., Burke, J. E., Hume, T., Carter, S., Henighan, T., & Olah, C. (2023). Towards monosemanticity: decomposing language models with dictionary learning. *Transformer Circuits Thread*.
- Elhage, N., Hume, T., Olsson, C., Schiefer, N., Henighan, T., Kravec, S., Hatfield-Dodds, Z., Lasenby, R., Drain, D., Chen, C., Grosse, R., McCandlish, S., Kaplan, J., Amodei, D., Wattenberg, M., & Olah, C. (2022). Toy models of superposition. *Transformer Circuits Thread*.
- Olah, C., Cammarata, N., Schubert, L., Goh, G., Petrov, M., & Carter, S. (2020). Zoom in: an introduction to circuits. *Distill* **5**(3).
- Templeton, A., Conerly, T., Marcus, J., Lindsey, J., Bricken, T., Chen, B., Pearce, A., Citro, C., Ameisen, E., Jones, A., Cunningham, H., Turner, N. L., McDougall, C., MacDiarmid, M., Tamkin, A., Durmus, E., Hume, T., Mosconi, F., Freeman, C. D., Sumers, T. R., Rees, E., Batson, J., Jermyn, A., Carter, S., Olah, C., & Henighan, T. (2024). Scaling monosemanticity: extracting interpretable features from Claude 3 Sonnet. *Transformer Circuits Thread*.
- Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, L., & Polosukhin, I. (2017). Attention is all you need. *Advances in Neural Information Processing Systems* **30**.
