from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#DB URL
SQLALCHEMY_DB  = 'sqlite:///./blog.db'

#CREATE DB ENGINE
engine = create_engine(SQLALCHEMY_DB,connect_args= {'check_same_thread':False})

#CREATING SESSION TO DB GET<POST<DELTE<FILTER.....
sessionLocal = sessionmaker(bind=engine,autocommit=False,autoflush=False)


Base = declarative_base()

