from pathlib import Path

from partner_agent_stack import AgentOrchestrator, PolicyEngine, TraceSink
from partner_agent_stack.stack import Ticket


def test_standard_refund_requires_approval(tmp_path: Path):
    decision = AgentOrchestrator(PolicyEngine(), TraceSink(tmp_path / "trace.jsonl")).handle(
        Ticket("T", "A", "billing", "high", "refund my charge", "standard")
    )
    assert decision.action == "request_approval"
    assert decision.requires_approval is True


def test_enterprise_refund_is_allowed(tmp_path: Path):
    decision = AgentOrchestrator(PolicyEngine(), TraceSink(tmp_path / "trace.jsonl")).handle(
        Ticket("T", "A", "billing", "high", "refund my charge", "enterprise")
    )
    assert decision.action == "refund"
    assert decision.requires_approval is False
