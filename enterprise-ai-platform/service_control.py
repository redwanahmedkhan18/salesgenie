#!/usr/bin/env python3
"""
SalesGenie Service Control Panel
Control any microservice: Restart, Stop, Start, Maintenance Mode, Logs
"""

import asyncio
import aiohttp
import logging
from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, List, Optional, Any
import subprocess
import os
import signal
import hashlib

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("salesgenie.service-control")

@dataclass
class ServiceStatus:
    name: str
    port: int
    status: str
    pid: Optional[int] = None
    memory_mb: float = 0.0
    cpu_percent: float = 0.0
    uptime: str = "0s"
    errors: int = 0
    last_error: Optional[str] = None

class ServiceController:
    def __init__(self):
        self.services = self._load_services_config()
        self.maintenance_mode: Dict[str, bool] = {}
    
    def _load_services_config(self) -> Dict[str, Dict]:
        return {
            "auth_service": {"port": 8001, "command": "python3 -m uvicorn enterprise_ai_platform.auth_service.main:app --host 0.0.0.0 --port 8001 --reload"},
            "user_service": {"port": 8002, "command": "python3 -m uvicorn enterprise_ai_platform.user_service.main:app --host 0.0.0.0 --port 8002 --reload"},
            "organization_service": {"port": 8003, "command": "python3 -m uvicorn enterprise_ai_platform.organization_service.main:app --host 0.0.0.0 --port 8003 --reload"},
            "billing_service": {"port": 8004, "command": "python3 -m uvicorn enterprise_ai_platform.billing_service.main:app --host 0.0.0.0 --port 8004 --reload"},
            "ai_gateway_service": {"port": 8000, "command": "python3 -m uvicorn enterprise_ai_platform.ai_gateway_service.main:app --host 0.0.0.0 --port 8000 --reload"},
            "whatsapp_service": {"port": 8005, "command": "python3 -m uvicorn enterprise_ai_platform.whatsapp_service.main:app --host 0.0.0.0 --port 8005 --reload"},
            "knowledge_service": {"port": 8006, "command": "python3 -m uvicorn enterprise_ai_platform.knowledge_service.main:app --host 0.0.0.0 --port 8006 --reload"},
            "sales_service": {"port": 8007, "command": "python3 -m uvicorn enterprise_ai_platform.sales_service.main:app --host 0.0.0.0 --port 8007 --reload"},
            "ticket_service": {"port": 8008, "command": "python3 -m uvicorn enterprise_ai_platform.ticket_service.main:app --host 0.0.0.0 --port 8008 --reload"},
            "vector_service": {"port": 8009, "command": "python3 -m uvicorn enterprise_ai_platform.vector_service.main:app --host 0.0.0.0 --port 8009 --reload"},
            "chat_service": {"port": 8010, "command": "python3 -m uvicorn enterprise_ai_platform.chat_service.main:app --host 0.0.0.0 --port 8010 --reload"},
            "workflow_service": {"port": 8011, "command": "python3 -m uvicorn enterprise_ai_platform.workflow_service.main:app --host 0.0.0.0 --port 8011 --reload"},
            "slack_service": {"port": 8024, "command": "python3 -m uvicorn slack-service.main:app --host 0.0.0.0 --port 8024 --reload"},
            "discord_service": {"port": 8026, "command": "python3 -m uvicorn discord-service.main:app --host 0.0.0.0 --port 8026 --reload"},
        }
    
    def get_service_list(self) -> List[Dict[str, Any]]:
        services = []
        for name, config in self.services.items():
            status = self._check_service_status(name, config)
            services.append({
                "name": name,
                "port": config["port"],
                "status": status.status,
                "maintenance": self.maintenance_mode.get(name, False),
                "command": config["command"]
            })
        return services
    
    def _check_service_status(self, name: str, config: Dict) -> ServiceStatus:
        import socket
        
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex(('localhost', config["port"]))
        sock.close()
        
        is_running = result == 0
        pid = self._find_pid(config["port"]) if is_running else None
        
        return ServiceStatus(
            name=name,
            port=config["port"],
            status="running" if is_running else "stopped",
            pid=pid,
            cpu_percent=0.0,
            memory_mb=0.0,
            uptime="0s"
        )
    
    def _find_pid(self, port: int) -> Optional[int]:
        try:
            result = subprocess.run(
                ["lsof", "-i", f":{port}", "-t"],
                capture_output=True, text=True, timeout=5
            )
            if result.returncode == 0 and result.stdout.strip():
                return int(result.stdout.strip().split('\n')[0])
        except:
            pass
        return None
    
    async def start_service(self, name: str, user: str) -> Dict[str, Any]:
        self.audit_log("service_start", user, name)
        
        if name not in self.services:
            return {"success": False, "error": "Service not found"}
        
        config = self.services[name]
        
        if self._is_running(config["port"]):
            return {"success": False, "error": "Service already running"}
        
        try:
            subprocess.Popen(
                config["command"].split(),
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                start_new_session=True
            )
            
            await asyncio.sleep(2)
            
            if self._is_running(config["port"]):
                return {
                    "success": True,
                    "message": f"Service {name} started",
                    "pid": self._find_pid(config["port"]),
                    "port": config["port"]
                }
            else:
                return {"success": False, "error": "Service failed to start"}
                
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    async def stop_service(self, name: str, user: str) -> Dict[str, Any]:
        self.audit_log("service_stop", user, name)
        
        if name not in self.services:
            return {"success": False, "error": "Service not found"}
        
        config = self.services[name]
        pid = self._find_pid(config["port"])
        
        if not pid:
            return {"success": False, "error": "Service not running"}
        
        try:
            os.kill(pid, signal.SIGTERM)
            await asyncio.sleep(1)
            
            if self._is_running(config["port"]):
                os.kill(pid, signal.SIGKILL)
                await asyncio.sleep(1)
            
            if not self._is_running(config["port"]):
                return {"success": True, "message": f"Service {name} stopped"}
            else:
                return {"success": False, "error": "Failed to stop service"}
                
        except ProcessLookupError:
            return {"success": True, "message": f"Service {name} already stopped"}
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    async def restart_service(self, name: str, user: str, rolling: bool = False) -> Dict[str, Any]:
        self.audit_log("service_restart", user, name)
        
        if name not in self.services:
            return {"success": False, "error": "Service not found"}
        
        stop_result = await self.stop_service(name, user)
        await asyncio.sleep(2)
        
        start_result = await self.start_service(name, user)
        
        if start_result.get("success"):
            return {
                "success": True,
                "message": f"Service {name} restarted successfully",
                "old_pid": stop_result.get("pid"),
                "new_pid": start_result.get("pid"),
                "port": start_result.get("port")
            }
        else:
            return {"success": False, "error": f"Restart failed: {start_result.get('error')}"}
    
    def set_maintenance_mode(self, name: str, enabled: bool, user: str) -> Dict[str, Any]:
        self.audit_log("maintenance_mode", user, f"{name}={enabled}")
        
        if name not in self.services:
            return {"success": False, "error": "Service not found"}
        
        self.maintenance_mode[name] = enabled
        
        return {
            "success": True,
            "message": f"Maintenance mode {'enabled' if enabled else 'disabled'} for {name}"
        }
    
    def health_check(self, name: str) -> Dict[str, Any]:
        if name not in self.services:
            return {"status": "unknown", "error": "Service not found"}
        
        config = self.services[name]
        status = self._check_service_status(name, config)
        
        return {
            "status": status.status,
            "port": config["port"],
            "pid": status.pid,
            "uptime": status.uptime,
            "response_time_ms": status.response_time_ms if hasattr(status, 'response_time_ms') else 0
        }
    
    def get_service_logs(self, name: str, lines: int = 100, tail: bool = True) -> Dict[str, Any]:
        if name not in self.services:
            return {"success": False, "error": "Service not found"}
        
        log_path = f"/var/log/salesgenie/{name}.log"
        
        try:
            if not os.path.exists(log_path):
                return {"success": True, "logs": [], "message": "No logs available"}
            
            with open(log_path, 'r') as f:
                if tail:
                    lines_list = f.readlines()[-lines:]
                else:
                    lines_list = f.readlines()[:lines]
            
            return {
                "success": True,
                "logs": [line.strip() for line in lines_list],
                "line_count": len(lines_list),
                "file": log_path
            }
            
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    def download_logs(self, name: str) -> Dict[str, Any]:
        if name not in self.services:
            return {"success": False, "error": "Service not found"}
        
        log_path = f"/var/log/salesgenie/{name}.log"
        
        try:
            if not os.path.exists(log_path):
                return {"success": False, "error": "No logs available"}
            
            with open(log_path, 'rb') as f:
                content = f.read()
            
            return {
                "success": True,
                "content": content.decode('utf-8', errors='ignore'),
                "size_bytes": len(content),
                "file": log_path
            }
            
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    async def rolling_restart(self, service_names: List[str], user: str) -> Dict[str, Any]:
        results = []
        
        for name in service_names:
            result = await self.restart_service(name, user, rolling=True)
            results.append({"service": name, "result": result})
            await asyncio.sleep(5)
        
        failed = [r for r in results if not r["result"].get("success")]
        
        return {
            "success": len(failed) == 0,
            "results": results,
            "failed_count": len(failed)
        }
    
    def audit_log(self, action: str, user: str, service: str):
        import json
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "action": action,
            "user": user,
            "service": service,
            "request_id": hashlib.sha256(f"{user}{datetime.now().isoformat()}".encode()).hexdigest()[:12]
        }
        
        audit_path = "/var/log/salesgenie/audit.log"
        os.makedirs(os.path.dirname(audit_path), exist_ok=True)
        
        with open(audit_path, 'a') as f:
            f.write(json.dumps(log_entry) + "\n")
    
    def _is_running(self, port: int) -> bool:
        import socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex(('localhost', port))
        sock.close()
        return result == 0

if __name__ == "__main__":
    controller = ServiceController()
    
    print("=" * 60)
    print("SalesGenie Service Control Panel")
    print("=" * 60)
    
    services = controller.get_service_list()
    print(f"\nManaged Services: {len(services)}")
    print("-" * 60)
    for svc in services:
        status_icon = "✓" if svc["status"] == "running" else "✗"
        maint_icon = " [MAINT]" if svc["maintenance"] else ""
        print(f"{status_icon} {svc['name']:20} Port {svc['port']:5} {maint_icon}")
    
    print("\nAvailable Commands:")
    print("  controller.start_service('auth_service', 'admin')")
    print("  controller.stop_service('ticket_service', 'admin')")
    print("  controller.restart_service('slack_service', 'admin')")
    print("  controller.set_maintenance_mode('sales_service', True, 'admin')")
    print("  controller.get_service_logs('auth_service', lines=50)")
    print("  controller.health_check('postgres')")
    print("  controller.rolling_restart(['sales', 'ticket'], 'admin')")