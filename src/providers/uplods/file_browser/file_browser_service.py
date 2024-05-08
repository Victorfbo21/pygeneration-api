import httpx
from dotenv import load_dotenv
import os
load_dotenv()


async def get_token():
    login_url = os.environ.get('UPLOAD_LOGIN_URL')
    username = os.environ.get('UPLOAD_USERNAME')
    password = os.environ.get('UPLOAD_PASSWORD')

    credentials = {
        'username': username,
        'password': password
    }

    headers = {
        'Content-Type': 'application/json'
    }

    async with httpx.AsyncClient() as server:
        response = await server.post(login_url, json=credentials, headers=headers)
        return response.read()


async def upload_image_base(path,data, token, type):

    async with httpx.AsyncClient() as sever:
        response = await sever.post(path, data=data, headers={'x-auth': token, 'Content-Type': type})
        return response.read()


async def create_shared_file(public_path, token):
    data = {
        'password': '',
        'expires': '820',
        'unit': 'days'
    }
    headers = {
        'x-auth': token,
        'Content-Type': 'application/json'
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(public_path, json=data, headers=headers)
        return response.json()


class FileBrowser:

    async def upload_image(self, upload_data):
        try:

            base_path = f"{os.environ.get('BASE_UPLOAD_PATH')}/{upload_data['filename'].strip()}?override=true"
            public_path = (f"{os.environ.get('SHARE_UPLOAD_PUBLIC')}/{upload_data['filename'].strip()}"
                           f"?expires=820&unit=days")

            token = await get_token()

            upload_image_base_response = await upload_image_base(base_path, upload_data["data"], token,
                                                                 upload_data['filename'])

            upload_image_public_response = await create_shared_file(public_path, token)


            return {
                "error": False,
                "fileURL": f"{os.environ.get('SHARED_UPLOAD_URL_BASE')}".replace("@@HASH@@",
                                                                                 upload_image_public_response['hash'])
            }

        except Exception as e:
            print(f'Erro ao fazer upload :{e}')
            return {
                "error": True,
                "fileURL": ""
            }
