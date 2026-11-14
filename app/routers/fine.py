from fastapi import APIRouter,Depends,HTTPException
from app.database import get_db
from app.schemas.fine import FineCreate,FineResponse,FineUpdate
from app.crud.fine import create_fine,get_all_fine,get_one_fine_by_id,update_fine,delete_fine
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/fine"
)

@router.get("/", response_model=list[FineResponse])
def read_fine(db:Session=Depends(get_db)):
    return get_all_fine(db)

@router.get("/{fine_id}", response_model=FineResponse)
def read_fine_id(fine_id:int, db:Session=Depends(get_db)):
    fine = get_one_fine_by_id(db, fine_id)
    if not fine:
        raise HTTPException(
            status_code=404,
            detail="Fine not found"
        )
    return fine

@router.post("/", response_model=FineResponse)
def post_fine(fine:FineCreate , db:Session=Depends(get_db)):
    result = create_fine(db, fine)
    if not result:
        raise HTTPException(
            status_code=400,
            detail="Cannot create fine. Check borrowing record, overdue status, or existing fine."
        )
    return result


@router.put("/{fine_id}", response_model=FineResponse)
def put_fine(fine_id:int,fine_data:FineUpdate ,db:Session=Depends(get_db)):
    fine = update_fine(db,fine_id ,fine_data)
    if not fine:
        raise HTTPException(
            status_code=404,
            detail="Fine not found"
        )
    return fine

@router.delete("/{fine_id}")
def remove_fine(fine_id:int, db:Session=Depends(get_db)):
    fine = get_one_fine_by_id(db, fine_id)
    if not fine:
        raise HTTPException(
            status_code=404,
            detail="fine not found"
        )
    result = delete_fine(db, fine_id)

    if not result:
        raise HTTPException(
            status_code=400,
            detail="Unable to delete fine"
        )

    return {"message": "Fine deleted successfully"}
                