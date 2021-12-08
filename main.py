#import fastapi
from fastapi import FastAPI

#인스턴스 생성
# uvicorn main:app --reload 의 app name
app = FastAPI()

@app.get('/') # / is baseurl , operation path
#handle the path
def index():
    return {'data':{'name':'jo'}}

#pathparameter
#같은 경로 blog 를 사용하는경우 패스파라미터가 상단에 있으면 패스파라미터로 주소로 읽힘 
@app.get('/blog/unpublished')
def unpublished():
    return {'data':'all unpublished blogs'}

@app.get('/blog/{blog_id}')
def show(blog_id:int): #파라미터로 받을 타입설정
    return {'data':blog_id}

@app.get('/blog/{blog_id}/comments')
def comments(blog_id:int):
    return {'data':{blog_id:'2'}}

