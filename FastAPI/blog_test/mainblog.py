from fastapi import FastAPI,status,Response,HTTPException
from fastapi.params import Depends
from sqlalchemy.sql.expression import delete
from sqlalchemy.sql.functions import mode
import uvicorn
from schemas import BlogSchema,ShowBlog,User
from sqlalchemy.orm import Session
from models import Blog,UserModel
from db_connect import engine,Base,sessionLocal
from typing import List
from passlib.context import CryptContext

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
@app.get('/blog',response_model=List[ShowBlog])
def blog(db:Session = Depends(get_db)):
    blogs = db.query(Blog).all()
    blog_list = [{'id':b.id,'title':b.title,'body':b.body} for b in blogs]
    # data = {'status':'success','blog':blog_list}
    return blog_list

#Fetching SINGLE BLOG
@app.get('/blog/{id}',response_model=ShowBlog, status_code=200)
def blogSingle(response:Response,id, db:Session = Depends(get_db)):
    blog = db.query(Blog).filter(Blog.id == id).first()
    data = []
    if not blog:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'detail': f'No blog with {id} found'}
    data = {'title':blog.title,'body':blog.body}
    return data

#-------EDIT
@app.put('/blog/{id}')
def blogEdit(id,request:BlogSchema,db:Session = Depends(get_db)):
    blog = db.query(Blog).filter(Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'{id} Not Found')
    blog.update({'title':request.title,'body':request.body})
    db.commit()
    return {'data':'update'}

#-------DELETE
@app.delete('/blog/{id}')
def blogDelete(id,db:Session = Depends(get_db)):
    blog = db.query(Blog).filter(Blog.id==id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'{id} Not Found')
    
    blog.delete(synchronize_session=False)
    db.commit()
    data = {'msg':'deleted'}
    return data

#-----------------------------CREATE USER
pwd_cxt = CryptContext(schemes=["bcrypt"],deprecated="auto")

@app.post('/user',tags=['user'])
def createUser(request:User,db:Session = Depends(get_db)):
    hashedPassword = pwd_cxt.hash(request.password)
    new_user = UserModel(name=request.name,email=request.email,password=hashedPassword)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {'status':'user created','username':new_user.name,'email':new_user.email}

@app.get('/user/{id}',tags=['user'])
def showUser(id:int,db:Session = Depends(get_db)):
    user = db.query(UserModel).filter(UserModel.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="No Such User Found")
    return {'status':'success','username':user.name}

#--- FOR DEBUG
if __name__ == "__main__":
    uvicorn.run(app,host="127.0.0.1",port=9000)