from pydantic import BaseModel

#---blog creation
class BlogSchema(BaseModel):
    title: str
    body: str

