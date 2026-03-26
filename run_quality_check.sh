#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT_DIR"

ARTIFACT_DIR="${QUALITY_ARTIFACT_DIR:-$ROOT_DIR/outputs/quality_check}"
EVALUATION_MANIFEST="${QUALITY_EVALUATION_MANIFEST:-$ROOT_DIR/evaluation_manifest.ci.json}"
PYCACHE_PREFIX="${QUALITY_PYCACHE_PREFIX:-/tmp/code-analyzer-pyc}"
RUN_TESTS=1
RUN_EVALUATION=1
SMOKE_REPO=""

while [[ $# -gt 0 ]]; do
  case "$1" in
    --artifact-dir)
      ARTIFACT_DIR="$2"
      shift 2
      ;;
    --evaluation-manifest)
      EVALUATION_MANIFEST="$2"
      shift 2
      ;;
    --repo)
      SMOKE_REPO="$2"
      shift 2
      ;;
    --skip-tests)
      RUN_TESTS=0
      shift
      ;;
    --skip-evaluation)
      RUN_EVALUATION=0
      shift
      ;;
    *)
      if [[ -z "$SMOKE_REPO" ]]; then
        SMOKE_REPO="$1"
        shift
      else
        echo "[ERROR] unexpected argument: $1" >&2
        exit 2
      fi
      ;;
  esac
done

mkdir -p "$ARTIFACT_DIR"

echo "[CHECK] shell syntax"
bash -n run_local.sh run_agent.sh run_governance_check.sh run_drift_check.sh run_release_readiness.sh

echo "[CHECK] python compile"
PYTHONPYCACHEPREFIX="$PYCACHE_PREFIX" python3 -m py_compile \
  main.py agent.py evaluation_harness.py \
  tests/test_grounding.py tests/test_agent.py tests/test_evaluation_harness.py

if [[ "$RUN_TESTS" -eq 1 ]]; then
  echo "[CHECK] unit tests"
  PYTHONPYCACHEPREFIX="$PYCACHE_PREFIX" python3 -m pytest -q
fi

if [[ "$RUN_EVALUATION" -eq 1 ]]; then
  if [[ ! -f "$EVALUATION_MANIFEST" ]]; then
    echo "[ERROR] evaluation manifest not found: $EVALUATION_MANIFEST" >&2
    exit 2
  fi
  echo "[CHECK] evaluation harness"
  cp "$EVALUATION_MANIFEST" "$ARTIFACT_DIR/evaluation.manifest.json"
  PYTHONPYCACHEPREFIX="$PYCACHE_PREFIX" python3 main.py \
    --evaluate-manifest "$EVALUATION_MANIFEST" \
    --evaluation-json "$ARTIFACT_DIR/evaluation.results.json" \
    --evaluation-md "$ARTIFACT_DIR/evaluation.results.md" \
    --benchmark-md "$ARTIFACT_DIR/evaluation.benchmark.md" \
    --benchmark-csv "$ARTIFACT_DIR/evaluation.benchmark.csv"
fi

if [[ -n "$SMOKE_REPO" ]]; then
  echo "[CHECK] deterministic pipeline smoke run for repo: $SMOKE_REPO"
  ./run_agent.sh document --repo "$SMOKE_REPO" --goal "architecture and dependencies" --mode deterministic >/dev/null
fi

echo "[INFO] artifacts: $ARTIFACT_DIR"
echo "[OK] quality checks passed"
