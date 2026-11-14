from sqlalchemy.orm import Session
from app.models.borrowing import Borrowing
from app.models.book import Book
from app.models.member import Member
from app.schemas.borrowing import BorrowingCreate, BorrowingUpdate
from datetime import date

def create_borrowing(db:Session, borrowing:BorrowingCreate):
    book = db.query(Book).filter(Book.id == borrowing.book_id).first()
    if not book:
        return None
    if book.quantity <= 0:
        return None
    
    member = db.query(Member).filter(Member.id == borrowing.member_id).first()
    if not member:
        return None
    if not member.is_active:
        return None
    if borrowing.due_date < date.today():
     return None
    
    try:
        db_borrowing = Borrowing(**borrowing.model_dump())
        db.add(db_borrowing)
        book.quantity -= 1
        db.commit()
        db.refresh(db_borrowing)
        return db_borrowing
    except Exception:
         db.rollback()
         raise

def get_all_borrowing(db:Session):
    borrowings = db.query(Borrowing).all()
    return borrowings


def get_borrowing_by_id(db:Session, borrowing_id : int):
    borrowing = db.query(Borrowing).filter(Borrowing.id == borrowing_id).first()
    return borrowing

def update_borrowing(db:Session,borrowing_id : int, borrowing_data:BorrowingUpdate):
        borrowing = db.query(Borrowing).filter(Borrowing.id == borrowing_id).first()
        if not borrowing:
             return None
        update_data = borrowing_data.model_dump(exclude_unset=True).items()
        for key, value in update_data:
             setattr(borrowing,key,value)
        db.commit()
        db.refresh(borrowing)
        return borrowing





def return_book(db:Session, borrowing_id: int):
     borrowing = db.query(Borrowing).filter(Borrowing.id == borrowing_id).first()
     if not borrowing:
          return None
     if borrowing.status == "returned":
          return None
     try:

      borrowing.return_date = date.today()
      borrowing.status = "returned"
      borrowing.book.quantity += 1
      
      db.commit()
      db.refresh(borrowing)
      
      return borrowing
     except Exception:
          db.rollback()
          raise

     
