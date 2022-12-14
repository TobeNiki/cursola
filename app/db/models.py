from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy import Column
from db.database import Base
from sqlalchemy.sql.sqltypes import Boolean, Integer, String


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)
    is_active = Column(Boolean, default=True)
    
    