import pymongo as mongo
from fastapi import APIRouter, Request
from src.controllers.auth_controller import AuthController
from dotenv import load_dotenv
import os
load_dotenv()

MONGO_URL = os.getenv("MONGO_URL")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME")

client = mongo.MongoClient(MONGO_URL)
db = client[MONGO_DB_NAME]
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
