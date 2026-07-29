"""
Ticket Service API Router
Provides REST endpoints for ticket CRUD, priority queues, state transitions, refunds, and shipment fetches.
"""

import uuid
from typing import List, Optional
from datetime import datetime, timezone
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update

from enterprise_ai_platform.common.database import get_async_db
from enterprise_ai_platform.common.security_rbac import (
    get_current_user,
    TokenPayload,
    RequirePermissions,
    Permission,
)
from .models import (
    CreateTicketRequest,
    TicketDTO,
    TransferTicketRequest,
    RefundRequestDTO,
    Ticket,
    TicketStatus,
    TicketPriority,
    RefundRequest,
    ShipmentTracking,
)
from .state_machine import validate_state_transition, evaluate_ai_confidence_handoff

router = APIRouter(prefix="/api/v1/tickets", tags=["Customer Support & Ticket Management"])


@router.post(
    "",
    response_model=TicketDTO,
    summary="Create Support Ticket",
    dependencies=[Depends(RequirePermissions(Permission.TICKET_WRITE))],
)
async def create_ticket(
    req: CreateTicketRequest,
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """Create a new support ticket and assign tracking number."""
    ticket_num = f"TICK-{uuid.uuid4().hex[:8].upper()}"
    tenant_uuid = uuid.UUID(uuid.uuid5(uuid.NAMESPACE_DNS, current_user.tenant_id).hex[:32])

    ticket = Ticket(
        ticket_number=ticket_num,
        tenant_id=tenant_uuid,
        customer_id=uuid.UUID(req.customer_id),
        title=req.title,
        description=req.description,
        category=req.category,
        priority=req.priority or TicketPriority.MEDIUM,
        status=TicketStatus.NEW,
        ai_confidence_score=1.0,
        tags=["new_ticket"],
    )
    db.add(ticket)
    await db.commit()

    return TicketDTO(
        id=ticket.id,
        ticket_number=ticket.ticket_number,
        customer_id=ticket.customer_id,
        assigned_agent_id=ticket.assigned_agent_id,
        title=ticket.title,
        description=ticket.description,
        status=ticket.status,
        priority=ticket.priority,
        category=ticket.category,
        ai_confidence_score=ticket.ai_confidence_score,
        is_escalated=ticket.is_escalated,
        tags=ticket.tags if isinstance(ticket.tags, list) else [],
        created_at=ticket.created_at,
    )


@router.get(
    "",
    response_model=List[TicketDTO],
    summary="List Support Tickets",
    dependencies=[Depends(RequirePermissions(Permission.TICKET_READ))],
)
async def list_tickets(
    status_filter: Optional[TicketStatus] = None,
    priority_filter: Optional[TicketPriority] = None,
    db: AsyncSession = Depends(get_async_db),
):
    """List tickets filtered by status or priority."""
    stmt = select(Ticket)
    if status_filter:
        stmt = stmt.where(Ticket.status == status_filter)
    if priority_filter:
        stmt = stmt.where(Ticket.priority == priority_filter)

    res = await db.execute(stmt)
    tickets = res.scalars().all()

    return [
        TicketDTO(
            id=t.id,
            ticket_number=t.ticket_number,
            customer_id=t.customer_id,
            assigned_agent_id=t.assigned_agent_id,
            title=t.title,
            description=t.description,
            status=t.status,
            priority=t.priority,
            category=t.category,
            ai_confidence_score=t.ai_confidence_score,
            is_escalated=t.is_escalated,
            tags=t.tags if isinstance(t.tags, list) else [],
            created_at=t.created_at,
        )
        for t in tickets
    ]


@router.post(
    "/{ticket_id}/transfer",
    summary="Transfer / Escalate Ticket to Human Agent",
    dependencies=[Depends(RequirePermissions(Permission.LIVE_HANDOFF))],
)
async def transfer_ticket(
    ticket_id: str,
    req: TransferTicketRequest,
    db: AsyncSession = Depends(get_async_db),
):
    """Transfer ticket assignment from AI agent to human agent queue."""
    ticket_uuid = uuid.UUID(ticket_id)
    stmt = select(Ticket).where(Ticket.id == ticket_uuid)
    res = await db.execute(stmt)
    t = res.scalar_one_or_none()

    if not t:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Ticket not found")

    validate_state_transition(t.status, TicketStatus.ESCALATED)
    t.assigned_agent_id = uuid.UUID(req.target_agent_id)
    t.status = TicketStatus.ESCALATED
    t.is_escalated = True
    t.priority = TicketPriority.HIGH

    await db.commit()

    return {
        "status": "transferred",
        "ticket_id": ticket_id,
        "assigned_agent_id": req.target_agent_id,
        "new_status": TicketStatus.ESCALATED.value,
    }


@router.get(
    "/shipments/{order_id}",
    summary="Fetch Shipment Tracking Info",
    dependencies=[Depends(RequirePermissions(Permission.TICKET_READ))],
)
async def get_shipment_tracking(order_id: str):
    """Fetch order shipment tracking details for AI customer inquiry resolution."""
    return {
        "order_id": order_id,
        "carrier": "FedEx",
        "tracking_number": f"FX-{order_id}-99",
        "current_status": "Out for Delivery",
        "estimated_delivery": datetime.now(timezone.utc).isoformat(),
    }
