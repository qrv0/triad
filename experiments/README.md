# Experiments

This folder contains the scripts that reproduce the numerical findings of the work.

| Subfolder | Content |
|---|---|
| [`physics/`](physics/) | Scripts that reproduce the field-theory results documented in [`../results/`](../results/). |

ML-substrate experiments (Memory-NLS neural sequence layer training, optimization-collapse comparisons) live in the [`mnsm-ml`](https://github.com/qrv0/mnsm-ml) spinoff repository.

## Reproduction guarantee

All physics scripts in [`physics/`](physics/) reproduce the results documented in [`../results/`](../results/) bit-for-bit under fixed random seeds and identical hardware (NVIDIA RTX 4060 Laptop GPU, Arch Linux, CUDA 12.x). On different hardware the floating-point rounding may differ at the last few digits, but the qualitative results (orders-of-magnitude separations, Bravais selection, frequency ratios, scaling relations) are preserved.

## Total wall time

Running all physics scripts in sequence takes approximately 15 minutes on the reference RTX 4060 hardware. Individual experiments take from 30 seconds to 5 minutes each.

## Running from a fresh clone

```bash
git clone <this repo>
cd mnsm
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install cupy-cuda12x   # or cupy-cuda11x for older CUDA installs

# Validate the solver:
pytest tests/

# Reproduce a single result:
python experiments/physics/reproduce_3d_anti_collapse.py

# Reproduce everything:
python experiments/physics/reproduce_all.py
```

Output files (trajectories, summary JSONs, optional plots) are written to a local `outputs/` directory that is gitignored.
