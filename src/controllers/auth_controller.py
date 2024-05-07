from flask import jsonify
from src.services.auth_service import AuthService

class AuthController:

    def __init__(self, db):
        self._authService = AuthService(db)

    async def login(self, payload):
        try:
            email = payload["email"]
            password = payload["password"]
            logged = await self._authService.login(email, password)

            return logged
        except Exception as e:
            print(f"Erro ao logar:", e)
            return e
