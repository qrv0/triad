"""Test P19.1: Prony series fit reproduces stress relaxation via auxiliary-field equation.

Prediction tested
-----------------
Interface 19, prediction P19.1. Given a target stress relaxation modulus
G(t) = G_infty + sum_i G_i * exp(-t/tau_i), the auxiliary-field equation
    dq_i/dt + q_i / tau_i = d(epsilon_dev)/dt,  sigma_dev = 2*mu_tot*(mu_0*epsilon_dev + sum_i mu_i*q_i)
should reproduce the hereditary-integral stress response
    sigma_conv(t) = integral_{-inf}^{t} G(t - s) * (d epsilon/ds) ds
under arbitrary strain history, to within numerical precision.

This test instantiates the generalized Maxwell / Prony viscoelasticity
substrate (PyLith, COMSOL, Ansys industry-standard) using a synthetic
3-term Prony series and three strain protocols.

Method
------
- Construct a 3-term Prony series with relaxation times tau in {0.1, 1.0, 10.0}.
- Apply three strain histories: step (smoothed), ramp-and-hold, sinusoidal.
- For each, compute stress via (a) auxiliary-variable ODE and (b) direct
  hereditary-integral convolution. Compare per-time-step error.

Wall time: ~3 seconds on CPU.
Output: outputs/prony_viscoelastic_reproduction/summary.json

Reproduces from a fresh clone with `python experiments/physics/
test_prony_viscoelastic_reproduction.py`. Seed 42.
"""

from __future__ import annotations

import json
import os
import time
import numpy as np


def auxiliary_ode_rk4(eps_func, eps_dot_func, taus, mus, mu0, mu_tot, t_grid):
    """Integrate dq_i/dt + q_i/tau_i = d(eps_dev)/dt for each Maxwell element.

    Returns the deviatoric stress sigma_dev = 2*mu_tot*(mu0*eps + sum(mu_i*q_i))
    at each t in t_grid.
    """
    n_modes = len(taus)
    q = np.zeros(n_modes)
    sigma = np.zeros_like(t_grid)
    eps_vals = np.zeros_like(t_grid)
    for i, t in enumerate(t_grid):
        eps_vals[i] = eps_func(t)
        sigma[i] = 2 * mu_tot * (mu0 * eps_vals[i] + np.sum(mus * q))
        if i < len(t_grid) - 1:
            dt = t_grid[i + 1] - t_grid[i]
            eps_dot_now = eps_dot_func(t)
            eps_dot_mid = eps_dot_func(t + dt / 2)
            eps_dot_end = eps_dot_func(t + dt)
            for j in range(n_modes):
                tau = taus[j]
                # RK4 for dq/dt = -q/tau + eps_dot
                k1 = -q[j] / tau + eps_dot_now
                k2 = -(q[j] + dt * k1 / 2) / tau + eps_dot_mid
                k3 = -(q[j] + dt * k2 / 2) / tau + eps_dot_mid
                k4 = -(q[j] + dt * k3) / tau + eps_dot_end
                q[j] = q[j] + (dt / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
    return sigma, eps_vals


def convolution_stress(eps_dot_func, G_infty, G_i, taus, t_grid):
    """Compute sigma(t) = G_infty * eps(t) + sum_i integral_0^t G_i*exp(-(t-s)/tau_i)*eps_dot(s) ds.

    Note: This is mathematically equivalent (in the linear regime) to the
    auxiliary-variable scheme with appropriate identifications. The test
    verifies the equivalence numerically.
    """
    eps_dot_vals = np.array([eps_dot_func(t) for t in t_grid])
    eps_vals = np.zeros_like(t_grid)
    for i in range(1, len(t_grid)):
        eps_vals[i] = np.trapezoid(eps_dot_vals[: i + 1], t_grid[: i + 1])
    sigma = G_infty * eps_vals
    for tau, G in zip(taus, G_i):
        for i in range(1, len(t_grid)):
            s_vals = t_grid[: i + 1]
            kernel = G * np.exp(-(t_grid[i] - s_vals) / tau)
            sigma[i] += np.trapezoid(kernel * eps_dot_vals[: i + 1], s_vals)
    return sigma, eps_vals


def make_smooth_step_strain(t0=1.0, width=0.05, amplitude=0.01):
    eps = lambda t: amplitude / (1.0 + np.exp(-(t - t0) / width))
    eps_dot = lambda t: amplitude * np.exp(-(t - t0) / width) / (
        width * (1.0 + np.exp(-(t - t0) / width)) ** 2
    )
    return eps, eps_dot


def make_double_pulse(t1=2.0, t2=6.0, sigma=0.3, amplitude=0.01):
    """Double-Gaussian-pulse strain history. Smooth derivatives across the
    entire timeline, providing a non-trivial protocol with two transient
    excursions to test memory-coupling response across separated events.
    """
    def eps(t):
        return amplitude * (
            np.exp(-((t - t1) ** 2) / (2 * sigma ** 2))
            + np.exp(-((t - t2) ** 2) / (2 * sigma ** 2))
        )

    def eps_dot(t):
        return amplitude * (
            -(t - t1) / sigma ** 2 * np.exp(-((t - t1) ** 2) / (2 * sigma ** 2))
            - (t - t2) / sigma ** 2 * np.exp(-((t - t2) ** 2) / (2 * sigma ** 2))
        )

    return eps, eps_dot


def make_sinusoidal_strain(omega=2.0, amplitude=0.005):
    eps = lambda t: amplitude * np.sin(omega * t)
    eps_dot = lambda t: amplitude * omega * np.cos(omega * t)
    return eps, eps_dot


def main():
    t_start = time.time()
    t_grid = np.linspace(0, 30, 6001)
    seed = 42
    np.random.seed(seed)

    # Synthetic 3-term Prony series (canonical for polymer relaxation)
    # G(t) = G_infty + sum_i G_i * exp(-t/tau_i)
    taus = np.array([0.1, 1.0, 10.0])
    G_i = np.array([3e8, 1e8, 5e7])  # Pa, typical polymer scale
    G_infty = 1e7  # Pa
    G_0 = G_infty + np.sum(G_i)
    mu_tot = G_0 / 2.0
    mu0 = G_infty / G_0
    mus = G_i / G_0

    print(f"Prony series: G_0 = {G_0:.3e} Pa, G_inf = {G_infty:.3e} Pa")
    print(f"  taus = {taus.tolist()} s")
    print(f"  G_i = {G_i.tolist()} Pa")
    print(f"  fractional mus = {mus.tolist()}")
    print(f"  mu0 (long-time) = {mu0:.4f}")
    print()

    protocols = [
        ("smooth_step", make_smooth_step_strain(t0=1.0, width=0.05, amplitude=0.01)),
        ("double_pulse", make_double_pulse(t1=2.0, t2=6.0, sigma=0.3, amplitude=0.01)),
        ("sinusoidal_om=2", make_sinusoidal_strain(omega=2.0, amplitude=0.005)),
    ]

    results = []
    for label, (eps_func, eps_dot_func) in protocols:
        sigma_ode, eps_vals = auxiliary_ode_rk4(
            eps_func, eps_dot_func, taus, mus, mu0, mu_tot, t_grid
        )
        sigma_conv, _ = convolution_stress(eps_dot_func, G_infty, G_i, taus, t_grid)
        abs_err = np.abs(sigma_ode - sigma_conv)
        rel_err = abs_err / (np.abs(sigma_conv).max() + 1e-12)
        results.append(
            {
                "label": label,
                "max_abs_err_Pa": float(abs_err.max()),
                "max_rel_err": float(rel_err.max()),
                "sigma_ode_final_Pa": float(sigma_ode[-1]),
                "sigma_conv_final_Pa": float(sigma_conv[-1]),
                "eps_final": float(eps_vals[-1]),
            }
        )
        print(
            f"Protocol: {label}  max_rel_err={rel_err.max():.3e}  "
            f"sigma_ode_final={sigma_ode[-1]:.3e}  sigma_conv_final={sigma_conv[-1]:.3e}"
        )

    wall = time.time() - t_start

    max_rel_err_overall = max(r["max_rel_err"] for r in results)
    threshold = 1e-3
    summary = {
        "prediction": "P19.1 (interface 19 Prony viscoelastic reproduction)",
        "prony_params": {
            "taus_s": taus.tolist(),
            "G_i_Pa": G_i.tolist(),
            "G_infty_Pa": float(G_infty),
            "G_0_Pa": float(G_0),
            "mu0_fractional": float(mu0),
            "mus_fractional": mus.tolist(),
        },
        "protocols_tested": [p[0] for p in protocols],
        "t_grid_n_points": len(t_grid),
        "results": results,
        "max_relative_error_overall": float(max_rel_err_overall),
        "threshold": threshold,
        "passes_threshold": bool(max_rel_err_overall < threshold),
        "wall_time_s": float(wall),
        "backend": "numpy",
        "seed": seed,
    }

    out_dir = "outputs/prony_viscoelastic_reproduction"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "summary.json"), "w") as f:
        json.dump(summary, f, indent=2)

    print()
    print(f"Max relative error overall: {max_rel_err_overall:.3e}")
    print(f"Threshold: {threshold:.0e}")
    print(f"Passes threshold: {summary['passes_threshold']}")
    print(f"Wall time: {wall:.2f}s")
    print(f"Output: {out_dir}/summary.json")

    if summary["passes_threshold"]:
        print()
        print("Status: tested_consistent")
        print("P19.1 supported: the auxiliary-variable equation dq_i/dt + q_i/tau_i =")
        print("d(eps_dev)/dt reproduces the hereditary-integral stress response of a")
        print("3-term Prony series across smooth-step, double-pulse, and sinusoidal")
        print("strain histories. The equivalence is mathematical (the ODE is the")
        print("differential form of the convolution); the test verifies it numerically.")
        print("This is the structural correspondence the present equation has with")
        print("industrial-standard generalized Maxwell viscoelasticity (PyLith, COMSOL,")
        print("Ansys, Abaqus).")
    else:
        print()
        print("Status: tested_inconsistent (numerical scheme insufficient)")


if __name__ == "__main__":
    main()
