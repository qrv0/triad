<div align="center">

# triad

**One equation. Three principles. Twenty-two substrates.**

*The form of what persists across coupled extended systems — derived from how persistent things behave, not from prior literature.*

[![License: MIT](https://img.shields.io/badge/code-MIT-blue.svg)](LICENSE)
[![License: CC BY 4.0](https://img.shields.io/badge/docs-CC_BY_4.0-lightgrey.svg)](LICENSE-docs)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Paper](https://img.shields.io/badge/paper-manuscript-green)](paper/manuscript.md)
[![ML spinoff: mnsm](https://img.shields.io/badge/ML_spinoff-mnsm-orange)](https://github.com/qrv0/mnsm)

![3D anti-collapse — same equation, same initial condition, with vs. without memory](assets/anti_collapse_hero.gif)

*Left: the field collapses to a lattice-clipped singular state.* &nbsp; · &nbsp; *Right: multi-timescale memory bounds the collapse, releases the field into an extended state.*

</div>

---

## The three principles

<table>
<tr>
<td width="33%" valign="top">

### **P1 · Oscillation**

Every persistent extended entity oscillates.

Complex fields with phase are the natural state objects — static structure is unstable.

</td>
<td width="33%" valign="top">

### **P2 · Self-reference**

To exist is to interact with one's own state.

The present depends on the present (cubic self-interaction) **and** on the past (integral memory).

</td>
<td width="33%" valign="top">

### **P3 · Coupling**

Isolation is temporary.

Persistent structure requires ongoing exchange with the environment — dissipation and noise, FDT-locked.

</td>
</tr>
</table>

→ Full statements: [`principles/`](principles/)

---

## The equation

<div align="center">

$$
i\hbar\, \partial_t \Psi = \left[\,-\frac{\hbar^2}{2m} D^2 + V_{\text{ext}} + \Lambda |\Psi|^2 + V_{\text{mem}} + \alpha (-\Delta)^{\sigma/2} - i\Gamma\,\right]\Psi + \eta
$$

</div>

with the auxiliary-field memory $V_{\text{mem}} = \sum_j \lambda_j y_j$, where $\partial_t y_j = \nu_j(\rho - y_j)$, and noise $\eta$ satisfying the fluctuation-dissipation relation.

<table>
<tr>
<td><b>P1</b> →</td>
<td>$-\frac{\hbar^2}{2m}D^2$, $\alpha(-\Delta)^{\sigma/2}$</td>
<td><i>kinetic (oscillation)</i></td>
</tr>
<tr>
<td><b>P2</b> →</td>
<td>$\Lambda|\Psi|^2$, $V_{\text{mem}}$</td>
<td><i>self-interaction + memory</i></td>
</tr>
<tr>
<td><b>P3</b> →</td>
<td>$-i\Gamma$, $\eta$</td>
<td><i>dissipation + FDT-locked noise</i></td>
</tr>
</table>

→ Derivation: [`equation/01-derivation.md`](equation/01-derivation.md) · Markovian embedding: [`equation/02-markovian-embedding.md`](equation/02-markovian-embedding.md)

---

## Where it appears

Twenty-two substrates documented across this repo and the [`mnsm`](https://github.com/qrv0/mnsm) ML spinoff. Three evidentiary classes:

<details open>
<summary><b>🔷 Mathematical equivalence</b> &nbsp; <i>— no calibration required, same equation</i></summary>

| | Substrate |
|---|---|
| 🌊 | [Other NLS systems](interfaces/01-other-nls-systems.md) (BEC, optical solitons, deep-water waves) |
| 🧠 | [State space models](https://github.com/qrv0/mnsm/blob/main/interfaces/01-state-space-models.md) (S4, Mamba, RWKV in machine learning) |
| 🔄 | [Memory-Kuramoto oscillators](interfaces/10-kuramoto-synchronization.md) |

</details>

<details open>
<summary><b>🔶 Calibration-dependent structural correspondence</b> &nbsp; <i>— same form, substrate-specific units</i></summary>

| | Substrate |
|---|---|
| 🌌 | [Baryon acoustic oscillations](interfaces/02-baryon-acoustic.md) (early-universe cosmology) |
| 🎵 | [Chladni cymatic patterns](interfaces/03-chladni-cymatics.md) |
| 🧬 | [Gamma neural entrainment](interfaces/04-gamma-entrainment.md) (40 Hz, GENUS, Alzheimer's) |
| 🪨 | [Archaeoacoustic resonance](interfaces/05-archaeoacoustic-resonance.md) (megalithic chambers) |
| 🦠 | [B-cell affinity maturation](interfaces/11-immune-affinity-maturation.md) |
| 🐦 | [Active matter](interfaces/13-active-matter.md) (flocks, swarms, active gels) |
| ❤️ | [Cardiac electrophysiology](interfaces/15-cardiac-dynamics.md) |
| 🧪 | [Gene regulation + circadian rhythms](interfaces/16-gene-regulation-circadian.md) |
| ⚛️ | [Non-Markovian open quantum systems](interfaces/18-pseudomode-quantum.md) |
| 🏗️ | [Generalized Maxwell viscoelasticity](interfaces/19-viscoelasticity-prony.md) |
| 🌠 | [Warm-inflation cosmology](interfaces/20-warm-inflation.md) |
| 📊 | [Hawkes self-exciting processes](interfaces/21-hawkes-intensity.md) |
| 🌍 | [Earthquake cycle dynamics](interfaces/22-earthquake-cycle.md) |

</details>

<details open>
<summary><b>🔸 Mechanism-shape and convergent-program correspondence</b> &nbsp; <i>— same trajectory or convergent observation</i></summary>

| | Substrate |
|---|---|
| 🌌 | [Cosmological expansion as anti-collapse release](interfaces/07-cosmological-expansion.md) |
| 🔍 | [Mechanistic interpretability of attention models](https://github.com/qrv0/mnsm/blob/main/interfaces/02-mechanistic-interpretability.md) |
| 🧠 | [Critical-brain dynamics](interfaces/09-critical-brain.md) |
| 🎯 | [Friston free-energy principle + active inference](interfaces/12-friston-free-energy.md) |
| ⛰️ | [Self-organized criticality](interfaces/14-self-organized-criticality.md) |
| 🌳 | [Multi-species ecosystem dynamics](interfaces/17-ecosystem-dynamics.md) |

</details>

→ Full catalog with derivations: [`interfaces/README.md`](interfaces/README.md)

---

## What it does, numerically

<table>
<tr>
<th>Finding</th>
<th>Result</th>
<th>Detail</th>
</tr>
<tr>
<td><b>3D anti-collapse</b></td>
<td>~10⁵ × final-peak separation at $\Lambda = -8$ between unmemoried and memoried runs</td>
<td><a href="results/04-anti-collapse-3d.md"><code>results/04</code></a></td>
</tr>
<tr>
<td><b>Spontaneous BCC selection</b></td>
<td>Body-centered cubic, score 0.44 with +0.13 gap over next-best Bravais option</td>
<td><a href="results/05-bravais-selection.md"><code>results/05</code></a></td>
</tr>
<tr>
<td><b>Dimensional rescaling</b></td>
<td>$\Sigma\lambda_{\text{crit}} \sim |\Lambda|/d$ for $d \in \{2, 3\}$, geometrically derivable</td>
<td><a href="results/06-dimensional-rescaling.md"><code>results/06</code></a></td>
</tr>
<tr>
<td><b>Conservation diagnostics</b></td>
<td>Norm conservation to $10^{-13}$ fp64; FDT equipartition within 0.5%</td>
<td><a href="tests/test_conservation.py"><code>tests/</code></a></td>
</tr>
<tr>
<td><b>Cross-substrate empirical instance</b></td>
<td>Same trajectory-shape signature at 70M neural network parameters (Memory-NLS vs Transformer)</td>
<td><a href="https://github.com/qrv0/mnsm/blob/main/results/01-optimization-collapse-empirical.md"><code>mnsm/results/01</code></a></td>
</tr>
</table>

---

## Read it your way

<table>
<tr>
<td width="20%" align="center"><b>🌱 New here</b><br><a href="paths/if-you-are-new.md">if-you-are-new</a></td>
<td width="20%" align="center"><b>⚛️ Physics</b><br><a href="paths/if-you-are-from-physics.md">if-you-are-from-physics</a></td>
<td width="20%" align="center"><b>🤖 ML</b><br><a href="paths/if-you-are-from-ml.md">if-you-are-from-ml</a></td>
<td width="20%" align="center"><b>🧠 Neuroscience</b><br><a href="paths/if-you-are-from-neuroscience.md">if-you-are-from-neuroscience</a></td>
<td width="20%" align="center"><b>📚 Philosophy</b><br><a href="paths/if-you-are-from-philosophy.md">if-you-are-from-philosophy</a></td>
</tr>
</table>

Each path threads the same content in an order suited to that background. Switching mid-journey is encouraged.

---

## Run it

```bash
git clone https://github.com/qrv0/triad
cd triad
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pip install cupy-cuda12x   # or cupy-cuda11x for older CUDA

# Validate solver (~30 s)
python -m tests.test_conservation

# Reproduce 3D anti-collapse (~4 min on RTX 4060)
python experiments/physics/reproduce_3d_anti_collapse.py
```

Or run in browser without local setup:

- 🎬 [`playground/01-just-watch.ipynb`](playground/01-just-watch.ipynb) — Gaussian → BCC crystal, no code edits
- 🎛️ [`playground/02-adjust-the-knobs.ipynb`](playground/02-adjust-the-knobs.ipynb) — interactive parameter exploration
- 🛠️ [`playground/03-build-your-own.ipynb`](playground/03-build-your-own.ipynb) — guided implementation

All runs use fixed seeds, bit-for-bit reproducible on identical hardware.

---

## Repository map

| | Folder | Content |
|---|---|---|
| 📐 | [`principles/`](principles/) | The three structural axioms (P1, P2, P3) |
| 📜 | [`equation/`](equation/) | Derivation, Markovian embedding, reductions to known equations |
| 📊 | [`results/`](results/) | Anti-collapse, crystallization, Bravais selection, vibrational modes, dimensional rescaling |
| 🌐 | [`interfaces/`](interfaces/) | 20 cross-domain mappings (+ 2 in [`mnsm`](https://github.com/qrv0/mnsm)) |
| 🧭 | [`methodology/`](methodology/) | Structural realism, limits of falsification, six criteria, calibration philosophy |
| 🛤️ | [`paths/`](paths/) | Reader-specific entry routes |
| 🎮 | [`playground/`](playground/) | Interactive Colab notebooks |
| ⚙️ | [`implementation/`](implementation/) | CuPy physics solver |
| 🧪 | [`experiments/`](experiments/) | Reproduction scripts |
| 📄 | [`paper/`](paper/) | Full manuscript |
| ✅ | [`tests/`](tests/) | Conservation diagnostics |
| 🎨 | [`assets/`](assets/) | Visual outputs |
| 🔬 | [`open-problems/`](open-problems/) | Open research questions, uniform template |
| 📅 | [`RESEARCH-AGENDA.md`](RESEARCH-AGENDA.md) | 6/12/24-month horizons |
| 🏛️ | [`STRUCTURE.md`](STRUCTURE.md) | Why the repository is shaped this way |

---

<details>
<summary><b>📖 More on the methodology</b></summary>

The work is evaluated by criteria appropriate to a structural theory, not by single-experiment refutation. Two principles govern the frame:

1. **Coupling is the default, isolation is temporary.** The third structural axiom (P3) asserts that perfect dynamical isolation does not occur. → [`principles/03-coupling.md`](principles/03-coupling.md)

2. **Structural realism, not strict falsificationism.** A theory whose third axiom denies isolation cannot be evaluated by single-experiment refutation that presupposes isolation. The work is evaluated by six structural criteria: internal consistency, reproducibility, generative scope, cross-domain coherence, parsimony, comprehensiveness. → [`methodology/02-limits-of-falsification.md`](methodology/02-limits-of-falsification.md)

Full methodological frame: [`methodology/`](methodology/).

</details>

<details>
<summary><b>🚧 Current state and open frontiers</b></summary>

**Stable load-bearing content:**
- The three principles, the equation derivation, the Markovian embedding, the reductions
- Methodological frame: structural realism, six criteria, calibration philosophy, Mori-Zwanzig foundation
- Conservation diagnostics verified to machine precision
- 3D anti-collapse, BCC selection, dimensional rescaling at $d \in \{2,3\}$
- The cross-substrate empirical instance at 70M neural network parameters in [`mnsm`](https://github.com/qrv0/mnsm)
- 22 cross-domain interfaces, calibration-acknowledged

**Active frontier:**
- Phase-diagram and vibrational test recalibration
- Sharpening predictions in recently added interfaces (18 pseudomode, 19 viscoelasticity, 20 warm inflation, 21 Hawkes, 22 earthquake) into testable protocols
- → [`RESEARCH-AGENDA.md`](RESEARCH-AGENDA.md)

**Known gaps:**
- Eight open problems catalogued in [`open-problems/`](open-problems/) with status `not_yet_tested` or `partial`
- Analytical derivation of anti-collapse beyond leading order
- Dimensional rescaling beyond $d = 3$ (simple $1/d$ does not extend cleanly)
- Renormalization-group analysis and quantum extension

> Coupling is the default. Issues, pull requests, and external mappings of the structure to further substrates are explicitly welcomed. See [`CONTRIBUTING.md`](CONTRIBUTING.md).

</details>

<details>
<summary><b>📚 Citation</b></summary>

```bibtex
@misc{triad,
  title  = {Triad: A Structural Field Equation of Persistent Extended Entities},
  author = {qrv0},
  year   = {2026},
  url    = {https://github.com/qrv0/triad},
  note   = {Three structural principles, one equation, twenty-two cross-substrate documentations across triad and mnsm.}
}
```

Full paper: [`paper/manuscript.md`](paper/manuscript.md) · ML implementation: [`mnsm`](https://github.com/qrv0/mnsm)

</details>

<details>
<summary><b>🤖 On AI-assisted contribution</b></summary>

This work was developed with substantial AI-assisted formalization. The methodological frame has direct implications for how AI assistants should engage with the codebase: avoid competitive-benchmark framing, respect the structural-realist evaluation criteria, do not dismiss cross-domain interfaces as "speculative". Operational constraints in [`CLAUDE.md`](CLAUDE.md) ensure that assistance aligns with what this work is, rather than the default frame an AI assistant trained on standard ML content would naturally adopt.

</details>

---

<div align="center">
<sub>Code: <a href="LICENSE">MIT</a> &nbsp; · &nbsp; Documentation: <a href="LICENSE-docs">CC BY 4.0</a></sub>
</div>
