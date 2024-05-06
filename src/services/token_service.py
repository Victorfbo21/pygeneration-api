import jwt
import datetime
import os

class TokenService:

    @staticmethod
    async def generate_token(payload):
        secret_key = os.getenv("TOKEN_APP_SECRET")

        token_data = {
            'sub': {
                "id": str(payload["id"]),
                "type": payload["type"]
            },
            'exp': datetime.datetime.now() + datetime.timedelta(minutes=120)
        }

        token = jwt.encode(payload=token_data, key=secret_key, algorithm='HS256')

        return token
