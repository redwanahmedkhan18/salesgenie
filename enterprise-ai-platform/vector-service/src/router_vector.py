"""
Vector Service API Router
Endpoints for BAAI bge-m3 embedding generation, pgvector semantic search, and passage re-ranking.
Implements full hybrid search pipeline with Step 5: Merge Results.
"""

from typing import List, Dict, Any, Optional
from pydantic import BaseModel
from fastapi import APIRouter, Depends, HTTPException, status

from enterprise_ai_platform.common.security_rbac import (
    get_current_user,
    TokenPayload,
    RequirePermissions,
    Permission,
)
from .embedding_engine import embedding_engine
from .reranker_engine import reranker_engine, RerankResultDTO
from .keyword_engine import keyword_engine
from .vector_store import vector_store_manager, VectorSearchRequest

router = APIRouter(prefix="/api/v1/vector", tags=["Vector Search & RAG Embeddings"])


class EmbedRequest(BaseModel):
    text: str


class EmbedResponse(BaseModel):
    dimension: int
    vector: List[float]


class HybridSearchRequest(BaseModel):
    query: str
    top_k: int = 5
    min_similarity: float = 0.70
    metadata_filters: Optional[Dict[str, Any]] = None


class HybridSearchResponse(BaseModel):
    results: List[RerankResultDTO]
    total_results: int


class RerankRequest(BaseModel):
    query: str
    documents: List[Dict[str, Any]]
    top_k: int = 5


class IndexRebuildRequest(BaseModel):
    tenant_id: Optional[str] = None


class IndexDocumentRequest(BaseModel):
    chunk_id: str
    document_id: str
    content: str
    metadata: Optional[Dict[str, Any]] = None
    chunk_index: int = 0


class IndexDocumentResponse(BaseModel):
    chunk_id: str
    document_id: str
    status: str


@router.get(
    "/index",
    response_model=List[Dict[str, Any]],
    summary="List All Indexed Documents",
    dependencies=[Depends(RequirePermissions(Permission.KNOWLEDGE_READ))],
)
async def list_documents():
    """List all indexed document chunks."""
    return vector_store_manager.list_documents()


@router.post(
    "/index",
    response_model=IndexDocumentResponse,
    summary="Index a New Document Chunk",
    dependencies=[Depends(RequirePermissions(Permission.KNOWLEDGE_WRITE))],
)
async def index_document(req: IndexDocumentRequest):
    """Add a new document chunk to the vector index."""
    vector_store_manager.index_document(
        chunk_id=req.chunk_id,
        document_id=req.document_id,
        content=req.content,
        metadata=req.metadata,
        chunk_index=req.chunk_index
    )
    return IndexDocumentResponse(
        chunk_id=req.chunk_id,
        document_id=req.document_id,
        status="indexed"
    )


@router.post("/embed", response_model=EmbedResponse, summary="Generate BAAI bge-m3 Embedding")
async def generate_embedding(req: EmbedRequest):
    """Generate 1024-dimensional dense vector embedding for query text."""
    vector = embedding_engine.generate_embedding(req.text)
    return EmbedResponse(dimension=len(vector), vector=vector)


@router.post(
    "/search",
    response_model=List[RerankResultDTO],
    summary="Semantic Vector Search & Re-ranking",
    dependencies=[Depends(RequirePermissions(Permission.KNOWLEDGE_READ))],
)
async def vector_search(req: VectorSearchRequest):
    """Execute vector cosine retrieval and BAAI passage re-ranking."""
    results = await vector_store_manager.search_vector_store(req)
    return results


@router.post(
    "/search/hybrid",
    response_model=HybridSearchResponse,
    summary="Hybrid Search: Vector + Keyword + Metadata Fusion",
    dependencies=[Depends(RequirePermissions(Permission.KNOWLEDGE_READ))],
)
async def hybrid_search(req: HybridSearchRequest):
    """
    Execute hybrid search combining:
    - Vector similarity (semantic)
    - Keyword search (BM25)
    - Metadata filtering
    
    Step 5: Results are merged using Reciprocal Rank Fusion (RRF)
    """
    search_req = VectorSearchRequest(
        query=req.query,
        tenant_id="default",
        top_k=req.top_k,
        min_similarity=req.min_similarity,
        metadata_filters=req.metadata_filters
    )
    results = await vector_store_manager.search_vector_store(search_req)
    return HybridSearchResponse(results=results, total_results=len(results))


@router.post(
    "/rerank",
    response_model=List[RerankResultDTO],
    summary="Cross-Encoder Re-ranking",
    dependencies=[Depends(RequirePermissions(Permission.KNOWLEDGE_READ))],
)
async def rerank(req: RerankRequest):
    """
    Execute cross-encoder re-ranking on provided documents.
    
    Step 6: Rerank using BAAI cross-encoder model
    """
    results = reranker_engine.rerank_passages(req.query, req.documents, top_k=req.top_k)
    return results


@router.delete(
    "/index/{chunk_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete Document from Index",
    dependencies=[Depends(RequirePermissions(Permission.KNOWLEDGE_WRITE))],
)
async def delete_from_index(chunk_id: str):
    """Delete a document chunk from the vector index."""
    if chunk_id in vector_store_manager._index:
        del vector_store_manager._index[chunk_id]
        vector_store_manager._vector_store = [
            item for item in vector_store_manager._vector_store
            if item.get("chunk_id") != chunk_id
        ]
        keyword_engine.remove_document(chunk_id)
        return None
    raise HTTPException(status_code=404, detail=f"Chunk {chunk_id} not found")


@router.post(
    "/rebuild",
    response_model=Dict[str, Any],
    summary="Rebuild Vector Index",
    dependencies=[Depends(RequirePermissions(Permission.KNOWLEDGE_ADMIN))],
)
async def rebuild_index(req: IndexRebuildRequest = IndexRebuildRequest()):
    """
    Rebuild the vector index from scratch.
    Used for maintenance and re-indexing operations.
    """
    vector_store_manager._index.clear()
    vector_store_manager._vector_store.clear()
    vector_store_manager._initialize_sample_data()
    return {"status": "rebuilt", "tenant_id": req.tenant_id or "default"}
