from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Blog(Base):
    __tablename__ = 'blogs'
    id = Column(Integer, primary_key=True, index = True)
    title = Column(String)
    body = Column(String)
    user_id = Column(Integer, ForeignKey('users.id')) # foreign key to user id
    creator = relationship('User', back_populates='blogs') # back populate to creator

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index = True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    
    blogs = relationship('Blog', back_populates='creator') #back populate to user

