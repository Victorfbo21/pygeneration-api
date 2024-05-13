from fastapi import APIRouter, Request, Response
from src.controllers.works_controller import WorksController
from src.database.db import db
import json

works_router = APIRouter()

works_controller = WorksController(db)

@works_router.post('/create')
async def create_work(request : Request):
    body = await request.json()
    result = await works_controller.create_work(body)

    return Response(content=json.dumps(result) , status_code=result["statusCode"])


@works_router.get('/works')
async def list_works(request : Request):
    body = await request.json()
    print(body)
    result = await works_controller.list_works()

    return Response(content=json.dumps(result) , status_code=result["statusCode"])