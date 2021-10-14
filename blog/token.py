from datetime import datetime, timedelta
from typing import Optional
from jose import jwt, JWTError
from . import schemas
# from datetime import datetime, timedelta
#     from blog.models import User
#     from blog.extensions import db
#     from blog.utils import encode_token

SECRET_KEY = "caeba5f8b1c53aad0465e80072644a4cc14b5c4a84c99d08365c82632cd24569"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = schemas.TokenData(email=email)
    except JWTError:
        raise credentials_exception
        