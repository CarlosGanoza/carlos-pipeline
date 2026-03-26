# Usage

## Prerequisites

- Python 3.9+
- `pip`
- Graphviz if you want rendered diagram images

Optional:

- Ollama for local model-assisted runs

## Deterministic run

```bash
./run_agent.sh document --repo ./tests/fixtures/noise_proof_repo --mode deterministic
```

## Agent-assisted run

```bash
./run_agent.sh document --repo ./tests/fixtures/noise_proof_repo --mode agent
```

## Standalone analyzer

```bash
python3 main.py --repo ./tests/fixtures/noise_proof_repo --mode deterministic
```

## Validation run

```bash
bash run_quality_check.sh --evaluation-manifest evaluation_manifest.ci.json
```

## Sample artifacts

See:

- `sample_output/Output_code_analyzer_code_analyzer_demo_repo_100kloc/`

for an example completed run produced by the pipeline.
