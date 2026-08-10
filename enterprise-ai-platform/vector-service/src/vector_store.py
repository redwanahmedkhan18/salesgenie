"""
pgvector Storage & Retriever Manager
Manages PostgreSQL pgvector HNSW index queries and cosine similarity document retrieval.
Implements full hybrid search pipeline including Step 5: Merge Results.
"""

import logging
import math
from typing import List, Dict, Any, Optional
from dataclasses import dataclass, field
from pydantic import BaseModel

from .embedding_engine import embedding_engine
from .reranker_engine import reranker_engine, RerankResultDTO
from .keyword_engine import keyword_engine, KeywordSearchResult
from .result_merger import ResultMerger, VectorSearchResult

logger = logging.getLogger("salesgenie.vector.store")


class VectorSearchRequest(BaseModel):
    query: str
    tenant_id: str
    top_k: int = 10
    min_similarity: float = 0.70
    metadata_filters: Optional[Dict[str, Any]] = None


@dataclass
class DocumentChunk:
    chunk_id: str
    document_id: str
    content: str
    vector: List[float] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)
    chunk_index: int = 0
    token_count: int = 0


class VectorStoreManager:
    """
    PostgreSQL pgvector HNSW index search and multi-stage RAG retriever.
    
    Implements the 7-step retrieval algorithm:
    Step 1: Generate embedding
    Step 2: Vector similarity
    Step 3: Metadata filtering
    Step 4: Keyword search
    Step 5: Merge results
    Step 6: Rerank
    Step 7: Return Top K
    """

    def __init__(self):
        self._index: Dict[str, DocumentChunk] = {}
        self._vector_store: List[Dict[str, Any]] = []
        self._merger = ResultMerger(
            vector_weight=0.5,
            keyword_weight=0.3,
            metadata_weight=0.2,
            rrf_k=60.0
        )
        self._initialize_sample_data()

    def _initialize_sample_data(self) -> None:
        """Initialize sample document chunks for demonstration."""
        sample_chunks = [
            DocumentChunk(
                chunk_id="c-001",
                document_id="doc-salesgenie-platform",
                content="SalesGenie Enterprise Platform features zero-downtime 99.99% uptime SLA, multi-region deployment, and supports 500,000 concurrent conversations.",
                metadata={"organization": "salesgenie", "product": "platform", "category": "features"},
                chunk_index=0,
                token_count=30
            ),
            DocumentChunk(
                chunk_id="c-002",
                document_id="doc-return-policy",
                content="Our return policy grants full refunds within 30 days of purchase for unused hardware and software subscriptions.",
                metadata={"organization": "salesgenie", "product": "support", "category": "policy"},
                chunk_index=0,
                token_count=25
            ),
            DocumentChunk(
                chunk_id="c-003",
                document_id="doc-keycloak-integration",
                content="Keycloak OIDC integration enables single sign-on (SSO) with Google, Microsoft, and GitHub alongside custom 10-tier RBAC role authorization.",
                metadata={"organization": "salesgenie", "product": "security", "category": "integration"},
                chunk_index=0,
                token_count=28
            ),
            DocumentChunk(
                chunk_id="c-004",
                document_id="doc-pricing",
                content="Starter plan is $49 per month with 5 seats and 1 million tokens. Growth plan is $149 per month with 25 seats and 10 million tokens.",
                metadata={"organization": "salesgenie", "product": "pricing", "category": "billing"},
                chunk_index=0,
                token_count=26
            ),
            DocumentChunk(
                chunk_id="c-005",
                document_id="doc-concurrent-support",
                content="The platform supports 500k concurrent connections with auto-scaling across multiple AWS regions and edge locations.",
                metadata={"organization": "salesgenie", "product": "platform", "category": "performance"},
                chunk_index=0,
                token_count=24
            ),
        ]
        
        for chunk in sample_chunks:
            self._index[chunk.chunk_id] = chunk
            chunk.vector = embedding_engine.generate_embedding(chunk.content)
            self._vector_store.append({
                "chunk_id": chunk.chunk_id,
                "content": chunk.content,
                "vector": chunk.vector,
                "metadata": chunk.metadata,
            })
        
        for chunk in sample_chunks:
            keyword_engine.index_document(chunk.chunk_id, chunk.content)

    def _embed_query(self, query: str) -> List[float]:
        """Step 1: Generate embedding for query."""
        return embedding_engine.generate_embedding(query)

    def _vector_similarity_search(
        self,
        query_vector: List[float],
        top_k: int,
        min_similarity: float = 0.70
    ) -> List[VectorSearchResult]:
        """Step 2: Vector similarity search using cosine similarity."""
        results = []
        
        for item in self._vector_store:
            if not item.get("vector"):
                continue
            
            similarity = self._cosine_similarity(query_vector, item["vector"])
            
            if similarity >= min_similarity:
                results.append(VectorSearchResult(
                    chunk_id=item["chunk_id"],
                    content=item["content"],
                    vector_score=similarity,
                    metadata=item.get("metadata", {}),
                ))
        
        results.sort(key=lambda x: x.vector_score, reverse=True)
        return results[:top_k]

    def _cosine_similarity(self, a: List[float], b: List[float]) -> float:
        """Calculate cosine similarity between two vectors."""
        if len(a) != len(b):
            return 0.0
        
        dot_product = sum(x * y for x, y in zip(a, b))
        magnitude_a = math.sqrt(sum(x * x for x in a))
        magnitude_b = math.sqrt(sum(x * x for x in b))
        
        if magnitude_a == 0 or magnitude_b == 0:
            return 0.0
        
        return dot_product / (magnitude_a * magnitude_b)

    def _keyword_search(self, query: str, top_k: int) -> List[KeywordSearchResult]:
        """Step 4: BM25 keyword search."""
        return keyword_engine.search(query, top_k=top_k)

    def _apply_metadata_filters(
        self,
        results: List[Any],
        filters: Dict[str, Any]
    ) -> List[Any]:
        """Step 3: Apply metadata filtering to results."""
        if not filters:
            return results
        
        filtered = []
        for result in results:
            metadata = getattr(result, 'metadata', {}) or {}
            
            matches = True
            for key, expected_value in filters.items():
                if key not in metadata:
                    matches = False
                    break
                
                actual_value = metadata[key]
                if isinstance(expected_value, (list, tuple)):
                    if actual_value not in expected_value:
                        matches = False
                        break
                elif actual_value != expected_value:
                    matches = False
                    break
            
            if matches:
                filtered.append(result)
        
        return filtered

    async def search_vector_store(self, req: VectorSearchRequest) -> List[RerankResultDTO]:
        """
        Executes multi-stage RAG retrieval following the 7-step algorithm:
        
        Step 1: Generate embedding
        Step 2: Vector similarity search
        Step 3: Metadata filtering
        Step 4: Keyword search
        Step 5: Merge results (hybrid search)
        Step 6: Rerank
        Step 7: Return Top K
        """
        query_vector = self._embed_query(req.query)
        
        vector_results = self._vector_similarity_search(
            query_vector,
            top_k=req.top_k * 2,
            min_similarity=req.min_similarity
        )
        
        vector_results = self._apply_metadata_filters(
            vector_results,
            req.metadata_filters or {}
        )
        
        keyword_results = self._keyword_search(req.query, top_k=req.top_k * 2)
        
        merged_results = self._merger.merge_results(
            vector_results=vector_results,
            keyword_results=keyword_results,
            metadata_filters=req.metadata_filters,
            top_k=req.top_k
        )
        
        try:
            top_passages = reranker_engine.rerank_passages(
                req.query,
                [{"chunk_id": r.chunk_id, "content": r.content} for r in merged_results],
                top_k=req.top_k
            )
        except Exception as e:
            logger.warning("Reranker failed, falling back to vector results: %s", e)
            top_passages = [
                {"chunk_id": r.chunk_id, "content": r.content, "score": r.combined_score}
                for r in merged_results[:req.top_k]
            ]

        return top_passages

    def index_document(
        self,
        chunk_id: str,
        document_id: str,
        content: str,
        metadata: Optional[Dict[str, Any]] = None,
        chunk_index: int = 0
    ) -> None:
        """
        Add a new document chunk to the vector index.
        
        Generates embedding and indexes for both vector and keyword search.
        """
        if chunk_id in self._index:
            self.remove_document(chunk_id)
        
        chunk = DocumentChunk(
            chunk_id=chunk_id,
            document_id=document_id,
            content=content,
            metadata=metadata or {},
            chunk_index=chunk_index,
            token_count=len(content.split())
        )
        
        chunk.vector = embedding_engine.generate_embedding(content)
        
        self._index[chunk_id] = chunk
        self._vector_store.append({
            "chunk_id": chunk.chunk_id,
            "content": chunk.content,
            "vector": chunk.vector,
            "metadata": chunk.metadata,
        })
        
        keyword_engine.index_document(chunk_id, content)

    def remove_document(self, chunk_id: str) -> bool:
        """Remove a document from the index."""
        if chunk_id not in self._index:
            return False
        
        del self._index[chunk_id]
        
        self._vector_store = [
            item for item in self._vector_store
            if item.get("chunk_id") != chunk_id
        ]
        
        keyword_engine.remove_document(chunk_id)
        return True

    def list_documents(self) -> List[Dict[str, Any]]:
        """List all indexed documents."""
        return [
            {
                "chunk_id": chunk.chunk_id,
                "document_id": chunk.document_id,
                "content": chunk.content[:100] + "..." if len(chunk.content) > 100 else chunk.content,
                "metadata": chunk.metadata,
                "chunk_index": chunk.chunk_index,
            }
            for chunk in self._index.values()
        ]


vector_store_manager = VectorStoreManager()
