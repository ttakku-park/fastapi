from os import name
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from .database import Base



#database 의 base
class Blog(Base): 
    __tablename__ = 'blogs'

    id = Column(Integer,primary_key=True, index=True)
    title = Column(String(50))
    body = Column(String(100))

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer,primary_key=True, index=True)
    name = Column(String(50))
    email = Column(String(100))
    password = Column(String(500))
