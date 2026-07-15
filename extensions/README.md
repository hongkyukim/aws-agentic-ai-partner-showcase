# Workshop extensions

The default repository is Python + standard library so the room has a reliable baseline. Add vendor SDKs only in optional subprojects or extras, pin versions, and keep credentials out of Git.

Suggested extension directories:

- `extensions/mongodb/` — MongoDB adapter, indexes, retrieval contract;
- `extensions/mastra/` — TypeScript Mastra workflow spike;
- `extensions/aws/` — deployment and observability adapter for the approved account.

Each extension should consume the local domain contract and pass the same golden cases.
