# Lab 01 — Local production baseline

**Goal:** understand the complete request-to-decision path without cloud credentials.

## Steps

1. Run `python3 scripts/generate_sample_data.py`.
2. Open `data/generated/tickets.jsonl` and identify the risky standard-account refund.
3. Run `python3 scripts/run_demo.py`.
4. Read `reports/demo_run.md` and inspect `data/generated/trace.jsonl`.
5. Run `python3 scripts/evaluate_agents.py`.
6. Change one policy or add one ticket, then update the expected result in the evaluator.

## Discussion

- Which parts are deterministic application code versus model behavior?
- What should be retried, and what should never be retried automatically?
- Where would authentication, authorization, rate limits, and idempotency live?
- What event would an operator need to reconstruct a bad decision?
