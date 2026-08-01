#!/bin/bash
# SalesGenie Local Startup Script (No Docker Required)
# Uses SQLite for database and in-memory Redis for development

echo "=== Starting SalesGenie Local Development Environment ==="

cd /home/user/salesgenie
source .venv/bin/activate

# Set environment for SQLite (in-memory)
export USE_SQLITE=true
export DATABASE_URL="sqlite:///./salesgenie_dev.db"
export REDIS_URL="redis://localhost:6380/0"
export REDIS_HOST="localhost"
export REDIS_PORT=6380

echo "Environment configured for SQLite database mode"

# Create SQLite database with all tables
echo "Initializing SQLite database..."
python3 << 'EOF'
import asyncio
import sqlite3
from pathlib import Path

db_path = Path("/home/user/salesgenie/salesgenie_dev.db")

# Connect and create basic tables
conn = sqlite3.connect(str(db_path))
cursor = conn.cursor()

# Create tables needed for auth service
cursor.executescript("""
CREATE TABLE IF NOT EXISTS auth_user_sessions (
    id TEXT PRIMARY KEY,
    user_id TEXT NOT NULL,
    refresh_token_hash TEXT NOT NULL,
    device_name TEXT,
    ip_address TEXT,
    user_agent TEXT,
    is_active BOOLEAN DEFAULT 1,
    expires_at TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    tenant_id TEXT
);

CREATE TABLE IF NOT EXISTS auth_user_devices (
    id TEXT PRIMARY KEY,
    user_id TEXT NOT NULL,
    device_identifier TEXT NOT NULL UNIQUE,
    device_type TEXT NOT NULL,
    is_trusted BOOLEAN DEFAULT 0,
    last_used_at TIMESTAMP NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS auth_mfa_secrets (
    id TEXT PRIMARY KEY,
    user_id TEXT NOT NULL UNIQUE,
    secret_key TEXT NOT NULL,
    is_enabled BOOLEAN DEFAULT 0,
    backup_codes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS auth_workspace_invitations (
    id TEXT PRIMARY KEY,
    email TEXT NOT NULL,
    role TEXT DEFAULT 'support_agent',
    invited_by_user_id TEXT NOT NULL,
    token TEXT NOT NULL UNIQUE,
    status TEXT DEFAULT 'pending',
    expires_at TIMESTAMP,
    tenant_id TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS auth_oauth_accounts (
    id TEXT PRIMARY KEY,
    user_id TEXT NOT NULL,
    provider TEXT NOT NULL,
    provider_user_id TEXT NOT NULL UNIQUE,
    access_token TEXT NOT NULL,
    refresh_token TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_sessions_user_id ON auth_user_sessions(user_id);
CREATE INDEX IF NOT EXISTS idx_sessions_refresh_token ON auth_user_sessions(refresh_token_hash);
CREATE INDEX IF NOT EXISTS idx_mfa_user_id ON auth_mfa_secrets(user_id);
""")

conn.commit()
conn.close()
print("Database tables created successfully")
EOF

echo ""
echo "=== Starting Backend Services ==="

# Function to start service
start_service() {
    local port=$1
    local name=$2
    echo "Starting $name on port $port..."
    uvicorn enterprise_ai_platform.${name}.main:app --host 0.0.0.0 --port $port &
}

# Start all backend services
SERVICES=(
    "8000:ai_gateway_service"
    "8001:auth_service"
    "8002:user_service"
    "8003:organization_service"
    "8004:billing_service"
    "8005:whatsapp_service"
    "8006:knowledge_service"
    "8007:sales_service"
    "8008:ticket_service"
    "8009:vector_service"
    "8010:analytics_service"
    "8011:workflow_service"
    "8013:search_service"
    "8014:notification_service"
    "8015:file_service"
    "8016:customer_service"
    "8017:support_service"
    "8018:conversation_service"
    "8019:telegram_service"
    "8020:messenger_service"
    "8021:email_service"
    "8022:lead_intelligence_service"
)

for entry in "${SERVICES[@]}"; do
    IFS=':' read -r port name <<< "$entry"
    start_service $port $name
done

sleep 5

echo ""
echo "=== Starting Frontend ==="
npm run dev &
FRONTEND_PID=$!

echo ""
echo "=== All Services Started ==="
echo "Frontend:       http://localhost:4321"
echo "Auth:           http://localhost:8001"
echo "AI Gateway:     http://localhost:8000"
echo ""
echo "Login:          http://localhost:4321/login"
echo "Sign Up:        http://localhost:4321/signup"
echo ""
echo "Database:       SQLite (salesgenie_dev.db)"
echo "Press Ctrl+C to stop all services"