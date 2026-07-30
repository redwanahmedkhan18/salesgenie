#!/bin/bash
# SalesGenie Development Deployment Script for Ubuntu Linux
# Usage: cd /home/user/salesgenie && bash deploy.sh

echo "=========================================="
echo "  SalesGenie Development Deployment"
echo "=========================================="
echo ""

# Activate virtual environment
source .venv/bin/activate

# Start backend services in background
echo "Starting backend services..."

# Auth Service (Port 8001)
nohup python3 -m uvicorn enterprise_ai_platform.auth_service.main:app \
  --host 0.0.0.0 --port 8001 --reload > /tmp/auth.log 2>&1 &

# Analytics Service (Port 8010)
nohup python3 -m uvicorn enterprise_ai_platform.analytics_service.main:app \
  --host 0.0.0.0 --port 8010 --reload > /tmp/analytics.log 2>&1 &

# WhatsApp Service (Port 8005)
nohup python3 -m uvicorn enterprise_ai_platform.whatsapp_service.main:app \
  --host 0.0.0.0 --port 8005 --reload > /tmp/whatsapp.log 2>&1 &

# Lead Intelligence Service (Port 8006)
nohup python3 -m uvicorn enterprise_ai_platform.lead_intelligence_service.main:app \
  --host 0.0.0.0 --port 8006 --reload > /tmp/lead-intel.log 2>&1 &

# Wait for backend services to start
sleep 3

# Start frontend
echo "Starting frontend..."
nohup npm run dev > /tmp/frontend.log 2>&1 &

# Wait for frontend to start
sleep 3

echo ""
echo "=========================================="
echo -e "\033[32m  All Services Running! \033[0m"
echo "=========================================="
echo ""
echo "Access URLs:"
echo "  Frontend:  http://localhost:4321"
echo "  Auth:      http://localhost:8001"
echo "  Analytics: http://localhost:8010"
echo "  WhatsApp:  http://localhost:8005"
echo "  Lead Intel: http://localhost:8006"
echo ""
echo "To stop all services:"
echo "  pkill -f 'uvicorn.*enterprise'"
echo "  pkill -f 'astro dev'"
echo ""

# Show service status
echo "Service Status:"
curl -s http://localhost:8001/health/live && echo " - Auth Service OK"
curl -s http://localhost:8010/health/live && echo " - Analytics OK"
curl -s http://localhost:8005/docs > /dev/null && echo "WhatsApp OK"
curl -s http://localhost:8006/docs > /dev/null && echo "Lead Intel OK"
curl -s http://localhost:4321/ > /dev/null && echo "Frontend OK"