import pymongo as mongo
from fastapi import FastAPI, UploadFile, Request
from dotenv import load_dotenv
import os
from src.controllers.users_controller import UsersController
from src.controllers.auth_controller import AuthController
import requests

load_dotenv()

MONGO_URL = os.getenv("MONGO_URL")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME")

app = FastAPI()

client = mongo.MongoClient(MONGO_URL)
db = client[MONGO_DB_NAME]

users_controller = UsersController(db)
auth_controller = AuthController(db)


@app.get('/')
async def index():
    return 'Banco Conectado e API Rodando!'


@app.get('/users')
def list_users():
    return users_controller.listar_usuarios()


@app.post('/users/create')
async def create_user():
    # Use 'async def' if your UsersController method is asynchronous
    body = await requests.Request.json()
    return users_controller.criar_usuario(body)


@app.put('/users/upload-image')
async def upload_profile_image(file: UploadFile):

    upload_image_data = {
        "filename": file.filename.replace(" ", ""),
        "mimetype": file.content_type,
        "data": await file.read()
    }

    result = await users_controller.upload_image(upload_image_data)
    return result


@app.put('/users/update')
async def update_user(request: Request):
    body = await request.json()
    user_id = body["user_id"]
    payload = body["payload"]
    result = await users_controller.update_user(user_id, payload)

    return result


@app.post("/auth/login")
async def login(request : Request):
    body = await request.json()

    payload = {
        "email":  body["email"],
        "password": body["password"]
    }
    
    result = await auth_controller.login(payload)

    return result
