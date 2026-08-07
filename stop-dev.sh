#!/bin/bash

echo "=========================================="
echo "Stopping SalesGenie Development Services"
echo "=========================================="

echo "Stopping Python services..."
pkill -f "uvicorn" 2>/dev/null || true
for port in 8000 8001 8002 8003 8004 8005 8006 8007 8008 8009 8010 8011 8012 8013 8014 8015 8016 8017 8018 8019 8020 8021 8022 8023 8024 8026 8027 8028 8029 8030; do
  pkill -f "python3.*:$port" 2>/dev/null || true
  fuser -k $port/tcp 2>/dev/null || true
done

echo "Stopping frontend..."
pkill -f "astro dev" 2>/dev/null || true
pkill -f "npm run dev" 2>/dev/null || true
pkill -f "node.*astro" 2>/dev/null || true

echo "Stopping Docker infrastructure..."
docker compose -f docker-compose.yml stop 2>/dev/null || true

echo ""
echo "All services stopped."