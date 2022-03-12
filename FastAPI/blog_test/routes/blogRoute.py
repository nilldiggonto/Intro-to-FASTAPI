
from fastapi import APIRouter
from .. import schemas
from ..db_connect import get_db
from ..models import Blog
from fastapi.params import Depends
from sqlalchemy.orm import Session


from typing import List


router = APIRouter()

#---Getting BLOG LIST
@router.get('/blog',response_model=List[schemas.ShowBlog])
def blog(db:Session = Depends(get_db)):
    blogs = db.query(Blog).all()
    blog_list = [{'id':b.id,'title':b.title,'body':b.body} for b in blogs]
    # data = {'status':'success','blog':blog_list}
    return blog_list