"""
Unit Tests for Chat Service Models
"""

import pytest
import uuid
from datetime import datetime, timezone
from unittest.mock import MagicMock

from chat_service.src.models import (
    ChannelType,
    ConversationSession,
    NormalizedMessagePayload,
)


class TestChannelType:
    def test_channel_type_values(self):
        assert ChannelType.WEBSITE == "website"
        assert ChannelType.WHATSAPP == "whatsapp"
        assert ChannelType.MESSENGER == "messenger"
        assert ChannelType.TELEGRAM == "telegram"
        assert ChannelType.INSTAGRAM == "instagram"
        assert ChannelType.SLACK == "slack"
        assert ChannelType.DISCORD == "discord"
        assert ChannelType.EMAIL == "email"
        assert ChannelType.VOICE == "voice"


class TestNormalizedMessagePayload:
    def test_defaults(self):
        payload = NormalizedMessagePayload(
            session_id="sess_123",
            channel=ChannelType.WEBSITE,
            sender_id="cust_456",
            sender_type="customer",
            content="Hello, I need help!",
        )
        assert payload.session_id == "sess_123"
        assert payload.channel == ChannelType.WEBSITE
        assert payload.sender_id == "cust_456"
        assert payload.sender_type == "customer"
        assert payload.content == "Hello, I need help!"
        assert payload.media_url is None
        assert payload.metadata == {}

    def test_with_values(self):
        now = datetime.now(timezone.utc)
        payload = NormalizedMessagePayload(
            session_id="sess_789",
            channel=ChannelType.WHATSAPP,
            sender_id="cust_abc",
            sender_type="customer",
            content="Order status check",
            media_url="https://example.com/image.jpg",
            timestamp=now,
            metadata={"order_id": "ORD-12345"},
        )
        assert payload.channel == ChannelType.WHATSAPP
        assert payload.media_url == "https://example.com/image.jpg"
        assert payload.timestamp == now
        assert payload.metadata == {"order_id": "ORD-12345"}


class TestConversationSession:
    def test_conversation_session_defaults(self):
        session = ConversationSession(
            tenant_id=uuid.uuid4(),
            channel=ChannelType.WEBSITE,
            customer_id=uuid.uuid4(),
            last_message_at=datetime.now(timezone.utc),
        )
        assert session.is_active is True
        assert session.unread_count == 0

    def test_conversation_session_with_values(self):
        tenant_id = uuid.uuid4()
        customer_id = uuid.uuid4()
        agent_id = uuid.uuid4()
        now = datetime.now(timezone.utc)

        session = ConversationSession(
            tenant_id=tenant_id,
            channel=ChannelType.SLACK,
            customer_id=customer_id,
            assigned_agent_id=agent_id,
            is_active=False,
            unread_count=5,
            last_message_at=now,
        )
        assert session.channel == ChannelType.SLACK
        assert session.customer_id == customer_id
        assert session.assigned_agent_id == agent_id
        assert session.is_active is False
        assert session.unread_count == 5
        assert session.last_message_at == now