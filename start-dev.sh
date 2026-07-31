#!/bin/bash
# SalesGenie Development Startup Script
# Starts all development services including Mailpit for email testing

echo "Starting SalesGenie Development Environment..."

# Activate virtual environment
source .venv/bin/activate

# Start infrastructure (if not running)
echo "Starting infrastructure services..."
docker-compose up -d postgres redis minio

# Start Mailpit for local email testing (zero cost)
echo "Starting Mailpit for email testing..."
if ! docker ps | grep -q mailpit; then
    docker run -d --name mailpit -p 1025:1025 -p 8025:8025 axllent/mailpit 2>/dev/null || true
fi

# Wait for services to be ready
echo "Waiting for services to be ready..."
sleep 5

# Run database migrations
echo "Running database migrations..."
alembic upgrade head

# Start services in development mode
echo "Starting services..."

# Auth Service (Port 8001)
echo "Starting Auth Service on port 8001..."
uvicorn enterprise_ai_platform.auth_service.main:app --host 0.0.0.0 --port 8001 --reload &

# User Service (Port 8002)
echo "Starting User Service on port 8002..."
uvicorn enterprise_ai_platform.user_service.main:app --host 0.0.0.0 --port 8002 --reload &

# Organization Service (Port 8003)
echo "Starting Organization Service on port 8003..."
uvicorn enterprise_ai_platform.organization_service.main:app --host 0.0.0.0 --port 8003 --reload &

# Billing Service (Port 8004)
echo "Starting Billing Service on port 8004..."
uvicorn enterprise_ai_platform.billing_service.main:app --host 0.0.0.0 --port 8004 --reload &

# WhatsApp Service (Port 8005)
echo "Starting WhatsApp Service on port 8005..."
uvicorn enterprise_ai_platform.whatsapp_service.main:app --host 0.0.0.0 --port 8005 --reload &

# AI Gateway Service (Port 8000)
echo "Starting AI Gateway Service on port 8000..."
uvicorn enterprise_ai_platform.ai_gateway_service.main:app --host 0.0.0.0 --port 8000 --reload &

# Knowledge Service (Port 8006)
echo "Starting Knowledge Service on port 8006..."
uvicorn enterprise_ai_platform.knowledge_service.main:app --host 0.0.0.0 --port 8006 --reload &

# Sales Service (Port 8007)
echo "Starting Sales Service on port 8007..."
uvicorn enterprise_ai_platform.sales_service.main:app --host 0.0.0.0 --port 8007 --reload &

# Ticket Service (Port 8008)
echo "Starting Ticket Service on port 8008..."
uvicorn enterprise_ai_platform.ticket_service.main:app --host 0.0.0.0 --port 8008 --reload &

# Vector Service (Port 8009)
echo "Starting Vector Service on port 8009..."
uvicorn enterprise_ai_platform.vector_service.main:app --host 0.0.0.0 --port 8009 --reload &

# Analytics Service (Port 8010)
echo "Starting Analytics Service on port 8010..."
uvicorn enterprise_ai_platform.analytics_service.main:app --host 0.0.0.0 --port 8010 --reload &

# Workflow Service (Port 8011)
echo "Starting Workflow Service on port 8011..."
uvicorn enterprise_ai_platform.workflow_service.main:app --host 0.0.0.0 --port 8011 --reload &

# Search Service (Port 8013)
echo "Starting Search Service on port 8013..."
uvicorn enterprise_ai_platform.search_service.main:app --host 0.0.0.0 --port 8013 --reload &

# Notification Service (Port 8014)
echo "Starting Notification Service on port 8014..."
uvicorn enterprise_ai_platform.notification_service.main:app --host 0.0.0.0 --port 8014 --reload &

# File Service (Port 8015)
echo "Starting File Service on port 8015..."
uvicorn enterprise_ai_platform.file_service.main:app --host 0.0.0.0 --port 8015 --reload &

# Customer Service (Port 8016)
echo "Starting Customer Service on port 8016..."
uvicorn enterprise_ai_platform.customer_service.main:app --host 0.0.0.0 --port 8016 --reload &

# Support Service (Port 8017)
echo "Starting Support Service on port 8017..."
uvicorn enterprise_ai_platform.support_service.main:app --host 0.0.0.0 --port 8017 --reload &

# Conversation Service (Port 8018)
echo "Starting Conversation Service on port 8018..."
uvicorn enterprise_ai_platform.conversation_service.main:app --host 0.0.0.0 --port 8018 --reload &

# Telegram Service (Port 8019)
echo "Starting Telegram Service on port 8019..."
uvicorn enterprise_ai_platform.telegram_service.main:app --host 0.0.0.0 --port 8019 --reload &

# Messenger Service (Port 8020)
echo "Starting Messenger Service on port 8020..."
uvicorn enterprise_ai_platform.messenger_service.main:app --host 0.0.0.0 --port 8020 --reload &

# Email Service (Port 8021)
echo "Starting Email Service on port 8021..."
uvicorn enterprise_ai_platform.email_service.main:app --host 0.0.0.0 --port 8021 --reload &

# Lead Intelligence Service (Port 8022)
echo "Starting Lead Intelligence Service on port 8022..."
uvicorn enterprise_ai_platform.lead_intelligence_service.main:app --host 0.0.0.0 --port 8022 --reload &

echo ""
echo "All services started!"
echo "AI Gateway:       http://localhost:8000"
echo "Auth:             http://localhost:8001"
echo "User:             http://localhost:8002"
echo "Organization:     http://localhost:8003"
echo "Billing:          http://localhost:8004"
echo "WhatsApp:         http://localhost:8005"
echo "Knowledge:        http://localhost:8006"
echo "Sales:            http://localhost:8007"
echo "Ticket:           http://localhost:8008"
echo "Vector:           http://localhost:8009"
echo "Analytics:        http://localhost:8010"
echo "Workflow:         http://localhost:8011"
echo "Search:           http://localhost:8013"
echo "Notification:     http://localhost:8014"
echo "File:             http://localhost:8015"
echo "Customer:         http://localhost:8016"
echo "Support:          http://localhost:8017"
echo "Conversation:     http://localhost:8018"
echo "Telegram:         http://localhost:8019"
echo "Messenger:        http://localhost:8020"
echo "Email:            http://localhost:8021"
echo "Lead Intelligence: http://localhost:8022"
echo ""
echo "Mailpit (Email Testing): http://localhost:8025"
echo "Mailpit SMTP:            localhost:1025"
echo ""
echo "Press Ctrl+C to stop all services"