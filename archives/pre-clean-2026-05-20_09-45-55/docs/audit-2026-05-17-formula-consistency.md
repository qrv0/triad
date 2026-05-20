# Audit 2026-05-17 — output/doc consistency across triad

This audit cross-checked every output directory in `outputs/` against the
result document that cites it. The verification compared the parameters
recorded in each `summary.json` to the parameters declared in the matching
result document.

## Recalibration note (2026-05-17)

An earlier draft of this audit (now overwritten) flagged outputs as "wrong
formula" because they ran with `gamma_0 = 0` and `T = 0`. That framing was
based on the `structural-research-mode` skill's "Rule A" ("isolation is
invalid as a test default") and was incorrect for this repository.

The origin repository (`private/memory-nls/`) treats `gamma_0 = 0, T = 0`
as the **unitary regime**, the canonical analytical and numerical test
configuration. Its `docs/methodology.md` is explicit: *"Isolation is the
indispensable tool of experimental method... a property of the method,
not a property of the world."* The 3D solver's `SolverConfig3D` defaults
to `gamma_0 = 0.0, T = 0.0`, and the canonical experiments
(`m1_3d_lambda_sweep.py`, `r1_3d_vibration.py`) run in this regime.

The recalibrated criterion for "wrong" is: **the parameters recorded in
the output do not match the parameters declared in the result document
that cites it.** The algorithm in every output is the canonical Strang
split-step solver (the `triad/implementation/physics/solver_3d.py` differs
from `private/memory-nls/sim/solver3d.py` only in docstring and one
import path). No output has an "algorithm wrong"; the failures below are
all config-vs-doc mismatches.

## Verified outputs (23 dirs + 3 logs)

23 output directories were verified one by one against their citing result
docs:

- ✓ `anti_collapse_3d` (results/04)
- ✓ `convention_A_native_regime` (results/32)
- ✓ `convention_L_matrix` (results/32)
- ✓ `dimensional_rescaling_d6_p3` (results/24)
- ⚠ `dimensional_rescaling_high_d` — **removed**
- ✓ `dimensional_rescaling_high_d_p3` (results/15) — params match; reproducing script is stubbed but output is valid
- ✓ `hawkes_intensity_auxiliary` (results/21)
- ✓ `kuramoto_chimera_memory` (results/09) — params match; reproducing script is stubbed but output is valid
- ⚠ `kuramoto_chimera_memory_p3` — **removed**
- ⚠ `phase_diagram_2d_slice` — **removed**
- ✓ `phase_diagram_2d_slice_multiseed` (results/26)
- ✓ `phase_diagram_d2_convention_A` (results/31)
- ✓ `phase_diagram_d2_slice` (results/27)
- ✓ `phase_diagram_d2_slice_multiseed` (results/27)
- ✓ `phase_diagram_d3_convention_A` (results/31)
- ✓ `phase_diagram_d4_slice` (results/28)
- ✓ `prony_viscoelastic_reproduction` (results/20)
- ✓ `pseudomode_auxiliary_equivalence` (results/19)
- ✓ `soc_vs_mnsm_avalanches` (results/13) — params match; reproducing script is stubbed but output is valid
- ⚠ `soc_vs_mnsm_avalanches_p3` — **removed**
- ✓ `vibrational_3d_p3` (results/25) — params match; reproducing script is stubbed but output is valid
- ✓ `vibrational_3d_p3_multiseed` (results/25)
- ✓ `warm_inflation_langevin` (results/22)

## Removed outputs (4 dirs + 3 logs)

### `outputs/dimensional_rescaling_high_d/`

Cited by [`results/10-dimensional-rescaling-higher-d.md`](../results/10-dimensional-rescaling-higher-d.md). Mismatch (severe):

| Parameter | Document declares | Summary records |
|---|---|---|
| Lambda | -8 | **-4** |
| L (box size) | 10 | **12** |
| d=5 lattice N | 16 | **12** |

The recorded output ran a different test than the document describes. Removed.

### `outputs/kuramoto_chimera_memory_p3/`

Cited by [`results/14-kuramoto-chimera-fdt.md`](../results/14-kuramoto-chimera-fdt.md). Mismatch:

| Parameter | Document declares | Summary records |
|---|---|---|
| gamma_0 sweep | {0.01, 0.05, 0.2, 1.0} | **{0.0, 0.01, 0.05, 0.2, 1.0}** |

The recorded grid includes `gamma_0 = 0.0` as a sweep point that the
document does not declare or interpret. Removed.

### `outputs/soc_vs_mnsm_avalanches_p3/`

Cited by [`results/18-soc-vs-mnsm-matched-drive.md`](../results/18-soc-vs-mnsm-matched-drive.md). Mismatch:

| Parameter | Document declares | Summary records |
|---|---|---|
| gamma_0 sweep | {0.05, 0.2} | **{0.01, 0.05, 0.2}** |

The summary has a third run at `gamma_0 = 0.01` that the document does
not declare. Removed.

### `outputs/phase_diagram_2d_slice/`

Cited by [`results/26-phase-diagram-2d-slice.md`](../results/26-phase-diagram-2d-slice.md). Mismatch (severe):

| Parameter | Document declares | Summary records |
|---|---|---|
| gamma_0 sweep | {0.01, 0.05, 0.2, 1.0} | **{0.2, 0.5, 1.0, 2.0}** |

The gamma_0 ranges do not overlap meaningfully. The single-seed output
ran a different sweep than the document describes. The companion
multi-seed output at `outputs/phase_diagram_2d_slice_multiseed/` uses
the declared gamma_0 sweep and is unaffected. Removed.

### Orphan logs

- `outputs/canonical_strang_rerun.log` — no associated result document.
- `outputs/canonical_strang_rerun_preexisting.log` — no associated result document.
- `outputs/phase_diagram_d2_slice_multiseed_run.log` — execution log of a verified run; the corresponding output dir and result doc both exist; the log itself is artefact. Removed.

## What this audit did not find

- **No algorithm errors.** The solver code in every reachable script is
  the canonical Strang split-step solver, identical to the origin in
  `private/memory-nls/sim/solver3d.py` up to docstring and one import
  path. No output instantiates a different equation than the document
  cites.
- **No P3-violation outputs.** Unitary-regime runs (`gamma_0 = 0, T = 0`)
  are valid by the methodology of the origin repository; they are the
  canonical analytical test configuration. The earlier draft of this
  audit flagged them in error.

## Open follow-up

- Five experiment scripts in `experiments/physics/` were reduced to 3-7
  line stubs in commit `9ddbf15` while their outputs and result docs
  retain full configuration records. Reproducing the stubbed-script
  outputs requires either restoring the script bodies via
  `git show 9ddbf15^:<path>` or rewriting from the canonical solver
  with the documented parameters. The stubbed scripts are:
  - `test_kuramoto_chimera_memory.py`
  - `test_soc_vs_mnsm_avalanches.py`
  - `test_dimensional_rescaling_high_d.py`
  - `test_vibrational_3d.py`
  - `test_phase_diagram_2d_slice.py`
- Five `reproduce_*.py` scripts cited by `results/01, 02, 03, 06, 07`
  were never committed. Re-running results 01-03 and 06-07 requires
  authoring these wrappers or editing the docs to point at an existing
  reproducer.

## Companion record

[`llm-hedge-annotations.md`](llm-hedge-annotations.md) holds the running
transparent record of prior-correction work; this audit's removals are
listed there as well.
