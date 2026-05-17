# mnsm

### Memory-NLS — an active research program on persistent extended systems

**Three structural principles. One equation. Twenty-two substrates across two repositories.**

[![License: MIT](https://img.shields.io/badge/Code_License-MIT-blue.svg)](LICENSE)
[![License: CC BY 4.0](https://img.shields.io/badge/Docs_License-CC_BY_4.0-lightgrey.svg)](LICENSE-docs)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Paper](https://img.shields.io/badge/paper-manuscript.md-green)](paper/manuscript.md)
[![ML implementation: mnsm-ml](https://img.shields.io/badge/ML_implementation-mnsm--ml-orange)](https://github.com/qrv0/mnsm-ml)

![3D field anti-collapse with versus without memory](assets/anti_collapse_hero.gif)

*One equation, one initial condition, one ingredient added. Left: the field collapses to a lattice-clipped singular state. Right: the multi-timescale memory potential builds up with lag, bounds the collapse, and releases the field into an extended state. The same trajectory-shape signature appears across [twenty-two substrates](#where-it-appears) where the structural form of P1+P2+P3 is operative — from BAO-era cosmological structure formation to 70M-parameter neural network optimization. Detail in [`results/04-anti-collapse-3d.md`](results/04-anti-collapse-3d.md); cross-substrate observable in [`mnsm-ml/results/01`](https://github.com/qrv0/mnsm-ml/blob/main/results/01-optimization-collapse-empirical.md).*

---

## What this is

An active research program tracking the appearance of a single mathematical structure across substrates. The structure is derived from three principles about persistent extended entities (P1 oscillation, P2 self-reference via memory, P3 coupling). The principles select an equation. The equation appears, with substrate-specific calibration, in twenty-two independently documented physical, biological, and computational systems — currently. The list is not closed.

The work is not assembled from prior literature. The principles come from observation of how persistent extended things behave; the equation is what those principles force; the cross-substrate instances are where the form independently appears. The methodological frame is **structural realism**, not falsificationist competitive empiricism; the work is evaluated by [six structural criteria](methodology/04-the-six-criteria.md) under [`methodology/`](methodology/), not by single-experiment refutation or benchmark performance.

The ML implementation depth — PyTorch Memory-NLS sequence layer, matched-Transformer comparison, the 70M-parameter optimization-collapse empirical finding — lives in the [`mnsm-ml`](https://github.com/qrv0/mnsm-ml) spinoff. The two repositories advance in parallel.

---

## The equation

$$
i\hbar\, \partial_t \Psi = \left[\,-\frac{\hbar^2}{2m} D^2 + V_{\text{ext}} + \Lambda |\Psi|^2 + V_{\text{mem}} + \alpha (-\Delta)^{\sigma/2} - i\Gamma\,\right]\Psi + \eta
$$

with $V_{\text{mem}} = \sum_j \lambda_j y_j$ and $\partial_t y_j = \nu_j (\rho - y_j)$, and $\eta$ satisfying the FDT correlator $\langle\eta\eta^*\rangle = 2\gamma_0 k_B T \delta(t-t')\delta(\mathbf{x}-\mathbf{x}')$.

P1 is the kinetic and cubic terms (intrinsic oscillation). P2 is the auxiliary-field memory hierarchy $\{y_j\}$ with relaxation rates $\{\nu_j\}$ (self-reference across multiple timescales). P3 is the FDT-locked dissipation $\Gamma$ and noise $\eta$ (coupling to environment). Full derivation from principles: [`equation/01-derivation.md`](equation/01-derivation.md). Markovian embedding showing the memory hierarchy is the diagonal SSM structure: [`equation/02-markovian-embedding.md`](equation/02-markovian-embedding.md).

---

## Where it appears

Twenty-two substrates documented across two repositories, in three evidentiary classes (full catalog in [`interfaces/README.md`](interfaces/README.md)):

**Mathematical equivalence, no calibration required.** Other NLS systems ([`01`](interfaces/01-other-nls-systems.md): BEC, optical solitons, deep-water waves); diagonal-state structured state space models in machine learning ([`mnsm-ml/01-state-space-models.md`](https://github.com/qrv0/mnsm-ml/blob/main/interfaces/01-state-space-models.md)); memory-augmented Kuramoto oscillators ([`10`](interfaces/10-kuramoto-synchronization.md)).

**Calibration-dependent structural correspondence.** Baryon acoustic oscillations in early-universe cosmology ([`02`](interfaces/02-baryon-acoustic.md)); Chladni cymatic patterns ([`03`](interfaces/03-chladni-cymatics.md)); gamma-frequency neural entrainment ([`04`](interfaces/04-gamma-entrainment.md)); archaeoacoustic resonance in megalithic chambers ([`05`](interfaces/05-archaeoacoustic-resonance.md)); B-cell affinity maturation ([`11`](interfaces/11-immune-affinity-maturation.md)); active matter with alignment memory ([`13`](interfaces/13-active-matter.md)); cardiac electrophysiology ([`15`](interfaces/15-cardiac-dynamics.md)); gene regulation and circadian rhythms ([`16`](interfaces/16-gene-regulation-circadian.md)); non-Markovian open quantum systems via pseudomode embedding ([`18`](interfaces/18-pseudomode-quantum.md)); generalized Maxwell viscoelasticity ([`19`](interfaces/19-viscoelasticity-prony.md)); warm-inflation cosmology ([`20`](interfaces/20-warm-inflation.md)); Hawkes self-exciting processes ([`21`](interfaces/21-hawkes-intensity.md)); earthquake-cycle dynamics ([`22`](interfaces/22-earthquake-cycle.md)).

**Mechanism-shape and convergent-program correspondence.** Cosmological expansion as anti-collapse release ([`07`](interfaces/07-cosmological-expansion.md)); mechanistic interpretability of attention-based language models ([`mnsm-ml/02-mechanistic-interpretability.md`](https://github.com/qrv0/mnsm-ml/blob/main/interfaces/02-mechanistic-interpretability.md)); critical-brain dynamics ([`09`](interfaces/09-critical-brain.md)); Friston's free-energy principle and active inference ([`12`](interfaces/12-friston-free-energy.md)); self-organized criticality ([`14`](interfaces/14-self-organized-criticality.md)); multi-species ecosystem dynamics ([`17`](interfaces/17-ecosystem-dynamics.md)).

Each interface document derives the structural mapping, names substrate-specific calibration choices, and lists locally testable predictions evaluated under [criterion 4 (cross-domain coherence)](methodology/04-the-six-criteria.md). New substrates are added as the structural form is recognized; the program is not closed.

---

## Where it has been verified

**3D anti-collapse** ($\Sigma\lambda = 4$, $\sigma_0 = 0.5$ normalized, $N = 128$, $L = 20$, $dt = 0.0025$, 4000 steps):

| $\Lambda$ | No-memory final peak | With-memory final peak | Ratio |
|---|---|---|---|
| $-6$ | 0.0015 | 0.0006 | 2.5× |
| $-8$ | 61.96 | 0.0006 | $\sim 10^5$ |
| $-10$ | 59.27 | 0.0027 | $\sim 2 \times 10^4$ |
| $-12$ | 57.02 | 0.0018 | $\sim 3 \times 10^4$ |

The no-memory runs at $\Lambda \le -8$ lock at the lattice-clipped peak ($\sim 57$–$62$); the memoried runs at the same $\Lambda$ unwind to peaks of order $10^{-3}$. Four-to-five orders of magnitude separation across the supercritical $\Lambda$ range. Detail: [`results/04-anti-collapse-3d.md`](results/04-anti-collapse-3d.md).

**Spontaneous Bravais selection** (3D, $\Lambda = -8$, $\Sigma\lambda = 1.5$): the released crystalline state consistently selects body-centered cubic symmetry, score $\sim 0.44$ with gap $+0.13$ over the next-best option. Detail: [`results/05-bravais-selection.md`](results/05-bravais-selection.md).

**Dimensional rescaling** of the memory coupling required to release supercritical collapse: $\Sigma\lambda_{\text{crit}} \sim |\Lambda|/d$ for $d \in \{2, 3\}$ (derivable from the geometry of the collapse focal region). Higher-dimensional extension is in active investigation; the simple $1/d$ form does not extend cleanly past $d = 3$ in canonical parameter ranges. Detail: [`results/06-dimensional-rescaling.md`](results/06-dimensional-rescaling.md), [`results/24-dimensional-rescaling-d6.md`](results/24-dimensional-rescaling-d6.md).

**Conservation diagnostics** (norm, FDT thermalization, memory-field stationary state, dissipative decay): verified to machine precision in fp64. Detail: [`tests/test_conservation.py`](tests/test_conservation.py).

---

## How to read this

The work asks to be read by criteria appropriate to a structural theory. Two principles govern the methodological frame, documented in [`methodology/`](methodology/):

1. **Coupling is the default, isolation is temporary.** The third structural axiom (P3) asserts that perfect dynamical isolation does not occur. Detail: [`principles/03-coupling.md`](principles/03-coupling.md).

2. **Structural realism, not strict falsificationism.** A theory whose third axiom denies isolation cannot be evaluated by single-experiment refutation that presupposes isolation. The work is evaluated by six structural criteria: internal consistency, reproducibility, generative scope, cross-domain coherence, parsimony, comprehensiveness. Detail: [`methodology/02-limits-of-falsification.md`](methodology/02-limits-of-falsification.md).

Pick your reading entry point:

- → **I'm new to all this**: [`paths/if-you-are-new.md`](paths/if-you-are-new.md)
- → **I'm from physics**: [`paths/if-you-are-from-physics.md`](paths/if-you-are-from-physics.md)
- → **I'm from machine learning**: [`paths/if-you-are-from-ml.md`](paths/if-you-are-from-ml.md) (also leads into [`mnsm-ml`](https://github.com/qrv0/mnsm-ml))
- → **I'm from neuroscience**: [`paths/if-you-are-from-neuroscience.md`](paths/if-you-are-from-neuroscience.md)
- → **I'm from philosophy of science**: [`paths/if-you-are-from-philosophy.md`](paths/if-you-are-from-philosophy.md)

---

## See it run

```bash
git clone https://github.com/qrv0/mnsm
cd mnsm
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pip install cupy-cuda12x  # or cupy-cuda11x for older CUDA

# Validate the solver (~30 seconds on RTX 4060)
python -m tests.test_conservation

# Reproduce the headline 3D anti-collapse result under coupled regime (~4 minutes)
python experiments/physics/reproduce_3d_anti_collapse.py
```

Or watch in a notebook without local setup:

- [`playground/01-just-watch.ipynb`](playground/01-just-watch.ipynb): a Gaussian state spontaneously crystallizing into a BCC pattern.
- [`playground/02-adjust-the-knobs.ipynb`](playground/02-adjust-the-knobs.ipynb): parameter exploration.
- [`playground/03-build-your-own.ipynb`](playground/03-build-your-own.ipynb): guided implementation from scratch.

All numerical results use fixed random seeds and reproduce bit-for-bit on identical hardware (NVIDIA RTX 4060 Laptop GPU, Arch Linux, CUDA 12.x).

---

## What is in this repository

| Folder | Content |
|---|---|
| [`principles/`](principles/) | The three structural axioms (P1, P2, P3) |
| [`equation/`](equation/) | Derivation, Markovian embedding, 2D and 3D forms, reductions to known equations |
| [`results/`](results/) | Numerical findings: anti-collapse, crystallization, Bravais selection, vibration spectrum, dimensional rescaling |
| [`interfaces/`](interfaces/) | Cross-domain mappings (20 substrates here + 2 in [`mnsm-ml`](https://github.com/qrv0/mnsm-ml)) |
| [`methodology/`](methodology/) | Structural realism, limits of falsification, six criteria, calibration philosophy, time-as-calibration, Mori-Zwanzig foundation, tautology objection |
| [`paths/`](paths/) | Reader-background-specific entry routes |
| [`playground/`](playground/) | Interactive notebooks (Colab-runnable) |
| [`implementation/`](implementation/) | CuPy physics solver (the PyTorch ML layer lives in [`mnsm-ml`](https://github.com/qrv0/mnsm-ml)) |
| [`experiments/`](experiments/) | Reproduction scripts |
| [`paper/`](paper/) | The full manuscript |
| [`tests/`](tests/) | Conservation, FDT, anti-collapse sanity tests |
| [`assets/`](assets/) | Visual assets (GIFs, plots) |
| [`open-problems/`](open-problems/) | Catalogue of open research problems with uniform template |
| [`RESEARCH-AGENDA.md`](RESEARCH-AGENDA.md) | 6/12/24-month research horizons; convergent programs; how to contribute |
| [`STRUCTURE.md`](STRUCTURE.md) | Why the repository is shaped the way it is |

---

## Current state and open frontiers

Three layers with different stability characteristics.

**Stable load-bearing content:**

- The three structural principles, the equation derivation, the Markovian embedding, the reductions to known equations.
- The methodological frame: structural realism, six criteria, calibration philosophy, time-as-calibration, Mori-Zwanzig foundation, tautology-objection treatment.
- Conservation diagnostics verified to machine precision.
- 3D anti-collapse under P3-coupled regime, with transient-peak separation of $\sim 14\times$ at $\Lambda = -8$.
- The cross-substrate empirical instance at 70M neural network parameters in [`mnsm-ml`](https://github.com/qrv0/mnsm-ml).
- Twenty cross-domain interfaces here plus two in the ML spinoff, calibration-acknowledged.

**Active frontier:**

- Recalibration of phase-diagram and vibrational tests to the coupled-regime canonical (per [`CLAUDE.md`](CLAUDE.md) Rule 10), in progress as of 2026-05-17.
- Sharpening predictions in the recently added interfaces (18 pseudomode quantum, 19 viscoelasticity, 20 warm inflation, 21 Hawkes, 22 earthquake cycle) into testable protocols.
- Detail: [`RESEARCH-AGENDA.md`](RESEARCH-AGENDA.md).

**Known gaps:**

- Eight open problems catalogued in [`open-problems/`](open-problems/) with status `not_yet_tested` or `partial`.
- Analytical derivation of the anti-collapse mechanism beyond the leading-order skeleton ([`open-problems/01`](open-problems/01-analytical-anti-collapse.md)).
- Dimensional rescaling formula's behavior beyond $d = 3$ ([`results/24-dimensional-rescaling-d6.md`](results/24-dimensional-rescaling-d6.md) suggests the simple $1/d$ form does not extend cleanly).
- Renormalization-group analysis ([`open-problems/04`](open-problems/04-continuum-rg.md)) and quantum extension ([`open-problems/05`](open-problems/05-quantum-extension.md)).

> Coupling is the default. Issues, pull requests, and external mappings of the structure to further domains are explicitly welcomed. See [`CONTRIBUTING.md`](CONTRIBUTING.md) for the engagement workflow.

---

## Citation

```bibtex
@misc{mnsm,
  title  = {Memory-Nonlinear State Models: An active research program on persistent extended systems},
  author = {qrv0},
  year   = {2026},
  url    = {https://github.com/qrv0/mnsm},
  note   = {Three structural principles, one equation, twenty-two cross-substrate documentations across mnsm and mnsm-ml.}
}
```

The full paper is in [`paper/manuscript.md`](paper/manuscript.md); the ML implementation depth is in [`mnsm-ml`](https://github.com/qrv0/mnsm-ml).

---

## License

Code: [`LICENSE`](LICENSE) (MIT). Documentation and paper: [`LICENSE-docs`](LICENSE-docs) (CC BY 4.0).

---

## On AI-assisted contribution

This work was developed with substantial AI-assisted formalization. The methodological frame has direct implications for how AI assistants should engage with the codebase: avoid competitive-benchmark framing, respect the structural-realist evaluation criteria, do not dismiss cross-domain interfaces as "speculative". The operational constraints in [`CLAUDE.md`](CLAUDE.md) ensure that assistance aligns with what this work is, rather than the default frame an AI assistant trained on standard ML content would naturally adopt.
