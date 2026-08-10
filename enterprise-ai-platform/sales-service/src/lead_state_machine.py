"""
Lead Lifecycle State Machine & Validation
Enforces valid state transitions for the sales lead qualification pipeline.

Lead States: new -> qualified -> contacted -> converted -> churned
  - new: Lead just created, not yet scored
  - qualified: Lead scored >= 70 (BANT qualified)
  - contacted: Sales rep has reached out
  - converted: Lead became a customer
  - churned: Lead disqualified or became inactive

See WORKFLOWS.md Section 3 (Lead & Opportunity Pipeline).
"""

from typing import Set, Dict
from fastapi import HTTPException, status
from .models import Lead


VALID_LEAD_TRANSITIONS: Dict[str, Set[str]] = {
    "new": {"qualified", "disqualified"},
    "qualified": {"contacted", "disqualified"},
    "contacted": {"converted", "churned", "disqualified"},
    "converted": set(),
    "churned": set(),
    "disqualified": {"qualified"},
}

LEAD_STATES = set(VALID_LEAD_TRANSITIONS.keys())


def validate_lead_state_transition(current_status: str, target_status: str) -> bool:
    """Validate if a lead state transition is allowed."""
    if target_status not in LEAD_STATES:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Invalid lead status '{target_status}'. Must be one of: {', '.join(sorted(LEAD_STATES))}",
        )
    allowed = VALID_LEAD_TRANSITIONS.get(current_status, set())
    if target_status not in allowed:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Invalid lead state transition from '{current_status}' to '{target_status}'.",
        )
    return True


def transition_lead_status(lead: Lead, new_status: str, reason: str = "") -> None:
    """Transition a lead to a new status with validation."""
    validate_lead_state_transition(lead.status, new_status)
    lead.status = new_status
