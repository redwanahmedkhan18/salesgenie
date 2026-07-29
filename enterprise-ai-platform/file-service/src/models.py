"""
File Service Data Models & Schemas
File metadata models and file operation DTOs.
"""

import uuid
from datetime import datetime
from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field
import enum

from enterprise_ai_platform.common.models_base import (
    Base,
    UUIDPrimaryKeyMixin,
    TimestampMixin,
    TenantIsolationMixin,
)
from sqlalchemy import Column, String, Boolean, Text, Integer, ForeignKey, JSON
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.orm import Mapped, mapped_column


class FileVisibility(str, enum.Enum):
    """Visibility levels for files."""
    PRIVATE = "private"
    TENANT = "tenant"
    PUBLIC = "public"


class FileCategory(str, enum.Enum):
    """Categories of files."""
    DOCUMENT = "document"
    IMAGE = "image"
    VIDEO = "video"
    AUDIO = "audio"
    SPREADSHEET = "spreadsheet"
    PRESENTATION = "presentation"
    ARCHIVE = "archive"
    OTHER = "other"


class FileMetadata(Base, UUIDPrimaryKeyMixin, TimestampMixin, TenantIsolationMixin):
    """File metadata stored in database, with actual content in MinIO."""
    __tablename__ = "file_metadata"

    bucket: Mapped[str] = mapped_column(
        String(100), nullable=False, index=True,
        comment="MinIO bucket name"
    )
    object_key: Mapped[str] = mapped_column(
        String(500), nullable=False, unique=True,
        comment="MinIO object key"
    )
    filename: Mapped[str] = mapped_column(
        String(255), nullable=False,
        comment="Original filename"
    )
    file_size: Mapped[int] = mapped_column(
        Integer, nullable=False,
        comment="File size in bytes"
    )
    content_type: Mapped[str] = mapped_column(
        String(200), nullable=False,
        comment="MIME content type"
    )
    file_category: Mapped[str] = mapped_column(
        String(30), nullable=False, default="other",
        comment="Category of the file"
    )
    visibility: Mapped[str] = mapped_column(
        String(20), nullable=False, default="private",
        comment="Visibility level"
    )
    checksum: Mapped[Optional[str]] = mapped_column(
        String(64), nullable=True,
        comment="SHA-256 checksum of file content"
    )
    etag: Mapped[Optional[str]] = mapped_column(
        String(100), nullable=True,
        comment="MinIO ETag for the object"
    )
    version: Mapped[int] = mapped_column(
        Integer, default=1, nullable=False,
        comment="File version number"
    )
    is_deleted: Mapped[bool] = mapped_column(
        Boolean, default=False, nullable=False,
        comment="Soft delete flag"
    )
    deleted_at: Mapped[Optional[datetime]] = mapped_column(
        nullable=True,
        comment="When the file was soft-deleted"
    )
    uploaded_by: Mapped[Optional[str]] = mapped_column(
        String(100), nullable=True, index=True,
        comment="ID of the user who uploaded the file"
    )
    download_count: Mapped[int] = mapped_column(
        Integer, default=0, nullable=False,
        comment="Number of times the file has been downloaded"
    )
    metadata_json: Mapped[Optional[dict]] = mapped_column(
        JSONB, nullable=True,
        comment="Additional file metadata"
    )
    tags: Mapped[Optional[List[str]]] = mapped_column(
        JSONB, nullable=True,
        comment="Tags for the file"
    )

    @property
    def download_url(self) -> str:
        """Generate a presigned download URL path."""
        return f"/api/v1/files/{self.id}/download"


# -------------------------------------------------------------------
# Pydantic Schemas / DTOs
# -------------------------------------------------------------------

class FileMetadataDTO(BaseModel):
    id: str
    filename: str
    file_size: int
    content_type: str
    file_category: str
    visibility: str
    checksum: Optional[str] = None
    version: int
    is_deleted: bool
    uploaded_by: Optional[str] = None
    download_count: int
    tags: Optional[List[str]] = None
    metadata: Optional[Dict[str, Any]] = None
    download_url: str
    tenant_id: str
    created_at: datetime
    updated_at: datetime


class FileUploadResponse(BaseModel):
    file_id: str
    filename: str
    file_size: int
    content_type: str
    bucket: str
    object_key: str
    version: int
    status: str
    uploaded_at: datetime
    download_url: str


class FileDownloadResponse(BaseModel):
    filename: str
    content_type: str
    file_size: int
    download_url: str
    expires_in: int


class FileSearchRequest(BaseModel):
    query: Optional[str] = None
    file_categories: Optional[List[str]] = None
    tags: Optional[List[str]] = None
    visibility: Optional[str] = None
    uploaded_by: Optional[str] = None
    date_from: Optional[datetime] = None
    date_to: Optional[datetime] = None
    size: int = 50
    from_: int = 0
    sort_by: str = "created_at"
    sort_order: str = "desc"


class FileSearchResponse(BaseModel):
    total_hits: int
    hits: List[FileMetadataDTO]
    took_ms: int


class FileStatsDTO(BaseModel):
    file_category: str
    count: int
    total_size_bytes: int
    percentage: float


class FileOverviewDTO(BaseModel):
    total_files: int
    total_size_bytes: int
    total_size_mb: float
    files_by_category: Dict[str, int]
    files_by_visibility: Dict[str, int]
    top_tags: List[Dict[str, Any]]
    recent_uploads: List[FileMetadataDTO]
    storage_usage: Dict[str, int]


class FileVersionDTO(BaseModel):
    version: int
    file_size: int
    uploaded_at: datetime
    uploaded_by: Optional[str] = None


class FileShareRequest(BaseModel):
    file_id: str
    expires_in_hours: int = 24
    max_downloads: Optional[int] = None
    password: Optional[str] = None


class FileShareResponse(BaseModel):
    share_id: str
    share_url: str
    expires_at: datetime
    max_downloads: Optional[int] = None
    download_count: int