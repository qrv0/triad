# Physics solver

GPU-accelerated implementation of the memory-augmented nonlinear Schrödinger field equation on a 2D or 3D periodic lattice. The solver uses a Strang split-step integrator with the kinetic step evaluated in Fourier space via cuFFT.

## Files

| File | Content |
|---|---|
| `solver_3d.py` | The main 3D integrator. Exposes `SolverConfig3D` (parameters) and `run` (integration loop). |
| `kernels.py` | Memory kernel definitions, including local (delta) and spatially non-local (Gaussian, exponential) variants. |
| `observables.py` | Diagnostics: norm, peak, FWHM, IPR, radial power spectrum, crystallinity, Bravais lattice detection. |
| `precision.py` | Backend abstraction (cupy / numpy) and precision mode (fp64 / fp32 / fp16). |
| `sanity.py` | Conservation test suite. |
| `__init__.py` | Public API. |

## Usage

```python
from mnsm.implementation.physics import SolverConfig3D, MemoryConfig, run, make_default_observables

cfg = SolverConfig3D(
    N=128,                              # lattice size per dimension
    L=20.0,                             # box length
    dt=0.0025,                          # time step
    n_steps=4000,                       # integration length
    Lambda=-8.0,                        # nonlinear coupling
    init_sigma=0.5,                     # initial Gaussian width
    init_k0=(0.0, 0.0, 0.0),            # initial momentum (zero for collapse studies)
    memory=MemoryConfig(
        nus=[10.0, 0.5],
        lambdas=[3.0, 1.0],             # Sigma_lambda = 4.0, the 3D anti-collapse value
        spatial="local",
    ),
    gamma_0=0.0,                        # no dissipation
    T=0.0,                              # no noise
    precision="fp32",
    seed=42,
)

result = run(cfg, observables_fn=make_default_observables(cfg.L))
# result['psi_final'] is the final field
# result['samples'] is a list of dicts with observables at sampled timesteps
```

## Algorithm

Each time step decomposes into five substeps (the Strang split-step scheme):

1. **Half potential step in real space**: pointwise phase rotation by $\exp(-i V_{\text{tot}} dt/2)$, where $V_{\text{tot}} = \Lambda \rho + V_{\text{mem}}$. Unitary for real $V_{\text{tot}}$.
2. **Full kinetic step in momentum space**: pre-computed propagator $U_k = \exp(-i H_{\text{kin}}(\mathbf{k}) dt)$ applied via cuFFT 3D forward and inverse transforms.
3. **Half potential step in real space** with the density updated from step 2.
4. **OU update of auxiliary fields**: $y_j \leftarrow e^{-\nu_j dt} y_j + (1 - e^{-\nu_j dt}) \rho_{\text{eff}}$, exact analytical step for the multi-exponential memory kernel.
5. **Stochastic increment** (if $\Gamma > 0$ and $T > 0$): FDT-locked noise injection.

The leading splitting error is $O(dt^2)$.

## Validation

Run the sanity tests:

```bash
python -m mnsm.implementation.physics.sanity
```

Or, more typically, via the test suite:

```bash
pytest ../../tests/test_conservation.py
```

The tests verify norm conservation in unitary regimes, pure dissipative decay, FDT thermalization, and the supercritical-collapse signature.

## Performance

On NVIDIA RTX 4060 Laptop GPU (Ada Lovelace, 8 GB VRAM):

| Lattice | Per-step wall time (fp32) |
|---|---|
| $64^3$ | ~5 ms |
| $96^3$ | ~15 ms |
| $128^3$ | ~35 ms |
| $192^3$ | ~120 ms |

A typical production run (4000 steps at $128^3$) takes approximately 2.5 minutes. The full validation suite runs in under a minute.

## Where to find the results this code produces

- [`../../experiments/physics/`](../../experiments/physics/), Scripts that reproduce the paper figures.
- [`../../results/`](../../results/), Documentation of the numerical findings.
- [`../../tests/`](../../tests/), Validation tests.
