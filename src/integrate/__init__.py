"""Integration module.

This module contains the integrated server factory that combines MCP and webhook
functionality into a single FastAPI application.
"""

from __future__ import annotations

from .app import IntegratedServerFactory, integrated_factory

__all__ = [
    "IntegratedServerFactory",
    "integrated_factory",
]
