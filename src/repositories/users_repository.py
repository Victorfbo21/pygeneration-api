import bcrypt
import os
import asyncio
from bson.objectid import ObjectId
from src.models.service import Service

class UsersRepository:

    def __init__(self, db):
        self.db = db

    def listar_usuarios(self):
        try:
            users = self.db.users.find()
            return [user for user in users]
        except Exception as e:
            print(f"Erro ao Listar Usuários {e}")

    async def inserir_usuario(self, novo_usuario):
        try:
            verify_exists = await self.db.users.find_one({'email': novo_usuario["email"]})

            if verify_exists:
                return {
                    'data': None,
                    'error': True,
                    'statusCode': 400,
                    'message': 'Usuário Já Cadastrado'
                }
            
            novo_usuario["password"] = (bcrypt.hashpw(novo_usuario["password"].encode('utf-8'), bcrypt.gensalt())
                                        .decode('utf-8'))
            
            user_created = self.db.users.insert_one(novo_usuario)
            inserted_id = user_created.inserted_id

            return {
                'data': str(inserted_id),
                'error': False,
                'statusCode': 201,
                'message': 'Usuário Cadastrado com Sucesso!'
            }

        except Exception as e:
            print(f"Erro ao inserir usuário: {e}")
            return False

    async def upload_profile_image(self, file):
        try:
            return file

        except Exception as e:
            print(f"Erro ao fazer upload da imagem : {e}")
            return e

    async def update_usuario(self, user_id, payload):
        try:
            updated = self.db.users.find_one_and_update(
                {"_id": ObjectId(user_id)},
                {"$set": payload},
                return_document=True
            )

            return updated

        except Exception as e:
            print(f"Erro ao atualizar usuário")
            return e

    async def get_user_by_email(self, email):
        try:
            user = self.db.users.find_one({"email": email})

            return user

        except Exception as e:
            print(f"Erro ao recuperar usuário:", e)
            return e