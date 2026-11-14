from sqlalchemy.orm import Session
from app.models.author import Author
from app.schemas.author import AuthorCreate,AuthorUpdate

def create_author(db:Session, author:AuthorCreate):
    db_author = Author(**author.model_dump())
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author

def get_all_author(db:Session):
    authors = db.query(Author).all()
    return authors


def get_author_by_id(db:Session, author_id:int):
    author = db.query(Author).filter(Author.id == author_id).first()
    return author


def update_author(db:Session,author_id:int, author_data:AuthorUpdate):
    author = db.query(Author).filter(Author.id == author_id).first()
    if not author:
        return None

    update_data= author_data.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(author, key,value)

    db.commit()
    db.refresh(author)
    return author


def delete_author(db:Session, author_id:int):
    author = db.query(Author).filter(Author.id == author_id).first()
    if not author:
        return None
    
    if author.books:
     return None
    
    db.delete(author)
    db.commit()

    return True
