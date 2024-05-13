from fastapi import APIRouter
from src.routes.users_routes import users_router
from src.routes.auth_routes import auth_router
from src.routes.works_routes import works_router
from src.middlewares import auth_middleware


base_route = APIRouter()

base_route.include_router(users_router,tags=["users"], prefix='/users')
base_route.include_router(auth_router, tags=["auth"], prefix='/auth')
base_route.include_router(works_router, tags=["works"], prefix='/works')



