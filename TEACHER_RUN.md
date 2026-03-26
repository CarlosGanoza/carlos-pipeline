# Teacher Run Guide

This package contains the `code-analyzer` pipeline so you can run the same local repository analysis workflow on another computer.

## Prerequisites

- Python 3.9+ available as `python3`
- `pip` available for Python package installs
- Ollama installed if you want the default LLM-enhanced mode
- Or a loopback-only OpenAI-compatible local server if you want to use `LLM_BACKEND=openai_compatible`
- Graphviz installed if you want rendered `architecture_clean.png` and `architecture_clean.svg`
  The wrappers also auto-detect a user-space install at `~/.local/bin/dot` or `GRAPHVIZ_DOT`

## Quick Start

From the project root:

```bash
chmod +x run_agent.sh
./run_agent.sh document --repo ./tests/fixtures/noise_proof_repo --mode deterministic
```

That command runs a fully local deterministic analysis on the included sample repo.

## LLM-Enhanced Mode

If a local backend is available, you can run the hybrid pipeline:

```bash
./run_agent.sh document --repo ./tests/fixtures/noise_proof_repo --mode agent
```

Current behavior:

- Deterministic extraction always builds the base report
- The selected local backend only enhances selected narrative sections
- Evidence, traceability, and diagrams remain deterministic
- If an LLM enhancement section fails validation, only that section is rejected

## Standalone Analyzer

The standalone pipeline entrypoint is also available:

```bash
python3 main.py --repo ./tests/fixtures/noise_proof_repo --mode deterministic
```

Hybrid mode with Ollama:

```bash
python3 main.py --repo ./tests/fixtures/noise_proof_repo --mode agent --require-llm
```

Enterprise preset example:

```bash
python3 main.py --repo ./tests/fixtures/noise_proof_repo --mode deterministic --policy-pack enterprise_local_strict
```

Available built-in policy packs:

- `enterprise_local_strict`
- `regulated_internal_docs`
- `runtime_validation_local`
- `runtime_disabled`

Hybrid mode with an OpenAI-compatible local endpoint:

```bash
LLM_BACKEND=openai_compatible OPENAI_BASE_URL=http://127.0.0.1:8000/v1 OPENAI_COMPATIBLE_MODEL=local-model \
python3 main.py --repo ./tests/fixtures/noise_proof_repo --mode agent --require-llm
```

Install optional dependencies:

```bash
python3 -m pip install -r requirements.txt
```

Install local dev and test dependencies:

```bash
python3 -m pip install -r requirements-dev.txt
```

For presentation asset generation:

```bash
python3 -m pip install -r requirements-presentation.txt
```

If Graphviz is installed outside your default `PATH`, set:

```bash
export GRAPHVIZ_DOT=/absolute/path/to/dot
```

Regression checks:

```bash
python3 -m unittest discover -s tests -p 'test_*.py'
```

If `pytest` is installed, `pytest -q` also works.

CI-style quality gate run:

```bash
bash run_quality_check.sh --evaluation-manifest evaluation_manifest.ci.json
```

That command runs shell checks, Python compile checks, unit tests, and the evaluation harness with enforced benchmark quality gates. Outputs are written under `outputs/quality_check/` by default.

CI-style governance run:

```bash
bash run_governance_check.sh --review-policy review_policy.ci.json --reviewers security_lead,architecture_lead --deployer release_manager
```

That command runs a deterministic analysis on the bundled fixture repo, records multi-role reviewer approvals, publishes the run with a distinct deployer identity, and verifies that approval and publish audit artifacts are produced under `outputs/governance_check/`.

Nightly drift run:

```bash
bash run_drift_check.sh --baseline drift_baseline.ci.json --reviewers security_lead,architecture_lead
```

That command reruns the CI quality and governance pipelines, compares the resulting metrics and governance artifacts against the stored drift baseline, and writes `drift.summary.json` plus `drift.summary.md` under `outputs/drift_check/`.
It also regenerates cumulative trend files across prior drift runs in the same artifact root:

- `drift.history.json`
- `drift.history.md`
- `drift.history.csv`

The scheduled GitHub workflow restores and saves that drift artifact root through the Actions cache, so nightly runs accumulate into a rolling history instead of resetting each time.

Release readiness stop check:

```bash
bash run_release_readiness.sh --criteria release_readiness.ci.json --reviewers security_lead,architecture_lead --deployer release_manager --exception-policy release_exceptions.ci.json --operator-assignments 'release_signer:signer;release_publisher:publisher;release_notifier:notifier'
```

That command runs the drift pipeline end to end, evaluates release criteria over the current quality, governance, and drift outputs, checks the rolling drift history thresholds, and writes `release_readiness.json` plus `release_readiness.md` under `outputs/release_readiness/`.
The default CI criteria now also expect role-based distinct approvals, reviewer and deployer identity checks, and a non-zero current drift pass streak. `release_exceptions.ci.json` is the local waiver file for time-bounded exceptions, and the resulting release artifact records both applied waivers and waived failures.
That waiver file now has its own local policy too: active waivers must be ticketed, justified, approved by a configured waiver approver identity, scoped to a concrete target, and time-bounded, and the bundle emits `enterprise_waiver_audit.json` plus `enterprise_waiver_audit.md` so exception quality is audited rather than silently trusted.
It also writes an enterprise dashboard bundle:

- `enterprise_dashboard.json`
- `enterprise_dashboard.md`
- `enterprise_dashboard.html`
- `enterprise_portal.json`
- `enterprise_portal.md`
- `enterprise_portal.html`
- `index.json`
- `index.html`
- `enterprise_asset_manifest.json`
- `enterprise_asset_manifest.md`
- `enterprise_incident_digest.json`
- `enterprise_incident_digest.md`
- `enterprise_incident_register.json`
- `enterprise_incident_register.md`
- `enterprise_ticket_queue.json`
- `enterprise_ticket_queue.md`
- `enterprise_retention_plan.json`
- `enterprise_retention_plan.md`
- `enterprise_waiver_audit.json`
- `enterprise_waiver_audit.md`
- `enterprise_notification_plan.json`
- `enterprise_notification_plan.md`
- `enterprise_notifications.json`
- `enterprise_notifications.md`
- `enterprise_notification_dispatch.json`
- `enterprise_notification_history.json`
- `enterprise_notification_history.md`
- `enterprise_attestation.json`
- `enterprise_attestation.md`
- `enterprise_attestation.verify.json`
- `enterprise_bundle_verification.json`
- `enterprise_bundle_verification.md`
- `enterprise_bundle_verification.independent.json`
- `enterprise_bundle_verification.independent.md`
- `enterprise_bundle_export.json`
- `enterprise_bundle_export.md`
- `enterprise_bundle_export.verify.json`
- `enterprise_bundle_export.verify.md`
- `enterprise_bundle_publish.json`
- `enterprise_bundle_publish.md`
- `enterprise_bundle_publish.verify.json`
- `enterprise_bundle_publish.verify.md`
- `enterprise_bundle_restore.json`
- `enterprise_bundle_restore.md`
- `enterprise_bundle_restore.verify.json`
- `enterprise_bundle_restore.verify.md`
- `enterprise_publish_history.json`
- `enterprise_publish_history.md`
- `enterprise_history_backend.json`
- `enterprise_history_backend.md`
- `enterprise_history.sqlite3`
- `enterprise_retention_enforcement.json`
- `enterprise_retention_enforcement.md`
- `charts/*.svg`
- `badges/*.json`
- `badges/*.svg`

And a rolling release-readiness history bundle:

- `release_readiness.history.json`
- `release_readiness.history.md`
- `release_readiness.history.csv`
- `release_readiness.delta.json`
- `release_readiness.delta.md`

There is also a manual GitHub Actions workflow at `.github/workflows/release_readiness.yml` that runs the same stop check in CI and uploads the resulting artifacts.
If you want a publishable static status site, `.github/workflows/enterprise_portal.yml` runs the same release pipeline and deploys the resulting portal bundle to GitHub Pages.
If you want to prove the blocked-release path, `.github/workflows/release_failure_simulation.yml` runs an intentionally failing criteria set and uploads the resulting failure-simulation, incident, and verification artifacts.
The notification bundle now includes provider-ready payloads for `generic_webhook`, `slack`, `teams`, `github_issue`, `jira_issue`, `pagerduty`, and `email`, the notification plan records which channels should fire for the current release state, and the dispatch/history artifacts record requested channels plus delivery outcomes over time.
The enterprise release bundle also now includes a persistent incident register and ticket queue, so repeated blocked runs can be tracked as new, ongoing, or resolved incidents instead of only producing one-run incident digests.
The release-history charts now also include `charts/active_incidents.svg` and `charts/ticket_candidates.svg`, so the portal shows whether operational incident pressure is improving or getting worse across release runs.
If you want actual provider delivery instead of only saved payloads, the release runner now accepts `INCIDENT_PROVIDER_CONFIGS_JSON` or `INCIDENT_PROVIDER_CONFIGS_JSON_FILE`; a working schema example is in `notification_providers.example.json`, including direct `github_issue` and `jira_issue` API delivery settings.
The release runner also now accepts `--export-policy export_policy.ci.json` and emits export artifacts plus mirror/archive verification, so the release bundle can be copied out to a durable mirror directory and a `.tar.gz` archive instead of only living in the working artifact root.
On top of that, it now accepts `--publish-policy publish_policy.ci.json` and can upload the exported archive or selected metadata files to remote HTTP(S) targets or provider-aware backends such as `aws_s3`, `gcs`, `azure_blob`, `jfrog_artifactory`, `github_release_asset`, and `filesystem_copy`; an example target schema is in `publish_policy.example.json`. Publish targets now also support retry/backoff controls like `max_attempts`, `backoff_seconds`, `retry_status_codes`, and `retry_reasons`.
Those per-run publish artifacts are now also accumulated into `enterprise_publish_history.json` and `enterprise_publish_history.md`, so repeated release runs show target-delivery reliability over time instead of only the latest upload attempt.
For stronger provenance, the release runner also supports pluggable signing backends through `ARTIFACT_SIGNING_CONFIG_JSON` or `ARTIFACT_SIGNING_CONFIG_JSON_FILE`, plus helper env vars like `ARTIFACT_SIGNING_BACKEND`, `ARTIFACT_SIGNING_PRIVATE_KEY_PATH`, and `ARTIFACT_SIGNING_PUBLIC_KEY_PATH`. The current backends are `hmac-sha256`, `openssl_rsa_sha256`, `cosign_blob`, and `aws_kms`; an example config is in `artifact_signing.example.json`.
If you want to re-verify a produced release root without rerunning the full pipeline, `bash run_bundle_verification.sh --artifact-dir <release_root>` writes `enterprise_bundle_verification.independent.json` and `enterprise_bundle_verification.independent.md`.
If you want to prove archive recovery directly, `bash run_bundle_restore.sh --artifact-dir <release_root> --policy recovery_policy.ci.json` writes `enterprise_bundle_restore.json`, `enterprise_bundle_restore.md`, `enterprise_bundle_restore.verify.json`, and `enterprise_bundle_restore.verify.md`, and it re-verifies the restored bundle in its recovered location.
If you want cleanup to be executable instead of only planned, `bash run_retention_enforcement.sh --artifact-dir <release_root> --policy retention_policy.ci.json` writes a dry-run enforcement report, and adding `--apply` actually prunes the sessions selected by the retention plan.
The release runner now also accepts `--recovery-policy recovery_policy.ci.json`, so export, publish, restore, and restored-bundle verification all happen in one governed release-readiness run instead of recovery being a manual follow-up.
The release pipeline now also syncs a durable SQLite summary backend at `enterprise_history.sqlite3`, with human-readable rollup artifacts in `enterprise_history_backend.json` and `enterprise_history_backend.md`.
Notification providers now support retry and dedupe controls such as `max_attempts`, `backoff_seconds`, `retry_status_codes`, and `dedupe_window_hours`; the updated schema is in `notification_providers.example.json`.
For provenance, `artifact_signing.example.json` now shows `openssl_rsa_sha256`, `cosign_blob`, and `aws_kms` profile shapes. The `cosign` and local Moto-backed `aws_kms` paths have both been live-validated in this environment.
The release runner now re-syncs `enterprise_history.sqlite3` after export/publish as well, so `enterprise_history_backend.json` captures the current run's publish state immediately instead of waiting for the next run.
There is now a dedicated `access_policy.ci.json` gate for enterprise operator roles and secret-boundary enforcement. `bash run_release_readiness.sh --access-policy access_policy.ci.json --review-policy review_policy.ci.json --deployer release_manager --exception-policy release_exceptions.ci.json --operator-assignments 'release_signer:signer;release_publisher:publisher;release_notifier:notifier'` writes `enterprise_access_audit.json` and `enterprise_access_audit.md`, and release readiness now fails if required operator roles are missing, if configured action coverage is incomplete, if separation-of-duty rules are violated, if reviewer or deployer identities fail policy, or if policy files embed inline secrets instead of placeholders such as `${ENV_VAR}` or `env:SECRET_NAME`.
The retention policy now also supports `legal_hold_session_ids`, `legal_hold_globs`, and `keep_sessions_with_active_incidents`, so the retention plan and enforcement reports preserve explicitly held sessions and runs linked to active incidents instead of pruning them accidentally.

## Main Files

- `main.py`: standalone analyzer pipeline
- `agent.py`: agent workflow and local grounded Q&A utilities
- `run_agent.sh`: easiest wrapper for local execution
- `submission/README.md`: full project and submission documentation

## Outputs

Generated outputs are written under either:

- `outputs/` for root-output runs
- Desktop report bundles under `~/Desktop/code_analyzer_reports/<repo_name>/` for default packaged runs
