#!/usr/bin/env python3
"""
SalesGenie Advanced Security Protection System
Provides DDoS protection, rate limiting, intrusion detection, and data leak prevention
"""

import asyncio
import time
import hashlib
import hmac
import ipaddress
import logging
from typing import Dict, Set, Optional, Tuple
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from collections import defaultdict
import re
import json
from enum import Enum

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("salesgenie.security")

class ThreatLevel(Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"

@dataclass
class SecurityEvent:
    timestamp: datetime
    source_ip: str
    event_type: str
    threat_level: ThreatLevel
    details: dict
    blocked: bool = False

@dataclass
class RateLimitRule:
    max_requests: int
    window_seconds: int
    burst_size: int = 10

@dataclass
class IPBlock:
    ip: str
    blocked_until: datetime
    reason: str
    threat_level: ThreatLevel

class AdvancedSecurityManager:
    def __init__(self):
        self.rate_limits: Dict[str, list] = defaultdict(list)
        self.ip_blocks: Dict[str, IPBlock] = {}
        self.security_events: list = []
        self.whitelisted_ips: Set[str] = set()
        self.blacklisted_ips: Set[str] = set()
        self.global_request_count = 0
        self.start_time = datetime.now()
        
        self.global_rate_limit = RateLimitRule(max_requests=100000, window_seconds=60)
        self.ip_rate_limit = RateLimitRule(max_requests=1000, window_seconds=60, burst_size=100)
        self.endpoint_rate_limits: Dict[str, RateLimitRule] = {}
        
        self._setup_default_rules()
    
    def _setup_default_rules(self):
        self.endpoint_rate_limits = {
            "/api/v1/auth/login": RateLimitRule(max_requests=10, window_seconds=60),
            "/api/v1/auth/register": RateLimitRule(max_requests=5, window_seconds=60),
            "/api/v1/llm/chat": RateLimitRule(max_requests=60, window_seconds=60),
            "/api/v1/webhooks": RateLimitRule(max_requests=100, window_seconds=60),
            "/api/v1/documents/upload": RateLimitRule(max_requests=20, window_seconds=60),
        }
        
        self.whitelisted_ips = {
            "127.0.0.1",
            "::1",
            "10.0.0.0/8",
            "172.16.0.0/12",
            "192.168.0.0/16",
        }
    
    def is_ip_whitelisted(self, ip: str) -> bool:
        try:
            ip_obj = ipaddress.ip_address(ip)
            for cidr in self.whitelisted_ips:
                if "/" in cidr:
                    if ip_obj in ipaddress.ip_network(cidr, strict=False):
                        return True
                elif ip == cidr:
                    return True
        except ValueError:
            pass
        return False
    
    def is_ip_blacklisted(self, ip: str) -> bool:
        return ip in self.blacklisted_ips or ip in self.ip_blocks
    
    def block_ip(self, ip: str, reason: str, duration_minutes: int, threat_level: ThreatLevel):
        block = IPBlock(
            ip=ip,
            blocked_until=datetime.now() + timedelta(minutes=duration_minutes),
            reason=reason,
            threat_level=threat_level
        )
        self.ip_blocks[ip] = block
        logger.warning(f"Blocked IP {ip} for {duration_minutes} minutes - Reason: {reason}")
        
        event = SecurityEvent(
            timestamp=datetime.now(),
            source_ip=ip,
            event_type="ip_blocked",
            threat_level=threat_level,
            details={"reason": reason, "duration_minutes": duration_minutes}
        )
        self.security_events.append(event)
    
    def check_rate_limit(self, ip: str, endpoint: str) -> Tuple[bool, Optional[int]]:
        now = time.time()
        
        if self.is_ip_blacklisted(ip):
            return False, 0
        
        if self.global_request_count > self.global_rate_limit.max_requests:
            return False, 0
        
        global_window = now - self.global_rate_limit.window_seconds
        self.rate_limits[f"global"].clear()
        self.rate_limits[f"global"].append(now)
        
        ip_key = f"{ip}:{endpoint}"
        ip_window = now - self.ip_rate_limit.window_seconds
        self.rate_limits[ip_key] = [t for t in self.rate_limits[ip_key] if t > ip_window]
        
        if len(self.rate_limits[ip_key]) > self.ip_rate_limit.max_requests:
            return False, 0
        
        if endpoint in self.endpoint_rate_limits:
            rule = self.endpoint_rate_limits[endpoint]
            endpoint_window = now - rule.window_seconds
            self.rate_limits[endpoint] = [t for t in self.rate_limits[endpoint] if t > endpoint_window]
            if len(self.rate_limits[endpoint]) > rule.max_requests:
                return False, 0
        
        self.rate_limits[ip_key].append(now)
        remaining = self.ip_rate_limit.max_requests - len(self.rate_limits[ip_key])
        return True, remaining
    
    def detect_ddos(self, requests: list, window_seconds: int = 60) -> Tuple[bool, int]:
        now = time.time()
        recent = [r for r in requests if r >= now - window_seconds]
        request_rate = len(recent) / window_seconds
        
        if request_rate > 500:
            return True, len(recent)
        elif request_rate > 200:
            return True, len(recent)
        elif request_rate > 100:
            return True, len(recent)
        
        return False, 0
    
    def detect_brute_force(self, attempts: list, window_seconds: int = 300, max_attempts: int = 10) -> Tuple[bool, int]:
        now = time.time()
        recent = [a for a in attempts if a >= now - window_seconds]
        
        if len(recent) >= max_attempts:
            return True, len(recent)
        
        return False, 0
    
    def sanitize_input(self, data: str) -> str:
        dangerous_patterns = [
            r"<script[^>]*>.*?</script>",
            r"javascript:",
            r"on\w+\s*=",
            r"<iframe",
            r"<object",
            r"<embed",
            r"<form",
            r"<input",
            r"<img[^>]*onerror",
            r"<svg[^>]*onload",
        ]
        
        sanitized = data
        for pattern in dangerous_patterns:
            sanitized = re.sub(pattern, "", sanitized, flags=re.IGNORECASE)
        
        return sanitized.strip()
    
    def detect_sql_injection(self, input_str: str) -> bool:
        sql_patterns = [
            r"(?i)(\b(SELECT|INSERT|UPDATE|DELETE|DROP|CREATE|ALTER|TRUNCATE)\b)",
            r"(?i)(--|#|/\*|\*/)",
            r"(?i)(OR\s+1\s*=\s*1)",
            r"(?i)(UNION\s+SELECT)",
            r"(?i)(\'\s*OR\s*\')",
            r"(?i)(EXEC\s*\()",
            r"(?i)(xp_cmdshell)",
        ]
        
        for pattern in sql_patterns:
            if re.search(pattern, input_str):
                return True
        return False
    
    def mask_sensitive_data(self, data: dict) -> dict:
        sensitive_keys = [
            "password", "token", "api_key", "secret", "credential",
            "private_key", "access_token", "refresh_token", "auth",
            "credit_card", "ssn", "social_security", "bank_account"
        ]
        
        masked = data.copy()
        for key, value in masked.items():
            if any(sensitive in key.lower() for sensitive in sensitive_keys):
                if isinstance(value, str):
                    masked[key] = "****MASKED****"
                elif isinstance(value, dict):
                    masked[key] = self.mask_sensitive_data(value)
        
        return masked
    
    def generate_request_id(self, ip: str, user_agent: str) -> str:
        data = f"{ip}:{user_agent}:{time.time()}"
        return hashlib.sha256(data.encode()).hexdigest()[:16]
    
    def log_security_event(self, event: SecurityEvent):
        self.security_events.append(event)
        logger.info(f"Security Event [{event.threat_level.value}]: {event.event_type} from {event.source_ip}")
        
        if event.threat_level in [ThreatLevel.HIGH, ThreatLevel.CRITICAL]:
            with open("/var/log/salesgenie/security.log", "a") as f:
                f.write(json.dumps({
                    "timestamp": event.timestamp.isoformat(),
                    "source_ip": event.source_ip,
                    "event_type": event.event_type,
                    "threat_level": event.threat_level.value,
                    "details": event.details,
                    "blocked": event.blocked
                }) + "\n")

class DDoSProtection:
    def __init__(self, max_requests_per_second: int = 100):
        self.max_rps = max_requests_per_second
        self.request_counts: Dict[str, list] = defaultdict(list)
        self.alerted_ips: Set[str] = set()
    
    def check_protection(self, ip: str) -> bool:
        now = time.time()
        window = now - 1
        
        self.request_counts[ip] = [t for t in self.request_counts[ip] if t > window]
        self.request_counts[ip].append(now)
        
        rps = len(self.request_counts[ip])
        
        if rps > self.max_rps * 2:
            return False
        elif rps > self.max_rps * 1.5 and ip not in self.alerted_ips:
            self.alerted_ips.add(ip)
        return True

class WAFRules:
    def __init__(self):
        self.rules = [
            self._block_sql_injection,
            self._block_xss,
            self._block_path_traversal,
            self._block_prohibited_methods,
        ]
    
    def _block_sql_injection(self, request_path: str, headers: dict, body: str) -> bool:
        sqli_patterns = [
            r"(?i)(UNION\s+SELECT)",
            r"(?i)(OR\s+1\s*=\s*1)",
            r"(?i)(SELECT\s+.*\s+FROM)",
            r"(?i)(DROP\s+TABLE)",
            r"(?i)(INSERT\s+INTO)",
        ]
        
        all_data = f"{request_path} {headers.get('User-Agent', '')} {body}"
        for pattern in sqli_patterns:
            if re.search(pattern, all_data):
                return True
        return False
    
    def _block_xss(self, request_path: str, headers: dict, body: str) -> bool:
        xss_patterns = [
            r"(?i)<script[^>]*>",
            r"(?i)javascript:",
            r"(?i)on\w+\s*=",
            r"(?i)<iframe",
            r"(?i)<object",
            r"(?i)<embed",
        ]
        
        all_data = f"{request_path} {headers.get('User-Agent', '')} {body}"
        for pattern in xss_patterns:
            if re.search(pattern, all_data):
                return True
        return False
    
    def _block_path_traversal(self, request_path: str) -> bool:
        traversal_patterns = [
            r"\.\./",
            r"\.\.\\",
            r"%2e%2e%2f",
            r"%2e%2e/",
            r"\.\.%2f",
        ]
        
        for pattern in traversal_patterns:
            if re.search(pattern, request_path, re.IGNORECASE):
                return True
        return False
    
    def _block_prohibited_methods(self, method: str) -> bool:
        prohibited = ["TRACE", "TRACK", "CONNECT"]
        return method.upper() in prohibited
    
    def check_request(self, method: str, path: str, headers: dict, body: str = "") -> bool:
        for rule in self.rules:
            if rule(path, headers, body):
                return False
        return True

if __name__ == "__main__":
    security = AdvancedSecurityManager()
    waf = WAFRules()
    ddos = DDoSProtection()
    
    print("Security Protection System initialized")
    print(f"Rate limits configured for: {list(security.endpoint_rate_limits.keys())}")
    print(f"WAF rules active: {len(waf.rules)}")
    print(f"DDoS protection threshold: {ddos.max_rps} requests/second")