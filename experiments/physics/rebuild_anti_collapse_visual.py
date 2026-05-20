"""Generate an impact-oriented Triad anti-collapse visual.

Runs the balanced 3D solver twice from the same initial state:

1. no memory: attractive nonlinear field collapses;
2. hierarchical memory: the field overshoots and releases.

Outputs:
    assets/anti_collapse_balanced.gif
    assets/anti_collapse_balanced.png
    outputs/anti_collapse_balanced/summary.json
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import PillowWriter

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from implementation.physics.balanced_solver_3d import BalancedSolverConfig3D, run
from implementation.physics.kernels import MemoryConfig
from implementation.physics.precision import get_backend, is_gpu, vram_estimate


def make_cfg(kind: str, args) -> BalancedSolverConfig3D:
    if kind == "memory":
        memory = MemoryConfig(
            # Strong two-timescale memory from the original 3D anti-collapse
            # regime: total Sigma_lambda = 4.0.
            nus=[10.0, 0.5],
            lambdas=[3.0, 1.0],
            spatial="local",
        )
    elif kind == "nomem":
        memory = MemoryConfig(nus=[], lambdas=[])
    else:
        raise ValueError(kind)

    return BalancedSolverConfig3D(
        N=args.N,
        L=args.L,
        dt=args.dt,
        n_steps=args.steps,
        Lambda=args.Lambda,
        gamma_0=args.gamma,
        T=args.temperature,
        memory=memory,
        init_sigma=args.sigma,
        init_k0=(1.0, 0.5, 0.0),
        precision=args.precision,
        seed=args.seed,
        sample_every=args.sample_every,
        frame_every=args.frame_every,
        noise_dx_scaling=False,
    )


def run_case(kind: str, args):
    cfg = make_cfg(kind, args)
    print(f"\n=== {kind} ===")
    result = run(cfg, collect_frames=True, verbose=True)
    return cfg, result


def normalise_frames(frames_a, frames_b):
    # Robust shared scale keeps the collapse visible without letting one clipped
    # pixel erase the memory-side structure.
    all_vals = np.concatenate([np.asarray(f).ravel() for f in frames_a + frames_b])
    vmax = float(np.percentile(all_vals, 99.7))
    return max(vmax, 1e-12)


def render_visual(nomem, mem, out_gif: Path, out_png: Path, args):
    frames_nomem = [np.asarray(f) for f in nomem["frames"]]
    frames_mem = [np.asarray(f) for f in mem["frames"]]
    n_frames = min(len(frames_nomem), len(frames_mem))
    frames_nomem = frames_nomem[:n_frames]
    frames_mem = frames_mem[:n_frames]

    samples_nomem = nomem["samples"]
    samples_mem = mem["samples"]
    vmax = normalise_frames(frames_nomem, frames_mem)

    fig = plt.figure(figsize=(13.5, 7.5), facecolor="#080806")
    grid = fig.add_gridspec(2, 2, height_ratios=[4.0, 1.35], hspace=0.18, wspace=0.08)
    ax_l = fig.add_subplot(grid[0, 0])
    ax_r = fig.add_subplot(grid[0, 1])
    ax_p = fig.add_subplot(grid[1, :])

    for ax in (ax_l, ax_r, ax_p):
        ax.set_facecolor("#080806")

    im_l = ax_l.imshow(frames_nomem[0].T, origin="lower", cmap="inferno", vmin=0, vmax=vmax)
    im_r = ax_r.imshow(frames_mem[0].T, origin="lower", cmap="viridis", vmin=0, vmax=vmax)

    for ax, title, color in [
        (ax_l, "No memory: collapse", "#ffb000"),
        (ax_r, "Hierarchical memory: anti-collapse", "#64ffda"),
    ]:
        ax.set_title(title, color=color, fontsize=16, weight="bold", pad=12)
        ax.set_xticks([])
        ax.set_yticks([])
        for spine in ax.spines.values():
            spine.set_color(color)
            spine.set_linewidth(1.5)

    ts_nomem = np.array([s["t"] for s in samples_nomem])
    peak_nomem = np.array([s["peak"] for s in samples_nomem])
    ts_mem = np.array([s["t"] for s in samples_mem])
    peak_mem = np.array([s["peak"] for s in samples_mem])
    ax_p.plot(ts_nomem, peak_nomem, color="#ffb000", lw=2.3, label="no memory")
    ax_p.plot(ts_mem, peak_mem, color="#64ffda", lw=2.3, label="hierarchical memory")
    ax_p.set_yscale("log")
    ax_p.set_xlabel("time", color="#f5f0df")
    ax_p.set_ylabel("peak density (log); equilibrium = bounded low plateau", color="#f5f0df")
    ax_p.tick_params(colors="#f5f0df")
    ax_p.grid(color="#ffffff", alpha=0.13, linewidth=0.7)
    ax_p.legend(facecolor="#11110d", edgecolor="#444", labelcolor="#f5f0df", loc="upper right")
    marker = ax_p.axvline(0, color="#ffffff", alpha=0.45, lw=1)

    fig.suptitle(
        "Triad Equilibrium: anti-collapse is the path, bounded persistence is the result",
        color="#f5f0df",
        fontsize=18,
        weight="bold",
        y=0.965,
    )

    def frame_time(i):
        step = i * args.frame_every
        return step * args.dt

    def update(i):
        im_l.set_data(frames_nomem[i].T)
        im_r.set_data(frames_mem[i].T)
        marker.set_xdata([frame_time(i), frame_time(i)])
        return im_l, im_r, marker

    out_gif.parent.mkdir(parents=True, exist_ok=True)
    out_png.parent.mkdir(parents=True, exist_ok=True)
    writer = PillowWriter(fps=args.fps)
    anim = None
    from matplotlib.animation import FuncAnimation

    anim = FuncAnimation(fig, update, frames=n_frames, interval=1000 / args.fps, blit=False)
    anim.save(out_gif, writer=writer, dpi=110)
    update(n_frames - 1)
    fig.savefig(out_png, dpi=180, facecolor=fig.get_facecolor(), bbox_inches="tight")
    plt.close(fig)


def write_summary(nomem, mem, out_path: Path, args):
    def summarize(result):
        peaks = [s["peak"] for s in result["samples"]]
        norms = [s["norm"] for s in result["samples"]]
        participation = [s["participation"] for s in result["samples"]]
        tail_n = max(3, len(peaks) // 5)
        tail = peaks[-tail_n:]
        tail_mean = sum(tail) / len(tail)
        tail_rel_std = float(np.std(tail) / max(tail_mean, 1e-30))
        return {
            "max_peak": max(peaks),
            "final_peak": peaks[-1],
            "final_over_max": peaks[-1] / max(max(peaks), 1e-30),
            "tail_peak_mean": tail_mean,
            "tail_peak_relative_std": tail_rel_std,
            "equilibrium_score": 1.0 / (1.0 + tail_rel_std + peaks[-1] / max(participation[-1], 1e-30)),
            "initial_norm": norms[0],
            "final_norm": norms[-1],
            "final_participation": participation[-1],
            "wall_time": result["wall_time"],
            "backend": result["backend"],
        }

    summary = {
        "experiment": "balanced_3d_anti_collapse_visual",
        "parameters": vars(args),
        "no_memory": summarize(nomem),
        "hierarchical_memory": summarize(mem),
    }
    summary["peak_separation_final_nomem_over_mem"] = (
        summary["no_memory"]["final_peak"] / max(summary["hierarchical_memory"]["final_peak"], 1e-30)
    )
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    return summary


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--N", type=int, default=96)
    parser.add_argument("--L", type=float, default=20.0)
    parser.add_argument("--dt", type=float, default=0.0025)
    parser.add_argument("--steps", type=int, default=2400)
    parser.add_argument("--Lambda", type=float, default=-10.0)
    parser.add_argument("--gamma", type=float, default=0.0)
    parser.add_argument("--temperature", type=float, default=0.0)
    parser.add_argument("--sigma", type=float, default=0.5)
    parser.add_argument("--precision", choices=["fp32", "fp64"], default="fp32")
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--sample-every", type=int, default=10)
    parser.add_argument("--frame-every", type=int, default=15)
    parser.add_argument("--fps", type=int, default=18)
    args = parser.parse_args()

    xp = get_backend()
    print(f"Backend: {xp.__name__} ({'GPU/CUDA' if is_gpu() else 'CPU'})")
    print("VRAM estimate:", vram_estimate(args.N, n_aux=4, precision=args.precision))

    _, nomem = run_case("nomem", args)
    _, mem = run_case("memory", args)

    out_gif = ROOT / "assets" / "anti_collapse_balanced.gif"
    out_png = ROOT / "assets" / "anti_collapse_balanced.png"
    out_summary = ROOT / "outputs" / "anti_collapse_balanced" / "summary.json"
    result_summary = ROOT / "results" / "anti-collapse-balanced-summary.json"

    render_visual(nomem, mem, out_gif, out_png, args)
    summary = write_summary(nomem, mem, out_summary, args)
    result_summary.write_text(json.dumps(summary, indent=2), encoding="utf-8")

    print("\nWrote:")
    print(f"  {out_gif}")
    print(f"  {out_png}")
    print(f"  {out_summary}")
    print(f"  {result_summary}")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
