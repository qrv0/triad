# Scripts

Asset generation scripts. These produce the visual content referenced in the
README, results documents, and interface documents. Output files are saved to
[`../assets/`](../assets/).

| Script | Output | What it does |
|---|---|---|
| `generate_hero_animation.py` | `assets/anti_collapse_hero.gif` | Runs the canonical 3D anti-collapse simulation (Λ=−8, Σλ=4.0) using the physics solver, renders side-by-side maximum-intensity projections (without memory / with memory) as an animated GIF. ~15 seconds. |
| `generate_trajectory_plots.py` | `assets/scale_up_val_ppl.png`, `assets/scale_up_trajectories.png` | Reads the scale-up training history JSONs and produces two plots: a single-panel validation perplexity comparison and a four-panel comprehensive trajectory analysis. ~5 seconds. |

## Running the scripts

```bash
# Hero animation (requires CUDA + cupy + cuFFT)
python scripts/generate_hero_animation.py

# Trajectory plots (requires matplotlib + numpy; reads outputs/scale_up/)
python scripts/generate_trajectory_plots.py
```

The hero animation requires the `LD_LIBRARY_PATH` to include the
`nvidia/cufft/lib` directory if cuFFT is installed via pip:

```bash
LD_LIBRARY_PATH="$(python -c 'import nvidia.cufft, os; print(os.path.dirname(nvidia.cufft.__file__))')/lib:$LD_LIBRARY_PATH" \
  python scripts/generate_hero_animation.py
```

The trajectory plot script requires that the scale-up training experiment
([`../experiments/neural/scale_up_dynamics.py`](../experiments/neural/scale_up_dynamics.py))
has been run and that the histories exist at
`../outputs/scale_up/{memnls,xformer}/history.json`.
