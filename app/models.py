from pickle import FALSE
from sqlalchemy import TIMESTAMP, Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.sql.expression import text
from .database import Base



class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False, unique=True)
    fullName= Column(String, nullable=False)
    # profileImgId = Column(String)
    # this need to be required and unique
    phoneNum = Column(String, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), 
                        nullable=False, server_default=text("now()"))
