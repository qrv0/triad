"""Hero animation: 3D anti-collapse using the canonical solver from the repo.

Runs the 3D Strang split-step solver with documented parameters:
  Lambda = -8, Sigma_lambda = 4.0 (3D-rescaled), nus = [10, 0.5].
These reproduce the ~10⁵x peak-density separation between unmemoried and
memoried 3D supercritical NLS (see results/04-anti-collapse-3d.md and
06-dimensional-rescaling.md).

Visualization: maximum-intensity projection (MIP) over the z axis, so the
3D collapse appears as a 2D bright concentration. Side-by-side with shared
display scale — the contrast tells the story directly.
"""

from __future__ import annotations

import math
import os
import sys
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Ensure the repo package is importable.
REPO_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(REPO_ROOT))

from implementation.physics import (
    SolverConfig3D, MemoryConfig, run,
)


# ---- Output ----
OUTPUT_DIR = REPO_ROOT / "assets"
OUTPUT_DIR.mkdir(exist_ok=True)
OUTPUT_PATH = OUTPUT_DIR / "anti_collapse_hero.gif"


# ---- Visual settings ----
DISPLAY_VMAX_RHO = 4.0          # rho units for MIP display
DISPLAY_VMAX_DISP = math.sqrt(DISPLAY_VMAX_RHO)


def run_3d(with_memory: bool):
    """Run 3D anti-collapse with canonical parameters, return snapshots."""
    cfg = SolverConfig3D(
        N=96,                         # smaller than 128 for animation speed
        L=20.0,
        dt=0.0025,
        n_steps=4000,
        Lambda=-8.0,
        gamma_0=0.0,
        T=0.0,
        memory=MemoryConfig(
            nus=[10.0, 0.5] if with_memory else [],
            lambdas=[3.0, 1.0] if with_memory else [],   # sum = 4.0
            spatial="local",
        ),
        init_sigma=0.5,
        init_k0=(0.0, 0.0, 0.0),
        sample_every=200,
        snapshot_every=50,            # → 80 snapshots
        precision="fp32",
        seed=42,
    )
    label = "with_memory" if with_memory else "no_memory"
    print(f"  {label}: running…")
    result = run(cfg, observables_fn=None, verbose=False)
    print(f"    wall time: {result['wall_time']:.1f}s, "
          f"{len(result['snapshots'])} snapshots")
    return result['snapshots']


def render_gif(snaps_left, snaps_right, output_path):
    """Render side-by-side MIP animation."""
    n_frames = min(len(snaps_left), len(snaps_right))
    images = []
    cmap = plt.get_cmap("inferno")

    # Compute MIP over z for each snapshot
    def mip(psi):
        rho = (psi.conj() * psi).real
        return rho.max(axis=2)        # max over z

    mips_left = [mip(s[1]) for s in snaps_left[:n_frames]]
    mips_right = [mip(s[1]) for s in snaps_right[:n_frames]]
    times = [snaps_left[i][0] for i in range(n_frames)]

    peaks_left = [m.max() for m in mips_left]
    peaks_right = [m.max() for m in mips_right]

    print(f"  left  MIP peak range: {min(peaks_left):.3f} → {max(peaks_left):.1f}")
    print(f"  right MIP peak range: {min(peaks_right):.3f} → {max(peaks_right):.4f}")

    L = 20.0  # box size

    for i in range(n_frames):
        fig, axes = plt.subplots(1, 2, figsize=(11, 6.2), facecolor="black",
                                  dpi=72, gridspec_kw={"wspace": 0.05})
        ax_l, ax_r = axes

        rho_l_disp = np.sqrt(np.maximum(mips_left[i], 0))
        ax_l.imshow(rho_l_disp.T, cmap=cmap, vmin=0, vmax=DISPLAY_VMAX_DISP,
                    origin="lower", extent=[-L/2, L/2, -L/2, L/2],
                    interpolation="bicubic")
        ax_l.set_title("WITHOUT memory · COLLAPSES",
                       color="#ff6b6b", fontsize=17, pad=12, fontweight="bold")
        ax_l.set_xticks([]); ax_l.set_yticks([])
        for spine in ax_l.spines.values():
            spine.set_edgecolor("#ff6b6b"); spine.set_linewidth(2.5)
        ax_l.text(0.5, -0.08, f"peak = {peaks_left[i]:.1f}",
                  transform=ax_l.transAxes, color="#ff6b6b", ha="center",
                  va="top", fontsize=14, family="monospace")

        rho_r_disp = np.sqrt(np.maximum(mips_right[i], 0))
        ax_r.imshow(rho_r_disp.T, cmap=cmap, vmin=0, vmax=DISPLAY_VMAX_DISP,
                    origin="lower", extent=[-L/2, L/2, -L/2, L/2],
                    interpolation="bicubic")
        ax_r.set_title("WITH memory · RELEASED",
                       color="#5eead4", fontsize=17, pad=12, fontweight="bold")
        ax_r.set_xticks([]); ax_r.set_yticks([])
        for spine in ax_r.spines.values():
            spine.set_edgecolor("#5eead4"); spine.set_linewidth(2.5)
        peak_r_str = (f"{peaks_right[i]:.3f}" if peaks_right[i] < 10
                      else f"{peaks_right[i]:.1f}")
        ax_r.text(0.5, -0.08, f"peak = {peak_r_str}",
                  transform=ax_r.transAxes, color="#5eead4", ha="center",
                  va="top", fontsize=14, family="monospace")

        fig.suptitle("Memory-NLS · 3D supercritical · MIP over z",
                     color="white", fontsize=13, y=0.97)
        fig.text(0.5, 0.025,
                 "Memory accumulates density history → builds repulsive potential → field released",
                 color="#999999", ha="center", fontsize=10, style="italic")

        plt.subplots_adjust(left=0.02, right=0.98, top=0.89, bottom=0.13)

        fig.canvas.draw()
        rgba = np.asarray(fig.canvas.buffer_rgba())
        rgb = rgba[..., :3].copy()
        images.append(Image.fromarray(rgb))
        plt.close(fig)

    images[0].save(
        output_path,
        save_all=True,
        append_images=images[1:],
        duration=85,
        loop=0,
        optimize=True,
    )
    print(f"GIF: {output_path.stat().st_size / 1024:.0f}KB, {len(images)} frames")


def main():
    print("3D anti-collapse animation (canonical solver from repo)")
    print(f"  parameters: Lambda=-8, Sigma_lambda=4.0 (3D-rescaled)")
    print()

    print("Running NO MEMORY case…")
    snaps_no_mem = run_3d(with_memory=False)

    print("Running WITH MEMORY case…")
    snaps_with_mem = run_3d(with_memory=True)

    print("Rendering GIF…")
    render_gif(snaps_no_mem, snaps_with_mem, OUTPUT_PATH)


if __name__ == "__main__":
    main()
