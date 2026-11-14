from fastapi import APIRouter,Depends, HTTPException
from app.schemas.borrowing import BorrowingCreate,BorrowingResponse, BorrowingUpdate
from app.database import get_db
from app.crud.borrowing import get_all_borrowing,get_borrowing_by_id,create_borrowing,update_borrowing,return_book
from sqlalchemy.orm import Session


router = APIRouter(
    prefix="/borrowing"
)

@router.get("/", response_model=list[BorrowingResponse])
def read_borrowing(db:Session=Depends(get_db)):
    return get_all_borrowing(db)

@router.get("/{borrowing_id}", response_model=BorrowingResponse)
def read_borrowing_by_id(borrowing_id:int, db:Session=Depends(get_db)):
    borrowing = get_borrowing_by_id(db, borrowing_id)
    if not borrowing:
        raise HTTPException(
            status_code=404,
            detail="Borrowing not found"
        )
    return borrowing

@router.post("/", response_model=BorrowingResponse)
def post_borrowing_by_id(borrowing:BorrowingCreate , db:Session=Depends(get_db)):
    result  =create_borrowing(db, borrowing)
    if result is None:
        raise HTTPException(
            status_code=400,
            detail="Cannot create borrowing. Check book availability, member status, and due date."
        )
    return result



@router.put("/{borrowing_id}", response_model=BorrowingResponse)
def put_borrowing(borrowing_id:int,borrowing_data:BorrowingUpdate ,db:Session=Depends(get_db)):
    borrowing = update_borrowing(db,borrowing_id ,borrowing_data)
    if not borrowing:
        raise HTTPException(
            status_code=404,
            detail="Borrowing not found"
        )
    return borrowing

@router.put("/{borrowing_id}/return", response_model=BorrowingResponse)
def return_borrowed_book(borrowing_id:int, db:Session=Depends(get_db)):
    borrowing = return_book(db, borrowing_id)
    if borrowing is None:
        raise HTTPException(
            status_code=400,
            detail="Borrowing not found"
        )

    return borrowing