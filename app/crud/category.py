from sqlalchemy.orm import Session
from app.models.category import Category
from app.schemas.category import CategoryCreate,CategoryUpdate


def create_category(db:Session,category:CategoryCreate ):
    db_category = Category(**category.model_dump())

    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category


def get_all_category(db:Session):
    categorys = db.query(Category).all()
    return categorys

def get_category_by_id(db:Session, category_id:int):
    category = db.query(Category).filter(Category.id == category_id).first()
    return category
    

def update_category(db:Session, category_id:int, category_data:CategoryUpdate):
    category = db.query(Category).filter(Category.id == category_id).first()
    if not category:
        return None

    update_data = category_data.model_dump(exclude_unset=True)
    for key,value in update_data.items():
        setattr(category,key,value)

    db.commit()
    db.refresh(category)
    return category

def delete_category(db:Session, category_id:int):
    category = db.query(Category).filter(Category.id == category_id).first()
    if not category:
        return None

    if category.books:
     return None
    
    db.delete(category)
    db.commit()
    return True

