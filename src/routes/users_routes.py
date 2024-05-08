from fastapi import APIRouter, UploadFile, Request
from src.database.db import db
import requests
from src.controllers.users_controller import UsersController


users_router = APIRouter()

users_controller = UsersController(db)


@users_router.post('/create')
async def create_user():
    body = await requests.Request.json()
    return users_controller.criar_usuario(body)


@users_router.get('/users')
def list_users():
    return users_controller.listar_usuarios()


@users_router.put('/upload-image')
async def upload_profile_image(file: UploadFile):

    upload_image_data = {
        "filename": file.filename.replace(" ", ""),
        "mimetype": file.content_type,
        "data": await file.read()
    }

    result = await users_controller.upload_image(upload_image_data)
    return result


@users_router.put('/update')
async def update_user(request: Request):
    body = await request.json()
    user_id = body["user_id"]
    payload = body["payload"]
    result = await users_controller.update_user(user_id, payload)

    return result
