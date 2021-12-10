from typing import List
from pydantic import BaseModel

import blog

# pydantic(response) model == schema / not related to database


class BlogBase(BaseModel):
    title:str
    body: str


class Blog(BlogBase): #BaseModel 은 ID랑 같이 나오는듯?

    class Config():
        orm_mode = True


class User(BaseModel):
    name : str
    email : str
    password : str


class ShowUser(BaseModel):
    name : str
    email : str
    blogs : List[Blog] = []

    class Config():
        orm_mode = True


class ShowBlog(Blog):
    
    title:str
    body: str
    creator : ShowUser #relationship 관계에서 가져올 스키마class 지정

    # db query사용, sqlalchemy의 orm을 사용하고있기 때문에 정의가 필요함
    class Config():
        orm_mode = True