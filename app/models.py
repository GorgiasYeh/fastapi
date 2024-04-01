from .database import Base
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP

class User(Base):
    __tablename__ = "User"
    
    id = Column(Integer, primary_key=True, nullable=False)
    userName = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    isArchive = Column(Boolean, default=False)
    createTime = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))