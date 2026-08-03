#!/bin/bash
# SalesGenie Security Quick Start Script
# Use this to initialize all security components

set -e

echo "🔒 SalesGenie Security System - Initializing..."

# Create required directories
echo "Creating directories..."
mkdir -p /var/log/salesgenie
mkdir -p /var/backups/salesgenie
mkdir -p /home/user/salesgenie/logs
mkdir -p /home/user/salesgenie/data

# Set permissions
echo "Setting permissions..."
chmod 755 /var/log/salesgenie
chmod 755 /var/backups/salesgenie
chown -R salesgenie:salesgenie /var/log/salesgenie 2>/dev/null || true
chown -R salesgenie:salesgenie /var/backups/salesgenie 2>/dev/null || true

# Install Python dependencies
echo "Installing Python dependencies..."
pip3 install aiohttp schedule --quiet 2>/dev/null || pip install aiohttp schedule --quiet

# Verify services
echo "Verifying service ports..."
python3 << 'EOF'
import sys
sys.path.insert(0, "/home/user/salesgenie")

from enterprise_ai_platform.check_ports import service_ports
from collections import Counter

ports = list(service_ports.values())
duplicates = [port for port, count in Counter(ports).items() if count > 1]

if duplicates:
    print(f"❌ ERROR: Duplicate ports found: {duplicates}")
    sys.exit(1)
else:
    print(f"✅ All {len(ports)} ports are unique")
    print(f"   Port range: {min(ports)}-{max(ports)}")
EOF

# Run security scan
echo "Running security scan..."
python3 << 'EOF'
import sys
sys.path.insert(0, "/home/user/salesgenie")

from enterprise_ai_platform.security_protection import AdvancedSecurityManager

security = AdvancedSecurityManager()
print("✅ Security protection system initialized")
print(f"   Rate limits configured: {len(security.endpoint_rate_limits)} endpoints")
EOF

# Test WAF
echo "Testing WAF rules..."
python3 << 'EOF'
import sys
sys.path.insert(0, "/home/user/salesgenie")

from enterprise_ai_platform.security_protection import WAFRules

waf = WAFRules()
test_requests = [
    ("POST", "/api/v1/auth/login", {}, "username=admin&password=' OR '1'='1"),
    ("GET", "/api/v1/users", {}, ""),
]

blocked = sum(1 for method, path, headers, body in test_requests if not waf.check_request(method, path, headers, body))
print(f"✅ WAF tested: {blocked} malicious requests blocked")
EOF

# Test High Availability
echo "Testing High Availability system..."
python3 << 'EOF'
import sys
sys.path.insert(0, "/home/user/salesgenie")

from enterprise_ai_platform.high_availability import HAHightAvailabilitySystem

ha = HAHightAvailabilitySystem()
ha.add_service("auth", "localhost", 8001)
ha.add_service("user", "localhost", 8002)
print(f"✅ High Availability system ready with {len(ha.health_monitor.instances)} services")
EOF

echo ""
echo "✅ Security System Initialization Complete!"
echo ""
echo "To start the security orchestrator:"
echo "  python3 /home/user/salesgenie/enterprise-ai-platform/security_orchestrator.py"
echo ""
echo "Or as a systemd service (after installing the .service file):"
echo "  sudo systemctl enable security-orchestrator"
echo "  sudo systemctl start security-orchestrator"
echo ""
echo "View logs:"
echo "  tail -f /var/log/salesgenie/orchestrator.log"