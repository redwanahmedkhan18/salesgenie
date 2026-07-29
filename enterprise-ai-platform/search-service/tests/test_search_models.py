"""
Unit Tests for Search Service Models
"""

import pytest
import uuid
from unittest.mock import MagicMock

from search_service.src.models import (
    SearchIndex,
    SearchHitDTO,
    SearchResponseDTO,
    IndexDocumentRequest,
    IndexDocumentResponse,
    BulkIndexRequest,
    SearchRequest,
    IndexStatsDTO,
    IndexSettingsDTO,
    SearchIndexType,
)


class TestSearchIndexType:
    def test_search_index_type_values(self):
        assert SearchIndexType.DOCUMENT == "document"
        assert SearchIndexType.CUSTOMER == "customer"
        assert SearchIndexType.TICKET == "ticket"
        assert SearchIndexType.CONVERSATION == "conversation"
        assert SearchIndexType.KNOWLEDGE_BASE == "knowledge_base"


class TestIndexDocumentRequest:
    def test_index_document_defaults(self):
        req = IndexDocumentRequest(
            index_type="document",
            document_id="doc_123",
            title="Test Document",
            content="Test content",
        )
        assert req.index_type == "document"
        assert req.document_id == "doc_123"
        assert req.is_public is False
        assert req.tags is None
        assert req.metadata is None

    def test_index_document_with_values(self):
        req = IndexDocumentRequest(
            index_type="knowledge_base",
            document_id="kb_456",
            title="Policy Document",
            content="Full policy content here",
            tags=["policy", "important"],
            metadata={"category": "hr", "version": "2.0"},
            is_public=True,
        )
        assert req.tags == ["policy", "important"]
        assert req.metadata == {"category": "hr", "version": "2.0"}
        assert req.is_public is True


class TestSearchRequest:
    def test_search_request_defaults(self):
        req = SearchRequest(query="test query")
        assert req.query == "test query"
        assert req.size == 10
        assert req.from_ == 0
        assert req.sort_by == "score"
        assert req.sort_order == "desc"
        assert req.highlight is True

    def test_search_request_with_values(self):
        req = SearchRequest(
            query="important document",
            index_types=["document", "knowledge_base"],
            tags=["policy"],
            size=20,
            from_=10,
            sort_by="date",
            sort_order="asc",
            highlight=False,
        )
        assert req.index_types == ["document", "knowledge_base"]
        assert req.tags == ["policy"]
        assert req.size == 20
        assert req.from_ == 10
        assert req.sort_by == "date"
        assert req.sort_order == "asc"
        assert req.highlight is False


class TestBulkIndexRequest:
    def test_bulk_index_request(self):
        req = BulkIndexRequest(
            documents=[
                IndexDocumentRequest(
                    index_type="document",
                    document_id="doc_1",
                    title="Doc 1",
                    content="Content 1",
                ),
                IndexDocumentRequest(
                    index_type="document",
                    document_id="doc_2",
                    title="Doc 2",
                    content="Content 2",
                ),
            ]
        )
        assert len(req.documents) == 2
        assert req.documents[0].document_id == "doc_1"
        assert req.documents[1].document_id == "doc_2"


class TestSearchHitDTO:
    def test_search_hit_dto(self):
        dto = SearchHitDTO(
            id="search_1",
            index_type="document",
            document_id="doc_123",
            title="Test Document",
            content="Test content here",
            tags=["important"],
            metadata={"category": "test"},
            score=0.95,
            highlights={"content": ["<em>Test</em> content here"]},
        )
        assert dto.id == "search_1"
        assert dto.index_type == "document"
        assert dto.document_id == "doc_123"
        assert dto.score == 0.95
        assert dto.highlights == {"content": ["<em>Test</em> content here"]}


class TestSearchResponseDTO:
    def test_search_response_dto(self):
        hit = SearchHitDTO(
            id="search_1",
            index_type="document",
            document_id="doc_123",
            title="Test",
            content="Content",
            score=0.95,
        )
        dto = SearchResponseDTO(
            query="test",
            total_hits=1,
            hits=[hit],
            took_ms=15,
        )
        assert dto.query == "test"
        assert dto.total_hits == 1
        assert len(dto.hits) == 1
        assert dto.took_ms == 15


class TestIndexStatsDTO:
    def test_index_stats_dto(self):
        from datetime import datetime
        dto = IndexStatsDTO(
            index_type="document",
            document_count=150,
            last_updated=datetime.now(),
        )
        assert dto.index_type == "document"
        assert dto.document_count == 150


class TestIndexSettingsDTO:
    def test_index_settings_dto(self):
        dto = IndexSettingsDTO(
            index_name="sg_tenant_documents",
            document_count=150,
            health="green",
            settings={"number_of_shards": 1, "number_of_replicas": 1},
        )
        assert dto.index_name == "sg_tenant_documents"
        assert dto.health == "green"
        assert dto.settings["number_of_shards"] == 1