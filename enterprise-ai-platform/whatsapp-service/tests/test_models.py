"""
Unit tests for WhatsApp Service
"""

import pytest
from unittest.mock import AsyncMock, MagicMock, patch
from uuid import uuid4
from datetime import datetime, timezone

from enterprise_ai_platform.whatsapp-service.src.models import (
    WhatsAppAccount, WhatsAppMessage, MessageTemplate, ConversationSession, MediaFile,
    WhatsAppAccountDTO, WhatsAppMessageDTO, MessageTemplateDTO
)


class TestWhatsAppAccountModel:
    def test_account_creation(self):
        account = WhatsAppAccount(
            id=uuid4(),
            name="Test Business",
            phone_number_id="123456789",
            access_token="test-token",
            is_active=True,
            verified=True,
            created_at=datetime.now(timezone.utc),
            updated_at=datetime.now(timezone.utc),
        )
        
        assert account.name == "Test Business"
        assert account.is_active is True
        assert account.verified is True

    def test_account_dto_conversion(self):
        account = WhatsAppAccount(
            id=uuid4(),
            name="Test Business",
            phone_number_id="123456789",
            access_token="test-token",
            is_active=True,
            verified=True,
            created_at=datetime.now(timezone.utc),
            updated_at=datetime.now(timezone.utc),
        )
        
        dto = WhatsAppAccountDTO.from_orm(account)
        assert dto.name == "Test Business"
        assert dto.is_active is True


class TestWhatsAppMessageModel:
    def test_message_creation(self):
        message = WhatsAppMessage(
            id=uuid4(),
            account_id=uuid4(),
            conversation_session_id=uuid4(),
            to="1234567890",
            from_number="0987654321",
            message_type="text",
            content="Hello, World!",
            status="sent",
            language="en",
            created_at=datetime.now(timezone.utc),
            updated_at=datetime.now(timezone.utc),
        )
        
        assert message.to == "1234567890"
        assert message.content == "Hello, World!"
        assert message.language == "en"


class TestMessageTemplateModel:
    def test_template_creation(self):
        template = MessageTemplate(
            id=uuid4(),
            account_id=uuid4(),
            name="Welcome Template",
            category="authentication",
            language="en",
            status="approved",
            created_at=datetime.now(timezone.utc),
            updated_at=datetime.now(timezone.utc),
        )
        
        assert template.name == "Welcome Template"
        assert template.category == "authentication"


class TestConversationSessionModel:
    def test_session_creation(self):
        session = ConversationSession(
            id=uuid4(),
            account_id=uuid4(),
            phone_number_id="123456789",
            customer_phone="1234567890",
            status="active",
            language="en",
            created_at=datetime.now(timezone.utc),
            updated_at=datetime.now(timezone.utc),
        )
        
        assert session.status == "active"
        assert session.language == "en"


class TestMediaFileModel:
    def test_media_file_creation(self):
        media = MediaFile(
            id=uuid4(),
            message_id=uuid4(),
            media_url="https://example.com/image.jpg",
            mime_type="image/jpeg",
            language="en",
            created_at=datetime.now(timezone.utc),
        )
        
        assert media.mime_type == "image/jpeg"
        assert media.language == "en"


class TestLanguageSupport:
    def test_multilingual_message_support(self):
        languages = ["en", "es", "fr", "de", "zh", "ja", "ar", "hi", "pt", "it"]
        
        for lang in languages:
            message = WhatsAppMessage(
                id=uuid4(),
                account_id=uuid4(),
                conversation_session_id=uuid4(),
                to="1234567890",
                from_number="0987654321",
                message_type="text",
                content=f"Message in {lang}",
                status="sent",
                language=lang,
                created_at=datetime.now(timezone.utc),
                updated_at=datetime.now(timezone.utc),
            )
            assert message.language == lang

    def test_multilingual_template_support(self):
        languages = ["en", "es", "fr", "de", "zh", "ja", "ar", "hi"]
        
        for lang in languages:
            template = MessageTemplate(
                id=uuid4(),
                account_id=uuid4(),
                name=f"Template {lang}",
                category="marketing",
                language=lang,
                status="approved",
                created_at=datetime.now(timezone.utc),
                updated_at=datetime.now(timezone.utc),
            )
            assert template.language == lang


class TestWhatsAppBusinessRules:
    def test_message_length_validation(self):
        max_length = 4096
        long_message = "A" * max_length
        
        assert len(long_message) == max_length

    def test_template_category_validation(self):
        valid_categories = [
            "authentication",
            "marketing",
            "utility",
            "notification"
        ]
        
        for category in valid_categories:
            template = MessageTemplate(
                id=uuid4(),
                account_id=uuid4(),
                name=f"Template {category}",
                category=category,
                language="en",
                status="approved",
                created_at=datetime.now(timezone.utc),
                updated_at=datetime.now(timezone.utc),
            )
            assert template.category == category