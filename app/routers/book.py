from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.book import BookResponse, BookCreate, BookUpdate
from app.crud.book import get_all_books , get_book_by_id, create_book, update_book, delete_book
router = APIRouter(
    prefix= "/books"
)

@router.get("/", response_model=list[ BookResponse])
def get_book(db:Session = Depends(get_db) ):
    return get_all_books(db)

@router.get("/{book_id}", response_model=BookResponse)
def get_book_id(book_id:int, db: Session = Depends(get_db)):
    book = get_book_by_id(db, book_id)
    if book == None:
        raise HTTPException(
            status_code= 404,
            detail="Book not found"
        )
    return book

@router.post("/", response_model=BookResponse)
def post_book(book: BookCreate, db:Session = Depends(get_db)):
    return create_book(db, book)

@router.put("/{book_id}", response_model=BookResponse)
def put_book(book_data:BookUpdate, book_id:int, db:Session= Depends(get_db) ):
    book =  update_book(db, book_id, book_data)
    if not book:
        raise HTTPException(
            status_code=404,
            detail="Book not found" )
    return book

@router.delete("/{book_id}")
def remove_book(book_id:int, db:Session = Depends(get_db)):
    book = delete_book(db, book_id)
    if not book:
        raise HTTPException(
                status_code=404,
                detail="Book not found" )
    return "Book Deleted"
    

