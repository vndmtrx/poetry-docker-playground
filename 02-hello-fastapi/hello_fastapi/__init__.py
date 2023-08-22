#!/usr/bin/env python
"""Módulo base do projeto, que imprime a versão do mesmo."""

from copy import copy
from fastapi.routing import APIRoute
from .main import app
from .healthcheck import add_healthcheck

__version__ = "0.1.0"


@app.on_event("startup")
def add_default_head_endpoints() -> None:  # pragma: no cover
    """Adiciona a possibilidade de usar HEAD como request quando GET é usado no endpoint."""
    for route in app.routes:
        if isinstance(route, APIRoute) and "GET" in route.methods:
            new_route = copy(route)
            new_route.methods = {"HEAD"}
            new_route.include_in_schema = False
            app.routes.append(new_route)


add_healthcheck(app)
