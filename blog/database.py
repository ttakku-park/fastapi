from sqlalchemy import create_engine, engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

#path 설정
SQLALCHAMY_DATABASE_URL = "mysql+pymysql://root:4352@localhost:3306/fastapi"
#engin 생성
engine = create_engine(SQLALCHAMY_DATABASE_URL,encoding="utf-8",echo=True)


# 세션로컬 생성
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
# base 생성
Base = declarative_base()

