"""Generate trajectory comparison plots for the scale-up experiment.

Reads outputs/scale_up/{memnls,xformer}/history.json and produces:
  assets/scale_up_trajectories.png   — comprehensive multi-panel comparison
  assets/scale_up_val_ppl.png         — single-panel val_ppl comparison

Plots are designed for inclusion in scale_up_results.md and the README.
"""

from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

REPO_ROOT = Path(__file__).parent.parent
ASSETS_DIR = REPO_ROOT / "assets"
ASSETS_DIR.mkdir(exist_ok=True)

# Load both histories
mem = json.load(open(REPO_ROOT / "outputs" / "scale_up" / "memnls" / "history.json"))
xfm = json.load(open(REPO_ROOT / "outputs" / "scale_up" / "xformer" / "history.json"))

# Color scheme
COLOR_MEM = "#5eead4"   # teal — MemNLS
COLOR_XFM = "#ff6b6b"   # red — Transformer
COLOR_BG = "#0a0a0a"
COLOR_GRID = "#222222"
COLOR_TEXT = "white"
COLOR_DIM = "#888888"


def style_ax(ax):
    ax.set_facecolor("#0f0f0f")
    ax.tick_params(colors=COLOR_TEXT)
    for spine in ax.spines.values():
        spine.set_edgecolor("#444444")
    ax.grid(True, color=COLOR_GRID, linewidth=0.5, alpha=0.7)
    ax.xaxis.label.set_color(COLOR_TEXT)
    ax.yaxis.label.set_color(COLOR_TEXT)


def plot_val_ppl_only():
    """Single-panel val_ppl comparison — the headline plot."""
    fig, ax = plt.subplots(figsize=(11, 6), facecolor=COLOR_BG, dpi=100)

    mem_steps = np.array(mem["val_step"])
    mem_ppl = np.exp(np.array(mem["val_loss"]))
    xfm_steps = np.array(xfm["val_step"])
    xfm_ppl = np.exp(np.array(xfm["val_loss"]))

    ax.plot(mem_steps, mem_ppl, color=COLOR_MEM, linewidth=2.4,
            label="Memory-NLS (with structural anti-collapse)", marker="o",
            markersize=2.5, alpha=0.95)
    ax.plot(xfm_steps, xfm_ppl, color=COLOR_XFM, linewidth=2.4,
            label="Transformer (no structural anti-collapse)", marker="o",
            markersize=2.5, alpha=0.95)

    # Mark MemNLS minimum
    mem_min_idx = int(np.argmin(mem_ppl))
    ax.scatter([mem_steps[mem_min_idx]], [mem_ppl[mem_min_idx]],
               s=140, color=COLOR_MEM, edgecolor="white", linewidth=1.5,
               zorder=10)
    ax.annotate(f"min {mem_ppl[mem_min_idx]:.2f}\n(step {mem_steps[mem_min_idx]})",
                xy=(mem_steps[mem_min_idx], mem_ppl[mem_min_idx]),
                xytext=(mem_steps[mem_min_idx] + 1500, mem_ppl[mem_min_idx] + 0.6),
                color=COLOR_MEM, fontsize=10, family="monospace")

    # Mark Transformer minimum
    xfm_min_idx = int(np.argmin(xfm_ppl))
    ax.scatter([xfm_steps[xfm_min_idx]], [xfm_ppl[xfm_min_idx]],
               s=140, color=COLOR_XFM, edgecolor="white", linewidth=1.5,
               zorder=10)
    ax.annotate(f"min {xfm_ppl[xfm_min_idx]:.2f}\n(step {xfm_steps[xfm_min_idx]})",
                xy=(xfm_steps[xfm_min_idx], xfm_ppl[xfm_min_idx]),
                xytext=(xfm_steps[xfm_min_idx] + 1500, xfm_ppl[xfm_min_idx] - 1.2),
                color=COLOR_XFM, fontsize=10, family="monospace")

    # Mark the crash peak
    crash_idx = int(np.argmax(xfm_ppl))
    ax.scatter([xfm_steps[crash_idx]], [xfm_ppl[crash_idx]],
               s=180, color=COLOR_XFM, edgecolor="yellow", linewidth=2,
               zorder=11, marker="X")
    ax.annotate(f"CRASH\npeak ppl {xfm_ppl[crash_idx]:.1f}\n(step {xfm_steps[crash_idx]})",
                xy=(xfm_steps[crash_idx], xfm_ppl[crash_idx]),
                xytext=(xfm_steps[crash_idx] + 2000, xfm_ppl[crash_idx] - 1.5),
                color="yellow", fontsize=11, family="monospace", fontweight="bold",
                arrowprops=dict(arrowstyle="->", color="yellow", linewidth=1.2))

    # Mark final values
    ax.annotate(f"final {mem_ppl[-1]:.2f}",
                xy=(mem_steps[-1], mem_ppl[-1]),
                xytext=(mem_steps[-1] - 8000, mem_ppl[-1] + 1.5),
                color=COLOR_MEM, fontsize=10, family="monospace",
                arrowprops=dict(arrowstyle="->", color=COLOR_MEM, linewidth=1, alpha=0.5))
    ax.annotate(f"final {xfm_ppl[-1]:.2f}",
                xy=(xfm_steps[-1], xfm_ppl[-1]),
                xytext=(xfm_steps[-1] - 8000, xfm_ppl[-1] + 1.5),
                color=COLOR_XFM, fontsize=10, family="monospace",
                arrowprops=dict(arrowstyle="->", color=COLOR_XFM, linewidth=1, alpha=0.5))

    ax.set_xlabel("training step", fontsize=12)
    ax.set_ylabel("validation perplexity (log scale)", fontsize=12)
    ax.set_yscale("log")
    ax.set_xlim(0, 50000)
    ax.legend(loc="upper right", fontsize=11, facecolor="#222222",
              edgecolor="#444444", labelcolor=COLOR_TEXT)
    ax.set_title("70M parameters · enwik8 · 50,000 steps · same training infrastructure",
                 color=COLOR_TEXT, fontsize=13, pad=12)

    fig.suptitle("Validation perplexity trajectory: structural anti-collapse vs catastrophic failure",
                 color=COLOR_TEXT, fontsize=15, y=0.99, fontweight="bold")

    style_ax(ax)
    plt.tight_layout()
    out = ASSETS_DIR / "scale_up_val_ppl.png"
    plt.savefig(out, facecolor=COLOR_BG, bbox_inches="tight", dpi=120)
    print(f"Saved: {out}")
    plt.close()


def plot_comprehensive():
    """Multi-panel comprehensive comparison."""
    fig = plt.figure(figsize=(13, 10), facecolor=COLOR_BG, dpi=100)
    gs = fig.add_gridspec(3, 2, height_ratios=[1.4, 1, 1], hspace=0.45, wspace=0.22)

    # Top: val_ppl spanning both columns
    ax_top = fig.add_subplot(gs[0, :])

    mem_steps = np.array(mem["val_step"])
    mem_ppl = np.exp(np.array(mem["val_loss"]))
    xfm_steps = np.array(xfm["val_step"])
    xfm_ppl = np.exp(np.array(xfm["val_loss"]))

    ax_top.plot(mem_steps, mem_ppl, color=COLOR_MEM, linewidth=2.2,
                label="Memory-NLS", marker="o", markersize=2.5)
    ax_top.plot(xfm_steps, xfm_ppl, color=COLOR_XFM, linewidth=2.2,
                label="Transformer", marker="o", markersize=2.5)

    # Highlight crash region
    crash_start = 28000
    crash_end = 35000
    ax_top.axvspan(crash_start, crash_end, alpha=0.15, color="#ff6b6b",
                   label=f"crash region")
    ax_top.text((crash_start + crash_end) / 2, ax_top.get_ylim()[1] * 0.7
                if ax_top.get_ylim()[1] > 1 else 25,
                "catastrophic\ncollapse",
                ha="center", color="#ffaa6b", fontsize=10, fontweight="bold",
                family="monospace")

    ax_top.set_xlabel("training step", fontsize=11)
    ax_top.set_ylabel("validation perplexity (log)", fontsize=11)
    ax_top.set_yscale("log")
    ax_top.set_xlim(0, 50000)
    ax_top.legend(loc="upper right", fontsize=10, facecolor="#222222",
                  edgecolor="#444444", labelcolor=COLOR_TEXT)
    ax_top.set_title("Validation perplexity trajectory",
                     color=COLOR_TEXT, fontsize=12, pad=8)
    style_ax(ax_top)

    # Middle-left: MemNLS train + val
    ax_ml = fig.add_subplot(gs[1, 0])
    mem_train_steps = np.array(mem["train_step"])
    mem_train = np.array(mem["train_loss"])
    ax_ml.plot(mem_train_steps, mem_train, color=COLOR_MEM, linewidth=1.5,
               alpha=0.7, label="train")
    ax_ml.plot(mem_steps, np.array(mem["val_loss"]), color=COLOR_MEM,
               linewidth=2.2, label="val")
    ax_ml.fill_between(mem_steps,
                       np.interp(mem_steps, mem_train_steps, mem_train),
                       np.array(mem["val_loss"]),
                       color=COLOR_MEM, alpha=0.18)
    ax_ml.set_xlabel("step", fontsize=10)
    ax_ml.set_ylabel("loss", fontsize=10)
    ax_ml.set_xlim(0, 50000)
    ax_ml.set_title("Memory-NLS · train + val",
                    color=COLOR_MEM, fontsize=11, pad=6, fontweight="bold")
    ax_ml.legend(loc="upper right", fontsize=9, facecolor="#222222",
                 edgecolor="#444444", labelcolor=COLOR_TEXT)
    style_ax(ax_ml)

    # Middle-right: Transformer train + val
    ax_mr = fig.add_subplot(gs[1, 1])
    xfm_train_steps = np.array(xfm["train_step"])
    xfm_train = np.array(xfm["train_loss"])
    ax_mr.plot(xfm_train_steps, xfm_train, color=COLOR_XFM, linewidth=1.5,
               alpha=0.7, label="train")
    ax_mr.plot(xfm_steps, np.array(xfm["val_loss"]), color=COLOR_XFM,
               linewidth=2.2, label="val")
    ax_mr.fill_between(xfm_steps,
                       np.interp(xfm_steps, xfm_train_steps, xfm_train),
                       np.array(xfm["val_loss"]),
                       color=COLOR_XFM, alpha=0.18)
    ax_mr.set_xlabel("step", fontsize=10)
    ax_mr.set_ylabel("loss", fontsize=10)
    ax_mr.set_xlim(0, 50000)
    ax_mr.set_title("Transformer · train + val",
                    color=COLOR_XFM, fontsize=11, pad=6, fontweight="bold")
    ax_mr.legend(loc="upper right", fontsize=9, facecolor="#222222",
                 edgecolor="#444444", labelcolor=COLOR_TEXT)
    style_ax(ax_mr)

    # Bottom-left: train-val gap evolution
    ax_bl = fig.add_subplot(gs[2, 0])
    mem_train_at_val = np.interp(mem_steps, mem_train_steps, mem_train)
    mem_gap = np.array(mem["val_loss"]) - mem_train_at_val
    xfm_train_at_val = np.interp(xfm_steps, xfm_train_steps, xfm_train)
    xfm_gap = np.array(xfm["val_loss"]) - xfm_train_at_val

    ax_bl.plot(mem_steps, mem_gap, color=COLOR_MEM, linewidth=2,
               label="Memory-NLS gap")
    ax_bl.plot(xfm_steps, xfm_gap, color=COLOR_XFM, linewidth=2,
               label="Transformer gap")
    ax_bl.axhline(0, color="#666666", linewidth=0.8, linestyle="--", alpha=0.7)
    ax_bl.set_xlabel("step", fontsize=10)
    ax_bl.set_ylabel("val − train", fontsize=10)
    ax_bl.set_xlim(0, 50000)
    ax_bl.set_title("Generalization gap evolution",
                    color=COLOR_TEXT, fontsize=11, pad=6)
    ax_bl.legend(loc="upper left", fontsize=9, facecolor="#222222",
                 edgecolor="#444444", labelcolor=COLOR_TEXT)
    style_ax(ax_bl)

    # Bottom-right: trajectory derivative — Δval per 500 steps
    ax_br = fig.add_subplot(gs[2, 1])
    mem_dval = np.diff(np.array(mem["val_loss"]))
    xfm_dval = np.diff(np.array(xfm["val_loss"]))

    ax_br.plot(mem_steps[1:], mem_dval, color=COLOR_MEM, linewidth=1.5,
               label="Memory-NLS Δval", alpha=0.85)
    ax_br.plot(xfm_steps[1:], xfm_dval, color=COLOR_XFM, linewidth=1.5,
               label="Transformer Δval", alpha=0.85)
    ax_br.axhline(0, color="#666666", linewidth=0.8, linestyle="--", alpha=0.7)
    ax_br.set_xlabel("step", fontsize=10)
    ax_br.set_ylabel("Δ val_loss / 500 steps", fontsize=10)
    ax_br.set_xlim(0, 50000)
    ax_br.set_title("Trajectory derivative · stability vs instability",
                    color=COLOR_TEXT, fontsize=11, pad=6)
    ax_br.legend(loc="upper right", fontsize=9, facecolor="#222222",
                 edgecolor="#444444", labelcolor=COLOR_TEXT)
    style_ax(ax_br)

    fig.suptitle(
        "Memory-NLS vs Transformer · 70M params · enwik8 · structural difference in optimization dynamics",
        color=COLOR_TEXT, fontsize=14, y=0.995, fontweight="bold")

    out = ASSETS_DIR / "scale_up_trajectories.png"
    plt.savefig(out, facecolor=COLOR_BG, bbox_inches="tight", dpi=120)
    print(f"Saved: {out}")
    plt.close()


if __name__ == "__main__":
    plot_val_ppl_only()
    plot_comprehensive()
    print("\nAll plots saved to assets/")
