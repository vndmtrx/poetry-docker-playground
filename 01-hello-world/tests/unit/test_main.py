#!/usr/bin/env python

from fastapi.testclient import TestClient

from hello_world.main import app

client = TestClient(app)


def test_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"menssagem": "Hello, world!"}
