from pydantic import BaseModel
# pydantic model == schema


class Blog(BaseModel): #BaseModel 은 ID랑 같이 나오는듯?
    title:str
    body: str

class ShowBlog(Blog):
    
    title:str
    body: str
    # db query사용, sqlalchemy의 orm을 사용하고있기 때문에 정의가 필요함
    class Config():
        orm_mode = True
