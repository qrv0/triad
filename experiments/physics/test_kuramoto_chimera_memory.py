"""Test prediction P10.1 (interface 10 Kuramoto synchronization).

Prediction: chimera-state stability in memory-Kuramoto ensembles is maximal
in the parameter window where the memory kernel timescale tau_mem is
comparable to the synchronization timescale tau_sync of the synchronized
cluster.

Method: simulate a 1D ring of N coupled phase oscillators with Gaussian
spatial coupling kernel, phase lag alpha near pi/2 (the Abrams-Strogatz
chimera regime), and a single-exponential coupling memory in the form of
the auxiliary-field Markovian embedding (the same construction documented
in ../../equation/02-markovian-embedding.md). Sweep the memory decay rate
nu (so tau_mem = 1/nu) across several decades. Measure chimera lifetime
at each tau_mem and check the predicted peak near tau_mem/tau_sync ~ 1.

Backend: numpy (CPU) at N=256. The dynamics is cheap enough to run on CPU
in minutes; a CuPy GPU version would be unnecessarily heavy for this scale.

Expected wall time: approximately 10 minutes on a modern CPU.

Output: outputs/kuramoto_chimera_memory/

This test does not duplicate any existing experiment in this folder.
"""

from __future__ import annotations
import json
import sys
import time
from pathlib import Path

import numpy as np


REPO_ROOT = Path(__file__).parent.parent.parent
OUTPUT_DIR = REPO_ROOT / "outputs" / "kuramoto_chimera_memory"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


# Simulation parameters (held constant across the sweep)
N = 256                  # ring size
T_FINAL = 250.0          # dimensionless time
DT = 0.025               # time step (CFL-stable for the kernel and lag)
SAMPLE_EVERY = 40        # observable sampling stride (every 1.0 time unit)
SIGMA_KERNEL = 12.0      # Gaussian kernel width (in units of oscillator index)
K_COUPLING = 1.0         # coupling strength
ALPHA = 1.45             # phase lag (rad); near pi/2 for chimera regime
OMEGA_SPREAD = 0.0       # zero spread: identical natural frequencies
SEED = 42

# Sweep: nu = 1/tau_mem in a decade-spanning range.
# tau_sync at K=1 on this kernel/lag is empirically ~1-3 units.
NU_VALUES = [0.01, 0.03, 0.1, 0.3, 1.0, 3.0, 10.0, 30.0]  # tau_mem = 100..0.033


def build_kernel(N: int, sigma: float) -> np.ndarray:
    """Periodic Gaussian kernel matrix G[i,j] = exp(-d(i,j)^2/(2 sigma^2)).

    Distance d(i,j) is the periodic ring distance.
    """
    idx = np.arange(N)
    diff = idx[:, None] - idx[None, :]
    # Periodic distance: min(|d|, N - |d|)
    periodic = np.minimum(np.abs(diff), N - np.abs(diff))
    K = np.exp(-(periodic.astype(np.float64) ** 2) / (2.0 * sigma ** 2))
    # Row-normalize so each row sums to 1 (proper kernel average)
    K /= K.sum(axis=1, keepdims=True)
    return K


def initial_condition_chimera(N: int, seed: int) -> np.ndarray:
    """Chimera-seed initial condition.

    Half the ring is set to nearly-synchronized phases (small perturbation
    around theta=0); the other half is set to uniformly random phases.
    The dynamics either preserves this asymmetry (chimera survives) or
    resolves to a uniform regime (chimera dissolves).
    """
    rng = np.random.default_rng(seed)
    theta = np.zeros(N, dtype=np.float64)
    half = N // 2
    # Synchronized half: small Gaussian noise around 0
    theta[:half] = 0.05 * rng.standard_normal(half)
    # Desynchronized half: uniform on [0, 2pi)
    theta[half:] = 2 * np.pi * rng.random(N - half)
    return theta


def local_order_parameter(theta: np.ndarray, K: np.ndarray) -> np.ndarray:
    """Local complex order parameter z_i = sum_j K_ij exp(i theta_j)."""
    z_complex = K @ np.exp(1j * theta)
    return z_complex


def chimera_index(theta: np.ndarray, K: np.ndarray) -> float:
    """Quantitative chimera index: standard deviation of local |z| across ring.

    For a fully synchronized state, |z_i| ≈ 1 everywhere, std ≈ 0.
    For a fully desynchronized state, |z_i| ≈ 0 everywhere, std ≈ 0.
    For a chimera, |z_i| ≈ 1 on one side and ≈ 0 on the other, std is large.
    A robust threshold: index > 0.1 corresponds to a distinct chimera structure
    on this scale; lower means the asymmetry has dissolved.
    """
    z = local_order_parameter(theta, K)
    r_local = np.abs(z)
    return float(np.std(r_local))


def simulate(nu: float, K_kernel: np.ndarray, theta0: np.ndarray,
             t_final: float, dt: float, sample_every: int) -> dict:
    """Simulate memory-Kuramoto on the ring.

    Equation (Markovian embedding of single-exponential memory):
        d theta_i / dt = K_coupling * Im[ exp(-i(theta_i + alpha)) * Y_i ]
        d Y_i / dt = nu * (Z_i - Y_i)
    where:
        Z_i = sum_j K_kernel[i,j] exp(i theta_j(t))    (instantaneous local order)
        Y_i(t) = nu * integral_0^t exp(-nu*(t-t')) Z_i(t') dt'   (memory-integrated)
    """
    N = len(theta0)
    theta = theta0.copy()
    # Initialize auxiliary field to the instantaneous order at t=0
    Y = local_order_parameter(theta, K_kernel)

    n_steps = int(t_final / dt)
    samples = []
    # Exact OU update factor (independent of dt; paper §4.1 specifies this is exact):
    # Y(t+dt) = exp(-nu dt) Y(t) + (1 - exp(-nu dt)) Z   (frozen-Z over step)
    decay = np.exp(-nu * dt)
    accumulator = 1.0 - decay

    for step in range(n_steps):
        # Instantaneous local order parameter
        Z = local_order_parameter(theta, K_kernel)
        # Memory auxiliary field update (Markovian embedding; exact per paper §4.1)
        Y = decay * Y + accumulator * Z
        # Phase update using memory-integrated order Y
        coupling = K_COUPLING * np.imag(np.exp(-1j * (theta + ALPHA)) * Y)
        theta = theta + dt * coupling
        # Wrap to [0, 2pi)
        theta = np.mod(theta, 2 * np.pi)

        # Sample observables periodically
        if step % sample_every == 0:
            ci = chimera_index(theta, K_kernel)
            samples.append({"t": step * dt, "chimera_index": ci})

    return {
        "nu": nu,
        "tau_mem": 1.0 / nu,
        "samples": samples,
        "final_theta": theta,
    }


def chimera_lifetime(samples: list, threshold: float = 0.1) -> float:
    """Compute chimera lifetime: time spent above the chimera-index threshold.

    Defined as the fraction of sampled time during which the chimera index
    exceeds the threshold. A value near 1.0 means the chimera persists
    throughout the simulation; a value near 0.0 means the chimera dissolves
    quickly.
    """
    above = [s for s in samples if s["chimera_index"] > threshold]
    if not samples:
        return 0.0
    return len(above) / len(samples)


def main():
    print(f"Phase 9 Test A: memory-Kuramoto chimera stability (P10.1)")
    print(f"N = {N}, T_final = {T_FINAL}, dt = {DT}")
    print(f"Sweep nu = {NU_VALUES}")
    print(f"Output: {OUTPUT_DIR}")

    K = build_kernel(N, SIGMA_KERNEL)
    theta0 = initial_condition_chimera(N, SEED)

    t_total = time.time()
    runs = []
    for nu in NU_VALUES:
        t0 = time.time()
        result = simulate(nu, K, theta0, T_FINAL, DT, SAMPLE_EVERY)
        lifetime = chimera_lifetime(result["samples"], threshold=0.1)
        run_time = time.time() - t0

        run_summary = {
            "nu": nu,
            "tau_mem": result["tau_mem"],
            "chimera_lifetime_fraction": lifetime,
            "mean_chimera_index": float(np.mean([s["chimera_index"] for s in result["samples"]])),
            "final_chimera_index": result["samples"][-1]["chimera_index"],
            "wall_time": run_time,
        }
        runs.append(run_summary)

        # Save trajectory
        ci_series = np.array([s["chimera_index"] for s in result["samples"]])
        ts = np.array([s["t"] for s in result["samples"]])
        np.savez(
            OUTPUT_DIR / f"nu_{nu:.3f}.npz",
            ts=ts,
            chimera_index=ci_series,
            final_theta=result["final_theta"],
            nu=nu,
            tau_mem=result["tau_mem"],
        )
        print(f"  nu = {nu:>7.3f} (tau_mem = {result['tau_mem']:>7.3f}): "
              f"lifetime = {lifetime:.3f}, mean CI = {run_summary['mean_chimera_index']:.4f}, "
              f"t = {run_time:.1f}s")

    t_total = time.time() - t_total
    print(f"\nTotal wall time: {t_total:.1f}s")

    # Summary
    summary = {
        "prediction": "P10.1 (interface 10)",
        "parameters": {
            "N": N,
            "T_final": T_FINAL,
            "dt": DT,
            "sigma_kernel": SIGMA_KERNEL,
            "K_coupling": K_COUPLING,
            "alpha": ALPHA,
            "seed": SEED,
        },
        "runs": runs,
        "wall_time_total_s": t_total,
    }
    with open(OUTPUT_DIR / "summary.json", "w") as f:
        json.dump(summary, f, indent=2)

    # Print finalized table
    print()
    print(f"{'nu':>10} | {'tau_mem':>10} | {'chimera_lifetime':>18} | {'mean_CI':>10}")
    print("-" * 60)
    for r in runs:
        print(f"{r['nu']:>10.3f} | {r['tau_mem']:>10.3f} | {r['chimera_lifetime_fraction']:>18.3f} | "
              f"{r['mean_chimera_index']:>10.4f}")

    # Identify peak
    peak_run = max(runs, key=lambda r: r["chimera_lifetime_fraction"])
    print(f"\nPeak chimera lifetime: nu = {peak_run['nu']}, tau_mem = {peak_run['tau_mem']:.3f}, "
          f"lifetime fraction = {peak_run['chimera_lifetime_fraction']:.3f}")
    print()
    print("Prediction check (P10.1): the peak should sit near tau_mem ~ tau_sync ~ 1-3 units")
    print(f"  for the kernel and K used. Observed peak at tau_mem = {peak_run['tau_mem']:.3f}.")


if __name__ == "__main__":
    main()
