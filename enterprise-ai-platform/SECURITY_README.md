# SalesGenie Security & Server Management System

## Overview

This system provides enterprise-grade security and high-availability for the SalesGenie AI platform. It protects against hackers, manages server resources, prevents crashes, and ensures data integrity.

## Components

### 1. `security_orchestrator.py` - Main Orchestrator
Central control point that integrates all security components:
- Rate limiting
- WAF (Web Application Firewall)
- DDoS protection
- Intrusion detection
- Health monitoring

### 2. `security_protection.py` - Core Security
- **AdvancedSecurityManager**: Main security manager with rate limiting, IP blocking
- **WAFRules**: Web Application Firewall rules for SQL injection, XSS, path traversal
- **DDoSProtection**: Distributed Denial of Service protection
- **ThreatLevel**: Classification of security threats

### 3. `server_management.py` - Server Monitoring
- Health checks for all microservices
- Auto-restart on failure
- Crash detection and recovery
- Resource monitoring

### 4. `container_security.py` - Container & Runtime Security
- Secrets detector (finds API keys, passwords in code)
- Process integrity checker
- Resource limiter
- Container runtime protection

### 5. `high_availability.py` - High Availability
- Load balancing with multiple algorithms
- Circuit breaker pattern
- Adaptive throttling
- Traffic management

### 6. `nginx.conf` - Nginx Security Configuration
- TLS 1.3 only
- Security headers
- Rate limiting zones
- DDoS protection rules
- WAF patterns

### 7. `backup_recovery.py` - Backup & DR
- Automated daily backups
- Incremental hourly backups
- Disaster recovery procedures
- Backup verification

## Security Features

### Attack Prevention
- Block SQL injection, XSS, path traversal attacks
- Rate limiting per IP and endpoint
- DDoS protection with adaptive thresholds
- IP blacklisting for malicious actors

### Data Protection
- Automatic secrets detection
- Input sanitization
- Sensitive data masking in logs
- TLS 1.3 encryption

### High Availability
- Load balancing across service instances
- Circuit breakers for failing services
- Auto-scaling based on traffic
- Graceful degradation

### Crash Prevention
- Health checks every 5 seconds
- Automatic service restart on failure
- Resource monitoring with alerts
- Scheduled restarts to prevent memory leaks

## Deployment

### Using Systemd
```bash
# Install as systemd service
sudo cp security-orchestrator.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable security-orchestrator
sudo systemctl start security-orchestrator
```

### Manual Start
```bash
cd /home/user/salesgenie
export PYTHONPATH=/home/user/salesgenie
python3 enterprise-ai-platform/security_orchestrator.py
```

## Configuration

Edit `.cors-config` for:
- CORS allowed origins
- Rate limits
- Security thresholds
- Logging settings
- Recovery policies

## Monitoring

The system exposes metrics at:
- `/health` - Health check endpoint
- Logs: `/var/log/salesgenie/`
- Security events logged for SIEM integration

## Traffic Management

### Rate Limiting
- Global: 100,000 requests/minute
- Auth endpoints: 5-10 requests/minute
- API endpoints: 1000 requests/minute per IP

### DDoS Protection
- Threshold: 500 requests/second per IP
- Ban duration: 24 hours for detected attacks

### Adaptive Throttling
- Automatically throttles during high traffic
- Prevents resource exhaustion

## Recovery

### Backup Schedule
- Full backup: Daily at 02:00 UTC
- Incremental: Every hour
- Verification: Weekly on Sundays

### Restore Process
```bash
python3 -c "
from enterprise_ai_platform.backup_recovery import DisasterRecovery
dr = DisasterRecovery()
dr.restore_from_backup('salesgenie_full_20260803_020000')
"
```

## Security Architecture

```
                    Users
                      |
            CDN/WAF (Cloudflare)
                      |
                  Load Balancer
                      |
            ┌───────────────────┐
            │   Security Layer  │
            │  - DDoS Protection│
            │  - Rate Limiting  │
            │  - WAF Rules      │
            └───────────────────┘
                      |
            ┌───────────────────┐
            │  Application      │
            │  Services (26)    │
            └───────────────────┘
                      |
         ┌────────────┴────────────┐
         │            │              │
      Database     Vector DB      Redis
```

## Threat Response

| Threat Level | Response |
|-------------|----------|
| Low | Log only, monitor |
| Medium | Log + notify |
| High | Block IP for 60 min |
| Critical | Block IP for 24 hours |

## Resource Protection

- Memory: Alert at 85%, throttle at 95%
- CPU: Alert at 80%, throttle at 90%
- Disk: Alert at 90%, emergency stop at 95%

## Integration with Microservices

All services in `.env.services`:
- Auth (8001) - Strict rate limiting
- User (8002) - Moderate rate limiting
- Sales (8007) - Standard rate limiting
- Ticket (8008) - Standard rate limiting
- AI Gateway (8000) - Adaptive rate limiting
- Slack (8024) - Standard rate limiting
- Discord (8026) - Standard rate limiting

## Emergency Procedures

### Server Overload
1. Traffic automatically throttled based on load
2. Low-priority requests dropped
3. Alerts sent to admin dashboard

### Data Breach
1. Automatic IP block
2. Session invalidation
3. Audit log generation
4. Security team notification

### Service Crash
1. Service auto-restart (max 3 attempts)
2. Health check confirms recovery
3. Alert sent if restart fails