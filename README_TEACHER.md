## Code Analyzer Local Pipeline

This folder is the local-only version of the project.

What it contains:
- `main.py`: deterministic codebase analyzer
- `agent.py`: local agent orchestration
- `run_local.sh`: simplest local run entrypoint
- `run_agent.sh`: local agent-enhanced run entrypoint
- `run_quality_check.sh`: validation harness entrypoint
- `docs/`: operator and product notes
- `submission/`: report-oriented summary material
- `tests/fixtures/`: sample repos for demos
- `outputs_quality_check/`: latest quality summary artifacts

What it does:
- scans a repo locally
- extracts grounded facts
- builds documentation and architecture artifacts
- stays local-first without enterprise approval or publish workflow

What it intentionally excludes:
- enterprise governance and publish scripts
- live credential files
- bulky historical evaluation run directories

Suggested teacher demo order:
1. Open `run_local.sh`
2. Open `main.py`
3. Open `outputs_quality_check/evaluation.results.md`
4. Run against a demo repo
