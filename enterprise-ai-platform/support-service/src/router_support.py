"""
Support Service API Router
Endpoints for support tickets, ticket notes, assignments, and live chat handoff.
"""

import uuid
from datetime import datetime, timezone, timedelta
from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func, and_, update
from sqlalchemy.orm import selectinload

from enterprise_ai_platform.common.database import get_async_db
from enterprise_ai_platform.common.security_rbac import (
    get_current_user,
    TokenPayload,
    RequirePermissions,
    Permission,
)
from .models import (
    Ticket,
    TicketNote,
    TicketAssignment,
    LiveHandoff,
    TicketDTO,
    CreateTicketRequest,
    UpdateTicketRequest,
    AssignTicketRequest,
    TicketNoteDTO,
    CreateNoteRequest,
    LiveHandoffDTO,
    CreateHandoffRequest,
    TicketAnalyticsDTO,
)

router = APIRouter(prefix="/api/v1/tickets", tags=["Support Tickets & Live Handoff"])


def _get_tenant_uuid(current_user: TokenPayload) -> uuid.UUID:
    """Extract tenant UUID from current user token."""
    return uuid.UUID(uuid.uuid5(uuid.NAMESPACE_DNS, current_user.tenant_id).hex[:32])


def _ticket_to_dto(t: Ticket, tenant_uuid: uuid.UUID) -> TicketDTO:
    """Convert Ticket model to DTO."""
    return TicketDTO(
        id=t.id,
        customer_id=t.customer_id,
        conversation_id=t.conversation_id,
        title=t.title,
        description=t.description,
        status=t.status,
        priority=t.priority,
        category=t.category,
        source=t.source,
        assigned_to=t.assigned_to,
        assigned_at=t.assigned_at,
        resolved_at=t.resolved_at,
        closed_at=t.closed_at,
        resolution_notes=t.resolution_notes,
        satisfaction_score=t.satisfaction_score,
        satisfaction_feedback=t.satisfaction_feedback,
        is_escalated=t.is_escalated,
        escalation_reason=t.escalation_reason,
        tenant_id=tenant_uuid,
        created_at=t.created_at,
        updated_at=t.updated_at,
    )


# -------------------------------------------------------------------
# Ticket CRUD
# -------------------------------------------------------------------

@router.post("/", response_model=TicketDTO, status_code=status.HTTP_201_CREATED,
             summary="Create Support Ticket")
async def create_ticket(
    req: CreateTicketRequest,
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """Create a new support ticket."""
    tenant_uuid = _get_tenant_uuid(current_user)

    ticket = Ticket(
        tenant_id=tenant_uuid,
        customer_id=req.customer_id,
        conversation_id=req.conversation_id,
        title=req.title,
        description=req.description,
        priority=req.priority,
        category=req.category,
        source=req.source,
        metadata_json=req.metadata_json,
    )
    db.add(ticket)
    await db.commit()
    await db.refresh(ticket)

    return _ticket_to_dto(ticket, tenant_uuid)


@router.get("/", response_model=List[TicketDTO], summary="List Support Tickets")
async def list_tickets(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    category: Optional[str] = Query(None, description="Filter by category"),
    assigned_to: Optional[uuid.UUID] = Query(None, description="Filter by assigned agent"),
    customer_id: Optional[uuid.UUID] = Query(None, description="Filter by customer"),
    is_escalated: Optional[bool] = Query(None, description="Filter by escalation"),
    search: Optional[str] = Query(None, description="Search by title or description"),
    limit: int = Query(50, ge=1, le=200),
    offset: int = Query(0, ge=0),
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """List support tickets with filtering and search."""
    tenant_uuid = _get_tenant_uuid(current_user)
    stmt = select(Ticket).where(Ticket.tenant_id == tenant_uuid)

    if status:
        stmt = stmt.where(Ticket.status == status)
    if priority:
        stmt = stmt.where(Ticket.priority == priority)
    if category:
        stmt = stmt.where(Ticket.category == category)
    if assigned_to:
        stmt = stmt.where(Ticket.assigned_to == assigned_to)
    if customer_id:
        stmt = stmt.where(Ticket.customer_id == customer_id)
    if is_escalated is not None:
        stmt = stmt.where(Ticket.is_escalated == is_escalated)
    if search:
        search_term = f"%{search}%"
        stmt = stmt.where(
            (Ticket.title.ilike(search_term)) |
            (Ticket.description.ilike(search_term))
        )

    stmt = stmt.order_by(Ticket.created_at.desc()).limit(limit).offset(offset)
    res = await db.execute(stmt)
    tickets = res.scalars().all()

    return [_ticket_to_dto(t, tenant_uuid) for t in tickets]


@router.get("/{ticket_id}", response_model=TicketDTO, summary="Get Ticket Details")
async def get_ticket(
    ticket_id: uuid.UUID,
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """Get detailed ticket information."""
    tenant_uuid = _get_tenant_uuid(current_user)

    stmt = select(Ticket).where(Ticket.id == ticket_id, Ticket.tenant_id == tenant_uuid)
    res = await db.execute(stmt)
    ticket = res.scalar_one_or_none()

    if not ticket:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Ticket {ticket_id} not found",
        )

    return _ticket_to_dto(ticket, tenant_uuid)


@router.patch("/{ticket_id}", response_model=TicketDTO, summary="Update Ticket")
async def update_ticket(
    ticket_id: uuid.UUID,
    req: UpdateTicketRequest,
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """Update ticket attributes."""
    tenant_uuid = _get_tenant_uuid(current_user)

    stmt = select(Ticket).where(Ticket.id == ticket_id, Ticket.tenant_id == tenant_uuid)
    res = await db.execute(stmt)
    ticket = res.scalar_one_or_none()

    if not ticket:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Ticket {ticket_id} not found",
        )

    if req.title is not None:
        ticket.title = req.title
    if req.description is not None:
        ticket.description = req.description
    if req.status is not None:
        ticket.status = req.status
        if req.status == "resolved":
            ticket.resolved_at = datetime.now(timezone.utc)
        elif req.status == "closed":
            ticket.closed_at = datetime.now(timezone.utc)
    if req.priority is not None:
        ticket.priority = req.priority
    if req.category is not None:
        ticket.category = req.category
    if req.assigned_to is not None:
        ticket.assigned_to = req.assigned_to
        ticket.assigned_at = datetime.now(timezone.utc)
    if req.resolution_notes is not None:
        ticket.resolution_notes = req.resolution_notes
    if req.satisfaction_score is not None:
        ticket.satisfaction_score = req.satisfaction_score
    if req.satisfaction_feedback is not None:
        ticket.satisfaction_feedback = req.satisfaction_feedback
    if req.is_escalated is not None:
        ticket.is_escalated = req.is_escalated
    if req.escalation_reason is not None:
        ticket.escalation_reason = req.escalation_reason

    await db.commit()
    await db.refresh(ticket)

    return _ticket_to_dto(ticket, tenant_uuid)


@router.delete("/{ticket_id}", status_code=status.HTTP_204_NO_CONTENT, summary="Delete Ticket")
async def delete_ticket(
    ticket_id: uuid.UUID,
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """Soft delete a support ticket."""
    tenant_uuid = _get_tenant_uuid(current_user)

    stmt = select(Ticket).where(Ticket.id == ticket_id, Ticket.tenant_id == tenant_uuid)
    res = await db.execute(stmt)
    ticket = res.scalar_one_or_none()

    if not ticket:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Ticket {ticket_id} not found",
        )

    ticket.status = "closed"
    ticket.closed_at = datetime.now(timezone.utc)
    await db.commit()
    return None


# -------------------------------------------------------------------
# Ticket Assignment
# -------------------------------------------------------------------

@router.post("/{ticket_id}/assign", response_model=TicketDTO, summary="Assign Ticket to Agent")
async def assign_ticket(
    ticket_id: uuid.UUID,
    req: AssignTicketRequest,
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """Assign a ticket to a support agent."""
    tenant_uuid = _get_tenant_uuid(current_user)

    stmt = select(Ticket).where(Ticket.id == ticket_id, Ticket.tenant_id == tenant_uuid)
    res = await db.execute(stmt)
    ticket = res.scalar_one_or_none()

    if not ticket:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Ticket {ticket_id} not found",
        )

    # Deactivate previous assignments
    await db.execute(
        update(TicketAssignment)
        .where(TicketAssignment.ticket_id == ticket_id, TicketAssignment.is_active == True)
        .values(is_active=False, unassigned_at=datetime.now(timezone.utc))
    )

    # Create new assignment
    assignment = TicketAssignment(
        ticket_id=ticket_id,
        agent_id=req.agent_id,
        assigned_by=req.assigned_by,
    )
    db.add(assignment)

    ticket.assigned_to = req.agent_id
    ticket.assigned_at = datetime.now(timezone.utc)

    await db.commit()
    await db.refresh(ticket)

    return _ticket_to_dto(ticket, tenant_uuid)


# -------------------------------------------------------------------
# Ticket Notes
# -------------------------------------------------------------------

@router.post("/notes", response_model=TicketNoteDTO, status_code=status.HTTP_201_CREATED,
             summary="Add Ticket Note")
async def add_note(
    req: CreateNoteRequest,
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """Add a note to a support ticket."""
    tenant_uuid = _get_tenant_uuid(current_user)

    stmt = select(Ticket).where(Ticket.id == req.ticket_id, Ticket.tenant_id == tenant_uuid)
    res = await db.execute(stmt)
    ticket = res.scalar_one_or_none()

    if not ticket:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Ticket {req.ticket_id} not found",
        )

    note = TicketNote(
        ticket_id=req.ticket_id,
        author_id=uuid.UUID(current_user.sub),
        content=req.content,
        is_internal=req.is_internal,
    )
    db.add(note)
    await db.commit()
    await db.refresh(note)

    return TicketNoteDTO(
        id=note.id, ticket_id=note.ticket_id, author_id=note.author_id,
        author_type=note.author_type, content=note.content,
        is_internal=note.is_internal, created_at=note.created_at, updated_at=note.updated_at,
    )


@router.get("/{ticket_id}/notes", response_model=List[TicketNoteDTO], summary="Get Ticket Notes")
async def get_notes(
    ticket_id: uuid.UUID,
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """Get all notes for a support ticket."""
    tenant_uuid = _get_tenant_uuid(current_user)

    stmt = select(Ticket).where(Ticket.id == ticket_id, Ticket.tenant_id == tenant_uuid)
    res = await db.execute(stmt)
    ticket = res.scalar_one_or_none()

    if not ticket:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Ticket {ticket_id} not found",
        )

    note_stmt = select(TicketNote).where(TicketNote.ticket_id == ticket_id)
    note_res = await db.execute(note_stmt)
    notes = note_res.scalars().all()

    return [
        TicketNoteDTO(
            id=n.id, ticket_id=n.ticket_id, author_id=n.author_id,
            author_type=n.author_type, content=n.content,
            is_internal=n.is_internal, created_at=n.created_at, updated_at=n.updated_at,
        )
        for n in notes
    ]


# -------------------------------------------------------------------
# Live Handoff
# -------------------------------------------------------------------

@router.post("/handoffs", response_model=LiveHandoffDTO, status_code=status.HTTP_201_CREATED,
             summary="Request Live Chat Handoff")
async def request_handoff(
    req: CreateHandoffRequest,
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """Request a live chat handoff from AI agent to human agent."""
    tenant_uuid = _get_tenant_uuid(current_user)

    timeout = datetime.now(timezone.utc) + timedelta(minutes=5)

    handoff = LiveHandoff(
        tenant_id=tenant_uuid,
        conversation_id=req.conversation_id,
        customer_id=req.customer_id,
        requested_by=req.requested_by,
        reason=req.reason,
        timeout_at=timeout,
    )
    db.add(handoff)
    await db.commit()
    await db.refresh(handoff)

    return LiveHandoffDTO(
        id=handoff.id, ticket_id=handoff.ticket_id, conversation_id=handoff.conversation_id,
        customer_id=handoff.customer_id, requested_by=handoff.requested_by,
        reason=handoff.reason, assigned_agent_id=handoff.assigned_agent_id,
        accepted_at=handoff.accepted_at, declined_at=handoff.declined_at,
        status=handoff.status, timeout_at=handoff.timeout_at,
        tenant_id=tenant_uuid, created_at=handoff.created_at,
    )


@router.post("/handoffs/{handoff_id}/accept", response_model=LiveHandoffDTO,
             summary="Accept Live Handoff")
async def accept_handoff(
    handoff_id: uuid.UUID,
    agent_id: uuid.UUID = Query(..., description="Agent ID accepting the handoff"),
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """Accept a pending live chat handoff."""
    tenant_uuid = _get_tenant_uuid(current_user)

    stmt = select(LiveHandoff).where(LiveHandoff.id == handoff_id, LiveHandoff.tenant_id == tenant_uuid)
    res = await db.execute(stmt)
    handoff = res.scalar_one_or_none()

    if not handoff:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Handoff {handoff_id} not found",
        )

    if handoff.status != "pending":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Handoff is already {handoff.status}",
        )

    if datetime.now(timezone.utc) > handoff.timeout_at:
        handoff.status = "timed_out"
        await db.commit()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Handoff has timed out",
        )

    handoff.assigned_agent_id = agent_id
    handoff.accepted_at = datetime.now(timezone.utc)
    handoff.status = "accepted"

    await db.commit()
    await db.refresh(handoff)

    return LiveHandoffDTO(
        id=handoff.id, ticket_id=handoff.ticket_id, conversation_id=handoff.conversation_id,
        customer_id=handoff.customer_id, requested_by=handoff.requested_by,
        reason=handoff.reason, assigned_agent_id=handoff.assigned_agent_id,
        accepted_at=handoff.accepted_at, declined_at=handoff.declined_at,
        status=handoff.status, timeout_at=handoff.timeout_at,
        tenant_id=tenant_uuid, created_at=handoff.created_at,
    )


# -------------------------------------------------------------------
# Analytics
# -------------------------------------------------------------------

@router.get("/analytics/overview", response_model=TicketAnalyticsDTO,
            summary="Get Support Analytics Overview")
async def get_analytics(
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """Get support ticket analytics overview."""
    tenant_uuid = _get_tenant_uuid(current_user)

    # Total tickets
    total_stmt = select(func.count()).select_from(Ticket).where(Ticket.tenant_id == tenant_uuid)
    total_res = await db.execute(total_stmt)
    total_tickets = total_res.scalar() or 0

    # By status
    status_stmt = (
        select(Ticket.status, func.count())
        .where(Ticket.tenant_id == tenant_uuid)
        .group_by(Ticket.status)
    )
    status_res = await db.execute(status_stmt)
    status_counts = {row[0]: row[1] for row in status_res.fetchall()}

    # By priority
    priority_stmt = (
        select(Ticket.priority, func.count())
        .where(Ticket.tenant_id == tenant_uuid)
        .group_by(Ticket.priority)
    )
    priority_res = await db.execute(priority_stmt)
    priority_counts = {row[0]: row[1] for row in priority_res.fetchall()}

    # By category
    category_stmt = (
        select(Ticket.category, func.count())
        .where(Ticket.tenant_id == tenant_uuid)
        .group_by(Ticket.category)
    )
    category_res = await db.execute(category_stmt)
    category_counts = {row[0]: row[1] for row in category_res.fetchall()}

    # Average satisfaction
    sat_stmt = select(func.avg(Ticket.satisfaction_score)).where(
        Ticket.tenant_id == tenant_uuid, Ticket.satisfaction_score.isnot(None)
    )
    sat_res = await db.execute(sat_stmt)
    avg_satisfaction = float(sat_res.scalar() or 0)

    # Escalation rate
    escalated_stmt = (
        select(func.count())
        .select_from(Ticket)
        .where(Ticket.tenant_id == tenant_uuid, Ticket.is_escalated == True)
    )
    escalated_res = await db.execute(escalated_stmt)
    escalated_count = escalated_res.scalar() or 0
    escalation_rate = (escalated_count / total_tickets * 100) if total_tickets > 0 else 0

    # Average resolution time
    resolved_stmt = (
        select(func.avg(
            (Ticket.resolved_at - Ticket.created_at).total_seconds() / 3600
        ))
        .where(
            Ticket.tenant_id == tenant_uuid,
            Ticket.resolved_at.isnot(None)
        )
    )
    resolved_res = await db.execute(resolved_stmt)
    avg_resolution = float(resolved_res.scalar() or 0)

    return TicketAnalyticsDTO(
        total_tickets=total_tickets,
        open_tickets=status_counts.get("open", 0),
        in_progress_tickets=status_counts.get("in_progress", 0),
        resolved_tickets=status_counts.get("resolved", 0),
        closed_tickets=status_counts.get("closed", 0),
        avg_resolution_time_hours=round(avg_resolution, 2),
        avg_satisfaction_score=round(avg_satisfaction, 2),
        tickets_by_priority=priority_counts,
        tickets_by_category=category_counts,
        escalation_rate=round(escalation_rate, 2),
    )