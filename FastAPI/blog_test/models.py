from typing import Collection

# from sqlalchemy.sql.schema import ForeignKey
from db_connect import Base
from sqlalchemy import Column,String,Integer,ForeignKey
from sqlalchemy.orm import relationship

class Blog(Base):
    __tablename__ = "blog"
    id      =   Column(Integer,primary_key=True,index=True)
    title   =   Column(String)
    body    =   Column(String)

    user_id =   Column(Integer,ForeignKey('users.id'))
    owner   =   relationship('UserModel',back_populates="blogs")

class UserModel(Base):
    __tablename__ = 'users'
    id      =   Column(Integer,primary_key=True,index=True)
    name    =   Column(String)
    email   =   Column(String)
    password=   Column(String)
    blogs   =   relationship('Blog',back_populates='owner')
    
