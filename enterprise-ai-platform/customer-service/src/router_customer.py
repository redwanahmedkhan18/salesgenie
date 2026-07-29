"""
Customer Service API Router
Endpoints for customer profiles, segments, tags, notes, and purchase history.
"""

import uuid
from datetime import datetime, timezone
from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func, and_
from sqlalchemy.orm import selectinload

from enterprise_ai_platform.common.database import get_async_db
from enterprise_ai_platform.common.security_rbac import (
    get_current_user,
    TokenPayload,
    RequirePermissions,
    Permission,
)
from .models import (
    Customer,
    CustomerSegment,
    CustomerTag,
    CustomerNote,
    CustomerOrder,
    CustomerSegmentMember,
    CustomerTagMember,
    CustomerDTO,
    CreateCustomerRequest,
    UpdateCustomerRequest,
    CustomerSegmentDTO,
    CreateSegmentRequest,
    CustomerTagDTO,
    CreateTagRequest,
    CustomerNoteDTO,
    CreateNoteRequest,
    CustomerOrderDTO,
    CustomerHistoryDTO,
)

router = APIRouter(prefix="/api/v1/customers", tags=["Customer Profiles & CRM"])


def _get_tenant_uuid(current_user: TokenPayload) -> uuid.UUID:
    """Extract tenant UUID from current user token."""
    return uuid.UUID(uuid.uuid5(uuid.NAMESPACE_DNS, current_user.tenant_id).hex[:32])


def _customer_to_dto(c: Customer, tenant_uuid: uuid.UUID) -> CustomerDTO:
    """Convert Customer model to DTO with segment/tag names."""
    segment_names = [s.name for s in c.segments] if c.segments else []
    tag_names = [t.name for t in c.tags] if c.tags else []
    return CustomerDTO(
        id=c.id,
        email=c.email,
        phone_number=c.phone_number,
        full_name=c.full_name,
        company_name=c.company_name,
        avatar_url=c.avatar_url,
        job_title=c.job_title,
        lead_status=c.lead_status,
        lead_score=c.lead_score,
        lifetime_value=float(c.lifetime_value),
        total_orders=c.total_orders,
        last_interaction_at=c.last_interaction_at,
        is_active=c.is_active,
        tenant_id=tenant_uuid,
        created_at=c.created_at,
        segments=segment_names,
        tags=tag_names,
    )


# -------------------------------------------------------------------
# Customer CRUD
# -------------------------------------------------------------------

@router.post("/", response_model=CustomerDTO, status_code=status.HTTP_201_CREATED,
             summary="Create New Customer")
async def create_customer(
    req: CreateCustomerRequest,
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """Create a new customer profile with optional segments and tags."""
    tenant_uuid = _get_tenant_uuid(current_user)

    customer = Customer(
        tenant_id=tenant_uuid,
        email=req.email,
        phone_number=req.phone_number,
        full_name=req.full_name,
        company_name=req.company_name,
        avatar_url=req.avatar_url,
        job_title=req.job_title,
        lead_status=req.lead_status,
        lead_score=req.lead_score,
    )
    db.add(customer)
    await db.flush()

    # Add segment memberships
    if req.segment_ids:
        for seg_id in req.segment_ids:
            member = CustomerSegmentMember(customer_id=customer.id, segment_id=seg_id)
            db.add(member)

    # Add tag memberships
    if req.tag_ids:
        for tag_id in req.tag_ids:
            member = CustomerTagMember(customer_id=customer.id, tag_id=tag_id)
            db.add(member)

    await db.commit()
    await db.refresh(customer)
    return _customer_to_dto(customer, tenant_uuid)


@router.get("/", response_model=List[CustomerDTO], summary="List Customers")
async def list_customers(
    lead_status: Optional[str] = Query(None, description="Filter by lead status"),
    segment_id: Optional[uuid.UUID] = Query(None, description="Filter by segment"),
    tag_id: Optional[uuid.UUID] = Query(None, description="Filter by tag"),
    search: Optional[str] = Query(None, description="Search by name, email, or phone"),
    limit: int = Query(50, ge=1, le=200),
    offset: int = Query(0, ge=0),
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """List customers with optional filtering and search."""
    tenant_uuid = _get_tenant_uuid(current_user)
    stmt = select(Customer).where(Customer.tenant_id == tenant_uuid)

    if lead_status:
        stmt = stmt.where(Customer.lead_status == lead_status)

    if search:
        search_term = f"%{search}%"
        stmt = stmt.where(
            (Customer.full_name.ilike(search_term)) |
            (Customer.email.ilike(search_term)) |
            (Customer.phone_number.ilike(search_term))
        )

    if segment_id:
        stmt = stmt.join(CustomerSegmentMember).where(CustomerSegmentMember.segment_id == segment_id)

    if tag_id:
        stmt = stmt.join(CustomerTagMember).where(CustomerTagMember.tag_id == tag_id)

    stmt = stmt.options(
        selectinload(Customer.segments),
        selectinload(Customer.tags),
    ).order_by(Customer.created_at.desc()).limit(limit).offset(offset)

    res = await db.execute(stmt)
    customers = res.scalars().all()

    return [_customer_to_dto(c, tenant_uuid) for c in customers]


@router.get("/{customer_id}", response_model=CustomerHistoryDTO, summary="Get Customer Details")
async def get_customer(
    customer_id: uuid.UUID,
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """Get detailed customer profile with notes, orders, and interaction summary."""
    tenant_uuid = _get_tenant_uuid(current_user)

    stmt = (
        select(Customer)
        .where(Customer.id == customer_id, Customer.tenant_id == tenant_uuid)
        .options(
            selectinload(Customer.segments),
            selectinload(Customer.tags),
            selectinload(Customer.notes),
            selectinload(Customer.orders),
            selectinload(Customer.interaction_summary),
        )
    )
    res = await db.execute(stmt)
    customer = res.scalar_one_or_none()

    if not customer:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Customer {customer_id} not found",
        )

    notes = [
        CustomerNoteDTO(
            id=n.id, customer_id=n.customer_id, author_id=n.author_id,
            content=n.content, is_internal=n.is_internal,
            created_at=n.created_at, updated_at=n.updated_at,
        )
        for n in (customer.notes or [])
    ]

    orders = [
        CustomerOrderDTO(
            id=o.id, customer_id=o.customer_id, order_number=o.order_number,
            amount=float(o.amount), currency=o.currency, status=o.status,
            product_name=o.product_name, created_at=o.created_at,
        )
        for o in (customer.orders or [])
    ]

    interaction_text = customer.interaction_summary.summary_text if customer.interaction_summary else None

    return CustomerHistoryDTO(
        customer=_customer_to_dto(customer, tenant_uuid),
        notes=notes,
        orders=orders,
        interaction_summary=interaction_text,
    )


@router.patch("/{customer_id}", response_model=CustomerDTO, summary="Update Customer")
async def update_customer(
    customer_id: uuid.UUID,
    req: UpdateCustomerRequest,
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """Update customer profile attributes."""
    tenant_uuid = _get_tenant_uuid(current_user)

    stmt = select(Customer).where(Customer.id == customer_id, Customer.tenant_id == tenant_uuid)
    res = await db.execute(stmt)
    customer = res.scalar_one_or_none()

    if not customer:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Customer {customer_id} not found",
        )

    if req.email is not None:
        customer.email = req.email
    if req.phone_number is not None:
        customer.phone_number = req.phone_number
    if req.full_name is not None:
        customer.full_name = req.full_name
    if req.company_name is not None:
        customer.company_name = req.company_name
    if req.avatar_url is not None:
        customer.avatar_url = req.avatar_url
    if req.job_title is not None:
        customer.job_title = req.job_title
    if req.lead_status is not None:
        customer.lead_status = req.lead_status
    if req.lead_score is not None:
        customer.lead_score = req.lead_score
    if req.is_active is not None:
        customer.is_active = req.is_active

    # Update segments
    if req.segment_ids is not None:
        await db.execute(
            CustomerSegmentMember.__table__.delete().where(
                CustomerSegmentMember.customer_id == customer_id
            )
        )
        for seg_id in req.segment_ids:
            db.add(CustomerSegmentMember(customer_id=customer_id, segment_id=seg_id))

    # Update tags
    if req.tag_ids is not None:
        await db.execute(
            CustomerTagMember.__table__.delete().where(
                CustomerTagMember.customer_id == customer_id
            )
        )
        for tag_id in req.tag_ids:
            db.add(CustomerTagMember(customer_id=customer_id, tag_id=tag_id))

    await db.commit()
    await db.refresh(customer)

    stmt = (
        select(Customer)
        .where(Customer.id == customer_id)
        .options(selectinload(Customer.segments), selectinload(Customer.tags))
    )
    res = await db.execute(stmt)
    customer = res.scalar_one()

    return _customer_to_dto(customer, tenant_uuid)


@router.delete("/{customer_id}", status_code=status.HTTP_204_NO_CONTENT, summary="Delete Customer")
async def delete_customer(
    customer_id: uuid.UUID,
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """Soft delete a customer profile."""
    tenant_uuid = _get_tenant_uuid(current_user)

    stmt = select(Customer).where(Customer.id == customer_id, Customer.tenant_id == tenant_uuid)
    res = await db.execute(stmt)
    customer = res.scalar_one_or_none()

    if not customer:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Customer {customer_id} not found",
        )

    customer.is_active = False
    await db.commit()
    return None


# -------------------------------------------------------------------
# Segments
# -------------------------------------------------------------------

@router.post("/segments", response_model=CustomerSegmentDTO, status_code=status.HTTP_201_CREATED,
             summary="Create Customer Segment")
async def create_segment(
    req: CreateSegmentRequest,
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """Create a new customer segment."""
    tenant_uuid = _get_tenant_uuid(current_user)

    segment = CustomerSegment(
        tenant_id=tenant_uuid,
        name=req.name,
        description=req.description,
        color=req.color,
    )
    db.add(segment)
    await db.commit()
    await db.refresh(segment)

    count_stmt = select(func.count()).select_from(CustomerSegmentMember).where(
        CustomerSegmentMember.segment_id == segment.id
    )
    count_res = await db.execute(count_stmt)
    count = count_res.scalar() or 0

    return CustomerSegmentDTO(
        id=segment.id, name=segment.name, description=segment.description,
        color=segment.color, is_system=segment.is_system,
        customer_count=count, tenant_id=tenant_uuid, created_at=segment.created_at,
    )


@router.get("/segments", response_model=List[CustomerSegmentDTO], summary="List Segments")
async def list_segments(
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """List all customer segments for the tenant."""
    tenant_uuid = _get_tenant_uuid(current_user)

    stmt = select(CustomerSegment).where(CustomerSegment.tenant_id == tenant_uuid)
    res = await db.execute(stmt)
    segments = res.scalars().all()

    result = []
    for seg in segments:
        count_stmt = select(func.count()).select_from(CustomerSegmentMember).where(
            CustomerSegmentMember.segment_id == seg.id
        )
        count_res = await db.execute(count_stmt)
        count = count_res.scalar() or 0

        result.append(CustomerSegmentDTO(
            id=seg.id, name=seg.name, description=seg.description,
            color=seg.color, is_system=seg.is_system,
            customer_count=count, tenant_id=tenant_uuid, created_at=seg.created_at,
        ))

    return result


# -------------------------------------------------------------------
# Tags
# -------------------------------------------------------------------

@router.post("/tags", response_model=CustomerTagDTO, status_code=status.HTTP_201_CREATED,
             summary="Create Customer Tag")
async def create_tag(
    req: CreateTagRequest,
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """Create a new customer tag."""
    tenant_uuid = _get_tenant_uuid(current_user)

    tag = CustomerTag(
        tenant_id=tenant_uuid,
        name=req.name,
        color=req.color,
    )
    db.add(tag)
    await db.commit()
    await db.refresh(tag)

    count_stmt = select(func.count()).select_from(CustomerTagMember).where(
        CustomerTagMember.tag_id == tag.id
    )
    count_res = await db.execute(count_stmt)
    count = count_res.scalar() or 0

    return CustomerTagDTO(
        id=tag.id, name=tag.name, color=tag.color,
        customer_count=count, tenant_id=tenant_uuid, created_at=tag.created_at,
    )


@router.get("/tags", response_model=List[CustomerTagDTO], summary="List Tags")
async def list_tags(
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """List all customer tags for the tenant."""
    tenant_uuid = _get_tenant_uuid(current_user)

    stmt = select(CustomerTag).where(CustomerTag.tenant_id == tenant_uuid)
    res = await db.execute(stmt)
    tags = res.scalars().all()

    result = []
    for tag in tags:
        count_stmt = select(func.count()).select_from(CustomerTagMember).where(
            CustomerTagMember.tag_id == tag.id
        )
        count_res = await db.execute(count_stmt)
        count = count_res.scalar() or 0

        result.append(CustomerTagDTO(
            id=tag.id, name=tag.name, color=tag.color,
            customer_count=count, tenant_id=tenant_uuid, created_at=tag.created_at,
        ))

    return result


# -------------------------------------------------------------------
# Notes
# -------------------------------------------------------------------

@router.post("/notes", response_model=CustomerNoteDTO, status_code=status.HTTP_201_CREATED,
             summary="Add Customer Note")
async def add_note(
    req: CreateNoteRequest,
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """Add a note to a customer profile."""
    tenant_uuid = _get_tenant_uuid(current_user)

    stmt = select(Customer).where(Customer.id == req.customer_id, Customer.tenant_id == tenant_uuid)
    res = await db.execute(stmt)
    customer = res.scalar_one_or_none()

    if not customer:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Customer {req.customer_id} not found",
        )

    note = CustomerNote(
        customer_id=req.customer_id,
        author_id=uuid.UUID(current_user.sub),
        content=req.content,
        is_internal=req.is_internal,
    )
    db.add(note)
    await db.commit()
    await db.refresh(note)

    return CustomerNoteDTO(
        id=note.id, customer_id=note.customer_id, author_id=note.author_id,
        content=note.content, is_internal=note.is_internal,
        created_at=note.created_at, updated_at=note.updated_at,
    )


# -------------------------------------------------------------------
# Analytics
# -------------------------------------------------------------------

@router.get("/analytics/overview", summary="Customer Analytics Overview")
async def customer_analytics(
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """Get customer analytics overview."""
    tenant_uuid = _get_tenant_uuid(current_user)

    total_stmt = select(func.count()).select_from(Customer).where(Customer.tenant_id == tenant_uuid)
    total_res = await db.execute(total_stmt)
    total_customers = total_res.scalar() or 0

    by_status_stmt = (
        select(Customer.lead_status, func.count())
        .where(Customer.tenant_id == tenant_uuid)
        .group_by(Customer.lead_status)
    )
    by_status_res = await db.execute(by_status_stmt)
    by_status = {row[0]: row[1] for row in by_status_res.fetchall()}

    ltv_stmt = select(func.sum(Customer.lifetime_value)).where(Customer.tenant_id == tenant_uuid)
    ltv_res = await db.execute(ltv_stmt)
    total_ltv = float(ltv_res.scalar() or 0)

    return {
        "total_customers": total_customers,
        "by_lead_status": by_status,
        "total_lifetime_value": total_ltv,
        "avg_lifetime_value": total_ltv / total_customers if total_customers > 0 else 0,
    }