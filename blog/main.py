from fastapi import FastAPI, Depends, status, Response, HTTPException
from sqlalchemy.sql import schema
from starlette.status import HTTP_201_CREATED
from typing import List
from . import schemas, model, database
from .database import Base, SessionLocal,engine
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from .hashing import Hash

# uvicorn blog.main:app --reload / blog 폴더 안의 main.py 명시
# from sqlalchemy의 engine이 아니라 databases.py 에서 만든 engine
# migrate 용도, 저상 실행 될 때 마다 적용
model.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal() #.database 의 SessionLocal
    try:
        yield db

    finally :
        #모든 작업이 끝나면 db or db connecion close.
        db.close()

#sqlalchemy orm 세션의 인스턴스
#@app.post('/blog', status_code=201)와같이 statuscode 를 명시해도 되지만, fastapi 의 status 사용가능
@app.post('/blog', status_code=status.HTTP_201_CREATED, tags=['blogs']) #tags 옵션은 swagger 카테고리 분리를 위함
def create(request:schemas.Blog,db:Session = Depends(get_db)):
    new_blog = model.Blog(title=request.title,body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@app.get('/blog',response_model=List[schemas.ShowBlog], tags=['blogs']) #모든 데이터를 출력하기위해 typing의 List 사용
def all(db:Session = Depends(get_db)):
    blogs = db.query(model.Blog).all()
    return blogs


@app.get('/blog/{id}', status_code=status.HTTP_200_OK,response_model=schemas.ShowBlog, tags=['blogs'])
def show(id,response:Response, db:Session = Depends(get_db)):

    blog = db.query(model.Blog).filter(model.Blog.id == id).first()

    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Blog with the id {id} is not abailable')
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'detail':f'Blog with the id {id} is not abailable'}

    return blog


@app.delete('/blog/{id}',status_code=status.HTTP_204_NO_CONTENT, tags=['blogs'])
def destroy(id,db : Session = Depends(get_db)):
    # update와 같은 방식으로 작성가능
    db.query(model.Blog).filter(model.Blog.id==id).delete(synchronize_session=False)
    db.commit()
    return {'detail':f'delete {id} done.'}


@app.put('/blog/{id}',status_code=status.HTTP_200_OK, tags=['blogs'])
def update(id, request:schemas.Blog, db:Session = Depends(get_db)):
    blog = db.query(model.Blog).filter(model.Blog.id==id) #request 사용시 schema의 모든 내용 update
    # db.query(model.Blog).filter(model.Blog.id==id).update(request)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'blog with id {id} not found')

    blog.update({model.Blog.title:request.title,model.Blog.body:request.body})
    db.commit()

    return f'detail : succesfuly update {id}'

# respones_model == schema (pydandic model)


#pwd_cxy = CryptContext(schemes=['bcrypt'], deprecated='auto')
@app.post('/user', response_model=schemas.ShowUser, tags=['users'])
def create_user(request:schemas.User, db:Session = Depends(get_db)):#요청 스키마와 응답 스키마가 다른 경우 예

    #hashedPassword = pwd_cxy.hash(request.password)

    #create 를 할 땐 sqlAlchemy가 필요
    new_user = model.User(name=request.name, email=request.email, password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@app.get('/user/{id}', response_model=schemas.ShowUser, tags=['users'])
def get_user(id=int, db: Session = Depends(get_db)):
    user = db.query(model.User).filter(model.User.id == id).first()
    
    if not user :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f'USER with the id {id} is not available')

    return user

