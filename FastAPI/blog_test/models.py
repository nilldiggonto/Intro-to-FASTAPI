from typing import Collection
from db_connect import Base
from sqlalchemy import Column,String,Integer

class Blog(Base):
    __tablename__ = "blog"
    id      =   Column(Integer,primary_key=True,index=True)
    title   =   Column(String)
    body    =   Column(String)
