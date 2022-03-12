from fastapi import FastAPI
from typing import Optional

from pydantic import BaseModel
import uvicorn

app = FastAPI()

#-----------create request body
class Blog(BaseModel):
    title:str
    body:str
    publish:Optional[bool]


#---------blog homepage

@app.get('/blog')
def index(limit=10,publish:bool = True,sort: Optional[str] = None):
    result = {
        'data':'blog home page',
        'limit':limit,
        'publish':publish
    }
    if publish:
        result['data']= 'All Publish Block'

    
    return result

#---------------Create blog
@app.post('/blog/create')
def createBlog(request:Blog):
    # print(request)
    data = {
        'status':'success',
        'msg':'created',
        'title':request.title
    }
    return data



#unpublish blog
@app.get('/blog/unpublished')
def blogUnpublish():
    result = {
        'data':'unpublish',
    }
    return result

#--- single blog
@app.get('/blog/{id}')
def blog(id:int):
    result = {
        'data':'blog',
        'blog_id':id
    }
    return result


#--- blog comment
@app.get('/blog/{id}/comments')
def blogComment(id:int,limit:int =10):
    result = {
        'name':'blog',
        'id':id,
        'limit':limit,
        'comments': [
            {
                'user':'ok',
                'comment':'hi',
                'id':1
            },
             {
                'user':'ok',
                'comment':'hi',
                'id':1
            }
        ]
    }
    return result


@app.get('/about')
def about():
    result = {
        'data':'blog about page'
    }
    return result


#to start server
"""
    uvicorn main:app --reload
"""

if __name__ == "__main__":
    uvicorn.run(app,host="127.0.0.1",port=9000)