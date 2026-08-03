#!/usr/bin/env python3
"""
SalesGenie High Availability & Traffic Management System
Provides load balancing, auto-scaling, traffic distribution, and crash prevention
"""

import asyncio
import aiohttp
import time
import statistics
import logging
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from collections import deque
import signal
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("salesgenie.ha-system")

@dataclass
class ServiceInstance:
    name: str
    host: str
    port: int
    healthy: bool = True
    last_heartbeat: Optional[datetime] = None
    load_average: float = 0.0
    response_time_ms: float = 0.0
    request_count: int = 0
    error_count: int = 0
    uptime_seconds: float = 0.0

@dataclass
class LoadBalancerConfig:
    algorithm: str = "weighted_round_robin"
    health_check_interval: int = 10
    timeout_ms: int = 5000
    max_retries: int = 3
    circuit_breaker_threshold: int = 5
    circuit_breaker_timeout: int = 30

class HealthMonitor:
    def __init__(self, check_interval: int = 5):
        self.check_interval = check_interval
        self.instances: Dict[str, List[ServiceInstance]] = {}
        self.healthy_instances: Dict[str, List[ServiceInstance]] = {}
        self.failed_instances: Dict[str, List[ServiceInstance]] = {}
        self.avg_response_times: Dict[str, deque] = {}
    
    async def check_instance_health(self, instance: ServiceInstance) -> bool:
        timeout = aiohttp.ClientTimeout(total=2)
        url = f"http://{instance.host}:{instance.port}/health"
        
        try:
            start_time = time.time()
            async with aiohttp.ClientSession(timeout=timeout) as session:
                async with session.get(url) as response:
                    elapsed = (time.time() - start_time) * 1000
                    instance.response_time_ms = elapsed
                    instance.healthy = response.status == 200
                    instance.last_heartbeat = datetime.now()
                    return instance.healthy
        except Exception as e:
            logger.warning(f"Health check failed for {instance.name}: {e}")
            instance.healthy = False
            return False
    
    async def monitor_all(self):
        for service_name, instances in self.instances.items():
            healthy = []
            unhealthy = []
            
            for instance in instances:
                await self.check_instance_health(instance)
                if instance.healthy:
                    healthy.append(instance)
                else:
                    unhealthy.append(instance)
            
            self.healthy_instances[service_name] = healthy
            self.failed_instances[service_name] = unhealthy

class LoadBalancer:
    def __init__(self, config: LoadBalancerConfig):
        self.config = config
        self.health_monitor = HealthMonitor()
        self.request_distribution: Dict[str, Dict[str, int]] = {}
        self.circuit_breakers: Dict[str, CircuitBreaker] = {}
        self.start_time = time.time()
    
    def add_instance(self, service_name: str, instance: ServiceInstance):
        if service_name not in self.health_monitor.instances:
            self.health_monitor.instances[service_name] = []
            self.request_distribution[service_name] = {}
            self.circuit_breakers[service_name] = CircuitBreaker(
                threshold=self.config.circuit_breaker_threshold,
                timeout=self.config.circuit_breaker_timeout
            )
        
        self.health_monitor.instances[service_name].append(instance)
        self.request_distribution[service_name][instance.name] = 0
        logger.info(f"Added instance {instance.name} for service {service_name}")
    
    def select_instance(self, service_name: str) -> Optional[ServiceInstance]:
        if service_name not in self.health_monitor.healthy_instances:
            return None
        
        healthy = self.health_monitor.healthy_instances[service_name]
        if not healthy:
            return None
        
        if self.config.algorithm == "round_robin":
            return self._round_robin(healthy)
        elif self.config.algorithm == "weighted_round_robin":
            return self._weighted_round_robin(healthy)
        elif self.config.algorithm == "least_connections":
            return self._least_connections(healthy)
        else:
            return healthy[0]
    
    def _round_robin(self, instances: List[ServiceInstance]) -> ServiceInstance:
        service_requests = self.request_distribution.get("default", {})
        total_requests = sum(service_requests.values()) % len(instances)
        return instances[total_requests % len(instances)]
    
    def _weighted_round_robin(self, instances: List[ServiceInstance]) -> ServiceInstance:
        weights = []
        for inst in instances:
            weight = 1.0
            if inst.healthy:
                weight = max(1, 10 - (inst.load_average / 10))
            weights.append(weight)
        
        total_weight = sum(weights)
        r = time.time() % 1
        
        for i, w in enumerate(weights):
            r -= w / total_weight
            if r <= 0:
                return instances[i]
        
        return instances[-1]
    
    def _least_connections(self, instances: List[ServiceInstance]) -> ServiceInstance:
        return min(instances, key=lambda i: self.request_distribution.get(i.name, 0))
    
    def record_request(self, service_name: str, instance: ServiceInstance, success: bool):
        if service_name not in self.request_distribution:
            self.request_distribution[service_name] = {}
        
        if instance.name not in self.request_distribution[service_name]:
            self.request_distribution[service_name][instance.name] = 0
        
        self.request_distribution[service_name][instance.name] += 1
        instance.request_count += 1
        
        if not success:
            instance.error_count += 1
            circuit_breaker = self.circuit_breakers.get(service_name)
            if circuit_breaker:
                circuit_breaker.record_failure()
        else:
            circuit_breaker = self.circuit_breakers.get(service_name)
            if circuit_breaker:
                circuit_breaker.record_success()

@dataclass
class CircuitBreakerState:
    CLOSED = "closed"
    OPEN = "open"
    HALF_OPEN = "half_open"

class CircuitBreaker:
    def __init__(self, threshold: int = 5, timeout: int = 30):
        self.threshold = threshold
        self.timeout = timeout
        self.failure_count = 0
        self.last_failure_time: Optional[datetime] = None
        self.state = CircuitBreakerState.CLOSED
    
    def record_success(self):
        self.failure_count = 0
        self.state = CircuitBreakerState.CLOSED
    
    def record_failure(self):
        self.failure_count += 1
        self.last_failure_time = datetime.now()
        
        if self.failure_count >= self.threshold:
            self.state = CircuitBreakerState.OPEN
    
    def can_execute(self) -> bool:
        if self.state == CircuitBreakerState.CLOSED:
            return True
        
        if self.state == CircuitBreakerState.OPEN:
            if self.last_failure_time and (datetime.now() - self.last_failure_time).seconds > self.timeout:
                self.state = CircuitBreakerState.HALF_OPEN
                return True
            return False
        
        return True

class TrafficManager:
    def __init__(self):
        self.traffic_rates: Dict[str, deque] = {}
        self.dropping_traffic = False
        self.throttle_level = 0
        self.peak_hour_threshold = 1000
    
    async def adaptive_throttling(self, current_rate: int) -> float:
        if current_rate < self.peak_hour_threshold:
            self.throttle_level = 0
            return 1.0
        
        rate_ratio = current_rate / self.peak_hour_threshold
        
        if rate_ratio > 3:
            self.dropping_traffic = True
            self.throttle_level = 3
            return 0.33
        elif rate_ratio > 2:
            self.dropping_traffic = True
            self.throttle_level = 2
            return 0.5
        elif rate_ratio > 1.5:
            self.throttle_level = 1
            return 0.75
        else:
            self.throttle_level = 0
            return 1.0
    
    def should_drop_request(self) -> bool:
        return self.dropping_traffic

class ResourceOptimizer:
    def __init__(self):
        self.memory_threshold = 0.85
        self.cpu_threshold = 0.80
        self.disk_threshold = 0.90
    
    async def get_system_metrics(self) -> dict:
        metrics = {}
        
        try:
            with open("/proc/meminfo", "r") as f:
                meminfo = f.read()
                for line in meminfo.split("\n"):
                    if "MemAvailable" in line:
                        available = int(line.split()[1]) * 1024
                    if "MemTotal" in line:
                        total = int(line.split()[1]) * 1024
                metrics["memory_usage"] = 1 - (available / total)
        except:
            metrics["memory_usage"] = 0.5
        
        try:
            with open("/proc/loadavg", "r") as f:
                load = f.read().split()[0]
                metrics["cpu_load"] = float(load) / os.cpu_count()
        except:
            metrics["cpu_load"] = 0.5
        
        try:
            statvfs = os.statvfs("/")
            metrics["disk_usage"] = 1 - (statvfs.f_bavail / statvfs.f_blocks)
        except:
            metrics["disk_usage"] = 0.5
        
        return metrics
    
    async def check_resource_pressure(self) -> Dict[str, bool]:
        metrics = await self.get_system_metrics()
        pressure = {
            "memory_high": metrics["memory_usage"] > self.memory_threshold,
            "cpu_high": metrics["cpu_load"] > self.cpu_threshold,
            "disk_full": metrics["disk_usage"] > self.disk_threshold
        }
        return pressure

class CrashProtection:
    def __init__(self):
        self.watchdog_interval = 60
        self.last_heartbeat = datetime.now()
        self.process_start_time = datetime.now()
        self.max_uptime = timedelta(hours=24)
        self.restart_on_signal = True
    
    async def periodic_restart_check(self):
        if datetime.now() - self.process_start_time > self.max_uptime:
            logger.warning("Scheduled restart after max uptime")
            return True
        return False
    
    async def detect_crash(self) -> bool:
        time_since_heartbeat = datetime.now() - self.last_heartbeat
        if time_since_heartbeat > timedelta(minutes=5):
            logger.error("Crash detected: No heartbeat for 5 minutes")
            return True
        return False
    
    def update_heartbeat(self):
        self.last_heartbeat = datetime.now()
        self.process_start_time = datetime.now()

class HAHightAvailabilitySystem:
    def __init__(self):
        self.load_balancer = LoadBalancer(LoadBalancerConfig())
        self.traffic_manager = TrafficManager()
        self.resource_optimizer = ResourceOptimizer()
        self.crash_protection = CrashProtection()
        self.health_monitor = HealthMonitor()
        self.running = False
    
    def add_service(self, name: str, host: str, port: int):
        instance = ServiceInstance(name=name, host=host, port=port)
        self.load_balancer.add_instance(name, instance)
        self.health_monitor.instances[name].append(instance)
    
    async def handle_request(self, service_name: str) -> Tuple[bool, Optional[str]]:
        if self.traffic_manager.should_drop_request():
            return False, "Service overloaded"
        
        instance = self.load_balancer.select_instance(service_name)
        if not instance:
            return False, "No healthy instances"
        
        cb = self.load_balancer.circuit_breakers.get(service_name)
        if cb and not cb.can_execute():
            return False, "Circuit breaker open"
        
        metrics = await self.resource_optimizer.get_system_metrics()
        if metrics.get("memory_usage", 0) > 0.95:
            return False, "Memory exhausted"
        
        instance.healthy = True
        self.load_balancer.record_request(service_name, instance, True)
        
        return True, f"http://{instance.host}:{instance.port}"

if __name__ == "__main__":
    ha_system = HAHightAvailabilitySystem()
    
    ha_system.add_service("auth", "localhost", 8001)
    ha_system.add_service("user", "localhost", 8002)
    ha_system.add_service("sales", "localhost", 8007)
    ha_system.add_service("ticket", "localhost", 8008)
    ha_system.add_service("analytics", "localhost", 8012)
    ha_system.add_service("search", "localhost", 8013)
    ha_system.add_service("notification", "localhost", 8014)
    
    print("High Availability System initialized")
    print(f"Managed services: {len(ha_system.health_monitor.instances)}")
    print(f"Features: Load balancing, Circuit breaking, Adaptive throttling, Resource optimization")