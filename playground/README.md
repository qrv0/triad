# Playground

This folder contains interactive notebooks that let you engage with the equation visually and computationally without first reading the paper or the technical documents. The notebooks are ordered by depth of engagement.

| Notebook | What you do |
|---|---|
| [`01-just-watch.ipynb`](01-just-watch.ipynb) | Press play. Watch the equation produce a body-centered cubic crystal from a featureless Gaussian initial state. No code edits required. |
| [`02-adjust-the-knobs.ipynb`](02-adjust-the-knobs.ipynb) | Interactive sliders for the nonlinear coupling Λ, the memory coupling Σλ, the initial Gaussian width σ₀. See how the late-time behavior depends on each. |
| [`03-build-your-own.ipynb`](03-build-your-own.ipynb) | Step-by-step guided implementation of the solver from scratch, in plain numpy with explanations. Slower but produces understanding rather than just observation. |

## How to run them

All three notebooks are Colab-compatible. You can open each in Google Colab without installing anything locally; Colab provides free GPU access sufficient for the runs in `01` and `02`. The third notebook runs on CPU and is intended for pedagogical reading rather than fast computation.

To run locally:

```bash
pip install -r ../requirements.txt
pip install jupyterlab cupy-cuda12x   # or cupy-cuda11x for CUDA 11
jupyter lab
```

Open the notebooks from the Jupyter file browser.

## What you can learn from each

**`01-just-watch.ipynb`** is the fastest path from zero context to a visual demonstration of what the equation does. The notebook displays the time evolution of the field's density, the appearance of the crystalline pattern, and the Bravais lattice score for the final configuration. The runtime on a free Colab GPU is a few minutes; on a local RTX-class GPU, under a minute.

**`02-adjust-the-knobs.ipynb`** lets you explore the parameter space interactively. The most useful exercises:

- Set memory coupling Σλ = 0 (no memory) and watch the field collapse at Λ ≤ -8.
- Set Σλ = 4 (3D-rescaled coupling) and watch the anti-collapse mechanism release the field.
- Set Σλ = 1.5 (crystalline window) and watch the BCC lattice form.
- Vary the initial Gaussian width σ₀ across the collapse threshold and see when the equation enters the supercritical regime.

The notebook is also useful for testing the dimensional rescaling claim: at Σλ ~ |Λ|/2 in 3D, the anti-collapse works; at Σλ ~ |Λ|/20 (the 2D value), it fails.

**`03-build-your-own.ipynb`** walks through the Strang split-step algorithm explicitly. Each cell explains one step (V/2 phase rotation, kinetic FFT, V/2 again with updated density, OU update of auxiliary fields, optional FDT noise increment) with the mathematics shown and the code written in readable form. The performance is slow because the notebook prioritizes clarity over efficiency, but the conceptual content is what the notebook is for.

## What these notebooks do not do

They do not run the full-resolution physics experiments from the paper. Those require the scripts in [`../experiments/physics/`](../experiments/physics/) and substantial GPU time. The notebooks are for engagement, not for reproduction of the paper's headline numerics.

They do not require any background in physics, machine learning, or computational science. The notebooks explain what each cell does in plain English. A reader who does not know what an FFT is can run the notebooks and still see the behavior; a reader who does know what an FFT is can read the code and see exactly what is being done.
