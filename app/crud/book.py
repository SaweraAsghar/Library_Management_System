from sqlalchemy.orm import Session
from app.models.book import Book
from app.models.author import Author
from app.models.category import Category
from app.schemas.book import BookCreate, BookUpdate

def create_book(db:Session, book:BookCreate):
    author = db.query(Author).filter(Author.id == book.author_id).first()
    if not author:
        return None

    category = db.query(Category).filter(Category.id == book.category_id).first()
    if not category:
        return None

    try:

        db_book=Book(**book.model_dump())

        db.add(db_book)
        db.commit()
        db.refresh(db_book)
        return db_book
    except Exception:
        db.rollback()
        raise


def get_all_books(db:Session):
    books = db.query(Book).all()
    return books


def get_book_by_id(db:Session, book_id:int):
    book = db.query(Book).filter(Book.id == book_id).first()
    return book


def update_book(db:Session, book_id:int, book_data:BookUpdate):
    
     book= db.query(Book).filter(Book.id == book_id).first()
     if not book:
         return None

     update_data = book_data.model_dump(exclude_unset=True)
     for key,value in update_data.items():
         setattr(book,key,value)
     db.commit()
     db.refresh(book)
     return book


def delete_book(db:Session, book_id:int):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        return None
    if book.borrowings:
     return None

    db.delete(book)
    db.commit()
    return True






