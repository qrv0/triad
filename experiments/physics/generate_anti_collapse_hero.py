"""Regenerate assets/anti_collapse_hero.gif under the P3-coupled-regime canonical.

Two 3D anti-collapse trajectories side-by-side, sampled at dense early times
(catching the with-memory transient peak around t=0.23 and the no-memory
collapse peak around t=1.0), rendered as z-midplane slices of |Psi|^2 on a
shared log colormap.

Canonical config per paper Section 6.1 + results/04 + CLAUDE.md Rule 8:
  N=128, L=20, dt=0.0025, n_steps=1200, sigma_init=0.5 normalized,
  Lambda=-8, gamma_0=0.2, T=1e-4, FDT correlator active,
  with-memory arm: two-mode (nu=10, lambda=3.0) + (nu=0.5, lambda=1.0).

Time window t in [0, 3] is where all the structural dynamics happens:
  t=0       both Gaussians (peak 1.44)
  t=0.23    with-memory transient peak (peak ~4.5, then decays)
  t=1.0     no-memory collapse peak (peak ~46, lattice-clipped)
  t=1.5+    no-memory releases; both arms thermalize toward floor 2T

Wall time: approximately 45 seconds on RTX 4060 (2 trajectories x 1200 steps,
plus frame rendering).
"""

from __future__ import annotations
import sys
import time
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
import imageio.v2 as imageio

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from implementation.physics import (
    SolverConfig3D,
    MemoryConfig,
    run,
    make_default_observables,
    is_gpu,
)


ASSETS_DIR = Path(__file__).parent.parent.parent / "assets"
FRAMES_DIR = ASSETS_DIR / "_hero_frames"
FRAMES_DIR.mkdir(parents=True, exist_ok=True)
OUTPUT_GIF = ASSETS_DIR / "anti_collapse_hero.gif"


def run_arm(with_memory: bool, n_steps: int = 1200, snapshot_every: int = 20):
    cfg = SolverConfig3D(
        N=128,
        L=20.0,
        dt=0.0025,
        n_steps=n_steps,
        Lambda=-8.0,
        gamma_0=0.2,
        T=1e-4,
        memory=MemoryConfig(
            nus=[10.0, 0.5] if with_memory else [],
            lambdas=[3.0, 1.0] if with_memory else [],
            spatial="local",
        ),
        init_sigma=0.5,
        init_k0=(0.0, 0.0, 0.0),
        sample_every=snapshot_every,
        snapshot_every=snapshot_every,
        precision="fp32",
        seed=42,
    )
    label = "with-memory" if with_memory else "no-memory"
    print(f"  running {label} arm (n_steps={n_steps}, snapshot_every={snapshot_every})...")
    t0 = time.time()
    result = run(cfg, observables_fn=make_default_observables(cfg.L), verbose=False)
    print(f"    {len(result['snapshots'])} snapshots, wall {time.time() - t0:.1f}s")
    return result


def render_frame(t, psi_no, psi_mem, peak_no, peak_mem, frame_idx):
    fig, axes = plt.subplots(1, 2, figsize=(10, 5.2), facecolor="#0b0b0d")
    z_mid = psi_no.shape[2] // 2
    rho_no = np.abs(psi_no[:, :, z_mid]) ** 2
    rho_mem = np.abs(psi_mem[:, :, z_mid]) ** 2

    norm = LogNorm(vmin=1e-4, vmax=60.0)

    for ax in axes:
        ax.set_facecolor("#0b0b0d")
        ax.set_xticks([])
        ax.set_yticks([])
        for s in ax.spines.values():
            s.set_visible(False)

    axes[0].imshow(rho_no, cmap="inferno", norm=norm, origin="lower", interpolation="bilinear")
    axes[0].set_title(
        f"no memory   max |Ψ|² = {peak_no:.2f}",
        color="#f0f0f0", fontsize=12, pad=10,
    )
    im1 = axes[1].imshow(rho_mem, cmap="inferno", norm=norm, origin="lower", interpolation="bilinear")
    axes[1].set_title(
        f"with memory   max |Ψ|² = {peak_mem:.2f}",
        color="#f0f0f0", fontsize=12, pad=10,
    )

    fig.suptitle(
        f"3D anti-collapse under P3-coupled regime    t = {t:5.2f}    (γ₀ = 0.2,  T = 10⁻⁴,  Λ = -8,  Σλ = 4,  z-midplane slice)",
        color="#f0f0f0", fontsize=11, y=0.98,
    )

    cbar = fig.colorbar(im1, ax=axes, location="right", fraction=0.025, pad=0.02)
    cbar.set_label("|Ψ|² (log scale)", color="#cccccc")
    cbar.ax.yaxis.set_tick_params(color="#cccccc")
    plt.setp(plt.getp(cbar.ax.axes, "yticklabels"), color="#cccccc")

    frame_path = FRAMES_DIR / f"frame_{frame_idx:03d}.png"
    fig.savefig(frame_path, dpi=100, bbox_inches="tight", facecolor=fig.get_facecolor())
    plt.close(fig)
    return frame_path


def select_frame_indices(n_snapshots: int) -> list[int]:
    """Subsample snapshots to ~30 frames with denser coverage of early dynamics
    where the with-memory transient peak (t~0.23) and no-memory collapse peak
    (t~1.0) live. Snapshots come at t = 0.05, 0.10, ..., 3.0 (60 total)."""
    # Dense from t=0.05 to t=1.0 (snapshot indices 0..19), every 2 -> 10 frames
    # Moderate from t=1.05 to t=2.0 (indices 20..39), every 4 -> 5 frames
    # Sparse from t=2.05 to t=3.0 (indices 40..59), every 5 -> 4 frames
    early = list(range(0, min(20, n_snapshots), 2))
    mid = list(range(20, min(40, n_snapshots), 4))
    late = list(range(40, n_snapshots, 5))
    return sorted(set(early + mid + late))


def main():
    print(f"Backend: {'cupy (GPU)' if is_gpu() else 'numpy (CPU)'}")
    print(f"Output: {OUTPUT_GIF}")
    print()

    t_total = time.time()
    res_no = run_arm(with_memory=False)
    res_mem = run_arm(with_memory=True)

    snapshots_no = res_no["snapshots"]
    snapshots_mem = res_mem["snapshots"]
    samples_no = res_no["samples"]
    samples_mem = res_mem["samples"]

    n_snap = min(len(snapshots_no), len(snapshots_mem))
    indices = select_frame_indices(n_snap)
    print(f"\n  selected {len(indices)} frames from {n_snap} snapshots")

    frame_paths = []
    for frame_idx, snap_idx in enumerate(indices):
        t_no, psi_no = snapshots_no[snap_idx]
        _, psi_mem = snapshots_mem[snap_idx]
        peak_no = samples_no[snap_idx]["peak"]
        peak_mem = samples_mem[snap_idx]["peak"]
        path = render_frame(t_no, psi_no, psi_mem, peak_no, peak_mem, frame_idx)
        frame_paths.append(path)
        if (frame_idx + 1) % 5 == 0:
            print(f"    frame {frame_idx + 1}/{len(indices)} (t={t_no:.2f})")

    print(f"\n  assembling gif ({len(frame_paths)} frames + hold)...")
    images = [imageio.imread(p) for p in frame_paths]
    images_with_hold = images + [images[-1]] * 8
    imageio.mimsave(OUTPUT_GIF, images_with_hold, duration=180, loop=0)

    for p in frame_paths:
        p.unlink()
    FRAMES_DIR.rmdir()

    sz = OUTPUT_GIF.stat().st_size
    print(f"\n  wrote {OUTPUT_GIF} ({sz/1024:.1f} KB)")
    print(f"\nTotal wall time: {time.time() - t_total:.1f} s.")


if __name__ == "__main__":
    main()
