# Lab 02 — MongoDB persistence and retrieval

**Goal:** design the data layer before connecting an agent to operational records.

## Exercise

Design three document families:

- `tickets`: customer request, priority, status, tenant/customer key, timestamps;
- `decisions`: proposed action, policy result, approval state, final response;
- `trace_events`: correlation id, event name, latency, model/tool metadata, redacted payload.

For each family, write down:

1. the access patterns;
2. the required indexes;
3. fields that must be redacted or encrypted;
4. the tenant filter that must be applied to every retrieval;
5. whether semantic retrieval is appropriate or an exact filter is safer.

## Optional implementation

Use the local JSONL files as the contract, then implement a MongoDB adapter that preserves the same `Ticket`, `Decision`, and trace event shapes. Add a retrieval function that requires an explicit `customer` or `tenant` scope. Never let a similarity search bypass authorization filters.

## Review questions

- How do you prevent cross-tenant retrieval?
- What makes a trace queryable during an incident?
- Which data belongs in a vector index, and which belongs in a normal index?
- How will you handle stale or conflicting customer context?
