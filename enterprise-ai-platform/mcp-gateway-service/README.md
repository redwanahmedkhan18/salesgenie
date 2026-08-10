# MCP Gateway Service

Controlled MCP (Model Context Protocol) tool gateway for SalesGenie AI agents.

## Overview

Provides a centralized, secure gateway for MCP tools with RBAC, audit logging,
rate limiting, and performance metrics.

## API Endpoints

### Tool Management
- `POST /api/v1/mcp/tools` - Register a new MCP tool
- `GET /api/v1/mcp/tools` - List available tools
- `GET /api/v1/mcp/tools/{id}` - Get tool details
- `PATCH /api/v1/mcp/tools/{id}` - Update tool
- `DELETE /api/v1/mcp/tools/{id}` - Delete tool

### Tool Execution
- `POST /api/v1/mcp/tools/{id}/execute` - Execute a tool by ID
- `POST /api/v1/mcp/execute` - Execute a tool by name

### Audit & Stats
- `GET /api/v1/mcp/logs` - Get execution logs
- `GET /api/v1/mcp/stats` - Get tool statistics

## Running Locally

```bash
pip install -r ../../requirements.txt
cp .env.example .env
export PYTHONPATH=/path/to/enterprise-ai-platform
python3 -m uvicorn main:app --reload --port 8028
```

## Testing

```bash
pytest tests/ -v
```
