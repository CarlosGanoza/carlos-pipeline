#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT_DIR"

if [[ -d "$HOME/.local/bin" ]]; then
  export PATH="$HOME/.local/bin:$PATH"
fi
if [[ -z "${GRAPHVIZ_DOT:-}" && -x "$HOME/.local/bin/dot" ]]; then
  export GRAPHVIZ_DOT="$HOME/.local/bin/dot"
fi

# Fail closed for sensitive repositories: this wrapper enforces local-only inference.
export STRICT_LOCAL_ONLY="${STRICT_LOCAL_ONLY:-1}"
if [[ "${STRICT_LOCAL_ONLY}" != "1" ]]; then
  echo "❌ STRICT_LOCAL_ONLY must be 1 for ./run_agent.sh."
  echo "Run python3 agent.py directly only if you intentionally allow remote endpoints."
  exit 1
fi

export LLM_BACKEND="${LLM_BACKEND:-ollama}"
export OLLAMA_MODEL="${OLLAMA_MODEL:-qwen2.5-coder:7b}"
export OPENAI_BASE_URL="${OPENAI_BASE_URL:-http://127.0.0.1:8000/v1}"
export OPENAI_COMPATIBLE_MODEL="${OPENAI_COMPATIBLE_MODEL:-${OPENAI_MODEL:-local-model}}"
export OLLAMA_HTTP_TIMEOUT_SECONDS="${OLLAMA_HTTP_TIMEOUT_SECONDS:-900}"
export MAX_FILE_BYTES="${MAX_FILE_BYTES:-2097152}"
export STRICT_TRACEABILITY="${STRICT_TRACEABILITY:-1}"
export GROUNDING_PROFILE="${GROUNDING_PROFILE:-standard}"
export KEY_FILES_LIMIT="${KEY_FILES_LIMIT:-20}"
export DOC_DEFAULT_MODE="${DOC_DEFAULT_MODE:-deterministic}"
export LLM_OUTPUT_POLICY="${LLM_OUTPUT_POLICY:-strict_gate}"
case "${LLM_BACKEND}" in
  ollama)
    ;;
  openai_compatible|openai-compatible|openai)
    export LLM_BACKEND="openai_compatible"
    ;;
  *)
    echo "❌ Invalid LLM_BACKEND=${LLM_BACKEND}. Supported local backends: ollama, openai_compatible."
    exit 1
    ;;
esac

if [[ $# -eq 0 ]]; then
  echo "Usage examples:"
  echo "  (default for document is --mode ${DOC_DEFAULT_MODE})"
  echo "  ./run_agent.sh document --repo ./deepwiki-open"
  echo "  ./run_agent.sh document --repo ./deepwiki-open --goal \"auth and api\""
  echo "  STRICT_TRACEABILITY=1 KEY_FILES_LIMIT=0 ./run_agent.sh document --repo ./deepwiki-open --mode deterministic"
  echo "  ./run_agent.sh ask --question \"how many endpoints\" --fact-index outputs/fact_index.json"
  echo "  ./run_agent.sh compare-runs --base-run runs/run_x --head-run runs/run_y"
  echo "  ./run_agent.sh benchmark-models --repo ./deepwiki-open --models \"qwen2.5-coder:7b,qwen3-coder:30b\""
  exit 1
fi

ARGS=("$@")

if [[ "${#ARGS[@]}" -gt 0 ]]; then
  case "${ARGS[0]}" in
    document|ask|latest-summary|compare-runs|benchmark-models|-h|--help)
      ;;
    *)
      ARGS=("document" "${ARGS[@]}")
      ;;
  esac
fi

if [[ "${#ARGS[@]}" -gt 0 && "${ARGS[0]}" == "document" ]]; then
  HAS_MODE=0
  for token in "${ARGS[@]}"; do
    if [[ "${token}" == "--mode" || "${token}" == --mode=* ]]; then
      HAS_MODE=1
      break
    fi
  done
  if [[ "${HAS_MODE}" -eq 0 ]]; then
    ARGS+=("--mode" "${DOC_DEFAULT_MODE}")
    echo "[INFO] --mode not provided; defaulting to --mode ${DOC_DEFAULT_MODE} for stronger grounding."
  fi
fi

NEEDS_LLM=0
if [[ "${#ARGS[@]}" -gt 0 ]]; then
  case "${ARGS[0]}" in
    benchmark-models)
      NEEDS_LLM=1
      ;;
    document)
      EFFECTIVE_MODE="${DOC_DEFAULT_MODE}"
      NEXT_IS_MODE_VALUE=0
      for token in "${ARGS[@]:1}"; do
        if [[ "${NEXT_IS_MODE_VALUE}" -eq 1 ]]; then
          EFFECTIVE_MODE="${token}"
          NEXT_IS_MODE_VALUE=0
          continue
        fi
        if [[ "${token}" == "--mode" ]]; then
          NEXT_IS_MODE_VALUE=1
          continue
        fi
        if [[ "${token}" == --mode=* ]]; then
          EFFECTIVE_MODE="${token#--mode=}"
        fi
      done
      if [[ "${EFFECTIVE_MODE}" == "agent" ]]; then
        NEEDS_LLM=1
      fi
      ;;
  esac
fi

if [[ "${NEEDS_LLM}" -eq 1 ]]; then
  if [[ "${LLM_BACKEND}" == "ollama" ]]; then
    if ! command -v ollama >/dev/null 2>&1; then
      echo "❌ ollama CLI not found. Install Ollama first."
      exit 1
    fi

    if ! ollama list >/dev/null 2>&1; then
      echo "❌ Ollama server is not reachable."
      echo "Start Ollama app, or run: ollama serve"
      exit 1
    fi

    MODEL_LIST="$(ollama list)"
    if ! grep -q "^${OLLAMA_MODEL}" <<<"$MODEL_LIST"; then
      echo "[INFO] Pulling model ${OLLAMA_MODEL} (one-time download)..."
      ollama pull "${OLLAMA_MODEL}"
    fi
  else
    echo "[INFO] OpenAI-compatible local backend selected; health checks will run in Python against ${OPENAI_BASE_URL}."
  fi
else
  echo "[INFO] Selected command does not require live model access; skipping backend reachability checks."
fi

echo "[INFO] llm_backend=${LLM_BACKEND}"
if [[ "${LLM_BACKEND}" == "ollama" ]]; then
  echo "[INFO] ollama_model=${OLLAMA_MODEL}"
  case "${OLLAMA_MODEL}" in
    *14b*)
      echo "[WARN] qwen2.5-coder:14b is no longer the recommended default. Recent repo-side comparisons accepted 0 LLM sections, so prefer deterministic mode or choose a stronger model explicitly."
      ;;
    *30b*|*32b*|*70b*)
      echo "[WARN] Large local Ollama model selected; synthesis steps can take several minutes on a laptop. Keep OLLAMA_HTTP_TIMEOUT_SECONDS high."
      ;;
  esac
else
  echo "[INFO] openai_base_url=${OPENAI_BASE_URL}"
  echo "[INFO] openai_compatible_model=${OPENAI_COMPATIBLE_MODEL}"
fi
echo "[INFO] ollama_timeout_seconds=${OLLAMA_HTTP_TIMEOUT_SECONDS}"
echo "[INFO] max_file_bytes=${MAX_FILE_BYTES}"
echo "[INFO] strict_traceability=${STRICT_TRACEABILITY}"
echo "[INFO] grounding_profile=${GROUNDING_PROFILE}"
echo "[INFO] key_files_limit=${KEY_FILES_LIMIT}"
echo "[INFO] doc_default_mode=${DOC_DEFAULT_MODE}"
echo "[INFO] llm_output_policy=${LLM_OUTPUT_POLICY}"
echo "[INFO] Setup OK. Running local documentation agent..."

python3 -u agent.py "${ARGS[@]}"
