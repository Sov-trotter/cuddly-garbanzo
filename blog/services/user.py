from fastapi import APIRouter, Depends, status, HTTPException
from .. import models, schemas, database
from sqlalchemy.orm import Session
from ..hashing import Hash

def create_user(request: schemas.User, db: Session):
    new_user = models.User(name = request.name, email=request.email, password=Hash.encrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user 
    
def get_user(id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user with id {id} not found")
    return user
