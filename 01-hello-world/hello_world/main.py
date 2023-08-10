#!/usr/bin/env python

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def main_route():
    return {"menssagem": "Hello, world!"}
