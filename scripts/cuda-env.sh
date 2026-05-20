#!/usr/bin/env bash
# Source this file before running CuPy FFT jobs when CUDA runtime libraries are
# installed from pip packages inside the local virtual environment.

set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
VENV="$ROOT/.venv"

if [[ ! -d "$VENV" ]]; then
  echo "Missing .venv at $VENV" >&2
  echo "Create it with: python -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt cupy-cuda12x nvidia-cufft-cu12 nvidia-cuda-runtime-cu12 nvidia-cublas-cu12" >&2
  return 1 2>/dev/null || exit 1
fi

source "$VENV/bin/activate"
CUDA_LIBS="$(python - <<'PY'
import glob
import site
paths = []
for base in site.getsitepackages():
    paths.extend(glob.glob(base + '/nvidia/*/lib'))
print(':'.join(paths))
PY
)"

export LD_LIBRARY_PATH="$CUDA_LIBS:${LD_LIBRARY_PATH:-}"
echo "Triad CUDA environment active."
python - <<'PY'
try:
    import cupy as cp
    props = cp.cuda.runtime.getDeviceProperties(0)
    name = props['name'].decode() if isinstance(props['name'], bytes) else props['name']
    print(f"CuPy {cp.__version__} on {name}")
except Exception as exc:
    print(f"CuPy check failed: {exc}")
PY
