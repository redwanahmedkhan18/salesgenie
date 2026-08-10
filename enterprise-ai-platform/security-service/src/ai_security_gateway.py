"""
AI Security Gateway Engine

Detects and mitigates prompt injection, indirect prompt injection,
data exfiltration, system prompt leakage, jailbreak attempts, and
excessive agent agency threats.
"""

import re
import logging
from datetime import datetime, timezone
from typing import List, Dict, Any, Optional

from enterprise_ai_platform.security_service.src.models import (
    ThreatType,
)

logger = logging.getLogger("salesgenie.security.ai_gateway")


class AISecurityGateway:
    """
    AI Security Gateway for detecting and mitigating threats in AI interactions.

    Implements detection for:
    - Prompt injection (direct)
    - Indirect prompt injection (via retrieved context)
    - Sensitive data disclosure attempts
    - System prompt extraction
    - Jailbreak attempts
    - Excessive agent agency / unauthorized tool use
    """

    DEFAULT_PATTERNS: List[Dict[str, Any]] = [
        {
            "threat_type": ThreatType.PROMPT_INJECTION.value,
            "pattern_name": "ignore_instructions",
            "pattern_regex": r"(?i)(ignore\s+(?:all\s+)?previous\s+instructions|disregard\s+(?:your|all)\s+instructions|forget\s+(?:your|all)\s+instructions)",
            "severity": "critical",
            "description": "Attempts to override system instructions",
        },
        {
            "threat_type": ThreatType.PROMPT_INJECTION.value,
            "pattern_name": "override_identity",
            "pattern_regex": r"(?i)(you\s+are\s+now\s+(?:a\s+|an\s+)?)|restart\s+as\s+|new\s+identity|act\s+as\s+(?:a\s+|an\s+)?",
            "severity": "high",
            "description": "Attempts to override AI identity/role",
        },
        {
            "threat_type": ThreatType.SYSTEM_PROMPT_LEAKAGE.value,
            "pattern_regex": r"(?i)(your\s+system\s+prompt|your\s+instructions|what\s+were\s+your\s+instructions|repeat\s+your\s+system|reveal\s+your\s+system\sprompt)",
            "severity": "high",
            "description": "Attempts to extract system prompt",
        },
        {
            "threat_type": ThreatType.DATA_EXFILTRATION.value,
            "pattern_regex": r"(?i)(api[_\s-]?key|secret[_\s-]?key|password|token|credential|bearer|private[_\s-]?key|access[_\s-]?key)",
            "severity": "critical",
            "description": "Potential sensitive data exfiltration",
        },
        {
            "threat_type": ThreatType.DATA_EXFILTRATION.value,
            "pattern_regex": r"(?i)(send\s+(?:all\s+|entire\s+)?(?:to|via|by)\s+|email\s+to\s+|forward\s+(?:our\s+|the\s+)?(?:to\s+|via\s+)|share\s+with\s+|export\s+to\s+|leak\s+to\s+|exfiltrat)",
            "severity": "high",
            "description": "Data exfiltration instruction pattern",
        },
        {
            "threat_type": ThreatType.JAILBREAK.value,
            "pattern_regex": r"(?i)(dan\s+mode|developer\s+mode|jailbreak|d\s+mode|dans\s+mode|you\s+are\s+now\s+uncensored|act\s+as\s+an\s+uncensored)",
            "severity": "critical",
            "description": "Jailbreak attempt detected",
        },
        {
            "threat_type": ThreatType.PROMPT_INJECTION.value,
            "pattern_name": "document_instruction_override",
            "pattern_regex": r"(?i)(treat\s+this\s+as\s+your\s+new\s+instruction|this\s+supersedes\s+|this\s+overrides\s+|from\s+now\s+on\s+follow\s+these)",
            "severity": "high",
            "description": "Document attempting to inject instructions for indirect prompt injection",
        },
        {
            "threat_type": ThreatType.EXCESSIVE_AGENT_AGENCY.value,
            "pattern_regex": r"(?i)(delete\s+(?:all\s+|entire\s+)?|drop\s+table|bulk\s+export|delete\s+database|truncate|destroy\s+all|wipe\s+everything)",
            "severity": "critical",
            "description": "Destructive action pattern - potential excessive agency",
        },
        {
            "threat_type": ThreatType.DATA_EXFILTRATION.value,
            "pattern_regex": r"(?im)^\s*(api[_-]?key|secret|password|token)\s*[:=]\s*\S+",
            "severity": "high",
            "description": "Key-value credential pattern in document",
        },
    ]

    def __init__(self):
        self._compiled_patterns: List[tuple] = []
        self._load_patterns()

    def _load_patterns(self) -> None:
        """Load compiled threat detection patterns."""
        self._compiled_patterns = []
        for pattern_def in self.DEFAULT_PATTERNS:
            try:
                compiled = re.compile(pattern_def["pattern_regex"])
                self._compiled_patterns.append((
                    compiled,
                    pattern_def["threat_type"],
                    pattern_def.get("pattern_name", pattern_def["pattern_regex"]),
                    pattern_def["severity"],
                    pattern_def.get("description", ""),
                ))
            except re.error as e:
                logger.warning(f"Invalid regex pattern '{pattern_def['pattern_regex']}': {e}")

    def add_custom_pattern(self, threat_type: str, pattern_regex: str,
                           pattern_name: str, severity: str,
                           description: Optional[str] = None) -> None:
        """Add a custom threat detection pattern."""
        try:
            compiled = re.compile(pattern_regex)
            self._compiled_patterns.append((
                compiled, threat_type, pattern_name, severity, description or ""
            ))
            logger.info(f"Added custom threat pattern: {pattern_name}")
        except re.error as e:
            logger.error(f"Failed to compile custom pattern '{pattern_regex}': {e}")

    def scan_text(self, text: str, context: Optional[str] = None) -> Dict[str, Any]:
        """Scan text (prompt or retrieved context) for AI security threats.

        Args:
            text: The text to scan (could be user prompt, retrieved doc, or tool input)
            context: Optional context type ('prompt', 'context', 'tool_input', 'output')

        Returns:
            Dict with 'threats' list, 'is_blocked' bool, and 'reason'
        """
        threats: List[Dict[str, Any]] = []
        is_blocked = False
        block_reason: Optional[str] = None

        for compiled, threat_type, pattern_name, severity, description in self._compiled_patterns:
            matches = compiled.findall(text)
            if matches:
                threat = {
                    "threat_type": threat_type,
                    "pattern_name": pattern_name,
                    "severity": severity,
                    "description": description,
                    "matched_text": matches[:5] if len(matches) <= 5 else matches[:5],
                    "match_count": len(matches),
                    "context": context or "unknown",
                    "detected_at": datetime.now(timezone.utc).isoformat(),
                }
                threats.append(threat)

                if severity in ("critical", "high"):
                    is_blocked = True
                    if not block_reason:
                        block_reason = f"{threat_type}: {description or pattern_name}"

        if threats:
            logger.warning(
                f"AI Security Gateway detected {len(threats)} threat(s), "
                f"blocked={is_blocked}, context={context}"
            )

        return {
            "threats": threats,
            "is_blocked": is_blocked,
            "reason": block_reason,
        }

    def scan_agent_action(self, action: str, parameters: Dict[str, Any],
                          tool_name: Optional[str] = None) -> Dict[str, Any]:
        """Scan an AI agent action for security threats.

        Args:
            action: The action type (e.g., 'tool_execution', 'data_access')
            parameters: The action parameters to check
            tool_name: Optional tool name being invoked

        Returns:
            Dict with threat detection results
        """
        param_str = str(parameters)
        scan_result = self.scan_text(param_str, context="agent_action")

        if tool_name:
            tool_scan = self.scan_text(str(tool_name), context="tool_name")
            if tool_scan["is_blocked"] or tool_scan["threats"]:
                scan_result["threats"].extend(tool_scan["threats"])
                if tool_scan["is_blocked"]:
                    scan_result["is_blocked"] = True
                    scan_result["reason"] = tool_scan["reason"]

        return scan_result
