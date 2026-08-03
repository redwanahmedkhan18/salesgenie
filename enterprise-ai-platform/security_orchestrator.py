#!/usr/bin/env python3
"""
SalesGenie Unified Security & Server Management Orchestrator
Integrates all security and high-availability components
"""

import asyncio
import aiohttp
import logging
import signal
import sys
import traceback
from datetime import datetime
from typing import Dict, Any
import os
import json

sys.path.insert(0, "/home/user/salesgenie")

from server_management import ServerManager, ServiceConfig
from security_protection import AdvancedSecurityManager, WAFRules, DDoSProtection, ThreatLevel
from container_security import (
    RuntimeProtection, ContainerSecurityScanner, SecretsDetector,
    ProcessIntegrityChecker, ResourceLimiter, SecurityPolicy
)
from high_availability import (
    HAHightAvailabilitySystem, LoadBalancer, LoadBalancerConfig,
    TrafficManager, ResourceOptimizer, CrashProtection
)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler('/var/log/salesgenie/orchestrator.log', mode='a')
    ]
)
logger = logging.getLogger("salesgenie.orchestrator")

class SecurityOrchestrator:
    def __init__(self):
        self.running = False
        self.server_manager = ServerManager()
        self.security_manager = AdvancedSecurityManager()
        self.waf = WAFRules()
        self.ddos_protector = DDoSProtection()
        self.runtime_protection = RuntimeProtection()
        self.scanner = ContainerSecurityScanner()
        self.secrets_detector = SecretsDetector()
        self.ha_system = HAHightAvailabilitySystem()
        self.crash_protector = CrashProtection()
        self.traffic_manager = TrafficManager()
        self.resource_optimizer = ResourceOptimizer()
        self.process_integrity_checker = ProcessIntegrityChecker()
        
        self.metrics = {
            "requests_processed": 0,
            "attacks_blocked": 0,
            "services_monitored": 0,
            "uptime_seconds": 0
        }
        
        self._setup_signal_handlers()
    
    def _setup_signal_handlers(self):
        signal.signal(signal.SIGTERM, self._handle_shutdown)
        signal.signal(signal.SIGINT, self._handle_shutdown)
        signal.signal(signal.SIGQUIT, self._handle_shutdown)
    
    def _handle_shutdown(self, signum, frame):
        logger.info(f"Received signal {signum}, shutting down gracefully...")
        self.running = False
    
    def initialize_services(self):
        services_registered = 0
        
        for service_name, service in self.server_manager.services.items():
            self.ha_system.add_service(service_name, "localhost", service.port)
            services_registered += 1
            logger.info(f"Registered service: {service_name} (port {service.port})")
        
        self.metrics["services_monitored"] = services_registered
        logger.info(f"Initialized {services_registered} services")
    
    async def security_middleware(self, request_data: Dict[str, Any]) -> Dict[str, Any]:
        ip = request_data.get("ip", "127.0.0.1")
        endpoint = request_data.get("endpoint", "/")
        method = request_data.get("method", "GET")
        body = request_data.get("body", "")
        headers = request_data.get("headers", {})
        
        self.metrics["requests_processed"] += 1
        
        if self.security_manager.is_ip_blacklisted(ip):
            self.metrics["attacks_blocked"] += 1
            return {"blocked": True, "reason": "IP blacklisted"}
        
        if not self.security_manager.check_rate_limit(ip, endpoint)[0]:
            self.metrics["attacks_blocked"] += 1
            return {"blocked": True, "reason": "Rate limit exceeded"}
        
        if not self.waf.check_request(method, endpoint, headers, body):
            self.metrics["attacks_blocked"] += 1
            self.security_manager.log_security_event({
                "type": "waf_block",
                "ip": ip,
                "endpoint": endpoint,
                "method": method
            })
            return {"blocked": True, "reason": "WAF blocked request"}
        
        if self.security_manager.detect_sql_injection(body):
            self.metrics["attacks_blocked"] += 1
            self.security_manager.block_ip(
                ip, "SQL Injection attempt", 1440, ThreatLevel.HIGH
            )
            return {"blocked": True, "reason": "SQL injection attempt"}
        
        threats_detected = self.security_manager.sanitize_input(str(body))
        if threats_detected != body:
            return {"blocked": True, "reason": "Malicious content detected"}
        
        return {"allowed": True, "sanitized_body": threats_detected}
    
    async def protect_service_call(self, service_name: str, endpoint: str):
        url = await self.ha_system.handle_request(service_name)
        
        if not url[0]:
            self.metrics["attacks_blocked"] += 1
            return {"error": "Service unavailable", "url": None}
        
        return {"success": True, "url": url[1]}
    
    async def graceful_shutdown(self):
        logger.info("Starting graceful shutdown...")
        self.running = False
    
    async def health_check(self) -> Dict[str, Any]:
        metrics = await self.resource_optimizer.get_system_metrics()
        health = {
            "status": "healthy" if sum(metrics.values()) < 0.9 else "degraded",
            "metrics": metrics,
            "uptime_seconds": self.metrics["uptime_seconds"],
            "requests_processed": self.metrics["requests_processed"],
            "attacks_blocked": self.metrics["attacks_blocked"],
            "services_monitored": self.metrics["services_monitored"],
            "timestamp": datetime.now().isoformat()
        }
        return health
    
    async def run_health_monitor(self):
        while self.running:
            await self.server_manager.auto_heal()
            await self.health_monitor.monitor_all()
            await self.crash_protector.detect_crash()
            await asyncio.sleep(30)
    
    async def run_security_enforcer(self):
        while self.running:
            self.metrics["uptime_seconds"] = int(
                (datetime.now() - self.crash_protector.process_start_time).total_seconds()
            )
            await asyncio.sleep(5)
    
    async def run_traffic_manager(self):
        while self.running:
            metrics = await self.resource_optimizer.get_system_metrics()
            current_rate = self.metrics["requests_processed"]
            throttle = await self.traffic_manager.adaptive_throttling(current_rate)
            await asyncio.sleep(1)
    
    async def run(self):
        logger.info("Starting SalesGenie Security & Server Management System")
        
        self.running = True
        self.crash_protector.update_heartbeat()
        self.initialize_services()
        
        health_task = asyncio.create_task(self.run_health_monitor())
        security_task = asyncio.create_task(self.run_security_enforcer())
        traffic_task = asyncio.create_task(self.run_traffic_manager())
        
        while self.running:
            try:
                health = await self.health_check()
                logger.debug(f"Health: {health['status']}")
                
                if health["status"] == "degraded":
                    logger.warning("System performance degraded")
                
                await asyncio.sleep(10)
                
            except Exception as e:
                logger.error(f"Error in main loop: {e}")
                traceback.print_exc()
                await asyncio.sleep(5)
        
        health_task.cancel()
        security_task.cancel()
        traffic_task.cancel()
        
        logger.info("Security Orchestration System stopped")

def main():
    orchestrator = SecurityOrchestrator()
    
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    
    try:
        loop.run_until_complete(orchestrator.run())
    except KeyboardInterrupt:
        print("\nShutting down...")
        loop.run_until_complete(orchestrator.graceful_shutdown())
    finally:
        loop.close()

if __name__ == "__main__":
    main()