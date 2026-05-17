# Why this repository is shaped the way it is

The work registers a **structural claim** — that an equation derived from three principles about persistent extended entities recurs across substrates from cosmology to ML to biology — not a tool. The repository shape follows from the claim, not from standard ML / package conventions.

## The four layers

| Layer | What it is for | Folders |
|---|---|---|
| 🧩 **Argument** | What the work claims and why | [`principles/`](principles/) · [`equation/`](equation/) · [`methodology/`](methodology/) · [`paper/`](paper/) |
| 🔬 **Evidence** | What supports the claim | [`interfaces/`](interfaces/) · [`results/`](results/) · [`assets/`](assets/) |
| ⚙️ **Code** | For those who want to run it | [`implementation/`](implementation/) · [`experiments/`](experiments/) · [`tests/`](tests/) |
| 🛤️ **Routing** | Navigation across the layers | [`paths/`](paths/) · [`docs/`](docs/) · this file |

A reader encounters them roughly top-to-bottom: principles select the equation (argument); the equation is shown to recur in 20+ substrates and to produce a small family of numerical phenomena (evidence); the code reproduces all of that (code); the routing layer is for cross-area entry.

## What's not here

This is **not** a Python package, **not** a benchmark project, **not** a wiki of the paper. The repository is a body of work registered as structure. The code runs and the results reproduce — but the artefact is the structural argument, refracted across registers so that a reader from any background can find an entry point.

## Cross-repo

The ML-substrate implementation depth — the PyTorch sequence layer, the matched-architecture baseline, the 70M-parameter optimization-collapse empirical finding — lives in the [`mnsm`](https://github.com/qrv0/mnsm) spinoff, along with two ML-substrate interfaces (state space model equivalence; mechanistic-interpretability convergent prediction). The two repositories advance in parallel; this one holds the structural argument and the non-ML substrates.

A future physics-substrate spinoff (`triad-physics`) is a direction under consideration — the CuPy solver and physics-specific reproductions would naturally migrate to give the structural-claim portal a cleaner cross-area entry, while keeping the cross-domain ledger here.

## A note on self-reference

If you have read this file, you have just been subject to the second of the three principles that organize the work it documents. The work asserts that persistent extended entities are defined by self-reference, both instantaneously and across time, and that this is part of why they hold their shape. This document is the repository being self-referential about its own shape. That is not coincidence — it is the work.
