import pymongo as mongo
from fastapi import FastAPI
from src.routes.index import router

app = FastAPI()

app.include_router(router, prefix='/api')

print('--------> Api Rodando em http://localhost:8000 <--------')



