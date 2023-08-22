#!/usr/bin/env python
"""Módulo de exemplo de FastAPI."""

from fastapi import APIRouter, status
from pydantic import BaseModel

health = APIRouter()

## Health Checks


class HealthCheck(BaseModel):
    """Model para retorno do health check."""

    status: str = "OK"


@health.get(
    "/health",
    tags=["healthcheck"],
    summary="Perform a Health Check",
    response_description="Return HTTP Status Code 200 (OK)",
    status_code=status.HTTP_200_OK,
    response_model=HealthCheck,
)
def get_health() -> HealthCheck:  # pragma: no cover
    """Checagem de saúde da API."""
    return HealthCheck(status="OK")


def add_healthcheck(app):  # pragma: no cover
    """Adiciona o router de saúde na API principal."""
    app.include_router(health)