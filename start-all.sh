#!/bin/bash
# SalesGenie Complete Startup Script
# Starts all backend services and frontend

echo "=== Starting SalesGenie Complete Development Environment ==="
echo ""

# Activate virtual environment
source .venv/bin/activate 2>/dev/null || { echo "ERROR: .venv not found"; exit 1; }
echo "✓ Virtual environment activated"

# Start Mailpit for local email testing (zero cost)
echo "Starting Mailpit for email testing..."
docker run -d --name mailpit -p 1025:1025 -p 8025:8025 axllent/mailpit 2>/dev/null || echo "Mailpit already running or failed to start"
echo "✓ Mailpit started (SMTP: localhost:1025, Web: http://localhost:8025)"

# Start infrastructure
echo "Starting infrastructure services..."
docker-compose up -d postgres redis minio 2>/dev/null || echo "docker-compose services may already be running"
echo "✓ Infrastructure services started (PostgreSQL:5433, Redis:6380, MinIO:9000/9001)"

# Wait for services
sleep 2

echo ""
echo "=== Starting Backend Services ==="

# Start all services in background
SERVICES=(
    "ai_gateway_service:8000"
    "auth_service:8001"
    "user_service:8002"
    "organization_service:8003"
    "billing_service:8004"
    "whatsapp_service:8005"
    "knowledge_service:8006"
    "sales_service:8007"
    "ticket_service:8008"
    "vector_service:8009"
    "analytics_service:8010"
    "workflow_service:8011"
    "search_service:8013"
    "notification_service:8014"
    "file_service:8015"
    "customer_service:8016"
    "support_service:8017"
    "conversation_service:8018"
    "telegram_service:8019"
    "messenger_service:8020"
    "email_service:8021"
    "lead_intelligence_service:8022"
)

for service in "${SERVICES[@]}"; do
    IFS=':' read -r name port <<< "$service"
    echo "Starting $name on port $port..."
    uvicorn enterprise_ai_platform.${name}.main:app --host 0.0.0.0 --port $port --reload &
done

# Wait for backend services to start
sleep 3

echo ""
echo "=== Starting Frontend ==="
npm run dev &
FRONTEND_PID=$!

echo ""
echo "=== All Services Started ==="
echo ""
echo "Backend Services:"
echo "  AI Gateway:       http://localhost:8000"
echo "  Auth:             http://localhost:8001"
echo "  User:             http://localhost:8002"
echo "  Organization:     http://localhost:8003"
echo "  Billing:          http://localhost:8004"
echo "  WhatsApp:         http://localhost:8005"
echo "  Knowledge:        http://localhost:8006"
echo "  Sales:            http://localhost:8007"
echo "  Ticket:           http://localhost:8008"
echo "  Vector:           http://localhost:8009"
echo "  Analytics:        http://localhost:8010"
echo "  Workflow:         http://localhost:8011"
echo "  Search:           http://localhost:8013"
echo "  Notification:     http://localhost:8014"
echo "  File:             http://localhost:8015"
echo "  Customer:         http://localhost:8016"
echo "  Support:          http://localhost:8017"
echo "  Conversation:     http://localhost:8018"
echo "  Telegram:         http://localhost:8019"
echo "  Messenger:        http://localhost:8020"
echo "  Email:            http://localhost:8021"
echo "  Lead Intelligence: http://localhost:8022"
echo ""
echo "Frontend:"
echo "  Main App:         http://localhost:4321"
echo ""
echo "Email Testing:"
echo "  Mailpit Web UI:   http://localhost:8025"
echo "  Mailpit SMTP:     localhost:1025"
echo ""
echo "Infrastructure:"
echo "  PostgreSQL:       localhost:5433"
echo "  Redis:            localhost:6380"
echo "  MinIO S3:         http://localhost:9000"
echo ""
echo "To stop all services: pkill -f uvicorn; kill $FRONTEND_PID 2>/dev/null"
echo "Or press Ctrl+C to stop everything"