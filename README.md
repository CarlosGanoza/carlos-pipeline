# Code Analyzer Local Pipeline

This package contains the local-first version of the code analyzer.

## What it does

- scans a repository locally
- extracts grounded structural and behavioral facts
- generates documentation and architecture artifacts
- keeps the default workflow local and deterministic

## Included components

- `main.py`: deterministic analyzer and artifact generator
- `agent.py`: orchestration entrypoint for documentation runs
- `run_local.sh`: simplest local run wrapper
- `run_agent.sh`: local documentation wrapper
- `run_quality_check.sh`: validation harness
- `evaluation_manifest.ci.json`: benchmark manifest
- `outputs_quality_check/`: latest validation outputs
- `tests/fixtures/noise_proof_repo/`: bundled sample repository
- `sample_output/`: example generated run artifacts

## Quick start

Run a local deterministic analysis on the bundled sample repo:

```bash
chmod +x run_agent.sh
./run_agent.sh document --repo ./tests/fixtures/noise_proof_repo --mode deterministic
```

## Output artifacts

A completed run writes a timestamped folder with artifacts such as:

- `report.md`
- `run_summary.md`
- `fact_index.json`
- `architecture_model.json`
- `architecture_clean.svg`
- `architecture_clean.png`

## Validation

Run the packaged quality checks:

```bash
bash run_quality_check.sh --evaluation-manifest evaluation_manifest.ci.json
```

## Notes

- The default recommended workflow is deterministic local analysis.
- Optional local-model usage depends on local backend availability.
- This package intentionally excludes live enterprise credential files.
