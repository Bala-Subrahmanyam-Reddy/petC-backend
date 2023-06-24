from fastapi import FastAPI, HTTPException, Depends, Query
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from starlette.status import HTTP_401_UNAUTHORIZED

security = HTTPBearer()
valid_tokens = ["ada7s8d7sa", "token2", "token3"]


def is_valid_token(token: str) -> bool:
    return token in valid_tokens


def verify_token(token: str = Query(...)):
    if not is_valid_token(token):
        raise HTTPException(
            status_code=HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return token
