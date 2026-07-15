#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from partner_agent_stack import AgentOrchestrator, PolicyEngine, TraceSink  # noqa: E402
from partner_agent_stack.stack import load_tickets  # noqa: E402

DATA = ROOT / "data" / "generated"
REPORTS = ROOT / "reports"
TRACE_PATH = DATA / "trace.jsonl"
REPORTS.mkdir(exist_ok=True)
TRACE_PATH.unlink(missing_ok=True)

agent = AgentOrchestrator(PolicyEngine(), TraceSink(TRACE_PATH))
decisions = [agent.handle(ticket) for ticket in load_tickets(DATA / "tickets.jsonl")]
with (DATA / "decisions.jsonl").open("w", encoding="utf-8") as handle:
    for decision in decisions:
        handle.write(json.dumps(decision.__dict__, sort_keys=True) + "\n")

lines = ["# Local Demo Run", "", "| Ticket | Intent | Action | Approval |", "|---|---|---|---|"]
for d in decisions:
    lines.append(f"| {d.ticket_id} | {d.intent} | {d.action} | {'yes' if d.requires_approval else 'no'} |")
lines += ["", f"Trace events: `{TRACE_PATH.relative_to(ROOT)}`", "", "This is the seam where AWS observability, MongoDB persistence, and Mastra orchestration can be introduced."]
(REPORTS / "demo_run.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
print(f"processed {len(decisions)} tickets")
print(f"wrote {REPORTS / 'demo_run.md'}")
