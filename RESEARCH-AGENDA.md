# Research agenda

This document states the research program of mnsm explicitly: what is being worked on, what would constitute progress at various timescales, what convergent programs exist in the literature, and how to engage.

The work is structured as a research program rather than a finished body. Open questions are documented in [`open-problems/`](open-problems/); the methodology is in [`methodology/`](methodology/); the principal claims are in [`principles/`](principles/), [`equation/`](equation/), [`interfaces/`](interfaces/), and [`results/`](results/). This document organizes the program by horizon: what is the next six months of work, what is the twelve-month horizon, what is the twenty-four-month horizon.

## What "progress" means here

Progress is structural-realist: a result that strengthens cross-domain coherence (criterion 4), tightens the analytical derivation (criterion 1), extends generative scope (criterion 3), or operationalizes a moderate mapping into a strong one. Progress is not "beats benchmark X by Y percent" or "submits to journal Z"; the methodological frame in [`methodology/`](methodology/) rules out the former as the wrong evaluation criterion and the latter as the wrong validation path.

Local-falsifiable predictions remain locally falsifiable per [`methodology/02-limits-of-falsification.md`](methodology/02-limits-of-falsification.md). A failed reproduction of a numerical result, a counter-derivation, an empirical observation contradicting a predicted observational signature, all constitute local falsification of specific claims. The global structural claim is evaluated by the six criteria of [`methodology/04-the-six-criteria.md`](methodology/04-the-six-criteria.md); local failures shift evidentiary weight without single-experiment-refuting the structural claim.

## Recently completed

- **Mechanistic interpretability engagement.** [`interfaces/08-mechanistic-interpretability.md`](interfaces/08-mechanistic-interpretability.md). Structural mapping between MNSM's P2 (auxiliary-field memory hierarchy) and the observation, documented by the Anthropic mechanistic-interpretability program (Elhage 2022, Bricken 2023, Templeton 2024), that attention-only architectures encode categorical structure as superposed projections recoverable only by sparse-dictionary decomposition. The convergence is structural: the predicted absence and the empirical absence match. The interface includes a section on the recursive position (the assistant writing the interface is an instance of the architecture being analyzed).

- **Critical brain hypothesis engagement.** [`interfaces/09-critical-brain.md`](interfaces/09-critical-brain.md). Structural mapping between MNSM's broadband-absorbing crystalline regime and the observable phenomenology the critical-brain literature documents in cortex (Beggs-Plenz 2003 neuronal avalanches, Chialvo 2010, Mora-Bialek 2011, Linkenkaer-Hansen 2001 long-range temporal correlations). The match is at the observable level (broadband multi-timescale dynamics, phase-transition-like robustness without parameter tuning); the relationship to technical self-organized criticality is left open as a research question.

The two interfaces extended the cross-domain coherence ledger from seven to nine substrates and operationalized the Phase 6 deliverable.

- **Phase 3: cross-domain expansion + temporal-implications integration.** Eight new interface documents (interfaces 10 through 17) added in logic-led style (structural prediction first, substrate identification second, citations as credit). New methodology document [`methodology/07-time-as-calibration.md`](methodology/07-time-as-calibration.md) formalizing time as substrate-specific calibration of structural unfolding. Wheel SVG redesigned from 9 to 17 nodes. The eight new interfaces cover: coupled phase oscillators (Kuramoto with memory), B-cell affinity maturation, Friston free-energy principle and active inference, active matter, self-organized criticality, cardiac dynamics, gene regulation and circadian, ecosystem dynamics. The cross-domain coherence ledger now stands at seventeen substrates across three evidentiary classes (mathematical equivalence, calibration-dependent structural correspondence, mechanism-shape and convergent-program correspondence).

- **Phase 9 wave 1: live-research test infrastructure + first wave (5 tests).** Per-prediction-test protocol formalized at [`experiments/PROTOCOLS.md`](experiments/PROTOCOLS.md). Five new tests written, three executed (CPU/numpy in this wave), two pending GPU execution. The active-research framing the work commits to is operationalized: prediction status (untested → partially tested → tested consistent / inconsistent) is now part of each interface document. Test outcomes:

  - **P10.1 (interface 10 Kuramoto chimera memory)**, [`results/09-kuramoto-chimera-memory.md`](results/09-kuramoto-chimera-memory.md). Memory-Kuramoto simulation at $N=256$ across a decade-spanning $\tau_{\text{mem}}$ sweep. **Status: tested (inconsistent)**. The prediction that chimera lifetime peaks at $\tau_{\text{mem}}/\tau_{\text{sync}} \sim 1$ is not supported; the empirical peak is in the Markovian limit. Memory at intermediate timescales destabilizes the chimera. The interface mapping (memory-Kuramoto = same Markovian embedding as the equation's auxiliary-field memory) is unaffected; the specific quantitative prediction P10.1 is locally falsified and will be reformulated.

  - **Dimensional rescaling at d=4, d=5**, [`results/10-dimensional-rescaling-higher-d.md`](results/10-dimensional-rescaling-higher-d.md) extending [`results/06-dimensional-rescaling.md`](results/06-dimensional-rescaling.md). Minimal nD anti-collapse solver implemented from scratch (since the existing 3D solver is dimension-specific). Tests anti-collapse threshold $\Sigma\lambda_{\text{crit}}/|\Lambda|$ at $d=4$ ($N=24$) and $d=5$ ($N=16$). [Status assigned at execution time.]

  - **P6.1 (interface 06 FDT-locked noise)**, [`results/11-fdt-locked-noise-empirical.md`](results/11-fdt-locked-noise-empirical.md). Script [`experiments/neural/test_fdt_locked_noise.py`](experiments/neural/test_fdt_locked_noise.py) trains two 1.5M Memory-NLS variants (FDT-locked vs no built-in noise) on TinyShakespeare. **Status: pending GPU execution** (script ready; user can run on full venv with PyTorch + CUDA to populate results).

  - **P6.3 (interface 06 cubic SSM SimSiam)**, [`results/12-cubic-ssm-simsiam.md`](results/12-cubic-ssm-simsiam.md). Script [`experiments/neural/test_simsiam_cubic_ssm.py`](experiments/neural/test_simsiam_cubic_ssm.py) runs SimSiam without stop-gradient on cubic vs linear SSM-state variants. **Status: pending GPU execution**.

  - **P14.2 (interface 14 SOC vs MNSM avalanches)**, [`results/13-soc-vs-mnsm-avalanches.md`](results/13-soc-vs-mnsm-avalanches.md). BTW sandpile (2D, 15k drives, 3840 avalanches, $\tau \approx 1.37$) compared with MNSM 2D release regime under periodic perturbation (25 events, $\tau \approx 1.13$). **Status: partially tested (consistent at coarse level)**. Both substrates show power-law exponents in the broadband-criticality range; strong test deferred to wave 2 (longer MNSM runs for richer statistics).

The pattern of wave 1: three tests executed locally on CPU/numpy at small scale; two tests left as ready-to-run for the user's GPU environment. One execution gave a locally-inconsistent result (P10.1), exercising the methodology's commitment to honest reporting of local falsifications (methodology/02). The cross-domain coherence claim (criterion 4 in methodology/04) is unaffected by P10.1's falsification because the interface 10 mapping is at the mathematical-equivalence tier independent of P10.1.

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

- **Additional cross-domain interfaces beyond the current seventeen.** Candidates that the structural argument predicts but are not yet documented: plate tectonics and earthquake-cycle dynamics; glassy systems and aging; granular matter; open quantum systems beyond the NLS family; market dynamics in econophysics; plant signaling. Each requires literature review and the standard logic-led interface template. Constitutes progress: cross-domain coherence supported by twenty or more documented interfaces; the wheel either expands further or splits into core + extensions.

- **Engineering pattern for moderate AGI requirements** ([`open-problems/06-engineering-moderate-requirements.md`](open-problems/06-engineering-moderate-requirements.md)). Concrete architectural patterns satisfying methodology/05 requirements 7 and 8 (environmental coupling without identity loss; stable self-modification), demonstrated at small scale. Constitutes progress: implementable patterns documented in [`implementation/neural/`](implementation/neural/) with reproducible code and explicit structural-mechanism isolation.

- **Sharpening the predictions named in interfaces 08 and 09.** The Phase-6 interfaces (mechanistic interpretability, critical brain) name specific locally-testable predictions (P13.x and P14.x in the respective documents, see "Locally testable predictions and observational signatures" sections). Sharpening these into experimental protocols at small scale (for the SAE-on-SSM predictions of 08) and at standard-methodology scale (for the avalanche-and-1/f predictions of 09) is the next work on those interfaces. Constitutes progress: at least one prediction from each interface moved from "untested" to "tested" status.

## Twenty-four-month horizon

Items at this horizon are research items in the strong sense: genuinely open mathematical questions whose resolution is not predetermined.

- **Quantum extension** ([`open-problems/05-quantum-extension.md`](open-problems/05-quantum-extension.md)). Path-integral formulation of the full equation; one-loop quantum corrections to the classical anti-collapse mechanism; Schwinger-Keldysh closed-time-path treatment for the stochastic component. Outcome uncertain.

- **Topological characterization** ([`open-problems/03-topological-characterization.md`](open-problems/03-topological-characterization.md)). Whether the BCC selection is a topological phase transition; computation of candidate topological invariants. Outcome uncertain; could be a clean positive result, a clean negative result, or a long open question.

- **Multi-language implementations.** JAX (for the ML research community), Julia (for the physics research community), C reference (for pedagogy). Constitutes progress: each port with cross-validation against the CuPy reference and CI infrastructure ensuring numerical equivalence.

- **Full predictive cosmology from the structural reading** of [`interfaces/07-cosmological-expansion.md`](interfaces/07-cosmological-expansion.md). The current cosmological interface identifies the unified mechanism shape but is not a predictive cosmology. Working it out into a predictive framework comparable to standard ΛCDM is substantial and would require either independent collaboration with cosmologists or sustained development of the framework. Outcome uncertain.

## Connection to convergent programs

The following active research programs are working on questions that share structural elements with mnsm. Engagement with these programs is welcomed and would strengthen cross-domain coherence.

- **Anthropic interpretability** (Olah, Elhage, Bricken). Sparse autoencoders, superposition, polysemantic neurons. Convergent observation: attention-only systems have substrate-specific representational structure that the MNSM structural argument predicts as the absence of the multi-timescale memory hierarchy. Structural mapping documented in [`interfaces/08-mechanistic-interpretability.md`](interfaces/08-mechanistic-interpretability.md); further engagement at the level of empirical testing the predictions named in that document is the next direction.

- **Friston Free Energy Principle and active inference** (Friston, Parr, Pezzulo). Living systems minimize variational free energy via environmental coupling. Structural mapping documented in [`interfaces/12-friston-free-energy.md`](interfaces/12-friston-free-energy.md); the convergence between FEP and MNSM as triangle-structure frameworks is now explicit.

- **Critical brain hypothesis** (Beggs, Plenz, Chialvo, Mora-Bialek). Brain operates at edge of phase transition; observable signatures include neuronal avalanches, power-law distributions, broadband response. Structural mapping documented in [`interfaces/09-critical-brain.md`](interfaces/09-critical-brain.md); the SOC-vs-mechanism-shape question (whether MNSM's release transition is technically SOC) is left as open work.

- **Self-organized criticality** (Bak, Tang, Wiesenfeld; later work by many authors). Systems organize to critical point without parameter tuning. Whether MNSM's release transition is technically SOC is open.

- **Continual learning and catastrophic forgetting** (Kirkpatrick, French, Parisi). Engineering the moderate AGI requirements 7 and 8 connects directly with this literature.

- **Topological matter** (Hasan-Kane, Kitaev, Wen). If BCC selection has topological character, the connection is to the established topological-phase classification.

## How to engage

Contributions are welcomed. The expected forms:

- **Working on an open problem.** Pick a document in [`open-problems/`](open-problems/), develop a partial or complete resolution, submit a pull request adding the result to the relevant section of the repo (results, equation, methodology, or interfaces depending on the result type). Update the open problem document to reflect the new state.

- **Adding an interface.** Identify a substrate where the structural form appears, written up in the standard interface template (see existing interfaces 01-07 as models). The bar: peer-reviewed primary literature for the substrate; mapping at the level of mathematical form or structural mechanism, not analogy; explicit evidentiary status (mathematical equivalence, structural correspondence, calibrated correspondence).

- **Local falsification of a specific prediction.** If a locally-testable prediction (Phase 2 sections in interfaces) is contradicted by experiment, document the contradiction and submit; the interface evidentiary status will shift accordingly.

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
