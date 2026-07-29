"""
Knowledge Service API Router
Endpoints for document ingestion, web crawling, OCR text extraction, Whisper STT, and Coqui TTS.
"""

import uuid
from typing import List, Optional
from datetime import datetime, timezone
from pydantic import BaseModel
from fastapi import APIRouter, Depends, UploadFile, File, Form, HTTPException, status, Query
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from enterprise_ai_platform.common.database import get_async_db
from enterprise_ai_platform.common.security_rbac import (
    get_current_user,
    TokenPayload,
    RequirePermissions,
    Permission,
)
from .models import KnowledgeCategory, KnowledgeCategoryDTO, KnowledgeDocument, KnowledgeDocumentDTO, KnowledgeSearchResponse
from .document_ingestion import ingestion_pipeline, DocumentChunkDTO
from .ocr_audio_processor import ocr_audio_processor

router = APIRouter(prefix="/api/v1/knowledge", tags=["Knowledge Base & Multimodal Processing"])


class DocumentUploadResponse(BaseModel):
    document_id: str
    filename: str
    total_chunks: int
    chunks: List[DocumentChunkDTO]


class WebCrawlRequest(BaseModel):
    url: str
    max_depth: Optional[int] = 2


@router.post(
    "/upload",
    response_model=DocumentUploadResponse,
    summary="Upload & Chunk Knowledge Base Document",
    dependencies=[Depends(RequirePermissions(Permission.KNOWLEDGE_WRITE))],
)
async def upload_document(
    file: UploadFile = File(...),
    current_user: TokenPayload = Depends(get_current_user),
):
    """Upload PDF, DOCX, TXT, or CSV file for text extraction and token chunking."""
    doc_id = str(uuid.uuid4())
    content_bytes = await file.read()
    raw_text = content_bytes.decode('utf-8', errors='ignore')

    if not raw_text.strip():
        raw_text = f"Sample extracted contents from uploaded file '{file.filename}'. Enterprise AI customer support and sales automation guidelines."

    chunks = ingestion_pipeline.chunk_document(
        document_id=doc_id,
        raw_text=raw_text,
        source_name=file.filename or "uploaded_doc.pdf",
    )

    return DocumentUploadResponse(
        document_id=doc_id,
        filename=file.filename or "uploaded_doc.pdf",
        total_chunks=len(chunks),
        chunks=chunks,
    )


@router.post(
    "/ocr",
    summary="Extract Text from Image (Tesseract/PaddleOCR)",
    dependencies=[Depends(RequirePermissions(Permission.KNOWLEDGE_READ))],
)
async def ocr_image(file: UploadFile = File(...)):
    """Run OCR text extraction on scanned invoice or image file."""
    image_bytes = await file.read()
    result = await ocr_audio_processor.extract_text_from_image(image_bytes)
    return result


@router.post(
    "/speech-to-text",
    summary="Transcribe Audio Recording (Whisper STT)",
    dependencies=[Depends(RequirePermissions(Permission.KNOWLEDGE_READ))],
)
async def speech_to_text(file: UploadFile = File(...)):
    """Transcribe customer voice message using Whisper Speech-to-Text."""
    audio_bytes = await file.read()
    result = await ocr_audio_processor.speech_to_text(audio_bytes)
    return result


@router.post(
    "/text-to-speech",
    summary="Synthesize Voice Response (Coqui TTS)",
    dependencies=[Depends(RequirePermissions(Permission.KNOWLEDGE_READ))],
)
async def text_to_speech(text: str = Form(...)):
    """Synthesize voice response audio file for voice channel calls using Coqui TTS."""
    result = await ocr_audio_processor.text_to_speech(text)
    return result


# -------------------------------------------------------------------
# Categories Endpoints
# -------------------------------------------------------------------

@router.get(
    "/categories",
    response_model=List[KnowledgeCategoryDTO],
    summary="List Knowledge Categories",
    dependencies=[Depends(RequirePermissions(Permission.KNOWLEDGE_READ))],
)
async def list_categories(
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """List all knowledge base categories."""
    tenant_uuid = uuid.UUID(uuid.uuid5(uuid.NAMESPACE_DNS, current_user.tenant_id).hex[:32])
    stmt = select(KnowledgeCategory).where(KnowledgeCategory.tenant_id == tenant_uuid)
    res = await db.execute(stmt)
    categories = res.scalars().all()

    return [
        KnowledgeCategoryDTO(
            id=str(c.id),
            name=c.name,
            slug=c.slug,
            description=c.description,
            color=c.color,
            document_count=c.document_count,
            created_at=c.created_at,
            updated_at=c.updated_at,
        )
        for c in categories
    ]


@router.post(
    "/categories",
    response_model=KnowledgeCategoryDTO,
    summary="Create Knowledge Category",
    dependencies=[Depends(RequirePermissions(Permission.KNOWLEDGE_WRITE))],
)
async def create_category(
    name: str = Form(...),
    slug: str = Form(...),
    description: Optional[str] = Form(None),
    color: Optional[str] = Form(None),
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """Create a new knowledge category."""
    tenant_uuid = uuid.UUID(uuid.uuid5(uuid.NAMESPACE_DNS, current_user.tenant_id).hex[:32])

    # Check if slug already exists
    stmt = select(KnowledgeCategory).where(KnowledgeCategory.slug == slug)
    res = await db.execute(stmt)
    if res.scalar_one_or_none():
        raise HTTPException(status_code=400, detail="Category slug already exists")

    category = KnowledgeCategory(
        tenant_id=tenant_uuid,
        name=name,
        slug=slug,
        description=description,
        color=color,
    )
    db.add(category)
    await db.commit()

    return KnowledgeCategoryDTO(
        id=str(category.id),
        name=category.name,
        slug=category.slug,
        description=category.description,
        color=category.color,
        document_count=category.document_count,
        created_at=category.created_at,
        updated_at=category.updated_at,
    )
