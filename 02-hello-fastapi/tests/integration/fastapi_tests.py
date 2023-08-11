#!/usr/bin/env python

from fastapi.testclient import TestClient

from hello_fastapi.main import app

client = TestClient(app)


def fastapi_test():
    response1 = client.get("/users/me")
    user = dict(response1.json())["user_id"]
    response2 = client.get(f"/users/{user}")
    assert response2.status_code == 200
    assert response2.json() == {"user_id": "vndmtrx"}
