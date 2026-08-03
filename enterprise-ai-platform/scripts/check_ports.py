#!/usr/bin/env python3
"""
Port and Service Health Checker for SalesGenie Platform
Validates all microservices are running and ports are accessible.
"""

import asyncio
import aiohttp
from typing import Dict, List, Tuple
from dataclasses import dataclass
import socket

@dataclass
class ServiceStatus:
    name: str
    port: int
    expected: bool
    status: str  # running, stopped, error
    response_time_ms: float
    details: str = ""

SERVICES = [
    {"name": "AI Gateway Service", "port": 8000, "endpoint": "/api/v1/gateway/models"},
    {"name": "Auth Service", "port": 8001, "endpoint": "/api/v1/auth/me"},
    {"name": "User Service", "port": 8002, "endpoint": "/api/v1/users/me"},
    {"name": "Organization Service", "port": 8003, "endpoint": "/api/v1/organizations"},
    {"name": "Billing Service", "port": 8004, "endpoint": "/api/v1/billing/plans"},
    {"name": "WhatsApp Service", "port": 8005, "endpoint": "/api/v1/whatsapp/accounts"},
    {"name": "Knowledge Service", "port": 8006, "endpoint": "/api/v1/knowledge/categories"},
    {"name": "Sales Service", "port": 8007, "endpoint": "/api/v1/sales/health"},
    {"name": "Ticket Service", "port": 8008, "endpoint": "/api/v1/tickets"},
    {"name": "Vector Service", "port": 8009, "endpoint": "/health"},
    {"name": "Chat Service", "port": 8010, "endpoint": "/api/v1/chat/health"},
    {"name": "Workflow Service", "port": 8011, "endpoint": "/api/v1/workflows"},
    {"name": "Analytics Service", "port": 8012, "endpoint": "/api/v1/analytics/kpis"},
    {"name": "Search Service", "port": 8013, "endpoint": "/api/v1/search/stats"},
    {"name": "Notification Service", "port": 8014, "endpoint": "/api/v1/notifications/settings"},
    {"name": "File Service", "port": 8015, "endpoint": "/api/v1/files/upload"},
    {"name": "Customer Service", "port": 8016, "endpoint": "/api/v1/customers"},
    {"name": "Support Service", "port": 8017, "endpoint": "/api/v1/support/health"},
    {"name": "Conversation Service", "port": 8018, "endpoint": "/api/v1/conversations"},
    {"name": "Telegram Service", "port": 8019, "endpoint": "/api/v1/telegram/bots"},
    {"name": "Messenger Service", "port": 8020, "endpoint": "/api/v1/messenger/config"},
    {"name": "Email Service", "port": 8021, "endpoint": "/api/v1/email/templates"},
    {"name": "Lead Intelligence Service", "port": 8022, "endpoint": "/api/v1/lead-intelligence/profiles"},
    {"name": "Audit Service", "port": 8023, "endpoint": "/api/v1/audit/logs"},
    {"name": "Slack Service", "port": 8024, "endpoint": "/api/v1/slack/integrations"},
    {"name": "Discord Service", "port": 8026, "endpoint": "/api/v1/discord/integrations"},
]


async def check_port_open(port: int, host: str = 'localhost') -> bool:
    """Check if a port is open."""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)
        result = sock.connect_ex((host, port))
        sock.close()
        return result == 0
    except Exception:
        return False


async def check_http_endpoint(
    session: aiohttp.ClientSession, 
    port: int, 
    endpoint: str,
    timeout: float = 5.0
) -> Tuple[str, float, str]:
    """Check HTTP endpoint health."""
    url = f"http://localhost:{port}{endpoint}"
    start_time = asyncio.get_event_loop().time()
    
    try:
        async with session.get(url, timeout=aiohttp.ClientTimeout(total=timeout)) as response:
            elapsed = (asyncio.get_event_loop().time() - start_time) * 1000
            if response.status == 200:
                return "running", elapsed, "OK"
            else:
                return "error", elapsed, f"HTTP {response.status}"
    except asyncio.TimeoutError:
        elapsed = (asyncio.get_event_loop().time() - start_time) * 1000
        return "error", elapsed, "Timeout"
    except aiohttp.ClientError as e:
        elapsed = (asyncio.get_event_loop().time() - start_time) * 1000
        return "error", elapsed, str(e)
    except Exception as e:
        elapsed = (asyncio.get_event_loop().time() - start_time) * 1000
        return "error", elapsed, str(e)


async def check_service(service: Dict, session: aiohttp.ClientSession) -> ServiceStatus:
    """Check a single service's status."""
    port_open = await check_port_open(service['port'])
    
    if not port_open:
        return ServiceStatus(
            name=service['name'],
            port=service['port'],
            expected=True,
            status="stopped",
            response_time_ms=0,
            details="Port not open"
        )
    
    status, response_time, details = await check_http_endpoint(
        session, 
        service['port'], 
        service['endpoint']
    )
    
    return ServiceStatus(
        name=service['name'],
        port=service['port'],
        expected=True,
        status=status,
        response_time_ms=response_time,
        details=details
    )


async def check_all_services() -> List[ServiceStatus]:
    """Check all services concurrently."""
    async with aiohttp.ClientSession() as session:
        tasks = [check_service(service, session) for service in SERVICES]
        results = await asyncio.gather(*tasks, return_exceptions=True)
        
        statuses = []
        for result in results:
            if isinstance(result, Exception):
                # Fallback: check if port is open
                port_open = await check_port_open(SERVICES[len(statuses)]['port'])
                statuses.append(ServiceStatus(
                    name=SERVICES[len(statuses)]['name'],
                    port=SERVICES[len(statuses)]['port'],
                    expected=True,
                    status="stopped" if not port_open else "unknown",
                    response_time_ms=0,
                    details=str(result)
                ))
            else:
                statuses.append(result)
        
        return statuses


def print_report(statuses: List[ServiceStatus]) -> None:
    """Print a formatted health report."""
    print("\n" + "="*60)
    print("SALESGENIE PLATFORM HEALTH CHECK")
    print("="*60 + "\n")
    
    running = sum(1 for s in statuses if s.status == "running")
    total = len(statuses)
    
    print(f"Overall Status: {running}/{total} services running\n")
    
    for status in statuses:
        symbol = "✓" if status.status == "running" else "✗"
        color_code = "\033[92m" if status.status == "running" else "\033[91m" if status.status == "error" else "\033[93m"
        reset_code = "\033[0m"
        
        print(f"{color_code}{symbol}{reset_code} {status.name:<30} "
              f"Port {status.port:<5} "
              f"{status.status:<10} "
              f"{status.response_time_ms:.1f}ms" +
              (f" - {status.details}" if status.details else ""))
    
    print("\n" + "-"*60)
    print("\nPort Summary:")
    
    port_status = {}
    for s in statuses:
        port_status[s.port] = s.status
    
    for port, status in sorted(port_status.items()):
        print(f"  Port {port}: {status}")
    
    print("\n")


async def main():
    """Main entry point."""
    statuses = await check_all_services()
    print_report(statuses)
    
    # Return exit code based on health
    running = sum(1 for s in statuses if s.status == "running")
    return 0 if running == len(statuses) else 1


if __name__ == "__main__":
    exit_code = asyncio.run(main())
    exit(exit_code)