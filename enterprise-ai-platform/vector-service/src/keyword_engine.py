"""
Keyword Search Engine (BM25)
Implements text-based keyword search for hybrid retrieval.
"""

import re
from typing import List, Dict, Any, Optional
from dataclasses import dataclass
from pydantic import BaseModel


class KeywordSearchResult(BaseModel):
    chunk_id: str
    content: str
    bm25_score: float
    term_frequencies: Dict[str, int]


class KeywordSearchEngine:
    """BM25-style keyword search engine for hybrid retrieval."""

    def __init__(self, k1: float = 1.5, b: float = 0.75):
        self.k1 = k1
        self.b = b
        self._documents: Dict[str, Dict[str, Any]] = {}
        self._doc_lengths: Dict[str, int] = {}
        self._avg_doc_length: float = 0.0
        self._term_doc_freq: Dict[str, int] = {}

    def index_document(self, chunk_id: str, content: str) -> None:
        """Index a document for keyword search."""
        terms = self._tokenize(content)
        self._documents[chunk_id] = {
            "content": content,
            "terms": terms,
            "length": len(terms),
        }
        self._doc_lengths[chunk_id] = len(terms)
        
        for term in terms:
            self._term_doc_freq[term] = self._term_doc_freq.get(term, 0) + 1
        
        if self._documents:
            self._avg_doc_length = sum(self._doc_lengths.values()) / len(self._doc_lengths)

    def _tokenize(self, text: str) -> List[str]:
        """Tokenize text into lowercase terms."""
        text = text.lower()
        text = re.sub(r'[^\w\s]', ' ', text)
        return [t for t in text.split() if t]

    def _calculate_bm25_score(self, chunk_id: str, query_terms: List[str]) -> float:
        """Calculate BM25 score for a document against query terms."""
        if chunk_id not in self._documents:
            return 0.0
        
        doc = self._documents[chunk_id]
        doc_len = doc["length"]
        terms = doc["terms"]
        term_freqs: Dict[str, int] = {}
        
        for term in terms:
            term_freqs[term] = term_freqs.get(term, 0) + 1
        
        score = 0.0
        n = len(self._documents)
        avgdl = self._avg_doc_length if self._avg_doc_length > 0 else 1.0
        
        for term in query_terms:
            if term in term_freqs:
                f = term_freqs[term]
                n_q = self._term_doc_freq.get(term, 0)
                
                if n_q > 0:
                    idf = ((n - n_q + 0.5) / (n_q + 0.5))
                    idf = max(0.0, idf)
                    term_score = (f * (self.k1 + 1)) / (f + self.k1 * (1 - self.b + self.b * doc_len / avgdl))
                    score += idf * term_score
        
        return score

    def search(self, query: str, top_k: int = 10) -> List[KeywordSearchResult]:
        """Execute BM25 keyword search."""
        query_terms = self._tokenize(query)
        if not query_terms or not self._documents:
            return []
        
        scores = []
        for chunk_id in self._documents:
            score = self._calculate_bm25_score(chunk_id, query_terms)
            if score > 0:
                content = self._documents[chunk_id]["content"]
                term_freqs = {t: self._documents[chunk_id]["terms"].count(t) for t in set(query_terms) if t in self._documents[chunk_id]["terms"]}
                scores.append(KeywordSearchResult(
                    chunk_id=chunk_id,
                    content=content,
                    bm25_score=score,
                    term_frequencies=term_freqs,
                ))
        
        scores.sort(key=lambda x: x.bm25_score, reverse=True)
        return scores[:top_k]

    def update_document(self, chunk_id: str, content: str) -> None:
        """Update an existing document in the index."""
        if chunk_id in self._documents:
            old_terms = self._documents[chunk_id]["terms"]
            for term in old_terms:
                self._term_doc_freq[term] -= 1
        
        self.index_document(chunk_id, content)

    def remove_document(self, chunk_id: str) -> None:
        """Remove a document from the index."""
        if chunk_id in self._documents:
            old_terms = self._documents[chunk_id]["terms"]
            for term in old_terms:
                self._term_doc_freq[term] -= 1
            
            del self._documents[chunk_id]
            del self._doc_lengths[chunk_id]
            
            if self._documents:
                self._avg_doc_length = sum(self._doc_lengths.values()) / len(self._doc_lengths)


keyword_engine = KeywordSearchEngine()