from sqlalchemy.orm import declarative_base,sessionmaker
from sqlalchemy import Column,String,DateTime,Integer,create_engine
from datetime import datetime
import os

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

connection_string = "sqlite:///"+ os.path.join(BASE_DIR,'test.db')

Base = declarative_base()

engine = create_engine(connection_string,echo=True)

Session = sessionmaker()

class User(Base):
    __tablename__ = "users"
    id          =   Column(Integer(),primary_key=True)
    username    =   Column(String(25),nullable=False,unique=True)
    email       =   Column(String(80),nullable=False,unique=True)
    created_at  =   Column(DateTime(),default=datetime.utcnow)

    def __repr__(self):
        return f'username={self.username} email={self.email}'

newuser = User(id=1,username='nill',email='nill@nill.com')
print(newuser)
