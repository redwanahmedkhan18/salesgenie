"""
Search Service API Router
Endpoints for full-text search, document indexing, and search analytics.
"""

import uuid
import time
from typing import List, Optional, Dict, Any
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func, and_

from enterprise_ai_platform.common.database import get_async_db
from enterprise_ai_platform.common.security_rbac import (
    get_current_user,
    TokenPayload,
    RequirePermissions,
    Permission,
)
from .models import (
    SearchIndex,
    SearchHitDTO,
    SearchResponseDTO,
    IndexDocumentRequest,
    IndexDocumentResponse,
    BulkIndexRequest,
    SearchRequest,
    IndexStatsDTO,
    IndexSettingsDTO,
    SearchIndexType,
)

router = APIRouter(prefix="/api/v1/search", tags=["Full-Text Search & Indexing"])


def _get_tenant_uuid(current_user: TokenPayload) -> uuid.UUID:
    """Extract tenant UUID from current user token."""
    return uuid.UUID(uuid.uuid5(uuid.NAMESPACE_DNS, current_user.tenant_id).hex[:32])


def _index_to_hit(idx: SearchIndex, score: float = 1.0) -> SearchHitDTO:
    """Convert SearchIndex model to SearchHitDTO."""
    return SearchHitDTO(
        id=str(idx.id),
        index_type=idx.index_type,
        document_id=idx.document_id,
        title=idx.title,
        content=idx.content[:500] if idx.content else "",
        tags=idx.tags,
        metadata=idx.metadata_json,
        score=score,
        highlights=None,
    )


# -------------------------------------------------------------------
# Search
# -------------------------------------------------------------------

@router.post("/search", response_model=SearchResponseDTO, summary="Full-Text Search")
async def search(
    req: SearchRequest,
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """Execute full-text search across indexed content."""
    tenant_uuid = _get_tenant_uuid(current_user)
    start_time = time.time()

    stmt = select(SearchIndex).where(SearchIndex.tenant_id == tenant_uuid)

    # Filter by index types
    if req.index_types:
        stmt = stmt.where(SearchIndex.index_type.in_(req.index_types))

    # Filter by tags
    if req.tags:
        for tag in req.tags:
            stmt = stmt.where(SearchIndex.tags.contains([tag]))

    # Apply filters
    if req.filters:
        for key, value in req.filters.items():
            if key in req.filters:
                stmt = stmt.where(
                    SearchIndex.metadata_json[key].astext == str(value)
                )

    # Text search - simple LIKE-based search
    search_term = f"%{req.query}%"
    stmt = stmt.where(
        (SearchIndex.title.ilike(search_term)) |
        (SearchIndex.content.ilike(search_term))
    )

    # Pagination
    stmt = stmt.offset(req.from_).limit(req.size)

    res = await db.execute(stmt)
    indices = res.scalars().all()

    hits = [_index_to_hit(idx, score=1.0) for idx in indices]

    took_ms = int((time.time() - start_time) * 1000)

    return SearchResponseDTO(
        query=req.query,
        total_hits=len(hits),
        hits=hits,
        took_ms=took_ms,
        aggregations=None,
    )


@router.get("/search", response_model=SearchResponseDTO, summary="Search (GET)")
async def search_get(
    q: str = Query(..., description="Search query"),
    index_types: Optional[str] = Query(None, description="Comma-separated index types"),
    size: int = Query(10, ge=1, le=100),
    from_: int = Query(0, ge=0, alias="from"),
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """Search via GET request."""
    req = SearchRequest(
        query=q,
        index_types=index_types.split(",") if index_types else None,
        size=size,
        from_=from_,
    )
    return await search(req, current_user, db)


# -------------------------------------------------------------------
# Indexing
# -------------------------------------------------------------------

@router.post("/index", response_model=IndexDocumentResponse, status_code=status.HTTP_201_CREATED,
             summary="Index a Document")
async def index_document(
    req: IndexDocumentRequest,
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """Index a document for full-text search."""
    tenant_uuid = _get_tenant_uuid(current_user)

    # Check if document already exists
    stmt = select(SearchIndex).where(
        SearchIndex.tenant_id == tenant_uuid,
        SearchIndex.document_id == req.document_id,
        SearchIndex.index_type == req.index_type,
    )
    res = await db.execute(stmt)
    existing = res.scalar_one_or_none()

    if existing:
        existing.title = req.title
        existing.content = req.content
        existing.tags = req.tags
        existing.metadata_json = req.metadata
        existing.is_public = req.is_public
        existing.last_indexed_at = datetime.now(datetime.now().astimezone().tzinfo)
    else:
        idx = SearchIndex(
            tenant_id=tenant_uuid,
            index_type=req.index_type,
            document_id=req.document_id,
            title=req.title,
            content=req.content,
            tags=req.tags,
            metadata_json=req.metadata,
            is_public=req.is_public,
        )
        db.add(idx)

    await db.commit()

    return IndexDocumentResponse(
        document_id=req.document_id,
        index_type=req.index_type,
        status="indexed",
        indexed_at=datetime.now(datetime.now().astimezone().tzinfo),
    )


@router.post("/index/bulk", response_model=Dict[str, Any], summary="Bulk Index Documents")
async def bulk_index(
    req: BulkIndexRequest,
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """Bulk index multiple documents."""
    tenant_uuid = _get_tenant_uuid(current_user)
    indexed_count = 0
    errors = []

    for doc_req in req.documents:
        try:
            stmt = select(SearchIndex).where(
                SearchIndex.tenant_id == tenant_uuid,
                SearchIndex.document_id == doc_req.document_id,
                SearchIndex.index_type == doc_req.index_type,
            )
            res = await db.execute(stmt)
            existing = res.scalar_one_or_none()

            if existing:
                existing.title = doc_req.title
                existing.content = doc_req.content
                existing.tags = doc_req.tags
                existing.metadata_json = doc_req.metadata
                existing.last_indexed_at = datetime.now(datetime.now().astimezone().tzinfo)
            else:
                idx = SearchIndex(
                    tenant_id=tenant_uuid,
                    index_type=doc_req.index_type,
                    document_id=doc_req.document_id,
                    title=doc_req.title,
                    content=doc_req.content,
                    tags=doc_req.tags,
                    metadata_json=doc_req.metadata,
                    is_public=doc_req.is_public,
                )
                db.add(idx)

            indexed_count += 1
        except Exception as e:
            errors.append({"document_id": doc_req.document_id, "error": str(e)})

    await db.commit()

    return {
        "indexed": indexed_count,
        "errors": errors,
        "total": len(req.documents),
    }


@router.delete("/index/{document_id}", status_code=status.HTTP_204_NO_CONTENT,
               summary="Delete Document from Index")
async def delete_from_index(
    document_id: str,
    index_type: Optional[str] = Query(None, description="Index type to filter"),
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """Delete a document from the search index."""
    tenant_uuid = _get_tenant_uuid(current_user)

    stmt = select(SearchIndex).where(
        SearchIndex.tenant_id == tenant_uuid,
        SearchIndex.document_id == document_id,
    )

    if index_type:
        stmt = stmt.where(SearchIndex.index_type == index_type)

    res = await db.execute(stmt)
    indices = res.scalars().all()

    if not indices:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Document {document_id} not found in index",
        )

    for idx in indices:
        await db.delete(idx)

    await db.commit()
    return None


# -------------------------------------------------------------------
# Index Management
# -------------------------------------------------------------------

@router.get("/index/stats", response_model=List[IndexStatsDTO], summary="Get Index Statistics")
async def get_index_stats(
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """Get statistics for all search indices."""
    tenant_uuid = _get_tenant_uuid(current_user)

    stmt = (
        select(SearchIndex.index_type, func.count(), func.max(SearchIndex.last_indexed_at))
        .where(SearchIndex.tenant_id == tenant_uuid)
        .group_by(SearchIndex.index_type)
    )
    res = await db.execute(stmt)
    rows = res.fetchall()

    return [
        IndexStatsDTO(
            index_type=row[0],
            document_count=row[1],
            last_updated=row[2] or datetime.now(datetime.now().astimezone().tzinfo),
        )
        for row in rows
    ]


@router.get("/index/settings", response_model=List[IndexSettingsDTO], summary="Get Index Settings")
async def get_index_settings(
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """Get index settings and health."""
    tenant_uuid = _get_tenant_uuid(current_user)

    stmt = (
        select(SearchIndex.index_type, func.count())
        .where(SearchIndex.tenant_id == tenant_uuid)
        .group_by(SearchIndex.index_type)
    )
    res = await db.execute(stmt)
    rows = res.fetchall()

    return [
        IndexSettingsDTO(
            index_name=f"sg_{tenant_uuid}_{row[0]}s",
            document_count=row[1],
            health="green",
            settings={
                "number_of_shards": 1,
                "number_of_replicas": 1,
                "refresh_interval": "1s",
            },
        )
        for row in rows
    ]


@router.post("/index/rebuild", response_model=Dict[str, Any], summary="Rebuild Search Index")
async def rebuild_index(
    index_type: Optional[str] = Query(None, description="Index type to rebuild"),
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """Rebuild search index from scratch."""
    tenant_uuid = _get_tenant_uuid(current_user)

    stmt = select(SearchIndex).where(SearchIndex.tenant_id == tenant_uuid)
    if index_type:
        stmt = stmt.where(SearchIndex.index_type == index_type)

    res = await db.execute(stmt)
    indices = res.scalars().all()

    # In a real implementation, this would trigger an OpenSearch reindex
    # For now, we just update the last_indexed_at timestamp
    for idx in indices:
        idx.last_indexed_at = datetime.now(datetime.now().astimezone().tzinfo)

    await db.commit()

    return {
        "status": "rebuilt",
        "index_type": index_type or "all",
        "documents_processed": len(indices),
    }