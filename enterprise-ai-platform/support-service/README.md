# Support Service

Support ticket management, live chat handoff, and customer support operations for the SalesGenie platform.

## Overview

The Support Service manages all support-related operations including:

- **Support Tickets** - Customer support requests with status, priority, category tracking
- **Ticket Notes** - Internal and external notes on tickets
- **Ticket Assignments** - Assignment history to support agents
- **Live Handoff** - Live chat handoff from AI agents to human agents

## API Endpoints

### Tickets
- `POST /api/v1/tickets` - Create a new support ticket
- `GET /api/v1/tickets` - List tickets (with filtering)
- `GET /api/v1/tickets/{id}` - Get ticket details
- `PATCH /api/v1/tickets/{id}` - Update ticket
- `DELETE /api/v1/tickets/{id}` - Close ticket

### Assignment
- `POST /api/v1/tickets/{id}/assign` - Assign ticket to agent

### Notes
- `POST /api/v1/tickets/notes` - Add a note
- `GET /api/v1/tickets/{id}/notes` - Get ticket notes

### Live Handoff
- `POST /api/v1/tickets/handoffs` - Request live chat handoff
- `POST /api/v1/tickets/handoffs/{id}/accept` - Accept handoff

### Analytics
- `GET /api/v1/tickets/analytics/overview` - Support analytics

## Ticket Status Values
- `open` - New ticket
- `in_progress` - Agent working on it
- `pending` - Waiting for customer
- `resolved` - Issue resolved
- `closed` - Ticket closed
- `reopened` - Reopened

## Ticket Priority Values
- `low`, `medium`, `high`, `urgent`, `critical`

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