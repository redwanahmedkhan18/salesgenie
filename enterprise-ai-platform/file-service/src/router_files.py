"""
File Service API Router
Endpoints for file upload, download, search, and management.
"""

import uuid
import time
import hashlib
from typing import List, Optional, Dict, Any
from fastapi import APIRouter, Depends, HTTPException, status, Query, UploadFile, File as FastAPIFile, Response
from fastapi.responses import StreamingResponse
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func, and_, desc, asc, or_
from datetime import datetime, timedelta
from io import BytesIO

from enterprise_ai_platform.common.database import get_async_db
from enterprise_ai_platform.common.security_rbac import (
    get_current_user,
    TokenPayload,
)
from .models import (
    FileMetadata,
    FileMetadataDTO,
    FileUploadResponse,
    FileDownloadResponse,
    FileSearchRequest,
    FileSearchResponse,
    FileStatsDTO,
    FileOverviewDTO,
    FileVersionDTO,
    FileShareRequest,
    FileShareResponse,
    FileVisibility,
    FileCategory,
)

router = APIRouter(prefix="/api/v1/files", tags=["File Storage & Management"])


def _get_tenant_uuid(current_user: TokenPayload) -> uuid.UUID:
    """Extract tenant UUID from current user token."""
    return uuid.UUID(uuid.uuid5(uuid.NAMESPACE_DNS, current_user.tenant_id).hex[:32])


def _file_to_dto(file: FileMetadata) -> FileMetadataDTO:
    """Convert FileMetadata model to FileMetadataDTO."""
    return FileMetadataDTO(
        id=str(file.id),
        filename=file.filename,
        file_size=file.file_size,
        content_type=file.content_type,
        file_category=file.file_category,
        visibility=file.visibility,
        checksum=file.checksum,
        version=file.version,
        is_deleted=file.is_deleted,
        uploaded_by=file.uploaded_by,
        download_count=file.download_count,
        tags=file.tags,
        metadata=file.metadata_json,
        download_url=f"/api/v1/files/{file.id}/download",
        tenant_id=str(file.tenant_id),
        created_at=file.created_at,
        updated_at=file.updated_at,
    )


def _detect_category(content_type: str, filename: str) -> str:
    """Detect file category from content type and filename."""
    ct = content_type.lower()
    ext = filename.rsplit('.', 1)[-1].lower() if '.' in filename else ''

    if ct.startswith('image/') or ext in ('jpg', 'jpeg', 'png', 'gif', 'webp', 'svg'):
        return FileCategory.IMAGE
    elif ct.startswith('video/') or ext in ('mp4', 'avi', 'mov', 'mkv'):
        return FileCategory.VIDEO
    elif ct.startswith('audio/') or ext in ('mp3', 'wav', 'ogg', 'flac'):
        return FileCategory.AUDIO
    elif ct in ('application/vnd.ms-excel', 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet') or ext in ('xls', 'xlsx', 'csv'):
        return FileCategory.SPREADSHEET
    elif ct in ('application/vnd.ms-powerpoint', 'application/vnd.openxmlformats-officedocument.presentationml.presentation') or ext in ('ppt', 'pptx'):
        return FileCategory.PRESENTATION
    elif ct == 'application/pdf' or ext in ('pdf', 'doc', 'docx', 'txt', 'md'):
        return FileCategory.DOCUMENT
    elif ext in ('zip', 'tar', 'gz', 'rar'):
        return FileCategory.ARCHIVE
    else:
        return FileCategory.OTHER


def _compute_checksum(content: bytes) -> str:
    """Compute SHA-256 checksum of file content."""
    return hashlib.sha256(content).hexdigest()


# -------------------------------------------------------------------
# File Upload
# -------------------------------------------------------------------

@router.post("/upload", response_model=FileUploadResponse, status_code=status.HTTP_201_CREATED,
             summary="Upload a File")
async def upload_file(
    file: UploadFile = FastAPIFile(...),
    visibility: str = Query("private", description="File visibility"),
    tags: Optional[str] = Query(None, description="Comma-separated tags"),
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """Upload a file to storage."""
    tenant_uuid = _get_tenant_uuid(current_user)

    content = await file.read()
    await file.seek(0)

    checksum = _compute_checksum(content)
    file_category = _detect_category(file.content_type or 'application/octet-stream', file.filename)
    file_size = len(content)

    # Check if file already exists (same checksum)
    stmt = select(FileMetadata).where(
        FileMetadata.tenant_id == tenant_uuid,
        FileMetadata.checksum == checksum,
        FileMetadata.is_deleted == False,
    )
    res = await db.execute(stmt)
    existing = res.scalar_one_or_none()

    if existing:
        existing.version += 1
        existing.uploaded_by = current_user.sub
        existing.updated_at = datetime.now(datetime.now().astimezone().tzinfo)
        file_record = existing
    else:
        file_record = FileMetadata(
            tenant_id=tenant_uuid,
            bucket=f"sg-{tenant_uuid}",
            object_key=f"{tenant_uuid}/{file.filename}",
            filename=file.filename,
            file_size=file_size,
            content_type=file.content_type or 'application/octet-stream',
            file_category=file_category,
            visibility=visibility,
            checksum=checksum,
            uploaded_by=current_user.sub,
            tags=tags.split(',') if tags else None,
        )
        db.add(file_record)

    await db.commit()
    await db.refresh(file_record)

    return FileUploadResponse(
        file_id=str(file_record.id),
        filename=file_record.filename,
        file_size=file_record.file_size,
        content_type=file_record.content_type,
        bucket=file_record.bucket,
        object_key=file_record.object_key,
        version=file_record.version,
        status="uploaded",
        uploaded_at=file_record.created_at,
        download_url=f"/api/v1/files/{file_record.id}/download",
    )


@router.post("/upload/bulk", response_model=Dict[str, Any], summary="Bulk Upload Files")
async def bulk_upload(
    files: List[UploadFile] = FastAPIFile(...),
    visibility: str = Query("private", description="File visibility"),
    tags: Optional[str] = Query(None, description="Comma-separated tags"),
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """Bulk upload multiple files."""
    tenant_uuid = _get_tenant_uuid(current_user)
    uploaded = []
    errors = []

    for file in files:
        try:
            content = await file.read()
            await file.seek(0)

            checksum = _compute_checksum(content)
            file_category = _detect_category(file.content_type or 'application/octet-stream', file.filename)

            file_record = FileMetadata(
                tenant_id=tenant_uuid,
                bucket=f"sg-{tenant_uuid}",
                object_key=f"{tenant_uuid}/{file.filename}",
                filename=file.filename,
                file_size=len(content),
                content_type=file.content_type or 'application/octet-stream',
                file_category=file_category,
                visibility=visibility,
                checksum=checksum,
                uploaded_by=current_user.sub,
                tags=tags.split(',') if tags else None,
            )
            db.add(file_record)
            uploaded.append(file.filename)
        except Exception as e:
            errors.append({"filename": file.filename, "error": str(e)})

    await db.commit()

    return {
        "uploaded": len(uploaded),
        "errors": errors,
        "total": len(files),
    }


# -------------------------------------------------------------------
# File Download & Access
# -------------------------------------------------------------------

@router.get("/{file_id}/download", response_model=FileDownloadResponse, summary="Download File")
async def download_file(
    file_id: str,
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """Get a presigned download URL for a file."""
    tenant_uuid = _get_tenant_uuid(current_user)

    stmt = select(FileMetadata).where(
        FileMetadata.tenant_id == tenant_uuid,
        FileMetadata.id == file_id,
        FileMetadata.is_deleted == False,
    )
    res = await db.execute(stmt)
    file = res.scalar_one_or_none()

    if not file:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"File {file_id} not found",
        )

    # Increment download count
    file.download_count += 1
    await db.commit()

    # In a real implementation, this would generate a MinIO presigned URL
    # For now, return the download endpoint as the URL
    return FileDownloadResponse(
        filename=file.filename,
        content_type=file.content_type,
        file_size=file.file_size,
        download_url=f"/api/v1/files/{file_id}/content",
        expires_in=3600,
    )


@router.get("/{file_id}/content", summary="Get File Content")
async def get_file_content(
    file_id: str,
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """Stream file content."""
    tenant_uuid = _get_tenant_uuid(current_user)

    stmt = select(FileMetadata).where(
        FileMetadata.tenant_id == tenant_uuid,
        FileMetadata.id == file_id,
        FileMetadata.is_deleted == False,
    )
    res = await db.execute(stmt)
    file = res.scalar_one_or_none()

    if not file:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"File {file_id} not found",
        )

    # In a real implementation, this would stream from MinIO
    # For now, return placeholder content
    content = f"File content for {file.filename}".encode()
    return StreamingResponse(
        BytesIO(content),
        media_type=file.content_type,
        headers={"Content-Disposition": f"attachment; filename={file.filename}"},
    )


# -------------------------------------------------------------------
# File Management
# -------------------------------------------------------------------

@router.get("/", response_model=FileSearchResponse, summary="Search Files")
async def search_files(
    query: Optional[str] = Query(None, description="Search query"),
    file_categories: Optional[str] = Query(None, description="Comma-separated categories"),
    tags: Optional[str] = Query(None, description="Comma-separated tags"),
    visibility: Optional[str] = Query(None, description="Visibility filter"),
    uploaded_by: Optional[str] = Query(None, description="Filter by uploader"),
    date_from: Optional[datetime] = Query(None, description="Start date"),
    date_to: Optional[datetime] = Query(None, description="End date"),
    size: int = Query(50, ge=1, le=200),
    from_: int = Query(0, ge=0, alias="from"),
    sort_by: str = Query("created_at", description="Sort field"),
    sort_order: str = Query("desc", description="Sort order"),
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """Search files with filters."""
    tenant_uuid = _get_tenant_uuid(current_user)
    start_time = time.time()

    stmt = select(FileMetadata).where(
        FileMetadata.tenant_id == tenant_uuid,
        FileMetadata.is_deleted == False,
    )

    # Text search
    if query:
        search_term = f"%{query}%"
        stmt = stmt.where(FileMetadata.filename.ilike(search_term))

    # Filter by categories
    if file_categories:
        cats = file_categories.split(",")
        stmt = stmt.where(FileMetadata.file_category.in_(cats))

    # Filter by tags
    if tags:
        tag_list = tags.split(",")
        for tag in tag_list:
            stmt = stmt.where(FileMetadata.tags.contains([tag]))

    # Filter by visibility
    if visibility:
        stmt = stmt.where(FileMetadata.visibility == visibility)

    # Filter by uploader
    if uploaded_by:
        stmt = stmt.where(FileMetadata.uploaded_by == uploaded_by)

    # Date range filters
    if date_from:
        stmt = stmt.where(FileMetadata.created_at >= date_from)
    if date_to:
        stmt = stmt.where(FileMetadata.created_at <= date_to)

    # Sorting
    sort_col = getattr(FileMetadata, sort_by, FileMetadata.created_at)
    if sort_order.lower() == "desc":
        stmt = stmt.order_by(desc(sort_col))
    else:
        stmt = stmt.order_by(asc(sort_col))

    # Pagination
    stmt = stmt.offset(from_).limit(size)

    res = await db.execute(stmt)
    files = res.scalars().all()

    took_ms = int((time.time() - start_time) * 1000)

    return FileSearchResponse(
        total_hits=len(files),
        hits=[_file_to_dto(f) for f in files],
        took_ms=took_ms,
    )


@router.get("/{file_id}", response_model=FileMetadataDTO, summary="Get File Metadata")
async def get_file(
    file_id: str,
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """Get file metadata by ID."""
    tenant_uuid = _get_tenant_uuid(current_user)

    stmt = select(FileMetadata).where(
        FileMetadata.tenant_id == tenant_uuid,
        FileMetadata.id == file_id,
    )
    res = await db.execute(stmt)
    file = res.scalar_one_or_none()

    if not file:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"File {file_id} not found",
        )

    return _file_to_dto(file)


@router.delete("/{file_id}", status_code=status.HTTP_204_NO_CONTENT, summary="Delete File")
async def delete_file(
    file_id: str,
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """Soft delete a file."""
    tenant_uuid = _get_tenant_uuid(current_user)

    stmt = select(FileMetadata).where(
        FileMetadata.tenant_id == tenant_uuid,
        FileMetadata.id == file_id,
    )
    res = await db.execute(stmt)
    file = res.scalar_one_or_none()

    if not file:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"File {file_id} not found",
        )

    file.is_deleted = True
    file.deleted_at = datetime.now(datetime.now().astimezone().tzinfo)
    await db.commit()
    return None


@router.patch("/{file_id}", response_model=FileMetadataDTO, summary="Update File Metadata")
async def update_file(
    file_id: str,
    tags: Optional[str] = Query(None, description="Comma-separated tags"),
    visibility: Optional[str] = Query(None, description="New visibility"),
    metadata: Optional[str] = Query(None, description="JSON metadata"),
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """Update file metadata."""
    tenant_uuid = _get_tenant_uuid(current_user)

    stmt = select(FileMetadata).where(
        FileMetadata.tenant_id == tenant_uuid,
        FileMetadata.id == file_id,
    )
    res = await db.execute(stmt)
    file = res.scalar_one_or_none()

    if not file:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"File {file_id} not found",
        )

    if tags:
        file.tags = tags.split(',')
    if visibility:
        file.visibility = visibility
    if metadata:
        import json
        file.metadata_json = json.loads(metadata)

    file.updated_at = datetime.now(datetime.now().astimezone().tzinfo)
    await db.commit()

    return _file_to_dto(file)


# -------------------------------------------------------------------
# Analytics & Overview
# -------------------------------------------------------------------

@router.get("/overview", response_model=FileOverviewDTO, summary="Get File Overview")
async def get_file_overview(
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """Get file overview statistics."""
    tenant_uuid = _get_tenant_uuid(current_user)

    # Total files
    total_stmt = select(func.count()).select_from(FileMetadata).where(
        FileMetadata.tenant_id == tenant_uuid,
        FileMetadata.is_deleted == False,
    )
    total_res = await db.execute(total_stmt)
    total_files = total_res.scalar_one()

    # Total size
    size_stmt = select(func.sum(FileMetadata.file_size)).where(
        FileMetadata.tenant_id == tenant_uuid,
        FileMetadata.is_deleted == False,
    )
    size_res = await db.execute(size_stmt)
    total_size_bytes = size_res.scalar_one() or 0

    # Files by category
    cat_stmt = (
        select(FileMetadata.file_category, func.count(), func.sum(FileMetadata.file_size))
        .where(FileMetadata.tenant_id == tenant_uuid, FileMetadata.is_deleted == False)
        .group_by(FileMetadata.file_category)
    )
    cat_res = await db.execute(cat_stmt)
    files_by_category = {row[0]: row[1] for row in cat_res.fetchall()}

    # Files by visibility
    vis_stmt = (
        select(FileMetadata.visibility, func.count())
        .where(FileMetadata.tenant_id == tenant_uuid, FileMetadata.is_deleted == False)
        .group_by(FileMetadata.visibility)
    )
    vis_res = await db.execute(vis_stmt)
    files_by_visibility = {row[0]: row[1] for row in vis_res.fetchall()}

    # Top tags
    tag_stmt = (
        select(FileMetadata.tags, func.count())
        .where(FileMetadata.tenant_id == tenant_uuid, FileMetadata.is_deleted == False)
        .limit(100)
    )
    tag_res = await db.execute(tag_stmt)
    tag_counts: Dict[str, int] = {}
    for row in tag_res.fetchall():
        tags = row[0]
        if tags:
            for tag in tags:
                tag_counts[tag] = tag_counts.get(tag, 0) + row[1]

    top_tags = sorted(
        [{"tag": k, "count": v} for k, v in tag_counts.items()],
        key=lambda x: x["count"],
        reverse=True,
    )[:10]

    # Recent uploads
    recent_stmt = (
        select(FileMetadata)
        .where(FileMetadata.tenant_id == tenant_uuid, FileMetadata.is_deleted == False)
        .order_by(desc(FileMetadata.created_at))
        .limit(5)
    )
    recent_res = await db.execute(recent_stmt)
    recent_uploads = [_file_to_dto(f) for f in recent_res.scalars().all()]

    # Storage usage by category
    storage_usage = {}
    for row in cat_res.fetchall():
        storage_usage[row[0]] = row[2] or 0

    return FileOverviewDTO(
        total_files=total_files,
        total_size_bytes=total_size_bytes,
        total_size_mb=round(total_size_bytes / (1024 * 1024), 2),
        files_by_category=files_by_category,
        files_by_visibility=files_by_visibility,
        top_tags=top_tags,
        recent_uploads=recent_uploads,
        storage_usage=storage_usage,
    )


@router.get("/stats/by-category", response_model=List[FileStatsDTO], summary="Get Category Statistics")
async def get_category_stats(
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """Get file statistics grouped by category."""
    tenant_uuid = _get_tenant_uuid(current_user)

    stmt = (
        select(FileMetadata.file_category, func.count(), func.sum(FileMetadata.file_size))
        .where(FileMetadata.tenant_id == tenant_uuid, FileMetadata.is_deleted == False)
        .group_by(FileMetadata.file_category)
        .order_by(desc(func.count()))
    )
    res = await db.execute(stmt)
    rows = res.fetchall()

    total_count = sum(row[1] for row in rows)
    total_size = sum(row[2] or 0 for row in rows)

    return [
        FileStatsDTO(
            file_category=row[0],
            count=row[1],
            total_size_bytes=row[2] or 0,
            percentage=(row[1] / total_count * 100) if total_count > 0 else 0.0,
        )
        for row in rows
    ]


# -------------------------------------------------------------------
# File Sharing
# -------------------------------------------------------------------

@router.post("/share", response_model=FileShareResponse, summary="Create File Share")
async def create_file_share(
    req: FileShareRequest,
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """Create a shared download link for a file."""
    tenant_uuid = _get_tenant_uuid(current_user)

    stmt = select(FileMetadata).where(
        FileMetadata.tenant_id == tenant_uuid,
        FileMetadata.id == req.file_id,
        FileMetadata.is_deleted == False,
    )
    res = await db.execute(stmt)
    file = res.scalar_one_or_none()

    if not file:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"File {req.file_id} not found",
        )

    share_id = str(uuid.uuid4())
    expires_at = datetime.now(datetime.now().astimezone().tzinfo) + timedelta(hours=req.expires_in_hours)

    return FileShareResponse(
        share_id=share_id,
        share_url=f"/api/v1/files/share/{share_id}",
        expires_at=expires_at,
        max_downloads=req.max_downloads,
        download_count=0,
    )


@router.get("/share/{share_id}", response_model=FileDownloadResponse, summary="Access Shared File")
async def access_shared_file(
    share_id: str,
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """Access a file via a share link."""
    # In a real implementation, this would validate the share_id
    # and check expiration/download limits
    return FileDownloadResponse(
        filename="shared_file",
        content_type="application/octet-stream",
        file_size=0,
        download_url=f"/api/v1/files/share/{share_id}/content",
        expires_in=3600,
    )