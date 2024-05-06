from src.repositories.users_repository import UsersRepository
import bcrypt
from src.services.token_service import TokenService


class AuthService:

    def __init__(self, db):
        self._usersRepository = UsersRepository(db)
        self._tokenService = TokenService()

    async def login(self, email, password):
        try:
            user = await self._usersRepository.get_user_by_email(email)

            if not user:
                return {
                    "data": None,
                    "error": True,
                    "statusCode": 400,
                    "msg": "Usuário não encontrado na base de dados"
                }

            is_valid_password = bcrypt.checkpw(password.encode('utf-8'), user["password"].encode('utf-8'))

            if not is_valid_password:
                return {
                    "data": None,
                    "error": True,
                    "statusCode": 400,
                    "msg": "Digite a senha Correta"
                }

            payload = {
                "id": user["_id"],
                "type": user["type"]
            }
            token = await self._tokenService.generate_token(payload)

            return {
                "data": {
                    "accessToken": token
                },
                "error": False,
                "statusCode": 200,
                "msg": 'Usuário Logado com Sucesso!'
            }

        except Exception as e:
            print(f"Erro ao realizar login:", e)
            return e
