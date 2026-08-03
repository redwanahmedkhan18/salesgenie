#!/usr/bin/env python3
"""
SalesGenie Server Management & Health Monitoring System
Provides auto-recovery, crash prevention, and high availability
"""

import asyncio
import aiohttp
import subprocess
import logging
from typing import Dict, List, Optional
from dataclasses import dataclass, field
from datetime import datetime, timedelta
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("salesgenie.server-management")

@dataclass
class ServiceConfig:
    name: str
    port: int
    command: str
    health_endpoint: str
    restart_threshold: int = 3
    cooldown_minutes: int = 5
    last_restart: Optional[datetime] = None
    restart_count: int = 0
    is_active: bool = True

@dataclass
class ServiceHealth:
    name: str
    status: str
    response_time_ms: float
    last_check: datetime
    error_message: str = ""

SERVICES = [
    ServiceConfig("auth", 8001, "python3 -m uvicorn enterprise_ai_platform.auth_service.main:app --host 0.0.0.0 --port 8001 --reload", "/health/live"),
    ServiceConfig("user", 8002, "python3 -m uvicorn enterprise_ai_platform.user_service.main:app --host 0.0.0.0 --port 8002 --reload", "/health/live"),
    ServiceConfig("organization", 8003, "python3 -m uvicorn enterprise_ai_platform.organization_service.main:app --host 0.0.0.0 --port 8003 --reload", "/health/live"),
    ServiceConfig("billing", 8004, "python3 -m uvicorn enterprise_ai_platform.billing_service.main:app --host 0.0.0.0 --port 8004 --reload", "/health/live"),
    ServiceConfig("knowledge", 8006, "python3 -m uvicorn enterprise_ai_platform.knowledge_service.main:app --host 0.0.0.0 --port 8006 --reload", "/health/live"),
    ServiceConfig("sales", 8007, "python3 -m uvicorn enterprise_ai_platform.sales_service.main:app --host 0.0.0.0 --port 8007 --reload", "/api/v1/sales/health"),
    ServiceConfig("ticket", 8008, "python3 -m uvicorn enterprise_ai_platform.ticket_service.main:app --host 0.0.0.0 --port 8008 --reload", "/health"),
    ServiceConfig("analytics", 8012, "python3 -m uvicorn enterprise_ai_platform.analytics_service.main:app --host 0.0.0.0 --port 8012 --reload", "/health"),
    ServiceConfig("search", 8013, "python3 -m uvicorn enterprise_ai_platform.search_service.main:app --host 0.0.0.0 --port 8013 --reload", "/health"),
    ServiceConfig("notification", 8014, "python3 -m uvicorn enterprise_ai_platform.notification_service.main:app --host 0.0.0.0 --port 8014 --reload", "/health"),
    ServiceConfig("customer", 8016, "python3 -m uvicorn enterprise_ai_platform.customer_service.main:app --host 0.0.0.0 --port 8016 --reload", "/health"),
    ServiceConfig("support", 8017, "python3 -m uvicorn enterprise_ai_platform.support_service.main:app --host 0.0.0.0 --port 8017 --reload", "/health"),
    ServiceConfig("conversation", 8018, "python3 -m uvicorn enterprise_ai_platform.conversation_service.main:app --host 0.0.0.0 --port 8018 --reload", "/health"),
    ServiceConfig("telegram", 8019, "python3 -m uvicorn enterprise_ai_platform.telegram_service.main:app --host 0.0.0.0 --port 8019 --reload", "/health"),
    ServiceConfig("messenger", 8020, "python3 -m uvicorn enterprise_ai_platform.messenger_service.main:app --host 0.0.0.0 --port 8020 --reload", "/health"),
    ServiceConfig("email", 8021, "python3 -m uvicorn enterprise_ai_platform.email_service.main:app --host 0.0.0.0 --port 8021 --reload", "/health"),
    ServiceConfig("lead_intelligence", 8022, "python3 -m uvicorn enterprise_ai_platform.lead_intelligence_service.main:app --host 0.0.0.0 --port 8022 --reload", "/health"),
    ServiceConfig("audit", 8023, "python3 -m uvicorn enterprise_ai_platform.audit_service.main:app --host 0.0.0.0 --port 8023 --reload", "/health"),
    ServiceConfig("slack", 8024, "python3 -m uvicorn slack-service.main:app --host 0.0.0.0 --port 8024 --reload", "/health/live"),
    ServiceConfig("discord", 8026, "python3 -m uvicorn discord-service.main:app --host 0.0.0.0 --port 8026 --reload", "/health/live"),
    ServiceConfig("ai_gateway", 8000, "python3 -m uvicorn enterprise_ai_platform.ai_gateway_service.main:app --host 0.0.0.0 --port 8000 --reload", "/api/v1/gateway/models"),
    ServiceConfig("whatsapp", 8005, "python3 -m uvicorn enterprise_ai_platform.whatsapp_service.main:app --host 0.0.0.0 --port 8005 --reload", "/health"),
    ServiceConfig("knowledge", 8006, "python3 -m uvicorn enterprise_ai_platform.knowledge_service.main:app --host 0.0.0.0 --port 8006 --reload", "/health"),
    ServiceConfig("sales", 8007, "python3 -m uvicorn enterprise_ai_platform.sales_service.main:app --host 0.0.0.0 --port 8007 --reload", "/api/v1/sales/health"),
    ServiceConfig("ticket", 8008, "python3 -m uvicorn enterprise_ai_platform.ticket_service.main:app --host 0.0.0.0 --port 8008 --reload", "/health"),
    ServiceConfig("vector", 8009, "python3 -m uvicorn enterprise_ai_platform.vector_service.main:app --host 0.0.0.0 --port 8009 --reload", "/health"),
    ServiceConfig("slack", 8024, "python3 -m uvicorn slack-service.main:app --host 0.0.0.0 --port 8024 --reload", "/health/live"),
    ServiceConfig("discord", 8026, "python3 -m uvicorn discord-service.main:app --host 0.0.0.0 --port 8026 --reload", "/health/live"),
]

class ServerManager:
    def __init__(self):
        self.services = {s.name: s for s in SERVICES}
        self.health_history: Dict[str, List[ServiceHealth]] = {s: [] for s in self.services}
        self.rate_limiter = TokenBucketRateLimiter()
        
    async def check_service_health(self, service: ServiceConfig) -> ServiceHealth:
        start_time = time.time()
        try:
            url = f"http://localhost:{service.port}{service.health_endpoint}"
            async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=5)) as session:
                async with session.get(url) as response:
                    elapsed = (time.time() - start_time) * 1000
                    return ServiceHealth(
                        name=service.name,
                        status="healthy" if response.status == 200 else "degraded",
                        response_time_ms=elapsed,
                        last_check=datetime.now()
                    )
        except Exception as e:
            elapsed = (time.time() - start_time) * 1000
            return ServiceHealth(
                name=service.name,
                status="unhealthy",
                response_time_ms=elapsed,
                last_check=datetime.now(),
                error_message=str(e)
            )
    
    async def restart_service(self, service: ServiceConfig) -> bool:
        now = datetime.now()
        
        if service.last_restart and now - service.last_restart < timedelta(minutes=service.cooldown_minutes):
            logger.warning(f"Service {service.name} in cooldown period")
            return False
        
        try:
            logger.info(f"Restarting service: {service.name}")
            subprocess.Popen(service.command.split(), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            service.last_restart = now
            service.restart_count += 1
            return True
        except Exception as e:
            logger.error(f"Failed to restart {service.name}: {e}")
            return False
    
    async def auto_heal(self):
        for service in self.services.values():
            health = await self.check_service_health(service)
            self.health_history[service.name].append(health)
            
            if len(self.health_history[service.name]) > 10:
                self.health_history[service.name].pop(0)
            
            if health.status == "unhealthy":
                recent_failures = sum(1 for h in self.health_history[service.name][-3:] if h.status == "unhealthy")
                if recent_failures >= 3 and service.restart_count < service.restart_threshold:
                    await self.restart_service(service)

class TokenBucketRateLimiter:
    def __init__(self, max_tokens: int = 1000, refill_rate: float = 10.0):
        self.max_tokens = max_tokens
        self.tokens = max_tokens
        self.refill_rate = refill_rate
        self.last_refill = time.time()
        self.lock = asyncio.Lock()
    
    async def acquire(self, tokens: int = 1) -> bool:
        async with self.lock:
            now = time.time()
            tokens_to_add = (now - self.last_refill) * self.refill_rate
            self.tokens = min(self.max_tokens, self.tokens + tokens_to_add)
            self.last_refill = now
            
            if self.tokens >= tokens:
                self.tokens -= tokens
                return True
            return False

if __name__ == "__main__":
    manager = ServerManager()
    print("Server Management System initialized")
    print(f"Monitoring {len(manager.services)} services")