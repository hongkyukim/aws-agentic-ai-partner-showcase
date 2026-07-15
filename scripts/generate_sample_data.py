#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data" / "generated"
OUT.mkdir(parents=True, exist_ok=True)

TICKETS = [
    {"id": "T-1001", "customer": "Acme Labs", "category": "billing", "priority": "high", "text": "Please refund the duplicate charge from yesterday.", "account_tier": "standard"},
    {"id": "T-1002", "customer": "Northstar", "category": "access", "priority": "medium", "text": "Our operator cannot login and needs a password reset.", "account_tier": "enterprise"},
    {"id": "T-1003", "customer": "Acme Labs", "category": "incident", "priority": "critical", "text": "The production API is down for all users.", "account_tier": "standard"},
    {"id": "T-1004", "customer": "Pioneer", "category": "question", "priority": "low", "text": "What is the retention period for exported reports?", "account_tier": "standard"},
    {"id": "T-1005", "customer": "VectorWorks", "category": "billing", "priority": "high", "text": "Our enterprise plan was charged twice; please refund one invoice.", "account_tier": "enterprise"},
]

with (OUT / "tickets.jsonl").open("w", encoding="utf-8") as handle:
    for ticket in TICKETS:
        handle.write(json.dumps(ticket, sort_keys=True) + "\n")
print(f"generated {len(TICKETS)} tickets -> {OUT / 'tickets.jsonl'}")
