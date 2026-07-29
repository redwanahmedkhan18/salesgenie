"""
Ticket State Machine & AI Handoff Evaluator
Enforces state machine transition rules and AI confidence threshold escalations.
"""

from typing import Set, Tuple
from fastapi import HTTPException, status
from .models import TicketStatus, TicketPriority, Ticket


VALID_TRANSITIONS: dict[TicketStatus, Set[TicketStatus]] = {
    TicketStatus.NEW: {TicketStatus.OPEN, TicketStatus.IN_PROGRESS, TicketStatus.ESCALATED},
    TicketStatus.OPEN: {TicketStatus.IN_PROGRESS, TicketStatus.PENDING_CUSTOMER, TicketStatus.ESCALATED, TicketStatus.RESOLVED},
    TicketStatus.IN_PROGRESS: {TicketStatus.PENDING_CUSTOMER, TicketStatus.ESCALATED, TicketStatus.RESOLVED},
    TicketStatus.PENDING_CUSTOMER: {TicketStatus.IN_PROGRESS, TicketStatus.RESOLVED, TicketStatus.CLOSED},
    TicketStatus.ESCALATED: {TicketStatus.IN_PROGRESS, TicketStatus.RESOLVED},
    TicketStatus.RESOLVED: {TicketStatus.CLOSED, TicketStatus.OPEN},
    TicketStatus.CLOSED: {TicketStatus.OPEN},
}

# AI Handoff Confidence Threshold (AI confidence < 0.75 triggers auto-escalation to human agent queue)
AI_HANDOFF_CONFIDENCE_THRESHOLD = 0.75


def validate_state_transition(current_status: TicketStatus, target_status: TicketStatus) -> bool:
    """Validates if state transition is allowed in the ticket lifecycle state machine."""
    allowed = VALID_TRANSITIONS.get(current_status, set())
    if target_status not in allowed:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Invalid ticket state transition from '{current_status.value}' to '{target_status.value}'",
        )
    return True


def evaluate_ai_confidence_handoff(ticket: Ticket, confidence_score: float) -> Tuple[bool, str]:
    """
    Evaluates AI confidence score for a ticket response.
    Returns (should_escalate, explanation_reason).
    """
    ticket.ai_confidence_score = confidence_score
    if confidence_score < AI_HANDOFF_CONFIDENCE_THRESHOLD:
        ticket.is_escalated = True
        ticket.status = TicketStatus.ESCALATED
        ticket.priority = TicketPriority.HIGH
        return True, f"AI confidence ({confidence_score:.2f}) dropped below threshold ({AI_HANDOFF_CONFIDENCE_THRESHOLD}). Escalated to human support queue."
    
    return False, "AI response within safe confidence bounds."
