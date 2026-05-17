"""Convention x L matrix at d=2, d=3: complete the cross-convention audit.

Per results/30 (convention audit) and results/31 (Convention A vs B at L=20),
the convention and L choices interact: Convention A at L=10 is the implicit
setup of the dimensional-rescaling series (results/06, 10, 15, 24); Convention
B at L=20 is the canonical anti-collapse + phase-diagram setup. The L=20
results in results/31 showed that at fixed L=20, Convention A loses focal-
collapse access at both d=2 and d=3.

This script completes the (convention, L, d) matrix at the 4 cells not yet
documented in this repository's literature:

  (Convention A, L=10, d=2): the original dimensional-rescaling series setup
  (Convention A, L=10, d=3): the original dimensional-rescaling series setup
  (Convention B, L=10, d=2): new
  (Convention B, L=10, d=3): new

For each cell, runs the same 5x4 (Sigma_lambda, gamma_0) grid as the L=20
counterparts in results/26, 27, 31. Single seed per grid point (the convention
+ L effect dominates the seed variance).

Output: outputs/convention_L_matrix/summary.json with all 80 grid points
(4 cells x 20 points).

Wall time estimate: ~12-20 min on RTX 4060.
"""

from __future__ import annotations
import json
import time
from pathlib import Path

import numpy as np

try:
    import cupy as cp
    xp = cp
    USING_GPU = True
except ImportError:
    xp = np
    USING_GPU = False


REPO_ROOT = Path(__file__).parent.parent.parent
OUTPUT_DIR = REPO_ROOT / "outputs" / "convention_L_matrix"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def fft_kinetic_phase(N: int, L: float, d: int):
    k_axis = 2 * xp.pi * xp.fft.fftfreq(N, d=L / N)
    grids = xp.meshgrid(*[k_axis] * d, indexing="ij")
    k_squared = sum(g ** 2 for g in grids)
    return -1j * 0.5 * k_squared


def initial_state(N: int, L: float, d: int, sigma_init: float, convention: str):
    """Initial Gaussian state in convention A or B."""
    coord = xp.linspace(-L / 2, L / 2, N, endpoint=False)
    grids = xp.meshgrid(*[coord] * d, indexing="ij")
    r_squared = sum(g ** 2 for g in grids)
    if convention == "A":
        # non-normalized (continuum L2 = 1)
        prefactor = (1.0 / (sigma_init * float(np.sqrt(2 * np.pi)))) ** (d / 2)
        psi = prefactor * xp.exp(-r_squared / (2 * sigma_init ** 2))
        psi = psi.astype(xp.complex64)
    elif convention == "B":
        # discrete L2 = 1
        psi = xp.exp(-r_squared / (2 * sigma_init ** 2)).astype(xp.complex64)
        dx = L / N
        norm = float(xp.sqrt(xp.sum(xp.abs(psi) ** 2) * dx ** d))
        psi = psi / norm
    else:
        raise ValueError(f"Unknown convention {convention}")
    return psi


def run_cell(d: int, N: int, L: float, sigma_init: float, convention: str,
             Lambda: float, Sigma_lambda: float, gamma_0: float, T_bath: float,
             nu_fast: float = 10.0, nu_slow: float = 0.5,
             dt: float = 0.0025, n_steps: int = 2000, seed: int = 42) -> dict:
    rng = np.random.default_rng(seed)
    psi = initial_state(N, L, d, sigma_init, convention)
    kinetic_phase = fft_kinetic_phase(N, L, d)
    propagator = xp.exp(kinetic_phase * dt)

    lambda_fast = Sigma_lambda * 0.75
    lambda_slow = Sigma_lambda * 0.25
    y_fast = xp.zeros_like(psi.real, dtype=xp.float32)
    y_slow = xp.zeros_like(psi.real, dtype=xp.float32)
    decay_fast = float(np.exp(-nu_fast * dt))
    decay_slow = float(np.exp(-nu_slow * dt))
    accum_fast = 1.0 - decay_fast
    accum_slow = 1.0 - decay_slow

    dissipation_factor = float(np.exp(-gamma_0 * dt))
    noise_amp = float(np.sqrt(2.0 * gamma_0 * T_bath * dt))

    dx = L / N
    initial_norm = float(xp.sum(xp.abs(psi) ** 2) * dx ** d)
    initial_peak = float(xp.max(xp.abs(psi) ** 2))

    max_peak = initial_peak
    t0 = time.time()
    for step in range(n_steps):
        rho = (psi.real ** 2 + psi.imag ** 2).astype(xp.float32)
        V_mem = lambda_fast * y_fast + lambda_slow * y_slow
        V_total = Lambda * rho + V_mem
        psi = psi * xp.exp(-1j * V_total * dt / 2)
        psi = xp.fft.ifftn(xp.fft.fftn(psi) * propagator)
        rho = (psi.real ** 2 + psi.imag ** 2).astype(xp.float32)
        V_mem = lambda_fast * y_fast + lambda_slow * y_slow
        V_total = Lambda * rho + V_mem
        psi = psi * xp.exp(-1j * V_total * dt / 2)
        y_fast = decay_fast * y_fast + accum_fast * rho
        y_slow = decay_slow * y_slow + accum_slow * rho
        psi = psi * dissipation_factor
        if noise_amp > 0:
            xi_re = xp.asarray(rng.standard_normal(psi.shape).astype(np.float32))
            xi_im = xp.asarray(rng.standard_normal(psi.shape).astype(np.float32))
            psi = psi + noise_amp * (xi_re + 1j * xi_im) / float(np.sqrt(2.0))
        if step % 25 == 0:
            cur_peak = float(xp.max((psi.real ** 2 + psi.imag ** 2)))
            if cur_peak > max_peak:
                max_peak = cur_peak

    wall = time.time() - t0
    final_peak = float(xp.max((psi.real ** 2 + psi.imag ** 2)))
    final_norm = float(xp.sum(xp.abs(psi) ** 2) * dx ** d)
    peak_growth = max_peak / max(initial_peak, 1e-12)
    final_ratio = final_peak / max(initial_peak, 1e-12)

    if peak_growth > 50 and final_ratio > 10:
        regime = "collapse"
    elif peak_growth > 5 and final_ratio < 0.5:
        regime = "released"
    elif peak_growth > 50:
        regime = "runaway"
    elif 0.5 <= final_ratio <= 2.0:
        regime = "stable"
    elif final_ratio < 0.5 and peak_growth < 2:
        regime = "dispersive"
    else:
        regime = "intermediate"

    return {
        "convention": convention, "d": d, "N": N, "L": L,
        "sigma_init": sigma_init,
        "Sigma_lambda": Sigma_lambda, "gamma_0": gamma_0,
        "initial_peak": initial_peak, "initial_norm": initial_norm,
        "max_peak": max_peak, "final_peak": final_peak, "final_norm": final_norm,
        "peak_growth_ratio": peak_growth, "final_ratio": final_ratio,
        "regime": regime, "wall_time": wall,
    }


def main():
    print(f"Convention x L matrix at d=2, d=3")
    print(f"Backend: {'cupy (GPU)' if USING_GPU else 'numpy (CPU)'}")

    Lambda = -8.0
    T_bath = 0.001
    n_steps = 2000

    # Define the 4 cells at L=10 (the 4 cells at L=20 are in results/26, 27, 31)
    CELLS = [
        {"label": "A_L10_d2", "convention": "A", "d": 2, "N": 128, "L": 10.0, "sigma_init": 0.4,
         "SL": [0.05, 0.1, 0.5, 1.0, 2.0]},
        {"label": "A_L10_d3", "convention": "A", "d": 3, "N": 48, "L": 10.0, "sigma_init": 0.4,
         "SL": [0.5, 1.0, 1.5, 2.0, 4.0]},
        {"label": "B_L10_d2", "convention": "B", "d": 2, "N": 128, "L": 10.0, "sigma_init": 0.5,
         "SL": [0.05, 0.1, 0.5, 1.0, 2.0]},
        {"label": "B_L10_d3", "convention": "B", "d": 3, "N": 48, "L": 10.0, "sigma_init": 0.5,
         "SL": [0.5, 1.0, 1.5, 2.0, 4.0]},
    ]
    GAMMA_0_VALUES = [0.01, 0.05, 0.2, 1.0]

    all_results = {}
    t_total = time.time()

    for cell in CELLS:
        label = cell["label"]
        print(f"\n=== Cell {label}: convention={cell['convention']}, d={cell['d']}, "
              f"L={cell['L']}, N={cell['N']}, sigma={cell['sigma_init']} ===")
        psi_init = initial_state(cell["N"], cell["L"], cell["d"],
                                  cell["sigma_init"], cell["convention"])
        dx = cell["L"] / cell["N"]
        init_peak = float(xp.max(xp.abs(psi_init) ** 2))
        init_norm = float(xp.sum(xp.abs(psi_init) ** 2) * dx ** cell["d"])
        print(f"  Initial: peak={init_peak:.4f}, discrete L2 norm={init_norm:.4f}, dx={dx:.4f}")

        grid = []
        for sl in cell["SL"]:
            for g0 in GAMMA_0_VALUES:
                seed = 42 + int(sl * 10) + int(g0 * 100)
                r = run_cell(d=cell["d"], N=cell["N"], L=cell["L"],
                             sigma_init=cell["sigma_init"], convention=cell["convention"],
                             Lambda=Lambda, Sigma_lambda=sl, gamma_0=g0, T_bath=T_bath,
                             n_steps=n_steps, seed=seed)
                grid.append(r)
                print(f"  Sl={sl:>5.2f}, g0={g0:>5.2f}: regime={r['regime']:>14s}  "
                      f"peak_growth={r['peak_growth_ratio']:>8.2f}  "
                      f"final_ratio={r['final_ratio']:>10.4f}  "
                      f"t={r['wall_time']:.1f}s")

        regime_counts = {}
        for r in grid:
            regime_counts[r["regime"]] = regime_counts.get(r["regime"], 0) + 1
        print(f"  Regime counts: {regime_counts}")
        all_results[label] = {
            "cell": cell, "grid": grid, "regime_counts": regime_counts,
            "initial_peak": init_peak, "initial_norm": init_norm,
        }

    t_total = time.time() - t_total
    print(f"\nTotal wall: {t_total:.1f}s")
    print(f"\nSummary across cells:")
    for label, data in all_results.items():
        print(f"  {label}: {data['regime_counts']}")

    summary = {
        "prediction_tested": "Convention x L matrix at d=2, d=3 to complete the convention audit",
        "config": {"Lambda": Lambda, "T_bath": T_bath, "n_steps": n_steps,
                   "dt": 0.0025, "nu_fast": 10.0, "nu_slow": 0.5},
        "gamma_0_values": GAMMA_0_VALUES,
        "cells": all_results,
        "wall_time_total_s": t_total,
        "backend": "cupy" if USING_GPU else "numpy",
    }
    with open(OUTPUT_DIR / "summary.json", "w") as f:
        json.dump(summary, f, indent=2)
    print(f"\nSummary written to {OUTPUT_DIR}/summary.json")


if __name__ == "__main__":
    main()
