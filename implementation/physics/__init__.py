"""Physics solvers for Triad field simulations.

The package keeps two solver lines:

- `balanced_solver_3d`: current clean rebuild solver with explicit splitting and
  noise conventions.
- `reference_solver_3d`: historical Memory-NLS solver preserved from the origin
  path where the anti-collapse simulation first emerged.
"""

from .balanced_solver_3d import (
    BalancedSolverConfig3D,
    build_initial_state,
    default_observables,
    run,
    step,
)
from .kernels import MemoryConfig, apply_spatial_kernel, build_spatial_kernel_fft_3d
from .precision import Precision, get_backend, is_gpu, to_cpu, vram_estimate

__all__ = [
    "BalancedSolverConfig3D",
    "build_initial_state",
    "default_observables",
    "run",
    "step",
    "MemoryConfig",
    "apply_spatial_kernel",
    "build_spatial_kernel_fft_3d",
    "Precision",
    "get_backend",
    "is_gpu",
    "to_cpu",
    "vram_estimate",
]
