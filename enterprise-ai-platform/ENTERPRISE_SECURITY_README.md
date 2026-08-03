# SalesGenie Enterprise Security System

## Overview

Built for enterprise AI customer support and sales platforms. This system provides infrastructure-grade security with dashboard management, audit capabilities, zero-trust verification, and compliance features expected by enterprise customers.

## Core Modules

### 1. Security Dashboard (`enterprise_security_dashboard.py`)
Central hub providing:
- Real-time security score (0-100)
- Active threat visualization
- Security metrics dashboard
- System health overview

### 2. Audit Log System
Comprehensive auditing of all activities:
- User actions and logins
- System changes
- API usage
- Data modifications
- Security events

### 3. Session Management
Enterprise-grade session control:
- Multi-device session tracking
- Termination from any device
- Session limits and timeouts
- Activity monitoring

### 4. API Key Management
Complete key lifecycle:
- Generate with custom scopes
- Rotate automatically
- Revoke instantly
- Usage tracking

### 5. Secrets Manager
Central secrets vault:
- Provider integrations (OpenAI, Stripe, AWS, etc.)
- AES-256 encryption
- Automatic rotation
- Expiration alerts

### 6. Zero Trust Verification
Continuous verification:
- Device fingerprinting
- IP reputation scoring
- Geolocation validation
- Risk scoring algorithm

## Security Features

### Threat Detection
- Impossible travel detection
- Brute force protection
- Credential stuffing detection
- API abuse detection
- DDoS protection

### Protection Layers
- WAF (SQL Injection, XSS, CSRF)
- Rate limiting by user/workspace/org
- IP allowlist/blocklist
- Country blocking
- Geo-blocking

### Compliance Ready
- GDPR support
- SOC 2 Type II
- HIPAA compliance
- ISO 27001 alignment
- PCI DSS controls

## API Endpoints

```
GET    /api/v1/security/dashboard
GET    /api/v1/security/threats
GET    /api/v1/security/events
POST   /api/v1/security/audit
GET    /api/v1/sessions
POST   /api/v1/sessions/terminate
GET    /api/v1/api-keys
POST   /api/v1/api-keys
POST   /api/v1/secrets
GET    /api/v1/secrets/status
POST   /api/v1/zero-trust/verify
GET    /api/v1/monitoring/health
GET    /api/v1/backup/stats
POST   /api/v1/backup/create
GET    /api/v1/compliance/report
```

## Security Score Calculation

Score = 100 - (Threats × 2) - (Low MFA % × 10) - (Avg Risk × 20)

Components:
- MFA Coverage (weight: 30%)
- Secrets Rotation (weight: 25%)
- Threat Activity (weight: 25%)
- Session Security (weight: 20%)

## Configuration

```bash
# Environment Variables
SECURITY_SCORE_THRESHOLD=90
MFA_REQUIRED=true
SESSION_TIMEOUT_HOURS=8
RATE_LIMIT_DEFAULT=1000
RATE_LIMIT_AUTH=10
BACKUP_RETENTION_DAYS=30
```

## Monitoring

All events logged to `/var/log/salesgenie/`:
- `security.log` - Security events
- `audit.log` - Audit trail
- `access.log` - Access logs

## Compliance Reports

Generate with:
```python
from enterprise_security_dashboard import ComplianceGenerator
report = ComplianceGenerator.generate_report("gdpr")
```

## Integrations

- SIEM: Splunk, Datadog, Elastic, Azure Sentinel
- Alerts: Slack, Discord, Email, Webhooks
- Metrics: Prometheus, Grafana
- Logs: ELK Stack, CloudWatch

## Next Steps

The following modules need implementation based on the enterprise requirements:
1. Infrastructure Monitoring (Redis, Postgres, Vector DB)
2. Service Control Panel (Restart, Stop, Start, Logs)
3. Live Logs Viewer
4. Rate Limiting Center
5. Firewall Rules Management
6. Certificate Manager
7. Email Security
8. Webhook Management
9. Compliance Center
10. Backup & Disaster Recovery

## Usage Example

```python
from enterprise_security_dashboard import SecurityDashboard, SessionManager, APIKeyManager

# Initialize
dashboard = SecurityDashboard()
sessions = SessionManager()
api_keys = APIKeyManager()

# Create admin session
session = sessions.create_session("sess_001", "admin_001", {
    "device": "Chrome",
    "os": "macOS",
    "location": "New York",
    "ip": "203.0.113.5"
})

# Create service API key
key = api_keys.create_key("Billing Service", ["read", "write"], expires_in_days=90)

# Check security status
overview = dashboard.get_security_overview()
print(f"Security Score: {overview['security_score']}/100")
```