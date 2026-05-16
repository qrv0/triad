# Open problem 07: Additional cross-domain substrates

**Status:** Open. Candidates identified; documentation not yet written.

## Precise statement

The cross-domain coherence criterion (methodology/04 criterion 4) is currently operative across nine documented interfaces in [`../interfaces/`](../interfaces/): seven substrate-instantiations of the structural form (NLS systems, BAO, cymatics, gamma entrainment, archaeoacoustic resonance, state space models, cosmological expansion) plus two convergent-program engagements (mechanistic interpretability, critical brain). The mechanistic-interpretability and critical-brain interfaces address contemporary research programs rather than new physical substrates; they are not candidates for this open problem. Five additional candidate substrates have been identified as candidate instantiations of the structural form not yet documented. Each requires literature review, careful structural mapping, and documentation in the standard interface template. The open problem is to develop these five into full interface documents.

## What is known

The five candidate substrates with preliminary structural mapping:

1. **Kuramoto synchronization.** The Kuramoto model of coupled phase oscillators is P1+P3 in its base form (oscillators coupled to environment via mean-field interaction). Generalized Kuramoto with memory kernels (Strogatz; Pikovsky-Rosenblum-Kurths) extends to P1+P2+P3. The mapping is mathematically tight: phase variables ↔ field arguments; coupling strengths ↔ $\Lambda$; memory kernels ↔ $V_{\text{mem}}$. Evidentiary status: candidate for "mathematical equivalence" tier (alongside [`../interfaces/06-state-space-models.md`](../interfaces/06-state-space-models.md)).

2. **Immune affinity maturation.** B-cell affinity maturation in germinal centers has triangle structure: antibody repertoire (field $\Psi$) + somatic hypermutation memory ($V_{\text{mem}}$) + antigen environment (coupling). Spontaneous selection of specific antibody clones from continuous repertoire is analogous to BCC selection from Gaussian initial state. Cites Mesin et al. (2016 Cell); Victora-Nussenzweig (2022 Annu Rev Immunol). Evidentiary status: structural correspondence.

3. **Friston Free Energy Principle / active inference.** Living systems minimize variational free energy via coupling to environment; active inference updates internal model based on prediction errors. Mapping: internal states ↔ field; generative model ↔ $V_{\text{mem}}$; sensory observations and actions ↔ environmental coupling. Friston-Buzsaki-Kiebel hierarchical predictive coding has explicit multi-timescale memory matching $\nu_j$ hierarchy. Cites Friston (2010 Nat Rev Neurosci); Parr-Pezzulo-Friston (2022 MIT Press). Evidentiary status: structural with explicit hierarchical mapping; potentially as strong as the SSM correspondence if developed rigorously.

4. **Active matter.** Self-propelled particles, flocks, swarms (Vicsek, Toner-Tu, active gels) have energy injection (coupling to environment) + interaction (self-coupling) + dynamics (extended oscillatory systems). Spontaneous symmetry breaking analogous to BCC selection. Cites Marchetti et al. (2013 RMP); Ramaswamy (2017 J Stat Mech); Bechinger et al. (2016 RMP). Evidentiary status: structural correspondence in soft-matter substrate.

5. **Self-organized criticality.** Bak-Tang-Wiesenfeld sand-pile, neuronal avalanches (Beggs-Plenz). Systems self-organize to critical point without external parameter tuning. The MNSM selects specific state (BCC + broadband absorption) from continuum without external tuning, which may or may not be SOC in the technical sense. Cites Bak-Tang-Wiesenfeld (1987 PRL); Beggs-Plenz (2003 J Neurosci); Mora-Bialek (2011 J Stat Phys). Evidentiary status: structural similarity; technical SOC status open.

## What is missing

- Full interface documents for each of the five candidates, following the template in [`../interfaces/`](../interfaces/) (Physical setup / Structural correspondence / What is same and different / What this correspondence is and is not / Common dismissals / Locally testable predictions / References).
- Term-by-term mathematical mappings (where possible) and clear identification of where the mapping is mathematical (no calibration) vs structural (calibration acknowledged).
- Updates to the cross-domain wheel SVG if these substrates are promoted to the wheel (currently 9-node after the Phase 6 expansion).

## What would constitute progress

- Five new interface files in [`../interfaces/`](../interfaces/), each substantive (40-180 lines depending on the depth of the mapping).
- Each file with peer-reviewed primary literature citations.
- Each file with explicit evidentiary status (mathematical equivalence, calibration-dependent structural correspondence, or mechanism-shape and convergent-program correspondence per the three-class division in [`../interfaces/README.md`](../interfaces/README.md)).
- Each file with "Common dismissals" and "Locally testable predictions" sections.
- Decision on the wheel: expand from the current 9-node layout to 14 (5 new substrates added on top of the Phase 6 expansion) or keep at 9 with new interfaces listed separately.

## Suggested approaches

- **One interface at a time.** Each interface is independent; the order can be chosen for maximum impact. Friston FEP is the most consequential (active research program; potentially mathematical-equivalence tier); Kuramoto is the cleanest (well-established mathematical literature); immune is the most biologically distinct (independent confirmation of the cross-domain claim in living tissue beyond gamma entrainment); active matter is the most contemporary (recent literature explosion); SOC is the most universality-claim.
- **Literature review per candidate.** Each candidate requires a focused literature review identifying the primary sources, the canonical formulation, the connections to the MNSM equation, and the dismissals likely from the substrate community.

## Connections to existing repo content

- [`../interfaces/README.md`](../interfaces/README.md): the existing nine interfaces set the template and the bar; the three-class evidentiary division catalogued there is where each new substrate must be situated.
- [`../methodology/04-the-six-criteria.md`](../methodology/04-the-six-criteria.md) criterion 4: each new interface increases cross-domain coherence quantitatively.
- [`../principles/README.md`](../principles/README.md) section "Why exactly three": the triangle topology argument generalizes to predict that any substrate sustaining the triangle is an instantiation; the additional substrates here are candidates the argument predicts should exist.
- [`02-phase-diagram.md`](02-phase-diagram.md): each new substrate's calibration places it at a specific region of the phase diagram.
- [`08-calibration-philosophy.md`](08-calibration-philosophy.md): the calibration choices for each new substrate must respect cross-substrate consistency.
