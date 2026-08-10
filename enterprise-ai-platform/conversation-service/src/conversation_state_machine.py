"""
Conversation State Machine & Validation
Enforces valid state transitions for customer conversations.

Conversation States:
  active -> paused | resolved | closed
  paused -> active | resolved | closed
  resolved -> closed | active (reopen)
  closed -> (terminal)

See WORKFLOWS.md Section 4 (Conversation Lifecycle).
"""

from typing import Set, Dict
from fastapi import HTTPException, status


VALID_CONVERSATION_TRANSITIONS: Dict[str, Set[str]] = {
    "active": {"paused", "resolved", "closed"},
    "paused": {"active", "resolved", "closed"},
    "resolved": {"closed", "active"},
    "closed": set(),
}

CONVERSATION_STATES = set(VALID_CONVERSATION_TRANSITIONS.keys())


def validate_conversation_state_transition(current_status: str, target_status: str) -> bool:
    """Validate if a conversation state transition is allowed."""
    if target_status not in CONVERSATION_STATES:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Invalid conversation status '{target_status}'. Must be one of: {', '.join(sorted(CONVERSATION_STATES))}",
        )
    allowed = VALID_CONVERSATION_TRANSITIONS.get(current_status, set())
    if target_status not in allowed:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Invalid conversation state transition from '{current_status}' to '{target_status}'.",
        )
    return True
