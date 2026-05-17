# Research agenda

This document states the research program of mnsm explicitly: what is being worked on, what would constitute progress at various timescales, what convergent programs exist in the literature, and how to engage.

The work is structured as a research program rather than a finished body. Open questions are documented in [`open-problems/`](open-problems/); the methodology is in [`methodology/`](methodology/); the principal claims are in [`principles/`](principles/), [`equation/`](equation/), [`interfaces/`](interfaces/), and [`results/`](results/). This document organizes the program by horizon: what is the next six months of work, what is the twelve-month horizon, what is the twenty-four-month horizon.

## What "progress" means here

Progress is structural-realist: a result that strengthens cross-domain coherence (criterion 4), tightens the analytical derivation (criterion 1), extends generative scope (criterion 3), or operationalizes a moderate mapping into a strong one. Progress is not "beats benchmark X by Y percent" or "submits to journal Z"; the methodological frame in [`methodology/`](methodology/) rules out the former as the wrong evaluation criterion and the latter as the wrong validation path.

Locally-testable quantitative predictions are evaluated by coupled-regime numerical reproduction per [`methodology/02-limits-of-falsification.md`](methodology/02-limits-of-falsification.md). A failed reproduction, a counter-derivation, or an empirical observation inconsistent with a predicted observable contributes evidence inconsistent with the specific calibration under criterion 4 and prompts investigation of calibration, auxiliary numerical assumptions (Duhem-Quine), or implementation. The global structural claim is evaluated by the six criteria of [`methodology/04-the-six-criteria.md`](methodology/04-the-six-criteria.md); inconsistent local evidence shifts weight under criterion 4 without single-experiment-refuting the structural claim.

## Current state of the research

The repository documents the equation, its derivation from P1+P2+P3, and the cross-domain instances where the same structural form independently appears. Substantive contributions to date:

**Numerical findings on the equation itself** (in [`results/`](results/)):

- 3D supercritical anti-collapse phenomenology with $\Sigma\lambda \sim |\Lambda|/d$ dimensional rescaling: results/04, results/06, results/24.
- Spontaneous Bravais (BCC) selection of the released crystalline state at $\Sigma\lambda \sim 1.5$: results/05.
- Internal vibrational spectrum of the crystalline state (2D and 3D): results/03, results/25.
- Phase-diagram slices in the $(\Sigma\lambda, \gamma_0)$ plane at $d \in \{2, 3, 4\}$ with multi-seed reproducibility: results/26, results/27, results/28.
- Higher-dimensional rescaling at $d=4, d=5, d=6$ with bath coupling: results/10, results/15, results/24.
- Two-convention audit ($\sigma=0.4$ unnormalized vs $\sigma=0.5$ normalized) and $L$-robustness check: results/30, results/31, results/32.
- Cross-substrate empirical instance at 70M neural network parameters: documented in implementation depth in the [mnsm-ml](https://github.com/qrv0/mnsm-ml) spinoff.

**Cross-domain instances** ([`interfaces/`](interfaces/) at 20 substrates here + 2 in the [mnsm-ml](https://github.com/qrv0/mnsm-ml) spinoff): NLS family, BAO cosmology, cymatics, gamma neural entrainment, archaeoacoustic resonance, cosmological expansion, critical brain, Kuramoto memory, immune affinity maturation, Friston FEP, active matter, SOC, cardiac dynamics, gene regulation/circadian, ecosystem dynamics, pseudomode quantum, Maxwell/Prony viscoelasticity, warm inflation, Hawkes processes, earthquake cycle (in this repo); plus structured state space models and mechanistic interpretability (in mnsm-ml). Each interface document derives its structural mapping and lists locally testable predictions evaluated under cross-domain coherence.

**Methodology** ([`methodology/`](methodology/)): structural realism (01), the limits of falsification (02), how to evaluate (03), the six criteria (04), implications for AGI (05), calibration philosophy (06), time as calibration (07), Mori-Zwanzig foundation (08), tautology-objection response (09). The methodological frame is articulated as positive structural-realist position, not as audit infrastructure.

**Solver and reproducibility** ([`implementation/physics/`](implementation/physics/), [`tests/`](tests/)): CuPy 3D Strang split-step solver with norm/FDT/dissipation/memory conservation diagnostics to machine precision. All reported numerics reproduce bit-for-bit at fixed seed on identical hardware.

**Cross-domain literature integration**: archaeoacoustic site spectrum audit (results/23) and cross-chamber check (results/29) integrating peer-reviewed measurements from Newgrange, Hypogeum, Göbekli Tepe; perturbative analytical sketch of the anti-collapse mechanism in open-problems/01.

## Six-month horizon

Items at this horizon are tractable with focused effort. They strengthen the existing claims rather than extending into new territory.

- **Analytical derivation of the anti-collapse mechanism** ([`open-problems/01-analytical-anti-collapse.md`](open-problems/01-analytical-anti-collapse.md)). Currently the anti-collapse separation ratio is demonstrated numerically only. An analytical derivation that yields the separation as a function of $(\Lambda, \Sigma\lambda, \nu_{\text{slow}}, d)$ would move the result from "numerical observation" to "derived theorem with numerical confirmation." Constitutes progress: a perturbative derivation linearizing around the collapse focal region, with one-loop overshoot magnitude as the leading result.

- **Phase diagram of the equation** ([`open-problems/02-phase-diagram.md`](open-problems/02-phase-diagram.md)). The full $(\Lambda, \Sigma\lambda, \nu_j, \sigma, \Gamma, T)$ parameter space mapped with regime classification. Constitutes progress: a figure (or set of figures) presenting 2D slices with each region color-coded by qualitative regime, with reproduction scripts.

- **Locally testable predictions per interface** (Phase 2 of the active-expansion plan; the existing seven interfaces 01-07 are done, the two new interfaces 08-09 include the section from the start). Each interface document in [`interfaces/`](interfaces/) has an explicit "Locally testable predictions and observational signatures" section distinguishing local predictions (falsifiable by standard experiment) from the global structural claim.

- **Calibration philosophy formalized** ([`open-problems/08-calibration-philosophy.md`](open-problems/08-calibration-philosophy.md), promoted to `methodology/06-calibration-philosophy.md`). A decision procedure for when calibrations matter and how cross-interface consistency operates. Constitutes progress: the methodology document is written and the case-by-case treatment in interfaces 04 and 05 is referenced to the formalization.

- **Sharpening the predictions named in interfaces 10 through 17.** The Phase-3 interfaces each name three locally-testable predictions. Sharpening these into experimental protocols (vaccine timing for immune, alternans threshold for cardiac, chimera-state stability for Kuramoto, etc.) is the next work on those interfaces. Constitutes progress: at least one prediction from each interface moved from "untested" to "partially tested" or "tested" status.

## Twelve-month horizon

Items at this horizon are substantial work requiring sustained effort.

- **Renormalization-group analysis** ([`open-problems/04-continuum-rg.md`](open-problems/04-continuum-rg.md)). One-loop beta functions for the principal couplings; fixed-point structure; identification of universal vs non-universal features. Constitutes progress: a derivation in standard field-theoretic format with cross-references to the established universality-class catalogue (Hohenberg-Halperin Models A-J).

- **Additional cross-domain interfaces beyond the current set.** Candidates that the structural argument predicts but are not yet documented: glassy systems and aging; granular matter; market dynamics in econophysics; plant signaling. Each requires literature review and the standard logic-led interface template. Constitutes progress: further cross-domain coherence; the wheel either expands further or splits into core + extensions.

- **Engineering pattern for moderate AGI requirements** ([`open-problems/06-engineering-moderate-requirements.md`](open-problems/06-engineering-moderate-requirements.md)). Concrete architectural patterns satisfying methodology/05 requirements 7 and 8 (environmental coupling without identity loss; stable self-modification), demonstrated at small scale. Constitutes progress: implementable patterns documented in the [`mnsm-ml`](https://github.com/qrv0/mnsm-ml) spinoff with reproducible code.

- **Sharpening the predictions named in the mech-interp and critical-brain interfaces.** The mechanistic-interpretability interface (in the [`mnsm-ml`](https://github.com/qrv0/mnsm-ml) spinoff) and the critical-brain interface ([`interfaces/09-critical-brain.md`](interfaces/09-critical-brain.md)) name specific locally-testable predictions. Sharpening these into experimental protocols at small scale (for the SAE-on-SSM predictions in the spinoff) and at standard-methodology scale (for the avalanche-and-1/f predictions in the critical-brain interface) is the next work on those interfaces. Constitutes progress: at least one prediction from each interface moved from "untested" to "tested" status.

## Twenty-four-month horizon

Items at this horizon are research items in the strong sense: genuinely open mathematical questions whose resolution is not predetermined.

- **Quantum extension** ([`open-problems/05-quantum-extension.md`](open-problems/05-quantum-extension.md)). Path-integral formulation of the full equation; one-loop quantum corrections to the classical anti-collapse mechanism; Schwinger-Keldysh closed-time-path treatment for the stochastic component. Outcome uncertain.

- **Topological characterization** ([`open-problems/03-topological-characterization.md`](open-problems/03-topological-characterization.md)). Whether the BCC selection is a topological phase transition; computation of candidate topological invariants. Outcome uncertain; could be a clean positive result, a clean negative result, or a long open question.

- **Multi-language implementations.** JAX (for the ML research community), Julia (for the physics research community), C reference (for pedagogy). Constitutes progress: each port with cross-validation against the CuPy reference and CI infrastructure ensuring numerical equivalence.

- **Full predictive cosmology from the structural reading** of [`interfaces/07-cosmological-expansion.md`](interfaces/07-cosmological-expansion.md). The current cosmological interface identifies the unified mechanism shape but is not a predictive cosmology. Working it out into a predictive framework comparable to standard ΛCDM is substantial and would require either independent collaboration with cosmologists or sustained development of the framework. Outcome uncertain.

## Connection to convergent programs

The following active research programs are working on questions that share structural elements with mnsm. Engagement with these programs is welcomed and would strengthen cross-domain coherence.

- **Anthropic interpretability** (Olah, Elhage, Bricken). Sparse autoencoders, superposition, polysemantic neurons. Convergent observation: attention-only systems have substrate-specific representational structure that the MNSM structural argument predicts as the absence of the multi-timescale memory hierarchy. Structural mapping documented in [`mnsm-ml/interfaces/02-mechanistic-interpretability.md`](https://github.com/qrv0/mnsm-ml/blob/main/interfaces/02-mechanistic-interpretability.md); further engagement at the level of empirical testing the predictions named in that document is the next direction.

- **Friston Free Energy Principle and active inference** (Friston, Parr, Pezzulo). Living systems minimize variational free energy via environmental coupling. Structural mapping documented in [`interfaces/12-friston-free-energy.md`](interfaces/12-friston-free-energy.md); the convergence between FEP and MNSM as triangle-structure frameworks is now explicit.

- **Critical brain hypothesis** (Beggs, Plenz, Chialvo, Mora-Bialek). Brain operates at edge of phase transition; observable signatures include neuronal avalanches, power-law distributions, broadband response. Structural mapping documented in [`interfaces/09-critical-brain.md`](interfaces/09-critical-brain.md); the SOC-vs-mechanism-shape question (whether MNSM's release transition is technically SOC) is left as open work.

- **Self-organized criticality** (Bak, Tang, Wiesenfeld; later work by many authors). Systems organize to critical point without parameter tuning. Whether MNSM's release transition is technically SOC is open.

- **Continual learning and catastrophic forgetting** (Kirkpatrick, French, Parisi). Engineering the moderate AGI requirements 7 and 8 connects directly with this literature.

- **Topological matter** (Hasan-Kane, Kitaev, Wen). If BCC selection has topological character, the connection is to the established topological-phase classification.

## How to engage

Contributions are welcomed. The expected forms:

- **Working on an open problem.** Pick a document in [`open-problems/`](open-problems/), develop a partial or complete resolution, submit a pull request adding the result to the relevant section of the repo (results, equation, methodology, or interfaces depending on the result type). Update the open problem document to reflect the new state.

- **Adding an interface.** Identify a substrate where the structural form appears, written up in the standard interface template (see existing interfaces 01-07 as models). The bar: peer-reviewed primary literature for the substrate; mapping at the level of mathematical form or structural mechanism, not analogy; explicit evidentiary status (mathematical equivalence, structural correspondence, calibrated correspondence).

- **Evidence inconsistent with a specific prediction calibration.** If a locally-testable prediction (in any interface's "Locally testable predictions" section) is not reproduced by a test, document the inconsistent evidence and submit; the interface evidentiary status shifts to "tested, inconsistent" under criterion 4, and the prompt becomes investigation of the calibration, auxiliary numerical assumptions (Duhem-Quine), or implementation. Inconsistent evidence does not falsify the structural claim.

- **Engagement at the conceptual level.** [GitHub Discussions on this repository](https://github.com/qrv0/mnsm/discussions) is the space for discussion of the program at the level of structure, methodology, and connection to other work. Discussion threads do not produce pull requests directly but shape the direction of subsequent work.

Contributors should be familiar with the operational constraints in [`CLAUDE.md`](CLAUDE.md) (these apply to human contributors as well as AI-assisted contributions) and the methodological frame in [`methodology/`](methodology/) (no Popperian falsification of the global structural claim; no competitive ML vocabulary; no scale-or-benchmark-driven framing; structural realism is the evaluation standard).

## Out of scope

The following are deliberately not on the research agenda, per the methodology and CLAUDE.md operational constraints:

- Scaling Memory-NLS to billions of parameters and competing on standard sequence-modeling benchmarks (CLAUDE.md Rule 7b).
- Comparative-benchmark studies framed as "Memory-NLS vs Transformer" with the framing of declaring a winner (CLAUDE.md Rule 7a; comparison-as-differentiation is allowed, comparison-as-competition is not).
- Seeking peer-review credentialing or academic affiliation as the validation path (CLAUDE.md Rule 5).
- Building a working AGI implementation as a deliverable ([`methodology/05-implications-for-agi.md`](methodology/05-implications-for-agi.md) explicitly disclaims this).
- Resolving the hard problem of consciousness ([`principles/03-coupling.md`](principles/03-coupling.md) "logical consequence of P3" is a structural claim; metaphysics of subjective experience is bracketed).
- Solving the alignment problem (orthogonal to architectural requirements; the work has nothing to say about goals, values, or safety).

These items are out of scope not because they are unimportant but because they require different methodologies and different work. The agenda above is what the present program is set up to advance.
