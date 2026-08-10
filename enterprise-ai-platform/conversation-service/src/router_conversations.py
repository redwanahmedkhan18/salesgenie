"""
Conversation Service API Router
Endpoints for conversation management, messaging, and analytics.
"""

import uuid
import time
from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func, desc, asc, or_
from datetime import datetime, timedelta, timezone

from enterprise_ai_platform.common.database import get_async_db
from enterprise_ai_platform.common.security_rbac import (
    get_current_user,
    TokenPayload,
)
from .models import (
    Conversation,
    Message,
    ConversationDTO,
    MessageDTO,
    ConversationCreateRequest,
    ConversationCreateResponse,
    MessageCreateRequest,
    MessageCreateResponse,
    ConversationSearchResponse,
    MessageSearchResponse,
    ConversationStatsDTO,
    ConversationOverviewDTO,
    ConversationUpdateRequest,
    ConversationHandoffRequest,
    MessageStatus,
)
from .conversation_state_machine import validate_conversation_state_transition

router = APIRouter(prefix="/api/v1/conversations", tags=["Conversations & Messaging"])


def _get_tenant_uuid(current_user: TokenPayload) -> uuid.UUID:
    """Extract tenant UUID from current user token."""
    return uuid.UUID(uuid.uuid5(uuid.NAMESPACE_DNS, current_user.tenant_id).hex[:32])


def _conversation_to_dto(conv: Conversation) -> ConversationDTO:
    """Convert Conversation model to ConversationDTO."""
    return ConversationDTO(
        id=str(conv.id),
        title=conv.title,
        status=conv.status,
        channel=conv.channel,
        customer_id=conv.customer_id,
        agent_id=conv.agent_id,
        assigned_to=conv.assigned_to,
        initiated_by=conv.initiated_by,
        source_url=conv.source_url,
        metadata=conv.metadata_json,
        tags=conv.tags,
        message_count=conv.message_count,
        last_message_at=conv.last_message_at,
        last_message_preview=conv.last_message_preview,
        resolved_at=conv.resolved_at,
        satisfaction_score=conv.satisfaction_score,
        satisfaction_feedback=conv.satisfaction_feedback,
        is_handoff=conv.is_handoff,
        handoff_reason=conv.handoff_reason,
        handoff_at=conv.handoff_at,
        handoff_to=conv.handoff_to,
        duration_seconds=conv.duration_seconds,
        tenant_id=str(conv.tenant_id),
        created_at=conv.created_at,
        updated_at=conv.updated_at,
    )


def _message_to_dto(msg: Message) -> MessageDTO:
    """Convert Message model to MessageDTO."""
    return MessageDTO(
        id=str(msg.id),
        conversation_id=str(msg.conversation_id),
        role=msg.role,
        content=msg.content,
        status=msg.status,
        sender_id=msg.sender_id,
        token_count=msg.token_count,
        metadata=msg.metadata_json,
        is_edited=msg.is_edited,
        edited_at=msg.edited_at,
        read_by=msg.read_by,
        tenant_id=str(msg.tenant_id),
        created_at=msg.created_at,
        updated_at=msg.updated_at,
    )


# -------------------------------------------------------------------
# Conversation Management
# -------------------------------------------------------------------

@router.post("/", response_model=ConversationCreateResponse, status_code=status.HTTP_201_CREATED,
             summary="Create Conversation")
async def create_conversation(
    req: ConversationCreateRequest,
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """Create a new conversation."""
    tenant_uuid = _get_tenant_uuid(current_user)

    conv = Conversation(
        tenant_id=tenant_uuid,
        title=req.title,
        channel=req.channel,
        customer_id=req.customer_id,
        agent_id=req.agent_id,
        initiated_by=req.initiated_by,
        source_url=req.source_url,
        metadata_json=req.metadata,
        tags=req.tags,
    )
    db.add(conv)
    await db.commit()
    await db.refresh(conv)

    return ConversationCreateResponse(
        conversation_id=str(conv.id),
        status=conv.status,
        created_at=conv.created_at,
        title=conv.title,
    )


@router.get("/{conversation_id}", response_model=ConversationDTO, summary="Get Conversation")
async def get_conversation(
    conversation_id: str,
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """Get a specific conversation by ID."""
    tenant_uuid = _get_tenant_uuid(current_user)

    stmt = select(Conversation).where(
        Conversation.tenant_id == tenant_uuid,
        Conversation.id == conversation_id,
    )
    res = await db.execute(stmt)
    conv = res.scalar_one_or_none()

    if not conv:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Conversation {conversation_id} not found",
        )

    return _conversation_to_dto(conv)


@router.patch("/{conversation_id}", response_model=ConversationDTO, summary="Update Conversation")
async def update_conversation(
    conversation_id: str,
    req: ConversationUpdateRequest,
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """Update conversation metadata."""
    tenant_uuid = _get_tenant_uuid(current_user)

    stmt = select(Conversation).where(
        Conversation.tenant_id == tenant_uuid,
        Conversation.id == conversation_id,
    )
    res = await db.execute(stmt)
    conv = res.scalar_one_or_none()

    if not conv:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Conversation {conversation_id} not found",
        )

    update_data = req.model_dump(exclude_unset=True)
    if "status" in update_data and update_data["status"] is not None:
        validate_conversation_state_transition(conv.status, update_data["status"])
    for key, value in update_data.items():
        if key == "metadata":
            conv.metadata_json = value
        else:
            setattr(conv, key, value)

    conv.updated_at = datetime.now(timezone.utc)
    await db.commit()

    return _conversation_to_dto(conv)


@router.delete("/{conversation_id}", status_code=status.HTTP_204_NO_CONTENT, summary="Delete Conversation")
async def delete_conversation(
    conversation_id: str,
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """Delete a conversation and all its messages."""
    tenant_uuid = _get_tenant_uuid(current_user)

    stmt = select(Conversation).where(
        Conversation.tenant_id == tenant_uuid,
        Conversation.id == conversation_id,
    )
    res = await db.execute(stmt)
    conv = res.scalar_one_or_none()

    if not conv:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Conversation {conversation_id} not found",
        )

    # Delete all messages first
    msg_stmt = select(Message).where(Message.conversation_id == conversation_id)
    msg_res = await db.execute(msg_stmt)
    messages = msg_res.scalars().all()
    for msg in messages:
        await db.delete(msg)

    await db.delete(conv)
    await db.commit()
    return None


# -------------------------------------------------------------------
# Conversation Search
# -------------------------------------------------------------------

@router.get("/", response_model=ConversationSearchResponse, summary="Search Conversations")
async def search_conversations(
    query: Optional[str] = Query(None, description="Search query"),
    statuses: Optional[str] = Query(None, description="Comma-separated statuses"),
    channels: Optional[str] = Query(None, description="Comma-separated channels"),
    customer_ids: Optional[str] = Query(None, description="Comma-separated customer IDs"),
    agent_ids: Optional[str] = Query(None, description="Comma-separated agent IDs"),
    assigned_to: Optional[str] = Query(None, description="Assigned agent ID"),
    is_handoff: Optional[bool] = Query(None, description="Filter handoff conversations"),
    tags: Optional[str] = Query(None, description="Comma-separated tags"),
    date_from: Optional[datetime] = Query(None, description="Start date"),
    date_to: Optional[datetime] = Query(None, description="End date"),
    size: int = Query(50, ge=1, le=200),
    from_: int = Query(0, ge=0, alias="from"),
    sort_by: str = Query("last_message_at", description="Sort field"),
    sort_order: str = Query("desc", description="Sort order"),
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """Search conversations with filters."""
    tenant_uuid = _get_tenant_uuid(current_user)
    start_time = time.time()

    stmt = select(Conversation).where(Conversation.tenant_id == tenant_uuid)

    # Text search
    if query:
        search_term = f"%{query}%"
        stmt = stmt.where(
            or_(
                Conversation.title.ilike(search_term),
                Conversation.last_message_preview.ilike(search_term),
            )
        )

    # Filter by statuses
    if statuses:
        status_list = statuses.split(",")
        stmt = stmt.where(Conversation.status.in_(status_list))

    # Filter by channels
    if channels:
        channel_list = channels.split(",")
        stmt = stmt.where(Conversation.channel.in_(channel_list))

    # Filter by customer IDs
    if customer_ids:
        cust_list = customer_ids.split(",")
        stmt = stmt.where(Conversation.customer_id.in_(cust_list))

    # Filter by agent IDs
    if agent_ids:
        agent_list = agent_ids.split(",")
        stmt = stmt.where(Conversation.agent_id.in_(agent_list))

    # Filter by assigned agent
    if assigned_to:
        stmt = stmt.where(Conversation.assigned_to == assigned_to)

    # Filter by handoff
    if is_handoff is not None:
        stmt = stmt.where(Conversation.is_handoff == is_handoff)

    # Filter by tags
    if tags:
        tag_list = tags.split(",")
        for tag in tag_list:
            stmt = stmt.where(Conversation.tags.contains([tag]))

    # Date range filters
    if date_from:
        stmt = stmt.where(Conversation.created_at >= date_from)
    if date_to:
        stmt = stmt.where(Conversation.created_at <= date_to)

    # Sorting
    sort_col = getattr(Conversation, sort_by, Conversation.last_message_at)
    if sort_order.lower() == "desc":
        stmt = stmt.order_by(desc(sort_col))
    else:
        stmt = stmt.order_by(asc(sort_col))

    # Pagination
    stmt = stmt.offset(from_).limit(size)

    res = await db.execute(stmt)
    conversations = res.scalars().all()

    took_ms = int((time.time() - start_time) * 1000)

    return ConversationSearchResponse(
        total_hits=len(conversations),
        hits=[_conversation_to_dto(c) for c in conversations],
        took_ms=took_ms,
    )


# -------------------------------------------------------------------
# Messaging
# -------------------------------------------------------------------

@router.post("/{conversation_id}/messages", response_model=MessageCreateResponse,
             status_code=status.HTTP_201_CREATED, summary="Send Message")
async def send_message(
    conversation_id: str,
    req: MessageCreateRequest,
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """Send a message in a conversation."""
    tenant_uuid = _get_tenant_uuid(current_user)

    # Verify conversation exists
    conv_stmt = select(Conversation).where(
        Conversation.tenant_id == tenant_uuid,
        Conversation.id == conversation_id,
    )
    conv_res = await db.execute(conv_stmt)
    conv = conv_res.scalar_one_or_none()

    if not conv:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Conversation {conversation_id} not found",
        )

    msg = Message(
        tenant_id=tenant_uuid,
        conversation_id=conversation_id,
        role=req.role,
        content=req.content,
        status=MessageStatus.SENT,
        sender_id=req.sender_id,
        metadata_json=req.metadata,
    )
    db.add(msg)

    # Update conversation metadata
    conv.message_count += 1
    conv.last_message_at = datetime.now(datetime.now().astimezone().tzinfo)
    conv.last_message_preview = req.content[:200]

    await db.commit()
    await db.refresh(msg)

    return MessageCreateResponse(
        message_id=str(msg.id),
        status=msg.status,
        created_at=msg.created_at,
    )


@router.get("/{conversation_id}/messages", response_model=MessageSearchResponse, summary="Get Messages")
async def get_messages(
    conversation_id: str,
    size: int = Query(100, ge=1, le=500),
    from_: int = Query(0, ge=0, alias="from"),
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """Get messages for a conversation."""
    tenant_uuid = _get_tenant_uuid(current_user)
    start_time = time.time()

    # Verify conversation exists
    conv_stmt = select(Conversation).where(
        Conversation.tenant_id == tenant_uuid,
        Conversation.id == conversation_id,
    )
    conv_res = await db.execute(conv_stmt)
    conv = conv_res.scalar_one_or_none()

    if not conv:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Conversation {conversation_id} not found",
        )

    stmt = (
        select(Message)
        .where(Message.conversation_id == conversation_id)
        .order_by(Message.created_at)
        .offset(from_)
        .limit(size)
    )
    res = await db.execute(stmt)
    messages = res.scalars().all()

    took_ms = int((time.time() - start_time) * 1000)

    return MessageSearchResponse(
        total_hits=len(messages),
        hits=[_message_to_dto(m) for m in messages],
        took_ms=took_ms,
    )


# -------------------------------------------------------------------
# Handoff
# -------------------------------------------------------------------

@router.post("/{conversation_id}/handoff", response_model=ConversationDTO, summary="Handoff Conversation")
async def handoff_conversation(
    conversation_id: str,
    req: ConversationHandoffRequest,
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """Hand off a conversation to a human agent."""
    tenant_uuid = _get_tenant_uuid(current_user)

    stmt = select(Conversation).where(
        Conversation.tenant_id == tenant_uuid,
        Conversation.id == conversation_id,
    )
    res = await db.execute(stmt)
    conv = res.scalar_one_or_none()

    if not conv:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Conversation {conversation_id} not found",
        )

    conv.is_handoff = True
    conv.handoff_reason = req.reason
    conv.handoff_to = req.handoff_to
    conv.handoff_at = datetime.now(datetime.now().astimezone().tzinfo)
    conv.assigned_to = req.handoff_to
    conv.updated_at = datetime.now(datetime.now().astimezone().tzinfo)

    await db.commit()

    return _conversation_to_dto(conv)


# -------------------------------------------------------------------
# Analytics & Overview
# -------------------------------------------------------------------

@router.get("/overview", response_model=ConversationOverviewDTO, summary="Get Conversation Overview")
async def get_conversation_overview(
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """Get conversation overview statistics."""
    tenant_uuid = _get_tenant_uuid(current_user)

    # Total conversations
    total_stmt = select(func.count()).select_from(Conversation).where(Conversation.tenant_id == tenant_uuid)
    total_res = await db.execute(total_stmt)
    total_conversations = total_res.scalar_one()

    # Active conversations
    active_stmt = select(func.count()).select_from(Conversation).where(
        Conversation.tenant_id == tenant_uuid, Conversation.status == "active"
    )
    active_res = await db.execute(active_stmt)
    active_conversations = active_res.scalar_one()

    # Resolved conversations
    resolved_stmt = select(func.count()).select_from(Conversation).where(
        Conversation.tenant_id == tenant_uuid, Conversation.status == "resolved"
    )
    resolved_res = await db.execute(resolved_stmt)
    resolved_conversations = resolved_res.scalar_one()

    # Closed conversations
    closed_stmt = select(func.count()).select_from(Conversation).where(
        Conversation.tenant_id == tenant_uuid, Conversation.status == "closed"
    )
    closed_res = await db.execute(closed_stmt)
    closed_conversations = closed_res.scalar_one()

    # Average duration
    avg_dur_stmt = select(func.avg(Conversation.duration_seconds)).where(
        Conversation.tenant_id == tenant_uuid, Conversation.duration_seconds.isnot(None)
    )
    avg_dur_res = await db.execute(avg_dur_stmt)
    avg_duration_seconds = int(avg_dur_res.scalar_one() or 0)

    # Average satisfaction
    avg_sat_stmt = select(func.avg(Conversation.satisfaction_score)).where(
        Conversation.tenant_id == tenant_uuid, Conversation.satisfaction_score.isnot(None)
    )
    avg_sat_res = await db.execute(avg_sat_stmt)
    avg_satisfaction_score = float(avg_sat_res.scalar_one() or 0.0)

    # Handoff rate
    handoff_stmt = select(func.count()).select_from(Conversation).where(
        Conversation.tenant_id == tenant_uuid, Conversation.is_handoff == True
    )
    handoff_res = await db.execute(handoff_stmt)
    handoff_count = handoff_res.scalar_one()
    handoff_rate = (handoff_count / total_conversations * 100) if total_conversations > 0 else 0.0

    # Conversations by channel
    channel_stmt = (
        select(Conversation.channel, func.count())
        .where(Conversation.tenant_id == tenant_uuid)
        .group_by(Conversation.channel)
    )
    channel_res = await db.execute(channel_stmt)
    conversations_by_channel = {row[0]: row[1] for row in channel_res.fetchall()}

    # Conversations by status
    status_stmt = (
        select(Conversation.status, func.count())
        .where(Conversation.tenant_id == tenant_uuid)
        .group_by(Conversation.status)
    )
    status_res = await db.execute(status_stmt)
    conversations_by_status = {row[0]: row[1] for row in status_res.fetchall()}

    # Top agents
    agent_stmt = (
        select(Conversation.assigned_to, func.count())
        .where(Conversation.tenant_id == tenant_uuid, Conversation.assigned_to.isnot(None))
        .group_by(Conversation.assigned_to)
        .order_by(desc(func.count()))
        .limit(10)
    )
    agent_res = await db.execute(agent_stmt)
    top_agents = [{"agent_id": row[0], "count": row[1]} for row in agent_res.fetchall()]

    # Recent conversations
    recent_stmt = (
        select(Conversation)
        .where(Conversation.tenant_id == tenant_uuid)
        .order_by(desc(Conversation.created_at))
        .limit(5)
    )
    recent_res = await db.execute(recent_stmt)
    recent_conversations = [_conversation_to_dto(c) for c in recent_res.scalars().all()]

    return ConversationOverviewDTO(
        total_conversations=total_conversations,
        active_conversations=active_conversations,
        resolved_conversations=resolved_conversations,
        closed_conversations=closed_conversations,
        avg_duration_seconds=avg_duration_seconds,
        avg_satisfaction_score=round(avg_satisfaction_score, 2),
        handoff_rate=round(handoff_rate, 2),
        conversations_by_channel=conversations_by_channel,
        conversations_by_status=conversations_by_status,
        top_agents=top_agents,
        recent_conversations=recent_conversations,
    )


@router.get("/stats/by-status", response_model=List[ConversationStatsDTO], summary="Get Status Statistics")
async def get_status_stats(
    days: int = Query(30, ge=1, le=365, description="Number of days to analyze"),
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """Get conversation statistics grouped by status."""
    tenant_uuid = _get_tenant_uuid(current_user)
    cutoff = datetime.now(datetime.now().astimezone().tzinfo) - timedelta(days=days)

    stmt = (
        select(Conversation.status, func.count())
        .where(Conversation.tenant_id == tenant_uuid, Conversation.created_at >= cutoff)
        .group_by(Conversation.status)
        .order_by(desc(func.count()))
    )
    res = await db.execute(stmt)
    rows = res.fetchall()

    total = sum(row[1] for row in rows)

    return [
        ConversationStatsDTO(
            status=row[0],
            count=row[1],
            percentage=(row[1] / total * 100) if total > 0 else 0.0,
        )
        for row in rows
    ]


@router.get("/stats/by-channel", response_model=List[ConversationStatsDTO], summary="Get Channel Statistics")
async def get_channel_stats(
    days: int = Query(30, ge=1, le=365, description="Number of days to analyze"),
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """Get conversation statistics grouped by channel."""
    tenant_uuid = _get_tenant_uuid(current_user)
    cutoff = datetime.now(datetime.now().astimezone().tzinfo) - timedelta(days=days)

    stmt = (
        select(Conversation.channel, func.count())
        .where(Conversation.tenant_id == tenant_uuid, Conversation.created_at >= cutoff)
        .group_by(Conversation.channel)
        .order_by(desc(func.count()))
    )
    res = await db.execute(stmt)
    rows = res.fetchall()

    total = sum(row[1] for row in rows)

    return [
        ConversationStatsDTO(
            status=row[0],
            count=row[1],
            percentage=(row[1] / total * 100) if total > 0 else 0.0,
        )
        for row in rows
    ]