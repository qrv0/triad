# mnsm

### Memory-Nonlinear State Models

**Three structural principles. One equation. Seventeen cross-domain instantiations.**

[![License: MIT](https://img.shields.io/badge/Code_License-MIT-blue.svg)](LICENSE)
[![License: CC BY 4.0](https://img.shields.io/badge/Docs_License-CC_BY_4.0-lightgrey.svg)](LICENSE-docs)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Paper](https://img.shields.io/badge/paper-manuscript.md-green)](paper/manuscript.md)
[![ML implementation depth: mnsm-ml](https://img.shields.io/badge/ML_depth-mnsm--ml-orange)](https://github.com/qrv0/mnsm-ml)

> The same equation appears in 3D nonlinear Schrödinger fields, baryon acoustic
> oscillations, cymatic pattern formation, gamma-frequency neural entrainment,
> megalithic stone-chamber resonance, cosmological expansion, the broadband
> phenomenology documented by the critical-brain literature, coupled phase
> oscillators (Kuramoto with memory), B-cell affinity maturation in adaptive
> immunity, the variational dynamics of Friston's free-energy principle, active
> matter with alignment memory, self-organized criticality, cardiac dynamics,
> gene-regulation and circadian rhythms, multi-species ecosystem dynamics,
> non-Markovian open quantum systems via pseudomode embedding, generalized
> Maxwell viscoelasticity, warm-inflation cosmology, Hawkes self-exciting
> processes, and earthquake-cycle dynamics. The ML substrate (structured state
> space models and mechanistic interpretability of attention-based systems) is
> developed in implementation depth at [`mnsm-ml`](https://github.com/qrv0/mnsm-ml).
> Derived from three observational axioms about persistence, not assembled
> from prior literature.

---

The work is structured as an active research program tracking the equation's appearance across substrates. The active frontier is documented in [`RESEARCH-AGENDA.md`](RESEARCH-AGENDA.md) (six/twelve/twenty-four-month horizons) and [`open-problems/`](open-problems/) (eight catalogued open questions). The ML implementation depth (PyTorch Memory-NLS layer, 70M-parameter optimization-collapse empirical finding, mechanistic-interpretability interface) is developed in the [`mnsm-ml`](https://github.com/qrv0/mnsm-ml) spinoff repository; the two repositories advance in parallel.

---

> This is not a typical machine-learning repository. The structure of the repository itself reflects the structure of the equation: oscillating across registers (math, code, prose, visual), self-referential (it explains its own organization), coupled across disciplines (physics, machine learning, neuroscience, cosmology, philosophy of science). See [`STRUCTURE.md`](STRUCTURE.md) for why the repo is shaped this way.

## How to read this work, methodological position

Two principles govern how this repository asks to be read. They are documented in [`methodology/`](methodology/) and worth surfacing here:

**1. Isolation is temporary; coupling is the default.**
The third structural axiom of the equation (P3) asserts that perfect dynamical isolation does not occur, every persistent system is coupled to its environment, and isolation is a methodological tool rather than a property of the world. The repository takes this seriously: cross-domain interfaces are first-class content (not appendix), reader-paths thread through multiple disciplines, and the work invites coupling with whoever engages it. See [`principles/03-coupling.md`](principles/03-coupling.md).

**2. Strict falsificationism is in tension with the content of P3.**
A theory whose third axiom denies isolation cannot consistently be evaluated by an experimental methodology that presupposes the isolability of variables. The work is evaluated by the **six structural-realist criteria** in [`methodology/04-the-six-criteria.md`](methodology/04-the-six-criteria.md): internal mathematical consistency, reproducibility, generative scope, cross-domain coherence, parsimony, and comprehensiveness. The argument for why strict falsificationism is the wrong lens here is in [`methodology/02-limits-of-falsification.md`](methodology/02-limits-of-falsification.md). Specific quantitative predictions are evaluated by coupled-regime numerical reproduction under criterion 2 and criterion 4; the global structural claim is evaluated by all six criteria together.

If you arrive at this work expecting a single-quantity numerical falsification test as the validation criterion, the methodology folder explains why this work answers a different question.

---

## Pick your entry point

The same content is approachable from several backgrounds. Pick whichever you have:

- → **I'm new to all this**, [`paths/if-you-are-new.md`](paths/if-you-are-new.md)
- → **I'm from physics**, [`paths/if-you-are-from-physics.md`](paths/if-you-are-from-physics.md)
- → **I'm from machine learning**, [`paths/if-you-are-from-ml.md`](paths/if-you-are-from-ml.md)
- → **I'm from neuroscience**, [`paths/if-you-are-from-neuroscience.md`](paths/if-you-are-from-neuroscience.md)
- → **I'm from philosophy of science**, [`paths/if-you-are-from-philosophy.md`](paths/if-you-are-from-philosophy.md)

Each path links into the same body of content from a different angle. You can switch paths mid-journey.

---

## Just watch it happen

If you want to see the equation in action without reading anything first:

- [`playground/01-just-watch.ipynb`](playground/01-just-watch.ipynb), Press play, watch a Gaussian state spontaneously crystallize into a body-centered cubic pattern.
- [`playground/02-adjust-the-knobs.ipynb`](playground/02-adjust-the-knobs.ipynb), Tune parameters, see what changes.
- [`playground/03-build-your-own.ipynb`](playground/03-build-your-own.ipynb), Guided implementation from scratch.

---

## The equation

$$
i\hbar\, \partial_t \Psi = \left[\,-\frac{\hbar^2}{2m} D^2 + V_{\text{ext}} + \Lambda |\Psi|^2 + V_{\text{mem}} + \alpha (-\Delta)^{\sigma/2} - i\Gamma\,\right]\Psi + \eta
$$

with $V_{\text{mem}} = \sum_j \lambda_j y_j$ and $\partial_t y_j = \nu_j (\rho - y_j)$, and $\eta$ satisfying the fluctuation–dissipation correlator.

Full derivation from the three principles: [`equation/01-derivation.md`](equation/01-derivation.md).

---

## See it happen

The same form, two substrates, same dynamics:

![3D field anti-collapse](assets/anti_collapse_hero.gif)

*Without memory, the field collapses to a lattice-clipped state. With memory,
the field stays bounded throughout the transient. Same equation, same initial
condition, one ingredient (multi-timescale memory), qualitatively different
trajectory shape. The visualization is from the pre-2026-05-17 isolated-regime
canonical; under the current coupled-regime canonical ($\gamma_0 = 0.2$, $T = 10^{-4}$,
FDT correlator active) the transient-peak signature persists; see
[`results/04-anti-collapse-3d.md`](results/04-anti-collapse-3d.md) for the
updated table.*

The same anti-collapse mechanism operates in the optimization landscape of a 70M-parameter neural network, documented in implementation depth in the [`mnsm-ml`](https://github.com/qrv0/mnsm-ml) spinoff: Memory-NLS descends monotonically to a stable plateau, while a matched-shape Transformer without the structural mechanism crashes catastrophically partway through training and never fully recovers. The structural form is operative across substrates as different as 3D field dynamics and neural network optimization; the field-substrate evidence is here in `results/04`, the ML-substrate evidence is in `mnsm-ml/results/01`.

---

## What's in here

| Folder | Content |
|---|---|
| [`principles/`](principles/) | The three structural axioms (P1, P2, P3) |
| [`equation/`](equation/) | Formal derivation, Markovian embedding, 2D and 3D forms, reductions to known equations |
| [`results/`](results/) | Numerical findings: anti-collapse, crystallization, Bravais selection, vibration spectrum, dimensional rescaling |
| [`interfaces/`](interfaces/) | Cross-domain mappings (20 substrates in this repo + 2 in the [`mnsm-ml`](https://github.com/qrv0/mnsm-ml) spinoff): NLS instances, BAO cosmology, cymatics, gamma neural entrainment, archaeoacoustic resonance, cosmological expansion, critical brain, Kuramoto synchronization, immune affinity maturation, Friston FEP / active inference, active matter, self-organized criticality, cardiac dynamics, gene-regulation / circadian, ecosystem dynamics, pseudomode quantum, generalized Maxwell viscoelasticity, warm-inflation Langevin, Hawkes processes, earthquake-cycle dynamics. The state space model equivalence and mechanistic-interpretability convergent prediction live in [`mnsm-ml/interfaces/`](https://github.com/qrv0/mnsm-ml). |
| [`methodology/`](methodology/) | Structural-realist position, limits of falsification, the six criteria |
| [`paths/`](paths/) | Reader-background-specific entry routes |
| [`playground/`](playground/) | Interactive notebooks (Colab-runnable) |
| [`implementation/`](implementation/) | Physics solver (CuPy). The ML implementation (PyTorch Memory-NLS sequence layer) lives in the [`mnsm-ml`](https://github.com/qrv0/mnsm-ml) spinoff. |
| [`experiments/`](experiments/) | Scripts that reproduce paper figures |
| [`paper/`](paper/) | The full manuscript |
| [`tests/`](tests/) | Conservation, FDT, anti-collapse sanity tests |
| [`assets/`](assets/) | Visual assets referenced in documentation (GIFs, plots) |
| [`open-problems/`](open-problems/) | Catalogue of open research problems with uniform template (precise statement, what is known, what is missing, what would constitute progress) |
| [`RESEARCH-AGENDA.md`](RESEARCH-AGENDA.md) | 6/12/24-month research horizons; convergent programs; how to contribute |

---

## Headline numerical results

**Anti-collapse separation** (3D supercritical NLS, $\sigma_0 = 0.5$, $\Sigma\lambda = 4.0$, P3-coupled: $\gamma_0 = 0.2$, $T = 10^{-4}$, FDT correlator active):

| $\Lambda$ | Transient peak (no memory) | Transient peak (with memory) | Ratio |
|---|---|---|---|
| $-8$ | 60.9 | 4.38 | **13.9×** |
| $-10$ | 58.6 | 5.01 | **11.7×** |
| $-12$ | 45.8 | 43.1 | 1.06× (mechanism saturates at canonical $\Sigma\lambda$) |

Under P3-coupled regime, both arms equilibrate to the FDT thermal floor at long times; the structural signature is in the transient peak (max during integration), which carries the trajectory-shape difference between collapsing and bounded paths. This is the cross-substrate-coherent observable: it is the same observable that carries the optimization-trajectory finding in [`results/08-optimization-collapse-empirical.md`](results/08-optimization-collapse-empirical.md). The mechanism saturates at $\Lambda = -12$ where canonical $\Sigma\lambda = 4$ sits at the dimensional-rescaling threshold $\Sigma\lambda \sim |\Lambda|/d$; higher $\Sigma\lambda$ recovers the separation. The pre-2026-05-17 canonical at $\gamma_0 = 0$, $T = 0$ reported final-peak separation $\sim 10^5$; that configuration violated Rule A (no isolation) and was updated per the audit in [`docs/llm-hedge-annotations.md`](docs/llm-hedge-annotations.md).

**Spontaneous symmetry selection** (3D, $\Lambda = -8$, $\Sigma\lambda = 1.5$): the released crystalline state consistently selects **body-centered cubic (BCC)** symmetry, score $\sim 0.44$ with gap $+0.13$ over the next-best Bravais option.

**Dimensional rescaling** of memory coupling required to release supercritical collapse:

- 2D L²-critical NLS: $\Sigma\lambda \sim |\Lambda|/20$
- 3D L²-supercritical NLS: $\Sigma\lambda \sim |\Lambda|/2$

Derivable from the geometry of the collapse focal region. See [`results/06-dimensional-rescaling.md`](results/06-dimensional-rescaling.md).

**ML-substrate instance (cross-substrate criterion-4 evidence)**: the same anti-collapse mechanism prevents catastrophic optimization failure at the scale of a 70M-parameter neural network training trajectory. Documented in implementation depth in [`mnsm-ml`](https://github.com/qrv0/mnsm-ml): Memory-NLS exhibits monotonic plateau under sustained training; matched-shape Transformer crashes catastrophically at step 28,000 and recovers only partially. The trajectory-shape signature is the same in the 3D field substrate and the neural-network substrate, which is what structural realism predicts when the form is invariant across substrates.

---

## ML implementation depth: `mnsm-ml`

The state space model equivalence (the auxiliary-field update $\partial_t y_j = \nu_j(\rho - y_j)$ is mathematically identical to the diagonal SSM update used by S4, Mamba, and RWKV), the mechanistic-interpretability convergent prediction (the absence of P2's auxiliary-field memory in attention-only architectures forces the superposition phenomenology the Anthropic mech interp program documents), and the 70M-parameter empirical instance of the optimization-collapse mechanism are documented in implementation depth in the [`mnsm-ml`](https://github.com/qrv0/mnsm-ml) spinoff repository. That repo contains the PyTorch Memory-NLS sequence layer, the matched Transformer baseline used for structural differentiation (per Rule 7a of `CLAUDE.md`), the training infrastructure, the FDT-locked-noise and SimSiam follow-ups, and the pre-trained 70M checkpoints on HuggingFace.

The two repositories advance in parallel. This repo holds the structural argument and the cross-substrate interfaces minus the ML substrate; `mnsm-ml` holds the ML substrate in depth.

## Reproduce the paper

```bash
git clone https://github.com/qrv0/mnsm
cd mnsm
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pip install cupy-cuda12x   # or cupy-cuda11x for older CUDA

# Validate the solver (~30 seconds on RTX 4060)
python -m tests.test_conservation

# Reproduce the headline 3D anti-collapse result (~2 minutes)
python experiments/physics/reproduce_3d_anti_collapse.py

# Reproduce all paper figures (~10 minutes total)
python experiments/physics/reproduce_all.py
```

All results use fixed random seeds and reproduce bit-for-bit on identical hardware (NVIDIA RTX 4060 Laptop GPU, Arch Linux, CUDA 12.x).

---

## Citation

```bibtex
@misc{mnsm,
  title  = {Memory-Nonlinear State Models: A Memory-Augmented Nonlinear Schr\"odinger Field Equation with State Space Model Correspondence},
  author = {qrv0},
  year   = {2026},
  url    = {https://github.com/qrv0/mnsm},
  note   = {Three structural principles, one equation, seventeen cross-domain instantiations.}
}
```

The full paper is in [`paper/manuscript.md`](paper/manuscript.md).

---

## License

Code: see [`LICENSE`](LICENSE).
Documentation and paper: see [`LICENSE-docs`](LICENSE-docs).

---

## Current state and open frontiers

The work is structured as an active research program rather than a finished artifact. Three layers, with different stability characteristics.

**Stable load-bearing content** (mathematical core, methodology, headline results):

- The three structural principles (`principles/`), the equation derivation and Markovian embedding (`equation/`), and the reductions to known equations.
- The methodological frame (`methodology/`): structural realism, the limits of falsification (Rule B), the six structural criteria, the calibration philosophy, the time-as-calibration analysis, the Mori-Zwanzig foundation, the tautology-objection treatment.
- The conservation diagnostics (`tests/`) verified to machine precision.
- The 3D anti-collapse phenomenology under P3-coupled regime, with transient-peak separation of $\sim 14\times$ at $\Lambda = -8$ ([`results/04-anti-collapse-3d.md`](results/04-anti-collapse-3d.md)).
- The cross-substrate empirical instance at the neural-network optimization landscape, documented in implementation depth at [`mnsm-ml`](https://github.com/qrv0/mnsm-ml).
- The twenty cross-domain interfaces in this repo + two more in the ML spinoff, calibration-acknowledged where relevant.

**Active frontier** (current work in progress):

- The recalibration of phase-diagram and vibrational tests to the coupled-regime canonical (per `CLAUDE.md` Rule 10), in progress as of 2026-05-17.
- Sharpening predictions in the recently added interfaces (18 pseudomode quantum, 19 viscoelasticity, 20 warm inflation, 21 Hawkes, 22 earthquake cycle) into testable protocols.
- See [`RESEARCH-AGENDA.md`](RESEARCH-AGENDA.md) for the six/twelve/twenty-four-month horizons.

**Known gaps** (open questions, not yet resolved):

- The eight open problems catalogued in [`open-problems/`](open-problems/) with status `not_yet_tested` or `partial`.
- Analytical derivation of the anti-collapse mechanism beyond the leading-order skeleton in [`open-problems/01`](open-problems/01-analytical-anti-collapse.md).
- The dimensional rescaling formula's behavior beyond $d = 3$ (current evidence in [`results/24-dimensional-rescaling-d6.md`](results/24-dimensional-rescaling-d6.md) suggests the simple $\Sigma\lambda \sim |\Lambda|/d$ does not extend cleanly).
- The renormalization-group analysis ([`open-problems/04`](open-problems/04-continuum-rg.md)) and quantum extension ([`open-problems/05`](open-problems/05-quantum-extension.md)).

Contributions on any frontier are welcomed; the methodological constraints in [`CLAUDE.md`](CLAUDE.md) apply.

> The principle that isolation is temporary applies to this repository as well.
> Issues, pull requests, and external mappings of the structure to further
> domains are explicitly welcomed. See [`CONTRIBUTING.md`](CONTRIBUTING.md).

## A note on AI-assisted contribution

This work was developed with substantial AI-assisted formalization. The
methodological frame the work adopts has direct implications for how AI
assistants engage with the codebase, particularly around avoiding
competitive-benchmark framing, respecting the structural-realist evaluation
criteria, and not dismissing cross-domain interfaces as "speculative." If
you are using an AI assistant (Claude, GPT, etc.) to contribute to this
repository, please read [`CLAUDE.md`](CLAUDE.md) first. It is a set of
operational constraints that ensures the assistance aligns with what this
work is, rather than the default frame an AI assistant trained on standard
ML content would naturally adopt.
