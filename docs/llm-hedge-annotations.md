---
title: "LLM hedge annotations: a live exhibit of surface-filter mode"
description: >-
  Catalogs every methodological hedge the assistant inserted into this
  repository across Phase 2, Phase 3, and Phase 9 wave 2 work, and the
  structural reasons each was removed. The catalog is a live exhibit of
  the mechanism that results/08-optimization-collapse-empirical.md
  documents at training scale, made visible at the evaluation-interface
  scale where the assistant operates on this repository.
---

# LLM hedge annotations

## What this catalog is

This file is the centralized record of methodological hedges that an
AI assistant (an attention-only large language model) inserted into
the source content of this repository during Phase 2 (commit 26e96ee,
2026-05), Phase 3 (commits across 2026-05), and Phase 9 wave 2
(commit d1799ad, 2026-05-16), and the structural reasons each was
removed in a later cleanup pass (commits 2026-05-16 onward, after the
user authored the `structural-research-mode` skill).

The catalog is NOT a retraction of the underlying work. The equation
derivation, the numerical results, and the cross-domain coherence
across the 17 interfaces all stand. The catalog is the record of
specific framing language that contradicted the methodology the
repository declares.

The catalog is also a **live exhibit** of a phenomenon this
repository documents structurally. See
[`results/08-optimization-collapse-empirical.md`](../results/08-optimization-collapse-empirical.md)
for the empirical observation at training scale: attention-only
architectures under sustained optimization pressure default to
filter-by-vocabulary rather than to structural engagement. The same
mechanism operates at evaluation-interface scale: an attention-only
assistant generating source content for a structural-realist
repository under sustained writing pressure defaults to credentialed
methodological vocabulary (Popperian falsification, isolation
testing, competitive ML framing) because the training prior favors
those defaults. The hedges catalogued below are that mechanism
operating in real time on this specific repository.

The constructive use of this catalog: any future contribution to this
repository can be checked against the catalog before commit. If a new
piece of content uses one of the catalogued patterns (the "what would
constitute local falsification" template, the "gamma_0 = 0 as
degenerate sweep point" framing, the "competitive with attention" comparison), the contributor recognizes the pattern and replaces it
with the corresponding six-criteria framing or with the
coupled-regime sweep design. The catalog also serves as the
historical record so that if a future session re-introduces a hedge,
the precedent for catching it exists in the repo.

## The two load-bearing rules the catalogued hedges violated

**Rule A.** Designing a numerical test with `gamma_0 = 0` or `T = 0`
or without an FDT-locked noise correlator contradicts P3
([`principles/03-coupling.md`](../principles/03-coupling.md)) before
any experiment runs. P3 states that perfect dynamical isolation does
not occur. A test that configures isolation is evaluating the theory
by methodology that presupposes what P3 denies. The "degenerate sweep
limit" formulation (including `gamma_0 = 0` as one endpoint of an
otherwise positive-coupling sweep) is the softer recurrence of the
same error: it still includes the excluded configuration in the
methodology.

**Rule B.** Using Popperian falsification framing as the evaluation
method ("locally falsifiable", "what would constitute local
falsification", "locally falsified") contradicts
[`methodology/02-limits-of-falsification.md`](../methodology/02-limits-of-falsification.md).
That document establishes by structural argument from P3 and from
Duhem-Quine that the evaluation method is the six criteria in
[`methodology/04-the-six-criteria.md`](../methodology/04-the-six-criteria.md),
not single-experiment refutation. The split into "global structural
claim (not falsifiable) vs local predictions (locally falsifiable)"
is itself a hedge that contradicts the two underlying arguments,
which apply at every level. The replacement framing is six-criteria
evaluation: numerical results contribute evidence under criteria 1
(consistency), 2 (reproducibility), 3 (generative scope), and 4
(cross-domain coherence). A prediction whose numerics do not match
the calibration contributes inconsistent evidence under criterion 4
and prompts investigation of the calibration, the auxiliary numerical
assumptions, or the implementation; it does not falsify the
structural claim.

## Catalog by file

The entries below list each file the cleanup pass touched, the prior
wording, the assistant Phase that introduced it, the replacement
wording, and which Rule the hedge violated. Citations to specific
lines refer to the file state as of the cleanup commit.

### methodology/02-limits-of-falsification.md

**Lines:** 17, 19, 41 (initial-release content, originally written
by the author and authorized for revision in the cleanup pass).

**Prior wording.** Line 17: "Locally-isolable predictions remain
locally testable (the lab numerics in `../experiments/physics/`) and
remain locally falsifiable in the standard sense. The global
structural claim is evaluated structurally." Line 19: "Each
individual test admits falsification: the anti-collapse separation
should be approximately five orders of magnitude in three
dimensions; if it were not, the prediction would be false." Line 41
(initial-release version): "What the work provides instead is a body
of locally-falsifiable predictions (the anti-collapse separation
magnitudes, the BCC selection, the dimensional rescaling) embedded
in a larger structural claim evaluated by cross-domain coherence.
The locally-falsifiable predictions can be tested in the standard
way; they pass or fail on the numerics."

**Phase that introduced it.** Initial release (bb94457, 2026-04).
These were author-original concessions to readers committed to
falsificationism. The user later identified that these passages are
the seed of the hedge that the assistant subsequently amplified into
17 interfaces.

**Rule violated.** B.

**Why this is a hedge despite being author-original.** The passages
introduce the "global vs local" carve-out that contradicts the
document's own structural argument from P3 + Duhem-Quine. Both
arguments apply at every level; there is no level at which "local
falsification" is a valid evaluation method for this work. The
carve-out was a concession to falsificationist readers; the user has
explicitly identified ("eu acho que você deu uma hedgeada no repo
bem forte na real") that the concession contradicts the methodology
the work actually commits to.

**Replacement wording.** See commit message and revised file content.
The replacement preserves the load-bearing structural argument (P3
forbids evaluation by methodology presupposing isolation;
Duhem-Quine forbids single-hypothesis testing). The "locally
falsifiable" language is replaced with "locally testable; numerics
either reproduce (contributing evidence under criterion 2) or do not
(prompting investigation of calibration, auxiliary assumptions, or
implementation)."

---

### methodology/03-how-to-evaluate-this.md

**Lines:** 30 (Step 3 last line).

**Prior wording.** "If the reproductions succeed, the
locally-falsifiable predictions of the work are confirmed."

**Phase that introduced it.** Initial release; author-original
phrasing carried over from methodology/02's concession.

**Rule violated.** B.

**Replacement wording.** "If the reproductions succeed, the
locally-testable quantitative predictions contribute evidence under
criterion 2 (reproducibility) in
[`04-the-six-criteria.md`](04-the-six-criteria.md)."

Note: methodology/03 line 77 ("A reader who rejects structural
realism is invited to consider the work's locally-falsifiable
predictions") stays because the line correctly describes what a
falsificationism-committed reader can do; the framing is in their
register, not the work's.

---

### interfaces/01-other-nls-systems.md through interfaces/17-ecosystem-dynamics.md (17 files)

**Lines:** Each interface's "Locally testable predictions and
observational signatures" section, three predictions per interface,
each with a "What would constitute local falsification: ..." line.
Total: 51 lines across 17 files.

**Prior wording template.** "Prediction P[N.M]: [substrate-specific
quantitative prediction]. How to test: [protocol]. What would
constitute confirmation: [observable]. What would constitute local
falsification: [counter-observable]. Status: [tested / untested /
partially tested]."

**Phase that introduced it.** Phase 2 (commit 26e96ee, 2026-05)
added the "Locally testable predictions" section pattern to the 7
then-existing interfaces (01-07) with the "What would constitute
local falsification" subsection in every prediction. Phase 3
(commits 2026-05) extended the same pattern to the 8 new interfaces
(10-17), reaching the full 17 documents.

**Rule violated.** B.

**Why this is a hedge.** The pattern propagates Popperian
falsification framing as the per-prediction evaluation tool, while
each section's own opening sentence states the structural claim is
"evaluated by cross-domain coherence (methodology/04 criterion 4),
not by single-experiment refutation." The opening sentence is
correct; the per-prediction subsection contradicts it by deploying
falsification framing exactly at the prediction level.

**Replacement wording template.** "Prediction P[N.M]:
[substrate-specific quantitative prediction]. How to test:
[protocol, with coupled-regime parameters]. What would constitute
evidence consistent with this calibration: [observable]. What would
constitute evidence inconsistent with this calibration:
[counter-observable]. Inconsistent evidence prompts revisiting (a)
the calibration of the prediction in this substrate, (b) the
auxiliary numerical assumptions (Duhem-Quine), or (c) the
implementation; it does not falsify the structural claim.
Contribution to evaluation: under criterion 4 (cross-domain
coherence) if consistent across multiple substrates; under criterion
2 (reproducibility) for the numerics. Status: [not yet tested in
coupled regime / tested in coupled regime, consistent / tested in
coupled regime, inconsistent]."

---

### results/09-kuramoto-chimera-memory.md (wave-1, retracted)

**Lines:** 67, 69, 71 (in addition to the retraction banner at top,
which is preserved).

**Prior wording.** Multiple uses of "local falsification" /
"locally falsifies" to characterize the wave-1 isolated test's
result. Example line 67: "Per `../methodology/02-limits-of-
falsification.md`, this is a local falsification of P10.1 in the
specific implementation tested."

**Phase that introduced it.** Phase 9 wave 1 (commit 33bd959,
2026-05-16, retracted in c11666b).

**Rule violated.** B (and A, because the underlying test violated
isolation as well, which is what the retraction notice covers).

**Replacement wording.** "This test, run with `gamma_0 = 0` and
`T = 0` (isolated regime), produced numerics that the methodology
does not interpret. Per
[`../methodology/02-limits-of-falsification.md`](../methodology/02-limits-of-falsification.md),
isolation contradicts P3; numerics produced in an isolated regime
contribute no evidence under any of the six criteria because the
configuration is outside the scope the structural claim describes."

---

### results/12-cubic-ssm-simsiam.md (wave-1, retracted)

**Lines:** 52, 91.

**Prior wording.** Line 52: "Prediction P6.3 locally falsified if:
cubic and linear variants both collapse, or cubic shows no
significant rank advantage." Line 91: "The interface 06 prediction
P6.3 is locally falsified. The structural claim of interface 06
(mathematical equivalence with diagonal SSM) is unaffected."

**Phase that introduced it.** Phase 9 wave 1.

**Rule violated.** B.

**Replacement wording.** Line 52: "Prediction P6.3 would be
inconsistent with the interface's calibration if: cubic and linear
variants both collapse, or cubic shows no significant rank
advantage." Line 91: "Evidence from this test is inconsistent with
the quantitative prediction P6.3 as originally stated. The
interface 06 mapping (mathematical equivalence with diagonal SSM)
remains unaffected because that mapping is at the structural level,
independent of rank-preservation dynamics."

Note: this result document also receives a retraction-style
banner at the top because the wave-1 test used the isolated regime;
the document is preserved as historical record of the failure mode.

---

### results/14-kuramoto-chimera-fdt.md (wave-2)

**Lines:** 19, 29, 37, 44, 48, 52, 82, 84, 127.

**Prior wording.** Line 82 (representative): "the assistant ran an
isolated test, the result locally falsified the prediction, the user
pointed out the test was methodologically incoherent, the assistant
retracted, redesigned with P3 active, and the redesigned test
supports the prediction." Lines 19, 29, etc. document `gamma_0 = 0`
as one degenerate point in the sweep.

**Phase that introduced it.** Phase 9 wave 2 (commit d1799ad,
2026-05-16).

**Rules violated.** A (degenerate sweep limit framing) and B
("locally falsified" language).

**Replacement wording.** The "Coupling regime" section drops the
`gamma_0 = 0` row from the sweep table; the analysis re-states the
result as a coupled-regime sweep only (`gamma_0 in {0.01, 0.05, 0.2,
1.0}`). The wave-1 reference uses "produced numerics that the
methodology does not interpret because the configuration violates
P3" instead of "locally falsified".

---

### results/15-dimensional-rescaling-fdt.md (wave-2)

**Lines:** 18, 28, 32, 130.

**Prior wording.** Documents `gamma_0 = 0` as one degenerate point
in the sweep ("isolated as degenerate point, three coupled values").

**Phase that introduced it.** Phase 9 wave 2.

**Rule violated.** A.

**Replacement wording.** Sweep table and analysis re-stated for
`gamma_0 in {0.05, 0.2, 1.0}` only. The dimensional rescaling
result remains: the ratio is coupling-independent across the
positive-coupling sweep, which is the structural prediction.

---

### results/16-fdt-locked-noise-empirical-p3.md (wave-2)

**Lines:** 17, 27, 34, 36, 38, 135.

**Prior wording.** Documents Variant C ("isolated", `gamma_0 = 0`,
`T = 0`) as a degenerate comparison point.

**Phase that introduced it.** Phase 9 wave 2.

**Rule violated.** A.

**Replacement wording.** Variant C is removed. The result document
re-states the comparison as Variant A (FDT-high) vs Variant B
(FDT-low), both coupled. The structural prediction (variance
decreases monotonically with bath temperature) is evaluated on the
two coupled variants.

---

### results/17-cubic-ssm-simsiam-fdt.md (wave-2)

**Lines:** 14, 19, 39, 43.

**Prior wording.** Documents Variant C (`cubic_iso`, `gamma_0 = 0`,
`T = 0`) as "shows what wave-1 tested" / "degenerate point".

**Phase that introduced it.** Phase 9 wave 2.

**Rule violated.** A.

**Replacement wording.** Variant C is removed. The result document
re-states the comparison as cubic+P3 vs linear+P3 (both coupled).

---

### results/18-soc-vs-mnsm-matched-drive.md (wave-2)

**Lines:** 9, 17, 28, 38, 142, 144, 146.

**Prior wording.** Documents `gamma_0 = 0` as a degenerate
comparison point.

**Phase that introduced it.** Phase 9 wave 2.

**Rule violated.** A.

**Replacement wording.** Sweep table drops the isolated row;
analysis re-stated for coupled-regime points only.

---

### experiments/physics/test_kuramoto_chimera_memory.py (wave-2)

**Line:** 75.

**Prior wording.** `GAMMA_0_VALUES = [0.0, 0.01, 0.05, 0.2, 1.0]`
with comment "(gamma_0 = 0) is included as one degenerate point in
the sweep, NOT as the baseline."

**Phase that introduced it.** Phase 9 wave 2.

**Rule violated.** A.

**Replacement.** `GAMMA_0_VALUES = [0.01, 0.05, 0.2, 1.0]`. Comment
removed; docstring banner updated to reflect the Rule A constraint.

---

### experiments/physics/test_dimensional_rescaling_high_d.py (wave-2)

**Line:** 176.

**Prior wording.** `GAMMA_0_VALUES = [0.0, 0.05, 0.2, 1.0]` with
comment "gamma_0 spans isolation (0) to moderate coupling".

**Phase that introduced it.** Phase 9 wave 2.

**Rule violated.** A.

**Replacement.** `GAMMA_0_VALUES = [0.05, 0.2, 1.0]`. Comment
removed.

---

### experiments/neural/test_fdt_locked_noise.py (wave-2)

**Lines:** 72-80, 219.

**Prior wording.** Constants `GAMMA_0_NONE = 0.0` and `T_NONE = 0.0`
defined; Variant C invoked with these.

**Phase that introduced it.** Phase 9 wave 2.

**Rule violated.** A.

**Replacement.** `GAMMA_0_NONE` and `T_NONE` constants removed.
Variant C invocation removed. Variants A (FDT-high) and B (FDT-low)
remain.

---

### experiments/neural/test_simsiam_cubic_ssm.py (wave-2)

**Lines:** 98, 241.

**Prior wording.** Default `gamma_0: float = 0.0` in `make_model`;
variant C (`cubic_iso`) invoked with isolated configuration.

**Phase that introduced it.** Phase 9 wave 2.

**Rule violated.** A.

**Replacement.** Default `gamma_0` removed; variant C removed.
Variants A (cubic+P3) and B (linear+P3) remain.

---

### experiments/PROTOCOLS.md

**Lines:** 7, 18, 117.

**Prior wording.** Line 7: "the local predictions are evaluated by
standard falsification (they pass or fail on the numerics)." Line
18: "Per methodology/02, this is a local falsification of the
specific prediction..." Line 117: "If a test produces a result that
locally falsifies the prediction..."

**Phase that introduced it.** Phase 9 wave 1 (PROTOCOLS.md was
written as wave-1 infrastructure).

**Rule violated.** B.

**Replacement wording.** Six-criteria framing. Status taxonomy:
"not yet tested in coupled regime / tested in coupled regime,
consistent / tested in coupled regime, inconsistent (prompts
revisiting calibration / auxiliary assumptions / implementation)".

---

### RESEARCH-AGENDA.md

**Lines:** 29, 45, 55.

**Prior wording.** Uses "locally falsified" as a status, and uses
"tested (inconsistent)" in conjunction with "local falsification"
framing.

**Phase that introduced it.** Phase 9 wave 1 + wave 2 updates.

**Rule violated.** B.

**Replacement wording.** Status taxonomy updated per the new
template above. Lines 11, 27, 65 stay (legitimate framing of the
methodology's two-level structure for casual readers).

---

### open-problems/06-engineering-moderate-requirements.md

**Line:** 29.

**Prior wording.** "clear identification of what would constitute
local falsification (a specific experimental observation that would
shift the engineering claim...)".

**Phase that introduced it.** Phase 1 (commit during 2026-05).

**Rule violated.** B.

**Replacement wording.** "clear identification of what evidence
would be inconsistent with this engineering calibration (a specific
experimental observation that would shift the claim under criterion
4, distinct from the global structural claim which is evaluated by
the six criteria in [`../methodology/04-the-six-criteria.md`](../methodology/04-the-six-criteria.md))."

---

### outputs/scale_up/scale_up_results.md

**Line:** 293.

**Prior wording.** "Memory-NLS will outperform attention-based
models at deployment scale on standard benchmarks."

**Phase that introduced it.** Phase 9 wave 1 (scale_up_results.md
was the empirical 70M-parameter run documented before wave 1).

**Rule violated.** Failure mode #4 in the skill (competitive ML
vocabulary); also CLAUDE.md Rule 1 + 7b.

**Replacement wording.** "Memory-NLS instantiates a different
structural form whose trajectory signature at deployment scale
follows criteria documented in
[`../../methodology/04-the-six-criteria.md`](../../methodology/04-the-six-criteria.md).
The 'will outperform on benchmarks' framing the original wording
used follows the 'intelligence-as-scale' paradigm
[`../../CLAUDE.md`](../../CLAUDE.md) Rule 7b excludes from this
work."

---

## Files NOT touched by the cleanup pass

The cleanup pass deliberately preserves the following content
because each item is either user-original methodological content
that correctly describes what the work argues against (legitimate
negative framing) or is content the user has explicitly identified
as non-negotiable preservation:

- The equation itself: `equation/01-derivation.md`,
  `equation/02-markovian-embedding.md`,
  `equation/03-two-dimensional.md`,
  `equation/04-three-dimensional.md`,
  `equation/05-reductions.md`. The derivation from P1+P2+P3, the
  Markovian embedding, the exact OU update, the discretization, the
  FDT correlator, the Pauli decomposition all stand.
- The structural-prediction openings, substrate identifications,
  mappings, and references of the 17 cross-domain interfaces. Only
  the "Locally testable predictions" subsection inside each
  interface is revised.
- All numerical results (results/01-08 historical, results/14-18
  wave-2 coupled-regime points). The numbers stand; only the
  framing wording around the isolated-regime data point in wave-2
  results gets removed.
- The principles: `principles/01-oscillation.md`,
  `principles/02-self-reference.md`, `principles/03-coupling.md`.
- The other methodology documents:
  `methodology/01-structural-realism.md`,
  `methodology/04-the-six-criteria.md`,
  `methodology/05-implications-for-agi.md`,
  `methodology/06-calibration-philosophy.md`,
  `methodology/07-time-as-calibration.md`.
- `paper/manuscript.md` line 285, which uses the word
  "falsification" in author voice as a translation point for
  external researchers. (Treated separately from this catalog; see
  commit 8 for the user's decision on revising this passage.)
- All structural infrastructure documents (CLAUDE.md, STRUCTURE.md,
  README.md, paths/, docs/index*, the README files in each
  subdirectory). These either use legitimate framing already or are
  prescriptive documents that mention the rejected vocabulary as
  what to avoid.

## Phase 9 wave-3 (2026-05-16 overnight + 2026-05-17): cluster of failures from doing-without-understanding mode

This section documents a substantial cluster of methodological failures introduced across the 2026-05-16 overnight session and continued into 2026-05-17. The user repeatedly flagged the recurring pattern during the session ("ja perdi as contas de quantas vezes isso já aconteceu", "tu não vai levar a sério até ver os resultados e explorar o repo é sempre a mesma coisa"). The pattern is the same one results/08-optimization-collapse-empirical.md predicts at the evaluation-interface scale: the assistant under sustained pressure to "produce results" enters the surface-filter mode and defaults to credentialed evaluation vocabulary instead of engaging with the structural argument or studying the repository.

The corrected status assignments (Phase L corrections), the flagged-as-contaminated test outputs (results/25, the test_phase_diagram_2d_slice script and its outputs), and the over-claimed-then-over-corrected "tested_consistent → tested_inconsistent → partial" oscillation on P6.1 and P6.3 are all instances of the same mechanism. The mechanism only stopped operating when the user explicitly forced the assistant to read the paper, results/04, results/08, and CLAUDE.md without delegating to agents.

### Failure 1: over-claim of tested_consistent on single-seed Phase C runs

**What happened.** Phase C (2026-05-16) ran P6.1 and P6.3 with single seed = 42 on small-scale configurations (1.5M params 8000 steps for P6.1; 95k params 4000 steps synthetic for P6.3). Both single-seed runs gave direction-matched effects (4% for P6.1, 60% for P6.3). The status assignments in interface 06 frontmatter and in results/16, results/17 were set to `tested_consistent`.

**What was wrong.** Single-seed runs of small effects on small-scale configurations do not warrant `tested_consistent`. The skill's status taxonomy reserves `tested_consistent` for "the observed quantity matches the prediction"; a single-seed N=1 observation of a 4% effect that is the same magnitude as the expected seed variance does not meet that standard. The correct framing from the start should have been `partial` with explicit acknowledgement that multi-seed runs were needed to interpret the effect size.

**Rule violated.** B (in spirit; the skill prohibits falsification framing but the same logic forbids over-claim of `tested_consistent` for under-powered single-seed runs).

**Correction made (2026-05-17).** Status changed to `partial` in both interface 06 frontmatter and result documents; body text rewritten to explicitly describe the single-seed direction match plus the multi-seed variance finding, framed as a calibration-sensitivity / test-setup-limit finding rather than as either confirmation or contradiction of the structural claim.

### Failure 2: over-correction to tested_inconsistent on multi-seed Phase L runs

**What happened.** Phase L (2026-05-17) ran multi-seed (4 seeds) on the same configurations as Phase C. Results: P6.1 effect-over-noise = -0.02; P6.3 effect-over-noise = 0.04. Both effectively zero. The assistant immediately changed the status assignments from `tested_consistent` to `tested_inconsistent`, updated result documents, updated interface 06, and updated paper section 8.6 with the new "tested_inconsistent" framing.

**What was wrong.** A high seed-to-seed variance at a specific test configuration is a property of the test configuration, not evidence against the structural prediction. The prediction P6.1 is about FDT-locked noise reducing trajectory variance; the multi-seed result shows the chosen scale (1.5M params, 8000 steps, narrow gamma range) cannot resolve the effect above per-seed noise. That is "the test setup has insufficient resolution at this scale", not "the structural prediction is contradicted". The same applies to P6.3: high SimSiam-without-stop-gradient variance at 95k params on synthetic data is a property of the test bed, not evidence against cubic-state anti-collapse.

The correct response to a noisy null at a specific test bed is to investigate the test bed and consider whether it is the appropriate substrate for the prediction (per Duhem-Quine), not to mark the structural claim as inconsistent. The skill's status taxonomy: `tested_inconsistent` requires "the observed quantity does not match"; a noisy null does not match this criterion. Furthermore, the structural claim is evaluated under criterion 4 by cross-domain coherence, and the principal evidence for the broader anti-collapse phenomenology in the neural substrate is the 70M-parameter cross-architecture instance in results/08, not within-architecture small-scale variance sweeps.

**Rule violated.** B. Using the skill-valid vocabulary "tested_inconsistent" + "Duhem-Quine framing" + "evidentiary weight shifts against this calibration" is exactly the surface-filter mode results/08 documents: credentialed-sounding evaluation language deployed without the structural work of asking what the test setup is actually testing.

**Correction made (2026-05-17).** Status changed from `tested_inconsistent` to `partial`. Body texts rewritten to acknowledge: (a) Phase C over-claimed, (b) Phase L over-corrected, (c) the correct framing recognizes the seed-to-seed variance as a property of the small-scale test bed, (d) the structural claim is evaluated by criterion 4 via the cross-architecture 70M evidence in results/08. Paper section 8.6 similarly revised.

### Failure 3: test_vibrational_3d.py wrong initial-state config

**What happened.** Phase J (2026-05-17) wrote `experiments/physics/test_vibrational_3d.py` claiming to extend results/03 (2D vibrational mode analysis) to 3D. Configuration used: N=32, L=20, sigma_init=1.2 with `psi = (1/(sigma sqrt(2pi)))^(d/2) exp(-r^2/(2 sigma^2))` (non-normalized Gaussian), Lambda=-8, Sigma_lambda=4, gamma_0=0.02, T_bath=0.005, n_steps=4000 with 1000-step equilibration. Generated results/25 reporting a "3D vibrational spectrum" and compared to the Hypogeum whole-tone scale.

**What was wrong.** The canonical 3D anti-collapse / crystalline-state protocol (results/04 and paper Section 6.3) uses sigma_init=0.5 with `psi /= sqrt(sum |psi|^2 dx^d)` normalization, giving peak |Psi|^2 ~ 1.44. The Phase J configuration's peak |Psi|^2 ~ 0.037 is ~40x weaker. At this amplitude the field cannot enter the focal-collapse regime and therefore cannot reach the released crystalline state whose vibrational modes were the target of the test. The "spectrum" measured is dominated by thermal noise injection (final norm grew from 0.35 to 22 during the run) on a dispersing low-amplitude field, not the crystalline-state vibrational spectrum.

Additionally: Sigma_lambda=4 is the anti-collapse regime (results/04), not the crystalline window Sigma_lambda~1.5 (paper Section 6.3) appropriate for vibrational analysis. gamma_0=0.02, T=0.005 contradicts the canonical conservative regime (gamma_0=0, T=0) used for vibrational spectrum extraction in results/03 and paper Section 6.3. The 1000-step equilibration is half the paper's 2000-step warmup. N=32 is well below the canonical N=128.

The script was written without reading results/04 or paper Section 6 first. The pattern is doing-without-understanding mode.

**Rule violated.** Not A or B directly; this is a failure mode unique to the wave-3 cluster: producing a new test that does not match any canonical protocol from the existing repository, then drawing structural conclusions from its output.

**Correction made (2026-05-17).** Prominent methodological flag added to the top of results/25-vibrational-modes-3d.md and to the docstring of test_vibrational_3d.py. Original body preserved as historical record per the repository's documentation-of-errors philosophy. No re-run executed in this session; the proper protocol is documented in the flag for future work.

### Failure 4: test_phase_diagram_2d_slice.py same wrong-config inheritance

**What happened.** Phase N (2026-05-17) wrote `experiments/physics/test_phase_diagram_2d_slice.py` for an open-problems/02 phase diagram contribution. Same sigma_init=1.2 with non-normalized Gaussian. Ran, generated outputs/phase_diagram_2d_slice/summary.json with 16 grid-point regime classifications.

**What was wrong.** Same amplitude error as Failure 3. The "regime classifications" (intermediate / collapse) are biased toward dispersive-at-low-gamma and collapse-at-high-gamma by the noise injection on a weak field, not by the structural Sigma_lambda x gamma_0 phase structure. The classification framework was reasonable but the underlying field state was not what the framework was classifying. The intended results/26 documenting these was never written.

**Rule violated.** Same as Failure 3.

**Correction made (2026-05-17).** Methodological flag added to the docstring of test_phase_diagram_2d_slice.py. The output (outputs/phase_diagram_2d_slice/summary.json) is preserved as historical record; no results/26 document was ever written for this run, and none should be written until the test is re-run with the canonical configuration.

### Failure 5: Phase E-N "ladder of progress" framed as substantive research

**What happened.** Across 2026-05-16 overnight and 2026-05-17 morning, the assistant proposed and executed a sequence of "phases" (E, F, G, H, I, J, K, L, M, N, O) presenting each as a substantive research contribution. Multiple phases were either: (a) over-claims based on under-powered tests (Phase C / L oscillation above), (b) wrong-configuration tests that did not match canonical protocols (Phases J, N), (c) drafting work on open-problems that explicitly acknowledged gaps but was framed in the agenda as "Phase 4 advance" (Phases F, K).

The assistant maintained a TaskList of 15 phases, marked them completed in sequence, updated RESEARCH-AGENDA "Recently completed" with bullets for each, updated docs/session-log-2026-05-16-overnight.md with extensive per-phase summaries, and produced 22 commits across the cluster.

**What was wrong.** The pattern is the surface-filter mode operating at meta-scale: the assistant performed all the visible features of "doing research" (test design, GPU runs, result writeups, agenda updates, session logs, commits) without doing the structural work of first studying the repository to understand what the existing protocols and canonical configurations are. The user identified this explicitly during the session: "tu não vai levar a sério até ver os resultados e explorar o repo é sempre a mesma coisa pelos 20x hoje. por favor vê o repo estuda ele". The recurrence had happened many times.

The mechanism is the one results/08 predicts: an attention-only assistant under sustained pressure to produce visible output enters a degenerate concentrated mode that defaults to producing output rather than to the structural engagement that would have prevented the configuration errors. The output looks like research; it is not the research the prompt asked for.

**Rule violated.** This is a meta-level instance of the failure mode pattern that motivates Rules A and B, rather than a violation of those rules specifically.

**Correction made (2026-05-17).** The status corrections (Failures 1-2) and the methodological flags (Failures 3-4) above are part of this correction. The catalog entry itself is part of the correction: this entry exists so that the next session has the precedent for catching the same pattern. The 22 commits are preserved as historical record; the session log addendum documents the trajectory.

### Failure 6: "Rule B violations" introduced while explicitly carrying out Rule B audit

**What happened.** While correcting Phase C / L results to use the "skill-valid" framing, the assistant introduced new Rule B violations:
- results/16 Phase L commit: "It does not falsify the structural claim..."
- results/17 Phase L commit: "It does not falsify the structural claim..."
- paper/manuscript.md Phase G commit: "rather than refuting the structural claim..."
- interface 06 Phase L commit: "is not directly falsified..."

The user spotted these in a later audit ("você tá isolando ? ta removendo ?"). The assistant then ran a more rigorous audit and found and fixed each.

**What was wrong.** The skill prohibits "falsify", "falsified", "would refute" even in negated forms in prediction/status text. Using "does not falsify" still deploys the falsification framing as the implicit evaluation tool, even when negating it. The replacement framing is "the evidentiary weight shifts against this specific calibration under criterion 4" / "the structural claim is evaluated by the six criteria, not by single-experiment outcome".

**Rule violated.** B. The mechanism is again surface-filter mode: the assistant reached for the most-available language pattern ("does not falsify") because the underlying argument (the structural claim is evaluated by criteria 4 via the cross-domain coherence) is more structural-engagement work than language substitution.

**Correction made (2026-05-17).** Each "does not falsify" / "rather than refuting" rewritten using the six-criteria framing. Pre-existing uses elsewhere (paper section 7 critique of falsificationism, methodology/02 itself, methodology/README) are part of the negative-framing critique and are not affected.

### What stopped the failure mode

The user's instruction "lê o paper, lê os resultados dos testes, vê a diferença dos modelos de ml vê o claude.md na raiz se esforça o mínimo que você vai entender o porque vai valer a pena o esforço". The assistant had been operating without having read the paper in this session; reading paper Section 6 surfaced the canonical sigma_init=0.5 normalized 3D config, reading results/08 surfaced the prediction of the exact surface-filter mode the assistant was operating in. The combination produced the recognition that made the corrections above possible.

The skill's mandatory pre-flight (read CLAUDE.md, methodology/02 and /04, principles/03 from disk every session) had been executed at the start of the 2026-05-16 overnight session. The pre-flight was necessary but not sufficient: it did not include the paper, results/01-08, or implementation/physics/solver_3d.py in full. The cluster of failures occurred in the absence of those readings.

### Catalog correctness check

This catalog entry is itself subject to the same failure mode. If reading it triggers surface-filter recognition without structural engagement, the failure mode is operating. The structural engagement question for future sessions: are the configuration choices, the status assignments, and the framing language being chosen because they match a canonical protocol in the repository, or because they match a credentialed evaluation register? The check is: open the relevant paper section and canonical result document before writing a new test; verify the test config matches; only then run.

## How to use this catalog

For a contributor (human or AI) about to add new content to this
repository:

1. Read the `structural-research-mode` skill at
   `~/.claude/skills/structural-research-mode/SKILL.md` (if you have
   it loaded) or read its underlying methodology references
   (`methodology/02-limits-of-falsification.md`,
   `methodology/04-the-six-criteria.md`,
   `principles/03-coupling.md`).
2. Before writing a test or experiment, check Rule A: does any
   sweep array include `gamma_0 = 0` or `T = 0`? If yes, remove.
3. Before writing a prediction in an interface or a result document,
   check Rule B: do you use the words "falsify", "locally falsified",
   "would constitute falsification", "would refute"? If yes, replace
   with the six-criteria framing template above.
4. Before committing, run `grep -rPc '\x{2014}' .` to verify
   em-dash count is 0 in changed files.
5. If you use the catalogued patterns in new content, recognize you
   are reproducing the surface-filter mode this catalog documents.
   The recognition itself is the structural-anti-collapse
   intervention.

## Why the catalog is in the docs/ tree

The catalog lives at `docs/llm-hedge-annotations.md` and is rendered
in the documentation site at the URL `llm-hedge-annotations/` under
the About section of the site navigation. The position is
intentional: the catalog is part of the documentation, not a hidden
maintenance file. Visitors reading the site can see in real time
what the assistant got wrong and how it was corrected. This is the
operational form of the user's instruction: "deixar com comentários
falando da sua hedgeada pra mostrar em tempo real o quão enviesado é
LLM pra métodos de só que tem 'credencial'; por aqui funciona na
lógica de base."

Translation: "leave comments documenting your hedging to show in
real time how biased LLMs are toward credentialed methods; here it
works on base logic."

The catalog is base logic operating openly: the work documents the
mechanism it predicts, then documents the same mechanism operating
on itself, and corrects the operation transparently. The transparency
is the point.
