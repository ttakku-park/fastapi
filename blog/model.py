from os import name
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from .database import Base
from sqlalchemy.orm import relation, relationship


#database 의 base
class Blog(Base): 
    __tablename__ = 'blogs'

    id = Column(Integer,primary_key=True, index=True)
    title = Column(String(50))
    body = Column(String(100))
    user_id = Column(Integer, ForeignKey('users.id')) # foreignkey는 n 쪽에서 1 쪽을 바라봄
    
    creator = relationship('User', back_populates='blogs') # back_populates / User 의 blogs 와의  관계연결


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer,primary_key=True, index=True)
    name = Column(String(50))
    email = Column(String(100))
    password = Column(String(500))

    blogs = relationship('Blog', back_populates='creator')