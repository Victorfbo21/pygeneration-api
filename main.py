from fastapi import FastAPI
from src.routes.index import router
from src.database.db import db


app = FastAPI()



app.include_router(router, prefix='/api')

if "services" not in db.list_collection_names():
    db.create_collection("services")

print('--------> Api Rodando em http://localhost:8000 <--------')

