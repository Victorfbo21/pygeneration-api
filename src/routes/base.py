from fastapi import APIRouter
from src.routes.users_routes import users_router
from src.routes.auth_routes import auth_router

base_route = APIRouter()

base_route.include_router(users_router,tags=["users"], prefix='/users')
base_route.include_router(auth_router, tags=["auth"], prefix='/auth')


