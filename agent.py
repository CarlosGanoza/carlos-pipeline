import argparse
import json
import os
import re
import shutil
import sys
import time
import hashlib
import subprocess
import traceback
from datetime import datetime, timezone
from typing import Optional, Any, Callable

import main as analyzer

SYSTEM_PROMPT = (
    "You MUST reply in ENGLISH only. "
    "If you see Chinese, translate it internally and output only English. "
    "Do not output any Chinese characters."
)

MERMAID_TEMPLATE = """```mermaid
graph TD

subgraph Frontend
FE[Frontend]
NX[Next js]
RE[React]
FE --> NX --> RE
end

subgraph Backend
BE[Backend]
PY[Python API]
NO[Node js Server]
BE --> PY --> NO
end

subgraph Infrastructure
DO[Docker Container]
LC[Local Cloud]
DO --> LC
end

subgraph AI
OL[Ollama Models]
EG[Embedding and Generation]
OL --> EG
end

subgraph Output
UI[User Interface]
DG[Documentation Generation]
UI --> DG
end

FE --> BE
BE --> DO
BE --> OL
DG --> UI
```"""

STATE_FILENAME = "state.json"
FAILURE_FILENAME = "failure.json"
GATHER_CHECKPOINT_FILENAME = "gather_checkpoint.json"
SYNTHESIS_CHECKPOINT_FILENAME = "synthesis_checkpoint.json"
RUN_LOCK_FILENAME = "run.lock.json"
HEARTBEAT_FILENAME = "heartbeat.json"
FILE_WRITE_RETRIES = 3
FILE_WRITE_RETRY_BACKOFF_SECONDS = 0.1
RUN_HEARTBEAT_STALE_SECONDS = 300.0
RESUMABLE_RUN_STATUSES = {"running", "error", "failed_security_policy", "failed_gate"}


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def ensure_dir(path: str) -> None:
    os.makedirs(path, exist_ok=True)


def print_saved_if_exists(path: str) -> None:
    target = str(path or "").strip()
    if target and os.path.exists(target):
        print(f"[SAVED] {target}")


def write_json(path: str, data: dict[str, Any]) -> None:
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    last_error: Optional[Exception] = None
    for attempt in range(1, FILE_WRITE_RETRIES + 1):
        tmp = f"{path}.tmp.{os.getpid()}.{attempt}"
        try:
            with open(tmp, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=True, indent=2)
            os.replace(tmp, path)
            return
        except Exception as e:
            last_error = e
            try:
                if os.path.exists(tmp):
                    os.remove(tmp)
            except Exception:
                pass
            if attempt >= FILE_WRITE_RETRIES:
                break
            time.sleep(FILE_WRITE_RETRY_BACKOFF_SECONDS * attempt)
    if last_error:
        raise last_error


def write_text(path: str, text: str) -> None:
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    last_error: Optional[Exception] = None
    for attempt in range(1, FILE_WRITE_RETRIES + 1):
        tmp = f"{path}.tmp.{os.getpid()}.{attempt}"
        try:
            with open(tmp, "w", encoding="utf-8") as f:
                f.write(text)
            os.replace(tmp, path)
            return
        except Exception as e:
            last_error = e
            try:
                if os.path.exists(tmp):
                    os.remove(tmp)
            except Exception:
                pass
            if attempt >= FILE_WRITE_RETRIES:
                break
            time.sleep(FILE_WRITE_RETRY_BACKOFF_SECONDS * attempt)
    if last_error:
        raise last_error


def make_run_dir(runs_dir: str) -> tuple[str, str]:
    ensure_dir(runs_dir)
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    base_run_id = f"run_{stamp}"
    run_id = base_run_id
    run_path = os.path.join(runs_dir, run_id)
    idx = 1
    while os.path.exists(run_path):
        run_id = f"{base_run_id}_{idx}"
        run_path = os.path.join(runs_dir, run_id)
        idx += 1
    ensure_dir(run_path)
    return run_id, run_path


def add_event(state: dict[str, Any], stage: str, message: str, data: Optional[dict[str, Any]] = None) -> None:
    event = {"ts": utc_now_iso(), "stage": stage, "message": message}
    if data:
        event["data"] = data
    state.setdefault("events", []).append(event)


def save_state(run_path: str, state: dict[str, Any]) -> None:
    write_json(os.path.join(run_path, STATE_FILENAME), state)
    write_heartbeat(run_path, state)


def safe_save_state(run_path: str, state: dict[str, Any]) -> str:
    try:
        save_state(run_path, state)
        return ""
    except Exception as e:
        return str(e)


def read_json(path: str) -> Optional[dict[str, Any]]:
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        if isinstance(data, dict):
            return data
    except Exception:
        return None
    return None


def load_run_state(run_path: str) -> Optional[dict[str, Any]]:
    return read_json(os.path.join(run_path, STATE_FILENAME))


def ensure_run_state_defaults(state: dict[str, Any], *, repo_path: str, requested_mode: str, effective_mode: str) -> dict[str, Any]:
    state.setdefault("run_id", os.path.basename(repo_path))
    state.setdefault("started_at", utc_now_iso())
    state.setdefault("completed_at", None)
    state.setdefault("status", "running")
    state.setdefault("requested_mode", requested_mode)
    state.setdefault("mode", effective_mode)
    state.setdefault("repo_path", repo_path)
    state.setdefault("repo_metadata", {})
    state.setdefault("backend", analyzer.LLM_BACKEND)
    state.setdefault("model", analyzer.active_model() if effective_mode == "agent" else "deterministic_only")
    state.setdefault("max_iterations", 1)
    state.setdefault("events", [])
    state.setdefault("artifacts", {})
    state.setdefault("attempt_count", 1)
    state.setdefault("resume_count", 0)
    state.setdefault("current_stage", "plan")
    return state


def resolve_resume_run_path(runs_dir: str, resume_run: str) -> str:
    raw = str(resume_run or "").strip()
    if not raw:
        return ""
    expanded = os.path.abspath(os.path.expanduser(raw))
    if os.path.isdir(expanded):
        return expanded
    candidate = os.path.join(os.path.abspath(os.path.expanduser(runs_dir)), raw)
    if os.path.isdir(candidate):
        return candidate
    return ""


def _parse_iso_timestamp(value: str) -> Optional[datetime]:
    text = str(value or "").strip()
    if not text:
        return None
    try:
        return datetime.fromisoformat(text.replace("Z", "+00:00"))
    except Exception:
        return None


def load_heartbeat(run_path: str) -> Optional[dict[str, Any]]:
    return read_json(os.path.join(run_path, HEARTBEAT_FILENAME))


def write_heartbeat(run_path: str, state: dict[str, Any]) -> str:
    path = os.path.join(run_path, HEARTBEAT_FILENAME)
    payload = {
        "ts": utc_now_iso(),
        "status": str(state.get("status", "")).strip(),
        "current_stage": str(state.get("current_stage", "")).strip(),
        "attempt_count": int(state.get("attempt_count", 1) or 1),
        "run_id": str(state.get("run_id", "")).strip(),
        "pid": os.getpid(),
    }
    write_json(path, payload)
    return path


def _heartbeat_is_stale(heartbeat: Optional[dict[str, Any]], stale_seconds: float = RUN_HEARTBEAT_STALE_SECONDS) -> bool:
    if not isinstance(heartbeat, dict):
        return True
    ts = _parse_iso_timestamp(str(heartbeat.get("ts", "")).strip())
    if ts is None:
        return True
    return (datetime.now(timezone.utc) - ts.astimezone(timezone.utc)).total_seconds() > stale_seconds


def _run_lock_is_stale(
    lock_payload: Optional[dict[str, Any]],
    heartbeat: Optional[dict[str, Any]],
    stale_seconds: float = RUN_HEARTBEAT_STALE_SECONDS,
) -> bool:
    if isinstance(heartbeat, dict) and not _heartbeat_is_stale(heartbeat, stale_seconds=stale_seconds):
        return False
    if not isinstance(lock_payload, dict):
        return True
    ts = _parse_iso_timestamp(str(lock_payload.get("ts", "")).strip())
    if ts is None:
        return True
    return (datetime.now(timezone.utc) - ts.astimezone(timezone.utc)).total_seconds() > stale_seconds


def _write_lock_file_exclusive(path: str, payload: dict[str, Any]) -> None:
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    fd = os.open(path, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o644)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            json.dump(payload, f, ensure_ascii=True, indent=2)
    except Exception:
        try:
            os.remove(path)
        except Exception:
            pass
        raise


def acquire_run_lock(run_path: str, *, run_id: str, attempt_count: int) -> dict[str, Any]:
    lock_path = os.path.join(run_path, RUN_LOCK_FILENAME)
    stale_reclaimed = False
    while True:
        payload = {
            "ts": utc_now_iso(),
            "run_id": run_id,
            "pid": os.getpid(),
            "attempt_count": int(attempt_count),
            "stale_reclaimed": stale_reclaimed,
        }
        try:
            _write_lock_file_exclusive(lock_path, payload)
            return payload
        except FileExistsError:
            existing_lock = read_json(lock_path)
            heartbeat = load_heartbeat(run_path)
            if not _run_lock_is_stale(existing_lock, heartbeat):
                owner_pid = existing_lock.get("pid", "unknown") if isinstance(existing_lock, dict) else "unknown"
                owner_stage = heartbeat.get("current_stage", "unknown") if isinstance(heartbeat, dict) else "unknown"
                raise RuntimeError(f"Run is already active in {run_path} pid={owner_pid} stage={owner_stage}")
            try:
                os.remove(lock_path)
            except FileNotFoundError:
                continue
            stale_reclaimed = True


def release_run_lock(run_path: str) -> None:
    path = os.path.join(run_path, RUN_LOCK_FILENAME)
    try:
        if os.path.exists(path):
            os.remove(path)
    except Exception:
        pass


def write_failure_artifact(
    run_path: str,
    *,
    run_id: str,
    repo_path: str,
    stage: str,
    status: str,
    error: str,
    tb_text: str,
    resumable: bool,
    attempt_count: int,
) -> str:
    path = os.path.join(run_path, FAILURE_FILENAME)
    payload = {
        "ts": utc_now_iso(),
        "run_id": run_id,
        "repo_path": repo_path,
        "stage": stage,
        "status": status,
        "error": error,
        "traceback": tb_text,
        "resumable": resumable,
        "attempt_count": int(attempt_count),
    }
    write_json(path, payload)
    return path


def clear_failure_artifact(run_path: str) -> None:
    path = os.path.join(run_path, FAILURE_FILENAME)
    try:
        if os.path.exists(path):
            os.remove(path)
    except Exception:
        pass


def save_gather_checkpoint(run_path: str, payload: dict[str, Any]) -> str:
    path = os.path.join(run_path, GATHER_CHECKPOINT_FILENAME)
    write_json(path, payload)
    return path


def load_gather_checkpoint(run_path: str) -> Optional[dict[str, Any]]:
    return read_json(os.path.join(run_path, GATHER_CHECKPOINT_FILENAME))


def save_synthesis_checkpoint(run_path: str, payload: dict[str, Any]) -> str:
    path = os.path.join(run_path, SYNTHESIS_CHECKPOINT_FILENAME)
    write_json(path, payload)
    return path


def load_synthesis_checkpoint(run_path: str) -> Optional[dict[str, Any]]:
    return read_json(os.path.join(run_path, SYNTHESIS_CHECKPOINT_FILENAME))


def _artifact_json(state: dict[str, Any], key: str) -> Optional[dict[str, Any]]:
    path = str(state.get("artifacts", {}).get(key, "")).strip()
    if not path or not os.path.isfile(path):
        return None
    return read_json(path)


def _artifact_text(state: dict[str, Any], key: str) -> str:
    path = str(state.get("artifacts", {}).get(key, "")).strip()
    if not path or not os.path.isfile(path):
        return ""
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception:
        return ""


def load_gather_resume_context(run_path: str) -> Optional[dict[str, Any]]:
    checkpoint = load_gather_checkpoint(run_path)
    if not isinstance(checkpoint, dict):
        return None
    artifacts = checkpoint.get("artifacts", {})
    if not isinstance(artifacts, dict):
        return None

    required_json_keys = [
        "run_fact_index",
        "run_model_safe_fact_index",
        "run_prompt_fact_context",
        "run_claim_support_index",
    ]
    loaded: dict[str, Any] = {}
    for key in required_json_keys:
        path = str(artifacts.get(key, "")).strip()
        if not path or not os.path.isfile(path):
            return None
        payload = read_json(path)
        if not isinstance(payload, dict):
            return None
        loaded[key] = payload

    included_files = set([str(p).replace("\\", "/") for p in checkpoint.get("included_files", []) if str(p).strip()])
    line_counts_raw = checkpoint.get("line_counts", {})
    line_counts = {}
    if isinstance(line_counts_raw, dict):
        for path, count in line_counts_raw.items():
            try:
                line_counts[str(path).replace("\\", "/")] = int(count)
            except Exception:
                continue
    redaction_stats = checkpoint.get("redaction_stats", {})
    fact_index_cache_stats = checkpoint.get("fact_index_cache_stats", {})
    runtime_config = checkpoint.get("runtime_config", {})
    repo_fingerprint = str(checkpoint.get("repo_fingerprint", "")).strip()
    if not included_files or not line_counts or not isinstance(redaction_stats, dict) or not isinstance(fact_index_cache_stats, dict):
        return None

    return {
        "repo_fingerprint": repo_fingerprint,
        "included_files": included_files,
        "line_counts": line_counts,
        "redaction_stats": redaction_stats,
        "fact_index_cache_stats": fact_index_cache_stats,
        "runtime_config": runtime_config if isinstance(runtime_config, dict) else {},
        "fact_index": loaded["run_fact_index"],
        "model_safe_fact_index": loaded["run_model_safe_fact_index"],
        "prompt_fact_context": loaded["run_prompt_fact_context"],
        "claim_support_index": loaded["run_claim_support_index"],
    }


def load_synthesis_resume_context(run_path: str) -> Optional[dict[str, Any]]:
    checkpoint = load_synthesis_checkpoint(run_path)
    if not isinstance(checkpoint, dict):
        return None
    required = ["final_text", "final_validation", "final_gate", "source"]
    for key in required:
        if key not in checkpoint:
            return None
    if not isinstance(checkpoint.get("final_validation"), dict):
        return None
    if not isinstance(checkpoint.get("final_gate"), dict):
        return None
    return checkpoint


def _run_cmd(cmd: list[str], cwd: Optional[str] = None) -> tuple[int, str, str]:
    try:
        proc = subprocess.run(
            cmd,
            cwd=cwd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding="utf-8",
            errors="ignore",
            check=False,
        )
        return proc.returncode, proc.stdout.strip(), proc.stderr.strip()
    except Exception as e:
        return 1, "", str(e)


def get_repo_metadata(repo_path: str) -> dict[str, Any]:
    repo_abs = os.path.abspath(os.path.expanduser(repo_path))
    meta = {
        "repo_path": repo_abs,
        "git": {
            "is_git_repo": False,
            "commit": "",
            "branch": "",
            "dirty": None,
        },
    }
    rc, out, _ = _run_cmd(["git", "-C", repo_abs, "rev-parse", "--is-inside-work-tree"])
    if rc != 0 or out.strip().lower() != "true":
        return meta

    meta["git"]["is_git_repo"] = True
    rc, out, _ = _run_cmd(["git", "-C", repo_abs, "rev-parse", "HEAD"])
    if rc == 0 and out:
        meta["git"]["commit"] = out.splitlines()[0].strip()

    rc, out, _ = _run_cmd(["git", "-C", repo_abs, "rev-parse", "--abbrev-ref", "HEAD"])
    if rc == 0 and out:
        meta["git"]["branch"] = out.splitlines()[0].strip()

    rc, out, _ = _run_cmd(["git", "-C", repo_abs, "status", "--porcelain", "--untracked-files=no"])
    if rc == 0:
        meta["git"]["dirty"] = bool(out.strip())
    return meta


def compute_repo_fingerprint(included_files: set[str], line_counts: dict[str, int]) -> str:
    h = hashlib.sha256()
    for rel in sorted([p.replace("\\", "/") for p in included_files]):
        h.update(rel.encode("utf-8"))
        h.update(b":")
        h.update(str(int(line_counts.get(rel, 0))).encode("utf-8"))
        h.update(b"\n")
    return h.hexdigest()


def normalize_repo_path_value(path: str) -> str:
    return os.path.abspath(os.path.expanduser(path)).replace("\\", "/")


def evidence_to_path(evidence: str) -> str:
    s = str(evidence or "").strip()
    if "#L" in s:
        return s.split("#L", 1)[0]
    return s


def file_subsystem(path: str) -> str:
    return analyzer.derive_subsystem_name(path)


def safe_slug(name: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9_-]+", "_", name.strip())
    slug = slug.strip("_")
    return slug or "root"


def _filter_items_by_subsystem(items: list[dict[str, Any]], subsystem: str, file_key: str = "file") -> list[dict[str, Any]]:
    out = []
    for item in items:
        source_path = str(item.get("source_file", "")).replace("\\", "/")
        if file_key == "file" and source_path:
            path = source_path
        else:
            path = str(item.get(file_key, "")).replace("\\", "/")
        if not path:
            ev_path = evidence_to_path(str(item.get("source_evidence", "") or item.get("evidence", "")))
            path = ev_path
        if file_subsystem(path) == subsystem:
            out.append(item)
    return out


def build_subsystem_summary_map(fact_index: dict[str, Any]) -> dict[str, dict[str, Any]]:
    files = fact_index.get("files", [])
    endpoints = fact_index.get("api_endpoints", [])
    dependencies = fact_index.get("dependencies", [])
    scripts = fact_index.get("scripts", [])
    entrypoints = fact_index.get("entrypoints", [])
    infra = fact_index.get("infrastructure", [])
    ai = fact_index.get("ai_signals", [])
    sql_entities = fact_index.get("sql_entities", [])
    sql_queries = fact_index.get("sql_queries", [])
    language_symbols = fact_index.get("language_symbols", [])
    cross_file_symbol_edges = fact_index.get("cross_file_symbol_edges", [])
    cross_file_event_edges = fact_index.get("cross_file_event_edges", [])
    runtime_observations = fact_index.get("runtime_observations", [])

    subsystems: dict[str, dict[str, Any]] = {}
    for f in files:
        path = str(f.get("path", "")).replace("\\", "/")
        if not path:
            continue
        sub = file_subsystem(path)
        data = subsystems.setdefault(
            sub,
            {
                "files": [],
                "endpoints": [],
                "dependencies": [],
                "scripts": [],
                "entrypoints": [],
                "infrastructure": [],
                "ai_signals": [],
                "sql_entities": [],
                "sql_queries": [],
                "language_symbols": [],
                "cross_file_symbol_edges": [],
                "cross_file_event_edges": [],
                "runtime_observations": [],
                "languages": {},
            },
        )
        data["files"].append({"path": path, "line_count": int(f.get("line_count", 1) or 1)})
        lang = analyzer.infer_language(path)
        data["languages"][lang] = data["languages"].get(lang, 0) + 1

    for sub, data in subsystems.items():
        data["endpoints"] = _filter_items_by_subsystem(endpoints, sub)
        analyzer.annotate_api_endpoint_provenance(data["endpoints"])
        data["dependencies"] = _filter_items_by_subsystem(dependencies, sub)
        data["scripts"] = _filter_items_by_subsystem(scripts, sub)
        data["entrypoints"] = _filter_items_by_subsystem(entrypoints, sub)
        data["infrastructure"] = _filter_items_by_subsystem(infra, sub)
        data["ai_signals"] = _filter_items_by_subsystem(ai, sub)
        data["sql_entities"] = _filter_items_by_subsystem(sql_entities, sub)
        data["sql_queries"] = _filter_items_by_subsystem(sql_queries, sub)
        data["language_symbols"] = _filter_items_by_subsystem(language_symbols, sub)
        data["cross_file_symbol_edges"] = _filter_items_by_subsystem(cross_file_symbol_edges, sub, file_key="source_file")
        data["cross_file_event_edges"] = _filter_items_by_subsystem(cross_file_event_edges, sub, file_key="source_file")
        data["runtime_observations"] = _filter_items_by_subsystem(runtime_observations, sub)
        data["endpoint_verification"] = analyzer._runtime_endpoint_verification_counts({"api_endpoints": data["endpoints"]})
        data["endpoint_quality"] = analyzer.summarize_endpoint_quality_for_endpoints(data["endpoints"])
    return subsystems


def render_subsystem_markdown(name: str, data: dict[str, Any], max_list_items: int = 20) -> str:
    files = data.get("files", [])
    endpoints = data.get("endpoints", [])
    dependencies = data.get("dependencies", [])
    scripts = data.get("scripts", [])
    entrypoints = data.get("entrypoints", [])
    infra = data.get("infrastructure", [])
    ai = data.get("ai_signals", [])
    sql_entities = data.get("sql_entities", [])
    sql_queries = data.get("sql_queries", [])
    language_symbols = data.get("language_symbols", [])
    cross_file_symbol_edges = data.get("cross_file_symbol_edges", [])
    cross_file_event_edges = data.get("cross_file_event_edges", [])
    runtime_observations = data.get("runtime_observations", [])
    languages = data.get("languages", {})
    endpoint_verification = data.get("endpoint_verification", {})
    endpoint_quality = data.get("endpoint_quality", {})
    first_ev = f"{files[0]['path']}#L1" if files else "none"
    langs = ", ".join([f"{k}:{v}" for k, v in sorted(languages.items(), key=lambda x: (-x[1], x[0]))[:8]]) if languages else "Unknown"
    verified_count = int(endpoint_verification.get("verified", 0) or 0)
    static_only_count = int(endpoint_verification.get("static_only", 0) or 0)
    total_endpoint_count = max(0, int(endpoint_verification.get("total", len(endpoints)) or len(endpoints)))
    verification_pct = (float(verified_count) / float(total_endpoint_count) * 100.0) if total_endpoint_count > 0 else 0.0
    provenance_counts = endpoint_quality.get("provenance_counts", {}) if isinstance(endpoint_quality.get("provenance_counts", {}), dict) else {}
    confidence_counts = endpoint_quality.get("confidence_counts", {}) if isinstance(endpoint_quality.get("confidence_counts", {}), dict) else {}
    contract_spec_endpoints = int(endpoint_quality.get("contract_spec_endpoints", 0) or 0)
    linked_contract_spec_endpoints = int(endpoint_quality.get("linked_contract_spec_endpoints", 0) or 0)
    contract_backed_endpoints = int(endpoint_quality.get("contract_backed_endpoints", 0) or 0)
    implementation_endpoints = int(endpoint_quality.get("implementation_endpoints", 0) or 0)

    lines = [
        f"# Subsystem: {name}",
        "",
        "## Summary",
        f"- Files in subsystem: {len(files)}. [Evidence: {first_ev}]",
        f"- Languages: {langs}. [Evidence: {first_ev}]",
        f"- Endpoints detected: {len(endpoints)}. [Evidence: {endpoints[0]['evidence'] if endpoints else first_ev}]",
        f"- Endpoint verification coverage: {verification_pct:.1f}% ({verified_count}/{total_endpoint_count} runtime-verified, {static_only_count} static-only). [Evidence: {endpoints[0].get('verification_evidence', endpoints[0].get('evidence', first_ev)) if endpoints else first_ev}]",
        f"- Endpoint confidence mix: high={int(confidence_counts.get('high', 0) or 0)}, medium={int(confidence_counts.get('medium', 0) or 0)}, low={int(confidence_counts.get('low', 0) or 0)}. [Evidence: {endpoints[0].get('evidence', first_ev) if endpoints else first_ev}]",
        f"- Endpoint provenance mix: static_parse={int(provenance_counts.get('static_parse', 0) or 0)}, cross_file_inference={int(provenance_counts.get('cross_file_inference', 0) or 0)}, runtime_observation={int(provenance_counts.get('runtime_observation', 0) or 0)}. [Evidence: {endpoints[0].get('evidence', first_ev) if endpoints else first_ev}]",
        f"- Contract linkage: specs={contract_spec_endpoints}, linked_specs={linked_contract_spec_endpoints}, contract_backed={contract_backed_endpoints}/{implementation_endpoints}. [Evidence: {endpoints[0].get('linked_implementation_evidence', endpoints[0].get('evidence', first_ev)) if endpoints else first_ev}]",
        f"- Dependencies detected: {len(dependencies)}. [Evidence: {dependencies[0]['evidence'] if dependencies else first_ev}]",
        f"- Scripts detected: {len(scripts)}. [Evidence: {scripts[0]['evidence'] if scripts else first_ev}]",
        f"- Cross-language symbols detected: {len(language_symbols)}. [Evidence: {language_symbols[0]['evidence'] if language_symbols else first_ev}]",
        f"- Cross-file symbol edges detected: {len(cross_file_symbol_edges)}. [Evidence: {cross_file_symbol_edges[0]['evidence'] if cross_file_symbol_edges else first_ev}]",
        f"- Cross-file event edges detected: {len(cross_file_event_edges)}. [Evidence: {(cross_file_event_edges[0].get('source_evidence') or cross_file_event_edges[0].get('evidence', first_ev)) if cross_file_event_edges else first_ev}]",
        f"- Runtime observations linked to subsystem: {len(runtime_observations)}. [Evidence: {runtime_observations[0]['evidence'] if runtime_observations else first_ev}]",
        "",
        "## Files",
    ]
    if files:
        for item in files[:max_list_items]:
            lines.append(f"- `{item['path']}` line_count={item['line_count']}. [Evidence: {item['path']}#L1]")
    else:
        lines.append("- Unknown from provided code. [Evidence: none]")

    lines.append("")
    lines.append("## Endpoints")
    if endpoints:
        for item in endpoints[:max_list_items]:
            lines.append(
                f"- {item.get('method', 'GET')} {item.get('route', '/')} in {item.get('file', 'unknown')} "
                f"verification={item.get('verification_status', 'unknown')} strategy={item.get('verification_strategy', 'n/a')} "
                f"provenance={item.get('provenance_primary', 'unknown')} confidence={item.get('confidence', 'unknown')} "
                f"contract={'spec' if item.get('contract_spec') else ('backed' if item.get('contract_backed') else 'none')}. "
                f"[Evidence: {item.get('evidence', 'none')}]"
            )
    else:
        lines.append("- Unknown from provided code. [Evidence: none]")

    lines.append("")
    lines.append("## Dependencies")
    if dependencies:
        for item in dependencies[:max_list_items]:
            lines.append(f"- {item.get('name', 'unknown')} {item.get('version', 'unknown')}. [Evidence: {item.get('evidence', 'none')}]")
    else:
        lines.append("- Unknown from provided code. [Evidence: none]")

    lines.append("")
    lines.append("## Entry Signals")
    if entrypoints:
        for item in entrypoints[:max_list_items]:
            lines.append(f"- {item.get('kind', 'entrypoint')} in {item.get('file', 'unknown')}. [Evidence: {item.get('evidence', 'none')}]")
    else:
        lines.append("- Unknown from provided code. [Evidence: none]")

    lines.append("")
    lines.append("## Infrastructure and AI Signals")
    if infra:
        for item in infra[:max_list_items]:
            lines.append(f"- Infra {item.get('type', 'signal')} in {item.get('file', 'unknown')}. [Evidence: {item.get('evidence', 'none')}]")
    if ai:
        for item in ai[:max_list_items]:
            lines.append(f"- AI signal {item.get('name', 'unknown')}. [Evidence: {item.get('evidence', 'none')}]")
    if not infra and not ai:
        lines.append("- Unknown from provided code. [Evidence: none]")
    lines.append("")

    lines.append("## Data Layer")
    if sql_entities:
        for item in sql_entities[:max_list_items]:
            lines.append(
                f"- SQL entity {item.get('kind', 'entity')} {item.get('name', 'unknown')} in {item.get('file', 'unknown')}. "
                f"[Evidence: {item.get('evidence', 'none')}]"
            )
    if sql_queries:
        for item in sql_queries[:max_list_items]:
            lines.append(
                f"- SQL query {item.get('kind', 'query')} target {item.get('target', 'unknown')} in {item.get('file', 'unknown')}. "
                f"[Evidence: {item.get('evidence', 'none')}]"
            )
    if not sql_entities and not sql_queries:
        lines.append("- Unknown from provided code. [Evidence: none]")
    lines.append("")

    lines.append("## Cross-language Symbols")
    if language_symbols:
        for item in language_symbols[:max_list_items]:
            lines.append(
                f"- {item.get('language', 'code')} {item.get('kind', 'symbol')} {item.get('qualname', 'unknown')} in {item.get('file', 'unknown')}. "
                f"[Evidence: {item.get('evidence', 'none')}]"
            )
    else:
        lines.append("- Unknown from provided code. [Evidence: none]")
    lines.append("")

    lines.append("## Cross-file Symbol Graph")
    if cross_file_symbol_edges:
        for item in cross_file_symbol_edges[:max_list_items]:
            lines.append(
                f"- {item.get('source_symbol', 'unknown')} -> {item.get('target_symbol', 'unknown')} "
                f"target_file={item.get('target_file', 'unknown')} resolution={item.get('resolution', 'unknown')}. "
                f"[Evidence: {item.get('evidence', 'none')}]"
            )
    else:
        lines.append("- Unknown from provided code. [Evidence: none]")
    lines.append("")

    lines.append("## Cross-file Event Graph")
    if cross_file_event_edges:
        for item in cross_file_event_edges[:max_list_items]:
            lines.append(
                f"- {item.get('transport', 'event')} channel={item.get('channel', 'unknown')} "
                f"source={item.get('source_file', 'unknown')} target={item.get('target_file', 'unknown')} "
                f"resolution={item.get('resolution', 'unknown')}. "
                f"[Evidence: {item.get('source_evidence', item.get('evidence', 'none'))}]"
            )
    else:
        lines.append("- Unknown from provided code. [Evidence: none]")
    lines.append("")

    lines.append("## Runtime Observations")
    if runtime_observations:
        for item in runtime_observations[:max_list_items]:
            lines.append(
                f"- {item.get('kind', 'runtime_observation')} {item.get('summary', 'unknown')} via {item.get('command', 'unknown')}. "
                f"[Evidence: {item.get('evidence', 'none')}]"
            )
    else:
        lines.append("- Unknown from provided code. [Evidence: none]")
    lines.append("")
    return "\n".join(lines)


def write_subsystem_artifacts(fact_index: dict[str, Any], out_dir: str) -> dict[str, Any]:
    ensure_dir(out_dir)
    subsystems = build_subsystem_summary_map(fact_index)
    index_lines = ["# Subsystem Documentation Index", ""]
    doc_paths: list[str] = []

    for name in sorted(subsystems.keys()):
        data = subsystems[name]
        filename = f"{safe_slug(name)}.md"
        path = os.path.join(out_dir, filename)
        write_text(path, render_subsystem_markdown(name, data))
        doc_paths.append(path)
        index_lines.append(
            f"- `{name}`: files={len(data.get('files', []))}, endpoints={len(data.get('endpoints', []))}, "
            f"runtime_verified={data.get('endpoint_verification', {}).get('verified', 0)}, "
            f"verification_pct={((float(data.get('endpoint_verification', {}).get('verified', 0)) / float(max(1, data.get('endpoint_verification', {}).get('total', 0) or 1))) * 100.0) if data.get('endpoints', []) else 0.0:.1f}%, "
            f"high_conf_pct={(float(data.get('endpoint_quality', {}).get('high_confidence_endpoint_rate', 0.0) or 0.0) * 100.0):.1f}%, "
            f"contract_specs={data.get('endpoint_quality', {}).get('contract_spec_endpoints', 0)}, "
            f"contract_backed={data.get('endpoint_quality', {}).get('contract_backed_endpoints', 0)}, "
            f"cross_file={data.get('endpoint_quality', {}).get('cross_file_inference_endpoints', 0)}, "
            f"dependencies={len(data.get('dependencies', []))}, scripts={len(data.get('scripts', []))}"
        )

    index_path = os.path.join(out_dir, "README.md")
    write_text(index_path, "\n".join(index_lines) + "\n")
    return {
        "subsystem_count": len(subsystems),
        "subsystem_index": index_path,
        "subsystem_docs": doc_paths,
    }

def render_traceability_markdown(traceability: dict[str, Any]) -> str:
    scanned = int(traceability.get("scanned_files_count", 0))
    valid_paths = int(traceability.get("valid_evidence_paths_count", 0))
    coverage = float(traceability.get("evidence_file_coverage", 0.0))
    missing = int(traceability.get("files_missing_evidence_count", 0))
    strict_enabled = bool(traceability.get("strict_traceability_enabled", False))
    strict_pass = bool(traceability.get("strict_traceability_pass", True))
    missing_sample = traceability.get("files_missing_evidence_sample", [])

    lines = [
        "# Traceability Audit",
        "",
        "## Summary",
        f"- Scanned files: `{scanned}`",
        f"- Files referenced by evidence paths: `{valid_paths}`",
        f"- Evidence file coverage: `{coverage:.2%}`",
        f"- Files missing evidence references: `{missing}`",
        f"- Strict traceability enabled: `{strict_enabled}`",
        f"- Strict traceability pass: `{strict_pass}`",
        "",
        "## Interpretation",
        "1. High evidence file coverage means report claims are distributed across the scanned repository, not concentrated in a few files.",
        "2. Non-zero missing files means some scanned files were not referenced in factual claims and should be reviewed.",
        "3. Strict traceability pass confirms that every scanned file appears in at least one evidence token.",
        "",
        "## Missing File Sample",
    ]
    if missing_sample:
        for path in missing_sample[:30]:
            lines.append(f"- `{path}`")
    else:
        lines.append("- None")
    lines.append("")
    return "\n".join(lines)


def _load_json_file(path: str) -> Optional[dict[str, Any]]:
    if not os.path.exists(path):
        return None
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        if isinstance(data, dict):
            return data
    except Exception:
        return None
    return None


def _state_path(run_dir: str) -> str:
    return os.path.join(run_dir, "state.json")


def _summary_path(run_dir: str) -> str:
    return os.path.join(run_dir, "run_summary.md")


def _run_fact_index_path(run_dir: str, state: Optional[dict[str, Any]]) -> Optional[str]:
    if state:
        artifacts = state.get("artifacts", {})
        if isinstance(artifacts, dict):
            p = artifacts.get("run_fact_index")
            if isinstance(p, str) and p and os.path.exists(p):
                return p
    fallback = os.path.join(run_dir, "fact_index.json")
    if os.path.exists(fallback):
        return fallback
    return None


def _fact_snapshot(fact_index: dict[str, Any]) -> dict[str, Any]:
    files = [str(i.get("path", "")) for i in fact_index.get("files", []) if str(i.get("path", ""))]
    endpoints = [
        f"{str(i.get('method', 'GET')).upper()} {str(i.get('route', '/'))} :: {str(i.get('file', ''))}"
        for i in fact_index.get("api_endpoints", [])
    ]
    dependencies = [str(i.get("name", "")) for i in fact_index.get("dependencies", []) if str(i.get("name", ""))]
    scripts = [f"{str(i.get('name', ''))}::{str(i.get('command', ''))}" for i in fact_index.get("scripts", [])]
    entrypoints = [f"{str(i.get('kind', ''))}::{str(i.get('file', ''))}" for i in fact_index.get("entrypoints", [])]
    infra = [f"{str(i.get('type', ''))}::{str(i.get('file', ''))}" for i in fact_index.get("infrastructure", [])]
    sql_entities = [f"{str(i.get('kind', ''))}::{str(i.get('name', ''))}::{str(i.get('file', ''))}" for i in fact_index.get("sql_entities", [])]
    sql_queries = [f"{str(i.get('kind', ''))}::{str(i.get('target', ''))}::{str(i.get('file', ''))}" for i in fact_index.get("sql_queries", [])]
    cross_file_symbol_edges = [
        f"{str(i.get('source_symbol', ''))}::{str(i.get('target_symbol', ''))}::{str(i.get('source_file', ''))}::{str(i.get('target_file', ''))}"
        for i in fact_index.get("cross_file_symbol_edges", [])
    ]
    cross_file_event_edges = [
        f"{str(i.get('transport', ''))}::{str(i.get('channel', ''))}::{str(i.get('source_file', ''))}::{str(i.get('target_file', ''))}"
        for i in fact_index.get("cross_file_event_edges", [])
    ]
    return {
        "files_count": len(files),
        "endpoints_count": len(endpoints),
        "dependencies_count": len(dependencies),
        "scripts_count": len(scripts),
        "entrypoints_count": len(entrypoints),
        "infrastructure_count": len(infra),
        "sql_entities_count": len(sql_entities),
        "sql_queries_count": len(sql_queries),
        "cross_file_symbol_edges_count": len(cross_file_symbol_edges),
        "cross_file_event_edges_count": len(cross_file_event_edges),
        "files_set": sorted(set(files)),
        "endpoints_set": sorted(set(endpoints)),
        "dependencies_set": sorted(set(dependencies)),
        "scripts_set": sorted(set(scripts)),
        "entrypoints_set": sorted(set(entrypoints)),
        "infrastructure_set": sorted(set(infra)),
        "sql_entities_set": sorted(set(sql_entities)),
        "sql_queries_set": sorted(set(sql_queries)),
        "cross_file_symbol_edges_set": sorted(set(cross_file_symbol_edges)),
        "cross_file_event_edges_set": sorted(set(cross_file_event_edges)),
    }


def _set_delta(base_items: list[str], head_items: list[str], max_items: int = 20) -> dict[str, Any]:
    base = set(base_items)
    head = set(head_items)
    added = sorted(head - base)
    removed = sorted(base - head)
    return {
        "added_count": len(added),
        "removed_count": len(removed),
        "added": added[:max_items],
        "removed": removed[:max_items],
    }


def compare_snapshots(base_snapshot: dict[str, Any], head_snapshot: dict[str, Any]) -> dict[str, Any]:
    metrics = {}
    for key in ["files", "endpoints", "dependencies", "scripts", "entrypoints", "infrastructure", "sql_entities", "sql_queries", "cross_file_symbol_edges", "cross_file_event_edges"]:
        b = int(base_snapshot.get(f"{key}_count", 0))
        h = int(head_snapshot.get(f"{key}_count", 0))
        metrics[key] = {"base": b, "head": h, "delta": h - b}

    return {
        "metrics": metrics,
        "files": _set_delta(base_snapshot.get("files_set", []), head_snapshot.get("files_set", [])),
        "endpoints": _set_delta(base_snapshot.get("endpoints_set", []), head_snapshot.get("endpoints_set", [])),
        "dependencies": _set_delta(base_snapshot.get("dependencies_set", []), head_snapshot.get("dependencies_set", [])),
        "scripts": _set_delta(base_snapshot.get("scripts_set", []), head_snapshot.get("scripts_set", [])),
        "entrypoints": _set_delta(base_snapshot.get("entrypoints_set", []), head_snapshot.get("entrypoints_set", [])),
        "infrastructure": _set_delta(base_snapshot.get("infrastructure_set", []), head_snapshot.get("infrastructure_set", [])),
        "sql_entities": _set_delta(base_snapshot.get("sql_entities_set", []), head_snapshot.get("sql_entities_set", [])),
        "sql_queries": _set_delta(base_snapshot.get("sql_queries_set", []), head_snapshot.get("sql_queries_set", [])),
        "cross_file_symbol_edges": _set_delta(base_snapshot.get("cross_file_symbol_edges_set", []), head_snapshot.get("cross_file_symbol_edges_set", [])),
        "cross_file_event_edges": _set_delta(base_snapshot.get("cross_file_event_edges_set", []), head_snapshot.get("cross_file_event_edges_set", [])),
    }

def _normalize_architecture_model(model: Any) -> dict[str, Any]:
    if not isinstance(model, dict):
        return {"version": 1, "summary": {}, "nodes": [], "edges": []}
    nodes = model.get("nodes", [])
    edges = model.get("edges", [])
    summary = model.get("summary", {})
    return {
        "version": int(model.get("version", 1) or 1),
        "summary": summary if isinstance(summary, dict) else {},
        "nodes": nodes if isinstance(nodes, list) else [],
        "edges": edges if isinstance(edges, list) else [],
    }

def _architecture_model_from_run(run_dir: str, state: dict[str, Any], fact_index: dict[str, Any]) -> dict[str, Any]:
    artifacts = state.get("artifacts", {}) if isinstance(state.get("artifacts", {}), dict) else {}
    raw = str(artifacts.get("run_architecture_model", "")).strip()
    candidates: list[str] = []
    if raw:
        if os.path.isabs(raw):
            candidates.append(raw)
        else:
            candidates.append(os.path.join(run_dir, raw))
            candidates.append(os.path.join(run_dir, os.path.basename(raw)))
    candidates.append(os.path.join(run_dir, "architecture_model.json"))
    for path in candidates:
        payload = _load_json_file(path)
        if isinstance(payload, dict) and isinstance(payload.get("nodes", []), list):
            return _normalize_architecture_model(payload)
    existing = fact_index.get("architecture_model", {}) if isinstance(fact_index, dict) else {}
    if isinstance(existing, dict) and isinstance(existing.get("nodes", []), list) and existing.get("nodes"):
        return _normalize_architecture_model(existing)
    return _normalize_architecture_model(analyzer.build_architecture_model(fact_index))

def _architecture_count_metrics(base_counts: dict[str, Any], head_counts: dict[str, Any]) -> dict[str, dict[str, int]]:
    out: dict[str, dict[str, int]] = {}
    for key in sorted(set(base_counts.keys()) | set(head_counts.keys())):
        base_value = int(base_counts.get(key, 0) or 0)
        head_value = int(head_counts.get(key, 0) or 0)
        out[key] = {"base": base_value, "head": head_value, "delta": head_value - base_value}
    return out

def _architecture_item_delta(
    base_items: list[dict[str, Any]],
    head_items: list[dict[str, Any]],
    summarize,
    max_items: int = 20,
) -> dict[str, Any]:
    base_lookup = {
        str(item.get("id", "")).strip(): item
        for item in base_items
        if isinstance(item, dict) and str(item.get("id", "")).strip()
    }
    head_lookup = {
        str(item.get("id", "")).strip(): item
        for item in head_items
        if isinstance(item, dict) and str(item.get("id", "")).strip()
    }
    added_ids = sorted(set(head_lookup.keys()) - set(base_lookup.keys()))
    removed_ids = sorted(set(base_lookup.keys()) - set(head_lookup.keys()))
    return {
        "added_count": len(added_ids),
        "removed_count": len(removed_ids),
        "added": [summarize(head_lookup[item_id]) for item_id in added_ids[:max_items]],
        "removed": [summarize(base_lookup[item_id]) for item_id in removed_ids[:max_items]],
    }

def compare_architecture_models(base_model: dict[str, Any], head_model: dict[str, Any]) -> dict[str, Any]:
    base = _normalize_architecture_model(base_model)
    head = _normalize_architecture_model(head_model)

    def summarize_node(item: dict[str, Any]) -> dict[str, Any]:
        return {
            "id": str(item.get("id", "")).strip(),
            "label": str(item.get("label", "")).strip(),
            "kind": str(item.get("kind", "")).strip(),
            "bucket": str(item.get("bucket", "")).strip(),
            "layer": str(item.get("layer", "")).strip(),
        }

    def summarize_edge(item: dict[str, Any]) -> dict[str, Any]:
        return {
            "id": str(item.get("id", "")).strip(),
            "kind": str(item.get("kind", "")).strip(),
            "source": str(item.get("source", "")).strip(),
            "target": str(item.get("target", "")).strip(),
            "label": str(item.get("label", "")).strip(),
        }

    base_summary = base.get("summary", {}) if isinstance(base.get("summary", {}), dict) else {}
    head_summary = head.get("summary", {}) if isinstance(head.get("summary", {}), dict) else {}
    base_node_kind_counts = base_summary.get("node_kind_counts", {})
    head_node_kind_counts = head_summary.get("node_kind_counts", {})
    base_edge_kind_counts = base_summary.get("edge_kind_counts", {})
    head_edge_kind_counts = head_summary.get("edge_kind_counts", {})
    if not isinstance(base_node_kind_counts, dict):
        base_node_kind_counts = {}
    if not isinstance(head_node_kind_counts, dict):
        head_node_kind_counts = {}
    if not isinstance(base_edge_kind_counts, dict):
        base_edge_kind_counts = {}
    if not isinstance(head_edge_kind_counts, dict):
        head_edge_kind_counts = {}

    node_delta = _architecture_item_delta(base.get("nodes", []), head.get("nodes", []), summarize_node)
    edge_delta = _architecture_item_delta(base.get("edges", []), head.get("edges", []), summarize_edge)
    metrics = {
        "nodes": {
            "base": len(base.get("nodes", [])),
            "head": len(head.get("nodes", [])),
            "delta": len(head.get("nodes", [])) - len(base.get("nodes", [])),
        },
        "edges": {
            "base": len(base.get("edges", [])),
            "head": len(head.get("edges", [])),
            "delta": len(head.get("edges", [])) - len(base.get("edges", [])),
        },
    }
    changed = any(
        [
            metrics["nodes"]["delta"] != 0,
            metrics["edges"]["delta"] != 0,
            node_delta.get("added_count", 0) != 0,
            node_delta.get("removed_count", 0) != 0,
            edge_delta.get("added_count", 0) != 0,
            edge_delta.get("removed_count", 0) != 0,
        ]
    )
    return {
        "changed": changed,
        "metrics": metrics,
        "node_kinds": _architecture_count_metrics(base_node_kind_counts, head_node_kind_counts),
        "edge_kinds": _architecture_count_metrics(base_edge_kind_counts, head_edge_kind_counts),
        "nodes": node_delta,
        "edges": edge_delta,
        "base_summary": base_summary,
        "head_summary": head_summary,
    }

def render_architecture_diff_markdown(
    architecture_diff: dict[str, Any],
    *,
    header: str = "# Architecture Comparison",
    base_run_id: str = "",
    head_run_id: str = "",
) -> str:
    diff = architecture_diff if isinstance(architecture_diff, dict) else {}
    metrics = diff.get("metrics", {}) if isinstance(diff.get("metrics", {}), dict) else {}
    node_kinds = diff.get("node_kinds", {}) if isinstance(diff.get("node_kinds", {}), dict) else {}
    edge_kinds = diff.get("edge_kinds", {}) if isinstance(diff.get("edge_kinds", {}), dict) else {}
    node_delta = diff.get("nodes", {}) if isinstance(diff.get("nodes", {}), dict) else {}
    edge_delta = diff.get("edges", {}) if isinstance(diff.get("edges", {}), dict) else {}

    lines = [header, ""]
    if base_run_id or head_run_id:
        lines.append(f"- Base run: `{base_run_id or 'base'}`")
        lines.append(f"- Head run: `{head_run_id or 'head'}`")
        lines.append("")
    lines.append(f"- Changed: `{bool(diff.get('changed', False))}`")
    for key in ["nodes", "edges"]:
        metric = metrics.get(key, {})
        lines.append(f"- {key}: base={metric.get('base', 0)} head={metric.get('head', 0)} delta={metric.get('delta', 0)}")

    changed_node_kinds = [kind for kind, item in sorted(node_kinds.items()) if int(item.get("delta", 0) or 0) != 0]
    if changed_node_kinds:
        lines.extend(["", "## Node Kind Deltas"])
        for kind in changed_node_kinds:
            item = node_kinds.get(kind, {})
            lines.append(f"- {kind}: base={item.get('base', 0)} head={item.get('head', 0)} delta={item.get('delta', 0)}")

    changed_edge_kinds = [kind for kind, item in sorted(edge_kinds.items()) if int(item.get("delta", 0) or 0) != 0]
    if changed_edge_kinds:
        lines.extend(["", "## Edge Kind Deltas"])
        for kind in changed_edge_kinds:
            item = edge_kinds.get(kind, {})
            lines.append(f"- {kind}: base={item.get('base', 0)} head={item.get('head', 0)} delta={item.get('delta', 0)}")

    lines.extend(["", "## Node Changes"])
    lines.append(f"- Added: {node_delta.get('added_count', 0)}")
    lines.append(f"- Removed: {node_delta.get('removed_count', 0)}")
    for item in node_delta.get("added", []):
        lines.append(f"- Added node: {item.get('kind', 'node')} `{item.get('label') or item.get('id')}`")
    for item in node_delta.get("removed", []):
        lines.append(f"- Removed node: {item.get('kind', 'node')} `{item.get('label') or item.get('id')}`")

    lines.extend(["", "## Edge Changes"])
    lines.append(f"- Added: {edge_delta.get('added_count', 0)}")
    lines.append(f"- Removed: {edge_delta.get('removed_count', 0)}")
    for item in edge_delta.get("added", []):
        lines.append(f"- Added edge: {item.get('kind', 'edge')} `{item.get('source', '')}` -> `{item.get('target', '')}`")
    for item in edge_delta.get("removed", []):
        lines.append(f"- Removed edge: {item.get('kind', 'edge')} `{item.get('source', '')}` -> `{item.get('target', '')}`")
    lines.append("")
    return "\n".join(lines)


def render_run_diff_markdown(diff: dict[str, Any]) -> str:
    base_run = diff.get("base_run_id", "base")
    head_run = diff.get("head_run_id", "head")
    base_git = diff.get("base_git", {}) if isinstance(diff.get("base_git", {}), dict) else {}
    head_git = diff.get("head_git", {}) if isinstance(diff.get("head_git", {}), dict) else {}
    cmp = diff.get("comparison", {})
    metrics = cmp.get("metrics", {})
    lines = [
        "# Run Comparison",
        "",
        f"- Base run: `{base_run}`",
        f"- Head run: `{head_run}`",
    ]
    if base_git.get("branch") or base_git.get("commit"):
        lines.append(f"- Base git branch: `{base_git.get('branch', '')}`")
        lines.append(f"- Base git commit: `{str(base_git.get('commit', ''))[:12]}`")
    if head_git.get("branch") or head_git.get("commit"):
        lines.append(f"- Head git branch: `{head_git.get('branch', '')}`")
        lines.append(f"- Head git commit: `{str(head_git.get('commit', ''))[:12]}`")
    lines.extend(["", "## Metric Deltas"])
    for key in ["files", "endpoints", "dependencies", "scripts", "entrypoints", "infrastructure", "sql_entities", "sql_queries", "cross_file_symbol_edges", "cross_file_event_edges"]:
        m = metrics.get(key, {})
        lines.append(f"- {key}: base={m.get('base', 0)} head={m.get('head', 0)} delta={m.get('delta', 0)}")

    def add_section(name: str) -> None:
        section = cmp.get(name, {})
        lines.append("")
        lines.append(f"## {name.title()} Changes")
        lines.append(f"- Added: {section.get('added_count', 0)}")
        lines.append(f"- Removed: {section.get('removed_count', 0)}")
        for item in section.get("added", []):
            lines.append(f"- Added item: {item}")
        for item in section.get("removed", []):
            lines.append(f"- Removed item: {item}")

    for sec in ["files", "endpoints", "dependencies", "scripts", "entrypoints", "infrastructure", "sql_entities", "sql_queries", "cross_file_symbol_edges", "cross_file_event_edges"]:
        add_section(sec)
    architecture_diff = diff.get("architecture", {})
    if isinstance(architecture_diff, dict):
        lines.extend(["", render_architecture_diff_markdown(architecture_diff, header="## Architecture Changes").strip()])
    lines.append("")
    return "\n".join(lines)


def compare_run_dirs(base_run_dir: str, head_run_dir: str) -> dict[str, Any]:
    base_state = _load_json_file(_state_path(base_run_dir))
    head_state = _load_json_file(_state_path(head_run_dir))

    base_fact_path = _run_fact_index_path(base_run_dir, base_state)
    head_fact_path = _run_fact_index_path(head_run_dir, head_state)
    if not base_fact_path or not head_fact_path:
        raise RuntimeError("Missing fact_index in one of the run directories.")

    base_fact = load_fact_index(base_fact_path)
    head_fact = load_fact_index(head_fact_path)

    base_snapshot = _fact_snapshot(base_fact)
    head_snapshot = _fact_snapshot(head_fact)
    base_architecture = _architecture_model_from_run(base_run_dir, base_state or {}, base_fact)
    head_architecture = _architecture_model_from_run(head_run_dir, head_state or {}, head_fact)
    return {
        "base_run_id": os.path.basename(base_run_dir),
        "head_run_id": os.path.basename(head_run_dir),
        "base_run_dir": base_run_dir,
        "head_run_dir": head_run_dir,
        "base_git": (base_state or {}).get("repo_metadata", {}).get("git", {}),
        "head_git": (head_state or {}).get("repo_metadata", {}).get("git", {}),
        "comparison": compare_snapshots(base_snapshot, head_snapshot),
        "architecture": compare_architecture_models(base_architecture, head_architecture),
    }


def build_repo_run_trends(
    runs_dir: str,
    repo_path: str,
    *,
    max_runs: int = 200,
) -> dict[str, Any]:
    root = os.path.abspath(os.path.expanduser(str(runs_dir or "").strip()))
    repo_norm = normalize_repo_path_value(repo_path)
    entries: list[dict[str, Any]] = []
    if root and os.path.isdir(root):
        for name in os.listdir(root):
            run_dir = os.path.join(root, name)
            if not os.path.isdir(run_dir):
                continue
            state = load_run_state(run_dir)
            if not isinstance(state, dict):
                continue
            state_repo = normalize_repo_path_value(str(state.get("repo_path", "")))
            if state_repo != repo_norm:
                continue
            fact_index = _artifact_json(state, "run_fact_index") or {}
            git_info = state.get("repo_metadata", {}).get("git", {}) if isinstance(state.get("repo_metadata", {}), dict) else {}
            timings = state.get("timing", {}) if isinstance(state.get("timing", {}), dict) else {}
            if not timings and isinstance(state.get("timings", {}), dict):
                timings = state.get("timings", {})
            gate = state.get("gate", {}) if isinstance(state.get("gate", {}), dict) else {}
            entries.append(
                {
                    "run_id": str(state.get("run_id", name)).strip() or name,
                    "run_dir": run_dir,
                    "status": str(state.get("status", "")).strip(),
                    "started_at": str(state.get("started_at", "")).strip(),
                    "completed_at": str(state.get("completed_at", "")).strip(),
                    "requested_mode": str(state.get("requested_mode", "")).strip(),
                    "mode": str(state.get("mode", "")).strip(),
                    "audience": normalize_doc_audience(str(state.get("audience", "")).strip()),
                    "goal": str(state.get("goal", "")).strip(),
                    "branch": str(git_info.get("branch", "")).strip(),
                    "commit": str(git_info.get("commit", "")).strip(),
                    "gate_pass": bool(gate.get("pass", False)) or str(state.get("status", "")).strip() == "completed",
                    "report_source": str(state.get("report_source", "")).strip(),
                    "files": len(fact_index.get("files", [])) if isinstance(fact_index.get("files", []), list) else 0,
                    "endpoints": len(fact_index.get("api_endpoints", [])) if isinstance(fact_index.get("api_endpoints", []), list) else 0,
                    "runtime_observations": len(fact_index.get("runtime_observations", [])) if isinstance(fact_index.get("runtime_observations", []), list) else 0,
                    "subsystems": len(build_subsystem_summary_map(fact_index)) if fact_index else 0,
                    "total_sec": float(timings.get("total_sec", 0.0) or 0.0),
                }
            )
    entries = sorted(
        entries,
        key=lambda item: (
            str(item.get("completed_at", "")).strip() or str(item.get("started_at", "")).strip(),
            str(item.get("run_id", "")).strip(),
        ),
    )
    if max_runs > 0 and len(entries) > max_runs:
        entries = entries[-max_runs:]

    status_counts: dict[str, int] = {}
    mode_counts: dict[str, int] = {}
    audience_counts: dict[str, int] = {}
    branch_map: dict[str, dict[str, Any]] = {}
    commit_seen: set[str] = set()
    recent_commits: list[dict[str, Any]] = []
    total_runs = len(entries)
    passed_runs = sum(1 for item in entries if bool(item.get("gate_pass", False)))
    avg_total_sec = (
        sum(float(item.get("total_sec", 0.0) or 0.0) for item in entries) / float(total_runs)
        if total_runs
        else 0.0
    )
    for item in entries:
        status = str(item.get("status", "")).strip() or "unknown"
        mode = str(item.get("mode", "")).strip() or "unknown"
        audience = normalize_doc_audience(str(item.get("audience", "reviewer")).strip())
        branch = str(item.get("branch", "")).strip() or "detached"
        commit = str(item.get("commit", "")).strip()
        status_counts[status] = status_counts.get(status, 0) + 1
        mode_counts[mode] = mode_counts.get(mode, 0) + 1
        audience_counts[audience] = audience_counts.get(audience, 0) + 1
        branch_summary = branch_map.setdefault(
            branch,
            {
                "branch": branch,
                "runs": 0,
                "passed_runs": 0,
                "latest_run_id": "",
                "latest_commit": "",
                "latest_completed_at": "",
                "avg_total_sec": 0.0,
                "avg_endpoints": 0.0,
            },
        )
        branch_summary["runs"] += 1
        branch_summary["passed_runs"] += 1 if bool(item.get("gate_pass", False)) else 0
        branch_summary["avg_total_sec"] += float(item.get("total_sec", 0.0) or 0.0)
        branch_summary["avg_endpoints"] += float(item.get("endpoints", 0) or 0)
        completed_at = str(item.get("completed_at", "")).strip() or str(item.get("started_at", "")).strip()
        if completed_at >= str(branch_summary.get("latest_completed_at", "")):
            branch_summary["latest_completed_at"] = completed_at
            branch_summary["latest_run_id"] = str(item.get("run_id", "")).strip()
            branch_summary["latest_commit"] = commit
        if commit and commit not in commit_seen:
            commit_seen.add(commit)
            recent_commits.append(
                {
                    "branch": branch,
                    "commit": commit,
                    "run_id": str(item.get("run_id", "")).strip(),
                    "status": status,
                    "gate_pass": bool(item.get("gate_pass", False)),
                    "completed_at": completed_at,
                }
            )
    branch_summaries: list[dict[str, Any]] = []
    for item in branch_map.values():
        runs = int(item.get("runs", 0) or 0)
        branch_summaries.append(
            {
                **item,
                "pass_rate": (float(item.get("passed_runs", 0) or 0) / float(runs)) if runs else 0.0,
                "avg_total_sec": (float(item.get("avg_total_sec", 0.0) or 0.0) / float(runs)) if runs else 0.0,
                "avg_endpoints": (float(item.get("avg_endpoints", 0.0) or 0.0) / float(runs)) if runs else 0.0,
            }
        )
    branch_summaries = sorted(branch_summaries, key=lambda item: (-int(item.get("runs", 0) or 0), str(item.get("branch", ""))))
    recent_commits = sorted(recent_commits, key=lambda item: str(item.get("completed_at", "")), reverse=True)[:10]
    recent_runs = list(reversed(entries[-10:]))
    return {
        "generated_at": utc_now_iso(),
        "repo_path": analyzer.display_safe_path(repo_path),
        "runs_dir": root,
        "total_runs": total_runs,
        "branch_count": len(branch_summaries),
        "commit_count": len(commit_seen),
        "pass_rate": (float(passed_runs) / float(total_runs)) if total_runs else 0.0,
        "average_total_sec": avg_total_sec,
        "status_counts": status_counts,
        "mode_counts": mode_counts,
        "audience_counts": audience_counts,
        "branch_summaries": branch_summaries,
        "recent_commits": recent_commits,
        "recent_runs": recent_runs,
    }


def render_repo_run_trends_markdown(trends: dict[str, Any]) -> str:
    payload = trends if isinstance(trends, dict) else {}
    branch_summaries = payload.get("branch_summaries", []) if isinstance(payload.get("branch_summaries", []), list) else []
    recent_commits = payload.get("recent_commits", []) if isinstance(payload.get("recent_commits", []), list) else []
    recent_runs = payload.get("recent_runs", []) if isinstance(payload.get("recent_runs", []), list) else []
    lines = [
        "# Repo Run Trends",
        "",
        f"- Generated At: `{payload.get('generated_at', '')}`",
        f"- Repo Path: `{payload.get('repo_path', '')}`",
        f"- Runs Dir: `{payload.get('runs_dir', '')}`",
        f"- Total Runs: `{int(payload.get('total_runs', 0) or 0)}`",
        f"- Branch Count: `{int(payload.get('branch_count', 0) or 0)}`",
        f"- Commit Count: `{int(payload.get('commit_count', 0) or 0)}`",
        f"- Pass Rate: `{float(payload.get('pass_rate', 0.0) or 0.0):.2%}`",
        f"- Average Total Time Sec: `{float(payload.get('average_total_sec', 0.0) or 0.0):.3f}`",
        f"- Status Counts: `{json.dumps(payload.get('status_counts', {}), ensure_ascii=True, sort_keys=True)}`",
        f"- Mode Counts: `{json.dumps(payload.get('mode_counts', {}), ensure_ascii=True, sort_keys=True)}`",
        f"- Audience Counts: `{json.dumps(payload.get('audience_counts', {}), ensure_ascii=True, sort_keys=True)}`",
        "",
        "## Branch Summary",
        "",
        "| Branch | Runs | Pass Rate | Latest Run | Latest Commit | Avg Time Sec | Avg Endpoints |",
        "| --- | ---: | ---: | --- | --- | ---: | ---: |",
    ]
    for item in branch_summaries:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(item.get("branch", "")).strip() or "detached",
                    str(int(item.get("runs", 0) or 0)),
                    f"{float(item.get('pass_rate', 0.0) or 0.0):.2%}",
                    str(item.get("latest_run_id", "")).strip() or "-",
                    str(item.get("latest_commit", "")).strip()[:12] or "-",
                    f"{float(item.get('avg_total_sec', 0.0) or 0.0):.3f}",
                    f"{float(item.get('avg_endpoints', 0.0) or 0.0):.1f}",
                ]
            )
            + " |"
        )
    if not branch_summaries:
        lines.append("| detached | 0 | 0.00% | - | - | 0.000 | 0.0 |")
    lines.extend(
        [
            "",
            "## Recent Commits",
            "",
            "| Branch | Commit | Run | Status | Gate Pass | Completed At |",
            "| --- | --- | --- | --- | ---: | --- |",
        ]
    )
    for item in recent_commits:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(item.get("branch", "")).strip() or "detached",
                    str(item.get("commit", "")).strip()[:12] or "-",
                    str(item.get("run_id", "")).strip() or "-",
                    str(item.get("status", "")).strip() or "-",
                    str(bool(item.get("gate_pass", False))),
                    str(item.get("completed_at", "")).strip() or "-",
                ]
            )
            + " |"
        )
    if not recent_commits:
        lines.append("| detached | - | - | - | False | - |")
    lines.extend(
        [
            "",
            "## Recent Runs",
            "",
            "| Run | Status | Audience | Branch | Commit | Mode | Files | Endpoints | Total Sec |",
            "| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: |",
        ]
    )
    for item in recent_runs:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(item.get("run_id", "")).strip() or "-",
                    str(item.get("status", "")).strip() or "-",
                    normalize_doc_audience(str(item.get("audience", "")).strip()),
                    str(item.get("branch", "")).strip() or "detached",
                    str(item.get("commit", "")).strip()[:12] or "-",
                    str(item.get("mode", "")).strip() or "-",
                    str(int(item.get("files", 0) or 0)),
                    str(int(item.get("endpoints", 0) or 0)),
                    f"{float(item.get('total_sec', 0.0) or 0.0):.3f}",
                ]
            )
            + " |"
        )
    if not recent_runs:
        lines.append("| - | - | reviewer | detached | - | - | 0 | 0 | 0.000 |")
    lines.append("")
    return "\n".join(lines)


def find_previous_run_for_repo(
    runs_dir: str,
    current_run_dir: str,
    repo_path: str,
    current_state: Optional[dict[str, Any]] = None,
) -> Optional[dict[str, Any]]:
    if not os.path.isdir(runs_dir):
        return None
    current_abs = os.path.abspath(current_run_dir)
    repo_norm = normalize_repo_path_value(repo_path)
    current_git = {}
    if isinstance(current_state, dict):
        current_git = current_state.get("repo_metadata", {}).get("git", {}) or {}
    current_commit = str(current_git.get("commit", "")).strip()
    current_branch = str(current_git.get("branch", "")).strip()
    candidates = []
    for name in os.listdir(runs_dir):
        run_dir = os.path.join(runs_dir, name)
        if not os.path.isdir(run_dir):
            continue
        if os.path.abspath(run_dir) == current_abs:
            continue
        state = _load_json_file(_state_path(run_dir))
        if not state:
            continue
        state_repo = normalize_repo_path_value(str(state.get("repo_path", "")))
        if state_repo != repo_norm:
            continue
        if state.get("status") not in {"completed", "failed_gate"}:
            continue
        git_info = state.get("repo_metadata", {}).get("git", {}) or {}
        branch = str(git_info.get("branch", "")).strip()
        commit = str(git_info.get("commit", "")).strip()
        same_branch = bool(current_branch and branch and branch == current_branch)
        different_commit = bool(current_commit and commit and commit != current_commit)
        same_commit = bool(current_commit and commit and commit == current_commit)
        candidates.append(
            (
                1 if different_commit else 0,
                1 if same_branch else 0,
                0 if same_commit else 1,
                os.path.getmtime(_state_path(run_dir)),
                run_dir,
                state,
                branch,
                commit,
            )
        )

    if not candidates:
        return None
    candidates.sort(key=lambda x: (x[0], x[1], x[2], x[3]), reverse=True)
    _different_commit, _same_branch, _different_from_same_commit, _mtime, run_dir, state, branch, commit = candidates[0]
    return {
        "run_dir": run_dir,
        "state": state,
        "run_id": os.path.basename(run_dir),
        "branch": branch,
        "commit": commit,
    }


def first_evidence_from_files(fact_index: dict[str, Any]) -> str:
    files = fact_index.get("files", [])
    if files:
        first = files[0].get("path", "")
        if first:
            return f"{first}#L1"
    return "none"


def tokenize_goal(text: str) -> list[str]:
    tokens = re.findall(r"[a-zA-Z0-9_]+", text.lower())
    return [t for t in tokens if len(t) >= 3]


def build_goal_focus(fact_index: dict[str, Any], goal: str, max_items: int = 8) -> dict[str, Any]:
    tokens = tokenize_goal(goal)
    focus = {
        "tokens": tokens,
        "files": [],
        "endpoints": [],
        "dependencies": [],
        "scripts": [],
        "sql_entities": [],
        "sql_queries": [],
    }
    if not tokens:
        return focus

    def has_match(text: str) -> bool:
        low = text.lower()
        return any(t in low for t in tokens)

    for item in fact_index.get("files", []):
        path = str(item.get("path", ""))
        if path and has_match(path):
            focus["files"].append({"path": path, "evidence": f"{path}#L1"})
        if len(focus["files"]) >= max_items:
            break

    for item in fact_index.get("api_endpoints", []):
        route = str(item.get("route", ""))
        framework = str(item.get("framework", ""))
        if has_match(route) or has_match(framework):
            focus["endpoints"].append(
                {
                    "method": item.get("method", "GET"),
                    "route": route,
                    "evidence": item.get("evidence", "none"),
                }
            )
        if len(focus["endpoints"]) >= max_items:
            break

    for item in fact_index.get("dependencies", []):
        name = str(item.get("name", ""))
        if has_match(name):
            focus["dependencies"].append({"name": name, "evidence": item.get("evidence", "none")})
        if len(focus["dependencies"]) >= max_items:
            break

    for item in fact_index.get("scripts", []):
        name = str(item.get("name", ""))
        cmd = str(item.get("command", ""))
        if has_match(name) or has_match(cmd):
            focus["scripts"].append(
                {
                    "name": name,
                    "command": cmd,
                    "evidence": item.get("evidence", "none"),
                }
            )
        if len(focus["scripts"]) >= max_items:
            break

    for item in fact_index.get("sql_entities", []):
        name = str(item.get("name", ""))
        kind = str(item.get("kind", ""))
        if has_match(name) or has_match(kind):
            focus["sql_entities"].append(
                {
                    "kind": kind,
                    "name": name,
                    "evidence": item.get("evidence", "none"),
                }
            )
        if len(focus["sql_entities"]) >= max_items:
            break

    for item in fact_index.get("sql_queries", []):
        kind = str(item.get("kind", ""))
        target = str(item.get("target", ""))
        if has_match(kind) or has_match(target):
            focus["sql_queries"].append(
                {
                    "kind": kind,
                    "target": target,
                    "evidence": item.get("evidence", "none"),
                }
            )
        if len(focus["sql_queries"]) >= max_items:
            break

    return focus


def format_goal_focus(focus: dict[str, Any]) -> str:
    tokens = focus.get("tokens", [])
    lines = []
    if tokens:
        lines.append(f"- Goal tokens: {', '.join(tokens)}")

    files = focus.get("files", [])
    if files:
        lines.append("- File matches:")
        for item in files:
            lines.append(f"  - {item['path']} [Evidence: {item['evidence']}]")

    endpoints = focus.get("endpoints", [])
    if endpoints:
        lines.append("- Endpoint matches:")
        for item in endpoints:
            lines.append(f"  - {item['method']} {item['route']} [Evidence: {item['evidence']}]")

    deps = focus.get("dependencies", [])
    if deps:
        lines.append("- Dependency matches:")
        for item in deps:
            lines.append(f"  - {item['name']} [Evidence: {item['evidence']}]")

    scripts = focus.get("scripts", [])
    if scripts:
        lines.append("- Script matches:")
        for item in scripts:
            lines.append(f"  - {item['name']} -> {item['command']} [Evidence: {item['evidence']}]")

    sql_entities = focus.get("sql_entities", [])
    if sql_entities:
        lines.append("- SQL entity matches:")
        for item in sql_entities:
            lines.append(f"  - {item['kind']} {item['name']} [Evidence: {item['evidence']}]")

    sql_queries = focus.get("sql_queries", [])
    if sql_queries:
        lines.append("- SQL query matches:")
        for item in sql_queries:
            lines.append(f"  - {item['kind']} {item['target']} [Evidence: {item['evidence']}]")

    if not lines:
        lines.append("- No direct goal-specific matches found from deterministic facts.")
    return "\n".join(lines)


def build_grounding_feedback(validation: dict[str, Any], gate: dict[str, Any]) -> str:
    invalid_tokens = validation.get("invalid_evidence_tokens", [])[:10]
    invalid_paths = validation.get("invalid_evidence_paths", [])[:10]
    unsupported = validation.get("unsupported_claims_sample", [])[:5]
    lines = [
        "Previous draft failed strict grounding. Fix these issues:",
        f"- Evidence coverage observed: {gate.get('coverage', 0.0):.2%}",
        f"- Semantic claim coverage observed: {gate.get('semantic_coverage', 1.0):.2%}",
        f"- Claims without evidence tags: {validation.get('claims_without_evidence', 0)}",
        f"- Invalid evidence tokens: {validation.get('invalid_evidence_tokens_count', 0)}",
        f"- Invalid evidence paths: {validation.get('invalid_evidence_paths_count', 0)}",
        f"- Semantically unsupported claims: {validation.get('claims_semantically_unsupported', 0)}",
    ]
    if invalid_tokens:
        lines.append(f"- Sample invalid tokens: {', '.join(map(str, invalid_tokens))}")
    if invalid_paths:
        lines.append(f"- Sample invalid paths: {', '.join(map(str, invalid_paths))}")
    if unsupported:
        lines.append(f"- Sample unsupported claims: {' | '.join(map(str, unsupported))}")
    return "\n".join(lines)


def build_document_prompt(
    goal: str,
    redaction_stats: dict[str, Any],
    allowed_files_text: str,
    allowed_evidence_text: str,
    fact_context_json: str,
    goal_focus_text: str,
    feedback_text: str,
) -> str:
    goal_line = goal.strip() if goal.strip() else "Create full repository documentation with grounded evidence."
    feedback_block = f"\nReviewer Feedback To Fix:\n{feedback_text}\n" if feedback_text.strip() else ""

    return f"""
You are a senior software engineer.
Reply in ENGLISH only. Use clear headings and bullet points.

Operator Goal:
- {goal_line}

Task:
1) Explain what this repo does in 5 bullets.
2) Give an architecture diagram in Mermaid graph TD using THIS EXACT TEMPLATE.
Rules:
- Do NOT use parentheses, slashes, dots, or ampersands in any label.
- Use plain words only example Next js Node js Python API.
- Keep the same subgraph names and node IDs.
- If a component does not exist in the repo, remove that node.
- Do not invent new tech.

TEMPLATE must follow:
{MERMAID_TEMPLATE}

3) List the key folders and files and what each does.
4) Give step by step instructions to run locally.
5) Give 10 smart questions to understand the codebase deeply.
6) Provide a Graphviz DOT architecture diagram in a fenced dot block.
7) Provide a LikeC4 architecture snippet in a fenced likec4 block.

Grounding and anti hallucination rules:
- Every factual bullet MUST end with [Evidence: path#Lline].
- Use only line level evidence from Allowed Evidence Targets.
- If evidence is missing, write exactly: Unknown from provided code. [Evidence: none]
- Do not invent components, files, behavior, or APIs.
- Do not generalize beyond explicit facts in the retrieval-oriented prompt context.
- If a relationship is not directly supported by evidence, mark it unknown.

Security context:
- Source snippets were pre redacted for likely secrets.
- Redaction summary: {analyzer.summarize_redaction_stats(redaction_stats)}

Goal specific deterministic focus hints:
{goal_focus_text}

Allowed Source and Runtime Artifact Paths:
{allowed_files_text}

Allowed Evidence Targets:
{allowed_evidence_text}

Retrieval-Oriented Deterministic Prompt Context single source of truth for LLM synthesis:
{fact_context_json}
{feedback_block}
"""


LLM_SECTION_ENHANCEMENT_SPECS = [
    {
        "key": "executive_summary",
        "heading": "## Executive Summary (LLM Enhanced)",
        "source_heading": "## 1) High-level Repository Overview",
        "purpose": (
            "Write a polished reviewer-facing summary of what the repository does, "
            "its architectural shape, and the strongest grounded implementation signals."
        ),
    },
    {
        "key": "repo_walkthrough",
        "heading": "## Repo Walkthrough (LLM Enhanced)",
        "source_heading": "## 2) Summaries for Major Folders and Modules",
        "purpose": (
            "Explain how a reviewer should navigate the repository, which folders or modules "
            "matter first, and why they matter."
        ),
    },
    {
        "key": "runbook_notes",
        "heading": "## Runbook Notes (LLM Enhanced)",
        "source_heading": "## 6) Setup and Run Instructions (Inferred)",
        "purpose": (
            "Rewrite the setup and execution guidance into clearer reviewer-friendly runbook notes "
            "without inventing new commands or deployment behavior."
        ),
    },
]
MIN_LLM_SECTION_FACTUAL_BULLETS = 3
LLM_SECTION_ITEM_COUNT = 3
LLM_SECTION_SUPPORT_SNIPPET_RADIUS = 2
LLM_SECTION_SUPPORT_SNIPPET_LIMIT = 10
LLM_SECTION_SUPPORT_CONTEXT_CHARS = 3600


def extract_markdown_section(markdown: str, heading: str) -> str:
    pattern = re.compile(rf"(?ms)^{re.escape(heading)}\s*\n(.*?)(?=^##\s|\Z)")
    match = pattern.search(str(markdown or ""))
    if not match:
        return ""
    body = match.group(1).strip()
    if not body:
        return heading + "\n"
    return heading + "\n" + body + "\n"


def normalize_llm_section_output(text: str, expected_heading: str) -> str:
    raw = str(text or "").replace("\r\n", "\n").strip()
    if not raw:
        return expected_heading + "\n"

    raw = re.sub(r"^\s*```[a-zA-Z0-9_-]*\s*", "", raw)
    raw = re.sub(r"\s*```\s*$", "", raw)
    if expected_heading in raw:
        raw = raw.split(expected_heading, 1)[1]

    body_lines: list[str] = []
    numbered_index = 1
    for line in raw.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith("## "):
            if body_lines:
                break
            continue
        if re.match(r"^\d+\.\s+", stripped):
            if numbered_index > LLM_SECTION_ITEM_COUNT:
                break
            body_lines.append(f"{numbered_index}. " + re.sub(r"^\d+\.\s+", "", stripped))
            numbered_index += 1
            continue
        if stripped.startswith("- ") or stripped.startswith("* "):
            if numbered_index > LLM_SECTION_ITEM_COUNT:
                break
            body_lines.append(f"{numbered_index}. " + stripped[2:].strip())
            numbered_index += 1
            continue
        if body_lines:
            body_lines[-1] = body_lines[-1].rstrip() + " " + stripped
            continue
        if numbered_index > LLM_SECTION_ITEM_COUNT:
            break
        body_lines.append(f"{numbered_index}. " + stripped)
        numbered_index += 1

    body = "\n".join(body_lines).strip()
    if not body:
        return expected_heading + "\n"
    return expected_heading + "\n" + body + "\n"


def evaluate_llm_section_gate(
    section_markdown: str,
    allowed_line_counts: Optional[dict[str, int]] = None,
    claim_support_index: Optional[dict[str, Any]] = None,
) -> dict[str, Any]:
    text = str(section_markdown or "").replace("\r\n", "\n").strip()
    lines = [line.rstrip() for line in text.splitlines()]
    heading_lines = [line for line in lines if line.strip().startswith("## ")]
    body_lines = [line.strip() for line in lines[1:] if line.strip()]
    numbered_lines = [line for line in body_lines if re.match(r"^\d+\.\s+", line)]
    prose_lines = [line for line in body_lines if not re.match(r"^\d+\.\s+", line)]
    body_text = "\n".join(body_lines).strip()
    items_with_evidence = 0
    semantically_supported_items = 0
    invalid_evidence_tokens: list[str] = []
    unsupported_claims: list[str] = []
    for line in numbered_lines:
        token_groups = analyzer.extract_evidence_token_strings(line)
        if not token_groups:
            continue
        item_valid = True
        normalized_evidence_tokens: list[str] = []
        for token in token_groups:
            path, line_no, has_line = analyzer.parse_evidence_token(token)
            if path == "none" or not has_line or line_no is None:
                item_valid = False
                invalid_evidence_tokens.append(token.strip())
                continue
            if allowed_line_counts is not None:
                max_line = allowed_line_counts.get(path)
                if max_line is None or line_no < 1 or line_no > max_line:
                    item_valid = False
                    invalid_evidence_tokens.append(token.strip())
                    continue
            normalized_evidence_tokens.append(analyzer.make_evidence(path, line_no))
        if item_valid:
            items_with_evidence += 1
            if claim_support_index:
                claim_text = analyzer.strip_evidence_tags(line)
                claim_text = re.sub(r"^\d+\.\s*", "", claim_text).strip()
                support_texts = analyzer._candidate_support_texts(
                    claim_text,
                    analyzer._semantic_tokens(claim_text),
                    normalized_evidence_tokens,
                    claim_support_index,
                )
                score, _basis = analyzer._score_claim_against_support(claim_text, support_texts)
                if score >= analyzer.effective_min_claim_support_score():
                    semantically_supported_items += 1
                elif len(unsupported_claims) < 10:
                    unsupported_claims.append(claim_text[:160])
            else:
                semantically_supported_items += 1
    passed = (
        len(heading_lines) == 1
        and bool(body_text)
        and "```" not in text
        and len(body_text) >= 160
        and len(body_text) <= 2600
        and len(body_lines) == LLM_SECTION_ITEM_COUNT
        and len(numbered_lines) == LLM_SECTION_ITEM_COUNT
        and not prose_lines
        and items_with_evidence == LLM_SECTION_ITEM_COUNT
        and semantically_supported_items == LLM_SECTION_ITEM_COUNT
        and not invalid_evidence_tokens
    )
    return {
        "pass": passed,
        "body_chars": len(body_text),
        "line_count": len(body_lines),
        "numbered_lines": len(numbered_lines),
        "contains_code_fence": "```" in text,
        "items_with_evidence": items_with_evidence,
        "semantically_supported_items": semantically_supported_items,
        "invalid_evidence_tokens_count": len(invalid_evidence_tokens),
        "invalid_evidence_tokens": invalid_evidence_tokens[:20],
        "unsupported_claims_sample": unsupported_claims,
    }


def llm_section_best_effort_acceptable(gate: dict[str, Any]) -> bool:
    return bool(gate.get("pass", False)) or (
        not bool(gate.get("contains_code_fence", False))
        and int(gate.get("body_chars", 0)) >= 160
        and int(gate.get("numbered_lines", 0)) == LLM_SECTION_ITEM_COUNT
        and int(gate.get("items_with_evidence", 0)) == LLM_SECTION_ITEM_COUNT
        and int(gate.get("semantically_supported_items", 0)) == LLM_SECTION_ITEM_COUNT
        and int(gate.get("invalid_evidence_tokens_count", 0)) == 0
    )


def score_llm_section_candidate(candidate: dict[str, Any]) -> tuple[Any, ...]:
    gate = candidate.get("gate", {})
    return (
        1 if gate.get("pass", False) else 0,
        int(gate.get("semantically_supported_items", 0)),
        int(gate.get("items_with_evidence", 0)),
        -int(gate.get("invalid_evidence_tokens_count", 0)),
        int(gate.get("numbered_lines", 0)),
        int(gate.get("line_count", 0)),
        int(gate.get("body_chars", 0)),
    )


def build_llm_section_feedback(spec: dict[str, str], gate: dict[str, Any]) -> str:
    lines = [
        f"Previous draft for {spec['heading']} failed the overlay format rules. Fix these issues:",
        f"- Body characters observed: {gate.get('body_chars', 0)}",
        f"- Non-empty line count observed: {gate.get('line_count', 0)}",
        f"- Numbered lines observed: {gate.get('numbered_lines', 0)}",
        f"- Numbered items with valid evidence: {gate.get('items_with_evidence', 0)}",
        f"- Semantically supported numbered items: {gate.get('semantically_supported_items', 0)}",
        f"- Invalid evidence tokens: {gate.get('invalid_evidence_tokens_count', 0)}",
        f"- Contains code fence: {gate.get('contains_code_fence', False)}",
        "- Output exactly one section with the requested heading.",
        "- After the heading, write exactly 3 numbered items using `1.`, `2.`, `3.`.",
        "- Every numbered item must end with one or more valid `[Evidence: path#Lline]` tags.",
        "- Every numbered item must also be semantically supported by the deterministic facts behind those evidence tags.",
        "- Do not use bullet points, extra headings, code fences, tables, or diagrams.",
        "- Stay strictly within the facts already present in the deterministic base section.",
    ]
    unsupported = gate.get("unsupported_claims_sample", [])[:5]
    if unsupported:
        lines.append(f"- Sample semantically unsupported claims: {' | '.join(map(str, unsupported))}")
    return "\n".join(lines)


def collect_section_allowed_line_counts(base_section: str, line_counts: dict[str, int]) -> dict[str, int]:
    narrowed: dict[str, int] = {}
    for path, _line, has_line in analyzer.extract_evidence_tokens(base_section):
        if path == "none" or not has_line:
            continue
        max_line = line_counts.get(path)
        if max_line is not None:
            narrowed[path] = int(max_line)
    if not narrowed:
        for path in sorted(line_counts.keys())[:20]:
            narrowed[path] = int(line_counts[path])
    return narrowed


def collect_section_preferred_evidence(base_section: str, line_counts: dict[str, int]) -> list[str]:
    preferred: list[str] = []
    seen: set[str] = set()
    for path, line_no, has_line in analyzer.extract_evidence_tokens(base_section):
        if path == "none" or not has_line or line_no is None:
            continue
        max_line = line_counts.get(path)
        if max_line is None or line_no < 1 or line_no > max_line:
            continue
        token = analyzer.make_evidence(path, line_no)
        if token in seen:
            continue
        seen.add(token)
        preferred.append(token)
        if len(preferred) >= LLM_SECTION_SUPPORT_SNIPPET_LIMIT:
            break
    return preferred


def build_section_allowed_evidence_text(base_section: str, line_counts: dict[str, int]) -> str:
    narrowed = collect_section_allowed_line_counts(base_section, line_counts)
    preferred = collect_section_preferred_evidence(base_section, line_counts)
    parts: list[str] = []
    if preferred:
        parts.append(
            "Preferred Exact Evidence Tokens:\n" + "\n".join([f"- {token}" for token in preferred])
        )
    parts.append(
        "Allowed File Ranges:\n"
        + analyzer.format_allowed_evidence_for_prompt(narrowed, max_items=min(len(narrowed), 40) or 20)
    )
    return "\n\n".join([part.strip() for part in parts if part.strip()])


def trim_section_fact_context(fact_context_json: str, max_chars: int = 2500) -> str:
    text = str(fact_context_json or "").strip()
    if len(text) <= max_chars:
        return text
    return text[:max_chars].rstrip() + "\n... [truncated deterministic context]"


def _compact_section_line(text: str, max_chars: int = 220) -> str:
    collapsed = re.sub(r"\s+", " ", str(text or "").strip())
    if len(collapsed) <= max_chars:
        return collapsed
    return collapsed[: max_chars - 3].rstrip() + "..."


def _load_repo_evidence_snippet(
    repo_path: str,
    evidence_token: str,
    radius: int = LLM_SECTION_SUPPORT_SNIPPET_RADIUS,
) -> str:
    path, line_no, has_line = analyzer.parse_evidence_token(evidence_token)
    if path == "none" or not has_line or line_no is None:
        return ""
    absolute = os.path.join(repo_path, path)
    if not repo_path or not os.path.isfile(absolute):
        return ""
    try:
        with open(absolute, "r", encoding="utf-8", errors="ignore") as fh:
            lines = fh.read().splitlines()
    except Exception:
        return ""
    if line_no < 1 or line_no > len(lines):
        return ""
    start = max(1, line_no - radius)
    end = min(len(lines), line_no + radius)
    snippet_lines = [f"{evidence_token}"]
    for idx in range(start, end + 1):
        snippet_lines.append(f"{idx}: {_compact_section_line(lines[idx - 1], max_chars=180)}")
    return "\n".join(snippet_lines)


def build_section_support_context(
    repo_path: str,
    base_section: str,
    fact_context_json: str,
    line_counts: dict[str, int],
) -> str:
    parts: list[str] = []
    base_facts: list[str] = []
    for line in str(base_section or "").splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("## "):
            continue
        base_facts.append(f"- {_compact_section_line(stripped, max_chars=240)}")
        if len(base_facts) >= 8:
            break
    if base_facts:
        parts.append("Section Facts:\n" + "\n".join(base_facts))

    preferred = collect_section_preferred_evidence(base_section, line_counts)
    snippet_blocks = []
    for token in preferred[:LLM_SECTION_SUPPORT_SNIPPET_LIMIT]:
        snippet = _load_repo_evidence_snippet(repo_path, token)
        if snippet:
            snippet_blocks.append(snippet)
    if snippet_blocks:
        parts.append("Exact Supporting Snippets:\n" + "\n\n".join(snippet_blocks))

    compact_context = trim_section_fact_context(fact_context_json, max_chars=1200)
    if compact_context.strip():
        parts.append("Compact Deterministic Context:\n" + compact_context)

    merged = "\n\n".join([part.strip() for part in parts if part.strip()]).strip()
    if len(merged) <= LLM_SECTION_SUPPORT_CONTEXT_CHARS:
        return merged
    return merged[:LLM_SECTION_SUPPORT_CONTEXT_CHARS].rstrip() + "\n... [truncated section context]"


def build_llm_section_prompt(
    spec: dict[str, str],
    *,
    base_section: str,
    allowed_evidence_text: str,
    support_context_text: str,
    goal_focus_text: str,
    feedback_text: str,
) -> str:
    feedback_block = f"\nFeedback To Fix:\n{feedback_text}\n" if feedback_text.strip() else ""
    return f"""
You are polishing a deterministic repository report for readability.
Reply in ENGLISH only.

Task:
- Output ONLY one markdown section with this exact heading:
  {spec["heading"]}
- After the heading, write exactly 3 numbered items using `1.`, `2.`, `3.`.
- Every numbered item MUST end with one or more `[Evidence: path#Lline]` tags.
- Use only facts that are directly supported by the deterministic base section and retrieval context.
- Reuse the exact evidence tokens shown below whenever possible.
- Prefer synthesis, prioritization, and clearer explanations over repeating raw inventory.
- Do not output code fences, diagrams, tables, bullet lists, or any extra headings.
- Do not mention quality metrics, validation, or grounding policy in the final section text.
- Mention concrete modules, routes, files, or subsystems instead of vague phrases when the support context provides them.
- If a sentence cannot be supported by the deterministic base section, replace it with a different supported sentence.
- Do not invent new evidence tokens or change line numbers.

Section purpose:
- {spec["purpose"]}

Deterministic base section to improve:
{base_section}

Goal-specific deterministic focus hints:
{goal_focus_text}

Allowed Evidence Targets:
{allowed_evidence_text}

Supplemental deterministic context:
{support_context_text}
{feedback_block}
"""


def insert_sections_after_title(report: str, section_blocks: list[str]) -> str:
    blocks = [str(item).strip() for item in section_blocks if str(item or "").strip()]
    if not blocks:
        return report
    text = str(report or "").replace("\r\n", "\n").strip()
    if not text:
        return "\n\n".join(blocks) + "\n"

    lines = text.splitlines()
    title = lines[0].rstrip()
    remainder = "\n".join(lines[1:]).lstrip("\n")
    merged = title + "\n\n" + "\n\n".join(blocks)
    if remainder:
        merged += "\n\n" + remainder
    return merged.rstrip() + "\n"


def synthesize_hybrid_report(
    *,
    repo_path: str,
    effective_mode: str,
    llm_output_policy: str,
    fact_index: dict[str, Any],
    redaction_stats: dict[str, Any],
    included_files: set[str],
    line_counts: dict[str, int],
    allowed_evidence_text: str,
    fact_context_json: str,
    goal_focus_text: str,
    goal: str = "",
    audience: str = "reviewer",
    audience_plan: Optional[dict[str, Any]] = None,
    subsystem_priority_plan: Optional[dict[str, Any]] = None,
    max_iterations: int,
    claim_support_index: Optional[dict[str, Any]] = None,
    progress_callback: Optional[Callable[[str, dict[str, Any]], None]] = None,
) -> dict[str, Any]:
    def emit_progress(status: str, **data: Any) -> None:
        if progress_callback is None:
            return
        try:
            progress_callback(status, data)
        except Exception:
            pass

    base_report = analyzer.build_deterministic_report(fact_index, redaction_stats)
    deterministic_audience_plan = audience_plan if isinstance(audience_plan, dict) else build_audience_plan(
        fact_index,
        audience=audience,
        goal=goal,
    )
    deterministic_priority_plan = (
        subsystem_priority_plan
        if isinstance(subsystem_priority_plan, dict)
        else build_subsystem_priority_plan(
            fact_index,
            goal=goal,
            audience=audience,
        )
    )
    base_report = insert_sections_after_title(
        base_report,
        [
            render_audience_plan_markdown(deterministic_audience_plan),
            render_subsystem_priority_markdown(deterministic_priority_plan),
        ],
    )
    base_report = analyzer.sanitize_all_mermaid(base_report)
    base_validation = analyzer.validate_report_grounding(
        base_report,
        included_files,
        line_counts,
        claim_support_index=claim_support_index,
    )
    base_gate = analyzer.evaluate_grounding_gate(base_validation)

    final_text = base_report
    final_validation = base_validation
    final_gate = base_gate
    source = "deterministic_initial" if effective_mode == "deterministic" else "deterministic_base_only"
    enhancement_records: list[dict[str, Any]] = []
    applied_sections: list[dict[str, Any]] = []

    if effective_mode != "agent":
        return {
            "report": final_text,
            "validation": final_validation,
            "gate": final_gate,
            "source": source,
            "llm_enhancements": {
                "requested": False,
                "base_gate_pass": bool(base_gate.get("pass", False)),
                "accepted_sections_count": 0,
                "accepted_section_headings": [],
                "rejected_section_headings": [],
                "sections": [],
            },
        }

    record_map: dict[str, dict[str, Any]] = {}
    candidate_sections: list[dict[str, Any]] = []
    total_sections = len(LLM_SECTION_ENHANCEMENT_SPECS)
    emit_progress(
        "start",
        total_sections=total_sections,
        max_iterations=max(1, int(max_iterations or 1)),
    )
    for index, spec in enumerate(LLM_SECTION_ENHANCEMENT_SPECS, start=1):
        record = {
            "key": spec["key"],
            "heading": spec["heading"],
            "source_heading": spec["source_heading"],
            "status": "pending",
            "accepted_policy": "",
            "attempt_count": 0,
            "error": "",
        }
        enhancement_records.append(record)
        record_map[spec["key"]] = record
        emit_progress(
            "section_start",
            key=spec["key"],
            heading=spec["heading"],
            section_index=index,
            total_sections=total_sections,
        )

        base_section = extract_markdown_section(base_report, spec["source_heading"])
        if not base_section.strip():
            record["status"] = "skipped_missing_source_section"
            emit_progress(
                "section_skipped",
                key=spec["key"],
                heading=spec["heading"],
                reason="missing_source_section",
                section_index=index,
                total_sections=total_sections,
            )
            continue
        section_allowed_evidence_text = build_section_allowed_evidence_text(base_section, line_counts)
        section_support_context = build_section_support_context(
            repo_path,
            base_section,
            fact_context_json,
            line_counts,
        )

        feedback_text = ""
        best_candidate: Optional[dict[str, Any]] = None
        accepted_candidate: Optional[dict[str, Any]] = None
        for iteration in range(1, max(1, int(max_iterations or 1)) + 1):
            record["attempt_count"] = iteration
            emit_progress(
                "section_attempt",
                key=spec["key"],
                heading=spec["heading"],
                section_index=index,
                total_sections=total_sections,
                iteration=iteration,
                max_iterations=max(1, int(max_iterations or 1)),
            )
            try:
                prompt = build_llm_section_prompt(
                    spec,
                    base_section=base_section,
                    allowed_evidence_text=section_allowed_evidence_text,
                    support_context_text=section_support_context,
                    goal_focus_text=goal_focus_text,
                    feedback_text=feedback_text,
                )
                draft = analyzer.ollama_chat_with_retry(
                    model=analyzer.active_model(),
                    system=SYSTEM_PROMPT,
                    user=prompt,
                    temperature=0.2,
                )
                draft = maybe_translate_to_english(draft)
                normalized = normalize_llm_section_output(draft, spec["heading"])
                gate = evaluate_llm_section_gate(
                    normalized,
                    allowed_line_counts=line_counts,
                    claim_support_index=claim_support_index,
                )
                candidate = {
                    "key": spec["key"],
                    "heading": spec["heading"],
                    "iteration": iteration,
                    "markdown": normalized,
                    "gate": gate,
                }
                if best_candidate is None or score_llm_section_candidate(candidate) > score_llm_section_candidate(best_candidate):
                    best_candidate = candidate

                record["last_fragment_gate"] = {
                    "pass": gate.get("pass", False),
                    "body_chars": gate.get("body_chars", 0),
                    "line_count": gate.get("line_count", 0),
                    "numbered_lines": gate.get("numbered_lines", 0),
                    "items_with_evidence": gate.get("items_with_evidence", 0),
                    "invalid_evidence_tokens_count": gate.get("invalid_evidence_tokens_count", 0),
                    "contains_code_fence": gate.get("contains_code_fence", False),
                }
                if gate.get("pass", False):
                    accepted_candidate = candidate
                    record["status"] = "accepted_fragment"
                    record["accepted_policy"] = "strict_gate"
                    emit_progress(
                        "section_fragment_accepted",
                        key=spec["key"],
                        heading=spec["heading"],
                        section_index=index,
                        total_sections=total_sections,
                        iteration=iteration,
                        accepted_policy="strict_gate",
                    )
                    break
                feedback_text = build_llm_section_feedback(spec, gate)
            except Exception as e:
                record["error"] = str(e)
                feedback_text = f"Previous attempt failed with runtime error: {e}"
                emit_progress(
                    "section_attempt_error",
                    key=spec["key"],
                    heading=spec["heading"],
                    section_index=index,
                    total_sections=total_sections,
                    iteration=iteration,
                    error=str(e),
                )

        if accepted_candidate is None and analyzer.llm_best_effort_enabled(llm_output_policy) and best_candidate:
            best_gate = dict(best_candidate.get("gate", {}))
            if llm_section_best_effort_acceptable(best_gate):
                accepted_candidate = best_candidate
                record["status"] = "accepted_fragment"
                record["accepted_policy"] = "best_effort"
                emit_progress(
                    "section_fragment_accepted",
                    key=spec["key"],
                    heading=spec["heading"],
                    section_index=index,
                    total_sections=total_sections,
                    iteration=int(best_candidate.get("iteration", 0) or 0),
                    accepted_policy="best_effort",
                )

        if accepted_candidate is None:
            if record["status"] == "pending":
                record["status"] = "rejected_fragment"
            emit_progress(
                "section_rejected",
                key=spec["key"],
                heading=spec["heading"],
                section_index=index,
                total_sections=total_sections,
                reason=record["status"],
            )
            continue

        candidate_sections.append(accepted_candidate)
        record["accepted_iteration"] = int(accepted_candidate.get("iteration", 0) or 0)

    applied_blocks: list[str] = []
    for candidate in candidate_sections:
        trial_report = insert_sections_after_title(base_report, applied_blocks + [str(candidate.get("markdown", "")).strip()])
        trial_report = analyzer.sanitize_all_mermaid(trial_report)
        trial_validation = analyzer.validate_report_grounding(
            trial_report,
            included_files,
            line_counts,
            claim_support_index=claim_support_index,
        )
        trial_gate = analyzer.evaluate_grounding_gate(trial_validation)
        record = record_map.get(str(candidate.get("key", "")), {})
        if trial_gate.get("pass", False):
            applied_blocks.append(str(candidate.get("markdown", "")).strip())
            applied_sections.append(
                {
                    "key": str(candidate.get("key", "")),
                    "heading": str(candidate.get("heading", "")),
                    "iteration": int(candidate.get("iteration", 0) or 0),
                    "accepted_policy": str(record.get("accepted_policy", "")).strip(),
                    "markdown": str(candidate.get("markdown", "")).strip(),
                }
            )
            record["status"] = "applied"
            emit_progress(
                "section_applied",
                key=str(candidate.get("key", "")),
                heading=str(candidate.get("heading", "")),
                applied_sections_count=len(applied_sections),
                total_sections=total_sections,
            )
            final_text = trial_report
            final_validation = trial_validation
            final_gate = trial_gate
        else:
            record["status"] = "rejected_full_report_gate"
            record["full_report_gate"] = {
                "pass": trial_gate.get("pass", False),
                "coverage": trial_gate.get("coverage", 0.0),
                "semantic_coverage": trial_gate.get("semantic_coverage", 1.0),
            }
            emit_progress(
                "section_rejected",
                key=str(candidate.get("key", "")),
                heading=str(candidate.get("heading", "")),
                reason="full_report_gate",
                total_sections=total_sections,
            )

    accepted_headings = [item.get("heading", "") for item in applied_sections if str(item.get("heading", "")).strip()]
    rejected_headings = [
        item.get("heading", "")
        for item in enhancement_records
        if item.get("status") not in {"applied"}
    ]
    if applied_sections:
        source = "deterministic_with_llm_sections"
    emit_progress(
        "complete",
        total_sections=total_sections,
        applied_sections_count=len(applied_sections),
        accepted_sections_count=len(candidate_sections),
        source=source,
        gate_pass=bool(final_gate.get("pass", False)),
    )

    return {
        "report": final_text,
        "validation": final_validation,
        "gate": final_gate,
        "source": source,
        "llm_enhancements": {
            "requested": True,
            "base_gate_pass": bool(base_gate.get("pass", False)),
            "accepted_sections_count": len(accepted_headings),
            "accepted_section_headings": accepted_headings,
            "rejected_section_headings": rejected_headings,
            "sections": enhancement_records,
            "applied_sections": applied_sections,
        },
    }


def maybe_translate_to_english(text: str) -> str:
    if not analyzer.has_cjk(text):
        return text

    translate_prompt = f"""
Translate the following text to ENGLISH.
Rules:
* Output ONLY English.
* Keep headings, bullet formatting, and code blocks unchanged where possible.
* Do not include any Chinese characters.

TEXT:
{text}
"""
    return analyzer.ollama_chat_with_retry(
        model=analyzer.active_model(),
        system="Output ENGLISH only. No Chinese characters.",
        user=translate_prompt,
        temperature=0.0,
    )


def ensure_llm_backend_ready() -> dict[str, Any]:
    status = analyzer.probe_llm_backend()
    if not status.get("healthy") or not str(status.get("selected_model", "")).strip():
        raise RuntimeError(str(status.get("error", "")).strip() or "Local LLM backend health check failed.")
    analyzer.set_active_model_override(str(status.get("selected_model", "")).strip())
    return status


def run_agent_document(args: argparse.Namespace) -> int:
    repo_path = os.path.abspath(os.path.expanduser(args.repo))
    if not os.path.isdir(repo_path):
        print(f"❌ Path is not a folder: {repo_path}")
        return 1

    runs_dir = analyzer.resolve_runs_dir(args.runs_dir, repo_path=repo_path)
    report_home_dir = analyzer.default_repo_report_home(repo_path) if not str(args.runs_dir or "").strip() else ""
    llm_output_policy = analyzer.resolve_llm_output_policy(getattr(args, "llm_output_policy", ""))
    if args.mode == "agent" and analyzer.llm_best_effort_enabled(llm_output_policy):
        args.require_llm = True
    overall_t0 = time.perf_counter()
    repo_meta = get_repo_metadata(repo_path)
    scan_config = analyzer.load_repo_scan_config(repo_path)
    scan_config = analyzer.apply_policy_packs_to_scan_config(
        scan_config,
        getattr(args, "policy_pack", []),
        source="cli",
    )
    requested_grounding_profile = str(getattr(args, "grounding_profile", "")).strip() or analyzer.active_grounding_profile()
    if not bool(getattr(args, "grounding_profile_explicit", False)):
        recommended_grounding_profile = analyzer.normalize_grounding_profile(scan_config.get("recommended_grounding_profile", ""))
        if recommended_grounding_profile:
            requested_grounding_profile = recommended_grounding_profile
    analyzer.set_active_grounding_profile_override(requested_grounding_profile)
    runtime_config = analyzer.merge_runtime_probe_config(
        repo_path,
        scan_config,
        enabled=args.runtime_probe,
        commands=args.runtime_command,
        timeout_seconds=args.runtime_timeout_seconds,
        max_output_chars=args.runtime_max_output_chars,
    )
    effective_scan_config = analyzer.apply_runtime_config_to_scan_config(scan_config, runtime_config)
    requested_mode = args.mode
    effective_mode = requested_mode
    analyzer.clear_active_model_override()
    backend_status: dict[str, Any] = {
        "backend": analyzer.LLM_BACKEND,
        "healthy": False,
        "primary_model": analyzer.active_model(),
        "candidate_models": analyzer.model_candidates(),
        "available_models": [],
        "selected_model": "",
        "requested_mode": requested_mode,
        "effective_mode": requested_mode,
        "llm_output_policy": llm_output_policy,
        "grounding_profile": analyzer.active_grounding_profile(),
        "require_llm": bool(args.require_llm),
        "error": "",
    }
    if requested_mode == "agent":
        try:
            backend_status = ensure_llm_backend_ready()
            backend_status["requested_mode"] = requested_mode
            backend_status["require_llm"] = bool(args.require_llm)
        except Exception as e:
            backend_status["error"] = str(e)
            backend_status["requested_mode"] = requested_mode
            backend_status["require_llm"] = bool(args.require_llm)
            if args.require_llm:
                print(f"❌ {e}")
                return 1
            effective_mode = "deterministic"
            print(f"[WARN] Agent mode requested but local LLM is unavailable. Falling back to deterministic mode: {e}")
    backend_status["effective_mode"] = effective_mode

    resume_run_path = resolve_resume_run_path(runs_dir, args.resume_run)
    resuming = bool(resume_run_path)
    if resuming:
        run_path = resume_run_path
        state = load_run_state(run_path)
        if not isinstance(state, dict):
            print(f"❌ Resume run is missing {STATE_FILENAME}: {run_path}")
            return 1
        prior_repo_path = normalize_repo_path_value(str(state.get("repo_path", "")).strip()) if str(state.get("repo_path", "")).strip() else ""
        if prior_repo_path and prior_repo_path != normalize_repo_path_value(repo_path):
            print(f"❌ Resume run repo mismatch. Existing run repo={prior_repo_path} current repo={normalize_repo_path_value(repo_path)}")
            return 1
        if str(state.get("status", "")).strip() == "completed":
            print(f"❌ Run is already completed and does not need resume: {run_path}")
            return 1
        run_id = str(state.get("run_id", "")).strip() or os.path.basename(run_path.rstrip("/\\"))
        state = ensure_run_state_defaults(state, repo_path=repo_path, requested_mode=requested_mode, effective_mode=effective_mode)
        state["run_id"] = run_id
        state["goal"] = args.goal.strip()
        state["audience"] = normalize_doc_audience(getattr(args, "audience", ""))
        state["repo_path"] = repo_path
        state["repo_metadata"] = repo_meta
        state["backend"] = analyzer.LLM_BACKEND
        state["model"] = analyzer.active_model() if effective_mode == "agent" else "deterministic_only"
        state["max_iterations"] = args.max_iterations
        state["llm_output_policy"] = llm_output_policy
        state["requested_mode"] = requested_mode
        state["mode"] = effective_mode
        state["status"] = "running"
        state["completed_at"] = None
        state["finished_at"] = None
        state["attempt_count"] = int(state.get("attempt_count", 1) or 1) + 1
        state["resume_count"] = int(state.get("resume_count", 0) or 0) + 1
        state["current_stage"] = "resume"
        state.pop("error", None)
        state.pop("failure", None)
        clear_failure_artifact(run_path)
        add_event(state, "resume", "Resuming prior run from saved checkpoints.", data={"run_path": run_path})
    else:
        run_id, run_path = make_run_dir(runs_dir)
        state = {
            "run_id": run_id,
            "started_at": utc_now_iso(),
            "completed_at": None,
            "status": "running",
            "requested_mode": requested_mode,
            "mode": effective_mode,
            "goal": args.goal.strip(),
            "audience": normalize_doc_audience(getattr(args, "audience", "")),
            "repo_path": repo_path,
            "repo_metadata": repo_meta,
            "backend": analyzer.LLM_BACKEND,
            "model": analyzer.active_model() if effective_mode == "agent" else "deterministic_only",
            "max_iterations": args.max_iterations,
            "llm_output_policy": llm_output_policy,
            "events": [],
            "artifacts": {},
            "attempt_count": 1,
            "resume_count": 0,
            "current_stage": "plan",
        }
    run_lock_path = os.path.join(run_path, RUN_LOCK_FILENAME)
    run_heartbeat_path = os.path.join(run_path, HEARTBEAT_FILENAME)
    effective_scan_config = analyzer.augment_scan_config_with_repo_artifact_exclusions(
        repo_path,
        effective_scan_config,
        [runs_dir, run_path, analyzer.OUTPUT_DIR],
    )
    state["artifacts"]["run_lock"] = run_lock_path
    state["artifacts"]["run_heartbeat"] = run_heartbeat_path
    run_llm_backend_status_path = os.path.join(run_path, "llm_backend_status.json")
    run_security_policy_audit_path = os.path.join(run_path, "security_policy_audit.json")
    state["artifacts"]["run_llm_backend_status"] = run_llm_backend_status_path
    security_policy_audit = analyzer.build_security_policy_audit(
        effective_scan_config,
        runtime_config,
        requested_mode=requested_mode,
        effective_mode=effective_mode,
    )
    state["artifacts"]["run_security_policy_audit"] = run_security_policy_audit_path
    if resuming:
        add_event(state, "plan", "Reloaded run state and refreshed control artifacts for resume.")
    else:
        add_event(state, "plan", "Created agent run state and execution plan.")
    lock_acquired = False
    try:
        lock_info = acquire_run_lock(
            run_path,
            run_id=run_id,
            attempt_count=int(state.get("attempt_count", 1) or 1),
        )
        lock_acquired = True
        if lock_info.get("stale_reclaimed"):
            add_event(state, "resume" if resuming else "plan", "Reclaimed stale run lock before continuing.")
            print(f"[WARN] Reclaimed stale run lock for {run_path}")
        write_json(run_llm_backend_status_path, backend_status)
        write_json(run_security_policy_audit_path, security_policy_audit)
        if args.write_root_outputs:
            analyzer.save_fact_index(analyzer.SECURITY_POLICY_AUDIT_FILE, security_policy_audit)
            state["artifacts"]["root_security_policy_audit"] = analyzer.SECURITY_POLICY_AUDIT_FILE
        save_state(run_path, state)
    except Exception as e:
        if lock_acquired:
            release_run_lock(run_path)
        print(f"❌ {e}")
        return 1

        print(f"[INFO] run_id={run_id}")
        print(f"[INFO] run_path={run_path}")
        if report_home_dir:
            print(f"[INFO] desktop_report_home={report_home_dir}")
        print(f"[INFO] attempt_count={state.get('attempt_count', 1)}")
    print(f"[INFO] requested_mode={requested_mode}")
    print(f"[INFO] effective_mode={effective_mode}")
    print(f"[INFO] runtime_probe={bool(runtime_config.get('enabled', False))}")
    print(f"[INFO] runtime_commands={len(runtime_config.get('commands', []))}")
    print(f"[INFO] security_policy={analyzer.summarize_security_policy(effective_scan_config.get('security_policy', {}))}")
    if backend_status.get("selected_model"):
        print(f"[INFO] selected_model={backend_status.get('selected_model')}")
    if backend_status.get("error"):
        print(f"[INFO] llm_backend_status_error={backend_status.get('error')}")
    if not security_policy_audit.get("pass", False):
        print(f"❌ Security policy blocked execution: {'; '.join(security_policy_audit.get('violations', [])[:3])}")
        state["status"] = "failed_security_policy"
        state["current_stage"] = "plan"
        state["completed_at"] = utc_now_iso()
        failure_path = write_failure_artifact(
            run_path,
            run_id=run_id,
            repo_path=repo_path,
            stage="plan",
            status="failed_security_policy",
            error="; ".join(security_policy_audit.get("violations", [])[:3]),
            tb_text="",
            resumable=False,
            attempt_count=int(state.get("attempt_count", 1) or 1),
        )
        state["artifacts"]["run_failure"] = failure_path
        save_error = safe_save_state(run_path, state)
        if lock_acquired:
            release_run_lock(run_path)
        if save_error:
            print(f"[WARN] Failed to persist state after security policy block: {save_error}")
        print(f"[SAVED] {failure_path}")
        return 1
    if repo_meta.get("git", {}).get("is_git_repo"):
        print(
            "[INFO] git_repo branch="
            f"{repo_meta['git'].get('branch', '')} "
            f"commit={repo_meta['git'].get('commit', '')[:12]} "
            f"dirty={repo_meta['git'].get('dirty')}"
        )
    if args.goal.strip():
        print(f"[INFO] goal={args.goal.strip()}")

    current_stage = "plan"
    try:
        current_stage = "gather"
        state["current_stage"] = current_stage
        add_event(state, "gather", "Reading repository and applying pre-LLM redaction.")
        save_state(run_path, state)
        gather_t0 = time.perf_counter()
        reused_gather_checkpoint = False
        resume_gather = load_gather_resume_context(run_path) if resuming else None
        if resume_gather:
            _code, resume_redaction_stats = analyzer.read_files(
                repo_path,
                max_chars=analyzer.MAX_CHARS,
                collect_text=False,
                scan_config=effective_scan_config,
            )
            resume_included_files = set([p.replace("\\", "/") for p in resume_redaction_stats.get("included_files", [])])
            resume_line_counts = {
                p.replace("\\", "/"): int(n)
                for p, n in resume_redaction_stats.get("line_counts", {}).items()
            }
            current_fingerprint = compute_repo_fingerprint(resume_included_files, resume_line_counts) if resume_included_files else ""
            if current_fingerprint and current_fingerprint == str(resume_gather.get("repo_fingerprint", "")).strip():
                reused_gather_checkpoint = True
                redaction_stats = resume_gather["redaction_stats"]
                included_files = resume_gather["included_files"]
                line_counts = resume_gather["line_counts"]
                repo_fingerprint = str(resume_gather.get("repo_fingerprint", "")).strip()
                fact_index_cache_stats = resume_gather["fact_index_cache_stats"]
                fact_index = resume_gather["fact_index"]
                model_safe_fact_index = resume_gather["model_safe_fact_index"]
                prompt_fact_context = resume_gather["prompt_fact_context"]
                claim_support_index = resume_gather["claim_support_index"]
                runtime_config = analyzer.resolve_runtime_probe_config(fact_index, resume_gather.get("runtime_config", runtime_config))
                state["scan_stats"] = {
                    "files_read": int(resume_redaction_stats.get("files_read", 0)),
                    "chars_scanned": int(resume_redaction_stats.get("chars_scanned", 0)),
                    "chars_collected": int(resume_redaction_stats.get("chars_collected", 0)),
                    "skipped_by_size_count": int(resume_redaction_stats.get("skipped_by_size_count", 0)),
                }
                state["scan_config"] = {
                    "config_path": resume_redaction_stats.get("scan_config_path", ""),
                    "max_file_bytes": resume_redaction_stats.get("max_file_bytes"),
                    "security_policy_path": resume_redaction_stats.get("security_policy_path", ""),
                    "security_policy_name": resume_redaction_stats.get("security_policy_name", ""),
                    "policy_packs": resume_redaction_stats.get("policy_packs", []),
                }
                security_policy_audit = analyzer.build_security_policy_audit(
                    effective_scan_config,
                    runtime_config,
                    requested_mode=requested_mode,
                    effective_mode=effective_mode,
                    redaction_stats=redaction_stats,
                )
                write_json(run_security_policy_audit_path, security_policy_audit)
                if args.write_root_outputs:
                    analyzer.save_fact_index(analyzer.SECURITY_POLICY_AUDIT_FILE, security_policy_audit)
                if not security_policy_audit.get("pass", False):
                    raise RuntimeError(
                        f"Security policy blocked execution after resume verification: {'; '.join(security_policy_audit.get('violations', [])[:3])}"
                    )
                state["fact_index_cache"] = fact_index_cache_stats
                state["artifacts"]["run_gather_checkpoint"] = os.path.join(run_path, GATHER_CHECKPOINT_FILENAME)
                gather_sec = time.perf_counter() - gather_t0
                add_event(
                    state,
                    "resume",
                    "Reused gather checkpoint after fingerprint verification.",
                    data={"gather_sec": round(gather_sec, 3), "repo_fingerprint": repo_fingerprint[:16]},
                )
            else:
                add_event(state, "resume", "Gather checkpoint invalidated because repository fingerprint changed.")

        if not reused_gather_checkpoint:
            _code, redaction_stats = analyzer.read_files(
                repo_path,
                max_chars=analyzer.MAX_CHARS,
                collect_text=False,
                scan_config=effective_scan_config,
            )
            included_files = set([p.replace("\\", "/") for p in redaction_stats.get("included_files", [])])
            line_counts = {
                p.replace("\\", "/"): int(n)
                for p, n in redaction_stats.get("line_counts", {}).items()
            }
            if not included_files:
                raise RuntimeError("No files were collected. Check include extensions, skip rules, and max file size settings.")
            repo_fingerprint = compute_repo_fingerprint(included_files, line_counts)
            state["repo_fingerprint"] = repo_fingerprint
            state["scan_stats"] = {
                "files_read": int(redaction_stats.get("files_read", 0)),
                "chars_scanned": int(redaction_stats.get("chars_scanned", 0)),
                "chars_collected": int(redaction_stats.get("chars_collected", 0)),
                "skipped_by_size_count": int(redaction_stats.get("skipped_by_size_count", 0)),
            }
            state["scan_config"] = {
                "config_path": redaction_stats.get("scan_config_path", ""),
                "max_file_bytes": redaction_stats.get("max_file_bytes"),
                "security_policy_path": redaction_stats.get("security_policy_path", ""),
                "security_policy_name": redaction_stats.get("security_policy_name", ""),
                "policy_packs": redaction_stats.get("policy_packs", []),
            }
            fact_index, fact_index_cache_stats = analyzer.build_local_fact_index_incremental(
                repo_path=repo_path,
                included_files=sorted(list(included_files)),
                line_counts=line_counts,
                use_cache=True,
            )
            runtime_config = analyzer.resolve_runtime_probe_config(fact_index, runtime_config)
            security_policy_audit = analyzer.build_security_policy_audit(
                effective_scan_config,
                runtime_config,
                requested_mode=requested_mode,
                effective_mode=effective_mode,
                redaction_stats=redaction_stats,
            )
            write_json(run_security_policy_audit_path, security_policy_audit)
            if args.write_root_outputs:
                analyzer.save_fact_index(analyzer.SECURITY_POLICY_AUDIT_FILE, security_policy_audit)
            if not security_policy_audit.get("pass", False):
                raise RuntimeError(
                    f"Security policy blocked execution after scan: {'; '.join(security_policy_audit.get('violations', [])[:3])}"
                )

            run_runtime_observations_path = os.path.join(run_path, "runtime_observations.md")
            runtime_data = analyzer.collect_runtime_observations(
                repo_path=repo_path,
                fact_index=fact_index,
                runtime_config=runtime_config,
                artifact_path=run_runtime_observations_path,
            )
            fact_index = analyzer.apply_runtime_observations_to_fact_index(fact_index, runtime_data)
            fact_index = analyzer.refresh_architecture_views(fact_index)
            extra_evidence_targets: dict[str, int] = {}
            if runtime_data.get("artifact_path") and int(runtime_data.get("line_count", 0) or 0) > 0:
                extra_evidence_targets[str(runtime_data.get("artifact_path"))] = int(runtime_data.get("line_count", 0) or 0)
                state["artifacts"]["run_runtime_observations"] = run_runtime_observations_path
                if args.write_root_outputs:
                    shutil.copyfile(run_runtime_observations_path, analyzer.RUNTIME_OBSERVATIONS_FILE)
                    state["artifacts"]["root_runtime_observations"] = analyzer.RUNTIME_OBSERVATIONS_FILE
            included_files, line_counts = analyzer.merge_extra_evidence_targets(
                included_files,
                line_counts,
                extra_evidence_targets,
            )
            gather_sec = time.perf_counter() - gather_t0
            model_safe_fact_index = analyzer.build_model_safe_fact_index(fact_index)
            prompt_fact_context = analyzer.build_prompt_fact_context(fact_index)
            claim_support_index = analyzer.build_claim_support_index(fact_index, redaction_stats=redaction_stats)
            print(
                "[INFO] fact_index_cache_hits="
                f"{fact_index_cache_stats.get('cache_hits', 0)} "
                f"misses={fact_index_cache_stats.get('cache_misses', 0)}"
            )

            run_fact_path = os.path.join(run_path, "fact_index.json")
            analyzer.save_fact_index(run_fact_path, fact_index)
            state["artifacts"]["run_fact_index"] = run_fact_path
            run_model_safe_fact_path = os.path.join(run_path, "model_safe_fact_index.json")
            analyzer.save_fact_index(run_model_safe_fact_path, model_safe_fact_index)
            state["artifacts"]["run_model_safe_fact_index"] = run_model_safe_fact_path
            run_prompt_fact_context_path = os.path.join(run_path, "prompt_fact_context.json")
            analyzer.save_fact_index(run_prompt_fact_context_path, prompt_fact_context)
            state["artifacts"]["run_prompt_fact_context"] = run_prompt_fact_context_path
            run_claim_support_index_path = os.path.join(run_path, "claim_support_index.json")
            analyzer.save_fact_index(run_claim_support_index_path, claim_support_index)
            state["artifacts"]["run_claim_support_index"] = run_claim_support_index_path
            add_event(
                state,
                "gather",
                "Built deterministic fact index.",
                data={
                    "files": len(fact_index.get("files", [])),
                    "endpoints": len(fact_index.get("api_endpoints", [])),
                    "dependencies": len(fact_index.get("dependencies", [])),
                    "runtime_observations": len(fact_index.get("runtime_observations", [])),
                    "cache_hits": fact_index_cache_stats.get("cache_hits", 0),
                    "cache_misses": fact_index_cache_stats.get("cache_misses", 0),
                    "gather_sec": round(gather_sec, 3),
                },
            )
            state["fact_index_cache"] = fact_index_cache_stats
            if args.write_root_outputs:
                analyzer.save_fact_index(analyzer.FACT_INDEX_FILE, fact_index)
                state["artifacts"]["root_fact_index"] = analyzer.FACT_INDEX_FILE
                analyzer.save_fact_index(analyzer.MODEL_SAFE_FACT_INDEX_FILE, model_safe_fact_index)
                state["artifacts"]["root_model_safe_fact_index"] = analyzer.MODEL_SAFE_FACT_INDEX_FILE
                analyzer.save_fact_index(analyzer.PROMPT_FACT_CONTEXT_FILE, prompt_fact_context)
                state["artifacts"]["root_prompt_fact_context"] = analyzer.PROMPT_FACT_CONTEXT_FILE
                analyzer.save_fact_index(analyzer.CLAIM_SUPPORT_INDEX_FILE, claim_support_index)
                state["artifacts"]["root_claim_support_index"] = analyzer.CLAIM_SUPPORT_INDEX_FILE
                write_json(analyzer.LLM_BACKEND_STATUS_FILE, backend_status)
                state["artifacts"]["root_llm_backend_status"] = analyzer.LLM_BACKEND_STATUS_FILE
            save_gather_checkpoint(
                run_path,
                {
                    "repo_fingerprint": repo_fingerprint,
                    "included_files": sorted(list(included_files)),
                    "line_counts": line_counts,
                    "redaction_stats": redaction_stats,
                    "fact_index_cache_stats": fact_index_cache_stats,
                    "runtime_config": runtime_config,
                    "artifacts": {
                        "run_fact_index": state["artifacts"].get("run_fact_index", ""),
                        "run_model_safe_fact_index": state["artifacts"].get("run_model_safe_fact_index", ""),
                        "run_prompt_fact_context": state["artifacts"].get("run_prompt_fact_context", ""),
                        "run_claim_support_index": state["artifacts"].get("run_claim_support_index", ""),
                    },
                },
            )
            state["artifacts"]["run_gather_checkpoint"] = os.path.join(run_path, GATHER_CHECKPOINT_FILENAME)
            save_state(run_path, state)

        state["repo_fingerprint"] = repo_fingerprint
        run_fact_path = str(state.get("artifacts", {}).get("run_fact_index", "")).strip() or os.path.join(run_path, "fact_index.json")
        state["artifacts"]["run_fact_index"] = run_fact_path
        run_model_safe_fact_path = str(state.get("artifacts", {}).get("run_model_safe_fact_index", "")).strip() or os.path.join(run_path, "model_safe_fact_index.json")
        state["artifacts"]["run_model_safe_fact_index"] = run_model_safe_fact_path
        run_prompt_fact_context_path = str(state.get("artifacts", {}).get("run_prompt_fact_context", "")).strip() or os.path.join(run_path, "prompt_fact_context.json")
        state["artifacts"]["run_prompt_fact_context"] = run_prompt_fact_context_path
        run_claim_support_index_path = str(state.get("artifacts", {}).get("run_claim_support_index", "")).strip() or os.path.join(run_path, "claim_support_index.json")
        state["artifacts"]["run_claim_support_index"] = run_claim_support_index_path
        if args.write_root_outputs and reused_gather_checkpoint:
            analyzer.save_fact_index(analyzer.FACT_INDEX_FILE, fact_index)
            state["artifacts"]["root_fact_index"] = analyzer.FACT_INDEX_FILE
            analyzer.save_fact_index(analyzer.MODEL_SAFE_FACT_INDEX_FILE, model_safe_fact_index)
            state["artifacts"]["root_model_safe_fact_index"] = analyzer.MODEL_SAFE_FACT_INDEX_FILE
            analyzer.save_fact_index(analyzer.PROMPT_FACT_CONTEXT_FILE, prompt_fact_context)
            state["artifacts"]["root_prompt_fact_context"] = analyzer.PROMPT_FACT_CONTEXT_FILE
            analyzer.save_fact_index(analyzer.CLAIM_SUPPORT_INDEX_FILE, claim_support_index)
            state["artifacts"]["root_claim_support_index"] = analyzer.CLAIM_SUPPORT_INDEX_FILE
            write_json(analyzer.LLM_BACKEND_STATUS_FILE, backend_status)
            state["artifacts"]["root_llm_backend_status"] = analyzer.LLM_BACKEND_STATUS_FILE
        prompt_fact_index_json = json.dumps(prompt_fact_context, ensure_ascii=True, indent=2)

        allowed_files_text = analyzer.format_allowed_files_for_prompt(list(included_files))
        allowed_evidence_text = analyzer.format_allowed_evidence_for_prompt(line_counts)
        audience_name = normalize_doc_audience(getattr(args, "audience", ""))
        audience_plan = build_audience_plan(
            fact_index,
            audience=audience_name,
            goal=args.goal,
        )
        subsystem_priority_plan = build_subsystem_priority_plan(
            fact_index,
            goal=args.goal,
            audience=audience_name,
        )
        audience_plan_json_path = os.path.join(run_path, "audience_plan.json")
        audience_plan_md_path = os.path.join(run_path, "audience_plan.md")
        subsystem_priority_json_path = os.path.join(run_path, "subsystem_priorities.json")
        subsystem_priority_md_path = os.path.join(run_path, "subsystem_priorities.md")
        write_json(audience_plan_json_path, audience_plan)
        write_text(audience_plan_md_path, render_audience_plan_markdown(audience_plan))
        write_json(subsystem_priority_json_path, subsystem_priority_plan)
        write_text(subsystem_priority_md_path, render_subsystem_priority_markdown(subsystem_priority_plan))
        state["audience"] = audience_name
        state["artifacts"]["run_audience_plan"] = audience_plan_json_path
        state["artifacts"]["run_audience_plan_markdown"] = audience_plan_md_path
        state["artifacts"]["run_subsystem_priorities"] = subsystem_priority_json_path
        state["artifacts"]["run_subsystem_priorities_markdown"] = subsystem_priority_md_path
        goal_focus = build_goal_focus(fact_index, args.goal)
        goal_focus_text = "\n\n".join(
            [
                format_goal_focus(goal_focus),
                "Audience-specific deterministic guidance:\n" + format_audience_plan_for_prompt(audience_plan),
            ]
        )

        current_stage = "synthesize"
        state["current_stage"] = current_stage
        add_event(state, "synthesize", "Starting documentation synthesis loop.")
        if effective_mode == "agent":
            state["synthesis_progress"] = {
                "status": "starting",
                "updated_at": utc_now_iso(),
                "total_sections": len(LLM_SECTION_ENHANCEMENT_SPECS),
                "completed_sections": 0,
                "accepted_sections": 0,
                "current_heading": "",
                "current_iteration": 0,
                "max_iterations": int(args.max_iterations or 1),
            }
        save_state(run_path, state)
        synth_t0 = time.perf_counter()
        if effective_mode == "agent":
            print(
                f"[INFO] synthesize_sections={len(LLM_SECTION_ENHANCEMENT_SPECS)} "
                f"max_iterations={int(args.max_iterations or 1)}"
            )

        def on_synthesis_progress(status: str, payload: dict[str, Any]) -> None:
            if effective_mode != "agent":
                return
            progress = state.setdefault("synthesis_progress", {})
            progress["status"] = status
            progress["updated_at"] = utc_now_iso()
            if "total_sections" in payload:
                progress["total_sections"] = int(payload.get("total_sections", 0) or 0)
            if "heading" in payload:
                progress["current_heading"] = str(payload.get("heading", "")).strip()
            if "iteration" in payload:
                progress["current_iteration"] = int(payload.get("iteration", 0) or 0)
            if "max_iterations" in payload:
                progress["max_iterations"] = int(payload.get("max_iterations", 0) or 0)
            if status == "section_applied":
                progress["completed_sections"] = int(payload.get("applied_sections_count", 0) or 0)
                progress["accepted_sections"] = int(payload.get("applied_sections_count", 0) or 0)
            elif status == "section_fragment_accepted":
                progress["accepted_sections"] = int(progress.get("accepted_sections", 0) or 0) + 1
            elif status == "complete":
                progress["completed_sections"] = int(payload.get("applied_sections_count", 0) or 0)
                progress["accepted_sections"] = int(payload.get("accepted_sections_count", 0) or 0)
            message = ""
            heading = str(payload.get("heading", "")).strip()
            if status == "section_start":
                message = (
                    f"[INFO] synthesize_section={heading} "
                    f"({int(payload.get('section_index', 0) or 0)}/{int(payload.get('total_sections', 0) or 0)})"
                )
            elif status == "section_attempt":
                message = (
                    f"[INFO] synthesize_attempt heading={heading!r} "
                    f"iteration={int(payload.get('iteration', 0) or 0)}/"
                    f"{int(payload.get('max_iterations', 0) or 0)}"
                )
            elif status == "section_fragment_accepted":
                message = (
                    f"[INFO] synthesize_fragment_accepted heading={heading!r} "
                    f"policy={str(payload.get('accepted_policy', '')).strip() or 'unknown'}"
                )
            elif status == "section_applied":
                message = f"[INFO] synthesize_applied heading={heading!r}"
            elif status == "section_attempt_error":
                message = f"[WARN] synthesize_attempt_error heading={heading!r}: {str(payload.get('error', '')).strip()}"
            elif status == "complete":
                message = (
                    f"[INFO] synthesize_complete source={str(payload.get('source', '')).strip() or 'unknown'} "
                    f"accepted_sections={int(payload.get('accepted_sections_count', 0) or 0)} "
                    f"applied_sections={int(payload.get('applied_sections_count', 0) or 0)} "
                    f"gate_pass={bool(payload.get('gate_pass', False))}"
                )
            if message:
                print(message)
            safe_save_state(run_path, state)

        final_text = ""
        final_validation: dict[str, Any] = {}
        final_gate: dict[str, Any] = {"pass": False, "coverage": 0.0}
        source = "none"
        llm_enhancements: dict[str, Any] = {
            "requested": effective_mode == "agent",
            "base_gate_pass": False,
            "accepted_sections_count": 0,
            "accepted_section_headings": [],
            "rejected_section_headings": [],
            "sections": [],
            "applied_sections": [],
        }
        resumed_synthesis = load_synthesis_resume_context(run_path) if resuming else None
        if resumed_synthesis:
            final_text = str(resumed_synthesis.get("final_text", ""))
            final_validation = resumed_synthesis.get("final_validation", {})
            final_gate = resumed_synthesis.get("final_gate", {})
            source = str(resumed_synthesis.get("source", "checkpoint")).strip() or "checkpoint"
            if isinstance(resumed_synthesis.get("llm_enhancements", {}), dict):
                llm_enhancements = resumed_synthesis.get("llm_enhancements", {})
                state["llm_enhancements"] = llm_enhancements
            add_event(
                state,
                "resume",
                "Reused synthesis checkpoint and skipped report regeneration.",
                data={"source": source},
            )
        else:
            hybrid_result = synthesize_hybrid_report(
                repo_path=repo_path,
                effective_mode=effective_mode,
                llm_output_policy=llm_output_policy,
                fact_index=fact_index,
                redaction_stats=redaction_stats,
                included_files=included_files,
                line_counts=line_counts,
                allowed_evidence_text=allowed_evidence_text,
                fact_context_json=prompt_fact_index_json,
                goal_focus_text=goal_focus_text,
                goal=args.goal,
                audience=audience_name,
                audience_plan=audience_plan,
                subsystem_priority_plan=subsystem_priority_plan,
                max_iterations=args.max_iterations,
                claim_support_index=claim_support_index,
                progress_callback=on_synthesis_progress if effective_mode == "agent" else None,
            )
            final_text = str(hybrid_result.get("report", ""))
            final_validation = hybrid_result.get("validation", {})
            final_gate = hybrid_result.get("gate", {})
            source = str(hybrid_result.get("source", "none")).strip() or "none"
            llm_enhancements = hybrid_result.get("llm_enhancements", {}) if isinstance(hybrid_result.get("llm_enhancements", {}), dict) else llm_enhancements
            state["llm_enhancements"] = llm_enhancements
            add_event(
                state,
                "synthesize",
                "Built deterministic-first report and applied validated LLM enhancement sections.",
                data={
                    "source": source,
                    "llm_sections_applied": int(llm_enhancements.get("accepted_sections_count", 0) or 0),
                    "llm_sections_rejected": len(llm_enhancements.get("rejected_section_headings", [])),
                },
            )
            if effective_mode == "deterministic":
                add_event(state, "synthesize", "Built deterministic report in deterministic mode.")

            checkpoint_path = save_synthesis_checkpoint(
                run_path,
                {
                    "llm_output_policy": llm_output_policy,
                    "fallback_used": source.startswith("deterministic"),
                    "accepted_iteration": "",
                    "source": source,
                    "final_text": final_text,
                    "final_validation": final_validation,
                    "final_gate": final_gate,
                    "llm_enhancements": llm_enhancements,
                    "iterations": [],
                    "iteration_errors": [],
                },
            )
            state["artifacts"]["run_synthesis_checkpoint"] = checkpoint_path
            save_state(run_path, state)

        current_stage = "finalize"
        state["current_stage"] = current_stage
        state["artifacts"]["run_synthesis_checkpoint"] = os.path.join(run_path, SYNTHESIS_CHECKPOINT_FILENAME)
        save_state(run_path, state)

        traceability = {
            "scanned_files_count": int(final_validation.get("scanned_files_count", len(included_files))),
            "valid_evidence_paths_count": int(final_validation.get("valid_evidence_paths", 0)),
            "evidence_file_coverage": float(final_validation.get("file_evidence_coverage", 0.0)),
            "files_missing_evidence_count": int(final_validation.get("files_missing_evidence_count", 0)),
            "files_missing_evidence_sample": final_validation.get("files_missing_evidence_sample", []),
            "strict_traceability_enabled": bool(final_gate.get("strict_traceability_enabled", False)),
            "strict_traceability_pass": bool(final_gate.get("strict_traceability_pass", True)),
        }
        run_traceability_path = os.path.join(run_path, "traceability.json")
        run_traceability_md_path = os.path.join(run_path, "traceability.md")
        write_json(run_traceability_path, traceability)
        write_text(run_traceability_md_path, render_traceability_markdown(traceability))
        state["artifacts"]["run_traceability"] = run_traceability_path
        state["artifacts"]["run_traceability_markdown"] = run_traceability_md_path

        inference_records = analyzer.build_reasoned_inference_records(fact_index)
        inference_audit = {
            "record_count": len(inference_records),
            "records": inference_records,
        }
        run_inference_audit_path = os.path.join(run_path, "inference_audit.json")
        write_json(run_inference_audit_path, inference_audit)
        state["artifacts"]["run_inference_audit"] = run_inference_audit_path

        if effective_mode == "agent":
            run_llm_enhancements_path = os.path.join(run_path, "llm_enhancements.json")
            write_json(run_llm_enhancements_path, llm_enhancements)
            state["artifacts"]["run_llm_enhancements"] = run_llm_enhancements_path

        final_validation["classification_summary"] = fact_index.get("classification_summary", {})
        final_text = analyzer.append_quality_metrics(final_text, final_validation, redaction_stats, final_gate)
        best_effort_report = source.startswith("llm_best_effort")
        accepted_report = bool(final_gate.get("pass", False)) or best_effort_report
        run_report_path = os.path.join(run_path, "report.md" if accepted_report else "report_rejected.md")
        write_text(run_report_path, final_text)
        state["artifacts"]["run_report"] = run_report_path
        state["report_source"] = source
        state["llm_output_policy"] = llm_output_policy
        state["best_effort_accepted"] = best_effort_report
        state["gate"] = final_gate
        state["validation"] = final_validation

        state["artifacts"].update(analyzer.write_run_architecture_exports(run_path, final_text, fact_index, bool(args.write_root_outputs)))

        if args.write_root_outputs:
            if accepted_report:
                write_text(analyzer.OUTPUT_FILE, final_text)
                state["artifacts"]["root_report"] = analyzer.OUTPUT_FILE
            else:
                write_text(analyzer.REJECTED_REPORT_FILE, final_text)
                state["artifacts"]["root_report_rejected"] = analyzer.REJECTED_REPORT_FILE

        subsystem_stats = write_subsystem_artifacts(fact_index, os.path.join(run_path, "subsystems"))
        state["artifacts"]["run_subsystem_dir"] = os.path.join(run_path, "subsystems")
        state["artifacts"]["run_subsystem_index"] = subsystem_stats.get("subsystem_index", "")
        add_event(
            state,
            "subsystems",
            "Generated subsystem-level documentation artifacts.",
            data={"subsystem_count": subsystem_stats.get("subsystem_count", 0)},
        )

        run_diff_md_path = ""
        run_diff_json_path = ""
        run_architecture_diff_md_path = ""
        run_architecture_diff_json_path = ""
        previous = find_previous_run_for_repo(runs_dir, run_path, repo_path, current_state=state)
        if previous:
            try:
                diff_obj = compare_run_dirs(previous["run_dir"], run_path)
                run_diff_md_path = os.path.join(run_path, "run_diff.md")
                run_diff_json_path = os.path.join(run_path, "run_diff.json")
                run_architecture_diff_md_path = os.path.join(run_path, "architecture_diff.md")
                run_architecture_diff_json_path = os.path.join(run_path, "architecture_diff.json")
                write_text(run_diff_md_path, render_run_diff_markdown(diff_obj))
                write_json(run_diff_json_path, diff_obj)
                write_text(
                    run_architecture_diff_md_path,
                    render_architecture_diff_markdown(
                        diff_obj.get("architecture", {}),
                        base_run_id=diff_obj.get("base_run_id", ""),
                        head_run_id=diff_obj.get("head_run_id", ""),
                    ),
                )
                write_json(
                    run_architecture_diff_json_path,
                    diff_obj.get("architecture", {}) if isinstance(diff_obj.get("architecture", {}), dict) else {},
                )
                state["artifacts"]["run_diff_markdown"] = run_diff_md_path
                state["artifacts"]["run_diff_json"] = run_diff_json_path
                state["artifacts"]["run_architecture_diff_markdown"] = run_architecture_diff_md_path
                state["artifacts"]["run_architecture_diff_json"] = run_architecture_diff_json_path
                state["previous_run_id"] = previous.get("run_id", "")
                add_event(
                    state,
                    "compare",
                    "Computed run to run delta against previous repository run.",
                    data={"previous_run_id": previous.get("run_id", "")},
                )
            except Exception as e:
                add_event(
                    state,
                    "compare",
                    "Run comparison skipped due to comparison error.",
                    data={"error": str(e)},
                )
        else:
            add_event(state, "compare", "No previous comparable run found for this repository.")

        synth_sec = time.perf_counter() - synth_t0
        total_sec = time.perf_counter() - overall_t0
        state["timing"] = {
            "gather_sec": round(gather_sec, 3),
            "synthesize_sec": round(synth_sec, 3),
            "total_sec": round(total_sec, 3),
        }
        state["timings"] = dict(state["timing"])
        completed_at = utc_now_iso()
        state["completed_at"] = completed_at
        state["finished_at"] = completed_at
        state["status"] = "completed" if accepted_report else "failed_gate"
        state["current_stage"] = "completed" if accepted_report else "failed_gate"
        clear_failure_artifact(run_path)
        save_state(run_path, state)

        run_trends_json_path = os.path.join(run_path, "run_trends.json")
        run_trends_md_path = os.path.join(run_path, "run_trends.md")
        try:
            run_trends = build_repo_run_trends(runs_dir, repo_path)
            write_json(run_trends_json_path, run_trends)
            write_text(run_trends_md_path, render_repo_run_trends_markdown(run_trends))
            state["artifacts"]["run_trends"] = run_trends_json_path
            state["artifacts"]["run_trends_markdown"] = run_trends_md_path
            add_event(
                state,
                "trends",
                "Generated repo-level run trends across commits and branches.",
                data={"run_count": int(run_trends.get("total_runs", 0) or 0), "branch_count": int(run_trends.get("branch_count", 0) or 0)},
            )
        except Exception as e:
            add_event(state, "trends", "Repo trend generation skipped due to error.", data={"error": str(e)})
        accepted_llm_sections = llm_enhancements.get("accepted_section_headings", []) if isinstance(llm_enhancements, dict) else []
        rejected_llm_sections = llm_enhancements.get("rejected_section_headings", []) if isinstance(llm_enhancements, dict) else []
        classification_summary = fact_index.get("classification_summary", {}) if isinstance(fact_index.get("classification_summary", {}), dict) else {}

        run_summary_lines = [
            "# Agent Run Summary",
            "",
            f"- Run ID: `{run_id}`",
            f"- Repo Path: `{analyzer.display_safe_path(repo_path)}`",
            f"- Attempt Count: `{state.get('attempt_count', 1)}`",
            f"- Resume Count: `{state.get('resume_count', 0)}`",
            f"- Requested Mode: `{requested_mode}`",
            f"- Effective Mode: `{effective_mode}`",
            f"- Backend: `{analyzer.LLM_BACKEND}`",
            f"- Model: `{state['model']}`",
            f"- Goal: `{args.goal.strip() or 'full_repo_documentation'}`",
            f"- Audience: `{state.get('audience', 'reviewer')}`",
            f"- LLM Output Policy: `{llm_output_policy}`",
            f"- Report Source: `{source}`",
            f"- Best Effort Accepted: `{best_effort_report}`",
            f"- LLM Enhancement Sections Accepted: `{len(accepted_llm_sections)}`",
            f"- LLM Enhancement Sections Rejected: `{len(rejected_llm_sections)}`",
            f"- Gate Pass: `{final_gate.get('pass', False)}`",
            f"- Evidence Coverage: `{final_gate.get('coverage', 0.0):.2%}`",
            f"- Semantic Claim Coverage: `{final_gate.get('semantic_coverage', 1.0):.2%}`",
            f"- Semantic Validation Pass: `{final_gate.get('semantic_pass', True)}`",
            f"- Evidence File Coverage: `{final_validation.get('file_evidence_coverage', 0.0):.2%}`",
            f"- Files Missing Evidence: `{final_validation.get('files_missing_evidence_count', 0)}`",
            f"- Semantically Unsupported Claims: `{final_validation.get('claims_semantically_unsupported', 0)}`",
            f"- Report Artifact: `{os.path.basename(run_report_path)}`",
            f"- Repo Fingerprint: `{repo_fingerprint[:16]}...`",
            "",
            "## Key Metrics",
            f"- Files: `{len(fact_index.get('files', []))}`",
            f"- Endpoints: `{len(fact_index.get('api_endpoints', []))}`",
            f"- Runtime Services: `{analyzer._runtime_service_verification_counts(fact_index).get('total', 0)}`",
            f"- Services With Verified Endpoints: `{analyzer._runtime_service_verification_counts(fact_index).get('with_verified_endpoints', 0)}`",
            f"- Runtime-Verified Endpoints: `{analyzer._runtime_endpoint_verification_counts(fact_index).get('verified', 0)}`",
            f"- Static-Only Endpoints: `{analyzer._runtime_endpoint_verification_counts(fact_index).get('static_only', 0)}`",
            f"- Dependencies: `{len(fact_index.get('dependencies', []))}`",
            f"- Scripts: `{len(fact_index.get('scripts', []))}`",
            f"- SQL Entities: `{len(fact_index.get('sql_entities', []))}`",
            f"- SQL Queries: `{len(fact_index.get('sql_queries', []))}`",
            f"- Cross-language Symbols: `{len(fact_index.get('language_symbols', []))}`",
            f"- Cross-language Calls: `{len(fact_index.get('language_calls', []))}`",
            f"- Cross-file Symbol Edges: `{len(fact_index.get('cross_file_symbol_edges', []))}`",
            f"- Cross-file Event Edges: `{len(fact_index.get('cross_file_event_edges', []))}`",
            f"- Runtime Observations: `{len(fact_index.get('runtime_observations', []))}`",
            f"- Highest Data Classification: `{classification_summary.get('highest_classification', 'unclassified')}`",
            f"- Classified Files: `{classification_summary.get('classified_files', 0)}`",
            f"- Files Matched By Classification Rules: `{classification_summary.get('matched_files', 0)}`",
            f"- Redactions Applied: `{redaction_stats.get('total_redactions', 0)}`",
            f"- Custom Redaction Rules: `{redaction_stats.get('custom_redaction_rules_count', 0)}`",
            f"- Files Scanned: `{redaction_stats.get('files_read', 0)}`",
            f"- Characters Scanned: `{redaction_stats.get('chars_scanned', 0)}`",
            f"- Skipped Large Files: `{redaction_stats.get('skipped_by_size_count', 0)}`",
            f"- Fact Index Cache Hits: `{fact_index_cache_stats.get('cache_hits', 0)}`",
            f"- Fact Index Cache Misses: `{fact_index_cache_stats.get('cache_misses', 0)}`",
            f"- Subsystems Documented: `{subsystem_stats.get('subsystem_count', 0)}`",
            f"- Inference Records: `{len(inference_records)}`",
            f"- Strict Traceability Enabled: `{final_gate.get('strict_traceability_enabled', False)}`",
            f"- Strict Traceability Pass: `{final_gate.get('strict_traceability_pass', True)}`",
            f"- Gather Time Sec: `{gather_sec:.3f}`",
            f"- Synthesize Time Sec: `{synth_sec:.3f}`",
            f"- Total Time Sec: `{total_sec:.3f}`",
        ]
        repo_context = str(redaction_stats.get("repo_path", "")).strip() or repo_path
        scan_cfg_path = analyzer.display_safe_path(str(redaction_stats.get("scan_config_path", "")).strip(), repo_path=repo_context)
        if scan_cfg_path:
            run_summary_lines.append(f"- Scan Config: `{scan_cfg_path}`")
        redaction_policy_path = analyzer.display_safe_path(str(redaction_stats.get("redaction_policy_path", "")).strip(), repo_path=repo_context)
        if redaction_policy_path:
            run_summary_lines.append(f"- Redaction Policy: `{redaction_policy_path}`")
        security_policy_name = str(redaction_stats.get("security_policy_name", "")).strip()
        if security_policy_name:
            run_summary_lines.append(f"- Security Policy: `{security_policy_name}`")
        security_policy_path = analyzer.display_safe_path(str(redaction_stats.get("security_policy_path", "")).strip(), repo_path=repo_context)
        if security_policy_path:
            run_summary_lines.append(f"- Security Policy File: `{security_policy_path}`")
        policy_packs = [str(item).strip() for item in redaction_stats.get("policy_packs", []) if str(item).strip()]
        if policy_packs:
            run_summary_lines.append(f"- Policy Packs: `{', '.join(policy_packs)}`")
        classification_counts = classification_summary.get("classification_counts", {})
        if isinstance(classification_counts, dict) and classification_counts:
            run_summary_lines.append(f"- Classification Counts: `{json.dumps(classification_counts, ensure_ascii=True, sort_keys=True)}`")
        miss_files = fact_index_cache_stats.get("cache_miss_files_sample", [])
        if miss_files:
            run_summary_lines.append(f"- Cache Miss File Samples: `{', '.join(miss_files[:5])}`")
        if accepted_llm_sections:
            run_summary_lines.append(f"- Accepted LLM Section Headings: `{'; '.join(accepted_llm_sections)}`")
        if rejected_llm_sections:
            run_summary_lines.append(f"- Rejected LLM Section Headings: `{'; '.join(rejected_llm_sections)}`")
        git_info = repo_meta.get("git", {}) if isinstance(repo_meta, dict) else {}
        if git_info.get("is_git_repo"):
            run_summary_lines.append(f"- Git Branch: `{git_info.get('branch', '')}`")
            run_summary_lines.append(f"- Git Commit: `{git_info.get('commit', '')}`")
            run_summary_lines.append(f"- Git Dirty: `{git_info.get('dirty')}`")
        if state.get("previous_run_id"):
            run_summary_lines.append(f"- Previous Run Compared: `{state['previous_run_id']}`")
        if run_diff_md_path:
            run_summary_lines.append(f"- Run Diff Artifact: `{os.path.basename(run_diff_md_path)}`")
        prompt_context_artifact = state.get("artifacts", {}).get("run_prompt_fact_context", "")
        if prompt_context_artifact:
            run_summary_lines.append(f"- Prompt Context Artifact: `{os.path.basename(prompt_context_artifact)}`")
        claim_support_artifact = state.get("artifacts", {}).get("run_claim_support_index", "")
        if claim_support_artifact:
            run_summary_lines.append(f"- Claim Support Artifact: `{os.path.basename(claim_support_artifact)}`")
        llm_status_artifact = state.get("artifacts", {}).get("run_llm_backend_status", "")
        if llm_status_artifact:
            run_summary_lines.append(f"- LLM Backend Status Artifact: `{os.path.basename(llm_status_artifact)}`")
        security_policy_artifact = state.get("artifacts", {}).get("run_security_policy_audit", "")
        if security_policy_artifact:
            run_summary_lines.append(f"- Security Policy Audit Artifact: `{os.path.basename(security_policy_artifact)}`")
        heartbeat_artifact = state.get("artifacts", {}).get("run_heartbeat", "")
        if heartbeat_artifact:
            run_summary_lines.append(f"- Heartbeat Artifact: `{os.path.basename(heartbeat_artifact)}`")
        run_summary_lines.append("- Lock Lifecycle: `run.lock.json` is held during execution and removed on exit.")
        gather_checkpoint_artifact = state.get("artifacts", {}).get("run_gather_checkpoint", "")
        if gather_checkpoint_artifact:
            run_summary_lines.append(f"- Gather Checkpoint Artifact: `{os.path.basename(gather_checkpoint_artifact)}`")
        synthesis_checkpoint_artifact = state.get("artifacts", {}).get("run_synthesis_checkpoint", "")
        if synthesis_checkpoint_artifact:
            run_summary_lines.append(f"- Synthesis Checkpoint Artifact: `{os.path.basename(synthesis_checkpoint_artifact)}`")
        runtime_artifact = state.get("artifacts", {}).get("run_runtime_observations", "")
        if runtime_artifact:
            run_summary_lines.append(f"- Runtime Observations Artifact: `{os.path.basename(runtime_artifact)}`")
        llm_enhancement_artifact = state.get("artifacts", {}).get("run_llm_enhancements", "")
        if llm_enhancement_artifact:
            run_summary_lines.append(f"- LLM Enhancements Artifact: `{os.path.basename(llm_enhancement_artifact)}`")
        audience_plan_artifact = state.get("artifacts", {}).get("run_audience_plan", "")
        if audience_plan_artifact:
            run_summary_lines.append(f"- Audience Plan Artifact: `{os.path.basename(audience_plan_artifact)}`")
        subsystem_priority_artifact = state.get("artifacts", {}).get("run_subsystem_priorities", "")
        if subsystem_priority_artifact:
            run_summary_lines.append(f"- Subsystem Priorities Artifact: `{os.path.basename(subsystem_priority_artifact)}`")
        run_trends_artifact = state.get("artifacts", {}).get("run_trends", "")
        if run_trends_artifact:
            run_summary_lines.append(f"- Repo Run Trends Artifact: `{os.path.basename(run_trends_artifact)}`")
        run_summary_lines.append(f"- Traceability Artifact: `{os.path.basename(run_traceability_path)}`")
        run_summary_lines.append(f"- Traceability Markdown: `{os.path.basename(run_traceability_md_path)}`")
        run_summary_lines.append(f"- Inference Audit Artifact: `{os.path.basename(run_inference_audit_path)}`")
        run_summary_path = os.path.join(run_path, "run_summary.md")
        write_text(run_summary_path, "\n".join(run_summary_lines) + "\n")
        state["artifacts"]["run_summary"] = run_summary_path
        if report_home_dir:
            state["artifacts"].update(
                analyzer.write_repo_report_shortcuts(report_home_dir, run_path, run_summary_path, run_report_path)
            )

        save_state(run_path, state)
        if lock_acquired:
            release_run_lock(run_path)

        print_saved_if_exists(run_report_path)
        print_saved_if_exists(run_model_safe_fact_path)
        print_saved_if_exists(run_traceability_path)
        print_saved_if_exists(run_traceability_md_path)
        print_saved_if_exists(run_inference_audit_path)
        print_saved_if_exists(run_llm_backend_status_path)
        print_saved_if_exists(run_security_policy_audit_path)
        print_saved_if_exists(state["artifacts"].get("run_audience_plan", ""))
        print_saved_if_exists(state["artifacts"].get("run_audience_plan_markdown", ""))
        print_saved_if_exists(state["artifacts"].get("run_subsystem_priorities", ""))
        print_saved_if_exists(state["artifacts"].get("run_subsystem_priorities_markdown", ""))
        print_saved_if_exists(state["artifacts"].get("run_trends", ""))
        print_saved_if_exists(state["artifacts"].get("run_trends_markdown", ""))
        if state["artifacts"].get("run_llm_enhancements"):
            print_saved_if_exists(state["artifacts"]["run_llm_enhancements"])
        if state["artifacts"].get("run_gather_checkpoint"):
            print_saved_if_exists(state["artifacts"]["run_gather_checkpoint"])
        if state["artifacts"].get("run_synthesis_checkpoint"):
            print_saved_if_exists(state["artifacts"]["run_synthesis_checkpoint"])
        if state["artifacts"].get("run_runtime_observations"):
            print_saved_if_exists(state["artifacts"]["run_runtime_observations"])
        for artifact_key in ["run_architecture_model", "run_mermaid", "run_dot", "run_likec4", "run_svg", "run_png"]:
            artifact_path = str(state["artifacts"].get(artifact_key, "")).strip()
            if artifact_path:
                print_saved_if_exists(artifact_path)
        print_saved_if_exists(state["artifacts"].get("run_subsystem_index", ""))
        if run_diff_md_path:
            print_saved_if_exists(run_diff_md_path)
            print_saved_if_exists(run_diff_json_path)
        if run_architecture_diff_md_path:
            print_saved_if_exists(run_architecture_diff_md_path)
            print_saved_if_exists(run_architecture_diff_json_path)
        print_saved_if_exists(run_summary_path)
        print_saved_if_exists(os.path.join(run_path, "state.json"))
        if args.write_root_outputs and accepted_report:
            print_saved_if_exists(analyzer.OUTPUT_FILE)
        if args.write_root_outputs and not accepted_report:
            print_saved_if_exists(analyzer.REJECTED_REPORT_FILE)
        if args.write_root_outputs:
            print_saved_if_exists(analyzer.MODEL_SAFE_FACT_INDEX_FILE)
        print(f"[INFO] grounding_gate_pass={final_gate.get('pass', False)}")
        return 0 if accepted_report else 2

    except Exception as e:
        completed_at = utc_now_iso()
        state["completed_at"] = completed_at
        state["finished_at"] = completed_at
        state["status"] = "error"
        state["current_stage"] = current_stage
        state["error"] = str(e)
        add_event(state, "error", "Unhandled error during agent execution.", data={"error": str(e)})
        tb_text = traceback.format_exc()
        failure_path = write_failure_artifact(
            run_path,
            run_id=run_id,
            repo_path=repo_path,
            stage=current_stage,
            status="error",
            error=str(e),
            tb_text=tb_text,
            resumable=current_stage in {"gather", "synthesize", "finalize"},
            attempt_count=int(state.get("attempt_count", 1) or 1),
        )
        state["failure"] = {
            "stage": current_stage,
            "error": str(e),
            "resumable": current_stage in {"gather", "synthesize", "finalize"},
        }
        state["artifacts"]["run_failure"] = failure_path
        save_error = safe_save_state(run_path, state)
        if lock_acquired:
            release_run_lock(run_path)
        if save_error:
            print(f"[WARN] Failed to persist error state: {save_error}")
        print(f"❌ Error: {e}")
        print(f"[SAVED] {failure_path}")
        print(f"[SAVED] {os.path.join(run_path, STATE_FILENAME)}")
        return 1


STOPWORDS = {
    "the",
    "and",
    "for",
    "with",
    "from",
    "what",
    "where",
    "when",
    "which",
    "this",
    "that",
    "does",
    "about",
    "have",
    "has",
    "how",
    "many",
    "show",
    "list",
    "into",
    "your",
    "repo",
    "repository",
    "code",
    "project",
}

AUDIENCE_ALIASES = {
    "default": "reviewer",
    "review": "reviewer",
    "eng": "developer",
    "engineer": "developer",
    "dev": "developer",
    "ops": "operator",
    "operations": "operator",
    "sec": "security",
    "exec": "executive",
    "leadership": "executive",
}

AUDIENCE_PROFILES = {
    "reviewer": {
        "description": "Balanced repo review for architectural and maintenance understanding.",
        "boost_tokens": ["api", "service", "module", "runtime", "sql", "infra", "auth"],
    },
    "developer": {
        "description": "Implementation-first view for engineers making or reviewing code changes.",
        "boost_tokens": ["api", "service", "module", "client", "schema", "sql", "symbol"],
    },
    "operator": {
        "description": "Runtime and deployment-first view for operators and release owners.",
        "boost_tokens": ["runtime", "deploy", "infra", "docker", "queue", "job", "worker", "script"],
    },
    "security": {
        "description": "Surface-oriented view for security and governance review.",
        "boost_tokens": ["auth", "security", "secret", "token", "login", "sql", "runtime", "infra"],
    },
    "executive": {
        "description": "High-level view emphasizing critical subsystems and operational risk.",
        "boost_tokens": ["api", "runtime", "infra", "payment", "billing", "auth", "queue"],
    },
}


def normalize_doc_audience(value: str) -> str:
    raw = str(value or "").strip().lower().replace("-", "_").replace(" ", "_")
    if not raw:
        return "reviewer"
    normalized = AUDIENCE_ALIASES.get(raw, raw)
    if normalized in AUDIENCE_PROFILES:
        return normalized
    return "reviewer"


def available_doc_audiences() -> list[str]:
    return sorted(AUDIENCE_PROFILES.keys())


def _first_available_evidence(items: list[dict[str, Any]], fallback: str = "none") -> str:
    for item in items:
        if not isinstance(item, dict):
            continue
        for key in ["verification_evidence", "source_evidence", "evidence"]:
            value = str(item.get(key, "")).strip()
            if value:
                return value
        path = str(item.get("path", item.get("file", item.get("source_file", "")))).replace("\\", "/").strip()
        if path:
            try:
                line_no = int(item.get("line", item.get("source_line", 1)) or 1)
            except Exception:
                line_no = 1
            return f"{path}#L{max(1, line_no)}"
    return fallback or "none"


def _subsystem_priority_records(
    fact_index: dict[str, Any],
    *,
    goal: str = "",
    audience: str = "reviewer",
) -> list[dict[str, Any]]:
    subsystems = build_subsystem_summary_map(fact_index)
    goal_tokens = tokenize_goal(goal)
    audience_name = normalize_doc_audience(audience)
    audience_meta = AUDIENCE_PROFILES.get(audience_name, AUDIENCE_PROFILES["reviewer"])
    audience_tokens = [str(item).strip().lower() for item in audience_meta.get("boost_tokens", []) if str(item).strip()]
    records: list[dict[str, Any]] = []
    for name, data in subsystems.items():
        files = data.get("files", [])
        endpoints = data.get("endpoints", [])
        dependencies = data.get("dependencies", [])
        entrypoints = data.get("entrypoints", [])
        infra = data.get("infrastructure", [])
        ai_signals = data.get("ai_signals", [])
        sql_entities = data.get("sql_entities", [])
        sql_queries = data.get("sql_queries", [])
        language_symbols = data.get("language_symbols", [])
        runtime_observations = data.get("runtime_observations", [])
        search_haystack = " ".join(
            [
                name,
                " ".join([str(item.get("path", "")) for item in files if isinstance(item, dict)]),
                " ".join([str(item.get("route", "")) for item in endpoints if isinstance(item, dict)]),
                " ".join([str(item.get("name", "")) for item in dependencies if isinstance(item, dict)]),
                " ".join([str(item.get("name", "")) for item in sql_entities if isinstance(item, dict)]),
                " ".join([str(item.get("target", "")) for item in sql_queries if isinstance(item, dict)]),
            ]
        ).lower()
        goal_matches = [token for token in goal_tokens if token in search_haystack]
        audience_matches = [token for token in audience_tokens if token in search_haystack]

        score = int(len(files))
        score += int(len(endpoints)) * 5
        score += int(len(entrypoints)) * 3
        score += int(len(runtime_observations)) * 4
        score += int(len(sql_entities)) * 4
        score += int(len(sql_queries)) * 2
        score += int(len(infra)) * 3
        score += int(len(ai_signals)) * 2
        score += int(len(language_symbols))
        score += min(4, int(len(dependencies)))
        score += len(goal_matches) * 6
        score += len(audience_matches) * 4

        if score >= 22:
            change_risk = "high"
        elif score >= 11:
            change_risk = "medium"
        else:
            change_risk = "baseline"

        reasons: list[str] = []
        if endpoints:
            reasons.append(f"{len(endpoints)} endpoint(s)")
        if sql_entities or sql_queries:
            reasons.append(f"{len(sql_entities) + len(sql_queries)} data-layer signal(s)")
        if runtime_observations:
            reasons.append(f"{len(runtime_observations)} runtime observation(s)")
        if infra:
            reasons.append(f"{len(infra)} infrastructure signal(s)")
        if entrypoints:
            reasons.append(f"{len(entrypoints)} entrypoint signal(s)")
        if goal_matches:
            reasons.append(f"goal match: {', '.join(goal_matches[:3])}")
        if audience_matches:
            reasons.append(f"{audience_name} emphasis: {', '.join(audience_matches[:3])}")
        if not reasons:
            reasons.append(f"{len(files)} file(s)")

        evidence = _first_available_evidence(
            endpoints
            + entrypoints
            + runtime_observations
            + sql_entities
            + sql_queries
            + infra
            + files,
            fallback=first_evidence_from_files(fact_index),
        )
        records.append(
            {
                "subsystem": name,
                "change_risk": change_risk,
                "priority_score": score,
                "goal_matches": goal_matches,
                "audience_matches": audience_matches,
                "reasons": reasons,
                "file_count": len(files),
                "endpoint_count": len(endpoints),
                "runtime_observation_count": len(runtime_observations),
                "sql_signal_count": len(sql_entities) + len(sql_queries),
                "evidence": evidence,
            }
        )
    return sorted(
        records,
        key=lambda item: (
            -int(item.get("priority_score", 0) or 0),
            -int(item.get("endpoint_count", 0) or 0),
            -int(item.get("file_count", 0) or 0),
            str(item.get("subsystem", "")),
        ),
    )


def build_subsystem_priority_plan(
    fact_index: dict[str, Any],
    *,
    goal: str = "",
    audience: str = "reviewer",
    max_items: int = 5,
) -> dict[str, Any]:
    records = _subsystem_priority_records(fact_index, goal=goal, audience=audience)
    return {
        "audience": normalize_doc_audience(audience),
        "goal": str(goal or "").strip(),
        "priorities": records[: max(1, int(max_items or 5))],
        "subsystem_count": len(records),
    }


def render_subsystem_priority_markdown(priority_plan: dict[str, Any]) -> str:
    payload = priority_plan if isinstance(priority_plan, dict) else {}
    priorities = payload.get("priorities", []) if isinstance(payload.get("priorities", []), list) else []
    lines = [
        "## Priority Modules (Deterministic)",
        "",
    ]
    if not priorities:
        lines.append("1. No subsystem priorities could be inferred from the scanned repository. [Evidence: none]")
        lines.append("")
        return "\n".join(lines)
    for idx, item in enumerate(priorities, start=1):
        subsystem = str(item.get("subsystem", "root")).strip() or "root"
        change_risk = str(item.get("change_risk", "baseline")).strip() or "baseline"
        score = int(item.get("priority_score", 0) or 0)
        reasons = ", ".join([str(reason) for reason in item.get("reasons", []) if str(reason).strip()][:4]) or "structural presence"
        evidence = str(item.get("evidence", "none")).strip() or "none"
        lines.append(
            f"{idx}. Subsystem `{subsystem}` is a `{change_risk}`-risk review target with score `{score}` because it carries {reasons}. [Evidence: {evidence}]"
        )
    lines.append("")
    return "\n".join(lines)


def build_audience_plan(
    fact_index: dict[str, Any],
    *,
    audience: str = "reviewer",
    goal: str = "",
) -> dict[str, Any]:
    audience_name = normalize_doc_audience(audience)
    priorities = _subsystem_priority_records(fact_index, goal=goal, audience=audience_name)
    priority_names = [str(item.get("subsystem", "")).strip() for item in priorities[:3] if str(item.get("subsystem", "")).strip()]
    priority_label = ", ".join(priority_names[:2]) if priority_names else "the dominant subsystem inventory"
    first_file_evidence = first_evidence_from_files(fact_index)
    endpoints = fact_index.get("api_endpoints", []) if isinstance(fact_index.get("api_endpoints", []), list) else []
    entrypoints = fact_index.get("entrypoints", []) if isinstance(fact_index.get("entrypoints", []), list) else []
    scripts = fact_index.get("scripts", []) if isinstance(fact_index.get("scripts", []), list) else []
    infra = fact_index.get("infrastructure", []) if isinstance(fact_index.get("infrastructure", []), list) else []
    sql_entities = fact_index.get("sql_entities", []) if isinstance(fact_index.get("sql_entities", []), list) else []
    sql_queries = fact_index.get("sql_queries", []) if isinstance(fact_index.get("sql_queries", []), list) else []
    runtime_observations = fact_index.get("runtime_observations", []) if isinstance(fact_index.get("runtime_observations", []), list) else []
    language_symbols = fact_index.get("language_symbols", []) if isinstance(fact_index.get("language_symbols", []), list) else []

    entry_evidence = _first_available_evidence(entrypoints + scripts, fallback=first_file_evidence)
    interface_evidence = _first_available_evidence(endpoints + runtime_observations, fallback=entry_evidence)
    data_evidence = _first_available_evidence(sql_entities + sql_queries + language_symbols, fallback=interface_evidence)
    infra_evidence = _first_available_evidence(infra + runtime_observations, fallback=first_file_evidence)
    priority_evidence = str(priorities[0].get("evidence", first_file_evidence)).strip() if priorities else first_file_evidence

    if audience_name == "developer":
        items = [
            {
                "text": "Start with entrypoints and runnable scripts to identify where code paths begin before drilling into implementation details.",
                "evidence": entry_evidence,
            },
            {
                "text": f"Prioritize the highest-signal subsystems such as {priority_label} because they concentrate most of the implementation surface that future code changes will touch.",
                "evidence": priority_evidence,
            },
            {
                "text": "Trace API, SQL, and cross-language integration next so changes to one layer can be mapped to downstream contracts and data access paths.",
                "evidence": data_evidence,
            },
        ]
    elif audience_name == "operator":
        items = [
            {
                "text": "Begin with scripts, entrypoints, and runtime observations to understand how the repository is started, exercised, or probed locally.",
                "evidence": entry_evidence,
            },
            {
                "text": "Review infrastructure and packaging surfaces before reading deep application code because deployment shape and runtime boundaries matter first for operators.",
                "evidence": infra_evidence,
            },
            {
                "text": f"Use the priority subsystem shortlist such as {priority_label} to focus operational review on the areas with the densest interface and runtime signals.",
                "evidence": priority_evidence,
            },
        ]
    elif audience_name == "security":
        items = [
            {
                "text": "Start with externally reachable routes and runtime-touched services because those surfaces expose the clearest boundary between repository code and external interaction.",
                "evidence": interface_evidence,
            },
            {
                "text": "Review infrastructure and packaging artifacts alongside the priority subsystem shortlist to spot trust boundaries and deployment-relevant control points early.",
                "evidence": infra_evidence,
            },
            {
                "text": "Inspect SQL and cross-language integration paths after that because data access and interface translation often carry the highest review leverage in legacy systems.",
                "evidence": data_evidence,
            },
        ]
    elif audience_name == "executive":
        items = [
            {
                "text": f"Use the highest-priority subsystems such as {priority_label} as the main briefing slice because they concentrate most of the repository complexity and change pressure.",
                "evidence": priority_evidence,
            },
            {
                "text": "Review the outward-facing API and runtime surfaces next to understand where business-critical behavior is exposed or exercised.",
                "evidence": interface_evidence,
            },
            {
                "text": "Keep infrastructure and packaging artifacts in scope because they show how the repository is operationalized beyond raw source files.",
                "evidence": infra_evidence,
            },
        ]
    else:
        items = [
            {
                "text": f"Start with the highest-priority subsystems such as {priority_label} to anchor review time on the areas with the most structural and interface density.",
                "evidence": priority_evidence,
            },
            {
                "text": "Inspect entrypoints, routes, and runtime observations before low-level files so the overall execution path is clear before detailed reading begins.",
                "evidence": interface_evidence,
            },
            {
                "text": "Use SQL, infrastructure, and cross-language signals to validate how code, data, and operational boundaries connect across the repository.",
                "evidence": data_evidence,
            },
        ]
    return {
        "audience": audience_name,
        "description": str(AUDIENCE_PROFILES.get(audience_name, {}).get("description", "")).strip(),
        "goal": str(goal or "").strip(),
        "items": items,
    }


def render_audience_plan_markdown(audience_plan: dict[str, Any]) -> str:
    payload = audience_plan if isinstance(audience_plan, dict) else {}
    items = payload.get("items", []) if isinstance(payload.get("items", []), list) else []
    lines = [
        "## Audience Focus (Deterministic)",
        "",
    ]
    if not items:
        lines.append("1. No audience-specific focus was derived from the scanned repository. [Evidence: none]")
        lines.append("")
        return "\n".join(lines)
    for idx, item in enumerate(items, start=1):
        text = str(item.get("text", "")).strip() or "No audience-specific focus was derived from the scanned repository."
        evidence = str(item.get("evidence", "none")).strip() or "none"
        lines.append(f"{idx}. {text} [Evidence: {evidence}]")
    lines.append("")
    return "\n".join(lines)


def format_audience_plan_for_prompt(audience_plan: dict[str, Any]) -> str:
    payload = audience_plan if isinstance(audience_plan, dict) else {}
    audience = str(payload.get("audience", "reviewer")).strip() or "reviewer"
    description = str(payload.get("description", "")).strip()
    items = payload.get("items", []) if isinstance(payload.get("items", []), list) else []
    lines = [f"- Audience: {audience}"]
    if description:
        lines.append(f"- Audience intent: {description}")
    for item in items:
        if not isinstance(item, dict):
            continue
        text = str(item.get("text", "")).strip()
        evidence = str(item.get("evidence", "")).strip()
        if text:
            suffix = f" [Evidence: {evidence}]" if evidence else ""
            lines.append(f"- {text}{suffix}")
    return "\n".join(lines)


def tokenize_question(text: str) -> list[str]:
    tokens = re.findall(r"[a-zA-Z0-9_]+", text.lower())
    out = []
    for t in tokens:
        if len(t) < 3:
            continue
        if t in STOPWORDS:
            continue
        out.append(t)
    return out


def load_fact_index(path: str) -> dict[str, Any]:
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, dict):
        raise ValueError("Fact index must be a JSON object.")
    return data


def answer_question_from_fact_index(question: str, fact_index: dict[str, Any], max_items: int = 10) -> str:
    q = question.lower().strip()
    files = fact_index.get("files", [])
    endpoints = fact_index.get("api_endpoints", [])
    dependencies = fact_index.get("dependencies", [])
    scripts = fact_index.get("scripts", [])
    entrypoints = fact_index.get("entrypoints", [])
    infra = fact_index.get("infrastructure", [])
    ai = fact_index.get("ai_signals", [])
    sql_entities = fact_index.get("sql_entities", [])
    sql_queries = fact_index.get("sql_queries", [])
    languages = fact_index.get("languages", {})
    language_symbols = fact_index.get("language_symbols", [])
    cross_file_symbol_edges = fact_index.get("cross_file_symbol_edges", [])
    cross_file_event_edges = fact_index.get("cross_file_event_edges", [])
    runtime_observations = fact_index.get("runtime_observations", [])

    lines = ["# Grounded Answer", ""]
    seen_lines: set[str] = set()

    def append_line(text: str) -> None:
        if text not in seen_lines:
            seen_lines.add(text)
            lines.append(text)

    if "how many" in q and "file" in q:
        ev = first_evidence_from_files(fact_index)
        append_line(f"- Indexed files: {len(files)}. [Evidence: {ev}]")
        return "\n".join(lines) + "\n"

    if "language" in q:
        if languages:
            lang_text = ", ".join([f"{k}:{v}" for k, v in sorted(languages.items(), key=lambda x: (-x[1], x[0]))[:10]])
            ev = first_evidence_from_files(fact_index)
            append_line(f"- Detected languages by file count: {lang_text}. [Evidence: {ev}]")
        else:
            append_line("- Unknown from provided code. [Evidence: none]")
        return "\n".join(lines) + "\n"

    matched = False

    if "subsystem" in q or "module" in q or "folder" in q or "folders" in q or "navigate" in q:
        subsystems = build_subsystem_summary_map(fact_index)
        for name, data in sorted(subsystems.items(), key=lambda kv: (-len(kv[1].get("files", [])), kv[0]))[:max_items]:
            first_file = data.get("files", [{}])[0]
            ev = f"{first_file.get('path', '')}#L1" if first_file.get("path") else "none"
            verification = data.get("endpoint_verification", {})
            total_endpoints = max(0, int(verification.get("total", len(data.get("endpoints", []))) or len(data.get("endpoints", []))))
            verified = int(verification.get("verified", 0) or 0)
            verification_pct = (float(verified) / float(total_endpoints) * 100.0) if total_endpoints > 0 else 0.0
            append_line(
                f"- Subsystem {name}: files={len(data.get('files', []))} endpoints={len(data.get('endpoints', []))} "
                f"dependencies={len(data.get('dependencies', []))} sql_entities={len(data.get('sql_entities', []))} "
                f"symbols={len(data.get('language_symbols', []))} runtime_observations={len(data.get('runtime_observations', []))} "
                f"verification_pct={verification_pct:.1f}%. [Evidence: {ev}]"
            )
            matched = True

    if "endpoint" in q or "api" in q or "route" in q:
        if endpoints:
            for item in endpoints[:max_items]:
                ev = item.get("evidence", "none")
                method = item.get("method", "GET")
                route = item.get("route", "/")
                file_name = item.get("file", "unknown")
                append_line(f"- Endpoint {method} {route} in {file_name}. [Evidence: {ev}]")
                matched = True

    if "dependenc" in q or "package" in q:
        if dependencies:
            for item in dependencies[:max_items]:
                ev = item.get("evidence", "none")
                name = item.get("name", "unknown")
                ver = item.get("version", "unknown")
                append_line(f"- Dependency {name} version {ver}. [Evidence: {ev}]")
                matched = True

    if "script" in q or "run" in q or "start" in q:
        if scripts:
            for item in scripts[:max_items]:
                ev = item.get("evidence", "none")
                name = item.get("name", "unknown")
                cmd = item.get("command", "unknown")
                append_line(f"- Script {name} executes {cmd}. [Evidence: {ev}]")
                matched = True

    if "entry" in q:
        if entrypoints:
            seen_entrypoints: set[tuple[str, str]] = set()
            for item in entrypoints[:max_items]:
                ev = item.get("evidence", "none")
                kind = item.get("kind", "entrypoint")
                file_name = item.get("file", "unknown")
                key = (str(kind), str(file_name))
                if key in seen_entrypoints:
                    continue
                seen_entrypoints.add(key)
                append_line(f"- Entrypoint signal {kind} in {file_name}. [Evidence: {ev}]")
                matched = True

    if "infra" in q or "docker" in q or "deploy" in q or "workflow" in q or "ci" in q:
        if infra:
            for item in infra[:max_items]:
                ev = item.get("evidence", "none")
                infra_type = item.get("type", "infrastructure_signal")
                file_name = item.get("file", "unknown")
                append_line(f"- Infrastructure signal {infra_type} in {file_name}. [Evidence: {ev}]")
                matched = True

    if "ai" in q or "llm" in q or "ollama" in q or "embedding" in q:
        if ai:
            for item in ai[:max_items]:
                ev = item.get("evidence", "none")
                name = item.get("name", "unknown")
                append_line(f"- AI signal {name} detected. [Evidence: {ev}]")
                matched = True

    if "sql" in q or "table" in q or "view" in q or "schema" in q or "query" in q or "database" in q or "data" in q:
        for item in sql_entities[:max_items]:
            append_line(
                f"- SQL entity {item.get('kind', 'entity')} {item.get('name', 'unknown')} in {item.get('file', 'unknown')}. "
                f"[Evidence: {item.get('evidence', 'none')}]"
            )
            matched = True
        for item in sql_queries[:max_items]:
            append_line(
                f"- SQL query {item.get('kind', 'query')} target {item.get('target', 'unknown')} in {item.get('file', 'unknown')}. "
                f"[Evidence: {item.get('evidence', 'none')}]"
            )
            matched = True

    if "symbol" in q or "function" in q or "class" in q or "method" in q or "call" in q:
        for item in language_symbols[:max_items]:
            append_line(
                f"- {item.get('language', 'code')} {item.get('kind', 'symbol')} {item.get('qualname', 'unknown')} in {item.get('file', 'unknown')}. "
                f"[Evidence: {item.get('evidence', 'none')}]"
            )
            matched = True
        if "cross" in q or "graph" in q or "call graph" in q or "callgraph" in q:
            for item in cross_file_symbol_edges[:max_items]:
                append_line(
                    f"- Cross-file symbol call {item.get('source_symbol', 'unknown')} in {item.get('source_file', 'unknown')} "
                    f"targets {item.get('target_symbol', 'unknown')} in {item.get('target_file', 'unknown')} "
                    f"resolution={item.get('resolution', 'unknown')}. "
                    f"[Evidence: {item.get('evidence', 'none')}]"
                )
                matched = True

    if "event" in q or "queue" in q or "kafka" in q or "rabbitmq" in q or "message" in q:
        for item in cross_file_event_edges[:max_items]:
            append_line(
                f"- Cross-file event flow {item.get('transport', 'event')} channel {item.get('channel', 'unknown')} "
                f"from {item.get('source_file', 'unknown')} to {item.get('target_file', 'unknown')}. "
                f"[Evidence: {item.get('source_evidence', item.get('evidence', 'none'))}]"
            )
            matched = True

    if "runtime" in q or "dynamic" in q or "probe" in q or "observed" in q:
        for item in runtime_observations[:max_items]:
            append_line(
                f"- Runtime observation {item.get('kind', 'runtime_observation')} {item.get('summary', 'unknown')}. "
                f"[Evidence: {item.get('evidence', 'none')}]"
            )
            matched = True

    if matched:
        return "\n".join(lines) + "\n"

    tokens = tokenize_question(question)

    def matches(text: str) -> bool:
        low = text.lower()
        return any(t in low for t in tokens)

    hit_count = 0
    for item in files:
        path = str(item.get("path", ""))
        if tokens and matches(path):
            append_line(f"- File match {path}. [Evidence: {path}#L1]")
            hit_count += 1
            if hit_count >= max_items:
                break

    if hit_count < max_items:
        for item in dependencies:
            name = str(item.get("name", ""))
            if tokens and matches(name):
                append_line(f"- Dependency match {name}. [Evidence: {item.get('evidence', 'none')}]")
                hit_count += 1
                if hit_count >= max_items:
                    break

    if hit_count < max_items:
        for item in endpoints:
            route = str(item.get("route", ""))
            if tokens and matches(route):
                append_line(
                    f"- Endpoint match {item.get('method', 'GET')} {route}. [Evidence: {item.get('evidence', 'none')}]"
                )
                hit_count += 1
                if hit_count >= max_items:
                    break

    if hit_count < max_items:
        for item in sql_entities:
            name = str(item.get("name", ""))
            if tokens and matches(name):
                append_line(
                    f"- SQL entity match {item.get('kind', 'entity')} {name}. [Evidence: {item.get('evidence', 'none')}]"
                )
                hit_count += 1
                if hit_count >= max_items:
                    break

    if hit_count == 0:
        append_line("- Unknown from provided code. [Evidence: none]")

    return "\n".join(lines) + "\n"


def run_agent_ask(args: argparse.Namespace) -> int:
    fact_index_path = args.fact_index
    if not os.path.exists(fact_index_path):
        print(f"❌ fact index not found: {fact_index_path}")
        return 1

    try:
        fact_index = load_fact_index(fact_index_path)
    except Exception as e:
        print(f"❌ failed to load fact index: {e}")
        return 1

    answer = answer_question_from_fact_index(args.question, fact_index)
    print(answer.rstrip())
    if args.save_to.strip():
        write_text(args.save_to, answer)
        print(f"[SAVED] {args.save_to}")
    return 0


def run_agent_compare_runs(args: argparse.Namespace) -> int:
    base_run = args.base_run
    head_run = args.head_run
    if not os.path.isdir(base_run):
        print(f"❌ base run directory not found: {base_run}")
        return 1
    if not os.path.isdir(head_run):
        print(f"❌ head run directory not found: {head_run}")
        return 1

    try:
        diff_obj = compare_run_dirs(base_run, head_run)
    except Exception as e:
        print(f"❌ failed to compare runs: {e}")
        return 1

    md = render_run_diff_markdown(diff_obj)
    write_text(args.out_md, md)
    print(f"[SAVED] {args.out_md}")
    if args.out_json.strip():
        write_json(args.out_json, diff_obj)
        print(f"[SAVED] {args.out_json}")
    return 0


def run_agent_trend_runs(args: argparse.Namespace) -> int:
    repo_path = os.path.abspath(os.path.expanduser(args.repo))
    if not os.path.isdir(repo_path):
        print(f"❌ Path is not a folder: {repo_path}")
        return 1
    runs_dir = analyzer.resolve_runs_dir(args.runs_dir, repo_path=repo_path)
    trends = build_repo_run_trends(
        runs_dir,
        repo_path,
        max_runs=int(getattr(args, "max_runs", 200) or 200),
    )
    write_json(args.out_json, trends)
    print(f"[SAVED] {args.out_json}")
    markdown = render_repo_run_trends_markdown(trends)
    write_text(args.out_md, markdown)
    print(f"[SAVED] {args.out_md}")
    return 0

def parse_models_csv(value: str) -> list[str]:
    items = []
    for raw in str(value or "").split(","):
        item = raw.strip()
        if item:
            items.append(item)
    seen = set()
    out = []
    for item in items:
        if item in seen:
            continue
        seen.add(item)
        out.append(item)
    return out

def benchmark_rank_key(result: dict[str, Any]) -> tuple:
    # Higher quality first, then faster latency.
    err = str(result.get("error", "")).strip()
    if err:
        return (0, 0.0, 0, -10_000, -10_000, -10_000, -10_000.0)
    return (
        1 if result.get("gate_pass", False) else 0,
        float(result.get("coverage", 0.0)),
        int(result.get("accepted_sections_count", 0)),
        -int(result.get("invalid_tokens", 0)),
        -int(result.get("claims_without_evidence", 0)),
        int(result.get("factual_bullets", 0)),
        -float(result.get("elapsed_sec", 0.0)),
    )

def select_best_benchmark_result(results: list[dict[str, Any]]) -> Optional[dict[str, Any]]:
    if not results:
        return None
    passed = [item for item in results if bool(item.get("gate_pass", False)) and not str(item.get("error", "")).strip()]
    if not passed:
        return None
    ranked = sorted(passed, key=benchmark_rank_key, reverse=True)
    return ranked[0]

def render_model_benchmark_markdown(data: dict[str, Any]) -> str:
    safe_repo_path = analyzer.display_safe_path(str(data.get("repo_path", "")))
    lines = [
        "# Model Benchmark",
        "",
        f"- Created At: `{data.get('created_at', '')}`",
        f"- Repo Path: `{safe_repo_path}`",
        f"- Backend: `{data.get('backend', '')}`",
        f"- Strategy: `{data.get('strategy', 'full_document')}`",
        f"- Goal: `{data.get('goal', '')}`",
        f"- Prompt Hash: `{str(data.get('prompt_hash', ''))[:16]}...`",
        "",
        "## Results",
        "",
        "| Model | Gate | Coverage | Accepted Sections | Factual Bullets | Missing Evidence | Invalid Tokens | Time Sec | Source | Error |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---|---|",
    ]
    for item in data.get("results", []):
        lines.append(
            "| "
            f"{item.get('model', '')} | "
            f"{'yes' if item.get('gate_pass', False) else 'no'} | "
            f"{float(item.get('coverage', 0.0)):.2%} | "
            f"{int(item.get('accepted_sections_count', 0))} | "
            f"{int(item.get('factual_bullets', 0))} | "
            f"{int(item.get('claims_without_evidence', 0))} | "
            f"{int(item.get('invalid_tokens', 0))} | "
            f"{float(item.get('elapsed_sec', 0.0)):.3f} | "
            f"{item.get('source', '')} | "
            f"{item.get('error', '')} |"
        )

    best = data.get("best")
    lines.extend(
        [
            "",
            "## Recommendation",
            f"- Recommended model: `{(best or {}).get('model', 'none')}`",
        ]
    )
    if best:
        lines.append(
            f"- Why: gate_pass={best.get('gate_pass', False)}, coverage={float(best.get('coverage', 0.0)):.2%}, accepted_sections={int(best.get('accepted_sections_count', 0))}, time_sec={float(best.get('elapsed_sec', 0.0)):.3f}"
        )
        lines.extend(
            [
                "",
                "## Apply",
                f"- `export OLLAMA_MODEL=\"{best.get('model', '')}\"`",
            ]
        )
    else:
        lines.append("- No model recommendation: none of the tested models passed strict grounding gate.")
    return "\n".join(lines) + "\n"

def run_agent_benchmark_models(args: argparse.Namespace) -> int:
    repo_path = os.path.abspath(os.path.expanduser(args.repo))
    if not os.path.isdir(repo_path):
        print(f"❌ Path is not a folder: {repo_path}")
        return 1

    try:
        ensure_llm_backend_ready()
    except Exception as e:
        print(f"❌ {e}")
        return 1

    models = parse_models_csv(args.models)
    if not models:
        print("❌ No models provided. Use --models \"model_a,model_b\"")
        return 1

    _code, redaction_stats = analyzer.read_files(repo_path, max_chars=analyzer.MAX_CHARS, collect_text=False)
    included_files = set([p.replace("\\", "/") for p in redaction_stats.get("included_files", [])])
    line_counts = {
        p.replace("\\", "/"): int(n)
        for p, n in redaction_stats.get("line_counts", {}).items()
    }
    if not included_files:
        print("❌ No files were collected. Check include extensions, skip rules, and max file size settings.")
        return 1

    fact_index, _fact_index_cache_stats = analyzer.build_local_fact_index_incremental(
        repo_path=repo_path,
        included_files=sorted(list(included_files)),
        line_counts=line_counts,
        use_cache=True,
    )
    prompt_fact_context = analyzer.build_prompt_fact_context(fact_index)
    prompt_fact_index_json = json.dumps(prompt_fact_context, ensure_ascii=True, indent=2)
    claim_support_index = analyzer.build_claim_support_index(fact_index, redaction_stats=redaction_stats)
    allowed_files_text = analyzer.format_allowed_files_for_prompt(list(included_files))
    allowed_evidence_text = analyzer.format_allowed_evidence_for_prompt(line_counts)
    goal_focus = build_goal_focus(fact_index, args.goal)
    audience_name = normalize_doc_audience(getattr(args, "audience", ""))
    audience_plan = build_audience_plan(fact_index, audience=audience_name, goal=args.goal)
    subsystem_priority_plan = build_subsystem_priority_plan(
        fact_index,
        goal=args.goal,
        audience=audience_name,
    )
    goal_focus_text = "\n\n".join(
        [
            format_goal_focus(goal_focus),
            "Audience-specific deterministic guidance:\n" + format_audience_plan_for_prompt(audience_plan),
        ]
    )
    strategy = str(getattr(args, "strategy", "hybrid_sections")).strip() or "hybrid_sections"
    if strategy == "full_document":
        prompt_material = build_document_prompt(
            goal=args.goal,
            redaction_stats=redaction_stats,
            allowed_files_text=allowed_files_text,
            allowed_evidence_text=allowed_evidence_text,
            fact_context_json=prompt_fact_index_json,
            goal_focus_text=goal_focus_text,
            feedback_text="",
        )
    else:
        prompt_material = json.dumps(
            {
                "strategy": strategy,
                "goal": args.goal,
                "goal_focus": goal_focus,
                "prompt_fact_context": prompt_fact_context,
                "base_report": analyzer.build_deterministic_report(fact_index, redaction_stats),
            },
            ensure_ascii=True,
            sort_keys=True,
        )
    prompt_hash = hashlib.sha256(prompt_material.encode("utf-8")).hexdigest()

    results: list[dict[str, Any]] = []
    for model in models:
        print(f"[INFO] Benchmarking model={model}")
        item: dict[str, Any] = {"model": model}
        t0 = time.perf_counter()
        try:
            analyzer.set_active_model_override(model)
            if strategy == "full_document":
                draft = analyzer.ollama_chat_with_retry(
                    model=model,
                    system=SYSTEM_PROMPT,
                    user=prompt_material,
                    temperature=float(args.temperature),
                )
                if analyzer.has_cjk(draft):
                    translate_prompt = f"""
Translate the following text to ENGLISH.
Rules:
* Output ONLY English.
* Keep headings, bullet formatting, and code blocks unchanged where possible.
* Do not include any Chinese characters.

TEXT:
{draft}
"""
                    draft = analyzer.ollama_chat_with_retry(
                        model=model,
                        system="Output ENGLISH only. No Chinese characters.",
                        user=translate_prompt,
                        temperature=0.0,
                    )

                draft, _repair_stats = analyzer.repair_grounding_if_needed(
                    report=draft,
                    included_files=included_files,
                    line_counts=line_counts,
                    allowed_evidence_text=allowed_evidence_text,
                    system_prompt=SYSTEM_PROMPT,
                    claim_support_index=claim_support_index,
                )
                draft = analyzer.sanitize_all_mermaid(draft)
                validation = analyzer.validate_report_grounding(
                    draft,
                    included_files,
                    line_counts,
                    claim_support_index=claim_support_index,
                )
                gate = analyzer.evaluate_grounding_gate(validation)
                source = "full_document_prompt"
                llm_enhancements: dict[str, Any] = {}
            else:
                hybrid_result = synthesize_hybrid_report(
                    repo_path=repo_path,
                    effective_mode="agent",
                    llm_output_policy="strict_gate",
                    fact_index=fact_index,
                    redaction_stats=redaction_stats,
                    included_files=included_files,
                    line_counts=line_counts,
                    allowed_evidence_text=allowed_evidence_text,
                    fact_context_json=prompt_fact_index_json,
                    goal_focus_text=goal_focus_text,
                    goal=args.goal,
                    audience=audience_name,
                    audience_plan=audience_plan,
                    subsystem_priority_plan=subsystem_priority_plan,
                    max_iterations=int(getattr(args, "max_iterations", 3) or 3),
                    claim_support_index=claim_support_index,
                )
                draft = str(hybrid_result.get("report", ""))
                validation = hybrid_result.get("validation", {})
                gate = hybrid_result.get("gate", {})
                source = str(hybrid_result.get("source", "")).strip()
                llm_enhancements = hybrid_result.get("llm_enhancements", {}) if isinstance(hybrid_result.get("llm_enhancements", {}), dict) else {}

            item.update(
                {
                    "gate_pass": bool(gate.get("pass", False)),
                    "coverage": float(gate.get("coverage", 0.0)),
                    "factual_bullets": int(validation.get("factual_bullets", 0)),
                    "claims_without_evidence": int(validation.get("claims_without_evidence", 0)),
                    "invalid_tokens": int(validation.get("invalid_evidence_tokens_count", 0)),
                    "accepted_sections_count": int(llm_enhancements.get("accepted_sections_count", 0) or 0),
                    "source": source,
                    "output_chars": len(draft),
                }
            )
            if args.save_reports_dir.strip():
                ensure_dir(args.save_reports_dir)
                slug = safe_slug(model)
                report_path = os.path.join(args.save_reports_dir, f"{slug}.md")
                write_text(report_path, draft)
                item["draft_report"] = report_path
        except Exception as e:
            item["error"] = str(e)
            item.setdefault("gate_pass", False)
            item.setdefault("coverage", 0.0)
            item.setdefault("factual_bullets", 0)
            item.setdefault("claims_without_evidence", 0)
            item.setdefault("invalid_tokens", 0)
            item.setdefault("accepted_sections_count", 0)
            item.setdefault("source", "")
        finally:
            analyzer.clear_active_model_override()
        item["elapsed_sec"] = round(time.perf_counter() - t0, 3)
        results.append(item)

    best = select_best_benchmark_result(results)
    out_data = {
        "created_at": utc_now_iso(),
        "repo_path": repo_path,
        "backend": analyzer.LLM_BACKEND,
        "strategy": strategy,
        "goal": args.goal.strip() or "full_repo_documentation",
        "prompt_hash": prompt_hash,
        "results": results,
        "best": best,
    }

    write_json(args.out_json, out_data)
    print(f"[SAVED] {args.out_json}")
    md = render_model_benchmark_markdown(out_data)
    write_text(args.out_md, md)
    print(f"[SAVED] {args.out_md}")
    if best:
        print(f"[INFO] recommended_model={best.get('model', '')}")
    else:
        print("[WARN] No tested model passed strict grounding on this prompt.")
    return 0


def copy_latest_run_summary(runs_dir: str, out_path: str) -> bool:
    if not os.path.isdir(runs_dir):
        return False
    candidates = []
    for name in os.listdir(runs_dir):
        full = os.path.join(runs_dir, name)
        if os.path.isdir(full):
            state = os.path.join(full, "state.json")
            summary = os.path.join(full, "run_summary.md")
            if os.path.exists(state) and os.path.exists(summary):
                candidates.append((os.path.getmtime(state), summary))
    if not candidates:
        return False
    candidates.sort(key=lambda x: x[0], reverse=True)
    shutil.copyfile(candidates[0][1], out_path)
    return True


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Local privacy first code documentation agent with strict grounding gate."
    )
    sub = parser.add_subparsers(dest="command")

    doc = sub.add_parser("document", help="Run the documentation agent.")
    doc.add_argument("--repo", required=True, help="Path to repository to document.")
    doc.add_argument("--goal", default="", help="Optional subsystem goal, for example auth or payments.")
    doc.add_argument(
        "--audience",
        choices=available_doc_audiences(),
        default="reviewer",
        help="Audience-aware deterministic planning profile for report overlays and prioritization.",
    )
    doc.add_argument("--mode", choices=["agent", "deterministic"], default="agent")
    doc.add_argument("--max-iterations", type=int, default=3, help="Max LLM refinement loops in agent mode.")
    doc.add_argument(
        "--llm-output-policy",
        choices=["strict_gate", "best_effort"],
        default=analyzer.resolve_llm_output_policy(""),
        help="In agent mode, either require a grounded passing draft or keep the best Ollama draft after retries.",
    )
    doc.add_argument(
        "--grounding-profile",
        choices=["standard", "enterprise_strict"],
        default=analyzer.active_grounding_profile(),
        help="Grounding profile. `enterprise_strict` requires full semantic support and full traceability.",
    )
    doc.add_argument(
        "--policy-pack",
        action="append",
        default=[],
        help=f"Repeatable enterprise preset overlay. Available packs: {', '.join(analyzer.available_policy_pack_names())}.",
    )
    doc.add_argument(
        "--runs-dir",
        default="",
        help="Directory to store run artifacts and state. Defaults to ~/Desktop/code_analyzer_reports/<repo>/code_analyzer_reports.",
    )
    doc.add_argument(
        "--resume-run",
        default="",
        help="Resume a previous run by run directory path or run id inside --runs-dir.",
    )
    doc.add_argument(
        "--runtime-probe",
        action=argparse.BooleanOptionalAction,
        default=None,
        help="Optionally execute short local runtime probe commands and include them as grounded artifacts.",
    )
    doc.add_argument(
        "--runtime-command",
        action="append",
        default=[],
        help="Repeatable runtime probe command. If omitted and runtime probe is enabled, safe candidates are inferred from facts.",
    )
    doc.add_argument("--runtime-timeout-seconds", type=float, default=None)
    doc.add_argument("--runtime-max-output-chars", type=int, default=None)
    doc.add_argument(
        "--require-llm",
        action=argparse.BooleanOptionalAction,
        default=False,
        help="Fail instead of falling back to deterministic mode when the local LLM backend is unavailable.",
    )
    doc.add_argument(
        "--write-root-outputs",
        action=argparse.BooleanOptionalAction,
        default=False,
        help="Write report and architecture files to project root in addition to run folder.",
    )

    ask = sub.add_parser("ask", help="Answer a question using only local fact_index evidence.")
    ask.add_argument("--question", required=True, help="Question to answer.")
    ask.add_argument("--fact-index", default=analyzer.FACT_INDEX_FILE, help="Path to fact_index JSON file.")
    ask.add_argument("--save-to", default="", help="Optional path to save the grounded answer markdown.")

    latest = sub.add_parser("latest-summary", help="Copy latest run summary into a target markdown file.")
    latest.add_argument("--runs-dir", default="runs")
    latest.add_argument("--out", default="latest_run_summary.md")

    cmp_run = sub.add_parser("compare-runs", help="Compare two run directories and produce delta report.")
    cmp_run.add_argument("--base-run", required=True, help="Base run directory path.")
    cmp_run.add_argument("--head-run", required=True, help="Head run directory path.")
    cmp_run.add_argument("--out-md", default="run_compare.md", help="Output markdown path.")
    cmp_run.add_argument("--out-json", default="run_compare.json", help="Output JSON path.")

    trend = sub.add_parser("trend-runs", help="Aggregate run trends across commits and branches for one repository.")
    trend.add_argument("--repo", required=True, help="Repository path whose runs should be aggregated.")
    trend.add_argument(
        "--runs-dir",
        default="",
        help="Runs directory. Defaults to the repo-specific resolved runs dir.",
    )
    trend.add_argument("--max-runs", type=int, default=200, help="Maximum matching runs to include.")
    trend.add_argument("--out-md", default="run_trends.md", help="Output markdown path.")
    trend.add_argument("--out-json", default="run_trends.json", help="Output JSON path.")

    bench = sub.add_parser("benchmark-models", help="Benchmark local models with grounded quality checks.")
    bench.add_argument("--repo", required=True, help="Path to repository to benchmark against.")
    bench.add_argument(
        "--models",
        default="qwen2.5-coder:7b,qwen3-coder:30b",
        help="Comma-separated model list to benchmark.",
    )
    bench.add_argument(
        "--strategy",
        choices=["hybrid_sections", "full_document"],
        default="hybrid_sections",
        help="Benchmark the production hybrid section path or the legacy full-document prompt.",
    )
    bench.add_argument("--goal", default="", help="Optional focus goal for benchmark prompt.")
    bench.add_argument(
        "--audience",
        choices=available_doc_audiences(),
        default="reviewer",
        help="Audience-aware deterministic planning profile for benchmarked report generation.",
    )
    bench.add_argument("--max-iterations", type=int, default=3, help="Max section refinement loops for hybrid benchmark mode.")
    bench.add_argument("--temperature", type=float, default=0.0, help="Sampling temperature for benchmark.")
    bench.add_argument("--out-md", default="model_benchmark.md", help="Output markdown path.")
    bench.add_argument("--out-json", default="model_benchmark.json", help="Output JSON path.")
    bench.add_argument("--save-reports-dir", default="", help="Optional directory to save per-model draft reports.")

    return parser


def main() -> int:
    argv = sys.argv[1:]
    if argv and argv[0] not in {"document", "ask", "latest-summary", "compare-runs", "trend-runs", "benchmark-models", "-h", "--help"}:
        # Convenience: allow `python3 agent.py --repo ...` without explicit subcommand.
        argv = ["document"] + argv

    grounding_profile_explicit = any(
        arg == "--grounding-profile" or str(arg).startswith("--grounding-profile=")
        for arg in argv
    )
    parser = build_parser()
    args = parser.parse_args(argv)
    args.grounding_profile_explicit = grounding_profile_explicit

    if args.command == "document":
        return run_agent_document(args)
    if args.command == "ask":
        return run_agent_ask(args)
    if args.command == "latest-summary":
        ok = copy_latest_run_summary(args.runs_dir, args.out)
        if not ok:
            print("❌ No completed run summary found.")
            return 1
        print(f"[SAVED] {args.out}")
        return 0
    if args.command == "compare-runs":
        return run_agent_compare_runs(args)
    if args.command == "trend-runs":
        return run_agent_trend_runs(args)
    if args.command == "benchmark-models":
        return run_agent_benchmark_models(args)

    parser.print_help()
    return 1


if __name__ == "__main__":
    sys.exit(main())
