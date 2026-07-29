"""
Result Merger Engine (Step 5)
Merges results from vector search, keyword search, and metadata filtering
for hybrid search with proper score normalization and ranking.
"""

from typing import List, Dict, Any, Optional
from dataclasses import dataclass, field

from .reranker_engine import RerankResultDTO


@dataclass
class VectorSearchResult:
    chunk_id: str
    content: str
    vector_score: float
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class KeywordSearchResult:
    chunk_id: str
    content: str
    bm25_score: float
    term_frequencies: Dict[str, int] = field(default_factory=dict)


@dataclass
class MergedResult:
    chunk_id: str
    content: str
    vector_score: float = 0.0
    bm25_score: float = 0.0
    metadata_score: float = 0.0
    combined_score: float = 0.0
    source: str = ""
    metadata: Dict[str, Any] = field(default_factory=dict)


class ResultMerger:
    """
    Merges results from multiple retrieval strategies using Reciprocal Rank Fusion (RRF)
    and weighted scoring for hybrid search.
    
    Step 5: Merge results
    - Combines vector similarity results
    - Combines keyword (BM25) search results  
    - Applies metadata filtering scores
    - Normalizes and ranks combined results
    """

    def __init__(
        self,
        vector_weight: float = 0.5,
        keyword_weight: float = 0.3,
        metadata_weight: float = 0.2,
        rrf_k: float = 60.0
    ):
        self.vector_weight = vector_weight
        self.keyword_weight = keyword_weight
        self.metadata_weight = metadata_weight
        self.rrf_k = rrf_k

    def _normalize_score(self, score: float, min_val: float = 0.0, max_val: float = 1.0) -> float:
        """Normalize score to 0-1 range."""
        if max_val <= min_val:
            return 0.0
        return max(0.0, min(1.0, (score - min_val) / (max_val - min_val)))

    def _calculate_rrf_score(self, rank: int) -> float:
        """
        Calculate Reciprocal Rank Fusion score.
        RRF = 1 / (k + rank) where rank is 1-indexed position
        """
        return 1.0 / (self.rrf_k + rank)

    def merge_results(
        self,
        vector_results: List[VectorSearchResult],
        keyword_results: List[KeywordSearchResult],
        metadata_filters: Optional[Dict[str, Any]] = None,
        top_k: int = 10
    ) -> List[MergedResult]:
        """
        Merge results from vector and keyword search using hybrid scoring.
        
        Algorithm:
        1. Combine all unique chunk_ids from both result sets
        2. Calculate RRF scores for ranking
        3. Apply weighted scoring based on source
        4. Apply metadata filter scores if provided
        5. Sort by combined score
        6. Return top_k results
        """
        if not vector_results and not keyword_results:
            return []

        merged: Dict[str, MergedResult] = {}
        
        vector_scores = {r.chunk_id: r for r in vector_results}
        keyword_scores = {r.chunk_id: r for r in keyword_results}
        
        all_chunk_ids = set(vector_scores.keys()) | set(keyword_scores.keys())
        
        vector_ranks = {cid: rank for rank, cid in enumerate(vector_scores.keys(), 1)}
        keyword_ranks = {cid: rank for rank, cid in enumerate(keyword_scores.keys(), 1)}

        for chunk_id in all_chunk_ids:
            result = MergedResult(
                chunk_id=chunk_id,
                content="",
                metadata={}
            )

            if chunk_id in vector_scores:
                v_result = vector_scores[chunk_id]
                result.vector_score = v_result.vector_score
                result.content = v_result.content
                result.metadata = v_result.metadata
                result.source = "vector"
            elif chunk_id in keyword_scores:
                k_result = keyword_scores[chunk_id]
                result.bm25_score = k_result.bm25_score
                result.content = k_result.content
                result.source = "keyword"

            if chunk_id in keyword_scores:
                k_result = keyword_scores[chunk_id]
                result.bm25_score = k_result.bm25_score
                result.content = result.content or k_result.content

            if chunk_id in vector_scores:
                v_result = vector_scores[chunk_id]
                result.vector_score = v_result.vector_score
                result.content = result.content or v_result.content
                result.metadata = result.metadata or v_result.metadata

            vector_rank = vector_ranks.get(chunk_id, len(vector_results) + 1)
            keyword_rank = keyword_ranks.get(chunk_id, len(keyword_results) + 1)
            
            vector_rrf = self._calculate_rrf_score(vector_rank)
            keyword_rrf = self._calculate_rrf_score(keyword_rank)

            combined = 0.0
            if chunk_id in vector_scores:
                combined += self.vector_weight * vector_rrf
            if chunk_id in keyword_scores:
                combined += self.keyword_weight * keyword_rrf

            if metadata_filters:
                metadata_score = self._calculate_metadata_score(
                    result.metadata, metadata_filters
                )
                result.metadata_score = metadata_score
                combined += self.metadata_weight * metadata_score

            result.combined_score = combined

            merged[chunk_id] = result

        sorted_results = sorted(
            merged.values(),
            key=lambda x: x.combined_score,
            reverse=True
        )

        return sorted_results[:top_k]

    def _calculate_metadata_score(
        self,
        metadata: Dict[str, Any],
        filters: Dict[str, Any]
    ) -> float:
        """
        Calculate score based on metadata filter matching.
        Returns 0.0 to 1.0 score indicating filter match quality.
        """
        if not metadata or not filters:
            return 1.0

        score = 0.0
        total_filters = len(filters)

        for key, expected_value in filters.items():
            if key not in metadata:
                continue
            
            actual_value = metadata[key]
            
            if isinstance(expected_value, (list, tuple)):
                if actual_value in expected_value:
                    score += 1.0
            elif actual_value == expected_value:
                score += 1.0
            elif isinstance(actual_value, str) and isinstance(expected_value, str):
                if expected_value.lower() in actual_value.lower():
                    score += 0.5

        return score / total_filters if total_filters > 0 else 1.0

    def merge_to_rerank_dto(
        self,
        merged_results: List[MergedResult]
    ) -> List[RerankResultDTO]:
        """Convert merged results to RerankResultDTO format for downstream processing."""
        return [
            RerankResultDTO(
                chunk_id=r.chunk_id,
                content=r.content,
                relevance_score=r.combined_score,
                rank=i + 1
            )
            for i, r in enumerate(merged_results)
        ]


merger = ResultMerger()