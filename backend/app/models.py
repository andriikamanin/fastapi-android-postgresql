from sqlalchemy import Column, Integer, String
from .database import Base

class Image(Base):
    __tablename__ = "images"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, unique=True, index=True)
    description = Column(String)
