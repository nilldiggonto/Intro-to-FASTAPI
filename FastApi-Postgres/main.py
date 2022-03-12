from fastapi import FastAPI
from db_connect import Base,engine,sessionLocal

app = FastAPI()

Base.metadata.create_all(engine)
#--------------------- db connection
def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get('/')
def index():
    return "Ready App"