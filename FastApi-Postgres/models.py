from sqlalchemy import Column,String,Integer,ForeignKey,DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy.sql.sqltypes import Date
from db_connect import Base

class Book(Base):
    __tablename__ = 'book'
    
    id          =   Column(Integer,primary_key=True,index=True)
    title       =   Column(String)
    rating      =   Column(Integer)
    time_created=   Column(DateTime(timezone=True),server_default=func.now())
    time_updated=   Column(DateTime(timezone=True),onupdate=func.now())
    author_id   =   Column(Integer,ForeignKey("author.id"))
    author      =   relationship('Author')

class Author(Base):
    __tablename__ = 'author'
    id          =   Column(Integer,primary_key=True)
    name        =   Column(String)
    age         =   Column(String)
    time_created=   Column(DateTime(timezone=True),server_default=func.now())
    time_updated=   Column(DateTime(timezone=True),onupdate=func.now())
