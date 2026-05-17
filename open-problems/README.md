# Open problems

This folder catalogues problems that the work documents as currently open: questions where the structural argument either does not yet produce a result, produces a result that is not yet derived analytically, or implies a result whose engineering translation is not yet worked out. The folder exists to make the program visibly active rather than finished: questions remain, contributions are invited, and progress can be tracked.

The folder operates within the methodological frame in [`../methodology/`](../methodology/), specifically:

- The structural-realist evaluation in [`../methodology/02-limits-of-falsification.md`](../methodology/02-limits-of-falsification.md) and the six criteria of [`../methodology/04-the-six-criteria.md`](../methodology/04-the-six-criteria.md): the structural claim is evaluated by the six criteria, and is not subject to single-experiment refutation. Specific quantitative predictions are evaluated by numerical reproduction at the parameter values the experiment uses, contributing evidence under criterion 2 (reproducibility) and criterion 4 (cross-domain coherence).
- Open problems below are stated as work, not as criticisms. Their resolution would extend the work; their non-resolution does not falsify it. Where a non-resolution would shift the work's evidentiary position, that is stated explicitly.

## Uniform template

Each open problem document follows the same structure:

1. **Precise statement.** What exactly is the problem? Stated formally where possible (equation, conjecture, predicted behavior).
2. **What is known.** The existing results in repo that bear on the problem, with file references.
3. **What is missing.** The specific gap between current state and resolution.
4. **What would constitute progress.** Observable criteria: a derivation, a numerical confirmation, a counter-example, a reformulation, a rigorous bound. Multiple modes of progress acknowledged.
5. **Suggested approaches.** Methodological avenues, citing existing literature where applicable.
6. **Connections to existing repo content.** Cross-references to principles, equation, results, interfaces, methodology.

The uniform template enables comparison across problems and contribution by readers who can address one piece without needing the full context of the others.

## Catalogue

| File | Problem |
|---|---|
| [`01-analytical-anti-collapse.md`](01-analytical-anti-collapse.md) | Derive the overshoot condition for the anti-collapse mechanism analytically (currently demonstrated numerically only). |
| [`02-phase-diagram.md`](02-phase-diagram.md) | Map the full $(\Lambda, \Sigma\lambda, \nu_j, \sigma)$ parameter space and identify all dynamical regimes. |
| [`03-topological-characterization.md`](03-topological-characterization.md) | Is the BCC selection a topological phase transition? Identify candidate topological invariants. |
| [`04-continuum-rg.md`](04-continuum-rg.md) | Renormalization-group flow of the equation; identify relevant, marginal, irrelevant operators; look for fixed points. |
| [`05-quantum-extension.md`](05-quantum-extension.md) | Path-integral formulation; quantum corrections to the classical anti-collapse mechanism. |
| [`06-engineering-moderate-requirements.md`](06-engineering-moderate-requirements.md) | Work out methodology/05 requirements 7 and 8 (environmental coupling without identity loss; stable self-modification) at engineering level. |
| [`07-additional-substrates.md`](07-additional-substrates.md) | Candidate cross-domain instantiations not yet documented: Friston Free Energy Principle, Kuramoto synchronization, immune affinity maturation, active matter, self-organized criticality. |
| [`08-calibration-philosophy.md`](08-calibration-philosophy.md) | Decision procedure for when dimensional calibration choices matter and how they constrain across interfaces. |

## How to contribute

Contributions on any of these problems are welcomed. The expected form is either a pull request adding to one of the documents (clarifying the problem, narrowing its scope, identifying new known results, proposing approaches), a pull request producing a result (analytical derivation, numerical evidence, counter-example) accompanied by reproducible code where applicable, or a GitHub Discussions thread engaging with the problem at the conceptual level.

Contributors should be aware of the operational constraints in [`../CLAUDE.md`](../CLAUDE.md) (these apply to human contributors as much as to AI-assisted contributions) and the methodological frame in [`../methodology/`](../methodology/) (specifically the no-Popperian-falsification-of-global-claim, no-competitive-benchmark-framing, no-gatekeeping-as-validation-path commitments).

## Relationship to the rest of the repo

Open problems are not failures of the work. They are the work's current frontier. Each problem is stated in a way that names what would constitute progress; readers who care about the program can use the catalogue to identify where they can contribute and what would constitute a meaningful result. The folder is the operational form of "active research program" rather than "finished body of work."

When an open problem is resolved (positively or negatively), the corresponding document moves from "open" to "closed" status (a note added to the top); the document remains in the folder as the historical record of the question and its resolution. Closed problems are not deleted; they are part of the program's record.
