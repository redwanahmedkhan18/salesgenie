#!/bin/bash
# SalesGenie Full Startup Script
# Starts all backend services and frontend

echo "=== Starting SalesGenie Complete Environment ==="

cd /home/user/salesgenie
source .venv/bin/activate

# Start infrastructure
echo "Starting infrastructure..."
docker-compose up -d postgres redis minio mailpit

sleep 3

# Function to start service
start_service() {
    local port=$1
    local name=$2
    echo "Starting $name on port $port..."
    cd /home/user/salesgenie
    .venv/bin/uvicorn enterprise_ai_platform.${name}.main:app --host 0.0.0.0 --port $port &
}

# Start all backend services in background
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

# Wait for services to start
sleep 5

# Start frontend
echo "Starting frontend..."
npm run dev &

echo ""
echo "=== All Services Started ==="
echo "Backend: Ports 8000-8022"
echo "Frontend: Port 4321"
echo "Infrastructure: PostgreSQL(5433), Redis(6380), MinIO(9000), Mailpit(8025)"
echo ""
echo "Visit: http://localhost:4321"
echo "Login: http://localhost:4321/login"
echo ""
echo "Services running in background - use 'ps aux | grep uvicorn' to check"