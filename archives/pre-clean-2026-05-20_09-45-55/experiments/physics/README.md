# Physics experiments

Scripts that reproduce the numerical findings documented in [`../../results/`](../../results/). Each script is self-contained and uses fixed random seeds; running the same script on the same hardware reproduces bit-for-bit identical outputs.

| Script | Reproduces |
|---|---|
| `reproduce_3d_anti_collapse.py` | [`../../results/04-anti-collapse-3d.md`](../../results/04-anti-collapse-3d.md) |
| `reproduce_3d_bravais_sweep.py` | [`../../results/05-bravais-selection.md`](../../results/05-bravais-selection.md) |
| `reproduce_all.py` | The 3D reproduction scripts in sequence. |

Prediction-test scripts (named `test_<topic>.py`) implement the locally-testable predictions named in [`../../interfaces/`](../../interfaces/) and write to result documents in [`../../results/`](../../results/) with numbering ≥ 09. These tests follow the protocol in [`../PROTOCOLS.md`](../PROTOCOLS.md).

## Running a script

```bash
cd <repository root>
python experiments/physics/reproduce_3d_anti_collapse.py
```

Each script writes its output to `outputs/<experiment_name>/`, which is gitignored. The output includes trajectory `.npz` files, a `summary.json` with the headline numbers, and (optionally) a plot saved as `.png`.

## Hardware

The scripts use the CuPy backend via [`../../implementation/physics/`](../../implementation/physics/). They run on:

- NVIDIA GPUs with CUDA 11 or CUDA 12.
- CPU fallback (NumPy) for sanity-checking and the playground notebooks, but the production runs require GPU.

Wall times on the reference RTX 4060 hardware are documented in each script's docstring.

## Customization

Each script exposes its configuration at the top of the file. To explore alternative parameters, copy the script and modify the configuration. The validation suite in [`../../tests/`](../../tests/) ensures that the solver itself is sound; user-introduced parameter choices are the user's responsibility.

## Roadmap

Future directions (not yet implemented as reproduce scripts):

- Mesh-convergence sweeps: $N = 192$, $N = 256$, where compute permits.
- Spatial-kernel variations in 3D.
- 2D reproduction scripts (the 2D results in [`../../results/01-anti-collapse-2d.md`](../../results/01-anti-collapse-2d.md), [`02-spontaneous-crystallization.md`](../../results/02-spontaneous-crystallization.md), [`03-vibrational-modes.md`](../../results/03-vibrational-modes.md), [`07-temporal-spatial-asymmetry.md`](../../results/07-temporal-spatial-asymmetry.md) were produced from earlier versions of the solver; ports to the current `solver_3d.py` framework run-as-2D have not been finalized).
- Dense phase diagram in $(\Lambda, \Sigma\lambda)$.

These extensions are noted as open directions in [`../../paper/manuscript.md`](../../paper/manuscript.md), §10.
