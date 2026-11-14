from pydantic import BaseModel, ConfigDict
from datetime import date

class BorrowingCreate(BaseModel):
    book_id : int
    member_id : int
    due_date : date

class BorrowingUpdate(BaseModel):
    due_date : date |None=None
    

class BorrowingResponse(BaseModel):
    id :int
    book_id : int
    member_id : int
    due_date : date
    borrow_date :date
    return_date : date |None=None
    status : str 

    model_config=ConfigDict(from_attributes=True)
    

