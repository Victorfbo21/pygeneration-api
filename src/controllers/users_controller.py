from flask import jsonify
from src.services.users_service import UsersService


class UsersController:

    def __init__(self, db):
        self.usersService = UsersService(db)

    def listar_usuarios(self):
        try:
            users = self.usersService.listar_usuarios()
            for user in users:
                user['_id'] = str(user['_id'])

            return jsonify(users)

        except Exception as e:
            print(f"Erro ao listar usuários {e}")

    def criar_usuario(self, request_body):
        try:
            created_user = self.usersService.criar_usuario(request_body)
            return jsonify(created_user)
        except Exception as e:
            print(f"Erro ao Encaminhar Requisição de Criação de usuário : {e}")

    async def upload_image(self, resquest_file):
        try:
            file_uploaded = await self.usersService.upload_profile_image(resquest_file)

            return file_uploaded
        except Exception as e:
            print(f"Erro ao subir:{e}")

    async def update_user(self, user_id, payload):
        try:
            updated = await self.usersService.atualizar_usuario(user_id,payload)
        except Exception as e:
            print(f"Erro ao Atualizar Usuário", e)
            return e
