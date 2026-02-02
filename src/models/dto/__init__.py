"""Data transfer objects module.

This module contains Pydantic models for API responses and data transfer objects.
"""

from __future__ import annotations

from .health_check import HealthyCheckResponseDto

__all__ = [
    "HealthyCheckResponseDto",
]
