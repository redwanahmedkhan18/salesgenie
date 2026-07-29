# Chat Service

Real-time WebSocket Pub-Sub, Omnichannel Messaging (WhatsApp, Slack, Telegram, Email), and Webhooks for the SalesGenie platform.

## Overview

The Chat Service provides:

- **WebSocket Real-Time Chat** - Real-time messaging via WebSocket connections
- **Omnichannel Webhooks** - Unified webhook receiver for 9 channels (WhatsApp, Messenger, Telegram, Slack, Discord, Instagram, Email, Voice, Website)
- **Pub-Sub Pipeline** - Normalizes channel-specific payloads into a unified message stream
- **Connection Management** - Active WebSocket connection tracking per session

## Supported Channels

- Website chat
- WhatsApp
- Facebook Messenger
- Telegram
- Instagram
- Slack
- Discord
- Email
- Voice

## API Endpoints

### Webhooks
- `POST /api/v1/chat/webhooks/{channel}` - Unified webhook receiver

### WebSocket
- `WS /api/v1/chat/ws/{session_id}` - Real-time WebSocket connection

## Running Locally

```bash
pip install -r ../../requirements.txt
cp .env.example .env
cd migrations && alembic upgrade head
python main.py
```

## Testing

```bash
pytest tests/ -v
```