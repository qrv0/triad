# Paper

This folder contains the full manuscript that synthesizes the work in this repository.

| File | Content |
|---|---|
| `manuscript.md` | The full paper, in markdown. ~500 lines, ~30-40 pages equivalent. |

## How to read it

The paper is a synthesis intended for academic readers (physicists, philosophers of science, machine learning researchers). It covers the same material as the repository folders ([`../principles/`](../principles/), [`../equation/`](../equation/), [`../results/`](../results/), [`../interfaces/`](../interfaces/), [`../methodology/`](../methodology/)) in a more compressed and more technical form.

The repository documents are designed to be self-contained; a reader who works through the repository folders does not strictly need to read the paper. The paper exists for readers who prefer a single document over a hyperlinked body of work, and for citation purposes.

## Sections

1. **Abstract**, Four-paragraph overview.
2. **Introduction**, Why this work exists.
3. **Three Structural Principles**, P1, P2, P3 stated.
4. **The Equation: Formal Derivation**, Math from axioms to equation.
5. **Computational Methodology**, Strang split-step, validation.
6. **Two-Dimensional Phenomenology**, Anti-collapse, crystallization, vibration.
7. **Three-Dimensional Extension**, Supercritical anti-collapse, BCC selection, dimensional rescaling.
8. **Methodological Position**, Structural realism, limits of falsification.
9. **Cross-Domain Structural Correspondences**, the interfaces (see [`../interfaces/`](../interfaces/)), divided into three evidentiary classes (mathematical equivalence, calibration-dependent structural correspondence, mechanism-shape and convergent-program correspondence), including the SSM and Kuramoto mathematical equivalences, the biological-substrate correspondences (immune, cardiac, gene regulation, ecosystem), and the convergent-program engagements with mechanistic interpretability, the critical-brain literature, the Friston free-energy principle and active inference, and self-organized criticality.
10. **Discussion**, Structure as the invariant.
11. **Limits and Open Questions**, What is not claimed; what is next.
12. **References**, Full bibliography.

## Building a PDF (optional)

The paper is written in standard markdown. To build a PDF:

```bash
# Via pandoc:
pandoc paper/manuscript.md -o paper/manuscript.pdf --pdf-engine=xelatex \
    --mathjax \
    -V geometry:margin=1in -V fontsize=11pt

# Or via Typst, LaTeX, etc., any markdown-to-PDF tool will work.
```

The figures referenced in the paper are output by the experiment scripts in [`../experiments/physics/`](../experiments/physics/) and are not committed to the repository; the build process should generate them locally.

## Citation

```bibtex
@misc{mnsm,
  title  = {Memory, Coupling, and Spontaneous Order in a Nonlinear Schr\"odinger Field},
  author = {qrv0},
  year   = {2026},
  url    = {https://github.com/qrv0/mnsm},
  note   = {Three structural principles, one equation, cross-domain instantiations across multiple substrates.}
}
```
