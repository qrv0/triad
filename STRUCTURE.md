# Why this repository is shaped the way it is

This document is the repository explaining its own organization. It exists because the work it hosts is methodologically self-referential, an equation derived from the principle that *coupling is the default and isolation is temporary*, and a repository that organized that work into the standard machine-learning template would contradict the work it hosts.

## The constraint

The standard machine-learning repository has approximately the following shape: a top-level `README.md` and `LICENSE`, a `src/` folder, an `experiments/` folder, a `notebooks/` folder, and a `tests/` folder. This shape encodes a specific implicit ontology, code is primary, experiments validate the code, notebooks demonstrate the code, tests verify the code, and everything else is metadata. The shape works for software whose purpose is to be a tool. It works less well for software whose purpose is to *register a structural claim about persistent extended entities*.

This repository hosts work of the second kind. The code is real and runs; reproducibility is taken seriously. But the claim of the work is not "this code does X efficiently." The claim is that an equation derived from three minimal structural axioms generates a small family of phenomena, that the same equation appears in mathematically equivalent form in several other physical and computational domains, and that this cross-domain co-occurrence is itself the criterion by which the work should be evaluated. A standard repository template buries that claim under file-tree conventions designed for code-as-tool projects.

The shape of this repository is, therefore, a structural argument in its own right. The choices made below are deliberate.

## The twelve first-order folders

There are twelve folders at the top level: `principles/`, `equation/`, `results/`, `interfaces/`, `methodology/`, `paths/`, `playground/`, `implementation/`, `experiments/`, `paper/`, `tests/`, `open-problems/`. The repository root also contains `RESEARCH-AGENDA.md`, which sits beside `README.md`, `CLAUDE.md`, `STRUCTURE.md`, and `CONTRIBUTING.md`.

The ML implementation depth that previously lived under `implementation/neural/` and `experiments/neural/` was migrated on 2026-05-17 to the [`mnsm-ml`](https://github.com/qrv0/mnsm-ml) spinoff repository, along with the two ML-substrate interfaces (`06-state-space-models.md` and `08-mechanistic-interpretability.md`) and the optimization-collapse empirical result. The two repositories advance in parallel; this one holds the structural argument and the non-ML substrates.

`principles/` comes first because the work begins in axioms, not in code. Putting the three structural principles into a top-level folder, rather than burying them in the introduction of a README, is a declaration that this work is foundational rather than incremental. Anyone who reads the file tree before reading any prose sees that the entry point is mathematical principles.

`equation/` follows because the equation is what the principles select. The derivation, the Markovian embedding, the two-dimensional and three-dimensional forms, and the reductions to known equations are all in this folder. The equation is the load-bearing object of the work.

`results/` collects the numerical findings: anti-collapse, spontaneous crystallization, Bravais selection, the dimensional rescaling discovered in the three-dimensional case, the temporal–spatial asymmetry of the memory kernel. These are presented as separate documents because each is structurally distinct and each can be reproduced from the corresponding script in `experiments/physics/`.

`interfaces/` is the cross-domain section as a folder rather than a paper appendix. Each mapping has its own document, its own citations, and its own scope of claim. The twenty interfaces in this repository span: NLS instances (BEC, optical solitons, deep-water waves); baryon acoustic oscillations; Chladni cymatic patterns; gamma-frequency neural entrainment; archaeoacoustic resonance in megalithic chambers; cosmological expansion as anti-collapse release; the critical-brain literature; coupled phase oscillators (Kuramoto with memory); B-cell affinity maturation in adaptive immunity; the variational dynamics of the Friston free-energy principle and active inference; active matter (flocks, swarms, active gels); self-organized criticality; cardiac dynamics; gene-regulation and circadian rhythms; multi-species ecosystem dynamics; non-Markovian open quantum systems via pseudomode embedding; generalized Maxwell viscoelasticity; warm-inflation cosmology; Hawkes self-exciting processes; earthquake-cycle dynamics. Two further interfaces (structured state space models in machine learning; mechanistic-interpretability of attention-based systems) live in the [`mnsm-ml`](https://github.com/qrv0/mnsm-ml) spinoff repository alongside the ML implementation depth. The decision to elevate cross-domain mappings to first-class content rather than supplementary material is the most consequential structural choice in this repository. The interfaces divide into three evidentiary classes (mathematical equivalence, calibration-dependent structural correspondence, mechanism-shape and convergent-program correspondence) catalogued in [`interfaces/README.md`](interfaces/README.md).

`methodology/` holds the philosophical position. Structural realism, the limits of strict falsificationism, the six criteria by which structural theories are evaluated. Putting methodology in its own first-order folder, rather than letting it remain implicit, signals that the methodological frame is part of the work and not commentary on it.

`paths/` is the accessibility layer. Five entry routes for readers from five different backgrounds (new, physics, machine learning, neuroscience, philosophy). Each path threads through the same content in an order appropriate to a specific starting point. A reader who arrives without prior context has somewhere to begin; a specialist has a faster route. The same body of work supports both without dilution.

`playground/` contains three interactive notebooks, ordered by depth of engagement: just watch (passive), adjust the knobs (parameter exploration), build your own (guided implementation). The notebooks run in Google Colab without local setup. This folder exists because the work has visual and experiential content that a static document cannot convey, and because the alternative, making interested readers install CUDA, configure environments, and read code before seeing anything, filters out exactly the kind of newcomer who might engage most usefully.

`implementation/` holds the CuPy field-equation solver in `physics/`. The PyTorch sequence-layer implementation that was previously co-resident under `implementation/neural/` was migrated to the [`mnsm-ml`](https://github.com/qrv0/mnsm-ml) spinoff repository alongside the ML-substrate interfaces. The two implementations are mathematically equivalent at the level of auxiliary-field dynamics; the equivalence is the structural content the SSM correspondence (in the spinoff's `interfaces/01-state-space-models.md`) documents.

`experiments/` contains the scripts that reproduce the figures and tables in the paper. The decision to keep these scripts separate from the implementation library is standard practice and needs no special justification.

`paper/` contains the full manuscript. The decision to keep it as a single file rather than splitting into chapters is to preserve its readability as a paper rather than a wiki.

`tests/` contains the sanity tests that validate the solver. The decision to include conservation tests, FDT thermalization tests, and anti-collapse signature tests is standard practice for numerical work where reproducibility is asserted.

`open-problems/` catalogues the work's open research questions in uniform template (precise statement, what is known, what is missing, what would constitute progress, suggested approaches, repo connections). The folder makes the program visibly active rather than finished. Eight problems currently catalogued: analytical anti-collapse, full phase diagram, topological characterization, continuum RG, quantum extension, engineering moderate AGI requirements, additional cross-domain substrates, calibration philosophy. New problems are added as they are recognized; resolved problems are kept (marked closed) as the historical record.

`RESEARCH-AGENDA.md` at the repository root organizes the open problems by horizon (6 / 12 / 24 months) and identifies convergent research programs (Anthropic interpretability, Friston Free Energy Principle, critical brain hypothesis, self-organized criticality literature) where engagement would strengthen the cross-domain coherence claim.

## What the structure encodes about the work

Reading the folder tree top to bottom, a visitor encounters the structure in this order: axioms, equation, results, cross-domain interfaces, methodology, accessibility, interaction, code, reproduction, paper, validation. This ordering is not alphabetical and not the default of any package manager. It is the order in which the work was constructed and the order in which it is best read.

The axioms come first because everything else depends on them. The cross-domain interfaces come before the methodology because the methodology is a response to the question "how should this be evaluated?", a question that only becomes pressing once the cross-domain mappings are visible. The paths and the playground come before the implementation because the work is meant to be approachable and not solely a code object. The paper comes after the parts of the repository that prepare a reader to read it, not before.

## What this repository is not

This repository is not a Python package distribution. It can be installed and run, but the artefact is not "a library that lets you do X." It can be cited, but the artefact is not "a paper with code." It can be read sequentially, but the artefact is not "a book."

This repository is a body of work registered as structure. The folders, the documents, the code, the notebooks, the paper are all expressions of the same underlying claim, refracted into the registers in which different readers can encounter it. The hope is that the structural claim survives the diffusion across registers, that someone who only reads the README, someone who only runs the playground notebooks, someone who only reads the paper, and someone who reads everything, all come away with the same essential pattern in different degrees of resolution.

## A note on self-reference

If you have read this file, you have just been subject to the second of the three principles that organize the work it documents. The work asserts that persistent extended entities are defined by self-reference, both instantaneously and across time, and that this is part of why they hold their shape. This document is the repository being self-referential about its own shape. The document is also, in a smaller way, an instance of the structure the work describes. That is not a coincidence. It is the work.
