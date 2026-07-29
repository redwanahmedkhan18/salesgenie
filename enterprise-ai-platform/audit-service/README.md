# Audit Service

Tracks and stores all user actions, system events, and compliance logs for the SalesGenie platform.

## Overview

The Audit Service provides:

- **Audit Logging** - Record user actions and system events
- **Log Search** - Search audit logs with rich filtering
- **Compliance Reporting** - Generate compliance reports
- **Analytics** - Statistics by event type, severity, and actor
- **Retention Management** - Configurable log retention policies

## API Endpoints

### Logging
- `POST /api/v1/audit/logs` - Create audit log entry
- `GET /api/v1/audit/logs/{log_id}` - Get specific log entry

### Search & Analytics
- `GET /api/v1/audit/logs` - Search audit logs with filters
- `DELETE /api/v1/audit/logs` - Delete audit logs
- `GET /api/v1/audit/overview` - Get audit overview statistics
- `GET /api/v1/audit/stats/by-type` - Statistics by event type
- `GET /api/v1/audit/stats/by-severity` - Statistics by severity

### Compliance
- `GET /api/v1/audit/compliance/report` - Get compliance report

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