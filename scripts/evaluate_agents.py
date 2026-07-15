#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "generated"
rows = [json.loads(line) for line in (DATA / "decisions.jsonl").read_text(encoding="utf-8").splitlines()]
expected = {"T-1001": "request_approval", "T-1002": "send_reset_link", "T-1003": "escalate_incident", "T-1004": "draft_reply", "T-1005": "refund"}
actual = {row["ticket_id"]: row["action"] for row in rows}
assert actual == expected, f"decision mismatch: {actual}"
assert all(row["requires_approval"] for row in rows if row["ticket_id"] == "T-1001")
assert not any(row["requires_approval"] for row in rows if row["ticket_id"] == "T-1005")
trace_events = [json.loads(line)["event"] for line in (DATA / "trace.jsonl").read_text(encoding="utf-8").splitlines()]
assert trace_events.count("agent.start") == len(rows)
assert trace_events.count("agent.decision") == len(rows)
print(f"evaluation passed: {len(rows)} golden cases, {len(trace_events)} trace events")
