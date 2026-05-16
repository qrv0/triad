# Physics experiments

Scripts that reproduce the numerical findings documented in [`../../results/`](../../results/). Each script is self-contained and uses fixed random seeds; running the same script on the same hardware reproduces bit-for-bit identical outputs.

| Script | Reproduces |
|---|---|
| `reproduce_2d_anti_collapse.py` | [`../../results/01-anti-collapse-2d.md`](../../results/01-anti-collapse-2d.md) |
| `reproduce_2d_crystallization.py` | [`../../results/02-spontaneous-crystallization.md`](../../results/02-spontaneous-crystallization.md) |
| `reproduce_2d_vibration_spectrum.py` | [`../../results/03-vibrational-modes.md`](../../results/03-vibrational-modes.md) |
| `reproduce_3d_anti_collapse.py` | [`../../results/04-anti-collapse-3d.md`](../../results/04-anti-collapse-3d.md) |
| `reproduce_3d_bravais_sweep.py` | [`../../results/05-bravais-selection.md`](../../results/05-bravais-selection.md) |
| `reproduce_dimensional_rescaling.py` | [`../../results/06-dimensional-rescaling.md`](../../results/06-dimensional-rescaling.md) |
| `reproduce_temporal_spatial_asymmetry.py` | [`../../results/07-temporal-spatial-asymmetry.md`](../../results/07-temporal-spatial-asymmetry.md) |
| `reproduce_all.py` | All of the above in sequence. |

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

The current scripts reproduce the results in the paper. Future additions (not yet implemented):

- Mesh-convergence sweeps: $N = 192$, $N = 256$, where compute permits.
- Spatial-kernel variations in 3D (currently only 2D is fully documented).
- Resonance spectrum scan (R2 in the 2D `reach_report.md`, not yet ported to 3D).
- Dense phase diagram in $(\Lambda, \Sigma\lambda)$ (R4 in 2D, not yet ported to 3D).

These extensions are noted as open directions in [`../../paper/manuscript.md`](../../paper/manuscript.md), §10.
