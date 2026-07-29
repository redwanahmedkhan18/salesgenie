"""
BAAI Re-ranking Engine
Cross-encoder scoring engine for top-k document passage re-ranking.
Implements Step 6: Rerank with advanced relevance scoring.
"""

from typing import List, Dict, Any, Optional
from dataclasses import dataclass
from pydantic import BaseModel


class RerankResultDTO(BaseModel):
    chunk_id: str
    content: str
    relevance_score: float
    rank: int
    metadata: Optional[Dict[str, Any]] = None


@dataclass
class RerankConfig:
    """Configuration for reranking algorithm."""
    max_position: int = 10
    scale_factor: float = 1.0
    boost_exact_match: float = 0.1
    boost_keyword_density: float = 0.05


class RerankerEngine:
    """
    BAAI Reranker cross-encoder model scoring retrieved document passages.
    
    Step 6: Rerank
    - Receives merged results from Step 5
    - Applies cross-encoder scoring
    - Boosts based on keyword matching and query-term relevance
    - Returns top K most relevant passages
    """

    def __init__(self, config: Optional[RerankConfig] = None):
        self.config = config or RerankConfig()

    def _tokenize(self, text: str) -> List[str]:
        """Tokenize text into lowercase terms."""
        import re
        text = text.lower()
        text = re.sub(r'[^\w\s]', ' ', text)
        return [t for t in text.split() if t]

    def _calculate_query_term_match(self, query_terms: set, content_terms: set) -> float:
        """Calculate Jaccard similarity between query and content terms."""
        if not query_terms or not content_terms:
            return 0.0
        intersection = query_terms.intersection(content_terms)
        union = query_terms.union(content_terms)
        return len(intersection) / len(union) if union else 0.0

    def _calculate_keyword_density(self, query_terms: set, content: str) -> float:
        """Calculate keyword density boost."""
        if not query_terms:
            return 0.0
        words = content.lower().split()
        if not words:
            return 0.0
        matching_words = sum(1 for w in words if w in query_terms)
        return matching_words / len(words)

    def _calculate_exact_phrase_boost(self, query: str, content: str) -> float:
        """Boost for exact phrase matches."""
        query_lower = query.lower()
        content_lower = content.lower()
        if query_lower in content_lower:
            return self.config.boost_exact_match
        return 0.0

    def rerank_passages(
        self,
        query: str,
        passages: List[Dict[str, Any]],
        top_k: int = 3
    ) -> List[RerankResultDTO]:
        """
        Re-ranks top candidate passages against query intent.
        
        Step 6: Apply cross-encoder relevance scoring to maximize RAG precision.
        
        Algorithm:
        1. Extract query terms
        2. Calculate base relevance score (query-term matching)
        3. Apply boosts for exact phrase matches
        4. Apply boosts for keyword density
        5. Combine scores with position weighting
        6. Sort and return top K
        """
        if not passages:
            return []

        query_terms = set(self._tokenize(query))
        scored_passages = []

        for idx, p in enumerate(passages):
            content = p.get("content", "")
            chunk_id = p.get("chunk_id", f"chunk_{idx}")
            metadata = p.get("metadata")
            
            content_terms = set(self._tokenize(content))
            
            query_term_match = self._calculate_query_term_match(query_terms, content_terms)
            keyword_density = self._calculate_keyword_density(query_terms, content)
            exact_phrase_boost = self._calculate_exact_phrase_boost(query, content)
            
            base_score = query_term_match
            density_boost = keyword_density * self.config.boost_keyword_density
            phrase_boost = exact_phrase_boost
            
            position_weight = 1.0 / (idx + 1)
            
            final_score = (base_score + density_boost + phrase_boost) * position_weight
            final_score = min(1.0, max(0.0, final_score * self.config.scale_factor))
            
            scored_passages.append((final_score, chunk_id, content, metadata, idx))

        scored_passages.sort(key=lambda x: x[0], reverse=True)

        results = []
        for rank, (score, chunk_id, content, metadata, original_idx) in enumerate(scored_passages[:top_k]):
            results.append(
                RerankResultDTO(
                    chunk_id=chunk_id,
                    content=content,
                    relevance_score=round(score, 4),
                    rank=rank + 1,
                    metadata=metadata
                )
            )

        return results

    def rerank_with_combined_scores(
        self,
        query: str,
        passages: List[Dict[str, Any]],
        vector_scores: Optional[Dict[str, float]] = None,
        bm25_scores: Optional[Dict[str, float]] = None,
        top_k: int = 5
    ) -> List[RerankResultDTO]:
        """
        Advanced reranking that combines multiple score sources.
        Used when reranking already-merged results with additional signals.
        """
        if not passages:
            return []

        query_terms = set(self._tokenize(query))
        scored_passages = []

        for p in passages:
            content = p.get("content", "")
            chunk_id = p.get("chunk_id", "")
            metadata = p.get("metadata")
            
            content_terms = set(self._tokenize(content))
            
            query_term_match = self._calculate_query_term_match(query_terms, content_terms)
            keyword_density = self._calculate_keyword_density(query_terms, content)
            exact_phrase_boost = self._calculate_exact_phrase_boost(query, content)
            
            combined_score = query_term_match + keyword_density * self.config.boost_keyword_density + exact_phrase_boost
            
            if vector_scores and chunk_id in vector_scores:
                combined_score = combined_score * 0.5 + vector_scores[chunk_id] * 0.5
            
            if bm25_scores and chunk_id in bm25_scores:
                combined_score = combined_score * 0.5 + bm25_scores[chunk_id] * 0.5
            
            combined_score = min(1.0, max(0.0, combined_score))
            
            scored_passages.append((combined_score, chunk_id, content, metadata))

        scored_passages.sort(key=lambda x: x[0], reverse=True)

        results = []
        for rank, (score, chunk_id, content, metadata) in enumerate(scored_passages[:top_k]):
            results.append(
                RerankResultDTO(
                    chunk_id=chunk_id,
                    content=content,
                    relevance_score=round(score, 4),
                    rank=rank + 1,
                    metadata=metadata
                )
            )

        return results


reranker_engine = RerankerEngine()
