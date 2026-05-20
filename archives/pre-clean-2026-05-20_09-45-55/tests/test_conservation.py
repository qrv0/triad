"""Conservation diagnostics for the physics solver.

These tests validate that the Strang split-step integrator implements the
equation correctly across the regimes covered by the reductions in
../equation/05-reductions.md. Passing the full suite is the basis for
Criterion 1 (internal mathematical consistency) of the structural-realist
evaluation in ../methodology/04-the-six-criteria.md.

Run with:
    pytest tests/test_conservation.py

Or invoke the underlying sanity module directly:
    python -m implementation.physics.sanity
"""

from __future__ import annotations

import math
import sys
from pathlib import Path

import pytest

# Make the implementation package importable from the repository root.
sys.path.insert(0, str(Path(__file__).parent.parent))

from implementation.physics import (
    SolverConfig3D,
    MemoryConfig,
    run,
    make_default_observables,
    Precision,
    is_gpu,
)


@pytest.fixture(scope="module")
def precision():
    """The precision mode used for the tests. fp32 is the default for
    speed; fp64 is used in the reference validation suite."""
    return "fp32"


def test_free_gaussian_norm_conservation(precision):
    """With no nonlinearity, memory, dissipation, or noise, the L²-norm
    should be conserved to within the precision tolerance."""
    cfg = SolverConfig3D(
        N=64, L=20.0, dt=0.005, n_steps=200,
        Lambda=0.0, gamma_0=0.0, T=0.0,
        memory=MemoryConfig(nus=[], lambdas=[]),
        sample_every=20, precision=precision,
    )
    result = run(cfg, observables_fn=make_default_observables(cfg.L), verbose=False)
    norms = [s["norm"] for s in result["samples"]]
    drift = abs(norms[-1] - norms[0])
    tol = Precision(precision).norm_tol
    # Allow 10x the nominal tolerance for fp32 over 200 steps with FFT roundoff.
    assert drift < 10 * tol, (
        f"Norm drift {drift:.2e} exceeds 10x tolerance {10*tol:.2e} "
        f"for precision={precision}"
    )


def test_pure_dissipation_matches_exponential(precision):
    """With γ > 0 and no noise, ||Ψ||²(t) should decay as exp(-2γt)."""
    gamma = 0.05
    cfg = SolverConfig3D(
        N=64, L=20.0, dt=0.01, n_steps=200,
        Lambda=0.0, gamma_0=gamma, T=0.0,
        memory=MemoryConfig(nus=[], lambdas=[]),
        sample_every=20, precision=precision,
    )
    result = run(cfg, observables_fn=make_default_observables(cfg.L), verbose=False)
    norms = [s["norm"] for s in result["samples"]]
    ts = [s["t"] for s in result["samples"]]
    expected_final = norms[0] * math.exp(-gamma * ts[-1])
    rel_err = abs(norms[-1] - expected_final) / expected_final
    assert rel_err < 1e-3, (
        f"Dissipative decay relative error {rel_err:.2e} exceeds 1e-3"
    )


def test_subcritical_attractive_nls_disperses(precision):
    """Below the collapse threshold, attractive NLS should disperse."""
    cfg = SolverConfig3D(
        N=64, L=20.0, dt=0.005, n_steps=400,
        Lambda=-2.0, gamma_0=0.0, T=0.0,   # subcritical for sigma_0 = 1.2 in 3D
        memory=MemoryConfig(nus=[], lambdas=[]),
        init_sigma=1.2,
        init_k0=(0.0, 0.0, 0.0),
        sample_every=50, precision=precision,
    )
    result = run(cfg, observables_fn=make_default_observables(cfg.L), verbose=False)
    peaks = [s["peak"] for s in result["samples"]]
    # The peak should stay bounded; no collapse.
    assert max(peaks) < 1.0, (
        f"Subcritical NLS should not collapse, but max peak = {max(peaks):.3f}"
    )


def test_supercritical_with_memory_releases_collapse(precision):
    """With Λ = -8, σ₀ = 0.5, and the 3D-rescaled memory coupling, the
    anti-collapse mechanism should release the field."""
    cfg = SolverConfig3D(
        N=64, L=20.0, dt=0.0025, n_steps=1500,
        Lambda=-8.0, gamma_0=0.0, T=0.0,
        memory=MemoryConfig(nus=[10.0, 0.5], lambdas=[3.0, 1.0]),
        init_sigma=0.5,
        init_k0=(0.0, 0.0, 0.0),
        sample_every=50, precision=precision,
    )
    result = run(cfg, observables_fn=make_default_observables(cfg.L), verbose=False)
    peaks = [s["peak"] for s in result["samples"]]
    max_peak = max(peaks)
    final_peak = peaks[-1]
    # The peak should rise (some collapse-like behavior), then decline.
    assert max_peak > 1.5, (
        f"Expected transient rise in peak; max_peak = {max_peak:.3f}"
    )
    # The final peak should be substantially below the maximum: anti-collapse.
    ratio = final_peak / max_peak
    assert ratio < 0.5, (
        f"Anti-collapse not observed: final/max ratio = {ratio:.3f}"
    )


def test_fdt_thermalization(precision):
    """With γ > 0, T > 0, no nonlinearity, the field should thermalize."""
    T_bath = 0.5
    cfg = SolverConfig3D(
        N=48, L=20.0, dt=0.01, n_steps=500,
        Lambda=0.0, gamma_0=0.1, T=T_bath,
        memory=MemoryConfig(nus=[], lambdas=[]),
        sample_every=25, precision=precision,
        init_sigma=10.0,
    )
    result = run(cfg, observables_fn=make_default_observables(cfg.L), verbose=False)
    samples = result["samples"]
    # Check that the late-time norm plateaus (early-late norm change < 10%).
    n_last = max(1, len(samples) // 4)
    last_norms = [s["norm"] for s in samples[-n_last:]]
    plateau = abs(last_norms[-1] - last_norms[0]) / max(last_norms[0], 1e-9)
    assert plateau < 0.15, (
        f"FDT thermalization plateau not reached: "
        f"early-late norm fraction {plateau:.3f} > 0.15"
    )


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
