# Architecture review prompt

You are reviewing a production agentic AI system built from an orchestrator, operational data store, model runtime, policy engine, and observability pipeline.

Review this design against the following questions:

1. What is the agent allowed to decide, and what must remain deterministic application policy?
2. Which tools can mutate state? Are they idempotent and authorized?
3. How are tenant/customer scope, secrets, and prompt injection handled?
4. What is persisted, for how long, and how is it redacted?
5. What traces and metrics prove task success, safety, latency, and cost?
6. What happens on model timeout, tool failure, duplicate delivery, stale retrieval, and human rejection?
7. What is the smallest local test that demonstrates each safety invariant?

Return: risks ranked high/medium/low, missing controls, and five concrete acceptance tests.
