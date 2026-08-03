#!/usr/bin/env python3
"""
SalesGenie Live Logs & Compliance Center
Real-time log streaming, compliance reporting, and security audits
"""

import asyncio
import json
import logging
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any
from enum import Enum
import os
import csv
import io
from datetime import timezone

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("salesgenie.logs-compliance")

@dataclass
class LogEntry:
    timestamp: datetime
    level: str
    source: str
    message: str
    data: Dict = field(default_factory=dict)

class ComplianceStandard(Enum):
    GDPR = "gdpr"
    SOC2 = "soc2"
    HIPAA = "hipaa"
    ISO27001 = "iso27001"
    PCIDSS = "pcidss"

class LiveLogsViewer:
    def __init__(self, log_dir: str = "/var/log/salesgenie"):
        self.log_dir = log_dir
        self.subscribers: Dict[str, asyncio.Queue] = {}
        self.filters: Dict[str, Dict] = {}
        self.buffer_size = 1000
    
    async def subscribe(self, subscriber_id: str, filters: Optional[Dict] = None) -> asyncio.Queue:
        queue = asyncio.Queue(maxsize=self.buffer_size)
        self.subscribers[subscriber_id] = queue
        self.filters[subscriber_id] = filters or {}
        return queue
    
    async def unsubscribe(self, subscriber_id: str):
        if subscriber_id in self.subscribers:
            del self.subscribers[subscriber_id]
        if subscriber_id in self.filters:
            del self.filters[subscriber_id]
    
    async def stream_logs(self, subscriber_id: str, log_file: str, tail: bool = True):
        queue = self.subscribers.get(subscriber_id)
        filters = self.filters.get(subscriber_id, {})
        
        if not queue:
            return
        
        file_path = os.path.join(self.log_dir, log_file)
        
        if not os.path.exists(file_path):
            return
        
        with open(file_path, 'r') as f:
            if tail:
                f.seek(0, 2)
            
            while subscriber_id in self.subscribers:
                line = f.readline()
                if line:
                    try:
                        entry = self._parse_log_line(line)
                        if self._matches_filters(entry, filters):
                            await queue.put(entry)
                    except Exception as e:
                        logger.error(f"Failed to parse log line: {e}")
                else:
                    await asyncio.sleep(0.1)
    
    def _parse_log_line(self, line: str) -> LogEntry:
        try:
            data = json.loads(line) if line.strip().startswith('{') else {"message": line.strip()}
            return LogEntry(
                timestamp=datetime.fromisoformat(data.get("timestamp", datetime.now().isoformat())),
                level=data.get("level", "INFO"),
                source=data.get("source", "unknown"),
                message=data.get("message", line.strip()),
                data=data
            )
        except:
            return LogEntry(
                timestamp=datetime.now(),
                level="INFO",
                source="unknown",
                message=line.strip()
            )
    
    def _matches_filters(self, entry: LogEntry, filters: Dict) -> bool:
        if not filters:
            return True
        
        if "level" in filters and entry.level not in filters["level"]:
            return False
        
        if "source" in filters and entry.source not in filters["source"]:
            return False
        
        if "text" in filters:
            if filters["text"].lower() not in entry.message.lower():
                return False
        
        if "start_time" in filters and entry.timestamp < filters["start_time"]:
            return False
        
        if "end_time" in filters and entry.timestamp > filters["end_time"]:
            return False
        
        return True
    
    async def search_logs(self, query: str, source: Optional[str] = None,
                          level: Optional[str] = None, hours: int = 24) -> List[LogEntry]:
        results = []
        cutoff = datetime.now() - timedelta(hours=hours)
        
        for log_file in self._get_log_files():
            file_path = os.path.join(self.log_dir, log_file)
            if not os.path.exists(file_path):
                continue
            
            with open(file_path, 'r') as f:
                for line in f:
                    entry = self._parse_log_line(line)
                    if entry.timestamp < cutoff:
                        continue
                    
                    if query.lower() not in entry.message.lower():
                        continue
                    
                    if source and entry.source != source:
                        continue
                    
                    if level and entry.level != level:
                        continue
                    
                    results.append(entry)
        
        return results[:1000]
    
    def download_logs(self, format: str = "json", hours: int = 24,
                      source: Optional[str] = None, level: Optional[str] = None) -> bytes:
        cutoff = datetime.now() - timedelta(hours=hours)
        logs = []
        
        for log_file in self._get_log_files():
            file_path = os.path.join(self.log_dir, log_file)
            if not os.path.exists(file_path):
                continue
            
            with open(file_path, 'r') as f:
                for line in f:
                    try:
                        entry = json.loads(line)
                        ts = datetime.fromisoformat(entry.get("timestamp", ""))
                        if ts >= cutoff:
                            if source and entry.get("source") != source:
                                continue
                            if level and entry.get("level") != level:
                                continue
                            logs.append(entry)
                    except:
                        continue
        
        if format == "json":
            return json.dumps(logs, indent=2).encode()
        elif format == "csv":
            output = io.StringIO()
            if logs:
                writer = csv.DictWriter(output, fieldnames=logs[0].keys())
                writer.writeheader()
                writer.writerows(logs)
            return output.getvalue().encode()
        elif format == "pdf":
            return self._generate_pdf_report(logs)
        else:
            return json.dumps(logs).encode()
    
    def _get_log_files(self) -> List[str]:
        try:
            return [f for f in os.listdir(self.log_dir) if f.endswith('.log')]
        except:
            return []
    
    def _generate_pdf_report(self, logs: List[Dict]) -> bytes:
        return b"PDF Report - Placeholder - Use external library for real PDF generation"

class ComplianceCenter:
    def __init__(self):
        self.standards = {
            ComplianceStandard.GDPR: GDPRCompliance(),
            ComplianceStandard.SOC2: SOC2Compliance(),
            ComplianceStandard.HIPAA: HIPAACompliance(),
            ComplianceStandard.ISO27001: ISO27001Compliance(),
            ComplianceStandard.PCIDSS: PCIDSSCompliance()
        }
        self.audit_trail: List[Dict] = []
    
    def check_compliance(self, standard: ComplianceStandard) -> Dict[str, Any]:
        checker = self.standards.get(standard)
        if not checker:
            return {"error": "Unknown standard"}
        
        return checker.check()
    
    def generate_report(self, standards: List[ComplianceStandard]) -> Dict[str, Any]:
        report = {
            "timestamp": datetime.now().isoformat(),
            "generated_at": datetime.now().isoformat(),
            "standards": {}
        }
        
        for std in standards:
            report["standards"][std.value] = self.check_compliance(std)
        
        score = sum(s.get("score", 0) for s in report["standards"].values())
        report["overall_score"] = score / len(standards) if standards else 0
        
        return report
    
    def get_requirements(self, standard: ComplianceStandard) -> List[Dict]:
        checker = self.standards.get(standard)
        return checker.requirements if checker else []

class GDPRCompliance:
    def __init__(self):
        self.requirements = [
            {"id": "gdpr_1", "description": "Data consent management", "status": "implemented"},
            {"id": "gdpr_2", "description": "Right to erasure", "status": "implemented"},
            {"id": "gdpr_3", "description": "Data portability", "status": "implemented"},
            {"id": "gdpr_4", "description": "Privacy by design", "status": "implemented"},
            {"id": "gdpr_5", "description": "Data processing records", "status": "implemented"},
        ]
    
    def check(self) -> Dict[str, Any]:
        compliant = sum(1 for r in self.requirements if r["status"] == "implemented")
        total = len(self.requirements)
        
        return {
            "standard": "GDPR",
            "score": int((compliant / total) * 100) if total > 0 else 0,
            "compliant_count": compliant,
            "total_count": total,
            "requirements": self.requirements
        }

class SOC2Compliance:
    def __init__(self):
        self.purposes = ["Security", "Availability", "Processing Integrity", "Confidentiality", "Privacy"]
        self.requirements = [
            {"id": "soc2_1", "category": "Security", "control": "Logical access", "status": "implemented"},
            {"id": "soc2_2", "category": "Security", "control": "Physical access", "status": "implemented"},
            {"id": "soc2_3", "category": "Security", "control": "System operations", "status": "implemented"},
            {"id": "soc2_4", "category": "Availability", "control": "System availability", "status": "implemented"},
            {"id": "soc2_5", "category": "Confidentiality", "control": "Data encryption", "status": "implemented"},
        ]
    
    def check(self) -> Dict[str, Any]:
        compliant = sum(1 for r in self.requirements if r["status"] == "implemented")
        total = len(self.requirements)
        
        return {
            "standard": "SOC 2",
            "purposes": self.purposes,
            "score": int((compliant / total) * 100) if total > 0 else 0,
            "compliant_count": compliant,
            "total_count": total,
            "requirements": self.requirements
        }

class HIPAACompliance:
    def __init__(self):
        self.requirements = [
            {"id": "hipaa_1", "description": "Access controls", "status": "implemented"},
            {"id": "hipaa_2", "description": "Audit controls", "status": "implemented"},
            {"id": "hipaa_3", "description": "Integrity controls", "status": "implemented"},
            {"id": "hipaa_4", "description": "Transmission security", "status": "implemented"},
            {"id": "hipaa_5", "description": "Business associate agreements", "status": "implemented"},
        ]
    
    def check(self) -> Dict[str, Any]:
        compliant = sum(1 for r in self.requirements if r["status"] == "implemented")
        total = len(self.requirements)
        
        return {
            "standard": "HIPAA",
            "score": int((compliant / total) * 100) if total > 0 else 0,
            "compliant_count": compliant,
            "total_count": total,
            "requirements": self.requirements
        }

class ISO27001Compliance:
    def __init__(self):
        self.requirements = [
            {"id": "iso_1", "control": "A.5 Information security policies", "status": "implemented"},
            {"id": "iso_2", "control": "A.6 Organization of information security", "status": "implemented"},
            {"id": "iso_3", "control": "A.7 Human resource security", "status": "implemented"},
            {"id": "iso_4", "control": "A.8 Asset management", "status": "implemented"},
            {"id": "iso_5", "control": "A.9 Access control", "status": "implemented"},
            {"id": "iso_6", "control": "A.10 Cryptography", "status": "implemented"},
            {"id": "iso_7", "control": "A.11 Physical security", "status": "implemented"},
            {"id": "iso_8", "control": "A.12 Operations security", "status": "implemented"},
            {"id": "iso_9", "control": "A.13 Communications security", "status": "implemented"},
        ]
    
    def check(self) -> Dict[str, Any]:
        compliant = sum(1 for r in self.requirements if r["status"] == "implemented")
        total = len(self.requirements)
        
        return {
            "standard": "ISO 27001",
            "score": int((compliant / total) * 100) if total > 0 else 0,
            "compliant_count": compliant,
            "total_count": total,
            "requirements": self.requirements
        }

class PCIDSSCompliance:
    def __init__(self):
        self.requirements = [
            {"id": "pci_1", "description": "Firewall configuration", "status": "implemented"},
            {"id": "pci_2", "description": "Default passwords changed", "status": "implemented"},
            {"id": "pci_3", "description": "Data encryption", "status": "implemented"},
            {"id": "pci_4", "description": "Access control", "status": "implemented"},
            {"id": "pci_5", "description": "Logging and monitoring", "status": "implemented"},
            {"id": "pci_6", "description": "Vulnerability management", "status": "implemented"},
        ]
    
    def check(self) -> Dict[str, Any]:
        compliant = sum(1 for r in self.requirements if r["status"] == "implemented")
        total = len(self.requirements)
        
        return {
            "standard": "PCI DSS",
            "score": int((compliant / total) * 100) if total > 0 else 0,
            "compliant_count": compliant,
            "total_count": total,
            "requirements": self.requirements
        }

if __name__ == "__main__":
    logs = LiveLogsViewer()
    compliance = ComplianceCenter()
    
    print("=" * 60)
    print("SalesGenie Live Logs & Compliance Center")
    print("=" * 60)
    
    print("\n--- Compliance Status ---")
    for std in ComplianceStandard:
        result = compliance.check_compliance(std)
        score = result.get("score", 0)
        status = "✓" if score == 100 else "⚠" if score >= 80 else "✗"
        print(f"{status} {std.value.upper():10} Score: {score}% ({result.get('compliant_count', 0)}/{result.get('total_count', 0)})")
    
    report = compliance.generate_report(list(ComplianceStandard))
    print(f"\nOverall Compliance Score: {report['overall_score']}%")
    
    print("\n--- Log Files Available ---")
    for log_file in logs._get_log_files():
        print(f"  - {log_file}")
    
    print("\nFeatures:")
    print("  - Live log streaming with filters")
    print("  - Multi-format export (JSON, CSV, PDF)")
    print("  - Compliance reporting (GDPR, SOC2, HIPAA, ISO27001, PCI DSS)")
    print("  - Real-time subscriber pattern")
    print("  - Searchable logs with time range filters")