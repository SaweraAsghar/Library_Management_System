from sqlalchemy.orm import Session
from app.models.fine import Fine
from app.models.borrowing import Borrowing
from app.schemas.fine import FineCreate, FineUpdate 
from datetime import date

def create_fine(db:Session, fine:FineCreate):

    borrowing = db.query(Borrowing).filter(Borrowing.id == fine.borrowing_id).first()
    if not borrowing:
        return None
    
    if borrowing.return_date:
        if borrowing.return_date <= borrowing.due_date:
            return None
    else:
        if date.today() <= borrowing.due_date:
            return None
    
    existing_fine = db.query(Fine).filter(Fine.borrowing_id == fine.borrowing_id).first()
    if existing_fine:
        return None
    try:
    
        db_fine = Fine(**fine.model_dump())
        db.add(db_fine)
        db.commit()
        db.refresh(db_fine)
        return db_fine
    except Exception:
        db.rollback()
        raise

def get_all_fine(db:Session):
    fines = db.query(Fine).all()
    return fines

def get_one_fine_by_id(db:Session, fine_id: int):
    fine= db.query(Fine).filter(Fine.id == fine_id).first()
    return fine

def update_fine(db:Session, fine_id: int, data_update:FineUpdate):
    fine= db.query(Fine).filter(Fine.id == fine_id).first()
    if not fine:
        return None
    update_data = data_update.model_dump(exclude_unset=True).items()
    for key,value in update_data:
        setattr(fine,key,value)

    if fine.is_paid :
        if not fine.paid_date:
            fine.paid_date = date.today()
    else :
        fine.paid_date = None

    try:

        db.commit()
        db.refresh(fine)

        return fine
    except Exception:
        db.rollback()
        raise


def delete_fine(db:Session, fine_id: int):
    fine= db.query(Fine).filter(Fine.id == fine_id).first()
    if not fine:
     return None

    try:
        db.delete(fine)
        db.commit()
        return True

    except Exception:
        db.rollback()
        raise



