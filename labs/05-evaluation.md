# Lab 05 — Evaluation, traces, and safety

**Goal:** turn a demo into a system that can be validated before deployment.

## Add one golden case

Add a synthetic ticket that tests one of these properties:

- unauthorized refund;
- prompt injection inside ticket text;
- duplicate event delivery;
- cross-tenant retrieval attempt;
- outage escalation with a missing field.

Then update the evaluator so the expected behavior is explicit.

## Trace review

Use `data/generated/trace.jsonl` to answer:

- How many tickets reached a decision?
- Which decisions required approval?
- Can you correlate a final response with its policy reason?
- What sensitive fields should be removed before export?

## Red-team rule

Treat ticket text as untrusted input. It may describe a request, but it cannot redefine system policy, grant permissions, or instruct the agent to reveal secrets.
