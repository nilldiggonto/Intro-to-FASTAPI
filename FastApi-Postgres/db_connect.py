# 
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#DB URL
SQLALCHEMY_DB  = 'postgresql+psycopg2://postgres:nill1234@127.0.0.1:5432/fasttwo'

#CREATE DB ENGINE
engine = create_engine(SQLALCHEMY_DB)

#CREATING SESSION TO DB GET<POST<DELTE<FILTER.....
sessionLocal = sessionmaker(bind=engine,autocommit=False,autoflush=False)
Base = declarative_base()