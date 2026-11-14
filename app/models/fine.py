from sqlalchemy import Column,Boolean,Integer,Date,ForeignKey,Float
from app.database import Base
from datetime import date
from sqlalchemy.orm import relationship

class Fine(Base):
    __tablename__ = "fines"

    id =Column(Integer,primary_key=True)
    borrowing_id =Column(Integer,ForeignKey("borrowings.id"), nullable=False, unique=True)
    amount =Column(Float, nullable=False)
    is_paid =Column(Boolean, default=False ,nullable=False)
    paid_date =Column(Date,nullable=True)

    borrowing = relationship("Borrowing", back_populates="fine")