from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routes.base import base_route
from src.database.db import db
from src.middlewares import auth_middleware
from src.routes import works_routes

app = FastAPI()

# Configuração do CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite solicitações de todos os origens
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],  # Permite os métodos HTTP especificados
    allow_headers=["*"],  # Permite todos os cabeçalhos
)

app.add_middleware(auth_middleware)

app.include_router(base_route, prefix='/api')

if "works" not in db.list_collection_names():
    db.create_collection("works")

print('--------> Api Rodando em http://localhost:8000 <--------')
