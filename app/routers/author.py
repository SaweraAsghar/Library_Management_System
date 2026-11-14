from fastapi import Depends,APIRouter, HTTPException
from sqlalchemy.orm import Session
from app.schemas.author import AuthorCreate,AuthorResponse,AuthorUpdate
from app.database import get_db
from app.crud.author import get_all_author,get_author_by_id,update_author,delete_author, create_author

router = APIRouter(
    prefix= "/author"
)

@router.get("/", response_model=list[AuthorResponse])
def get_author(db:Session= Depends(get_db)):
    return get_all_author(db)

@router.get("/{author_id}", response_model=AuthorResponse)
def read_all(author_id : int, db:Session =Depends(get_db)):
    author = get_author_by_id(db,author_id)
    if author == None:
        raise HTTPException(
            status_code=404,
            detail="Author not found" 
        )
    return author

@router.post("/", response_model=AuthorResponse)
def post_author(author:AuthorCreate ,db:Session=Depends(get_db),):
    return create_author(db, author)


@router.put("/{author_id}", response_model=AuthorResponse)
def put_author(author_data :AuthorUpdate, author_id :int, db:Session=Depends(get_db)):
    author = update_author(db, author_id,author_data)
    if author == None:
        raise HTTPException(
            status_code=404,
            detail="Author not found"
        )
    return author

@router.delete("/{author_id}")
def remove_author(author_id:int , db:Session =Depends(get_db)):
    author = delete_author(db, author_id)
    if author is None:
        raise HTTPException(
            status_code=404,
            detail="Author not found"
        )
    result = delete_author(db, author_id)

    if result is None:
        raise HTTPException(
            status_code=400,
            detail="Cannot delete author because this author has books"
        )
    return {"message": "Author deleted successfully"}
