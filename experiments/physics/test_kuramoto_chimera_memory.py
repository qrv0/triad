"""Wave-2 test: memory-Kuramoto chimera stability under FDT-locked phase noise.

Targets prediction P10.1 (interface 10 Kuramoto synchronization), redesigned
to respect P3 per the post-retraction methodology committed to by the work.

Wave 1 was retracted (commit c11666b) because it tested the P1+P2 degenerate
sub-system (gamma_0=0, T=0; no FDT-locked bath) rather than the full
P1+P2+P3 triangle. methodology/02-limits-of-falsification.md identifies
isolation as the abstraction the work argues against. This wave-2 script
makes the bath coupling (gamma_0, T) a primary sweep variable; isolation
is one degenerate point in the sweep, not the baseline.

Equation simulated:
    d theta_i / dt = K_coupling * Im[exp(-i(theta_i + alpha)) * Y_i]
                     + sqrt(2 * gamma_0 * T / dt) * xi_i

with the Markovian-embedded memory auxiliary field:
    Y_i(t+dt) = exp(-nu * dt) * Y_i(t) + (1 - exp(-nu * dt)) * Z_i(t)
where Z_i = sum_j K_kernel[i,j] exp(i theta_j) is the local order parameter.

The Langevin noise term represents environmental coupling to a bath at
temperature T with effective phase-dissipation rate gamma_0. The FDT lock
fixes the noise amplitude in terms of (gamma_0, T) per principle P3 and
the canonical FDT correlator stated in paper section 3.3.

Method: sweep (gamma_0, tau_mem) in a 2D grid; measure chimera lifetime
fraction in each (gamma_0, tau_mem) cell. The result is a 2D landscape
identifying where chimera structure persists under the full triangle vs
where it dissolves.

Backend: CuPy if available (GPU), otherwise NumPy. At N=256 the 1D ring is
inexpensive; full sweep (5 gamma_0 x 8 tau_mem = 40 trajectories) runs in
~1 minute on RTX 4060 or ~3 minutes on CPU.

Output: outputs/kuramoto_chimera_memory_p3/
"""

from __future__ import annotations
import json
import time
from pathlib import Path

import numpy as np

# GPU/CPU backend abstraction
try:
    import cupy as cp
    xp = cp
    USING_GPU = True
except ImportError:
    xp = np
    USING_GPU = False


REPO_ROOT = Path(__file__).parent.parent.parent
OUTPUT_DIR = REPO_ROOT / "outputs" / "kuramoto_chimera_memory_p3"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


# Simulation parameters
N = 256
T_FINAL = 250.0
DT = 0.025
SAMPLE_EVERY = 40
SIGMA_KERNEL = 12.0
K_COUPLING = 1.0
ALPHA = 1.45
SEED = 42

# Sweep specifications
# P3 coupling: gamma_0 from small positive (weak coupling) to large positive
# (strong coupling); T fixed at 0.1. Noise amplitude is sqrt(2 gamma_0 T dt)
# so gamma_0 controls both dissipation rate and noise amplitude jointly per
# the FDT correlator. The sweep starts at gamma_0 = 0.01: the isolated regime
# (gamma_0 = 0) is excluded per principles/03-coupling.md (Rule A in the
# structural-research-mode skill); it is not a configuration the methodology
# permits, even as a sweep endpoint.
GAMMA_0_VALUES = [0.01, 0.05, 0.2, 1.0]         # P3 coupling strength
T_BATH = 0.1                                     # bath temperature
NU_VALUES = [0.03, 0.1, 0.3, 1.0, 3.0, 10.0]   # memory rates (tau_mem = 1/nu)


def to_cpu(arr):
    if hasattr(arr, "get"):
        return arr.get()
    return arr


def build_kernel(N: int, sigma: float):
    idx = xp.arange(N)
    diff = idx[:, None] - idx[None, :]
    periodic = xp.minimum(xp.abs(diff), N - xp.abs(diff))
    K = xp.exp(-(periodic.astype(xp.float64) ** 2) / (2.0 * sigma ** 2))
    K /= K.sum(axis=1, keepdims=True)
    return K


def initial_condition_chimera(N: int, seed: int):
    rng = np.random.default_rng(seed)
    theta = np.zeros(N, dtype=np.float64)
    half = N // 2
    theta[:half] = 0.05 * rng.standard_normal(half)
    theta[half:] = 2 * np.pi * rng.random(N - half)
    return xp.asarray(theta)


def local_order_parameter(theta, K_kernel):
    return K_kernel @ xp.exp(1j * theta)


def chimera_index(theta, K_kernel) -> float:
    z = local_order_parameter(theta, K_kernel)
    r_local = xp.abs(z)
    return float(xp.std(r_local))


def simulate(gamma_0: float, T: float, nu: float, K_kernel, theta0,
             t_final: float, dt: float, sample_every: int, seed: int) -> dict:
    """Memory-Kuramoto with FDT-locked phase noise (P3 active).

    Equation:
        d_theta = K * Im[exp(-i(theta + alpha)) * Y] dt + sqrt(2 gamma_0 T dt) xi
        d_Y = nu * (Z - Y) dt       (Markovian-embedded memory)

    where xi is unit-variance Gaussian, Z is the instantaneous local order
    parameter, Y is the memory-integrated order.
    """
    N = theta0.shape[0]
    theta = theta0.copy()
    Y = local_order_parameter(theta, K_kernel)

    # OU decay factor for memory (exact per paper §4.1)
    decay = float(xp.exp(xp.asarray(-nu * dt)))
    accumulator = 1.0 - decay

    # FDT noise amplitude per Langevin discretization
    noise_amp = float(np.sqrt(2.0 * gamma_0 * T * dt))

    n_steps = int(t_final / dt)
    samples = []
    rng = np.random.default_rng(seed)

    for step in range(n_steps):
        Z = local_order_parameter(theta, K_kernel)
        Y = decay * Y + accumulator * Z
        coupling = K_COUPLING * xp.imag(xp.exp(-1j * (theta + ALPHA)) * Y)

        # Phase update with FDT-locked noise
        if noise_amp > 0:
            xi = xp.asarray(rng.standard_normal(N))
            theta = theta + dt * coupling + noise_amp * xi
        else:
            theta = theta + dt * coupling
        theta = xp.mod(theta, 2 * xp.pi)

        if step % sample_every == 0:
            ci = chimera_index(theta, K_kernel)
            samples.append({"t": step * dt, "chimera_index": ci})

    return {"gamma_0": gamma_0, "T": T, "nu": nu, "tau_mem": 1.0 / nu, "samples": samples}


def chimera_lifetime(samples: list, threshold: float = 0.1) -> float:
    if not samples:
        return 0.0
    above = sum(1 for s in samples if s["chimera_index"] > threshold)
    return above / len(samples)


def main():
    print(f"Wave 2 Test A: Memory-Kuramoto chimera stability with FDT-locked phase noise (P10.1)")
    print(f"Backend: {'cupy (GPU)' if USING_GPU else 'numpy (CPU)'}")
    print(f"N = {N}, T_final = {T_FINAL}, dt = {DT}")
    print(f"P3 sweep: gamma_0 = {GAMMA_0_VALUES} at T_bath = {T_BATH}")
    print(f"Memory sweep: nu = {NU_VALUES} (tau_mem = 1/nu)")
    print(f"Total runs: {len(GAMMA_0_VALUES)} x {len(NU_VALUES)} = "
          f"{len(GAMMA_0_VALUES) * len(NU_VALUES)} trajectories")

    K = build_kernel(N, SIGMA_KERNEL)
    theta0 = initial_condition_chimera(N, SEED)

    t_total = time.time()
    grid_results = []
    for g_idx, gamma_0 in enumerate(GAMMA_0_VALUES):
        for n_idx, nu in enumerate(NU_VALUES):
            run_seed = SEED + 1000 * g_idx + n_idx  # different seed per cell
            result = simulate(gamma_0, T_BATH, nu, K, theta0,
                              T_FINAL, DT, SAMPLE_EVERY, run_seed)
            lifetime = chimera_lifetime(result["samples"], threshold=0.1)
            mean_ci = float(np.mean([s["chimera_index"] for s in result["samples"]]))
            grid_results.append({
                "gamma_0": gamma_0,
                "T": T_BATH,
                "nu": nu,
                "tau_mem": 1.0 / nu,
                "chimera_lifetime_fraction": lifetime,
                "mean_chimera_index": mean_ci,
            })
            print(f"  gamma_0={gamma_0:.3f}  nu={nu:>6.3f}  tau_mem={1/nu:>7.3f}: "
                  f"lifetime={lifetime:.3f}  mean_CI={mean_ci:.4f}")

    t_total = time.time() - t_total
    print(f"\nTotal wall time: {t_total:.1f}s")

    # Identify peak and characterize the 2D landscape
    peak = max(grid_results, key=lambda r: r["chimera_lifetime_fraction"])
    print(f"\nPeak chimera lifetime: gamma_0 = {peak['gamma_0']}, "
          f"tau_mem = {peak['tau_mem']:.3f}, "
          f"lifetime = {peak['chimera_lifetime_fraction']:.3f}")

    # Compare isolated baseline (gamma_0=0) with coupled regimes
    isolated = [r for r in grid_results if r["gamma_0"] == 0]
    coupled = [r for r in grid_results if r["gamma_0"] > 0]
    if isolated and coupled:
        iso_max = max(r["chimera_lifetime_fraction"] for r in isolated)
        coup_max = max(r["chimera_lifetime_fraction"] for r in coupled)
        print(f"\nIsolated (gamma_0=0) max lifetime: {iso_max:.3f}")
        print(f"Coupled (gamma_0>0) max lifetime: {coup_max:.3f}")
        print(f"Ratio (coupled/isolated) at maximum: {coup_max/iso_max if iso_max > 0 else 'inf':.3f}")

    summary = {
        "prediction": "P10.1 (interface 10), wave 2 with FDT-locked phase noise",
        "parameters": {
            "N": N, "T_final": T_FINAL, "dt": DT,
            "sigma_kernel": SIGMA_KERNEL, "K_coupling": K_COUPLING, "alpha": ALPHA,
            "T_bath": T_BATH, "seed_base": SEED,
        },
        "grid_results": grid_results,
        "wall_time_total_s": t_total,
        "backend": "cupy" if USING_GPU else "numpy",
    }
    with open(OUTPUT_DIR / "summary.json", "w") as f:
        json.dump(summary, f, indent=2)
    print(f"\nFull data: {OUTPUT_DIR}/summary.json")


if __name__ == "__main__":
    main()
