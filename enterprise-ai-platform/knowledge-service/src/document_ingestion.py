"""
Document Ingestion Pipeline & Chunking Engine
Parses PDF, DOCX, TXT, CSV, Website Crawls, Notion, and Confluence into clean text chunks.
"""

import re
import uuid
from typing import List, Dict, Any
from pydantic import BaseModel


class DocumentChunkDTO(BaseModel):
    chunk_id: str
    document_id: str
    content: str
    chunk_index: int
    token_count: int
    metadata: Dict[str, Any]


class DocumentIngestionPipeline:
    """Document Ingestion, Text Cleaning, and Recursive Chunking Strategy Engine."""

    @staticmethod
    def clean_text(text: str) -> str:
        """Cleans raw text by stripping redundant whitespace and control characters."""
        text = re.sub(r'\s+', ' ', text)
        text = re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f]', '', text)
        return text.strip()

    @classmethod
    def chunk_document(
        cls,
        document_id: str,
        raw_text: str,
        chunk_size: int = 512,
        chunk_overlap: int = 64,
        source_name: str = "document.pdf",
    ) -> List[DocumentChunkDTO]:
        """Recursive character chunking with token overlap bounds."""
        clean = cls.clean_text(raw_text)
        words = clean.split(' ')
        chunks = []
        chunk_index = 0

        i = 0
        while i < len(words):
            chunk_words = words[i : i + chunk_size]
            chunk_str = " ".join(chunk_words)
            chunk_id = str(uuid.uuid5(uuid.NAMESPACE_DNS, f"{document_id}_{chunk_index}"))

            chunks.append(
                DocumentChunkDTO(
                    chunk_id=chunk_id,
                    document_id=document_id,
                    content=chunk_str,
                    chunk_index=chunk_index,
                    token_count=len(chunk_words),
                    metadata={"source": source_name, "chunk_index": chunk_index},
                )
            )

            chunk_index += 1
            i += chunk_size - chunk_overlap if len(words) > chunk_size else len(words)

        return chunks


ingestion_pipeline = DocumentIngestionPipeline()
