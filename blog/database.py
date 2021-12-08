from sqlalchemy import create_engine, engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
SQLALCHAMY_DATABASE_URL = "mysql+pymysql://root:4352@localhost:3306/fastapi"

engine = create_engine(SQLALCHAMY_DATABASE_URL,encoding="utf-8",echo=True)



SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()

