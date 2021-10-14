from ..services import user
from fastapi import APIRouter, Depends, status, HTTPException
from .. import models, schemas, database
from sqlalchemy.orm import Session

router = APIRouter(prefix = '/user', tags = ["user"])
get_db = database.get_db

@router.post('/', response_model= schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create_user(request, db)

@router.get('/{id}', response_model= schemas.ShowUser)
def get_user(id: int, db: Session = Depends(get_db)):
    return user.get_user(id, db)