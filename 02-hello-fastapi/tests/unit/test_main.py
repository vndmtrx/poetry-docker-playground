#!/usr/bin/env python

from fastapi.testclient import TestClient

from hello_fastapi.main import app

client = TestClient(app)


def rota_root_test():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"mensagem": "Hello, FastAPI!"}


def le_meu_usuario_test():
    response = client.get("/users/me")
    assert response.status_code == 200
    assert response.json() == {"user_id": "vndmtrx"}


def le_usuario_test():
    response = client.get("/users/jose")
    assert response.status_code == 200
    assert response.json() == {"user_id": "jose"}
