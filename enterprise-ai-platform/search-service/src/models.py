"""
Search Service Data Models & Schemas
Search index models and search result DTOs.
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
from sqlalchemy import Column, String, Boolean, Text, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.orm import Mapped, mapped_column


class SearchIndexType(str, enum.Enum):
    """Types of content that can be indexed."""
    DOCUMENT = "document"
    CUSTOMER = "customer"
    TICKET = "ticket"
    CONVERSATION = "conversation"
    KNOWLEDGE_BASE = "knowledge_base"


class SearchIndex(Base, UUIDPrimaryKeyMixin, TimestampMixin, TenantIsolationMixin):
    """Search index entry for OpenSearch."""
    __tablename__ = "search_indices"

    index_type: Mapped[str] = mapped_column(
        String(30), nullable=False, index=True,
        comment="Type of indexed content"
    )
    document_id: Mapped[str] = mapped_column(
        String(100), nullable=False, index=True,
        comment="ID of the original document"
    )
    title: Mapped[str] = mapped_column(String(300), nullable=False)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    content_vector: Mapped[Optional[list]] = mapped_column(JSONB, nullable=True,
        comment="Vector embedding for semantic search")
    tags: Mapped[Optional[List[str]]] = mapped_column(JSONB, nullable=True)
    metadata_json: Mapped[Optional[dict]] = mapped_column(JSONB, nullable=True)
    is_public: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    last_indexed_at: Mapped[datetime] = mapped_column(
        default=lambda: datetime.now(datetime.now().astimezone().tzinfo),
        nullable=False
    )

    @property
    def index_name(self) -> str:
        """Generate OpenSearch index name based on tenant and type."""
        return f"sg_{self.tenant_id}_{self.index_type}s"


# -------------------------------------------------------------------
# Pydantic Schemas / DTOs
# -------------------------------------------------------------------

class SearchHitDTO(BaseModel):
    id: str
    index_type: str
    document_id: str
    title: str
    content: str
    tags: Optional[List[str]] = None
    metadata: Optional[Dict[str, Any]] = None
    score: float
    highlights: Optional[Dict[str, List[str]]] = None


class SearchResponseDTO(BaseModel):
    query: str
    total_hits: int
    hits: List[SearchHitDTO]
    took_ms: int
    aggregations: Optional[Dict[str, Any]] = None


class IndexDocumentRequest(BaseModel):
    index_type: str
    document_id: str
    title: str
    content: str
    tags: Optional[List[str]] = None
    metadata: Optional[Dict[str, Any]] = None
    is_public: bool = False


class IndexDocumentResponse(BaseModel):
    document_id: str
    index_type: str
    status: str
    indexed_at: datetime


class BulkIndexRequest(BaseModel):
    documents: List[IndexDocumentRequest]


class SearchRequest(BaseModel):
    query: str
    index_types: Optional[List[str]] = None
    tags: Optional[List[str]] = None
    filters: Optional[Dict[str, Any]] = None
    size: int = 10
    from_: int = 0
    sort_by: str = "score"
    sort_order: str = "desc"
    highlight: bool = True


class IndexStatsDTO(BaseModel):
    index_type: str
    document_count: int
    last_updated: datetime


class IndexSettingsDTO(BaseModel):
    index_name: str
    document_count: int
    health: str
    settings: Dict[str, Any]