#!/usr/bin/env python
"""Módulo de checagem de saúde do projeto."""

import logging
from fastapi import APIRouter, status
from pydantic import BaseModel

health = APIRouter()


class HealthCheck(BaseModel):
    """Model para retorno da checagem de saúde."""

    status: str = "OK"


class EndpointFilter(logging.Filter):
    """Filtro para remoção dos logs de saúde dos logs do endpoint."""

    def filter(self, record: logging.LogRecord) -> bool:  # pragma: no cover
        """Função que retorna se o endpoint é o /health."""
        return record.args and len(record.args) > 3 and record.args[2] != "/health"


@health.get(
    "/health",
    tags=["healthcheck"],
    summary="Efetua checagem de saúde da API para o container.",
    response_description="Retorna código de status 200 (OK) usando uma classe Pydantic.",
    status_code=status.HTTP_200_OK,
    response_model=HealthCheck,
)
def get_health() -> HealthCheck:  # pragma: no cover
    """Checagem de saúde da API."""
    return HealthCheck(status="OK")


def add_healthcheck(app):  # pragma: no cover
    """Adiciona o router de saúde na API principal."""
    logging.getLogger("uvicorn.access").addFilter(EndpointFilter())
    app.include_router(health)
