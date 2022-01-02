from pydantic import BaseModel

#---blog creation
class BlogSchema(BaseModel):
    title: str
    body: str

#--custom serializer
class ShowBlog(BaseModel):
    title: str
    body : str
    class Config():
        orm_mode = True

#---user schema
class User(BaseModel):
    name: str
    email: str
    password: str

