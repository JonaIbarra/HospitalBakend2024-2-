from jwt import JWT

def solicita_token(dato: dict) -> str:
    token = JWT().encode(payload=dato, key='mi_clave', algorithm='HS256')
    return token

def valida_token(token: str) -> dict:
    dato: dict = JWT().decode(token, key='mi_clave', algorithms=['HS256'])
    return dato
