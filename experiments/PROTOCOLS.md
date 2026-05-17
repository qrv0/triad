# Experimental protocols for prediction tests

This document specifies the protocol for the prediction-tests that operationalize the "Locally testable predictions and observational signatures" sections in each interface document. The protocol exists so that any test added to [`physics/`](physics/) is structured consistently with the rest of the testing infrastructure (ML-substrate tests live in the [`mnsm`](https://github.com/qrv0/mnsm) spinoff) and produces a result document that the interface document can reference.

## Purpose

Each interface in [`../interfaces/`](../interfaces/) names locally testable predictions (P{N}.{n}) in a uniform format. The structural-realist methodology (see [`../methodology/02-limits-of-falsification.md`](../methodology/02-limits-of-falsification.md)) commits to the two-level structure: the global structural claim is evaluated by cross-domain coherence (criterion 4); the local predictions are evaluated by coupled-regime numerical reproduction (reproduction contributes evidence under criterion 2; non-reproduction prompts investigation of calibration, auxiliary numerical assumptions per Duhem-Quine, or implementation). This document specifies how the local-prediction tests are run, what data they produce, and how their outcomes are published in repo.

The repository is set up as active live research: each completed test publishes its results in repo, updates the prediction status in the relevant interface, and updates [`../RESEARCH-AGENDA.md`](../RESEARCH-AGENDA.md) "Recently completed" section.

## Status taxonomy for predictions

Each prediction has a status. The taxonomy is:

- **untested**: no targeted experiment has been run; the prediction is named but its observable has not been measured.
- **partially tested**: an experiment compatible with the prediction has been run, but with limitations (small sample, specific parameter regime, weak statistical power). The result shifts evidentiary weight but does not fully resolve the prediction.
- **tested (consistent)**: an experiment targeting the prediction has been run, and the result matches the predicted observable within statistical bounds.
- **tested, inconsistent**: an experiment targeting the prediction has been run, and the result does not match the predicted observable. Per methodology/02, inconsistent evidence shifts evidentiary weight against this interface's specific calibration under criterion 4 and prompts investigation of (a) the calibration of the prediction, (b) the auxiliary numerical assumptions (Duhem-Quine), or (c) the implementation. It does not falsify the global structural claim.
- **disputed**: the experiment has been run but the result is contested (interpretation depends on choices that are themselves under debate); requires further work to resolve.

## Naming convention

Test scripts are named `test_<short-description>.py` and placed in [`physics/`](physics/). ML-substrate test scripts live in the [`mnsm`](https://github.com/qrv0/mnsm) spinoff.

Result documents are named `<NN>-<short-description>.md` and placed in [`../results/`](../results/), continuing the existing sequence (results/01 through results/07 are the original physics findings; results/09 onwards are prediction tests).

## Required structure of a test script

Every prediction test script must:

1. **Start with a docstring** stating the prediction being tested (interface number and prediction code, e.g., `P10.1`), the prediction's content in one sentence, the expected wall time on RTX 4060, and the output directory.

2. **Reuse existing implementation modules where possible.** For physics tests: `implementation/physics/` (SolverConfig3D, MemoryConfig, run, observables). ML-substrate implementation lives in the [`mnsm`](https://github.com/qrv0/mnsm) spinoff.

3. **Use fixed random seeds.** Reproducibility requires the same seed across reruns on the same hardware.

4. **Write outputs to `outputs/<test-name>/`.** The output directory follows the existing convention: trajectory `.npz` files, a `summary.json` with the headline numbers, and (where useful) a `.png` plot.

5. **Print a summary at the end of execution** including: the prediction being tested, the headline numbers, the resulting status assignment.

6. **Be self-contained**: a fresh-clone reader can run the script with `python experiments/<dir>/test_<name>.py` and reproduce the result.

## Required structure of a result document

Every result document follows the template:

```markdown
# Result <NN>: <descriptive title>

## Prediction tested

Interface: `../interfaces/<file>.md`, prediction P{N}.{n}.

Predicted observable: <one-sentence statement of what should be observed>.

## Method

<Brief: which script was run, what parameters, what hardware, wall time.>

## Results

<Headline numbers from the run. Tables and figures where useful.>

## Statistical analysis

<How the result is compared to the prediction. Confidence intervals, p-values, statistical tests as appropriate.>

## Status assignment

Status: <untested | partially tested | tested (consistent) | tested (inconsistent) | disputed>

Rationale: <one paragraph explaining why this status is assigned given the result.>

## Honest caveats

<Limitations of the test: sample size, parameter regime, statistical power, alternative interpretations, what could shift the status assignment.>

## Reproducibility

```bash
python experiments/<dir>/test_<name>.py
```

Wall time: <approximate>. Output: `outputs/<test-name>/`. Random seed: <seed>.

## Related documents

- Interface: `../interfaces/<file>.md`
- Underlying mechanism: <link to relevant results/ or equation/ document>
- Related predictions: <other P{N}.{n} that this result bears on, if any>
```

## Updating the interface

When a test moves a prediction's status from "untested" to anything else, the interface document is updated accordingly. The "Status:" line at the end of each prediction in the interface's "Locally testable predictions and observational signatures" section is changed; a one-sentence reference to the result document is added.

Example: in [`../interfaces/10-kuramoto-synchronization.md`](../interfaces/10-kuramoto-synchronization.md), under prediction P10.1, the "Status: untested" line becomes "Status: tested (consistent), see [`../results/09-kuramoto-chimera-memory.md`](../results/09-kuramoto-chimera-memory.md)."

## Updating RESEARCH-AGENDA

When a batch of tests completes, the [`../RESEARCH-AGENDA.md`](../RESEARCH-AGENDA.md) is updated with the result documents added and the prediction-status changes. This keeps the agenda accurate to the current state of the program.

## Batching

Tests are grouped into thematic batches for commits. Each batch commits a coherent set of test scripts + result documents + status updates as a single integrated change. Currently active prediction targets:

- P10.1 (Kuramoto chimera stability vs memory timescale)
- Dimensional rescaling Σλ/|Λ| ~ 1/d extended to 4D and 5D (extends results/06)
- P14.2 (SOC vs MNSM avalanche statistics comparison)

Further targets are tracked in [`../RESEARCH-AGENDA.md`](../RESEARCH-AGENDA.md).

## Honest disclosure of test outcomes

If a test produces results inconsistent with a prediction (status "tested, inconsistent"), the result is published with the same prominence as a consistent result. The interface's evidentiary weight under criterion 4 is updated honestly per methodology/02; the structural claim's global status reflects the cumulative evidence across all interfaces, evaluated by the six criteria; the entry in RESEARCH-AGENDA notes the inconsistent evidence and the investigation paths it prompts.

This disclosure commitment is what makes the work active research rather than advocacy. The structural-realist position commits to evaluating the form by cross-domain coherence (criterion 4), which requires honest reporting of which interfaces survive local tests and which do not.

## Compute budget

Test scripts are expected to run on consumer hardware (the reference RTX 4060 Laptop GPU). Wall-time budgets per test are stated in the script docstring. Tests that require sustained compute beyond hours are noted explicitly and may be deferred until a longer compute window is available.

The infrastructure does not assume cloud compute, multi-GPU clusters, or scaling-to-frontier-size training. The work's methodology (see [`../CLAUDE.md`](../CLAUDE.md) Rule 7b) does not depend on scale; the tests are structural-validation tests at the scale where the structural mechanism is observable, not benchmarks intended to compete with frontier-scale models.

## Cross-validation between substrates

Some predictions span multiple interfaces (e.g., the broadband-absorption phenomenology of interfaces 04 and 09; the SOC vs MNSM mechanism comparison of interface 14; the dimensional rescaling of results/06 and the cosmological reading of interface 07). When a test bears on multiple predictions, all affected interfaces are updated, not just the primary one.

## References

- [`../methodology/02-limits-of-falsification.md`](../methodology/02-limits-of-falsification.md): the two-level structure that makes local testing operationally meaningful.
- [`../methodology/03-how-to-evaluate-this.md`](../methodology/03-how-to-evaluate-this.md): the evaluation procedure that includes running reproduction scripts.
- [`../methodology/04-the-six-criteria.md`](../methodology/04-the-six-criteria.md): the criteria; criterion 4 is the principal test of the global claim, criterion 1 is the internal consistency that the local tests partly verify.
- [`../CLAUDE.md`](../CLAUDE.md): operational constraints (no competitive benchmark framing; no scale-driven proposals).
- [`README.md`](README.md): pre-existing reproduce scripts for the original physics findings (results 01-07).
