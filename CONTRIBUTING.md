# Contributing

This work is licensed open (MIT for code, CC BY 4.0 for documentation).
Contributions across the entire range of the repository are welcomed , 
from typo fixes to new cross-domain interfaces, from numerical
reproducibility verification to extensions of the equation into new
substrates. Three structural notes about the kind of contribution that
fits this repository:

## What kind of contributions fit

**Strongly fits:**

- New cross-domain interfaces. If you observe the same structural form
  in a domain not yet documented here — economic, biological, ecological,
  social — and can articulate the correspondence with peer-reviewed
  citations, that is exactly what the repository is for. The
  structural-realist methodology requires cross-domain coverage; more
  substrates strengthen the structural claim.

- Empirical replications of the documented results on different
  hardware, different random seeds, different software stacks. Confirming
  bit-for-bit reproducibility, or identifying specific deviations, is
  valuable.

- Extensions of the physics solver to new regimes (higher dimensions,
  alternative kernels, additional gauge structure, different boundary
  conditions). The solver in `implementation/physics/` is a foundation,
  not a complete library.

- Improvements to documentation accessibility: better illustrations,
  clearer explanations, additional reader paths (`paths/if-you-are-from-X.md`)
  for backgrounds not yet covered (chemistry, materials science,
  economics, biology, etc.).

- Notebooks that demonstrate specific properties of the equation
  interactively. Additional `playground/` notebooks are welcome.

**Should be discussed first** (open an issue):

- Deletion or significant restructuring of existing documents.
- Changes to the methodology framework (`methodology/`), these touch
  the load-bearing position of the work.

**Generally does not fit:**

- Pure benchmark-optimization PRs ("MNSM achieves N% better val_ppl
  than baseline X with this hyperparameter sweep"). The work does not
  adopt the benchmark-competitive paradigm; see
  [`CLAUDE.md`](CLAUDE.md) for the methodological position.
- "Modernization" PRs that import standard ML conventions (RoPE, RMSNorm,
  SwiGLU, etc.) into the MNSM implementation without structural
  motivation. The implementation is kept architecturally minimal by
  design.

## Methodological alignment

The repository operates under a specific methodological frame
(structural realism, in the sense of Worrall 1989 and Ladyman & Ross 2007).
Contributions that respect this frame are easier to integrate. The frame
is documented in:

- [`methodology/01-structural-realism.md`](methodology/01-structural-realism.md), the position.
- [`methodology/02-limits-of-falsification.md`](methodology/02-limits-of-falsification.md), why strict falsificationism is in tension with the work's content.
- [`methodology/03-how-to-evaluate-this.md`](methodology/03-how-to-evaluate-this.md), the procedure.
- [`methodology/04-the-six-criteria.md`](methodology/04-the-six-criteria.md), the evaluation criteria.

If you find the frame compelling, your contributions will land cleanly. If
you find the frame unconvincing, the methodology folder explains why the
choices were made; you may still contribute to the technical content
(equation, solver, results) without endorsing the framing.

## AI-assisted contribution

If you are using an AI assistant (Claude, GPT, Gemini, etc.) to help
with contributions to this repository, please read [`CLAUDE.md`](CLAUDE.md)
first. It is the set of operational constraints that ensures AI-assisted
work aligns with this repository's structural-realist methodology rather
than with the default frame an AI assistant trained on standard ML
content would naturally adopt.

## Practical workflow

1. **Open an issue** describing the contribution before opening a PR for
   anything beyond typo-level changes. This avoids wasted work on
   misaligned PRs.

2. **Branch off `main`**. Branch names reflect the contribution scope
   (`docs/`, `interface/`, `implementation/`, `experiment/`, `paper/`).

3. **Verify reproducibility** for any change that touches numerical
   results. The conservation tests in `tests/test_conservation.py` are
   the minimum bar; additional tests for new functionality are
   appreciated.

4. **Pull request descriptions** should state which structural principle
   or evaluation criterion the contribution serves. This helps the
   reviewer understand the alignment quickly.

5. **Tone in PR comments**: direct, specific, structurally grounded. No
   sycophancy, no hedging, no benchmark-competitive framing. See
   [`CLAUDE.md`](CLAUDE.md) for the conversational frame the
   repository adopts.

## Code of conduct

Engage with the work and with each other on its structural merits.
Disagreement is welcome when articulated; dismissal via category
weaponization ("speculative", "anthropomorphic", "fringe") without
engagement with the content is not. The methodology folder addresses
why this distinction matters.

## Licensing of contributions

By contributing you agree that your contributions are licensed under the
same terms as the rest of the repository: MIT for code, CC BY 4.0 for
documentation. You retain copyright; the licenses apply to the
distribution and modification rights.

## Questions

Open an issue. Tag with the relevant folder (`physics`, `neural`,
`methodology`, `interface`, `documentation`, etc.).
