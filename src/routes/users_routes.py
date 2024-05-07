import pymongo as mongo
from fastapi import APIRouter, UploadFile, Request
from dotenv import load_dotenv
import requests
from src.controllers.users_controller import UsersController
import os


users_router = APIRouter()

load_dotenv()
MONGO_URL = os.getenv("MONGO_URL")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME")

client = mongo.MongoClient(MONGO_URL)
db = client[MONGO_DB_NAME]
users_controller = UsersController(db)


@users_router.post('/users/create')
async def create_user():
    body = await requests.Request.json()
    return users_controller.criar_usuario(body)


@users_router.get('/users')
def list_users():
    return users_controller.listar_usuarios()


@users_router.put('/users/upload-image')
async def upload_profile_image(file: UploadFile):

    upload_image_data = {
        "filename": file.filename.replace(" ", ""),
        "mimetype": file.content_type,
        "data": await file.read()
    }

    result = await users_controller.upload_image(upload_image_data)
    return result


@users_router.put('/users/update')
async def update_user(request: Request):
    body = await request.json()
    user_id = body["user_id"]
    payload = body["payload"]
    result = await users_controller.update_user(user_id, payload)

    return result
