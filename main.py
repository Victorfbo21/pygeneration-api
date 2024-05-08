from fastapi import FastAPI
from src.routes.base import base_route
from src.database.db import db

app = FastAPI()


app.include_router(base_route, prefix='/api')


if "services" not in db.list_collection_names():
    db.create_collection("services")

print('--------> Api Rodando em http://localhost:8000 <--------')

