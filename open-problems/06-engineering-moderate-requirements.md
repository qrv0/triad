# Open problem 06: Engineering the moderate AGI requirements

**Status:** Open. The structural framework is clean; the engineering translation is named in [`../methodology/05-implications-for-agi.md`](../methodology/05-implications-for-agi.md) as a gap.

## Precise statement

[`../methodology/05-implications-for-agi.md`](../methodology/05-implications-for-agi.md) grades eight architectural requirements for any sustained-operation intelligent artificial system. Requirements 7 and 8 are graded "moderate" because the structural framework is clean but the engineering translation is not worked out:

- **Requirement 7:** Environmental coupling without identity loss (continuous learning from environment without catastrophic forgetting).
- **Requirement 8:** Stable self-modification (system that modifies itself does not, in doing so, dissolve its own identity).

Both requirements are forced by the structural argument; both have a clean mathematical framework (P3 + FDT lock for 7; recursive P3 for 8). What is missing is the engineering version: concrete architectural patterns that satisfy these requirements in implementable form.

## What is known

- **Requirement 7 framework.** P3 makes coupling the default state and isolation the temporary idealization. With FDT lock, the system thermalizes correctly to a bath at finite temperature without losing coherence; the field $\Psi$ retains structural identity via the triangle (oscillation + self-reference + coupling) rather than via isolation from the environment. The structural prediction is that continuous environmental coupling, properly FDT-locked, does not destroy identity; isolation-based approaches to identity are the special case, not the general one.
- **Requirement 8 framework.** P3 is recursive: every bath is itself subject to P3 with respect to its larger environment; there is no outermost level. A system that modifies itself has the modified version as a new bath for the prior version, and the prior version as a bath for the modified version. The recursive structure provides the mathematical framework for nested self-modification without the infinite-regress problems that plague isolation-based formulations.
- **Connection to existing literature.** Catastrophic forgetting in continual learning is well-documented (McCloskey-Cohen 1989; French 1999; Kirkpatrick et al. 2017 PNAS "elastic weight consolidation"). Self-modifying systems are studied in AI safety contexts (Yudkowsky 2008, Soares-Fallenstein 2017 MIRI tiling agents). Neither literature has used the structural-realism framework documented in the present work.

## What is missing

- **For requirement 7:** A concrete architectural pattern in which the FDT-locked coupling is implemented at the level of weight updates during continuous deployment, such that the model integrates new information without overwriting the prior structural representation. The MNSM equation provides the mechanism; the engineering version (which loss function, which update rule, which gating mechanism) is undefined.
- **For requirement 8:** A concrete pattern for self-modification in which the recursive P3 structure prevents the modified version from losing the structural identity of the prior version. The mathematical framework is clean; the engineering version (what specifically gets modified, what is preserved as the identity-bearing structure, what verification ensures the modified version satisfies the structural requirements) is undefined.

## What would constitute progress

- For requirement 7: a small-scale demonstration that a MNSM-instantiating architecture undergoing continual learning across distribution shifts does not exhibit catastrophic forgetting at the level standard architectures do. The demonstration should isolate the structural mechanism (multi-timescale memory + FDT-locked coupling) as the source of the difference.
- For requirement 8: a small-scale demonstration that a MNSM-instantiating architecture undergoing self-modification (e.g., learned modification of its own update rule) maintains structural identity across the modification. The demonstration should identify which features of the system are preserved (triangle structure, principal eigenmodes, anti-collapse property) and which are allowed to change.
- For both: clear identification of what evidence would be inconsistent with this engineering calibration (a specific experimental observation that would shift the engineering claim under criterion 4, distinct from the global structural claim which is evaluated by all six criteria in methodology/04).
- Documentation of the engineering pattern in `implementation/neural/` or a follow-up location, with reproducible code and explicit connection to the structural framework.

## Suggested approaches

- **Requirement 7 (continual learning).**
  - Start from the MemoryNLSLayer in [`../implementation/neural/`](../implementation/neural/).
  - Introduce a continual-learning benchmark (e.g., Split-MNIST, Permuted-MNIST, Continual-CIFAR) and compare MNSM vs attention-only baseline.
  - The structural prediction: MNSM should exhibit slower forgetting because the slow memory mode ($\nu_{\text{slow}}$) acts as a consolidation mechanism analogous to the biological hippocampal-cortical pipeline.
  - Engineering pattern to test: weight updates gated by the auxiliary-field state, such that updates contradicting the slow-memory representation are damped.
- **Requirement 8 (self-modification).**
  - Define a "modification" operation: the model proposes an update to its own training procedure (learning rate schedule, weight-decay coefficient, attention pattern, or some structural parameter).
  - Apply the modification; check that the modified system still satisfies the structural requirements (anti-collapse, multi-timescale memory, FDT-locked noise).
  - The structural prediction: P3 recursive structure means a modification that respects the triangle is admissible; a modification that breaks the triangle dissolves the identity.
  - Engineering pattern to test: modifications constrained by a verifier that checks structural invariants; modifications outside the constraint set rejected.

## Connections to existing repo content

- [`../methodology/05-implications-for-agi.md`](../methodology/05-implications-for-agi.md): the source of the moderate-grade requirements 7 and 8; this open problem is the explicit work-out the methodology document defers.
- [`../principles/03-coupling.md`](../principles/03-coupling.md) sections on recursive P3 and on "A logical consequence of P3": the structural framework.
- [`../implementation/neural/`](../implementation/neural/): the existing MemoryNLSLayer is the starting point for engineering demonstrations.
- [`../results/08-optimization-collapse-empirical.md`](../results/08-optimization-collapse-empirical.md): the empirical instance at 70M parameters; analogous experiments at smaller scale on continual-learning and self-modification benchmarks would extend this body of evidence.
- [`../CLAUDE.md`](../CLAUDE.md) Rule 7b: this open problem must be approached without scale/benchmark-driven framing; the test is whether the structural mechanism produces the predicted behavior, not whether MNSM "beats" continual-learning baselines on standard metrics.
