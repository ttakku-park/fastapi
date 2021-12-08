from fastapi import FastAPI
from . import schemas, model, database
from .database import Base,engine

# uvicorn blog.main:app --reload / blog 폴더 안의 main.py 명시
# from sqlalchemy의 engine이 아니라 databases.py 에서 만든 engine
model.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post('/blog')
def create(request:schemas.Blog):

    return request