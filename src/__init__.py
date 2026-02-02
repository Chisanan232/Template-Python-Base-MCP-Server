"""Template MCP Server - A Model Context Protocol server template.

This package provides a comprehensive template for building MCP (Model Context Protocol)
servers with support for multiple transport modes and integrated webhook functionality.

Main Components:
    - mcp: MCP server implementation with factory pattern
    - web_server: FastAPI web server for HTTP transports and webhooks
    - integrate: Integrated server combining MCP and webhook functionality
    - config: Configuration management with pydantic-settings
    - models: Pydantic models for CLI and DTO objects
    - entry: Command-line entry point

Features:
    - Multiple transport support (stdio, SSE, HTTP streaming)
    - Singleton factory pattern for server instances
    - Integrated mode for combined MCP + webhook servers
    - Comprehensive configuration management
    - Type-safe CLI argument parsing
    - Health check endpoints
    - CORS support
    - Development auto-reload

Quick Start:
    # Run with default stdio transport
    python -m src.entry

    # Run with SSE transport
    python -m src.entry --transport sse --port 8000

    # Run in integrated mode
    python -m src.entry --integrated --transport sse

Type System:
    The package provides comprehensive type definitions for static type checking
    and follows PEP 695 (Python 3.12+) using modern type statement syntax.
"""

from __future__ import annotations

# Re-export commonly used components for convenience
from .config import get_settings, Settings
from .models.cli import ServerConfig, LogLevel, MCPTransportType
from .models.dto.health_check import HealthyCheckResponseDto

__version__ = "0.0.0"
__author__ = "Template Author"
__email__ = "template@example.com"

__all__ = [
    # Configuration
    "get_settings",
    "Settings",
    # Models
    "ServerConfig",
    "LogLevel",
    "MCPTransportType",
    "HealthyCheckResponseDto",
]
