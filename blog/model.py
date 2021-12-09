from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from .database import Base



#database 의 base
class Blog(Base): 
    __tablename__ = 'blogs'
    
    id = Column(Integer,primary_key=True, index=True)
    title = Column(String(50))
    body = Column(String(100))