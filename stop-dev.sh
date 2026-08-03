#!/bin/bash

echo "=========================================="
echo "Stopping SalesGenie Development Services"
echo "=========================================="

# Kill Python/uvicorn processes
echo "Stopping Python services..."
pkill -f "uvicorn" 2>/dev/null || true
pkill -f "python3.*8000" 2>/dev/null || true
pkill -f "python3.*8001" 2>/dev/null || true
pkill -f "python3.*8024" 2>/dev/null || true
pkill -f "python3.*8026" 2>/dev/null || true
pkill -f "python3.*8027" 2>/dev/null || true
pkill -f "python3.*8028" 2>/dev/null || true
pkill -f "python3.*8029" 2>/dev/null || true
pkill -f "python3.*8030" 2>/dev/null || true

# Kill npm dev server
echo "Stopping frontend..."
pkill -f "astro dev" 2>/dev/null || true
pkill -f "npm run dev" 2>/dev/null || true

# Stop Docker containers
echo "Stopping Docker infrastructure..."
docker compose -f docker-compose.yml stop 2>/dev/null || true

echo ""
echo "All services stopped."