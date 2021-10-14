from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from ..token import create_access_token
from .. import schemas, database, models
from ..hashing import Hash

router = APIRouter()

@router.post("/login")
def login(request:OAuth2PasswordRequestForm = Depends(), db:Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User not found")
    
    if not Hash.verify(user.password, request.password):
        return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Invalid credentials")
    access_token = create_access_token(data = {"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}

