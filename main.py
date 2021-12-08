#import fastapi
from fastapi import FastAPI

#인스턴스 생성
app = FastAPI()

@app.get('/') # / is baseurl
#handle the path
def index():
    return {'data':{'name':'jo'}}

@app.get('/about')
def about():
    return {'data':{'about'}}