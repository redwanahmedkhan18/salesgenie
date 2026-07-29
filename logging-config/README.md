# SalesGenie Logging Configuration

## Overview

SalesGenie uses structured JSON logging for comprehensive observability across all services. Logs are designed to be queryable, searchable, and actionable.

## Log Structure

All logs follow a consistent JSON structure:

```json
{
  "timestamp": "2024-01-15T10:30:00.123Z",
  "level": "INFO",
  "service": "api-gateway",
  "request_id": "req_123456",
  "user_id": "user_789",
  "trace_id": "trace_abc123",
  "message": "User successfully authenticated",
  "module": "auth",
  "function": "authenticate_user",
  "line": 42,
  "duration_ms": 45,
  "context": {
    "method": "POST",
    "path": "/api/v1/auth/login",
    "status": 200
  }
}
```

## Log Levels

| Level | Description | Use Case |
|-------|-------------|----------|
| DEBUG | Detailed debug information | Development only |
| INFO | General information | Normal operation |
| WARNING | Warning conditions | Potential issues |
| ERROR | Error events | Failed operations |
| CRITICAL | Critical conditions | System failures |

## Context Fields

### Request Context
```json
{
  "request_id": "req_123456",
  "user_id": "user_789",
  "trace_id": "trace_abc123",
  "method": "POST",
  "path": "/api/v1/lead-intelligence/companies/search",
  "query_string": "industry=technology&location=us"
}
```

### Response Context
```json
{
  "status": 200,
  "duration_ms": 125,
  "body_size": 1024
}
```

### Database Context
```json
{
  "db_query": "SELECT * FROM companies WHERE industry = $1",
  "db_duration_ms": 15,
  "db_rows": 42
}
```

### AI Context
```json
{
  "ai_provider": "groq",
  "ai_model": "gpt-4o-mini",
  "ai_tokens_used": 500,
  "ai_cost_usd": 0.005
}
```

## Sensitive Data Redaction

The following fields are automatically redacted:

- `password`
- `token`
- `api_key`
- `secret`
- `authorization`
- `cookie`

Redaction is applied to:
- Request bodies
- Response bodies
- Headers
- Query parameters

## Log Categories

### Authentication Logs
```json
{"level": "INFO", "event": "user_login", "user_id": "user_123", "success": true}
{"level": "WARNING", "event": "login_failed", "ip": "192.168.1.1", "reason": "invalid_password"}
```

### Audit Logs
```json
{"level": "INFO", "event": "data_access", "resource": "customer:456", "action": "read"}
{"level": "INFO", "event": "data_modification", "resource": "lead:789", "action": "update"}
```

### Error Logs
```json
{"level": "ERROR", "event": "external_api_error", "provider": "whatsapp", "error": "rate_limited"}
{"level": "CRITICAL", "event": "database_connection_failed", "error": "connection_refused"}
```

## Log Retention

| Log Type | Retention | Storage |
|----------|-----------|---------|
| Application Logs | 30 days | Local + CloudWatch |
| Error Logs | 90 days | Local + CloudWatch |
| Audit Logs | 365 days | Local + S3 |
| Metrics | 90 days | Prometheus |
| Traces | 7 days | Jaeger |

## Querying Logs

### By Request ID
```bash
aws logs filter-log-events \
  --log-group-name /salesgenie/api-gateway \
  --filter-pattern '{$.request_id = "req_123456"}'
```

### By Error Level
```bash
kubectl logs -l app=api-gateway -n salesgenie | jq 'select(.level == "ERROR")'
```

### By Service
```bash
# Elasticsearch
GET /salesgenie-*/_search
{
  "query": {
    "term": {"service.keyword": "lead-intelligence"}
  }
}
```

## Log Shipping

### Fluentd Configuration
```xml
<source>
  @type tail
  path /var/log/salesgenie/app.log
  pos_file /var/log/fluentd-salesgenie.pos
  tag salesgenie.app
  format json
</source>

<match salesgenie.**>
  @type elasticsearch
  host elasticsearch
  port 9200
  logstash_format true
</match>
```

### CloudWatch Logs
```yaml
# Kubernetes daemonset
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: fluentd
spec:
  template:
    spec:
      containers:
      - name: fluentd
        image: fluent/fluentd:v1.16
        volumeMounts:
        - name: logs
          mountPath: /var/log/salesgenie
        - name: config
          mountPath: /fluentd/etc/
```

## Performance Considerations

### Sampling
- High-volume request logs: 10% sampling
- Error logs: 100% sampling
- Audit logs: 100% sampling

### Buffering
- Flush interval: 5 seconds
- Buffer size: 8MB
- Retry type: exponential backoff

### Log Levels in Production
- Console: INFO and above
- File: DEBUG and above
- Syslog: INFO and above