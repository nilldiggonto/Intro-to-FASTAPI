from fastapi import FastAPI,status,Response,HTTPException
from fastapi.params import Depends
from sqlalchemy.sql.expression import delete
from sqlalchemy.sql.functions import mode
import uvicorn
from schemas import BlogSchema
from sqlalchemy.orm import Session
from models import Blog
from db_connect import engine,Base,sessionLocal

app = FastAPI()
Base.metadata.create_all(engine)
#--------------------- db connection
def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()

#---CREATE-------------
@app.post('/create',status_code=201)
def create(request:BlogSchema,db : Session = Depends(get_db) ):
    new_blog = Blog(title= request.title,body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    data = {'status':'success','info':'created','title':request.title,'new_blog':new_blog}
    return data

#---Getting BLOG LIST
@app.get('/blog')
def blog(db:Session = Depends(get_db)):
    blogs = db.query(Blog).all()
    blog_list = [{'id':b.id,'title':b.title,'body':b.body} for b in blogs]
    data = {'status':'success','blog':blog_list}
    return data

#Fetching SINGLE BLOG
@app.get('/blog/{id}', status_code=200)
def blogSingle(response:Response,id, db:Session = Depends(get_db)):
    blog = db.query(Blog).filter(Blog.id == id).first()
    data = []
    if not blog:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'detail': f'No blog with {id} found'}
    data = {'id':blog.id,'title':blog.title,'body':blog.body}
    return data

#-------EDIT
@app.put('/blog/{id}')
def blogEdit(id,request:BlogSchema,db:Session = Depends(get_db)):
    blog = db.query(Blog).filter(Blog.id == id).update({'title':'update title'})
    if not blog.first():
        raise HTTPException('ok')
    return {'data':'update'}

#-------DELETE
@app.delete('/blog/{id}')
def blogDelete(id,db:Session = Depends(get_db)):
    db.query(Blog).filter(Blog.id==id).delete(synchronize_session=False)
    db.commit()
    data = {'msg':'deleted'}
    return data

#--- FOR DEBUG
if __name__ == "__main__":
    uvicorn.run(app,host="127.0.0.1",port=9000)