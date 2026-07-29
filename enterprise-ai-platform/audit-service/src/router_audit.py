"""
Audit Service API Router
Endpoints for audit logging, search, and compliance reporting.
"""

import uuid
import time
from typing import List, Optional, Dict, Any
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func, and_, desc, asc, or_
from datetime import datetime, timedelta

from enterprise_ai_platform.common.database import get_async_db
from enterprise_ai_platform.common.security_rbac import (
    get_current_user,
    TokenPayload,
)
from .models import (
    AuditLog,
    AuditLogDTO,
    AuditLogCreateRequest,
    AuditLogResponse,
    AuditSearchRequest,
    AuditSearchResponse,
    AuditStatsDTO,
    AuditOverviewDTO,
    AuditEventType,
    AuditSeverity,
)

router = APIRouter(prefix="/api/v1/audit", tags=["Audit Logging & Compliance"])


def _get_tenant_uuid(current_user: TokenPayload) -> uuid.UUID:
    """Extract tenant UUID from current user token."""
    return uuid.UUID(uuid.uuid5(uuid.NAMESPACE_DNS, current_user.tenant_id).hex[:32])


def _log_to_dto(log: AuditLog) -> AuditLogDTO:
    """Convert AuditLog model to AuditLogDTO."""
    return AuditLogDTO(
        id=str(log.id),
        event_type=log.event_type,
        severity=log.severity,
        actor_id=log.actor_id,
        actor_type=log.actor_type,
        resource_type=log.resource_type,
        resource_id=log.resource_id,
        action=log.action,
        description=log.description,
        ip_address=log.ip_address,
        user_agent=log.user_agent,
        request_id=log.request_id,
        metadata=log.metadata_json,
        is_compliance=log.is_compliance,
        retention_days=log.retention_days,
        tenant_id=str(log.tenant_id),
        created_at=log.created_at,
    )


# -------------------------------------------------------------------
# Audit Logging
# -------------------------------------------------------------------

@router.post("/logs", response_model=AuditLogResponse, status_code=status.HTTP_201_CREATED,
             summary="Create Audit Log Entry")
async def create_audit_log(
    req: AuditLogCreateRequest,
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """Create a new audit log entry."""
    tenant_uuid = _get_tenant_uuid(current_user)

    log = AuditLog(
        tenant_id=tenant_uuid,
        event_type=req.event_type,
        severity=req.severity,
        actor_id=req.actor_id,
        actor_type=req.actor_type,
        resource_type=req.resource_type,
        resource_id=req.resource_id,
        action=req.action,
        description=req.description,
        ip_address=req.ip_address,
        user_agent=req.user_agent,
        request_id=req.request_id,
        metadata_json=req.metadata,
        is_compliance=req.is_compliance,
        retention_days=req.retention_days,
    )
    db.add(log)
    await db.commit()

    return AuditLogResponse(id=str(log.id), status="created")


@router.get("/logs", response_model=AuditSearchResponse, summary="Search Audit Logs")
async def search_audit_logs(
    query: Optional[str] = Query(None, description="Search query"),
    event_types: Optional[str] = Query(None, description="Comma-separated event types"),
    severities: Optional[str] = Query(None, description="Comma-separated severities"),
    actor_ids: Optional[str] = Query(None, description="Comma-separated actor IDs"),
    resource_types: Optional[str] = Query(None, description="Comma-separated resource types"),
    actions: Optional[str] = Query(None, description="Comma-separated actions"),
    is_compliance: Optional[bool] = Query(None, description="Filter compliance events"),
    date_from: Optional[datetime] = Query(None, description="Start date"),
    date_to: Optional[datetime] = Query(None, description="End date"),
    size: int = Query(50, ge=1, le=200),
    from_: int = Query(0, ge=0, alias="from"),
    sort_by: str = Query("created_at", description="Sort field"),
    sort_order: str = Query("desc", description="Sort order"),
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """Search audit logs with filters."""
    tenant_uuid = _get_tenant_uuid(current_user)
    start_time = time.time()

    stmt = select(AuditLog).where(AuditLog.tenant_id == tenant_uuid)

    # Text search
    if query:
        search_term = f"%{query}%"
        stmt = stmt.where(
            or_(
                AuditLog.description.ilike(search_term),
                AuditLog.event_type.ilike(search_term),
                AuditLog.action.ilike(search_term),
            )
        )

    # Filter by event types
    if event_types:
        types = event_types.split(",")
        stmt = stmt.where(AuditLog.event_type.in_(types))

    # Filter by severities
    if severities:
        sevs = severities.split(",")
        stmt = stmt.where(AuditLog.severity.in_(sevs))

    # Filter by actor IDs
    if actor_ids:
        actors = actor_ids.split(",")
        stmt = stmt.where(AuditLog.actor_id.in_(actors))

    # Filter by resource types
    if resource_types:
        rtypes = resource_types.split(",")
        stmt = stmt.where(AuditLog.resource_type.in_(rtypes))

    # Filter by actions
    if actions:
        acts = actions.split(",")
        stmt = stmt.where(AuditLog.action.in_(acts))

    # Filter by compliance
    if is_compliance is not None:
        stmt = stmt.where(AuditLog.is_compliance == is_compliance)

    # Date range filters
    if date_from:
        stmt = stmt.where(AuditLog.created_at >= date_from)
    if date_to:
        stmt = stmt.where(AuditLog.created_at <= date_to)

    # Sorting
    sort_col = getattr(AuditLog, sort_by, AuditLog.created_at)
    if sort_order.lower() == "desc":
        stmt = stmt.order_by(desc(sort_col))
    else:
        stmt = stmt.order_by(asc(sort_col))

    # Pagination
    stmt = stmt.offset(from_).limit(size)

    res = await db.execute(stmt)
    logs = res.scalars().all()

    took_ms = int((time.time() - start_time) * 1000)

    return AuditSearchResponse(
        total_hits=len(logs),
        hits=[_log_to_dto(log) for log in logs],
        took_ms=took_ms,
    )


@router.get("/logs/{log_id}", response_model=AuditLogDTO, summary="Get Audit Log Entry")
async def get_audit_log(
    log_id: str,
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """Get a specific audit log entry by ID."""
    tenant_uuid = _get_tenant_uuid(current_user)

    stmt = select(AuditLog).where(
        AuditLog.tenant_id == tenant_uuid,
        AuditLog.id == log_id,
    )
    res = await db.execute(stmt)
    log = res.scalar_one_or_none()

    if not log:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Audit log entry {log_id} not found",
        )

    return _log_to_dto(log)


@router.delete("/logs", status_code=status.HTTP_204_NO_CONTENT, summary="Delete Audit Logs")
async def delete_audit_logs(
    event_types: Optional[str] = Query(None, description="Comma-separated event types to delete"),
    older_than_days: Optional[int] = Query(None, description="Delete logs older than N days"),
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """Delete audit logs (compliance-aware)."""
    tenant_uuid = _get_tenant_uuid(current_user)

    stmt = select(AuditLog).where(AuditLog.tenant_id == tenant_uuid)

    if event_types:
        types = event_types.split(",")
        stmt = stmt.where(AuditLog.event_type.in_(types))

    if older_than_days:
        cutoff = datetime.now(datetime.now().astimezone().tzinfo) - timedelta(days=older_than_days)
        stmt = stmt.where(AuditLog.created_at < cutoff)

    res = await db.execute(stmt)
    logs = res.scalars().all()

    for log in logs:
        await db.delete(log)

    await db.commit()
    return None


# -------------------------------------------------------------------
# Analytics & Compliance
# -------------------------------------------------------------------

@router.get("/overview", response_model=AuditOverviewDTO, summary="Get Audit Overview")
async def get_audit_overview(
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """Get audit overview statistics."""
    tenant_uuid = _get_tenant_uuid(current_user)
    now = datetime.now(datetime.now().astimezone().tzinfo)
    today_start = now.replace(hour=0, minute=0, second=0, microsecond=0)

    # Total events
    total_stmt = select(func.count()).select_from(AuditLog).where(AuditLog.tenant_id == tenant_uuid)
    total_res = await db.execute(total_stmt)
    total_events = total_res.scalar_one()

    # Events today
    today_stmt = select(func.count()).select_from(AuditLog).where(
        AuditLog.tenant_id == tenant_uuid,
        AuditLog.created_at >= today_start,
    )
    today_res = await db.execute(today_stmt)
    events_today = today_res.scalar_one()

    # Events by severity
    sev_stmt = (
        select(AuditLog.severity, func.count())
        .where(AuditLog.tenant_id == tenant_uuid)
        .group_by(AuditLog.severity)
    )
    sev_res = await db.execute(sev_stmt)
    events_by_severity = {row[0]: row[1] for row in sev_res.fetchall()}

    # Events by type
    type_stmt = (
        select(AuditLog.event_type, func.count())
        .where(AuditLog.tenant_id == tenant_uuid)
        .group_by(AuditLog.event_type)
    )
    type_res = await db.execute(type_stmt)
    events_by_type = {row[0]: row[1] for row in type_res.fetchall()}

    # Top actors
    actor_stmt = (
        select(AuditLog.actor_id, func.count())
        .where(AuditLog.tenant_id == tenant_uuid, AuditLog.actor_id.isnot(None))
        .group_by(AuditLog.actor_id)
        .order_by(desc(func.count()))
        .limit(10)
    )
    actor_res = await db.execute(actor_stmt)
    top_actors = [{"actor_id": row[0], "count": row[1]} for row in actor_res.fetchall()]

    # Compliance events
    comp_stmt = select(func.count()).select_from(AuditLog).where(
        AuditLog.tenant_id == tenant_uuid, AuditLog.is_compliance == True
    )
    comp_res = await db.execute(comp_stmt)
    compliance_events = comp_res.scalar_one()

    # Security alerts
    sec_stmt = select(func.count()).select_from(AuditLog).where(
        AuditLog.tenant_id == tenant_uuid, AuditLog.severity.in_(["critical", "error"])
    )
    sec_res = await db.execute(sec_stmt)
    security_alerts = sec_res.scalar_one()

    # Retention summary
    retention_stmt = (
        select(AuditLog.retention_days, func.count())
        .where(AuditLog.tenant_id == tenant_uuid)
        .group_by(AuditLog.retention_days)
    )
    retention_res = await db.execute(retention_stmt)
    retention_summary = {str(row[0]): row[1] for row in retention_res.fetchall()}

    return AuditOverviewDTO(
        total_events=total_events,
        events_today=events_today,
        events_by_severity=events_by_severity,
        events_by_type=events_by_type,
        top_actors=top_actors,
        compliance_events=compliance_events,
        security_alerts=security_alerts,
        retention_summary=retention_summary,
    )


@router.get("/stats/by-type", response_model=List[AuditStatsDTO], summary="Get Event Type Statistics")
async def get_event_type_stats(
    days: int = Query(30, ge=1, le=365, description="Number of days to analyze"),
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """Get statistics grouped by event type."""
    tenant_uuid = _get_tenant_uuid(current_user)
    cutoff = datetime.now(datetime.now().astimezone().tzinfo) - timedelta(days=days)

    stmt = (
        select(AuditLog.event_type, func.count())
        .where(AuditLog.tenant_id == tenant_uuid, AuditLog.created_at >= cutoff)
        .group_by(AuditLog.event_type)
        .order_by(desc(func.count()))
    )
    res = await db.execute(stmt)
    rows = res.fetchall()

    total = sum(row[1] for row in rows)

    return [
        AuditStatsDTO(
            event_type=row[0],
            count=row[1],
            percentage=(row[1] / total * 100) if total > 0 else 0.0,
        )
        for row in rows
    ]


@router.get("/stats/by-severity", response_model=List[AuditStatsDTO], summary="Get Severity Statistics")
async def get_severity_stats(
    days: int = Query(30, ge=1, le=365, description="Number of days to analyze"),
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """Get statistics grouped by severity."""
    tenant_uuid = _get_tenant_uuid(current_user)
    cutoff = datetime.now(datetime.now().astimezone().tzinfo) - timedelta(days=days)

    stmt = (
        select(AuditLog.severity, func.count())
        .where(AuditLog.tenant_id == tenant_uuid, AuditLog.created_at >= cutoff)
        .group_by(AuditLog.severity)
        .order_by(desc(func.count()))
    )
    res = await db.execute(stmt)
    rows = res.fetchall()

    total = sum(row[1] for row in rows)

    return [
        AuditStatsDTO(
            event_type=row[0],
            count=row[1],
            percentage=(row[1] / total * 100) if total > 0 else 0.0,
        )
        for row in rows
    ]


@router.get("/compliance/report", response_model=AuditSearchResponse, summary="Get Compliance Report")
async def get_compliance_report(
    date_from: Optional[datetime] = Query(None, description="Start date"),
    date_to: Optional[datetime] = Query(None, description="End date"),
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """Get compliance-relevant audit events."""
    tenant_uuid = _get_tenant_uuid(current_user)
    start_time = time.time()

    stmt = select(AuditLog).where(
        AuditLog.tenant_id == tenant_uuid,
        AuditLog.is_compliance == True,
    )

    if date_from:
        stmt = stmt.where(AuditLog.created_at >= date_from)
    if date_to:
        stmt = stmt.where(AuditLog.created_at <= date_to)

    stmt = stmt.order_by(desc(AuditLog.created_at)).limit(500)

    res = await db.execute(stmt)
    logs = res.scalars().all()

    took_ms = int((time.time() - start_time) * 1000)

    return AuditSearchResponse(
        total_hits=len(logs),
        hits=[_log_to_dto(log) for log in logs],
        took_ms=took_ms,
    )