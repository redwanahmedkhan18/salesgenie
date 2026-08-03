#!/bin/bash

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo -e "${YELLOW}Starting infrastructure...${NC}"
docker compose up -d postgres redis minio mailpit 2>&1

echo -e "${YELLOW}Waiting for services...${NC}"
sleep 3
docker compose ps --format "table {{.Name}}\t{{.Status}}"

echo -e "${YELLOW}Running database migrations...${NC}"
PGPASSWORD=salesgenie_secret_pass_2026 psql -h localhost -p 5433 -U salesgenie_admin -d salesgenie -f enterprise-ai-platform/database/full_migration.sql 2>/dev/null && echo -e "${GREEN}Database ready${NC}" || echo "Database may already be migrated"

echo -e "${YELLOW}Activating Python environment...${NC}"
source .venv/bin/activate 2>/dev/null || true

echo -e "${YELLOW}Starting all services...${NC}"

cd "$(pwd)"

# Core services
nohup python3 -m uvicorn enterprise_ai_platform.ai_gateway_service.main:app --host 0.0.0.0 --port 8000 > /tmp/gateway.log 2>&1 &
nohup python3 -m uvicorn enterprise_ai_platform.auth_service.main:app --host 0.0.0.0 --port 8001 > /tmp/auth.log 2>&1 &

# Integration services (from enterprise-ai-platform/)
cd enterprise-ai-platform/discord-service && nohup python3 -c "from main import app; import uvicorn; uvicorn.run(app, host='0.0.0.0', port=8026)" > /tmp/discord.log 2>&1 &
cd ../slack-service && nohup python3 -c "from main import app; import uvicorn; uvicorn.run(app, host='0.0.0.0', port=8024)" > /tmp/slack.log 2>&1 &
cd ../instagram-service && nohup python3 main.py > /tmp/instagram.log 2>&1 &

# Enterprise services
cd ../sso-service && nohup python3 -c "from main import create_app; import uvicorn; uvicorn.run(create_app(), host='0.0.0.0', port=8028)" > /tmp/sso.log 2>&1 &
cd ../ai-evaluation-framework/src && nohup python3 -c "from main import create_app; import uvicorn; uvicorn.run(create_app(), host='0.0.0.0', port=8029)" > /tmp/evaluation.log 2>&1 &

cd ../ABAC-engine && nohup python3 -c "from main import app; import uvicorn; uvicorn.run(app, host='0.0.0.0', port=8030)" > /tmp/abac.log 2>&1 &

cd "$(pwd)"

# Frontend
nohup npm run dev > /tmp/dev.log 2>&1 &

echo ""
echo "=========================================="
echo -e "${GREEN}SalesGenie Platform Running!${NC}"
echo "=========================================="
echo ""
echo "  Database:  psql -h localhost -p 5433 -U salesgenie_admin -d salesgenie"
echo "  Logs:      tail -f /tmp/*.log"
echo "  Stop all:  ./stop-dev.sh"
echo ""