from sqlalchemy import Column,String,Integer,ForeignKey,Date
from app.database import Base
from datetime import date
from sqlalchemy.orm import relationship

class Borrowing(Base):
    __tablename__ = "borrowings"

    id = Column(Integer, primary_key=True)
    book_id = Column(Integer,ForeignKey("books.id"), nullable=False)
    member_id = Column(Integer,ForeignKey("members.id"), nullable=False)
    borrow_date = Column(Date, default=date.today,nullable=False)
    due_date = Column(Date, nullable=False)
    return_date = Column(Date,nullable=True)
    status = Column(String(20),default="borrowed",nullable=False)

    book =relationship("Book", back_populates="borrowings")
    member =relationship("Member", back_populates="borrowings")
    fine =relationship("Fine", back_populates="borrowing", uselist=False)
    
    