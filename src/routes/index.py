from fastapi import APIRouter
from src.routes.users_routes import users_router
from src.routes.auth_routes import auth_router

router = APIRouter()

router.include_router(users_router, prefix='/users')
router.include_router(auth_router, prefix='/auth')


