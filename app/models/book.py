from sqlalchemy import Column,String,Integer,Float, ForeignKey
from app.database import Base
from sqlalchemy.orm import relationship


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    author_id = Column(Integer,ForeignKey("authors.id"), nullable=False)
    isbn = Column(String(20),unique=True, nullable=False)
    price = Column(Float,nullable=False)
    quantity = Column(Integer,default=0)
    description = Column(String(500),nullable=True)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)


    author =relationship("Author", back_populates="books")
    category =relationship("Category", back_populates="books")
    borrowings =relationship("Borrowing", back_populates="book")



