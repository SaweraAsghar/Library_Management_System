from sqlalchemy import Column,String,Integer, Boolean
from app.database import Base
from sqlalchemy.orm import relationship

class Member(Base):
    __tablename__ = "members"

    id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False)
    email = Column(String(150), unique=True, nullable=False)
    phone = Column(String(50), nullable=True)
    address = Column(String(300), nullable=True)
    is_active = Column(Boolean,default=True, nullable=False)

    borrowings =relationship("Borrowing", back_populates="member")

