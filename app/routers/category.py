from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.category import CategoryCreate,CategoryResponse,CategoryUpdate
from app.crud.category import create_category, get_all_category, get_category_by_id,update_category,delete_category

router = APIRouter(
    prefix= "/category"
)

@router.get("/", response_model=list[CategoryResponse])
def read_category(db:Session =Depends(get_db)):
    return get_all_category(db)

@router.get("/{category_id}", response_model=CategoryResponse)
def read_category_by_id(category_id: int ,db:Session = Depends(get_db)):
    category = get_category_by_id(db ,category_id)

    if not category:
        raise HTTPException(
            status_code= 404,
            detail="Category not found"
        )
    return category

@router.post("/", response_model=CategoryResponse)
def post_category(category:CategoryCreate ,db:Session=Depends(get_db)):
    return create_category(db, category)


@router.put("/{category_id}", response_model=CategoryResponse)
def put_category(category_data:CategoryUpdate ,category_id:int, db:Session=Depends(get_db)):
    category = update_category(db,category_id, category_data)

    if not category:
         raise HTTPException(
                status_code= 404,
                detail="Category not found"
            )
    return category

@router.delete("/{category_id}")
def remove_category(category_id:int, db:Session=Depends(get_db)):
    category = get_category_by_id(db, category_id)

    if category is None:
            raise HTTPException(
                status_code=404,
                detail="category not found"
            )
    result = delete_category(db, category_id)
    
    if result is None:
            raise HTTPException(
                status_code=400,
                detail="Cannot delete category because this category has books"
            )
    return {"message": "category deleted successfully"}
