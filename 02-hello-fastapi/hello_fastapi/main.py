#!/usr/bin/env python
"""Módulo de exemplo de FastAPI."""

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def rota_root():
    """Hello World na rota /"""
    return {"mensagem": "Hello, FastAPI!"}


@app.get("/users/me")
def le_meu_usuario():
    """Retorna o usuário corrente"""
    return {"user_id": "vndmtrx"}


@app.get("/users/{user_id}")
def le_usuario(user_id: str):
    """Retorna o usuário informado"""
    return {"user_id": user_id}
