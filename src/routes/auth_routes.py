from fastapi import APIRouter, Request, Response
from src.controllers.auth_controller import AuthController
import json
from src.database.db import db

auth_controller = AuthController(db)

auth_router = APIRouter()

@auth_router.post("/login")
async def login(request: Request):
    body = await request.json()

    payload = {
        "email": body["email"],
        "password": body["password"]
    }

    result = await auth_controller.login(payload)
    print(result["statusCode"])
    response = Response(content=json.dumps(result), status_code=result["statusCode"])
    return response
