from fastapi import APIRouter, Request
from src.controllers.auth_controller import AuthController

from src.database.db import db

auth_controller = AuthController(db)

auth_router = APIRouter()

@auth_router.post("/auth/login")
async def login(request: Request):
    body = await request.json()

    payload = {
        "email": body["email"],
        "password": body["password"]
    }

    result = await auth_controller.login(payload)

    return result
