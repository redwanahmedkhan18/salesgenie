# SalesGenie Monitoring & Observability

## Overview

This directory contains all monitoring, logging, and observability configurations for the SalesGenie platform.

## Components

### Prometheus (`prometheus.yml`)
- Service discovery for Kubernetes pods
- Custom metrics for API Gateway, Lead Intelligence, WhatsApp services
- Database connection monitoring
- AI token usage tracking

### Grafana Dashboards
- `system-overview.json` - Overall system health
- `api-performance.json` - API latency, error rates, throughput
- `ai-performance.json` - LLM usage, token consumption, costs

### Alerting Rules
- `alerting-rules.yml` - Production alert definitions
- `recording-rules.yml` - Pre-computed metrics

### Logging Configuration
- `logging.json` - Python logging configuration
- `config.yaml` - Detailed logging settings

## Quick Start

### 1. Deploy Prometheus
```bash
kubectl apply -f salesgenie-monitoring/
```

### 2. Import Grafana Dashboards
```bash
# Via Grafana UI:
# + -> Import -> Upload JSON file

# Or via API:
curl -X POST \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $GRAFANA_API_KEY" \
  -d @grafana/dashboards/system-overview.json \
  http://grafana.monitoring/api/dashboards/db
```

### 3. Verify Monitoring
```bash
# Check Prometheus targets
kubectl port-forward svc/prometheus-server 9090:80
open http://localhost:9090/targets

# Check Grafana
kubectl port-forward svc/grafana 3000:80
open http://localhost:3000
```

## Metrics Reference

### HTTP Metrics
| Metric | Description | Labels |
|--------|-------------|--------|
| `http_requests_total` | Total HTTP requests | service, method, status, path |
| `http_request_duration_seconds` | Request duration | service, path, method |
| `http_response_size_bytes` | Response size | service, path |

### Database Metrics
| Metric | Description | Labels |
|--------|-------------|--------|
| `pg_stat_database_numbackends` | Active connections | datname |
| `pg_stat_statements_total` | Query statistics | query, type |

### AI Metrics
| Metric | Description | Labels |
|--------|-------------|--------|
| `ai_tokens_used_total` | Tokens consumed | provider, model |
| `ai_request_duration_seconds` | LLM latency | provider, model |
| `ai_errors_total` | AI errors | provider, error_type |

## Dashboard Descriptions

### System Overview
Shows overall system health including:
- Service availability
- CPU/Memory usage
- Request rate
- Error rate
- Database connections

### API Performance
Displays API metrics:
- Request rate by service
- Error rates
- Response time distribution
- Top endpoints by latency

### AI Performance
Monitors AI usage:
- Token consumption
- Cost tracking
- Provider performance
- Error rates

## Alert Thresholds

### Critical Alerts
- Service down (immediate)
- High error rate > 5% for 5 minutes
- Database connection exhaustion

### Warning Alerts
- High CPU usage > 80% for 2 minutes
- High memory usage > 80% for 2 minutes
- Slow database queries

## Log Levels

| Level | Description | Action |
|-------|-------------|--------|
| DEBUG | Detailed info | Development only |
| INFO | Normal operation | None |
| WARNING | Potential issues | Monitor |
| ERROR | Failed operations | Alert |
| CRITICAL | System failures | Page |

## Best Practices

1. **Set appropriate retention policies**
2. **Use sampling for high-volume logs**
3. **Monitor cost of metrics collection**
4. **Alert on business metrics, not just technical**
5. **Correlate logs with traces**

## Troubleshooting

### Prometheus not scraping
```bash
kubectl logs -l app=prometheus -n monitoring
kubectl describe servicemonitor -n monitoring
```

### Grafana dashboard not loading
```bash
kubectl logs -l app.kubernetes.io/name=grafana -n monitoring
```

### High cardinality metrics
```bash
# Check metric cardinality
curl -s http://prometheus:9090/api/v1/status/buildinfo | jq
```