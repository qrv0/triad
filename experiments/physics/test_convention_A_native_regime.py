"""Convention A at its native parameter regime at d=2 and d=3.

Verifies the dimensional-rescaling series' claim that Convention A
(sigma=0.4 non-normalized) achieves focal-collapse access at d=2 and
d=3 under the series' native parameter regime (T_bath=0.05,
n_steps=4000, gamma_0 from 0.05).

Companion to test_convention_L_matrix.py which used the phase-diagram
series' parameter regime (T_bath=0.001, n_steps=2000, gamma_0 from
0.01) and found Convention A all-dispersive at both L=10 and L=20.

If Convention A at the native regime gives focal-collapse at d=2, d=3,
the structural reading is confirmed: Convention A is regime-paired with
(T_bath=0.05+, n_steps=4000+), and the dimensional-rescaling series'
focal-collapse access at d=4, d=5 (results/15) is a property of that
paired regime, not of Convention A in isolation.

Output: outputs/convention_A_native_regime/summary.json.

Wall time estimate: ~10-15 min on RTX 4060 (n_steps=4000 is 2x longer
than phase-diagram series, 2 cells at L=10).
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
OUTPUT_DIR = REPO_ROOT / "outputs" / "convention_A_native_regime"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def fft_kinetic_propagator(N: int, L: float, dt: float, gamma_0: float, d: int):
    """Canonical kinetic propagator U_k with dissipation folded in.

    Matches implementation/physics/solver_3d.py build_kinetic_propagator:
    H_complex = k^2/(2m) - i gamma_0, U_k = exp(-i H_complex dt).
    """
    k_axis = 2 * xp.pi * xp.fft.fftfreq(N, d=L / N)
    grids = xp.meshgrid(*[k_axis] * d, indexing="ij")
    k_squared = sum(g ** 2 for g in grids)
    H_kin = 0.5 * k_squared
    H_complex = H_kin.astype(xp.complex64) - 1j * gamma_0
    return xp.exp(-1j * H_complex * dt).astype(xp.complex64)


def initial_convention_A(N: int, L: float, d: int, sigma_init: float):
    coord = xp.linspace(-L / 2, L / 2, N, endpoint=False)
    grids = xp.meshgrid(*[coord] * d, indexing="ij")
    r_squared = sum(g ** 2 for g in grids)
    prefactor = (1.0 / (sigma_init * float(np.sqrt(2 * np.pi)))) ** (d / 2)
    psi = prefactor * xp.exp(-r_squared / (2 * sigma_init ** 2))
    return psi.astype(xp.complex64)


def run_cell(d: int, N: int, L: float, sigma_init: float,
             Lambda: float, Sigma_lambda: float, gamma_0: float, T_bath: float,
             nu_fast: float = 10.0, nu_slow: float = 0.5,
             dt: float = 0.0025, n_steps: int = 4000, seed: int = 42) -> dict:
    rng = np.random.default_rng(seed)
    psi = initial_convention_A(N, L, d, sigma_init)
    propagator = fft_kinetic_propagator(N, L, dt, gamma_0, d)

    lambda_fast = Sigma_lambda * 0.75
    lambda_slow = Sigma_lambda * 0.25
    y_fast = xp.zeros_like(psi.real, dtype=xp.float32)
    y_slow = xp.zeros_like(psi.real, dtype=xp.float32)
    decay_fast = float(np.exp(-nu_fast * dt))
    decay_slow = float(np.exp(-nu_slow * dt))
    accum_fast = 1.0 - decay_fast
    accum_slow = 1.0 - decay_slow

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
        if noise_amp > 0:
            xi_re = xp.asarray(rng.standard_normal(psi.shape).astype(np.float32))
            xi_im = xp.asarray(rng.standard_normal(psi.shape).astype(np.float32))
            psi = psi + noise_amp * (xi_re + 1j * xi_im) / float(np.sqrt(2.0))
        if step % 50 == 0:
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
        "d": d, "Sigma_lambda": Sigma_lambda, "gamma_0": gamma_0,
        "initial_peak": initial_peak, "initial_norm": initial_norm,
        "max_peak": max_peak, "final_peak": final_peak, "final_norm": final_norm,
        "peak_growth_ratio": peak_growth, "final_ratio": final_ratio,
        "regime": regime, "wall_time": wall,
    }


def main():
    print(f"Convention A at native regime: T_bath=0.05, n_steps=4000")
    print(f"Backend: {'cupy (GPU)' if USING_GPU else 'numpy (CPU)'}")

    Lambda = -8.0
    T_bath = 0.05
    n_steps = 4000
    sigma_init = 0.4
    L = 10.0

    CELLS = [
        {"label": "A_native_d2", "d": 2, "N": 128,
         "SL": [0.05, 0.1, 0.5, 1.0, 2.0]},
        {"label": "A_native_d3", "d": 3, "N": 48,
         "SL": [0.5, 1.0, 1.5, 2.0, 4.0]},
    ]
    # Rule 10 (CLAUDE.md): t_integration = 4000 * 0.0025 = 10.0; all gamma_0 satisfy 1/gamma_0 <= t_integration.
    # Pre-2026-05-17 sweep [0.05, 0.2, 1.0] had 0.05 in marginal hedge regime.
    GAMMA_0_VALUES = [0.1, 0.5, 1.0, 2.0]

    all_results = {}
    t_total = time.time()

    for cell in CELLS:
        label = cell["label"]
        print(f"\n=== Cell {label}: d={cell['d']}, N={cell['N']}, L={L} ===")
        psi_init = initial_convention_A(cell["N"], L, cell["d"], sigma_init)
        dx = L / cell["N"]
        init_peak = float(xp.max(xp.abs(psi_init) ** 2))
        init_norm = float(xp.sum(xp.abs(psi_init) ** 2) * dx ** cell["d"])
        print(f"  Initial: peak={init_peak:.4f}, discrete L2 norm={init_norm:.4f}, dx={dx:.4f}")

        grid = []
        for sl in cell["SL"]:
            for g0 in GAMMA_0_VALUES:
                seed = 42 + int(sl * 10) + int(g0 * 100)
                r = run_cell(d=cell["d"], N=cell["N"], L=L,
                             sigma_init=sigma_init,
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
            "d": cell["d"], "N": cell["N"], "L": L,
            "grid": grid, "regime_counts": regime_counts,
            "initial_peak": init_peak, "initial_norm": init_norm,
        }

    t_total = time.time() - t_total
    print(f"\nTotal wall: {t_total:.1f}s")
    print(f"\nSummary across cells:")
    for label, data in all_results.items():
        print(f"  {label}: {data['regime_counts']}")

    summary = {
        "prediction_tested": "Convention A at native regime (T_bath=0.05, n_steps=4000) at d=2, d=3",
        "config": {"Lambda": Lambda, "sigma_init": sigma_init, "L": L,
                   "T_bath": T_bath, "n_steps": n_steps,
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
