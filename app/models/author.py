from sqlalchemy import Column,Integer,String,Float
from app.database import Base
from sqlalchemy.orm import relationship


class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer,primary_key=True)
    name = Column(String(150),nullable=False )
    email = Column(String(150), unique=True, nullable=False)
    bio = Column(String(500), nullable=True)

    books = relationship("Book", back_populates="author")
