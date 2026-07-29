"""
Unit Tests for File Service Models
"""

import pytest
import uuid
from datetime import datetime
from unittest.mock import MagicMock

from file_service.src.models import (
    FileMetadata,
    FileMetadataDTO,
    FileUploadResponse,
    FileDownloadResponse,
    FileSearchRequest,
    FileSearchResponse,
    FileStatsDTO,
    FileOverviewDTO,
    FileVersionDTO,
    FileShareRequest,
    FileShareResponse,
    FileVisibility,
    FileCategory,
)


class TestFileVisibility:
    def test_visibility_values(self):
        assert FileVisibility.PRIVATE == "private"
        assert FileVisibility.TENANT == "tenant"
        assert FileVisibility.PUBLIC == "public"


class TestFileCategory:
    def test_category_values(self):
        assert FileCategory.DOCUMENT == "document"
        assert FileCategory.IMAGE == "image"
        assert FileCategory.VIDEO == "video"
        assert FileCategory.AUDIO == "audio"
        assert FileCategory.SPREADSHEET == "spreadsheet"
        assert FileCategory.PRESENTATION == "presentation"
        assert FileCategory.ARCHIVE == "archive"
        assert FileCategory.OTHER == "other"


class TestFileUploadResponse:
    def test_response(self):
        now = datetime.now()
        resp = FileUploadResponse(
            file_id="file_123",
            filename="report.pdf",
            file_size=102400,
            content_type="application/pdf",
            bucket="sg-tenant-1",
            object_key="tenant-1/report.pdf",
            version=1,
            status="uploaded",
            uploaded_at=now,
            download_url="/api/v1/files/file_123/download",
        )
        assert resp.file_id == "file_123"
        assert resp.filename == "report.pdf"
        assert resp.version == 1
        assert resp.status == "uploaded"


class TestFileDownloadResponse:
    def test_response(self):
        resp = FileDownloadResponse(
            filename="report.pdf",
            content_type="application/pdf",
            file_size=102400,
            download_url="/api/v1/files/file_123/content",
            expires_in=3600,
        )
        assert resp.filename == "report.pdf"
        assert resp.expires_in == 3600


class TestFileSearchRequest:
    def test_defaults(self):
        req = FileSearchRequest(query="report")
        assert req.query == "report"
        assert req.size == 50
        assert req.from_ == 0
        assert req.sort_by == "created_at"
        assert req.sort_order == "desc"

    def test_with_filters(self):
        req = FileSearchRequest(
            query="financial",
            file_categories=["document", "spreadsheet"],
            tags=["important", "q3"],
            visibility="tenant",
            uploaded_by="user_123",
            size=100,
            from_=10,
            sort_by="file_size",
            sort_order="asc",
        )
        assert req.file_categories == ["document", "spreadsheet"]
        assert req.tags == ["important", "q3"]
        assert req.visibility == "tenant"
        assert req.uploaded_by == "user_123"
        assert req.size == 100
        assert req.sort_order == "asc"


class TestFileMetadataDTO:
    def test_dto(self):
        now = datetime.now()
        dto = FileMetadataDTO(
            id="file_123",
            filename="report.pdf",
            file_size=102400,
            content_type="application/pdf",
            file_category="document",
            visibility="tenant",
            checksum="abc123",
            version=1,
            is_deleted=False,
            uploaded_by="user_456",
            download_count=10,
            tags=["important"],
            metadata={"department": "finance"},
            download_url="/api/v1/files/file_123/download",
            tenant_id="tenant_1",
            created_at=now,
            updated_at=now,
        )
        assert dto.id == "file_123"
        assert dto.filename == "report.pdf"
        assert dto.file_category == "document"
        assert dto.visibility == "tenant"
        assert dto.tags == ["important"]


class TestFileSearchResponse:
    def test_response(self):
        hit = FileMetadataDTO(
            id="file_1",
            filename="report.pdf",
            file_size=1024,
            content_type="application/pdf",
            file_category="document",
            visibility="private",
            version=1,
            is_deleted=False,
            download_count=0,
            download_url="/api/v1/files/file_1/download",
            tenant_id="tenant_1",
            created_at=datetime.now(),
            updated_at=datetime.now(),
        )
        resp = FileSearchResponse(
            total_hits=1,
            hits=[hit],
            took_ms=15,
        )
        assert resp.total_hits == 1
        assert len(resp.hits) == 1
        assert resp.took_ms == 15


class TestFileStatsDTO:
    def test_stats_dto(self):
        dto = FileStatsDTO(
            file_category="document",
            count=150,
            total_size_bytes=52428800,
            percentage=45.5,
        )
        assert dto.file_category == "document"
        assert dto.count == 150
        assert dto.total_size_bytes == 52428800
        assert dto.percentage == 45.5


class TestFileOverviewDTO:
    def test_overview_dto(self):
        now = datetime.now()
        dto = FileOverviewDTO(
            total_files=1000,
            total_size_bytes=524288000,
            total_size_mb=500.0,
            files_by_category={"document": 500, "image": 300, "video": 200},
            files_by_visibility={"private": 600, "tenant": 300, "public": 100},
            top_tags=[{"tag": "important", "count": 50}],
            recent_uploads=[],
            storage_usage={"document": 262144000, "image": 157286400, "video": 104857600},
        )
        assert dto.total_files == 1000
        assert dto.total_size_mb == 500.0
        assert dto.files_by_category["document"] == 500
        assert dto.storage_usage["document"] == 262144000


class TestFileShareRequest:
    def test_request(self):
        req = FileShareRequest(
            file_id="file_123",
            expires_in_hours=48,
            max_downloads=10,
            password="secret123",
        )
        assert req.file_id == "file_123"
        assert req.expires_in_hours == 48
        assert req.max_downloads == 10
        assert req.password == "secret123"


class TestFileShareResponse:
    def test_response(self):
        now = datetime.now()
        resp = FileShareResponse(
            share_id="share_123",
            share_url="/api/v1/files/share/share_123",
            expires_at=now,
            max_downloads=10,
            download_count=0,
        )
        assert resp.share_id == "share_123"
        assert resp.max_downloads == 10
        assert resp.download_count == 0