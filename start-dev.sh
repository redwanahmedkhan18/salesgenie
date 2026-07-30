#!/bin/bash
# SalesGenie Development Startup Script

echo "Starting SalesGenie Development Environment..."

# Activate virtual environment
source .venv/bin/activate

# Start infrastructure (if not running)
echo "Starting infrastructure services..."
docker-compose up -d postgres redis minio

# Wait for services to be ready
echo "Waiting for services to be ready..."
sleep 5

# Run database migrations
echo "Running database migrations..."
alembic upgrade head

# Start services in development mode
echo "Starting services..."

# Start auth service
echo "Starting Auth Service on port 8001..."
uvicorn enterprise_ai_platform.auth_service.main:app --host 0.0.0.0 --port 8001 --reload &

# Start analytics service
echo "Starting Analytics Service on port 8011..."
uvicorn enterprise_ai_platform.analytics_service.main:app --host 0.0.0.0 --port 8011 --reload &

# Start WhatsApp service
echo "Starting WhatsApp Service on port 8018..."
uvicorn enterprise_ai_platform.whatsapp_service.main:app --host 0.0.0.0 --port 8018 --reload &

# Start Lead Intelligence service
echo "Starting Lead Intelligence Service on port 8022..."
uvicorn enterprise_ai_platform.lead_intelligence_service.main:app --host 0.0.0.0 --port 8022 --reload &

echo ""
echo "All services started!"
echo "Auth: http://localhost:8001"
echo "Analytics: http://localhost:8011"
echo "WhatsApp: http://localhost:8018"
echo "Lead Intelligence: http://localhost:8022"
echo ""
echo "Press Ctrl+C to stop all services"