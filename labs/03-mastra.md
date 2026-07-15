# Lab 03 — Mastra orchestration

**Goal:** translate the local orchestration seam into an agent/workflow implementation without weakening the policy boundary.

## Exercise

Create a TypeScript spike outside the default local path with these conceptual boundaries:

- an agent or workflow receives the ticket;
- a classification step produces a typed intent;
- tools read approved context and prepare actions;
- a policy function converts a proposed action into `allow`, `request_approval`, or `deny`;
- the final response is generated from the policy result;
- each step emits a correlation id and trace event.

Use Mastra's current official documentation for exact APIs and package setup. Do not copy a version-sensitive snippet into this repository without pinning and testing it.

## Acceptance criteria

- a standard-account refund cannot complete without approval;
- tool inputs and outputs have explicit schemas;
- retries do not duplicate a refund;
- traces distinguish model reasoning, tool execution, and policy decisions;
- the local evaluator remains the source of truth for the golden cases.
