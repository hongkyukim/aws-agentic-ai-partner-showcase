from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class Ticket:
    id: str
    customer: str
    category: str
    priority: str
    text: str
    account_tier: str


@dataclass(frozen=True)
class Decision:
    ticket_id: str
    intent: str
    action: str
    response: str
    requires_approval: bool
    reason: str


class TraceSink:
    """Append-only JSONL trace sink; replace with an observability adapter later."""

    def __init__(self, path: Path):
        self.path = path
        self.path.parent.mkdir(parents=True, exist_ok=True)

    def record(self, event: str, **payload: Any) -> None:
        with self.path.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps({"event": event, **payload}, sort_keys=True) + "\n")


class PolicyEngine:
    """Explicit action guardrail: the model may recommend, never authorize."""

    def review(self, ticket: Ticket, proposed_action: str) -> tuple[str, bool, str]:
        if proposed_action == "refund" and ticket.account_tier != "enterprise":
            return "request_approval", True, "refunds for non-enterprise accounts require human approval"
        if proposed_action == "disable_account":
            return "request_approval", True, "account changes require human approval"
        return proposed_action, False, "action is within the local policy"


class AgentOrchestrator:
    """Deterministic orchestration that makes production concerns visible."""

    def __init__(self, policy: PolicyEngine, traces: TraceSink):
        self.policy = policy
        self.traces = traces

    def handle(self, ticket: Ticket) -> Decision:
        self.traces.record("agent.start", ticket_id=ticket.id)
        intent, proposed = self._classify(ticket)
        self.traces.record("agent.classified", ticket_id=ticket.id, intent=intent)
        action, needs_approval, reason = self.policy.review(ticket, proposed)
        response = self._response(ticket, action)
        decision = Decision(ticket.id, intent, action, response, needs_approval, reason)
        self.traces.record("agent.decision", **asdict(decision))
        return decision

    @staticmethod
    def _classify(ticket: Ticket) -> tuple[str, str]:
        text = ticket.text.lower()
        if "refund" in text or "charge" in text:
            return "billing_refund", "refund"
        if "password" in text or "login" in text:
            return "account_access", "send_reset_link"
        if "outage" in text or "down" in text:
            return "service_outage", "escalate_incident"
        return "general_support", "draft_reply"

    @staticmethod
    def _response(ticket: Ticket, action: str) -> str:
        if action == "request_approval":
            return f"Ticket {ticket.id} is queued for human approval before {ticket.category} action."
        if action == "refund":
            return f"A refund workflow was opened for {ticket.customer}."
        if action == "send_reset_link":
            return "A password-reset link was sent through the verified account channel."
        if action == "escalate_incident":
            return "The incident was escalated to the on-call team with priority context."
        return "A support response draft is ready for review."


def load_tickets(path: Path) -> list[Ticket]:
    rows = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line]
    return [Ticket(**row) for row in rows]
