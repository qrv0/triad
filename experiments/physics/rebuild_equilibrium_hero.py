"""Generate a richer Triad equilibrium hero visual.

This version is meant for the public README/landing page. It uses the balanced
3D solver and renders each run through a maximum-intensity projection plus a
central slice, with time-series metrics for peak concentration and effective
spatial support.

Outputs:
    assets/triad_equilibrium_hero.gif
    assets/triad_equilibrium_hero.mp4  (if ffmpeg is available)
    assets/triad_equilibrium_hero.png
    results/triad-equilibrium-hero-summary.json
"""

from __future__ import annotations

import argparse
import json
import shutil
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation, PillowWriter

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from implementation.physics.balanced_solver_3d import BalancedSolverConfig3D, step
from implementation.physics.balanced_solver_3d import (
    build_external_potential,
    build_initial_state,
    build_kinetic_dissipative_propagator,
    default_observables,
)
from implementation.physics.kernels import MemoryConfig, build_spatial_kernel_fft_3d
from implementation.physics.precision import Precision, get_backend, is_gpu, to_cpu, vram_estimate


def config(kind: str, args) -> BalancedSolverConfig3D:
    if kind == "memory":
        memory = MemoryConfig(nus=[10.0, 0.5], lambdas=[3.0, 1.0], spatial="local")
    else:
        memory = MemoryConfig(nus=[], lambdas=[])

    return BalancedSolverConfig3D(
        N=args.N,
        L=20.0,
        dt=0.0025,
        n_steps=args.steps,
        Lambda=args.Lambda,
        gamma_0=0.0,
        T=0.0,
        memory=memory,
        init_sigma=args.sigma,
        init_k0=(0.0, 0.0, 0.0),
        precision="fp32",
        seed=42,
        sample_every=args.sample_every,
        frame_every=args.frame_every,
        noise_dx_scaling=False,
    )


def run_capture(kind: str, args):
    cfg = config(kind, args)
    xp = get_backend()
    prec = Precision(cfg.precision)
    rng = xp.random.default_rng(cfg.seed)

    psi = build_initial_state(cfg, xp, prec)
    ys = [xp.zeros_like(psi.real).astype(prec.real) for _ in range(cfg.memory.n_modes)]
    U_k = build_kinetic_dissipative_propagator(cfg, xp, prec)
    V_ext = build_external_potential(cfg, xp, prec)
    G_k = None
    if cfg.memory.spatial != "local":
        G_k = build_spatial_kernel_fft_3d(cfg.N, cfg.L, cfg.memory.spatial, cfg.memory.scale, xp=xp, dtype=prec.real)

    observe = default_observables(cfg)
    samples = []
    frames = []
    t = 0.0

    print(f"\n=== {kind} N={cfg.N} steps={cfg.n_steps} ===")
    for i in range(cfg.n_steps + 1):
        if i % cfg.sample_every == 0:
            s = observe(psi, ys, t, i, xp)
            samples.append(s)
            if i % max(cfg.sample_every * 20, 1) == 0:
                print(f"step {i:5d}/{cfg.n_steps} t={t:6.3f} peak={s['peak']:.5g} support={s['participation']:.1f}")

        if i % cfg.frame_every == 0:
            rho = (psi.conj() * psi).real
            mid = cfg.N // 2
            mip_xy = to_cpu(xp.max(rho, axis=2))
            mip_xz = to_cpu(xp.max(rho, axis=1))
            slice_xy = to_cpu(rho[:, :, mid])
            frames.append({"mip_xy": mip_xy, "mip_xz": mip_xz, "slice_xy": slice_xy})

        if i == cfg.n_steps:
            break
        psi, ys, t = step(psi, ys, U_k, V_ext, G_k, cfg, t, xp, prec, rng)

    return {"config": cfg, "samples": samples, "frames": frames}


def robust_vmax(*runs):
    vals = []
    for run in runs:
        for f in run["frames"]:
            vals.append(f["mip_xy"].ravel())
            vals.append(f["slice_xy"].ravel())
    merged = np.concatenate(vals)
    return float(max(np.percentile(merged, 99.85), 1e-12))


def summarize(run):
    peaks = np.array([s["peak"] for s in run["samples"]], dtype=float)
    support = np.array([s["participation"] for s in run["samples"]], dtype=float)
    tail = peaks[-max(3, len(peaks) // 5):]
    return {
        "max_peak": float(peaks.max()),
        "final_peak": float(peaks[-1]),
        "final_over_max": float(peaks[-1] / max(peaks.max(), 1e-30)),
        "final_effective_support": float(support[-1]),
        "tail_peak_relative_std": float(tail.std() / max(tail.mean(), 1e-30)),
    }


def render(nomem, memory, args):
    out_gif = ROOT / "assets" / "triad_equilibrium_hero.gif"
    out_mp4 = ROOT / "assets" / "triad_equilibrium_hero.mp4"
    out_png = ROOT / "assets" / "triad_equilibrium_hero.png"
    out_json = ROOT / "results" / "triad-equilibrium-hero-summary.json"
    out_gif.parent.mkdir(parents=True, exist_ok=True)
    out_json.parent.mkdir(parents=True, exist_ok=True)

    n = min(len(nomem["frames"]), len(memory["frames"]))
    vmax = robust_vmax(nomem, memory)
    norm = plt.Normalize(vmin=0.0, vmax=vmax)

    fig = plt.figure(figsize=(18, 10.5), facecolor="#050604")
    gs = fig.add_gridspec(3, 4, height_ratios=[0.48, 3.15, 1.65], hspace=0.34, wspace=0.18)
    title_ax = fig.add_subplot(gs[0, :])
    title_ax.axis("off")
    title_ax.text(
        0.5,
        0.62,
        "Triad Equilibrium",
        ha="center",
        va="center",
        color="#f8f4df",
        fontsize=28,
        fontweight="bold",
    )
    title_ax.text(
        0.5,
        0.12,
        "same initial field + same attractive nonlinearity -> hierarchical memory converts collapse into bounded distributed persistence",
        ha="center",
        va="center",
        color="#cfc8ad",
        fontsize=13,
    )

    axes = [fig.add_subplot(gs[1, i]) for i in range(4)]
    ax_peak = fig.add_subplot(gs[2, :2])
    ax_support = fig.add_subplot(gs[2, 2:])
    for ax in axes + [ax_peak, ax_support]:
        ax.set_facecolor("#050604")

    images = [
        axes[0].imshow(nomem["frames"][0]["mip_xy"].T, origin="lower", cmap="inferno", norm=norm),
        axes[1].imshow(nomem["frames"][0]["slice_xy"].T, origin="lower", cmap="inferno", norm=norm),
        axes[2].imshow(memory["frames"][0]["mip_xy"].T, origin="lower", cmap="viridis", norm=norm),
        axes[3].imshow(memory["frames"][0]["slice_xy"].T, origin="lower", cmap="viridis", norm=norm),
    ]
    labels = ["No memory / projection", "No memory / center slice", "Memory / projection", "Memory / center slice"]
    colors = ["#ffb000", "#ffb000", "#64ffda", "#64ffda"]
    for ax, label, color in zip(axes, labels, colors):
        ax.set_title(label, color=color, fontsize=12, fontweight="bold")
        ax.set_xticks([])
        ax.set_yticks([])
        for spine in ax.spines.values():
            spine.set_color(color)
            spine.set_linewidth(1.2)

    ts_n = np.array([s["t"] for s in nomem["samples"]])
    pk_n = np.array([s["peak"] for s in nomem["samples"]])
    sp_n = np.array([s["participation"] for s in nomem["samples"]])
    ts_m = np.array([s["t"] for s in memory["samples"]])
    pk_m = np.array([s["peak"] for s in memory["samples"]])
    sp_m = np.array([s["participation"] for s in memory["samples"]])

    ax_peak.plot(ts_n, pk_n, color="#ffb000", lw=2, label="no memory")
    ax_peak.plot(ts_m, pk_m, color="#64ffda", lw=2, label="hierarchical memory")
    ax_peak.set_yscale("log")
    ax_peak.set_title("Collapse pressure: peak density", color="#f8f4df", fontsize=12)
    ax_peak.set_xlabel("time", color="#f8f4df")
    ax_peak.set_ylabel("peak density (log)", color="#f8f4df")

    ax_support.plot(ts_n, sp_n, color="#ffb000", lw=2, label="no memory")
    ax_support.plot(ts_m, sp_m, color="#64ffda", lw=2, label="hierarchical memory")
    ax_support.set_yscale("log")
    ax_support.set_title("Persistence: effective spatial support", color="#f8f4df", fontsize=12)
    ax_support.set_xlabel("time", color="#f8f4df")
    ax_support.set_ylabel("participation ratio (log)", color="#f8f4df")

    markers = [ax_peak.axvline(0, color="#ffffff", alpha=0.35), ax_support.axvline(0, color="#ffffff", alpha=0.35)]
    for ax in [ax_peak, ax_support]:
        ax.grid(color="#ffffff", alpha=0.12)
        ax.tick_params(colors="#f8f4df")
        ax.legend(facecolor="#11110d", edgecolor="#444", labelcolor="#f8f4df", loc="upper right", framealpha=0.82)

    summary = {
        "experiment": "triad_equilibrium_hero",
        "parameters": vars(args),
        "no_memory": summarize(nomem),
        "hierarchical_memory": summarize(memory),
    }
    summary["final_peak_separation_nomem_over_memory"] = summary["no_memory"]["final_peak"] / max(
        summary["hierarchical_memory"]["final_peak"], 1e-30
    )
    summary["final_support_gain_memory_over_nomem"] = summary["hierarchical_memory"]["final_effective_support"] / max(
        summary["no_memory"]["final_effective_support"], 1e-30
    )

    def frame_time(i):
        return i * args.frame_every * 0.0025

    def update(i):
        f_n = nomem["frames"][i]
        f_m = memory["frames"][i]
        images[0].set_data(f_n["mip_xy"].T)
        images[1].set_data(f_n["slice_xy"].T)
        images[2].set_data(f_m["mip_xy"].T)
        images[3].set_data(f_m["slice_xy"].T)
        t = frame_time(i)
        for marker in markers:
            marker.set_xdata([t, t])
        return images + markers

    anim = FuncAnimation(fig, update, frames=n, interval=1000 / args.fps, blit=False)
    fig.subplots_adjust(left=0.055, right=0.985, bottom=0.075, top=0.94)
    anim.save(out_gif, writer=PillowWriter(fps=args.fps), dpi=105)
    if shutil.which("ffmpeg"):
        anim.save(out_mp4, writer="ffmpeg", fps=args.fps, dpi=145, bitrate=4200)
    update(n - 1)
    fig.savefig(out_png, dpi=190, facecolor=fig.get_facecolor(), bbox_inches="tight", pad_inches=0.18)
    plt.close(fig)

    out_json.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(json.dumps(summary, indent=2))
    print("\nWrote:")
    print(f"  {out_gif}")
    if out_mp4.exists():
        print(f"  {out_mp4}")
    print(f"  {out_png}")
    print(f"  {out_json}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--N", type=int, default=128)
    parser.add_argument("--steps", type=int, default=2400)
    parser.add_argument("--Lambda", type=float, default=-10.0)
    parser.add_argument("--sigma", type=float, default=0.5)
    parser.add_argument("--sample-every", type=int, default=10)
    parser.add_argument("--frame-every", type=int, default=20)
    parser.add_argument("--fps", type=int, default=18)
    args = parser.parse_args()

    xp = get_backend()
    print(f"Backend: {xp.__name__} ({'GPU/CUDA' if is_gpu() else 'CPU'})")
    print("VRAM estimate:", vram_estimate(args.N, n_aux=2, precision="fp32"))

    nomem = run_capture("nomem", args)
    memory = run_capture("memory", args)
    render(nomem, memory, args)


if __name__ == "__main__":
    main()
