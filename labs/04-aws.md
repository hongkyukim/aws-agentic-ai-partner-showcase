# Lab 04 — AWS deployment and operations

**Goal:** map the local contract to a production AWS architecture.

## Architecture exercise

Choose and justify services for:

- model access and inference;
- agent runtime and deployment;
- secrets and identity;
- durable state and queues;
- logs, traces, metrics, and alerts;
- network boundaries and data residency;
- CI/CD, rollback, and human approval.

A valid answer names the service, the IAM principal, the data it sees, the timeout, the retry policy, and the estimated cost driver. Keep the answer specific to the AWS account and region being used.

## Optional extension

Implement a thin adapter around the local `AgentOrchestrator` rather than rewriting the policy logic. First run the evaluator locally; then run a single synthetic case in the approved AWS environment. Capture the deployment manifest and remove temporary resources after the lab.

## Operational checklist

- least-privilege IAM;
- budget alert and teardown command;
- no real customer data;
- request/response redaction;
- correlation ids across runtime and data stores;
- timeout and circuit-breaker behavior;
- human approval for irreversible actions;
- rollback tested with a known-good version.
