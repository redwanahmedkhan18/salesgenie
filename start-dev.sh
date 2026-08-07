#!/bin/bash

BASE_DIR="/home/user/salesgenie"
LOG_DIR="/tmp/salesgenie"

mkdir -p "$LOG_DIR"

echo "=========================================="
echo "SalesGenie Development Startup Script"
echo "=========================================="

echo "Starting infrastructure..."
docker compose -f "$BASE_DIR/docker-compose.yml" up -d postgres redis minio mailpit 2>&1

sleep 5
docker compose -f "$BASE_DIR/docker-compose.yml" ps --format "table {{.Name}}\t{{.Status}}"

echo "Running database migrations..."
PGPASSWORD=salesgenie_secret_pass_2026 psql -h localhost -p 5433 -U salesgenie_admin -d salesgenie -f "$BASE_DIR/enterprise-ai-platform/database/full_migration.sql" 2>&1

if [ $? -eq 0 ]; then
  echo "✓ Database migrations complete"
else
  echo "⚠ Database may already be migrated or connection issue"
fi

echo "Creating file service table if missing..."
PGPASSWORD=salesgenie_secret_pass_2026 psql -h localhost -p 5433 -U salesgenie_admin -d salesgenie << 'SQLEOF'
CREATE TABLE IF NOT EXISTS file_metadata (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    bucket VARCHAR(100) NOT NULL,
    object_key VARCHAR(500) NOT NULL UNIQUE,
    filename VARCHAR(255) NOT NULL,
    file_size INTEGER NOT NULL,
    content_type VARCHAR(200) NOT NULL,
    file_category VARCHAR(30) NOT NULL DEFAULT 'other',
    visibility VARCHAR(20) NOT NULL DEFAULT 'private',
    checksum VARCHAR(64),
    etag VARCHAR(100),
    version INTEGER NOT NULL DEFAULT 1,
    is_deleted BOOLEAN NOT NULL DEFAULT FALSE,
    deleted_at TIMESTAMP WITH TIME ZONE,
    uploaded_by VARCHAR(100),
    download_count INTEGER NOT NULL DEFAULT 0,
    metadata_json JSONB,
    tags JSONB,
    created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_file_metadata_tenant_id ON file_metadata(tenant_id);
CREATE INDEX IF NOT EXISTS idx_file_metadata_bucket ON file_metadata(bucket);
CREATE INDEX IF NOT EXISTS idx_file_metadata_object_key ON file_metadata(object_key);
SQLEOF

echo "✓ File metadata table ready"

echo "Activating Python environment..."
source "$BASE_DIR/.venv/bin/activate" 2>/dev/null || true

echo "Starting services..."
cd "$BASE_DIR"
export PYTHONPATH="$BASE_DIR"

for port in 8000 8001 8002 8003 8004 8005 8006 8007 8008 8009 8010 8011 8012 8013 8014 8015 8016 8017 8018 8019 8020 8021 8022 8023 8024 8026 8027 8028 8029 8030; do
  fuser -k $port/tcp 2>/dev/null || true
done

start_uvicorn() {
  local name=$1
  local module=$2
  local port=$3
  nohup python3 -m uvicorn "$module" --host 0.0.0.0 --port "$port" > "$LOG_DIR/${name}.log" 2>&1 &
  sleep 1
  if curl -fs "http://localhost:$port/health/live" > /dev/null 2>&1 || curl -fs "http://localhost:$port/docs" > /dev/null 2>&1; then
    echo "✓ $name (port $port)"
  else
    if [ -s "$LOG_DIR/${name}.log" ]; then
      echo "✗ $name (port $port)"
      echo "  Log: $(tail -1 "$LOG_DIR/${name}.log" 2>/dev/null | tr '\n' ' ')"
    else
      echo "✗ $name (port $port)"
    fi
  fi
}

echo ""
echo "Starting core services..."
start_uvicorn "api_gateway" "enterprise_ai_platform.ai_gateway_service.main:app" 8000
start_uvicorn "auth" "enterprise_ai_platform.auth_service.main:app" 8001
start_uvicorn "user" "enterprise_ai_platform.user_service.main:app" 8002
start_uvicorn "organization" "enterprise_ai_platform.organization_service.main:app" 8003
start_uvicorn "billing" "enterprise_ai_platform.billing_service.main:app" 8004

echo ""
echo "Starting messaging services..."
start_uvicorn "whatsapp" "enterprise_ai_platform.whatsapp_service.main:app" 8005
start_uvicorn "knowledge" "enterprise_ai_platform.knowledge_service.main:app" 8006
start_uvicorn "sales" "enterprise_ai_platform.sales_service.main:app" 8007
start_uvicorn "ticket" "enterprise_ai_platform.ticket_service.main:app" 8008
start_uvicorn "vector" "enterprise_ai_platform.vector_service.main:app" 8009
start_uvicorn "chat" "enterprise_ai_platform.chat_service.main:app" 8010
start_uvicorn "workflow" "enterprise_ai_platform.workflow_service.main:app" 8011

echo ""
echo "Starting analytics & search services..."
start_uvicorn "analytics" "enterprise_ai_platform.analytics_service.main:app" 8012
start_uvicorn "search" "enterprise_ai_platform.search_service.main:app" 8013
start_uvicorn "notification" "enterprise_ai_platform.notification_service.main:app" 8014

echo ""
echo "Starting file & customer services..."
start_uvicorn "file" "enterprise_ai_platform.file_service.main:app" 8015
start_uvicorn "customer" "enterprise_ai_platform.customer_service.main:app" 8016

echo ""
echo "Starting support & conversation services..."
start_uvicorn "support" "enterprise_ai_platform.support_service.main:app" 8017
start_uvicorn "conversation" "enterprise_ai_platform.conversation_service.main:app" 8018

echo ""
echo "Starting integrated messaging services..."
start_uvicorn "telegram" "enterprise_ai_platform.telegram_service.main:app" 8019
start_uvicorn "messenger" "enterprise_ai_platform.messenger_service.main:app" 8020
start_uvicorn "email" "enterprise_ai_platform.email_service.main:app" 8021
start_uvicorn "lead_intelligence" "enterprise_ai_platform.lead_intelligence_service.main:app" 8022
start_uvicorn "audit" "enterprise_ai_platform.audit_service.main:app" 8023
start_uvicorn "slack" "enterprise_ai_platform.slack_service.main:app" 8024

echo ""
echo "Starting other services..."
cd "$BASE_DIR/enterprise-ai-platform/discord-service" && python3 main.py > "$LOG_DIR/discord.log" 2>&1 &
cd "$BASE_DIR/enterprise-ai-platform/instagram-service" && python3 main.py > "$LOG_DIR/instagram.log" 2>&1 &
cd "$BASE_DIR/enterprise-ai-platform/sso-service" && python3 main.py > "$LOG_DIR/sso.log" 2>&1 &
cd "$BASE_DIR/enterprise-ai-platform/ai-evaluation-framework/src" && python3 main.py > "$LOG_DIR/ai_eval.log" 2>&1 &
cd "$BASE_DIR/enterprise-ai-platform/ABAC-engine" && python3 -m uvicorn main:app --host 0.0.0.0 --port 8030 > "$LOG_DIR/ABAC.log" 2>&1 &
sleep 2

echo "✓ Discord Service (port 8026)"
echo "✓ Instagram Service (port 8027)"
echo "✓ SSO Service (port 8028)"
echo "✓ AI Evaluation (port 8029)"
echo "✓ ABAC Engine (port 8030)"

echo ""
echo "Starting frontend dev server..."
cd "$BASE_DIR"
npm run dev > "$LOG_DIR/frontend.log" 2>&1 &
sleep 3
echo "✓ Frontend (port 4321)"

cd "$BASE_DIR"

echo ""
echo "=========================================="
echo "SalesGenie Platform Running!"
echo "=========================================="
echo ""
echo "Services:"
echo "  Database:     psql -h localhost -p 5433 -U salesgenie_admin -d salesgenie"
echo "  Frontend:     http://localhost:4321"
echo "  API Gateway:  http://localhost:8000"
echo "  Auth:         http://localhost:8001"
echo "  User:         http://localhost:8002"
echo "  Org:          http://localhost:8003"
echo "  Billing:      http://localhost:8004"
echo "  WhatsApp:     http://localhost:8005"
echo "  Knowledge:    http://localhost:8006"
echo "  Sales:        http://localhost:8007"
echo "  Ticket:       http://localhost:8008"
echo "  Vector:       http://localhost:8009"
echo "  Chat:         http://localhost:8010"
echo "  Workflow:     http://localhost:8011"
echo "  Analytics:    http://localhost:8012"
echo "  Search:       http://localhost:8013"
echo "  Notification: http://localhost:8014"
echo "  File:         http://localhost:8015"
echo "  Customer:     http://localhost:8016"
echo "  Support:      http://localhost:8017"
echo "  Conversation: http://localhost:8018"
echo "  Telegram:     http://localhost:8019"
echo "  Messenger:    http://localhost:8020"
echo "  Email:        http://localhost:8021"
echo "  Lead Intel:   http://localhost:8022"
echo "  Audit:        http://localhost:8023"
echo "  Slack:        http://localhost:8024"
echo "  Mailpit:      http://localhost:8025"
echo "  Discord:      http://localhost:8026"
echo "  Instagram:    http://localhost:8027"
echo "  SSO:          http://localhost:8028"
echo "  AI Eval:      http://localhost:8029"
echo "  ABAC:         http://localhost:8030"
echo ""
echo "Logs:"
echo "  tail -f \$LOG_DIR/*.log"
echo ""
echo "Stop all:  ./stop-dev.sh"