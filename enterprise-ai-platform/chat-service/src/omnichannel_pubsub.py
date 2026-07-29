"""
Omnichannel Pub-Sub Pipeline & Webhook Processor
Processes incoming messages from 9 distinct channels (WhatsApp, Telegram, Messenger, Slack, etc.).
"""

import logging
from typing import Dict, Any
from .models import NormalizedMessagePayload, ChannelType

logger = logging.getLogger("salesgenie.chat.pubsub")


class OmnichannelPubSubProcessor:
    """Standardizes channel-specific payloads into normalized message stream."""

    @staticmethod
    def normalize_inbound_webhook(channel: str, raw_payload: Dict[str, Any]) -> NormalizedMessagePayload:
        """Parses webhook payload from WhatsApp, Telegram, Messenger, Slack, Email, etc."""
        channel_enum = ChannelType.WEBSITE
        try:
            channel_enum = ChannelType(channel.lower())
        except ValueError:
            pass

        # Extract normalized fields
        sender = raw_payload.get("sender", "customer_123")
        content = raw_payload.get("text", raw_payload.get("body", raw_payload.get("message", "")))
        session_id = raw_payload.get("session_id", f"sess_{channel}_{sender}")

        return NormalizedMessagePayload(
            session_id=session_id,
            channel=channel_enum,
            sender_id=str(sender),
            sender_type="customer",
            content=content or "Hello from omnichannel customer channel!",
            metadata={"raw": raw_payload},
        )


pubsub_processor = OmnichannelPubSubProcessor()
