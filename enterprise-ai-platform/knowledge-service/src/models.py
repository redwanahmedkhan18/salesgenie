"""
Knowledge Service Models
Database models for knowledge documents and categories.
"""

import uuid
from datetime import datetime
from typing import Optional, List, Any
from pydantic import BaseModel
from sqlalchemy import Column, String, Text, Boolean, Integer, DateTime, JSON, ForeignKey, func
from sqlalchemy.dialects.postgresql import UUID as PGUUID
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class KnowledgeCategory(Base):
    __tablename__ = "knowledge_categories"

    id: uuid.UUID = Column(PGUUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    tenant_id: uuid.UUID = Column(PGUUID(as_uuid=True), nullable=False, index=True)
    name: str = Column(String(100), nullable=False)
    slug: str = Column(String(100), nullable=False, unique=True, index=True)
    description: Optional[str] = Column(Text, nullable=True)
    color: Optional[str] = Column(String(20), nullable=True)
    document_count: int = Column(Integer, nullable=False, default=0)
    created_at: datetime = Column(DateTime(timezone=True), nullable=False, default=func.now())
    updated_at: datetime = Column(DateTime(timezone=True), nullable=False, default=func.now(), onupdate=func.now())


class KnowledgeDocument(Base):
    __tablename__ = "knowledge_documents"

    id: uuid.UUID = Column(PGUUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    tenant_id: uuid.UUID = Column(PGUUID(as_uuid=True), nullable=False, index=True)
    title: str = Column(String(255), nullable=False)
    slug: str = Column(String(255), nullable=False, index=True)
    content: str = Column(Text, nullable=False)
    content_vector: Optional[dict] = Column(JSON, nullable=True)
    document_type: str = Column(String(50), nullable=False, default="article")
    category: Optional[str] = Column(String(100), nullable=True, index=True)
    tags: Optional[List[str]] = Column(JSON, nullable=True)
    status: str = Column(String(30), nullable=False, default="published")
    is_public: bool = Column(Boolean, nullable=False, default=False)
    view_count: int = Column(Integer, nullable=False, default=0)
    word_count: Optional[int] = Column(Integer, nullable=True)
    language: str = Column(String(10), nullable=False, default="en")
    source_url: Optional[str] = Column(Text, nullable=True)
    metadata_json: Optional[dict] = Column(JSON, nullable=True)
    created_at: datetime = Column(DateTime(timezone=True), nullable=False, default=func.now())
    updated_at: datetime = Column(DateTime(timezone=True), nullable=False, default=func.now(), onupdate=func.now())


# Pydantic DTOs for API responses

class KnowledgeCategoryDTO(BaseModel):
    id: str
    name: str
    slug: str
    description: Optional[str] = None
    color: Optional[str] = None
    document_count: int = 0
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class KnowledgeDocumentDTO(BaseModel):
    id: str
    title: str
    slug: str
    content: str
    document_type: str
    category: Optional[str] = None
    tags: Optional[List[str]] = None
    status: str
    is_public: bool
    view_count: int
    word_count: Optional[int] = None
    language: str
    source_url: Optional[str] = None
    metadata_json: Optional[dict] = None
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class KnowledgeSearchResponse(BaseModel):
    total_hits: int
    hits: List[KnowledgeDocumentDTO]
    took_ms: int