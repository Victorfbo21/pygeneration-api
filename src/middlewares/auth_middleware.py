from fastapi import Header, HTTPException

import jwt
import os

async def auth_middleware(request, call_next):
        print(request)
        token = request.headers.get('Authorization')

        if not token:
            raise HTTPException(status_code=401, detail='Token Não Encontrado!')

        try:
            secret_key = os.getenv("TOKEN_APP_SECRET")
            payload = jwt.decode(token, SECRET_KEY=secret_key, algorithms=["HS256"])
            request.state.payload = payload
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail='Token Expirado!')
        except jwt.InvalidTokenError:
            raise HTTPException(status_code=401, detail='Token Inválido')

        response = await call_next(request)
        return response
