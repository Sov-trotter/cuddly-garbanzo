from typing import List
from fastapi import APIRouter, Depends, status, Response, HTTPException
from .. import models, schemas, database
from sqlalchemy.orm import Session
from ..services import blog
from .. import oauth2

router = APIRouter(prefix = '/blog',tags=["blog"])
get_db = database.get_db

@router.get('/', tags = ["blog"])
def get_all(db: Session = Depends(get_db), current_user = Depends(oauth2.get_current_user)):
    return blog.get_all(db)

# create blog
@router.post('/', status_code=status.HTTP_201_CREATED)
def create_blog(req:schemas.Blog, db: Session = Depends(get_db), current_user = Depends(oauth2.get_current_user)):
    return blog.create_blog(req, db) 

@router.get('/{id}', status_code=status.HTTP_200_OK, response_model= schemas.ShowBlog)
def get_one(id: int, db: Session = Depends(get_db), current_user = Depends(oauth2.get_current_user)):
    return blog.get_one(id, db)
    
@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id, db: Session = Depends(get_db), current_user = Depends(oauth2.get_current_user)):
    return blog.delete_blog(id, db)

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_blog(id, request: schemas.Blog, db: Session = Depends(get_db), current_user = Depends(oauth2.get_current_user)):
    return blog.update_blog(id, request, db)