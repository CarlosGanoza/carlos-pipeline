# Pipeline Presentation Guide

## 1. What this project is
This project is a privacy-first, enterprise-style code analysis pipeline for legacy repositories. It scans a repository locally, extracts grounded facts from the code, generates documentation and architecture artifacts, validates evidence quality, and saves the whole run as an auditable artifact folder.

This is the right way to frame it:
- It is not just a report generator.
- It is a documentation pipeline with privacy controls, grounding, updateability, architecture outputs, and operational workflow support.
- It is still a research/prototype system, not a fully deployed enterprise product with auth, RBAC, monitoring, and compliance operations.

## 2. What we are actually using right now
Current defaults in this repo:
- `LLM_BACKEND=ollama`
- `OLLAMA_MODEL=qwen2.5-coder:7b`
- `STRICT_LOCAL_ONLY=1`
- `DOC_DEFAULT_MODE=deterministic`

What that means in plain English:
- The normal local backend is `Ollama`, and the runtime also supports loopback-only `openai_compatible` servers.
- The current default local model is `qwen2.5-coder:7b`.
- The wrapper `run_agent.sh` enforces local-only execution by default.
- When a command actually needs live model access and `LLM_BACKEND=ollama`, the wrapper checks whether the `ollama` CLI is installed, whether the Python `ollama` package is installed, whether the local Ollama server is reachable, and whether the requested model is already pulled.
- When `LLM_BACKEND=openai_compatible`, the wrapper keeps the endpoint loopback-only and lets the Python health check validate the local server.
- For class/demo safety, documentation runs default to `deterministic` mode unless you explicitly request `agent` mode.

Important honesty note:
- Some older submission artifacts in the repo mention `qwen2.5:7b`, and some later experiments tested `qwen3-coder:30b`.
- If someone asks, say: "Deterministic mode is the primary recommended workflow, and the current lightweight local-model default in this repo is `qwen2.5-coder:7b`."

## 3. The simplest demo choice
If you want the safest live demo, use:

```bash
./run_agent.sh document --repo ../code-analyzer-proof-repos/transit_enterprise_legacy_repo --mode deterministic --runs-dir ../code-analyzer-proof-repos/transit_enterprise_legacy_repo/code_analyzer_reports
```

Why:
- fastest
- predictable
- still shows the full pipeline
- does not depend on live model quality
- still proves privacy, grounding, architecture export, subsystem docs, diffs, and traceability

If you want to also show the local LLM path:

```bash
./run_agent.sh document --repo ../code-analyzer-proof-repos/transit_enterprise_legacy_repo --mode agent --max-iterations 1 --runs-dir ../code-analyzer-proof-repos/transit_enterprise_legacy_repo/code_analyzer_reports
```

## 4. Demo-day checklist from turning on the computer
Use this literally on the day of the presentation.

1. Turn on the computer and log in.
2. Open a terminal window.
3. Change into the project directory:

```bash
cd /path/to/code-analyzer
```

4. If you use a virtual environment, activate it now. If you do not use one, skip this step.

Example:

```bash
source .venv/bin/activate
```

5. Confirm Python is available:

```bash
python3 -V
```

6. Confirm you are in the correct repo root:

```bash
pwd
ls
```

7. If you plan to show `agent` mode, confirm Ollama is installed:

```bash
ollama --version
```

8. If you plan to show `agent` mode, confirm the local Ollama server is running:

```bash
ollama list
```

If that fails:
- open the Ollama app, or
- run `ollama serve`

9. If you plan to show `agent` mode, confirm the model exists locally:

```bash
ollama list | grep qwen2.5-coder:7b
```

If the model is missing:

```bash
ollama pull qwen2.5-coder:7b
```

10. Optional but recommended before class: refresh the presentation assets and run a clean deterministic smoke check:

```bash
./presentation_check.sh
```

11. If you want to prove the local LLM path too, do one quiet smoke check before class:

```bash
./run_agent.sh document --repo ./tests/fixtures/noise_proof_repo --mode agent --max-iterations 1 --runs-dir ./runs_smoke_llm
```

12. Right before presenting, keep these windows ready:
- terminal
- `run_agent.sh`
- `agent.py`
- `main.py`
- latest run folder in Finder or editor
- `presentation_downloads/code_analyzer_pipeline_presentation.pdf`

## 5. One-time setup if the machine is fresh
Only do this on a new machine.

1. Install Python 3.
2. Install Ollama.
3. Pull the local model:

```bash
ollama pull qwen2.5-coder:7b
```

4. Install Python dependencies if needed:

```bash
python3 -m pip install -r requirements.txt
```

If `requirements.txt` does not cover everything for your environment, the wrapper can still install the Python `ollama` package automatically when needed.

5. Optional presentation asset packages:

```bash
python3 -m pip install python-docx reportlab
```

## 6. Exact live demo script
This is the cleanest order.

### Step A. Show the safety-first wrapper
Open `run_agent.sh` and say:
- "This wrapper enforces local-only execution."
- "It sets `STRICT_LOCAL_ONLY=1`."
- "It verifies backend configuration before the documentation run starts."
- "When a command needs live model access, it checks the CLI, installs the Python package if missing, checks the local server, and pulls the model if needed."

### Step B. Run the safe documentation demo

```bash
./run_agent.sh document --repo ../code-analyzer-proof-repos/transit_enterprise_legacy_repo --mode deterministic --runs-dir ../code-analyzer-proof-repos/transit_enterprise_legacy_repo/code_analyzer_reports
```

What to say while it runs:
- "The wrapper hands off to `agent.py`, which creates a timestamped run directory."
- "Then the pipeline scans the repo, extracts deterministic facts, generates documentation, runs grounding checks, and writes artifacts."

### Step C. Open the newest run folder
Open the newest folder under `../code-analyzer-proof-repos/transit_enterprise_legacy_repo/code_analyzer_reports/`.

Open these files in this order:
1. `state.json`
2. `run_summary.md`
3. `model_safe_fact_index.json`
4. `prompt_fact_context.json`
5. `report.md`
6. `traceability.md`
7. `subsystems/README.md`
8. `run_diff.md`
9. `architecture_clean.png`

### Step D. Show one grounded Q and A example

```bash
python3 agent.py ask --question "how many endpoints were detected" --fact-index ../code-analyzer-proof-repos/transit_enterprise_legacy_repo/code_analyzer_reports/<latest>/fact_index.json
```

What to say:
- "This answer is grounded only in the extracted fact index."
- "It is not free-form chatting over the raw repo."

### Step E. If there is time, show evaluation

```bash
python3 main.py --evaluate-manifest evaluation_manifest.example.json
```

What to say:
- "This is how we prove privacy, accuracy, navigability, and updatability claims with repeatable scorecards."
- "For automation, the repo now also includes `evaluation_manifest.ci.json` and `bash run_quality_check.sh --evaluation-manifest evaluation_manifest.ci.json`, which enforces benchmark quality gates in CI."
- "The governance side is automated too with `bash run_governance_check.sh --review-policy review_policy.ci.json --reviewers security_lead,architecture_lead --deployer release_manager`, which performs role-based approve and publish checks with distinct reviewer and deployer identities and verifies the audit artifacts."
- "There is also a scheduled drift layer with `bash run_drift_check.sh --baseline drift_baseline.ci.json`, so the pipeline can flag nightly regressions even when no code is being actively changed."
- "That drift layer now keeps `drift.history.json`, `drift.history.md`, and `drift.history.csv`, so we can show trend lines over repeated nightly runs instead of only one-run snapshots."
- "The final stop button is `bash run_release_readiness.sh --criteria release_readiness.ci.json --reviewers security_lead,architecture_lead --deployer release_manager --exception-policy release_exceptions.ci.json --operator-assignments 'release_signer:signer;release_publisher:publisher;release_notifier:notifier'`, which rolls all of those signals into one ship or no-ship result with explicit waivers instead of hidden criteria edits."
- "Those waiver exceptions are now governed locally too: the same bundle emits `enterprise_waiver_audit.json` and `enterprise_waiver_audit.md`, and active waivers only count when they are ticketed, justified, approved by a configured waiver approver identity, scoped, and time-bounded."
- "That same stop check now emits `enterprise_dashboard.json`, `enterprise_dashboard.md`, and `enterprise_dashboard.html`, so the latest enterprise posture is viewable as a single snapshot instead of piecing together multiple raw artifacts."
- "It also emits `enterprise_portal.json`, `enterprise_portal.md`, and `enterprise_portal.html`, which gives the artifact root a single landing page with links to the latest dashboard, history, badges, and recent release runs."
- "For static publishing, that same portal is also copied to `index.html` and `index.json`, so a Pages deployment opens directly on the enterprise portal without any extra routing."
- "Those badges are now emitted as local `badges/*.svg` files too, so the portal and Pages deployment do not rely on external badge services."
- "And the root now includes `enterprise_asset_manifest.json` and `enterprise_asset_manifest.md`, which give a hash-and-size inventory for the published release artifacts."
- "The portal also now renders local `charts/*.svg` trend graphics for health, approvals, and failures across release-readiness runs, so the Pages site shows movement over time instead of only static tables."
- "There is also an `enterprise_incident_digest.json` and `enterprise_incident_digest.md`, so a blocked release produces a direct machine-readable list of what is failing the ship gate."
- "The bundle also emits `enterprise_retention_plan.json` and `enterprise_retention_plan.md`, so operators can see which release runs should be retained or pruned and why instead of treating cleanup as an ad hoc manual step."
- "That retention policy now supports legal holds and active-incident preservation, so the plan can explicitly protect named runs and blocked sessions instead of pruning them by age alone."
- "The release bundle now also emits `enterprise_notifications.json` plus `enterprise_notification_dispatch.json`, so the same gate output can feed Slack, email, GitHub Issue, or a generic webhook."
- "That notification bundle is now provider-specific instead of generic only: it includes ready payloads for Slack, Teams, GitHub Issues, Jira issues, PagerDuty, email, and a generic webhook."
- "And the dispatch artifact is now a summary, not just a one-channel result, so we can see requested channels, configured channels, per-channel attempts, and delivery outcomes in one place."
- "That provider path now supports direct API-style delivery too through `notification_providers.example.json`, so GitHub Issue and Jira issue channels can be executed, not only rendered as saved payloads."
- "There is now an `enterprise_notification_plan.json` and `enterprise_notification_plan.md`, so the release bundle shows which channels should fire for the current severity and policy instead of leaving routing implicit."
- "And there is now an `enterprise_notification_history.json` and `enterprise_notification_history.md`, so repeated release runs accumulate an auditable alert-delivery trail instead of only exposing the latest dispatch."
- "The release root now also emits `enterprise_incident_register.json` and `enterprise_incident_register.md`, so repeated blocked runs are tracked as new, ongoing, or resolved incidents instead of only showing the latest failure snapshot."
- "And it emits `enterprise_ticket_queue.json` and `enterprise_ticket_queue.md`, so those persistent incidents can be turned into provider-ready ticket candidates and escalation suggestions instead of relying on manual triage."
- "Those same release trends now also render `charts/active_incidents.svg` and `charts/ticket_candidates.svg`, so the enterprise portal shows whether incident pressure and ticket load are trending up or down over time."
- "And it emits `enterprise_attestation.json` and `enterprise_attestation.verify.json`, so the published bundle can carry signed metadata instead of only unsigned hashes."
- "That attestation path is now pluggable instead of fixed: it supports the original HMAC mode plus `openssl_rsa_sha256`, `cosign_blob`, and `aws_kms`, so provenance can move toward real asymmetric or managed-key signing instead of only shared-secret signing."
- "There is also an `enterprise_bundle_verification.json` and `enterprise_bundle_verification.md`, which re-check the published release root, attestation, incident digest, and notification status as one verification report."
- "There is now also a standalone `run_bundle_verification.sh` path that emits `enterprise_bundle_verification.independent.json` and `.md`, so operators can independently re-verify an already-produced release root."
- "The release runner now also emits `enterprise_bundle_export.json` and `enterprise_bundle_export.verify.json`, so the final bundle can be mirrored and archived into a durable external location and then re-verified after export."
- "And it now emits `enterprise_bundle_publish.json` and `enterprise_bundle_publish.verify.json`, so the exported archive or selected metadata files can be uploaded to remote HTTP(S) targets and then checked as a publish step instead of only being copied locally."
- "It now emits `enterprise_bundle_restore.json` and `enterprise_bundle_restore.verify.json` too, so that exported archive can be restored into a clean recovery location and the restored bundle can be re-verified as an actual disaster-recovery proof step."
- "That publish path now also supports provider-aware backends like `aws_s3`, `gcs`, `azure_blob`, `jfrog_artifactory`, `github_release_asset`, and `filesystem_copy`, so the same release bundle can be pushed into real enterprise storage and registry systems instead of only generic URLs."
- "Those per-run publish artifacts are now rolled into `enterprise_publish_history.json` and `enterprise_publish_history.md`, so the portal can show whether remote publish targets are staying reliable across releases instead of only showing the latest upload."
- "The release root now also maintains `enterprise_history.sqlite3` plus `enterprise_history_backend.json` and `.md`, so the release, notification, publish, and incident history is queryable from a durable backend instead of only flat files."
- "Notification delivery now supports retry and dedupe controls like `max_attempts`, `backoff_seconds`, and `dedupe_window_hours`, so enterprise channels can avoid duplicate tickets and survive transient failures."
- "Bundle publishing now has the same retry/backoff model for both HTTP and provider-backed uploads, so a transient object-store or registry hiccup does not immediately fail the release path."
- "The SQLite history backend is now re-synced after export and publish, so the current run's publish counters land in `enterprise_history_backend.json` immediately instead of lagging by one run."
- "Release readiness now has an access-control gate too: `enterprise_access_audit.json` checks operator roles like `signer`, `publisher`, and `notifier`, and it blocks the release if policy files carry inline secrets instead of environment or secret references."
- "And there is now a standalone `run_bundle_restore.sh` operator path, so recovery can be executed and verified independently of the full release pipeline when an operator needs to prove restore viability on demand."
- "And there is now a `run_retention_enforcement.sh` path that turns the retention plan into a real dry-run or apply step, writing `enterprise_retention_enforcement.json` and `.md` so cleanup is auditable too."
- "The access-control side is stronger too: `enterprise_access_audit.json` now checks configured action coverage and separation-of-duty rules over operator assignments, not only a flat list of roles."
- "It also now keeps `release_readiness.history.json`, `release_readiness.history.md`, and `release_readiness.history.csv`, so release stability can be tracked over repeated ship-gate runs instead of only looking at the latest result."
- "And it now emits `release_readiness.delta.json` and `release_readiness.delta.md`, so we can say exactly what improved or regressed compared with the previous release-gate run."
- "And there is now a dedicated failure-simulation workflow that intentionally fails the ship gate, so we can prove the blocked-release path and incident reporting instead of only showing green runs."
- "There is also a manual CI workflow for that same stop check, so release readiness can be run as an auditable action instead of only from a local shell."
- "And if we want a publishable enterprise surface, there is now a separate workflow that deploys that portal bundle to GitHub Pages instead of leaving it only as a workflow artifact."

### Step F. If there is time, show approval/publish workflow

```bash
python3 main.py --approve-run <run_id> --runs-dir outputs/runs --approved-by architecture_lead --approval-policy review_policy.example.json
python3 main.py --publish-run <run_id> --runs-dir outputs/runs --publish-dir outputs/published --approval-policy review_policy.example.json
```

What to say:
- "This moves the system closer to an enterprise workflow by adding explicit review and publish steps."

## 7. What happens internally from start to finish
This is the detailed technical flow.

1. `run_agent.sh` starts first.
2. It enforces `STRICT_LOCAL_ONLY=1`.
3. It sets backend and model defaults.
4. If the selected command needs live model access and `LLM_BACKEND=ollama`, it checks:
   - `ollama` CLI exists
   - Python package `ollama` exists or is installable
   - local Ollama server is reachable
   - requested model is present locally
   If `LLM_BACKEND=openai_compatible`, the wrapper skips the Ollama-specific CLI checks and the Python runtime probes the loopback-only OpenAI-style endpoint instead.
5. The wrapper calls `agent.py`.
6. `agent.py` creates a new run directory such as `runs/run_YYYYMMDD_HHMMSS`.
7. `agent.py` initializes `state.json` so the run is traceable from the first stage.
8. The gather stage scans the repository.
9. It applies path and extension filters.
10. It skips noisy directories and oversized files.
11. It applies built-in secret redaction and optional repo-specific redaction policy rules.
12. `main.py` extracts a deterministic `fact_index.json`.
13. That fact index includes files, languages, dependencies, scripts, endpoints, imports, infrastructure signals, AI signals, SQL facts, and language-specific symbol/call facts.
14. `main.py` also writes a `model_safe_fact_index.json`.
15. It writes `prompt_fact_context.json`, which is a compact, retrieval-oriented prompt payload for grounded synthesis.
16. In `deterministic` mode, the report is written directly from deterministic facts.
17. In `agent` mode, a local model drafts the report from model-safe context.
18. The grounding gate checks line-level evidence tags like `[Evidence: path#Lline]`.
19. The semantic validator checks whether factual claims are actually supported by extracted facts.
20. If model output fails, the pipeline falls back to deterministic output instead of saving untrusted text.
21. The pipeline exports:
   - report
   - traceability artifacts
   - inference audit
   - subsystem docs
   - architecture exports
   - optional run diff artifacts
22. The run summary is written.
23. Final status is recorded in `state.json`.
24. The documentation run exits cleanly.

## 8. What each artifact means
- `state.json`
  The execution timeline and state transitions for the run.
- `run_summary.md`
  The fastest summary of mode, metrics, timings, and gate outcome.
- `fact_index.json`
  The deterministic extracted facts from the repository.
- `model_safe_fact_index.json`
  Sanitized structured facts safe for prompt/caching use.
- `prompt_fact_context.json`
  A smaller grounding payload designed for synthesis.
- `report.md`
  The final documentation report.
- `traceability.json` and `traceability.md`
  Evidence and support audit for factual reporting.
- `inference_audit.json`
  Records about synthesis decisions and fallbacks.
- `subsystems/README.md`
  Navigation entrypoint for subsystem documentation.
- `run_diff.md` and `run_diff.json`
  Run-to-run change tracking.
- `architecture.mmd`
  Mermaid architecture source.
- `architecture.dot`
  Graphviz DOT architecture source.
- `architecture.likec4`
  LikeC4 architecture source.
- `architecture_clean.svg` and `architecture_clean.png`
  Rendered visual diagrams.
- `approval.json`
  Reviewer approval metadata for a completed run.
- `publish_manifest.json`
  Audited released-bundle manifest for published artifacts.

## 9. Enterprise-style operational features you can mention
These are the things that make it more than a one-shot report demo.

### Queue and worker layer
- `python3 main.py --enqueue-job ...`
- `python3 main.py --worker ...`
- `python3 main.py --status --queue-dir outputs/job_queue --all-queues`

What this proves:
- file-backed queue support
- stale-job reclaim
- worker heartbeats
- queue metrics
- named queues
- priority and retry backoff

### Evaluation layer
- `python3 main.py --evaluate-manifest evaluation_manifest.example.json`

What this proves:
- repeatable scoring for privacy, accuracy, navigability, and updatability
- benchmark-ready Markdown and CSV outputs

### Review and publish layer
- `python3 main.py --approve-run ...`
- `python3 main.py --publish-run ...`

What this proves:
- human approval step
- publish gating
- hashed artifact bundles
- auditable release metadata

## 10. Short talk track you can memorize
We built a local, privacy-first code-analysis pipeline for enterprise legacy repositories. The system does not just generate a report. It first extracts deterministic facts from the code, sanitizes what the model sees, generates documentation and architecture artifacts, validates evidence quality with a grounding gate, falls back safely if model output is weak, and saves every run as a traceable artifact set. We also added updateability, evaluation, queue operations, and approval/publish workflow so the project is closer to an enterprise-style documentation pipeline rather than a one-shot summarizer.

## 11. Honest answers to likely questions
### "Are you using an LLM?"
Yes. The default local backend is `Ollama` with `qwen2.5-coder:7b`, and the privacy-hardened build also supports loopback-only `openai_compatible` endpoints for local OpenAI-style servers.

### "Does the model see raw private code?"
The pipeline is designed to keep execution local and to send model-safe structured facts rather than a raw unrestricted source dump. It also supports redaction policy files and strict local endpoint locking.

### "What happens if the model gives a bad answer?"
The report is not trusted automatically. The grounding gate checks evidence formatting and semantic support. If the model output fails, the pipeline falls back to deterministic output.

### "Is this a real enterprise product?"
Not yet. It is an enterprise-style prototype/research pipeline. The core documentation engine, privacy controls, grounding, updateability, evaluation, queue operations, and publish workflow are implemented. Full enterprise production would still need service deployment, auth, RBAC, monitoring, compliance operations, and governance workflow.

### "Why not stop at the earlier version?"
Because an enterprise like BART would not trust a tool just because it produces a nice report. It has to be privacy-preserving, evidence-backed, auditable, updateable, and operationally manageable.

## 12. If you want to show the strongest possible closing
Say this:

"The earlier version showed that large repositories could be summarized. The final version shows that documentation can be generated more responsibly: locally, with evidence, with auditability, with updateability, and with an operational workflow that is closer to what an enterprise would actually trust."

## 13. Shutdown after the demo
After the run completes:
- the analyzer process exits on its own
- artifacts remain in the run folder
- Ollama may still be running in the background if you used `agent` mode

If you want to stop there, just close the terminal. If you want a clean stop, close the Ollama app or stop the related background process on your machine.
