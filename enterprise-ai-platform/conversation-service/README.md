# Conversation Service

Manages real-time conversations, messages, and chat sessions with AI agents for the SalesGenie platform.

## Overview

The Conversation Service provides:

- **Conversation Management** - Create, update, delete conversations
- **Messaging** - Send and retrieve messages within conversations
- **Conversation Search** - Search conversations with rich filtering
- **Handoff** - Hand off conversations from AI to human agents
- **Analytics** - Statistics by status, channel, and agent performance

## API Endpoints

### Conversations
- `POST /api/v1/conversations` - Create conversation
- `GET /api/v1/conversations/{id}` - Get conversation
- `PATCH /api/v1/conversations/{id}` - Update conversation
- `DELETE /api/v1/conversations/{id}` - Delete conversation
- `GET /api/v1/conversations` - Search conversations

### Messaging
- `POST /api/v1/conversations/{id}/messages` - Send message
- `GET /api/v1/conversations/{id}/messages` - Get messages

### Handoff
- `POST /api/v1/conversations/{id}/handoff` - Handoff to human agent

### Analytics
- `GET /api/v1/conversations/overview` - Overview statistics
- `GET /api/v1/conversations/stats/by-status` - Stats by status
- `GET /api/v1/conversations/stats/by-channel` - Stats by channel

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