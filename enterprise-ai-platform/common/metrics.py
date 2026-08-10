"""
Metrics Collection System for SalesGenie Enterprise Platform

Provides:
- Counter, Histogram, Gauge metric types
- In-memory metrics collection (no external dependency required)
- Prometheus-compatible export format
- Per-service metric prefixing

Follows observability.md Section 6 (Metrics Architecture) and Section 18 (Alerting Strategy).

Usage:
    from enterprise_ai_platform.common.metrics import get_metrics

    metrics = get_metrics("ai-gateway-service")
    metrics.increment("llm_requests_total", labels={"provider": "groq"})
    metrics.histogram("llm_response_time_ms", 150.5, labels={"provider": "groq"})

In production, metrics can be scraped from the /metrics endpoint.
"""

import os
import time
from typing import Dict, Optional, Any
from collections import defaultdict
from threading import Lock

from .logging import get_structured_logger

logger = get_structured_logger("salesgenie.metrics", "metrics")

_metrics_registry: Dict[str, "Metrics"] = {}
_registry_lock = Lock()
_disabled = os.getenv("DISABLE_METRICS", "").lower() in ("1", "true", "yes")


class Counter:
    """A monotonically increasing counter."""

    def __init__(self, name: str, description: str = "", labels: Optional[Dict[str, str]] = None):
        self.name = name
        self.description = description
        self._value = 0.0
        self._lock = Lock()
        self._labels = labels or {}

    def increment(self, value: float = 1.0, labels: Optional[Dict[str, str]] = None):
        if _disabled:
            return
        merged = {**self._labels, **(labels or {})}
        with self._lock:
            self._value += value
        logger.debug(
            f"Counter incremented: {self.name}",
            extra={"counter": self.name, "value": self._value, "labels": merged}
        )

    @property
    def value(self) -> float:
        return self._value


class Histogram:
    """A histogram metric for measuring distributions."""

    def __init__(self, name: str, description: str = "", labels: Optional[Dict[str, str]] = None,
                 buckets: Optional[list] = None):
        self.name = name
        self.description = description
        self._labels = labels or {}
        self._values: list = []
        self._lock = Lock()
        self._buckets = buckets or [1, 5, 10, 25, 50, 100, 250, 500, 1000, 2500, 5000, 10000, float("inf")]

    def observe(self, value: float, labels: Optional[Dict[str, str]] = None):
        if _disabled:
            return
        merged = {**self._labels, **(labels or {})}
        with self._lock:
            self._values.append(value)
        logger.debug(
            f"Histogram observed: {self.name} = {value}",
            extra={"histogram": self.name, "value": value, "labels": merged}
        )

    @property
    def count(self) -> int:
        return len(self._values)

    @property
    def sum(self) -> float:
        with self._lock:
            return sum(self._values)

    @property
    def avg(self) -> float:
        if not self._values:
            return 0.0
        return self.sum / len(self._values)


class Gauge:
    """A gauge metric for measuring current values."""

    def __init__(self, name: str, description: str = "", labels: Optional[Dict[str, str]] = None):
        self.name = name
        self.description = description
        self._value = 0.0
        self._lock = Lock()
        self._labels = labels or {}

    def set(self, value: float, labels: Optional[Dict[str, str]] = None):
        if _disabled:
            return
        merged = {**self._labels, **(labels or {})}
        with self._lock:
            self._value = value
        logger.debug(
            f"Gauge set: {self.name} = {value}",
            extra={"gauge": self.name, "value": value, "labels": merged}
        )

    def increment(self, value: float = 1.0, labels: Optional[Dict[str, str]] = None):
        if _disabled:
            return
        with self._lock:
            self._value += value

    def decrement(self, value: float = 1.0, labels: Optional[Dict[str, str]] = None):
        if _disabled:
            return
        with self._lock:
            self._value -= value

    @property
    def value(self) -> float:
        return self._value


class Metrics:
    """Metrics registry for a single service."""

    def __init__(self, service_name: str):
        self.service_name = service_name
        self._counters: Dict[str, Counter] = {}
        self._histograms: Dict[str, Histogram] = {}
        self._gauges: Dict[str, Gauge] = {}
        self._lock = Lock()

    def counter(self, name: str, description: str = "", labels: Optional[Dict[str, str]] = None) -> Counter:
        key = f"counter:{name}"
        with self._lock:
            if key not in self._counters:
                self._counters[key] = Counter(name, description, labels)
            return self._counters[key]

    def histogram(self, name: str, description: str = "", labels: Optional[Dict[str, str]] = None,
                  buckets: Optional[list] = None) -> Histogram:
        key = f"histogram:{name}"
        with self._lock:
            if key not in self._histograms:
                self._histograms[key] = Histogram(name, description, labels, buckets)
            return self._histograms[key]

    def gauge(self, name: str, description: str = "", labels: Optional[Dict[str, str]] = None) -> Gauge:
        key = f"gauge:{name}"
        with self._lock:
            if key not in self._gauges:
                self._gauges[key] = Gauge(name, description, labels)
            return self._gauges[key]

    def increment(self, name: str, value: float = 1.0, labels: Optional[Dict[str, str]] = None):
        self.counter(name).increment(value, labels)

    def observe(self, name: str, value: float, labels: Optional[Dict[str, str]] = None):
        self.histogram(name).observe(value, labels)

    def set_gauge(self, name: str, value: float, labels: Optional[Dict[str, str]] = None):
        self.gauge(name).set(value, labels)

    def to_prometheus(self) -> str:
        """Export metrics in Prometheus text format."""
        lines = []
        with self._lock:
            for key, counter in self._counters.items():
                lines.append(f"# HELP {counter.name} {counter.description}")
                lines.append(f"# TYPE {counter.name} counter")
                lines.append(f"{counter.name} {counter.value}")
            for key, hist in self._histograms.items():
                lines.append(f"# HELP {hist.name} {hist.description}")
                lines.append(f"# TYPE {hist.name} histogram")
                lines.append(f"{hist.name}_sum {hist.sum}")
                lines.append(f"{hist.name}_count {hist.count}")
                lines.append(f"{hist.name}_avg {hist.avg}")
            for key, gauge in self._gauges.items():
                lines.append(f"# HELP {gauge.name} {gauge.description}")
                lines.append(f"# TYPE {gauge.name} gauge")
                lines.append(f"{gauge.name} {gauge.value}")
        return "\n".join(lines)


def get_metrics(service_name: str) -> Metrics:
    """Get or create a Metrics registry for a service."""
    with _registry_lock:
        if service_name not in _metrics_registry:
            _metrics_registry[service_name] = Metrics(service_name)
        return _metrics_registry[service_name]


def get_all_metrics() -> Dict[str, Metrics]:
    """Get all registered metric registries."""
    with _registry_lock:
        return dict(_metrics_registry)
