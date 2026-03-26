# Evaluation Harness Results

- Generated At: `2026-03-25T21:36:55Z`
- Manifest: `/Users/carlosganoza/code-analyzer/evaluation_manifest.ci.json`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci`
- Cases: `271`

## Project Scorecard
### Privacy
- runs: `272`
- mean_redactions_applied: `0.000`
- security_policy_pass_rate: `1.000`
- model_safe_fact_index_rate: `1.000`

### Accuracy
- gate_pass_rate: `1.000`
- strict_traceability_pass_rate: `1.000`
- mean_evidence_coverage: `1.000`
- mean_semantic_coverage: `1.000`
- mean_unsupported_claims: `0.000`

### Goldens
- configured_runs: `272`
- pass_rate: `1.000`
- mean_precision: `1.000`
- mean_recall: `1.000`
- mean_f1: `1.000`
- mean_missing_count: `0.000`
- mean_unexpected_count: `0.000`

### Endpoint_Quality
- mean_verified_endpoint_rate: `0.000`
- mean_high_confidence_endpoint_rate: `0.007`
- mean_cross_file_inference_rate: `0.118`

### Navigability
- report_rate: `1.000`
- subsystem_index_rate: `1.000`
- graphviz_rate: `1.000`
- likec4_rate: `1.000`

### Updatability
- comparable_runs: `1`
- run_diff_artifact_rate: `1.000`
- pair_count: `1`
- pairs_with_fact_changes: `0`
- pairs_with_architecture_changes: `0`

## Quality Gates

- pass: `True`
- failure_count: `0`

### Project Scorecard Gates
- metric=`privacy.security_policy_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`accuracy.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`goldens.mean_precision` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`goldens.mean_recall` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`goldens.mean_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`accuracy.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`navigability.report_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`navigability.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: noise_repo_smoke

- Repo Path: `./tests/fixtures/noise_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/noise_repo_smoke`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.139`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143629` status=`completed` mode=`deterministic` elapsed=`0.139` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: updatability_repeat

- Repo Path: `./tests/fixtures/updatability_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/updatability_repeat`
- Run Count: `2`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.16249999999999998`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `2`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143629` status=`completed` mode=`deterministic` elapsed=`0.235` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`
- `run_20260325_143629_1` status=`completed` mode=`deterministic` elapsed=`0.09` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`2` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.run_diff_artifact_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

### Run Pairs
- `run_20260325_143629` -> `run_20260325_143629_1` endpoint_delta=`0` architecture_changed=`False` report_changed=`False`

## Case: demo_multistack_fixture

- Repo Path: `./tests/fixtures/demo_multistack_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/demo_multistack_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.104`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143629` status=`completed` mode=`deterministic` elapsed=`0.104` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: remix_fixture

- Repo Path: `./tests/fixtures/remix_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/remix_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.127`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143629` status=`completed` mode=`deterministic` elapsed=`0.127` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: nextjs_pages_api_fixture

- Repo Path: `./tests/fixtures/nextjs_pages_api_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/nextjs_pages_api_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.131`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143629` status=`completed` mode=`deterministic` elapsed=`0.131` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: nuxt_nitro_fixture

- Repo Path: `./tests/fixtures/nuxt_nitro_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/nuxt_nitro_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.119`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143629` status=`completed` mode=`deterministic` elapsed=`0.119` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: hono_fixture

- Repo Path: `./tests/fixtures/hono_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/hono_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.125`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143629` status=`completed` mode=`deterministic` elapsed=`0.125` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: koa_fixture

- Repo Path: `./tests/fixtures/koa_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/koa_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.125`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143630` status=`completed` mode=`deterministic` elapsed=`0.125` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: fastify_fixture

- Repo Path: `./tests/fixtures/fastify_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/fastify_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.116`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143630` status=`completed` mode=`deterministic` elapsed=`0.116` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: fastapi_router_fixture

- Repo Path: `./tests/fixtures/fastapi_router_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/fastapi_router_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.129`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143630` status=`completed` mode=`deterministic` elapsed=`0.129` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: flask_blueprint_fixture

- Repo Path: `./tests/fixtures/flask_blueprint_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/flask_blueprint_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.115`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143630` status=`completed` mode=`deterministic` elapsed=`0.115` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: flask_imported_blueprint_fixture

- Repo Path: `./tests/fixtures/flask_imported_blueprint_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/flask_imported_blueprint_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.062`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `1.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143630` status=`completed` mode=`deterministic` elapsed=`0.062` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: flask_imported_blueprint_noise_fixture

- Repo Path: `./tests/fixtures/flask_imported_blueprint_noise_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/flask_imported_blueprint_noise_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.061`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `1.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143630` status=`completed` mode=`deterministic` elapsed=`0.061` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: flask_imported_blueprint_handler_fixture

- Repo Path: `./tests/fixtures/flask_imported_blueprint_handler_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/flask_imported_blueprint_handler_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.075`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `1.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143630` status=`completed` mode=`deterministic` elapsed=`0.075` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: flask_imported_blueprint_handler_noise_fixture

- Repo Path: `./tests/fixtures/flask_imported_blueprint_handler_noise_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/flask_imported_blueprint_handler_noise_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.077`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `1.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143630` status=`completed` mode=`deterministic` elapsed=`0.077` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: js_route_constants_fixture

- Repo Path: `./tests/fixtures/js_route_constants_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/js_route_constants_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.121`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143630` status=`completed` mode=`deterministic` elapsed=`0.121` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: js_comment_noise_fixture

- Repo Path: `./tests/fixtures/js_comment_noise_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/js_comment_noise_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.111`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143631` status=`completed` mode=`deterministic` elapsed=`0.111` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: python_docstring_noise_fixture

- Repo Path: `./tests/fixtures/python_docstring_noise_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/python_docstring_noise_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.11`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143631` status=`completed` mode=`deterministic` elapsed=`0.11` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: websocket_fixture

- Repo Path: `./tests/fixtures/websocket_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/websocket_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.117`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143631` status=`completed` mode=`deterministic` elapsed=`0.117` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: fastapi_websocket_router_fixture

- Repo Path: `./tests/fixtures/fastapi_websocket_router_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/fastapi_websocket_router_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.076`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143631` status=`completed` mode=`deterministic` elapsed=`0.076` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: fastapi_imported_router_fixture

- Repo Path: `./tests/fixtures/fastapi_imported_router_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/fastapi_imported_router_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.075`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `1.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143631` status=`completed` mode=`deterministic` elapsed=`0.075` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: fastapi_imported_nested_router_fixture

- Repo Path: `./tests/fixtures/fastapi_imported_nested_router_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/fastapi_imported_nested_router_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.097`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `1.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143631` status=`completed` mode=`deterministic` elapsed=`0.097` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: fastapi_route_registration_fixture

- Repo Path: `./tests/fixtures/fastapi_route_registration_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/fastapi_route_registration_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.081`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143631` status=`completed` mode=`deterministic` elapsed=`0.081` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: fastapi_route_registration_noise_fixture

- Repo Path: `./tests/fixtures/fastapi_route_registration_noise_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/fastapi_route_registration_noise_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.082`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143631` status=`completed` mode=`deterministic` elapsed=`0.082` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: fastapi_imported_route_registration_fixture

- Repo Path: `./tests/fixtures/fastapi_imported_route_registration_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/fastapi_imported_route_registration_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.069`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `1.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143631` status=`completed` mode=`deterministic` elapsed=`0.069` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: fastapi_imported_route_registration_noise_fixture

- Repo Path: `./tests/fixtures/fastapi_imported_route_registration_noise_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/fastapi_imported_route_registration_noise_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.081`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `1.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143631` status=`completed` mode=`deterministic` elapsed=`0.081` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: fastapi_imported_router_call_handler_fixture

- Repo Path: `./tests/fixtures/fastapi_imported_router_call_handler_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/fastapi_imported_router_call_handler_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.074`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `1.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143631` status=`completed` mode=`deterministic` elapsed=`0.074` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: fastapi_imported_router_call_handler_noise_fixture

- Repo Path: `./tests/fixtures/fastapi_imported_router_call_handler_noise_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/fastapi_imported_router_call_handler_noise_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.074`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `1.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143631` status=`completed` mode=`deterministic` elapsed=`0.074` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: fastapi_api_route_decorator_fixture

- Repo Path: `./tests/fixtures/fastapi_api_route_decorator_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/fastapi_api_route_decorator_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.07`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143632` status=`completed` mode=`deterministic` elapsed=`0.07` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: fastapi_api_route_decorator_noise_fixture

- Repo Path: `./tests/fixtures/fastapi_api_route_decorator_noise_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/fastapi_api_route_decorator_noise_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.068`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143632` status=`completed` mode=`deterministic` elapsed=`0.068` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: fastapi_websocket_router_noise_fixture

- Repo Path: `./tests/fixtures/fastapi_websocket_router_noise_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/fastapi_websocket_router_noise_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.076`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143632` status=`completed` mode=`deterministic` elapsed=`0.076` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: fastapi_imported_router_noise_fixture

- Repo Path: `./tests/fixtures/fastapi_imported_router_noise_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/fastapi_imported_router_noise_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.063`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `1.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143632` status=`completed` mode=`deterministic` elapsed=`0.063` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: fastapi_imported_nested_router_noise_fixture

- Repo Path: `./tests/fixtures/fastapi_imported_nested_router_noise_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/fastapi_imported_nested_router_noise_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.079`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `1.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143632` status=`completed` mode=`deterministic` elapsed=`0.079` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: fastapi_websocket_route_decorator_fixture

- Repo Path: `./tests/fixtures/fastapi_websocket_route_decorator_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/fastapi_websocket_route_decorator_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.079`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143632` status=`completed` mode=`deterministic` elapsed=`0.079` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: fastapi_websocket_route_decorator_noise_fixture

- Repo Path: `./tests/fixtures/fastapi_websocket_route_decorator_noise_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/fastapi_websocket_route_decorator_noise_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.077`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143632` status=`completed` mode=`deterministic` elapsed=`0.077` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: starlette_routing_fixture

- Repo Path: `./tests/fixtures/starlette_routing_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/starlette_routing_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.075`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143632` status=`completed` mode=`deterministic` elapsed=`0.075` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: starlette_routing_noise_fixture

- Repo Path: `./tests/fixtures/starlette_routing_noise_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/starlette_routing_noise_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.091`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143632` status=`completed` mode=`deterministic` elapsed=`0.091` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: starlette_imported_routing_fixture

- Repo Path: `./tests/fixtures/starlette_imported_routing_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/starlette_imported_routing_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.079`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `1.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143632` status=`completed` mode=`deterministic` elapsed=`0.079` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: starlette_imported_routing_noise_fixture

- Repo Path: `./tests/fixtures/starlette_imported_routing_noise_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/starlette_imported_routing_noise_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.08`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `1.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143632` status=`completed` mode=`deterministic` elapsed=`0.08` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: starlette_imported_mount_routes_fixture

- Repo Path: `./tests/fixtures/starlette_imported_mount_routes_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/starlette_imported_mount_routes_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.098`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `1.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143632` status=`completed` mode=`deterministic` elapsed=`0.098` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: starlette_imported_mount_routes_noise_fixture

- Repo Path: `./tests/fixtures/starlette_imported_mount_routes_noise_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/starlette_imported_mount_routes_noise_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.075`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `1.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143633` status=`completed` mode=`deterministic` elapsed=`0.075` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: starlette_imported_mount_app_fixture

- Repo Path: `./tests/fixtures/starlette_imported_mount_app_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/starlette_imported_mount_app_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.077`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `1.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143633` status=`completed` mode=`deterministic` elapsed=`0.077` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: starlette_imported_mount_app_noise_fixture

- Repo Path: `./tests/fixtures/starlette_imported_mount_app_noise_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/starlette_imported_mount_app_noise_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.065`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `1.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143633` status=`completed` mode=`deterministic` elapsed=`0.065` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: starlette_imported_mount_handler_fixture

- Repo Path: `./tests/fixtures/starlette_imported_mount_handler_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/starlette_imported_mount_handler_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.075`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `1.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143633` status=`completed` mode=`deterministic` elapsed=`0.075` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: starlette_imported_mount_handler_noise_fixture

- Repo Path: `./tests/fixtures/starlette_imported_mount_handler_noise_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/starlette_imported_mount_handler_noise_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.075`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `1.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143633` status=`completed` mode=`deterministic` elapsed=`0.075` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: fastapi_websocket_registration_fixture

- Repo Path: `./tests/fixtures/fastapi_websocket_registration_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/fastapi_websocket_registration_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.079`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143633` status=`completed` mode=`deterministic` elapsed=`0.079` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: fastapi_websocket_registration_noise_fixture

- Repo Path: `./tests/fixtures/fastapi_websocket_registration_noise_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/fastapi_websocket_registration_noise_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.08`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143633` status=`completed` mode=`deterministic` elapsed=`0.08` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: fastapi_background_task_fixture

- Repo Path: `./tests/fixtures/fastapi_background_task_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/fastapi_background_task_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.084`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143633` status=`completed` mode=`deterministic` elapsed=`0.084` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: fastapi_background_task_noise_fixture

- Repo Path: `./tests/fixtures/fastapi_background_task_noise_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/fastapi_background_task_noise_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.083`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143633` status=`completed` mode=`deterministic` elapsed=`0.083` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: mixed_fastapi_background_task_flow_fixture

- Repo Path: `./tests/fixtures/mixed_fastapi_background_task_flow_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/mixed_fastapi_background_task_flow_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.096`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143633` status=`completed` mode=`deterministic` elapsed=`0.096` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: mixed_fastapi_background_task_flow_noise_fixture

- Repo Path: `./tests/fixtures/mixed_fastapi_background_task_flow_noise_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/mixed_fastapi_background_task_flow_noise_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.091`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143633` status=`completed` mode=`deterministic` elapsed=`0.091` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: mixed_fastapi_background_task_module_alias_flow_fixture

- Repo Path: `./tests/fixtures/mixed_fastapi_background_task_module_alias_flow_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/mixed_fastapi_background_task_module_alias_flow_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.087`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143633` status=`completed` mode=`deterministic` elapsed=`0.087` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: mixed_fastapi_background_task_module_alias_flow_noise_fixture

- Repo Path: `./tests/fixtures/mixed_fastapi_background_task_module_alias_flow_noise_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/mixed_fastapi_background_task_module_alias_flow_noise_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.083`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143634` status=`completed` mode=`deterministic` elapsed=`0.083` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: signalr_hub_fixture

- Repo Path: `./tests/fixtures/signalr_hub_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/signalr_hub_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.092`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143634` status=`completed` mode=`deterministic` elapsed=`0.092` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: signalr_hub_noise_fixture

- Repo Path: `./tests/fixtures/signalr_hub_noise_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/signalr_hub_noise_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.084`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143634` status=`completed` mode=`deterministic` elapsed=`0.084` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: csharp_grpc_fixture

- Repo Path: `./tests/fixtures/csharp_grpc_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/csharp_grpc_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.075`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `1.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143634` status=`completed` mode=`deterministic` elapsed=`0.075` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: csharp_grpc_noise_fixture

- Repo Path: `./tests/fixtures/csharp_grpc_noise_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/csharp_grpc_noise_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.073`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143634` status=`completed` mode=`deterministic` elapsed=`0.073` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: worker_entrypoint_fixture

- Repo Path: `./tests/fixtures/worker_entrypoint_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/worker_entrypoint_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.121`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143634` status=`completed` mode=`deterministic` elapsed=`0.121` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: celery_task_fixture

- Repo Path: `./tests/fixtures/celery_task_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/celery_task_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.108`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143634` status=`completed` mode=`deterministic` elapsed=`0.108` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: celery_task_noise_fixture

- Repo Path: `./tests/fixtures/celery_task_noise_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/celery_task_noise_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.111`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143634` status=`completed` mode=`deterministic` elapsed=`0.111` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: celery_producer_fixture

- Repo Path: `./tests/fixtures/celery_producer_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/celery_producer_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.092`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143634` status=`completed` mode=`deterministic` elapsed=`0.092` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: celery_producer_noise_fixture

- Repo Path: `./tests/fixtures/celery_producer_noise_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/celery_producer_noise_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.102`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143634` status=`completed` mode=`deterministic` elapsed=`0.102` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: airflow_dag_fixture

- Repo Path: `./tests/fixtures/airflow_dag_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/airflow_dag_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.104`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143634` status=`completed` mode=`deterministic` elapsed=`0.104` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: airflow_dag_noise_fixture

- Repo Path: `./tests/fixtures/airflow_dag_noise_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/airflow_dag_noise_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.099`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143635` status=`completed` mode=`deterministic` elapsed=`0.099` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: airflow_task_fixture

- Repo Path: `./tests/fixtures/airflow_task_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/airflow_task_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.098`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143635` status=`completed` mode=`deterministic` elapsed=`0.098` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: airflow_task_noise_fixture

- Repo Path: `./tests/fixtures/airflow_task_noise_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/airflow_task_noise_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.089`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143635` status=`completed` mode=`deterministic` elapsed=`0.089` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: airflow_decorator_dag_fixture

- Repo Path: `./tests/fixtures/airflow_decorator_dag_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/airflow_decorator_dag_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.08`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143635` status=`completed` mode=`deterministic` elapsed=`0.08` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: airflow_decorator_dag_noise_fixture

- Repo Path: `./tests/fixtures/airflow_decorator_dag_noise_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/airflow_decorator_dag_noise_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.074`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143635` status=`completed` mode=`deterministic` elapsed=`0.074` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: bullmq_worker_fixture

- Repo Path: `./tests/fixtures/bullmq_worker_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/bullmq_worker_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.11`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143635` status=`completed` mode=`deterministic` elapsed=`0.11` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: bullmq_worker_noise_fixture

- Repo Path: `./tests/fixtures/bullmq_worker_noise_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/bullmq_worker_noise_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.098`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143635` status=`completed` mode=`deterministic` elapsed=`0.098` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: bullmq_producer_fixture

- Repo Path: `./tests/fixtures/bullmq_producer_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/bullmq_producer_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.09`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143635` status=`completed` mode=`deterministic` elapsed=`0.09` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: bullmq_producer_noise_fixture

- Repo Path: `./tests/fixtures/bullmq_producer_noise_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/bullmq_producer_noise_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.08`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143635` status=`completed` mode=`deterministic` elapsed=`0.08` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: bullmq_flow_producer_fixture

- Repo Path: `./tests/fixtures/bullmq_flow_producer_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/bullmq_flow_producer_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.059`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143635` status=`completed` mode=`deterministic` elapsed=`0.059` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: bullmq_flow_producer_noise_fixture

- Repo Path: `./tests/fixtures/bullmq_flow_producer_noise_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/bullmq_flow_producer_noise_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.074`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143635` status=`completed` mode=`deterministic` elapsed=`0.074` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: bullmq_flow_producer_bulk_fixture

- Repo Path: `./tests/fixtures/bullmq_flow_producer_bulk_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/bullmq_flow_producer_bulk_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.07`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143636` status=`completed` mode=`deterministic` elapsed=`0.07` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: bullmq_flow_producer_bulk_noise_fixture

- Repo Path: `./tests/fixtures/bullmq_flow_producer_bulk_noise_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/bullmq_flow_producer_bulk_noise_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.057`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143636` status=`completed` mode=`deterministic` elapsed=`0.057` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: bullmq_repeatable_fixture

- Repo Path: `./tests/fixtures/bullmq_repeatable_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/bullmq_repeatable_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.092`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143636` status=`completed` mode=`deterministic` elapsed=`0.092` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: bullmq_job_scheduler_fixture

- Repo Path: `./tests/fixtures/bullmq_job_scheduler_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/bullmq_job_scheduler_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.076`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143636` status=`completed` mode=`deterministic` elapsed=`0.076` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: bullmq_job_scheduler_noise_fixture

- Repo Path: `./tests/fixtures/bullmq_job_scheduler_noise_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/bullmq_job_scheduler_noise_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.063`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143636` status=`completed` mode=`deterministic` elapsed=`0.063` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: mixed_bullmq_flow_fixture

- Repo Path: `./tests/fixtures/mixed_bullmq_flow_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/mixed_bullmq_flow_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.107`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143636` status=`completed` mode=`deterministic` elapsed=`0.107` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: mixed_bullmq_flow_producer_flow_fixture

- Repo Path: `./tests/fixtures/mixed_bullmq_flow_producer_flow_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/mixed_bullmq_flow_producer_flow_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.077`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143636` status=`completed` mode=`deterministic` elapsed=`0.077` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: mixed_bullmq_flow_producer_bulk_flow_fixture

- Repo Path: `./tests/fixtures/mixed_bullmq_flow_producer_bulk_flow_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/mixed_bullmq_flow_producer_bulk_flow_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.076`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143636` status=`completed` mode=`deterministic` elapsed=`0.076` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: mixed_bullmq_scheduler_flow_fixture

- Repo Path: `./tests/fixtures/mixed_bullmq_scheduler_flow_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/mixed_bullmq_scheduler_flow_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.081`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143636` status=`completed` mode=`deterministic` elapsed=`0.081` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: dagster_job_fixture

- Repo Path: `./tests/fixtures/dagster_job_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/dagster_job_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.104`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143636` status=`completed` mode=`deterministic` elapsed=`0.104` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: dagster_job_noise_fixture

- Repo Path: `./tests/fixtures/dagster_job_noise_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/dagster_job_noise_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.121`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143636` status=`completed` mode=`deterministic` elapsed=`0.121` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: dagster_asset_sensor_fixture

- Repo Path: `./tests/fixtures/dagster_asset_sensor_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/dagster_asset_sensor_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.094`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143636` status=`completed` mode=`deterministic` elapsed=`0.094` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: dagster_asset_sensor_noise_fixture

- Repo Path: `./tests/fixtures/dagster_asset_sensor_noise_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/dagster_asset_sensor_noise_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.11`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143637` status=`completed` mode=`deterministic` elapsed=`0.11` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: dagster_repository_fixture

- Repo Path: `./tests/fixtures/dagster_repository_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/dagster_repository_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.065`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143637` status=`completed` mode=`deterministic` elapsed=`0.065` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: dagster_repository_noise_fixture

- Repo Path: `./tests/fixtures/dagster_repository_noise_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/dagster_repository_noise_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.075`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143637` status=`completed` mode=`deterministic` elapsed=`0.075` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: csharp_hosted_service_fixture

- Repo Path: `./tests/fixtures/csharp_hosted_service_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/csharp_hosted_service_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.106`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143637` status=`completed` mode=`deterministic` elapsed=`0.106` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: csharp_hosted_service_noise_fixture

- Repo Path: `./tests/fixtures/csharp_hosted_service_noise_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/csharp_hosted_service_noise_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.118`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143637` status=`completed` mode=`deterministic` elapsed=`0.118` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: sidekiq_worker_fixture

- Repo Path: `./tests/fixtures/sidekiq_worker_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/sidekiq_worker_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.099`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143637` status=`completed` mode=`deterministic` elapsed=`0.099` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: sidekiq_worker_noise_fixture

- Repo Path: `./tests/fixtures/sidekiq_worker_noise_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/sidekiq_worker_noise_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.1`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143637` status=`completed` mode=`deterministic` elapsed=`0.1` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: sidekiq_producer_fixture

- Repo Path: `./tests/fixtures/sidekiq_producer_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/sidekiq_producer_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.09`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143637` status=`completed` mode=`deterministic` elapsed=`0.09` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: sidekiq_producer_noise_fixture

- Repo Path: `./tests/fixtures/sidekiq_producer_noise_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/sidekiq_producer_noise_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.09`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143637` status=`completed` mode=`deterministic` elapsed=`0.09` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: hangfire_recurring_job_fixture

- Repo Path: `./tests/fixtures/hangfire_recurring_job_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/hangfire_recurring_job_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.104`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143637` status=`completed` mode=`deterministic` elapsed=`0.104` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: hangfire_recurring_job_noise_fixture

- Repo Path: `./tests/fixtures/hangfire_recurring_job_noise_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/hangfire_recurring_job_noise_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.11`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143638` status=`completed` mode=`deterministic` elapsed=`0.11` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: quartz_scheduled_job_fixture

- Repo Path: `./tests/fixtures/quartz_scheduled_job_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/quartz_scheduled_job_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.106`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143638` status=`completed` mode=`deterministic` elapsed=`0.106` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: quartz_scheduled_job_noise_fixture

- Repo Path: `./tests/fixtures/quartz_scheduled_job_noise_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/quartz_scheduled_job_noise_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.101`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143638` status=`completed` mode=`deterministic` elapsed=`0.101` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: masstransit_consumer_fixture

- Repo Path: `./tests/fixtures/masstransit_consumer_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/masstransit_consumer_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.093`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143638` status=`completed` mode=`deterministic` elapsed=`0.093` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: masstransit_consumer_noise_fixture

- Repo Path: `./tests/fixtures/masstransit_consumer_noise_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/masstransit_consumer_noise_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.091`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143638` status=`completed` mode=`deterministic` elapsed=`0.091` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: masstransit_producer_fixture

- Repo Path: `./tests/fixtures/masstransit_producer_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/masstransit_producer_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.106`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143638` status=`completed` mode=`deterministic` elapsed=`0.106` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: masstransit_producer_noise_fixture

- Repo Path: `./tests/fixtures/masstransit_producer_noise_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/masstransit_producer_noise_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.091`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143638` status=`completed` mode=`deterministic` elapsed=`0.091` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: spring_scheduled_job_fixture

- Repo Path: `./tests/fixtures/spring_scheduled_job_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/spring_scheduled_job_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.103`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143638` status=`completed` mode=`deterministic` elapsed=`0.103` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: spring_scheduled_job_noise_fixture

- Repo Path: `./tests/fixtures/spring_scheduled_job_noise_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/spring_scheduled_job_noise_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.103`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143638` status=`completed` mode=`deterministic` elapsed=`0.103` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: spring_batch_job_fixture

- Repo Path: `./tests/fixtures/spring_batch_job_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/spring_batch_job_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.08`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143638` status=`completed` mode=`deterministic` elapsed=`0.08` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: spring_batch_job_noise_fixture

- Repo Path: `./tests/fixtures/spring_batch_job_noise_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/spring_batch_job_noise_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.087`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143639` status=`completed` mode=`deterministic` elapsed=`0.087` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: spring_kafka_consumer_fixture

- Repo Path: `./tests/fixtures/spring_kafka_consumer_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/spring_kafka_consumer_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.096`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143639` status=`completed` mode=`deterministic` elapsed=`0.096` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: spring_kafka_producer_fixture

- Repo Path: `./tests/fixtures/spring_kafka_producer_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/spring_kafka_producer_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.112`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143639` status=`completed` mode=`deterministic` elapsed=`0.112` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: spring_kafka_noise_fixture

- Repo Path: `./tests/fixtures/spring_kafka_noise_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/spring_kafka_noise_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.106`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143639` status=`completed` mode=`deterministic` elapsed=`0.106` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: spring_rabbitmq_consumer_fixture

- Repo Path: `./tests/fixtures/spring_rabbitmq_consumer_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/spring_rabbitmq_consumer_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.108`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143639` status=`completed` mode=`deterministic` elapsed=`0.108` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: spring_rabbitmq_producer_fixture

- Repo Path: `./tests/fixtures/spring_rabbitmq_producer_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/spring_rabbitmq_producer_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.096`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143639` status=`completed` mode=`deterministic` elapsed=`0.096` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: spring_rabbitmq_noise_fixture

- Repo Path: `./tests/fixtures/spring_rabbitmq_noise_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/spring_rabbitmq_noise_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.102`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143639` status=`completed` mode=`deterministic` elapsed=`0.102` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: go_cobra_command_fixture

- Repo Path: `./tests/fixtures/go_cobra_command_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/go_cobra_command_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.097`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143639` status=`completed` mode=`deterministic` elapsed=`0.097` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: go_cobra_command_noise_fixture

- Repo Path: `./tests/fixtures/go_cobra_command_noise_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/go_cobra_command_noise_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.103`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143639` status=`completed` mode=`deterministic` elapsed=`0.103` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: grpc_gateway_fixture

- Repo Path: `./tests/fixtures/grpc_gateway_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/grpc_gateway_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.102`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143639` status=`completed` mode=`deterministic` elapsed=`0.102` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: grpc_gateway_noise_fixture

- Repo Path: `./tests/fixtures/grpc_gateway_noise_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/grpc_gateway_noise_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.097`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143640` status=`completed` mode=`deterministic` elapsed=`0.097` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: goa_fixture

- Repo Path: `./tests/fixtures/goa_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/goa_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.069`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143640` status=`completed` mode=`deterministic` elapsed=`0.069` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: goa_noise_fixture

- Repo Path: `./tests/fixtures/goa_noise_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/goa_noise_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.076`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143640` status=`completed` mode=`deterministic` elapsed=`0.076` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: fiber_route_fixture

- Repo Path: `./tests/fixtures/fiber_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/fiber_route_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.102`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143640` status=`completed` mode=`deterministic` elapsed=`0.102` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: fiber_route_noise_fixture

- Repo Path: `./tests/fixtures/fiber_noise_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/fiber_route_noise_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.097`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143640` status=`completed` mode=`deterministic` elapsed=`0.097` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: laravel_artisan_command_fixture

- Repo Path: `./tests/fixtures/laravel_artisan_command_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/laravel_artisan_command_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.112`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143640` status=`completed` mode=`deterministic` elapsed=`0.112` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: laravel_artisan_command_noise_fixture

- Repo Path: `./tests/fixtures/laravel_artisan_command_noise_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/laravel_artisan_command_noise_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.102`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143640` status=`completed` mode=`deterministic` elapsed=`0.102` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: symfony_console_command_fixture

- Repo Path: `./tests/fixtures/symfony_console_command_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/symfony_console_command_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.1`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143640` status=`completed` mode=`deterministic` elapsed=`0.1` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: symfony_console_command_noise_fixture

- Repo Path: `./tests/fixtures/symfony_console_command_noise_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/symfony_console_command_noise_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.113`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143640` status=`completed` mode=`deterministic` elapsed=`0.113` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: laravel_scheduler_fixture

- Repo Path: `./tests/fixtures/laravel_scheduler_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/laravel_scheduler_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.111`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143640` status=`completed` mode=`deterministic` elapsed=`0.111` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: laravel_scheduler_noise_fixture

- Repo Path: `./tests/fixtures/laravel_scheduler_noise_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/laravel_scheduler_noise_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.111`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143641` status=`completed` mode=`deterministic` elapsed=`0.111` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: graphql_fixture

- Repo Path: `./tests/fixtures/graphql_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/graphql_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.118`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143641` status=`completed` mode=`deterministic` elapsed=`0.118` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: graphql_description_noise_fixture

- Repo Path: `./tests/fixtures/graphql_description_noise_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/graphql_description_noise_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.122`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143641` status=`completed` mode=`deterministic` elapsed=`0.122` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: graphql_resolver_fixture

- Repo Path: `./tests/fixtures/graphql_resolver_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/graphql_resolver_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.123`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143641` status=`completed` mode=`deterministic` elapsed=`0.123` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: graphql_resolver_noise_fixture

- Repo Path: `./tests/fixtures/graphql_resolver_noise_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/graphql_resolver_noise_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.098`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143641` status=`completed` mode=`deterministic` elapsed=`0.098` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: graphql_resolver_map_fixture

- Repo Path: `./tests/fixtures/graphql_resolver_map_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/graphql_resolver_map_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.077`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143641` status=`completed` mode=`deterministic` elapsed=`0.077` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: graphql_resolver_map_noise_fixture

- Repo Path: `./tests/fixtures/graphql_resolver_map_noise_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/graphql_resolver_map_noise_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.069`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143641` status=`completed` mode=`deterministic` elapsed=`0.069` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: graphql_resolver_map_variable_fixture

- Repo Path: `./tests/fixtures/graphql_resolver_map_variable_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/graphql_resolver_map_variable_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.065`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143641` status=`completed` mode=`deterministic` elapsed=`0.065` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: graphql_resolver_map_variable_noise_fixture

- Repo Path: `./tests/fixtures/graphql_resolver_map_variable_noise_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/graphql_resolver_map_variable_noise_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.06`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143641` status=`completed` mode=`deterministic` elapsed=`0.06` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: graphql_resolver_map_typed_variable_fixture

- Repo Path: `./tests/fixtures/graphql_resolver_map_typed_variable_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/graphql_resolver_map_typed_variable_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.064`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143641` status=`completed` mode=`deterministic` elapsed=`0.064` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: graphql_resolver_map_typed_variable_noise_fixture

- Repo Path: `./tests/fixtures/graphql_resolver_map_typed_variable_noise_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/graphql_resolver_map_typed_variable_noise_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.069`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143641` status=`completed` mode=`deterministic` elapsed=`0.069` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: graphql_resolver_map_spread_fixture

- Repo Path: `./tests/fixtures/graphql_resolver_map_spread_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/graphql_resolver_map_spread_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.075`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143642` status=`completed` mode=`deterministic` elapsed=`0.075` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: graphql_resolver_map_spread_noise_fixture

- Repo Path: `./tests/fixtures/graphql_resolver_map_spread_noise_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/graphql_resolver_map_spread_noise_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.059`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143642` status=`completed` mode=`deterministic` elapsed=`0.059` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: graphql_resolver_map_assertion_fixture

- Repo Path: `./tests/fixtures/graphql_resolver_map_assertion_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/graphql_resolver_map_assertion_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.064`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143642` status=`completed` mode=`deterministic` elapsed=`0.064` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: graphql_resolver_map_assertion_noise_fixture

- Repo Path: `./tests/fixtures/graphql_resolver_map_assertion_noise_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/graphql_resolver_map_assertion_noise_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.067`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143642` status=`completed` mode=`deterministic` elapsed=`0.067` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: graphql_resolver_map_imported_fixture

- Repo Path: `./tests/fixtures/graphql_resolver_map_imported_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/graphql_resolver_map_imported_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.077`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `1.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143642` status=`completed` mode=`deterministic` elapsed=`0.077` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: graphql_resolver_map_imported_noise_fixture

- Repo Path: `./tests/fixtures/graphql_resolver_map_imported_noise_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/graphql_resolver_map_imported_noise_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.075`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143642` status=`completed` mode=`deterministic` elapsed=`0.075` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: graphql_resolver_map_namespace_imported_fixture

- Repo Path: `./tests/fixtures/graphql_resolver_map_namespace_imported_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/graphql_resolver_map_namespace_imported_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.102`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `1.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143642` status=`completed` mode=`deterministic` elapsed=`0.102` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: graphql_resolver_map_namespace_imported_noise_fixture

- Repo Path: `./tests/fixtures/graphql_resolver_map_namespace_imported_noise_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/graphql_resolver_map_namespace_imported_noise_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.088`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143642` status=`completed` mode=`deterministic` elapsed=`0.088` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: graphql_resolve_field_fixture

- Repo Path: `./tests/fixtures/graphql_resolve_field_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/graphql_resolve_field_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.076`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143642` status=`completed` mode=`deterministic` elapsed=`0.076` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: graphql_resolve_field_noise_fixture

- Repo Path: `./tests/fixtures/graphql_resolve_field_noise_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/graphql_resolve_field_noise_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.061`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143642` status=`completed` mode=`deterministic` elapsed=`0.061` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: grpc_fixture

- Repo Path: `./tests/fixtures/grpc_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/grpc_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.12`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143642` status=`completed` mode=`deterministic` elapsed=`0.12` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: openapi_fixture

- Repo Path: `./tests/fixtures/openapi_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/openapi_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.117`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `1.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143642` status=`completed` mode=`deterministic` elapsed=`0.117` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: asyncapi_fixture

- Repo Path: `./tests/fixtures/asyncapi_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/asyncapi_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.121`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `1.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143643` status=`completed` mode=`deterministic` elapsed=`0.121` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: kubernetes_fixture

- Repo Path: `./tests/fixtures/kubernetes_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/kubernetes_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.118`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143643` status=`completed` mode=`deterministic` elapsed=`0.118` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: helm_ingress_fixture

- Repo Path: `./tests/fixtures/helm_ingress_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/helm_ingress_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.116`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143643` status=`completed` mode=`deterministic` elapsed=`0.116` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: kubectl_runbook_fixture

- Repo Path: `./tests/fixtures/kubectl_runbook_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/kubectl_runbook_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.115`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143643` status=`completed` mode=`deterministic` elapsed=`0.115` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: kubernetes_cronjob_fixture

- Repo Path: `./tests/fixtures/kubernetes_cronjob_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/kubernetes_cronjob_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.102`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143643` status=`completed` mode=`deterministic` elapsed=`0.102` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: github_actions_schedule_fixture

- Repo Path: `./tests/fixtures/github_actions_schedule_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/github_actions_schedule_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.107`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143643` status=`completed` mode=`deterministic` elapsed=`0.107` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: sveltekit_fixture

- Repo Path: `./tests/fixtures/sveltekit_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/sveltekit_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.127`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143643` status=`completed` mode=`deterministic` elapsed=`0.127` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: astro_fixture

- Repo Path: `./tests/fixtures/astro_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/astro_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.125`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143643` status=`completed` mode=`deterministic` elapsed=`0.125` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: nestjs_fixture

- Repo Path: `./tests/fixtures/nestjs_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/nestjs_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.129`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143643` status=`completed` mode=`deterministic` elapsed=`0.129` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: nestjs_gateway_fixture

- Repo Path: `./tests/fixtures/nestjs_gateway_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/nestjs_gateway_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.104`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143644` status=`completed` mode=`deterministic` elapsed=`0.104` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: nestjs_gateway_noise_fixture

- Repo Path: `./tests/fixtures/nestjs_gateway_noise_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/nestjs_gateway_noise_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.086`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143644` status=`completed` mode=`deterministic` elapsed=`0.086` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: nestjs_gateway_path_fixture

- Repo Path: `./tests/fixtures/nestjs_gateway_path_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/nestjs_gateway_path_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.065`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143644` status=`completed` mode=`deterministic` elapsed=`0.065` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: nestjs_gateway_path_noise_fixture

- Repo Path: `./tests/fixtures/nestjs_gateway_path_noise_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/nestjs_gateway_path_noise_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.06`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143644` status=`completed` mode=`deterministic` elapsed=`0.06` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: csharp_minimal_api_fixture

- Repo Path: `./tests/fixtures/csharp_minimal_api_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/csharp_minimal_api_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.117`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143644` status=`completed` mode=`deterministic` elapsed=`0.117` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: nestjs_constants_fixture

- Repo Path: `./tests/fixtures/nestjs_constants_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/nestjs_constants_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.116`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143644` status=`completed` mode=`deterministic` elapsed=`0.116` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: spring_fixture

- Repo Path: `./tests/fixtures/spring_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/spring_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.115`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143644` status=`completed` mode=`deterministic` elapsed=`0.115` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: spring_constants_fixture

- Repo Path: `./tests/fixtures/spring_constants_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/spring_constants_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.138`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143644` status=`completed` mode=`deterministic` elapsed=`0.138` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: drf_router_fixture

- Repo Path: `./tests/fixtures/drf_router_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/drf_router_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.125`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `1.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143644` status=`completed` mode=`deterministic` elapsed=`0.125` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: django_fixture

- Repo Path: `./tests/fixtures/django_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/django_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.113`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143645` status=`completed` mode=`deterministic` elapsed=`0.113` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: django_imported_view_fixture

- Repo Path: `./tests/fixtures/django_imported_view_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/django_imported_view_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.076`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `1.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143645` status=`completed` mode=`deterministic` elapsed=`0.076` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: django_imported_view_noise_fixture

- Repo Path: `./tests/fixtures/django_imported_view_noise_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/django_imported_view_noise_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.077`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `1.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143645` status=`completed` mode=`deterministic` elapsed=`0.077` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: django_class_view_fixture

- Repo Path: `./tests/fixtures/django_class_view_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/django_class_view_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.079`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `1.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143645` status=`completed` mode=`deterministic` elapsed=`0.079` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: django_class_view_noise_fixture

- Repo Path: `./tests/fixtures/django_class_view_noise_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/django_class_view_noise_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.077`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `1.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143645` status=`completed` mode=`deterministic` elapsed=`0.077` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: django_include_fixture

- Repo Path: `./tests/fixtures/django_include_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/django_include_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.08`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `1.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143645` status=`completed` mode=`deterministic` elapsed=`0.08` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: django_include_noise_fixture

- Repo Path: `./tests/fixtures/django_include_imported_view_noise_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/django_include_noise_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.153`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `1.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143645` status=`completed` mode=`deterministic` elapsed=`0.153` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: django_include_tuple_fixture

- Repo Path: `./tests/fixtures/django_include_tuple_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/django_include_tuple_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.077`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `1.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143645` status=`completed` mode=`deterministic` elapsed=`0.077` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: django_include_tuple_noise_fixture

- Repo Path: `./tests/fixtures/django_include_tuple_noise_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/django_include_tuple_noise_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.075`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `1.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143645` status=`completed` mode=`deterministic` elapsed=`0.075` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: rails_fixture

- Repo Path: `./tests/fixtures/rails_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/rails_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.135`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143645` status=`completed` mode=`deterministic` elapsed=`0.135` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: laravel_fixture

- Repo Path: `./tests/fixtures/laravel_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/laravel_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.118`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143645` status=`completed` mode=`deterministic` elapsed=`0.118` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: gin_fixture

- Repo Path: `./tests/fixtures/gin_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/gin_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.115`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143646` status=`completed` mode=`deterministic` elapsed=`0.115` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: chi_fixture

- Repo Path: `./tests/fixtures/chi_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/chi_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.116`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143646` status=`completed` mode=`deterministic` elapsed=`0.116` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: echo_fixture

- Repo Path: `./tests/fixtures/echo_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/echo_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.098`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143646` status=`completed` mode=`deterministic` elapsed=`0.098` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: django_include_missing_module_noise_fixture

- Repo Path: `./tests/fixtures/django_include_noise_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/django_include_missing_module_noise_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.056`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143646` status=`completed` mode=`deterministic` elapsed=`0.056` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: rust_route_fixture

- Repo Path: `./tests/fixtures/rust_route_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/rust_route_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.102`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143646` status=`completed` mode=`deterministic` elapsed=`0.102` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: actix_scope_fixture

- Repo Path: `./tests/fixtures/actix_scope_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/actix_scope_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.087`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143646` status=`completed` mode=`deterministic` elapsed=`0.087` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: actix_scope_noise_fixture

- Repo Path: `./tests/fixtures/actix_scope_noise_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/actix_scope_noise_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.074`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143646` status=`completed` mode=`deterministic` elapsed=`0.074` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: rocket_mount_fixture

- Repo Path: `./tests/fixtures/rocket_mount_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/rocket_mount_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.078`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143646` status=`completed` mode=`deterministic` elapsed=`0.078` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: rocket_mount_noise_fixture

- Repo Path: `./tests/fixtures/rocket_mount_noise_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/rocket_mount_noise_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.077`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143646` status=`completed` mode=`deterministic` elapsed=`0.077` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: warp_fixture

- Repo Path: `./tests/fixtures/warp_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/warp_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.081`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143646` status=`completed` mode=`deterministic` elapsed=`0.081` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: warp_noise_fixture

- Repo Path: `./tests/fixtures/warp_noise_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/warp_noise_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.083`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143647` status=`completed` mode=`deterministic` elapsed=`0.083` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: tonic_grpc_fixture

- Repo Path: `./tests/fixtures/tonic_grpc_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/tonic_grpc_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.074`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143647` status=`completed` mode=`deterministic` elapsed=`0.074` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: tonic_grpc_noise_fixture

- Repo Path: `./tests/fixtures/tonic_grpc_noise_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/tonic_grpc_noise_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.082`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143647` status=`completed` mode=`deterministic` elapsed=`0.082` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: axum_fixture

- Repo Path: `./tests/fixtures/axum_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/axum_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.103`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143647` status=`completed` mode=`deterministic` elapsed=`0.103` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: axum_comment_noise_fixture

- Repo Path: `./tests/fixtures/axum_comment_noise_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/axum_comment_noise_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.105`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143647` status=`completed` mode=`deterministic` elapsed=`0.105` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: rust_clap_command_fixture

- Repo Path: `./tests/fixtures/rust_clap_command_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/rust_clap_command_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.101`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143647` status=`completed` mode=`deterministic` elapsed=`0.101` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: rust_clap_command_noise_fixture

- Repo Path: `./tests/fixtures/rust_clap_command_noise_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/rust_clap_command_noise_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.084`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143647` status=`completed` mode=`deterministic` elapsed=`0.084` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: rust_clap_derive_fixture

- Repo Path: `./tests/fixtures/rust_clap_derive_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/rust_clap_derive_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.07`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143647` status=`completed` mode=`deterministic` elapsed=`0.07` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: rust_clap_derive_noise_fixture

- Repo Path: `./tests/fixtures/rust_clap_derive_noise_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/rust_clap_derive_noise_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.086`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143647` status=`completed` mode=`deterministic` elapsed=`0.086` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: csharp_attribute_route_fixture

- Repo Path: `./tests/fixtures/csharp_attribute_route_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/csharp_attribute_route_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.117`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143647` status=`completed` mode=`deterministic` elapsed=`0.117` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: php_route_fixture

- Repo Path: `./tests/fixtures/php_route_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/php_route_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.106`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143647` status=`completed` mode=`deterministic` elapsed=`0.106` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: ruby_route_fixture

- Repo Path: `./tests/fixtures/ruby_route_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/ruby_route_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.119`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143648` status=`completed` mode=`deterministic` elapsed=`0.119` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: aspnet_controller_fixture

- Repo Path: `./tests/fixtures/aspnet_controller_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/aspnet_controller_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.109`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143648` status=`completed` mode=`deterministic` elapsed=`0.109` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: csharp_attribute_noise_fixture

- Repo Path: `./tests/fixtures/csharp_attribute_noise_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/csharp_attribute_noise_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.121`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143648` status=`completed` mode=`deterministic` elapsed=`0.121` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: celery_beat_schedule_fixture

- Repo Path: `./tests/fixtures/celery_beat_schedule_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/celery_beat_schedule_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.115`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143648` status=`completed` mode=`deterministic` elapsed=`0.115` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: celery_beat_schedule_noise_fixture

- Repo Path: `./tests/fixtures/celery_beat_schedule_noise_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/celery_beat_schedule_noise_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.112`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143648` status=`completed` mode=`deterministic` elapsed=`0.112` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: django_channels_fixture

- Repo Path: `./tests/fixtures/django_channels_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/django_channels_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.101`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143648` status=`completed` mode=`deterministic` elapsed=`0.101` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: django_channels_noise_fixture

- Repo Path: `./tests/fixtures/django_channels_noise_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/django_channels_noise_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.103`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143648` status=`completed` mode=`deterministic` elapsed=`0.103` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: socketio_event_fixture

- Repo Path: `./tests/fixtures/socketio_event_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/socketio_event_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.114`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143648` status=`completed` mode=`deterministic` elapsed=`0.114` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: socketio_event_noise_fixture

- Repo Path: `./tests/fixtures/socketio_event_noise_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/socketio_event_noise_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.089`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143648` status=`completed` mode=`deterministic` elapsed=`0.089` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: socketio_inline_namespace_fixture

- Repo Path: `./tests/fixtures/socketio_inline_namespace_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/socketio_inline_namespace_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.077`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143649` status=`completed` mode=`deterministic` elapsed=`0.077` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: socketio_inline_namespace_noise_fixture

- Repo Path: `./tests/fixtures/socketio_inline_namespace_noise_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/socketio_inline_namespace_noise_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.064`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143649` status=`completed` mode=`deterministic` elapsed=`0.064` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: trpc_router_fixture

- Repo Path: `./tests/fixtures/trpc_router_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/trpc_router_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.116`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143649` status=`completed` mode=`deterministic` elapsed=`0.116` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: trpc_router_noise_fixture

- Repo Path: `./tests/fixtures/trpc_router_noise_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/trpc_router_noise_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.109`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143649` status=`completed` mode=`deterministic` elapsed=`0.109` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: go_cron_job_fixture

- Repo Path: `./tests/fixtures/go_cron_job_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/go_cron_job_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.113`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143649` status=`completed` mode=`deterministic` elapsed=`0.113` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: go_cron_job_noise_fixture

- Repo Path: `./tests/fixtures/go_cron_job_noise_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/go_cron_job_noise_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.097`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143649` status=`completed` mode=`deterministic` elapsed=`0.097` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: go_gocron_job_fixture

- Repo Path: `./tests/fixtures/go_gocron_job_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/go_gocron_job_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.095`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143649` status=`completed` mode=`deterministic` elapsed=`0.095` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: go_gocron_job_noise_fixture

- Repo Path: `./tests/fixtures/go_gocron_job_noise_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/go_gocron_job_noise_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.096`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143649` status=`completed` mode=`deterministic` elapsed=`0.096` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: rake_task_fixture

- Repo Path: `./tests/fixtures/rake_task_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/rake_task_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.121`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143649` status=`completed` mode=`deterministic` elapsed=`0.121` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: rake_task_noise_fixture

- Repo Path: `./tests/fixtures/rake_task_noise_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/rake_task_noise_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.1`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143649` status=`completed` mode=`deterministic` elapsed=`0.1` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: activejob_job_fixture

- Repo Path: `./tests/fixtures/activejob_job_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/activejob_job_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.091`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143650` status=`completed` mode=`deterministic` elapsed=`0.091` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: activejob_job_noise_fixture

- Repo Path: `./tests/fixtures/activejob_job_noise_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/activejob_job_noise_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.109`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143650` status=`completed` mode=`deterministic` elapsed=`0.109` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: activejob_producer_fixture

- Repo Path: `./tests/fixtures/activejob_producer_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/activejob_producer_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.11`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143650` status=`completed` mode=`deterministic` elapsed=`0.11` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: activejob_producer_noise_fixture

- Repo Path: `./tests/fixtures/activejob_producer_noise_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/activejob_producer_noise_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.102`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143650` status=`completed` mode=`deterministic` elapsed=`0.102` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: que_job_fixture

- Repo Path: `./tests/fixtures/que_job_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/que_job_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.086`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143650` status=`completed` mode=`deterministic` elapsed=`0.086` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: que_job_noise_fixture

- Repo Path: `./tests/fixtures/que_job_noise_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/que_job_noise_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.082`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143650` status=`completed` mode=`deterministic` elapsed=`0.082` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: que_producer_fixture

- Repo Path: `./tests/fixtures/que_producer_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/que_producer_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.086`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143650` status=`completed` mode=`deterministic` elapsed=`0.086` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: que_producer_noise_fixture

- Repo Path: `./tests/fixtures/que_producer_noise_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/que_producer_noise_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.095`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143650` status=`completed` mode=`deterministic` elapsed=`0.095` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: actioncable_channel_fixture

- Repo Path: `./tests/fixtures/actioncable_channel_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/actioncable_channel_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.106`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143650` status=`completed` mode=`deterministic` elapsed=`0.106` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: actioncable_channel_noise_fixture

- Repo Path: `./tests/fixtures/actioncable_channel_noise_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/actioncable_channel_noise_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.099`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143650` status=`completed` mode=`deterministic` elapsed=`0.099` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: laravel_queue_job_fixture

- Repo Path: `./tests/fixtures/laravel_queue_job_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/laravel_queue_job_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.112`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143651` status=`completed` mode=`deterministic` elapsed=`0.112` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: laravel_queue_job_noise_fixture

- Repo Path: `./tests/fixtures/laravel_queue_job_noise_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/laravel_queue_job_noise_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.109`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143651` status=`completed` mode=`deterministic` elapsed=`0.109` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: laravel_queue_producer_fixture

- Repo Path: `./tests/fixtures/laravel_queue_producer_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/laravel_queue_producer_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.084`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143651` status=`completed` mode=`deterministic` elapsed=`0.084` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: laravel_queue_producer_noise_fixture

- Repo Path: `./tests/fixtures/laravel_queue_producer_noise_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/laravel_queue_producer_noise_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.094`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143651` status=`completed` mode=`deterministic` elapsed=`0.094` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: kafka_consumer_fixture

- Repo Path: `./tests/fixtures/kafka_consumer_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/kafka_consumer_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.118`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143651` status=`completed` mode=`deterministic` elapsed=`0.118` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: kafka_consumer_noise_fixture

- Repo Path: `./tests/fixtures/kafka_consumer_noise_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/kafka_consumer_noise_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.096`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143651` status=`completed` mode=`deterministic` elapsed=`0.096` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: kafka_producer_fixture

- Repo Path: `./tests/fixtures/kafka_producer_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/kafka_producer_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.105`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143651` status=`completed` mode=`deterministic` elapsed=`0.105` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: kafka_producer_noise_fixture

- Repo Path: `./tests/fixtures/kafka_producer_noise_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/kafka_producer_noise_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.111`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143651` status=`completed` mode=`deterministic` elapsed=`0.111` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: mixed_kafka_flow_fixture

- Repo Path: `./tests/fixtures/mixed_kafka_flow_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/mixed_kafka_flow_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.113`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143651` status=`completed` mode=`deterministic` elapsed=`0.113` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: mixed_spring_kafka_flow_fixture

- Repo Path: `./tests/fixtures/mixed_spring_kafka_flow_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/mixed_spring_kafka_flow_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.117`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143651` status=`completed` mode=`deterministic` elapsed=`0.117` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: rabbitmq_consumer_fixture

- Repo Path: `./tests/fixtures/rabbitmq_consumer_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/rabbitmq_consumer_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.098`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143652` status=`completed` mode=`deterministic` elapsed=`0.098` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: rabbitmq_consumer_noise_fixture

- Repo Path: `./tests/fixtures/rabbitmq_consumer_noise_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/rabbitmq_consumer_noise_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.098`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143652` status=`completed` mode=`deterministic` elapsed=`0.098` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: rabbitmq_producer_fixture

- Repo Path: `./tests/fixtures/rabbitmq_producer_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/rabbitmq_producer_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.106`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143652` status=`completed` mode=`deterministic` elapsed=`0.106` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: rabbitmq_producer_noise_fixture

- Repo Path: `./tests/fixtures/rabbitmq_producer_noise_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/rabbitmq_producer_noise_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.097`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143652` status=`completed` mode=`deterministic` elapsed=`0.097` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: rabbitmq_js_consumer_fixture

- Repo Path: `./tests/fixtures/rabbitmq_js_consumer_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/rabbitmq_js_consumer_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.133`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143652` status=`completed` mode=`deterministic` elapsed=`0.133` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: rabbitmq_js_consumer_noise_fixture

- Repo Path: `./tests/fixtures/rabbitmq_js_consumer_noise_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/rabbitmq_js_consumer_noise_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.105`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143652` status=`completed` mode=`deterministic` elapsed=`0.105` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: mixed_rabbitmq_flow_fixture

- Repo Path: `./tests/fixtures/mixed_rabbitmq_flow_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/mixed_rabbitmq_flow_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.114`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143652` status=`completed` mode=`deterministic` elapsed=`0.114` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: mixed_spring_rabbitmq_flow_fixture

- Repo Path: `./tests/fixtures/mixed_spring_rabbitmq_flow_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/mixed_spring_rabbitmq_flow_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.106`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143652` status=`completed` mode=`deterministic` elapsed=`0.106` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: mixed_masstransit_flow_fixture

- Repo Path: `./tests/fixtures/mixed_masstransit_flow_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/mixed_masstransit_flow_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.109`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143652` status=`completed` mode=`deterministic` elapsed=`0.109` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: mixed_laravel_queue_flow_fixture

- Repo Path: `./tests/fixtures/mixed_laravel_queue_flow_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/mixed_laravel_queue_flow_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.108`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143653` status=`completed` mode=`deterministic` elapsed=`0.108` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: mixed_symfony_messenger_flow_fixture

- Repo Path: `./tests/fixtures/mixed_symfony_messenger_flow_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/mixed_symfony_messenger_flow_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.112`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143653` status=`completed` mode=`deterministic` elapsed=`0.112` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: mixed_sidekiq_flow_fixture

- Repo Path: `./tests/fixtures/mixed_sidekiq_flow_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/mixed_sidekiq_flow_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.113`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143653` status=`completed` mode=`deterministic` elapsed=`0.113` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: mixed_activejob_flow_fixture

- Repo Path: `./tests/fixtures/mixed_activejob_flow_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/mixed_activejob_flow_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.108`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143653` status=`completed` mode=`deterministic` elapsed=`0.108` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: mixed_que_flow_fixture

- Repo Path: `./tests/fixtures/mixed_que_flow_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/mixed_que_flow_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.103`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143653` status=`completed` mode=`deterministic` elapsed=`0.103` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: mixed_rabbitmq_queue_fixture

- Repo Path: `./tests/fixtures/mixed_rabbitmq_queue_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/mixed_rabbitmq_queue_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.12`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143653` status=`completed` mode=`deterministic` elapsed=`0.12` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: symfony_messenger_fixture

- Repo Path: `./tests/fixtures/symfony_messenger_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/symfony_messenger_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.106`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143653` status=`completed` mode=`deterministic` elapsed=`0.106` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: symfony_messenger_noise_fixture

- Repo Path: `./tests/fixtures/symfony_messenger_noise_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/symfony_messenger_noise_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.096`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143653` status=`completed` mode=`deterministic` elapsed=`0.096` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: symfony_message_producer_fixture

- Repo Path: `./tests/fixtures/symfony_message_producer_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/symfony_message_producer_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.092`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143653` status=`completed` mode=`deterministic` elapsed=`0.092` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: symfony_message_producer_noise_fixture

- Repo Path: `./tests/fixtures/symfony_message_producer_noise_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/symfony_message_producer_noise_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.104`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143654` status=`completed` mode=`deterministic` elapsed=`0.104` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: resque_worker_fixture

- Repo Path: `./tests/fixtures/resque_worker_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/resque_worker_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.092`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143654` status=`completed` mode=`deterministic` elapsed=`0.092` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: resque_worker_noise_fixture

- Repo Path: `./tests/fixtures/resque_worker_noise_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/resque_worker_noise_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.102`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143654` status=`completed` mode=`deterministic` elapsed=`0.102` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: resque_producer_fixture

- Repo Path: `./tests/fixtures/resque_producer_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/resque_producer_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.104`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143654` status=`completed` mode=`deterministic` elapsed=`0.104` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: resque_producer_noise_fixture

- Repo Path: `./tests/fixtures/resque_producer_noise_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/resque_producer_noise_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.093`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143654` status=`completed` mode=`deterministic` elapsed=`0.093` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: mixed_resque_flow_fixture

- Repo Path: `./tests/fixtures/mixed_resque_flow_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/mixed_resque_flow_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.097`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143654` status=`completed` mode=`deterministic` elapsed=`0.097` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: mixed_celery_flow_fixture

- Repo Path: `./tests/fixtures/mixed_celery_flow_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/mixed_celery_flow_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.105`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143654` status=`completed` mode=`deterministic` elapsed=`0.105` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: mixed_celery_canvas_flow_fixture

- Repo Path: `./tests/fixtures/mixed_celery_canvas_flow_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/mixed_celery_canvas_flow_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.102`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143654` status=`completed` mode=`deterministic` elapsed=`0.102` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: mixed_celery_canvas_flow_noise_fixture

- Repo Path: `./tests/fixtures/mixed_celery_canvas_flow_noise_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/mixed_celery_canvas_flow_noise_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.076`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143654` status=`completed` mode=`deterministic` elapsed=`0.076` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: quarkus_jaxrs_fixture

- Repo Path: `./tests/fixtures/quarkus_jaxrs_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/quarkus_jaxrs_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.106`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143654` status=`completed` mode=`deterministic` elapsed=`0.106` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: quarkus_jaxrs_noise_fixture

- Repo Path: `./tests/fixtures/quarkus_jaxrs_noise_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/quarkus_jaxrs_noise_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.097`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143655` status=`completed` mode=`deterministic` elapsed=`0.097` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: micronaut_controller_fixture

- Repo Path: `./tests/fixtures/micronaut_controller_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/micronaut_controller_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.095`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143655` status=`completed` mode=`deterministic` elapsed=`0.095` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: micronaut_controller_noise_fixture

- Repo Path: `./tests/fixtures/micronaut_controller_noise_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/micronaut_controller_noise_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.096`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143655` status=`completed` mode=`deterministic` elapsed=`0.096` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: ktor_fixture

- Repo Path: `./tests/fixtures/ktor_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/ktor_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.089`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143655` status=`completed` mode=`deterministic` elapsed=`0.089` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`

## Case: ktor_noise_fixture

- Repo Path: `./tests/fixtures/ktor_noise_proof_repo`
- Mode: `deterministic`
- Runs Dir: `/Users/carlosganoza/code-analyzer/evaluation_runs_ci/ktor_noise_fixture`
- Run Count: `1`
- Gate Pass Rate: `1.000`
- Mean Elapsed Sec: `0.09`
- Mean Evidence Coverage: `1.0`
- Mean Semantic Coverage: `1.0`
- Goldens Configured Runs: `1`
- Goldens Pass Rate: `1.0`
- Mean Golden Precision: `1.0`
- Mean Golden Recall: `1.0`
- Mean Golden F1: `1.0`
- Mean Verified Endpoint Rate: `0.0`
- Mean High Confidence Endpoint Rate: `0.0`
- Mean Cross-file Inference Rate: `0.0`
- Quality Gates Pass: `True`
- Subsystem Index Rate: `1.000`
- DOT Export Rate: `1.000`
- LikeC4 Export Rate: `1.000`

### Runs
- `run_20260325_143655` status=`completed` mode=`deterministic` elapsed=`0.09` gate=`True` coverage=`1.000` redactions=`0` goldens_f1=`1.0`

### Quality Gate Checks
- metric=`summary.gate_pass_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.goldens_configured_runs` op=`min` expected=`1` actual=`1` pass=`True`
- metric=`summary.mean_golden_f1` op=`min` expected=`1.0` actual=`1.0` pass=`True`
- metric=`summary.mean_evidence_coverage` op=`min` expected=`0.95` actual=`1.0` pass=`True`
- metric=`summary.subsystem_index_rate` op=`min` expected=`1.0` actual=`1.0` pass=`True`
