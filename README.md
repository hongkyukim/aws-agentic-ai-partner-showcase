# AWS Agentic AI Partner Showcase Extended

A hands-on companion repository for a production-minded agentic AI workshop featuring the development perspectives of **AWS**, **MongoDB**, and **Mastra**.

The default path is deliberately local and credential-free. Attendees build, test, trace, and review a customer-support agent before mapping the same seams to managed services.

## Workshop outcome

By the end, you will have:

- a deterministic agent workflow with explicit tool and policy boundaries;
- synthetic tickets and golden evaluation cases;
- append-only JSONL traces suitable for inspection or ingestion;
- a human-approval gate for risky actions;
- a concrete design map for orchestration, persistence/retrieval, deployment, and observability.

## Quickstart

Requires Python 3.11+.

```bash
python3 scripts/generate_sample_data.py
python3 scripts/run_demo.py
python3 scripts/evaluate_agents.py
python3 -m pytest -q
```

Or use the Makefile:

```bash
make demo
make evaluate
make test
```

Generated artifacts are ignored by Git:

- `data/generated/tickets.jsonl` — deterministic input;
- `data/generated/decisions.jsonl` — agent decisions;
- `data/generated/trace.jsonl` — lifecycle and decision events;
- `reports/demo_run.md` — human-readable run report.

## Teaching flow

### 90-minute version

1. **Context and architecture (10 min)** — identify where an agent ends and policy begins.
2. **Local implementation (20 min)** — run the demo and inspect `src/partner_agent_stack/stack.py`.
3. **MongoDB design exercise (15 min)** — model tickets, customer context, traces, and retrieval metadata; see `labs/02-mongodb.md`.
4. **Mastra orchestration exercise (15 min)** — translate the deterministic orchestrator into an agent/workflow/tool boundary; see `labs/03-mastra.md`.
5. **AWS production mapping (15 min)** — choose model hosting, runtime, identity, deployment, and observability seams; see `labs/04-aws.md`.
6. **Evaluation and Q&A (15 min)** — change a policy, add a golden case, and prove the behavior with `make evaluate`.

### Half-day version

Add a second pass where teams implement one extension: retrieval grounding, a new approval rule, a trace exporter, or an AWS deployment diagram. Use `prompts/` for architecture review and booth discussions.

## Architecture

```text
Ticket JSONL
    │
    ▼
Orchestrator ── classify ──► policy engine ──► decision / approval
    │                              │
    └──────────── TraceSink ◄──────┘
                    │
                    ▼
          JSONL traces + eval report
```

The local code keeps the interfaces intentionally small:

| Local seam | Production discussion |
|---|---|
| `AgentOrchestrator` | Mastra agent/workflow composition and tool execution |
| `Ticket` / `load_tickets` | MongoDB document model, indexes, vector or semantic retrieval |
| `PolicyEngine` | application authorization, approval workflow, least privilege |
| `TraceSink` | AWS and partner observability/tracing pipeline |
| `scripts/evaluate_agents.py` | regression, safety, and task-success evaluation |

## Partner and platform map

This repo is a teaching scaffold, not an official AWS, MongoDB, or Mastra sample. Use the official documentation and account-specific guidance for the cloud path.

| Perspective | Workshop connection | Optional extension |
|---|---|---|
| AWS | production runtime, model access, IAM, deployment, monitoring | replace local model/tool seams with the AWS services approved for your account; document region, cost, and IAM assumptions |
| MongoDB | operational ticket/customer records, retrieval context, trace persistence | persist `Ticket` and `Decision` documents; add indexes and an Atlas Vector Search design for grounded context |
| Mastra | agent, workflow, tool, and evaluation composition | port `AgentOrchestrator` into a TypeScript Mastra application while preserving the policy gate |

**Speaker context:** Abhijit Chakraborty (MongoDB), Sam Bhagwat (Mastra), and Sathisan Vannadil (AWS) are reflected as the perspectives in the event brief supplied for this workshop. Verify event logistics and current product names before presenting externally.

## Labs

- [01 — Local production baseline](labs/01-local-baseline.md)
- [02 — MongoDB persistence and retrieval](labs/02-mongodb.md)
- [03 — Mastra orchestration](labs/03-mastra.md)
- [04 — AWS deployment and operations](labs/04-aws.md)
- [05 — Evaluation, traces, and safety](labs/05-evaluation.md)

## Prompt cards

- [Architecture review](prompts/architecture-review.md)
- [Partner booth questions](prompts/partner-booth-questions.md)
- [Evaluation and red-team review](prompts/evaluation-review.md)

## Design rules

1. **The model proposes; policy authorizes.** Never let free-form model output directly perform a sensitive action.
2. **Inspect before generating.** In the MongoDB lab, define document shape, indexes, and retrieval filters before writing queries.
3. **Trace every meaningful transition.** Correlate input, classification, tool call, policy result, approval, and final response.
4. **Keep the local path deterministic.** Cloud credentials are optional, and evaluation must remain runnable offline.
5. **Name production assumptions.** Record model, region, data residency, retention, timeout, cost, and rollback decisions.

## Safety and cost

This workshop uses synthetic data only. Do not place credentials, customer data, or production identifiers in the repository. The optional cloud path should be run with least-privilege credentials, explicit budgets, and an approval step before provisioning resources.

## Further reading

The links below are starting points for the live workshop; product APIs and service names change, so confirm them immediately before the event:

- [AWS documentation](https://docs.aws.amazon.com/)
- [Amazon Bedrock](https://aws.amazon.com/bedrock/)
- [MongoDB AI resources](https://www.mongodb.com/products/platform/atlas-vector-search)
- [Mastra documentation](https://mastra.ai/docs)
- [Mastra GitHub](https://github.com/mastra-ai/mastra)
