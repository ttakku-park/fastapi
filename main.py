#import fastapi
from typing import Optional
from fastapi import FastAPI
#request body를 설정하기 위해서는 pydantic 모델이 필요
from pydantic import BaseModel
import uvicorn

#인스턴스 생성
# uvicorn main:app --reload 의 app name
app = FastAPI()

#queryparameter
#필수 매개변수 id:str / 기본값있는 매개변수 id:srt = '안녕' / 선택적선언 id : Optional[str] = None
@app.get('/blog') # / is baseurl , operation path
#handle the path
def index(limit=10, published:bool = True, q : Optional[str] = None):
    if published :
        return {'data':f'{limit} published blogs from the db,{q}'}
    else:
        return {'data':f'{limit} blogs from the db{q}'}
#pathparameter
#같은 경로 blog 를 사용하는경우 패스파라미터가 상단에 있으면 패스파라미터로 주소로 읽힘 
#@app.get('/blog?limit=10&published=true')
@app.get('/blog/unpublished')
def unpublished():
    return {'data':'all unpublished blogs'}

@app.get('/blog/{blog_id}')
def show(blog_id:int): #파라미터로 받을 타입설정
    return {'data':blog_id}

@app.get('/blog/{blog_id}/comments')
def comments(blog_id):
    return {'data':{blog_id:'2'}}


#post의 request body 스키마 
class Blog(BaseModel):
    title : str
    body : str
    published_at : Optional[bool]

@app.post('/blog')
def create_blog(request: Blog):
    return {'data':f'blog is created with {request.title}'}

