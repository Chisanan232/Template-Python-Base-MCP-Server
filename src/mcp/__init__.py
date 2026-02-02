"""MCP server module.

This module contains the MCP server implementation using the factory pattern.
"""

from __future__ import annotations

from .app import MCPServerFactory, mcp_factory

__all__ = [
    "MCPServerFactory",
    "mcp_factory",
]
