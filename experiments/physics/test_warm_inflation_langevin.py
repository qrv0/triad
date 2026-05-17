"""Test P20.3: Warm-inflation Langevin SDE thermalizes to FDT-equipartition.

Prediction tested
-----------------
Interface 20, prediction P20.3. The warm-inflation Langevin equation
    ddot phi + (3H + Upsilon) dot phi + V'(phi) = xi(t)
with FDT-locked noise <xi(t) xi(t')> = 2 Upsilon T delta(t-t') should
produce, in the strong-dissipation regime Upsilon >> H, a quasi-
equilibrium thermal state characterized by equipartition statistics:
    <dot phi^2> ~ T  (in natural units k_B = 1)

The cold-inflation limit Upsilon -> 0 should NOT produce thermalization;
the dissipation channel that balances the noise is absent.

Method
------
- Quadratic potential V(phi) = m^2 phi^2 / 2 (massive scalar, simplest case).
- Two regimes: strong dissipation (Upsilon = 20 H, FDT active) and cold
  inflation limit (Upsilon = 0, no dissipation).
- Stochastic Euler-Maruyama integration of the second-order Langevin SDE
  rewritten as two first-order equations on (phi, dot_phi).
- Run an ensemble of trajectories from cold start (phi_0=0, dot_phi_0=0).
- Measure ensemble statistics <dot_phi^2> after thermalization window.

Wall time: ~20 seconds for 200 ensemble members on CPU.
Output: outputs/warm_inflation_langevin/summary.json

Reproduces from a fresh clone with `python experiments/physics/
test_warm_inflation_langevin.py`. Seed 42.
"""

from __future__ import annotations

import json
import os
import time
import numpy as np


def integrate_warm_inflaton(
    Upsilon, H, T, m, dt, n_steps, phi0=0.0, phidot0=0.0, seed=42
):
    """Euler-Maruyama integration of warm-inflation Langevin SDE.

    dot phi = pi
    dot pi = -(3H + Upsilon) pi - m^2 phi + xi(t),  <xi(t) xi(t')> = 2 Upsilon T delta(t-t')

    Returns time, phi, pi=dot_phi arrays.
    """
    rng = np.random.default_rng(seed)
    phi = phi0
    pi = phidot0
    phis = np.zeros(n_steps + 1)
    pis = np.zeros(n_steps + 1)
    phis[0] = phi
    pis[0] = pi
    sqrt_dt = np.sqrt(dt)
    sigma_noise = np.sqrt(2 * Upsilon * T)
    for k in range(n_steps):
        dW = rng.standard_normal()
        force = -(3 * H + Upsilon) * pi - m ** 2 * phi
        phi_new = phi + dt * pi
        pi_new = pi + dt * force + sigma_noise * sqrt_dt * dW
        phi, pi = phi_new, pi_new
        phis[k + 1] = phi
        pis[k + 1] = pi
    t_grid = dt * np.arange(n_steps + 1)
    return t_grid, phis, pis


def run_ensemble(Upsilon, H, T, m, dt, n_steps, n_traj, seed_base=42):
    """Run ensemble of trajectories, return per-trajectory final statistics."""
    pi_squared_final = np.zeros(n_traj)
    phi_squared_final = np.zeros(n_traj)
    pi_squared_tail_mean = np.zeros(n_traj)
    tail_start = int(n_steps * 0.5)  # take statistics from second half of trajectory
    for i in range(n_traj):
        _, phis, pis = integrate_warm_inflaton(
            Upsilon, H, T, m, dt, n_steps, seed=seed_base + i
        )
        pi_squared_final[i] = pis[-1] ** 2
        phi_squared_final[i] = phis[-1] ** 2
        pi_squared_tail_mean[i] = np.mean(pis[tail_start:] ** 2)
    return {
        "pi_squared_final_mean": float(np.mean(pi_squared_final)),
        "pi_squared_final_std": float(np.std(pi_squared_final)),
        "phi_squared_final_mean": float(np.mean(phi_squared_final)),
        "phi_squared_final_std": float(np.std(phi_squared_final)),
        "pi_squared_tail_mean_avg": float(np.mean(pi_squared_tail_mean)),
        "pi_squared_tail_mean_std": float(np.std(pi_squared_tail_mean)),
    }


def main():
    t_start = time.time()

    # Common parameters
    H = 0.1  # Hubble rate (constant; de Sitter approximation)
    T = 1.0  # bath temperature
    m = 1.0  # inflaton mass (sets potential scale)
    dt = 0.01
    n_steps = 5000  # t_max = 50; with Upsilon=20H=2, thermalization ~ 5/Upsilon ~ 2.5
    n_traj = 200
    seed_base = 42

    print(f"Common parameters: H={H}, T={T}, m={m}, dt={dt}, n_steps={n_steps}, n_traj={n_traj}")
    print()

    # Strong-dissipation regime: Upsilon = 20 H (warm inflation, FDT active)
    Upsilon_warm = 20 * H
    print(f"Regime A: warm inflation, Upsilon={Upsilon_warm} (= {Upsilon_warm/H:.0f} H)")
    warm_stats = run_ensemble(Upsilon_warm, H, T, m, dt, n_steps, n_traj, seed_base)
    print(f"  <pi^2>_tail = {warm_stats['pi_squared_tail_mean_avg']:.4f} +/- {warm_stats['pi_squared_tail_mean_std']:.4f}")
    print(f"  <phi^2>_final = {warm_stats['phi_squared_final_mean']:.4f}")
    print()

    # Cold-inflation limit: Upsilon = 0 (no FDT noise)
    Upsilon_cold = 0.0
    print(f"Regime B: cold inflation, Upsilon={Upsilon_cold}")
    cold_stats = run_ensemble(Upsilon_cold, H, T, m, dt, n_steps, n_traj, seed_base + 10000)
    print(f"  <pi^2>_tail = {cold_stats['pi_squared_tail_mean_avg']:.4f} +/- {cold_stats['pi_squared_tail_mean_std']:.4f}")
    print(f"  <phi^2>_final = {cold_stats['phi_squared_final_mean']:.4f}")
    print()

    # Equipartition check: in strong dissipation warm regime, <pi^2> should approach T
    # because the FDT correlator <xi xi> = 2 Upsilon T delta drives the system to a
    # canonical Boltzmann distribution; for the kinetic degree of freedom this gives
    # <pi^2> = T (with k_B = 1, mass = 1 for the pi variable, since the Lagrangian
    # has standard normalization).
    expected_pi2 = T
    rel_err_warm = abs(warm_stats["pi_squared_tail_mean_avg"] - expected_pi2) / expected_pi2
    print(f"Equipartition check (warm regime):")
    print(f"  expected <pi^2> = T = {expected_pi2}")
    print(f"  measured <pi^2> = {warm_stats['pi_squared_tail_mean_avg']:.4f}")
    print(f"  relative error: {rel_err_warm:.3e}")
    print(f"  (cold regime: <pi^2>_cold = {cold_stats['pi_squared_tail_mean_avg']:.4f}, far from T)")

    wall = time.time() - t_start

    # Test passes if:
    # (a) warm regime <pi^2> within 15% of T (equipartition holds)
    # (b) cold regime <pi^2> much smaller than T (no thermalization)
    threshold_warm = 0.15
    threshold_cold_max = 0.1 * T  # cold regime should be far below T
    passes_warm = rel_err_warm < threshold_warm
    passes_cold = cold_stats["pi_squared_tail_mean_avg"] < threshold_cold_max
    passes = passes_warm and passes_cold

    summary = {
        "prediction": "P20.3 (interface 20 warm-inflation FDT equipartition)",
        "parameters": {
            "H": H,
            "T": T,
            "m": m,
            "dt": dt,
            "n_steps": n_steps,
            "n_traj": n_traj,
        },
        "warm_regime": {"Upsilon": Upsilon_warm, **warm_stats},
        "cold_regime": {"Upsilon": Upsilon_cold, **cold_stats},
        "equipartition": {
            "expected_pi_squared": expected_pi2,
            "warm_pi_squared_relative_error": float(rel_err_warm),
            "warm_passes_threshold_0.15": bool(passes_warm),
            "cold_pi_squared_below_threshold": bool(passes_cold),
            "overall_passes": bool(passes),
        },
        "wall_time_s": float(wall),
        "backend": "numpy",
        "seed_base": seed_base,
    }

    out_dir = "outputs/warm_inflation_langevin"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "summary.json"), "w") as f:
        json.dump(summary, f, indent=2)

    print()
    print(f"Wall time: {wall:.2f}s")
    print(f"Output: {out_dir}/summary.json")
    print(f"Overall passes: {passes}")

    if passes:
        print()
        print("Status: tested_consistent")
        print("P20.3 supported: in the strong-dissipation regime, the warm-inflaton")
        print("Langevin SDE thermalizes to the FDT-predicted equipartition state with")
        print("<pi^2> = T. The cold-inflation limit (Upsilon=0) shows no thermalization,")
        print("consistent with the structural prediction that the FDT lock requires")
        print("both dissipation and noise to be present and locked. This instantiates")
        print("the structural P3 condition the present equation derives.")
    else:
        print()
        print("Status: tested_inconsistent or partial")


if __name__ == "__main__":
    main()
