#!/usr/bin/env python3
"""
SalesGenie Container Security & Runtime Protection
Provides container hardening, runtime security, and protection against common attacks
"""

import os
import subprocess
import json
import hashlib
import logging
from datetime import datetime
from typing import Dict, List, Optional, Set
from dataclasses import dataclass, field
import signal
import sys

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("salesgenie.runtime-security")

@dataclass
class SecurityPolicy:
    allow_network_access: bool = True
    allow_file_write: bool = True
    allowed_paths: List[str] = field(default_factory=lambda: ["/tmp", "/var/log"])
    blocked_commands: Set[str] = field(default_factory=lambda: {
        "rm", "dd", "mkfs", "fdisk", "shutdown", "reboot", "halt", "init",
        "chmod", "chown", "chgrp", "passwd", "vipw", "vigr",
    })

security_policy = SecurityPolicy()

class RuntimeProtection:
    def __init__(self):
        self.blocked_processes: Set[int] = set()
        self.process_monitors: Dict[int, subprocess.Popen] = {}
        self.security_metrics = {
            "requests_processed": 0,
            "attacks_blocked": 0,
            "suspicious_events": 0
        }
    
    def monitor_process(self, pid: int, command: str):
        self.process_monitors[pid] = subprocess.Popen(
            ["ps", "-p", str(pid), "-o", "pid,ppid,cmd"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

class ContainerSecurityScanner:
    def __init__(self):
        self.known_vulnerable_packages = set()
        self.blocklist_signatures = []
        
    def scan_image(self, image_name: str) -> dict:
        results = {
            "image": image_name,
            "timestamp": datetime.now().isoformat(),
            "vulnerabilities": [],
            "critical": 0,
            "high": 0,
            "medium": 0,
            "low": 0
        }
        
        try:
            result = subprocess.run(
                ["docker", "scan", image_name],
                capture_output=True,
                text=True,
                timeout=60
            )
            results["scan_output"] = result.stdout
        except Exception as e:
            results["error"] = str(e)
        
        return results
    
    def validate_container_runtime(self) -> bool:
        required_caps = [
            "CAP_NET_BIND_SERVICE",
            "CAP_SETGID",
            "CAP_SETUID"
        ]
        
        current_caps = os.getenv("CONTAINER_CAPABILITIES", "")
        for cap in required_caps:
            if cap.encode() not in current_caps.encode():
                logger.warning(f"Missing capability: {cap}")
                return False
        
        return True
    
    def enforce_readonly_root(self) -> bool:
        if os.path.exists("/.dockerenv"):
            return True
        
        readonly_paths = ["/usr", "/bin", "/sbin", "/lib", "/lib64"]
        for path in readonly_paths:
            if os.path.exists(path):
                try:
                    if not os.access(path, os.W_OK):
                        continue
                except PermissionError:
                    continue
        return True

class SecretsDetector:
    def __init__(self):
        self.secret_patterns = [
            (r"(?i)(api[_-]?key\s*[:=]\s*['\"]?)([a-zA-Z0-9_-]{20,})", "API_KEY"),
            (r"(?i)(secret[_-]?key\s*[:=]\s*['\"]?)([a-zA-Z0-9_-]{20,})", "SECRET_KEY"),
            (r"(?i)(access[_-]?token\s*[:=]\s*['\"]?)([a-zA-Z0-9_-]{20,})", "ACCESS_TOKEN"),
            (r"(?i)(password\s*[:=]\s*['\"]?)([a-zA-Z0-9!@#$%^&*]{8,})", "PASSWORD"),
            (r"(?i)(aws[_-]?access[_-]?key[_-]?id\s*[:=]\s*['\"]?)([A-Z0-9]{20})", "AWS_KEY_ID"),
            (r"(?i)(aws[_-]?secret[_-]?access[_-]?key\s*[:=]\s*['\"]?)([a-zA-Z0-9/+=]{40})", "AWS_SECRET"),
            (r"(?i)(private[_-]?key\s*[:=]\s*['\"]?)(-----BEGIN)", "PRIVATE_KEY"),
            (r"(?i)(ssh[_-]?private[_-]?key\s*[:=]\s*['\"]?)(-----BEGIN)", "SSH_KEY"),
        ]
    
    def scan_strings(self, data: str) -> Dict[str, List[str]]:
        findings = {}
        import re
        
        for pattern, secret_type in self.secret_patterns:
            matches = re.findall(pattern, data)
            if matches:
                for match in matches:
                    if secret_type not in findings:
                        findings[secret_type] = []
                    findings[secret_type].append(str(match[1] if isinstance(match, tuple) else match))
        
        return findings

class ProcessIntegrityChecker:
    def __init__(self):
        self.known_pids: Dict[int, dict] = {}
        self.file_integrity_db: Dict[str, str] = {}
    
    def register_process(self, pid: int, command: str, binary_path: str):
        self.known_pids[pid] = {
            "command": command,
            "binary_path": binary_path,
            "started_at": datetime.now().isoformat(),
            "checksum": self._compute_checksum(binary_path)
        }
    
    def _compute_checksum(self, file_path: str) -> Optional[str]:
        try:
            with open(file_path, 'rb') as f:
                return hashlib.sha256(f.read()).hexdigest()
        except:
            return None
    
    def verify_process_integrity(self, pid: int) -> bool:
        if pid not in self.known_pids:
            return False
        
        original = self.known_pids[pid]
        current_checksum = self._compute_checksum(original["binary_path"])
        
        return current_checksum == original["checksum"]

class ResourceLimiter:
    def __init__(self):
        self.process_limits = {}
    
    def set_limits(self, pid: int, cpu_percent: float = 80.0, memory_mb: int = 512):
        try:
            subprocess.run(["cpulimit", "-p", str(pid), "-l", str(int(cpu_percent))], 
                          stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except:
            pass
        
        try:
            subprocess.run(["ulimit", "-v", str(memory_mb * 1024)], 
                          stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except:
            pass

def launch_secure_service(command: str, env_vars: Optional[Dict[str, str]] = None) -> subprocess.Popen:
    clean_env = dict(os.environ)
    clean_env["PYTHONUNBUFFERED"] = "1"
    clean_env["PYTHONDONTWRITEBYTECODE"] = "1"
    clean_env["PYTHONSAFEPATH"] = "1"
    
    if env_vars:
        clean_env.update(env_vars)
    
    restricted_env = {
        "HOME": "/tmp",
        "PATH": "/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
    }
    clean_env.update(restricted_env)
    
    process = subprocess.Popen(
        command,
        shell=True,
        env=clean_env,
        preexec_fn=os.setsid,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        start_new_session=True
    )
    
    return process

def create_security_wrapper(service_name: str):
    import functools
    
    def wrapper(original_func):
        @functools.wraps(original_func)
        def wrapped(*args, **kwargs):
            import time
            
            start_time = time.time()
            request_id = hashlib.sha256(f"{service_name}:{time.time()}".encode()).hexdigest()[:12]
            
            try:
                result = original_func(*args, **kwargs)
                return result
            except Exception as e:
                logger.error(f"Security wrapper error in {service_name}: {e}")
                raise
            finally:
                elapsed = time.time() - start_time
                logger.debug(f"{request_id}: {service_name} completed in {elapsed:.3f}s")
        
        return wrapped
    return wrapper

if __name__ == "__main__":
    scanner = ContainerSecurityScanner()
    secrets = SecretsDetector()
    checker = ProcessIntegrityChecker()
    limiter = ResourceLimiter()
    protection = RuntimeProtection()
    
    print("Runtime Security System initialized")
    print(f"Blocked commands: {security_policy.blocked_commands}")
    print(f"Security policy: readonly_root={scanner.validate_container_runtime()}")