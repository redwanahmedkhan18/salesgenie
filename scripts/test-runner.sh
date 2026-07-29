#!/bin/bash
# SalesGenie Test Runner

set -e

echo "Running SalesGenie Test Suite..."

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Test functions
run_unit_tests() {
    echo -e "${YELLOW}Running Unit Tests...${NC}"
    poetry run pytest tests/unit/ -v --cov=enterprise_ai_platform --cov-report=term-missing
    echo -e "${GREEN}Unit Tests Complete${NC}"
}

run_integration_tests() {
    echo -e "${YELLOW}Running Integration Tests...${NC}"
    poetry run pytest tests/integration/ -v
    echo -e "${GREEN}Integration Tests Complete${NC}"
}

run_e2e_tests() {
    echo -e "${YELLOW}Running E2E Tests...${NC}"
    npm run test:e2e
    echo -e "${GREEN}E2E Tests Complete${NC}"
}

run_load_tests() {
    echo -e "${YELLOW}Running Load Tests...${NC}"
    locust -f tests/load-tests/locustfile.py --headless -u 50 -r 5 --run-time 1m
    echo -e "${GREEN}Load Tests Complete${NC}"
}

run_security_tests() {
    echo -e "${YELLOW}Running Security Tests...${NC}"
    poetry run bandit -r enterprise-ai-platform/ -x enterprise_ai_platform/tests
    poetry export -f requirements.txt --without-hashes | poetry run safety check --stdin
    echo -e "${GREEN}Security Tests Complete${NC}"
}

run_all_tests() {
    run_unit_tests
    run_integration_tests
    run_e2e_tests
    run_security_tests
    echo -e "${GREEN}All Tests Complete!${NC}"
}

# Main
case "${1:-all}" in
    unit)
        run_unit_tests
        ;;
    integration)
        run_integration_tests
        ;;
    e2e)
        run_e2e_tests
        ;;
    load)
        run_load_tests
        ;;
    security)
        run_security_tests
        ;;
    all)
        run_all_tests
        ;;
    *)
        echo "Usage: $0 {unit|integration|e2e|load|security|all}"
        exit 1
        ;;
esac