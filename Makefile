.PHONY: test quality drift-check governance-check governance-check-demo governance-check-strict integration-preflight bundle-verification bundle-restore retention-enforcement enterprise-portal release-failure-simulation document agent-document release-readiness smoke

test:
	python3 -m unittest discover -s tests -p 'test_*.py'

quality:
	bash run_quality_check.sh --evaluation-manifest evaluation_manifest.ci.json

drift-check:
	bash run_drift_check.sh --artifact-dir /tmp/code-analyzer-drift --repo ./tests/fixtures/noise_proof_repo --skip-tests

governance-check:
	bash run_governance_check.sh --artifact-dir /tmp/code-analyzer-governance --review-policy review_policy.ci.json --repo ./tests/fixtures/noise_proof_repo

governance-check-demo:
	bash run_governance_check.sh --artifact-dir /tmp/code-analyzer-governance-demo --review-policy review_policy.multi_role.example.json --repo ./tests/fixtures/noise_proof_repo

governance-check-strict:
	bash run_governance_check.sh --artifact-dir /tmp/code-analyzer-governance-strict --review-policy review_policy.strict_promotion.example.json --repo ./tests/fixtures/noise_proof_repo

integration-preflight:
	bash run_integration_preflight.sh --artifact-dir /tmp/code-analyzer-integration-preflight --review-policy review_policy.ci.json --access-policy access_policy.ci.json

bundle-verification:
	bash run_release_readiness.sh --artifact-dir /tmp/code-analyzer-bundle --repo ./tests/fixtures/noise_proof_repo --skip-tests
	bash run_bundle_verification.sh --artifact-dir /tmp/code-analyzer-bundle

bundle-restore:
	bash run_release_readiness.sh --artifact-dir /tmp/code-analyzer-restore --repo ./tests/fixtures/noise_proof_repo --skip-tests
	bash run_bundle_restore.sh --artifact-dir /tmp/code-analyzer-restore

retention-enforcement:
	bash run_retention_enforcement.sh --artifact-dir /tmp/code-analyzer-retention --policy retention_policy.ci.json

enterprise-portal:
	bash run_release_readiness.sh --artifact-dir /tmp/code-analyzer-enterprise-portal --repo ./tests/fixtures/noise_proof_repo

release-failure-simulation:
	bash run_release_failure_simulation.sh --artifact-dir /tmp/code-analyzer-release-failure-simulation --repo ./tests/fixtures/noise_proof_repo

document:
	./run_local.sh

agent-document:
	./run_agent.sh document --repo ./tests/fixtures/noise_proof_repo --mode deterministic

release-readiness:
	bash run_release_readiness.sh --artifact-dir /tmp/code-analyzer-release --repo ./tests/fixtures/noise_proof_repo --skip-tests

smoke:
	bash run_quality_check.sh --skip-tests --skip-evaluation --repo ./tests/fixtures/noise_proof_repo --artifact-dir /tmp/code-analyzer-smoke
