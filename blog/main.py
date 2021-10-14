from fastapi import FastAPI
from sqlalchemy.sql.functions import user

from blog.routers import auth

# from blog import database
from . import models
from .database import engine 
from .routers import blog, user, auth

app = FastAPI()

# whenever we find a model, let's create it in the database
models.Base.metadata.create_all(engine)

app.include_router(blog.router, tags=["blog"])
app.include_router(user.router, tags=["user"])
app.include_router(auth.router, tags=["auth"])
