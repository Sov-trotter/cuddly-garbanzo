from sqlalchemy.orm import Session
from .. import models, schemas
from fastapi import HTTPException, status

def get_all(db:Session):
    return db.query(models.Blog).all()

def create_blog(req:schemas.Blog, db: Session):
    new_blog = models.Blog(title = req.title, body = req.body, user_id = 1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog) # refresh the new blog
    return new_blog

def delete_blog(id:int, db: Session):
    blog=db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")
    blog.delete(synchronize_session=False)
    db.commit()
    return 'done'

def update_blog(id, request: schemas.Blog, db: Session):
    blog=db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")
    blog.update(request.dict())
    db.commit()
    return 'updated'

def get_one_blog(id:int, db:Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()   
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")
    return blog
