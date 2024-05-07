from src.repositories.users_repository import UsersRepository
from src.providers.uplods.file_browser.file_browser_service import FileBrowser


class UsersService:

    def __init__(self, db):
        self._usersRepository = UsersRepository(db)
        self._fileBrowserSerice = FileBrowser()

    def listar_usuarios(self):
        users = self._usersRepository.listar_usuarios()
        return users

    def criar_usuario(self, request_body):
        try:
            create_user = self._usersRepository.inserir_usuario(request_body)
            return create_user
        except Exception as e:
            print(f"Erro ao criar usuário: {e}")

    async def upload_profile_image(self, request_file):
        try:
            uplod_file_response = await self._fileBrowserSerice.upload_image(request_file)

            uploaded_file = await self._usersRepository.upload_profile_image(request_file)

            return uploaded_file
        except Exception as e:
            print(f"Erro ao Subir Imagem : {e}")

    async def atualizar_usuario(self, user_id, payload):
        try:
            updated = await self._usersRepository.update_usuario(user_id, payload)

            return True

        except Exception as e:
            print(f"Erro ao atualizar Usuário:", e)
            return False
