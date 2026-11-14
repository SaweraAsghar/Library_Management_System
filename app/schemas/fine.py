from pydantic import BaseModel, ConfigDict, Field
from datetime import date

class FineCreate(BaseModel):
    borrowing_id : int
    amount : float = Field(gt=0)

class FineUpdate(BaseModel):
    amount : float |None = Field(default= None, gt=0)
    is_paid : bool |None=None
    paid_date : date |None=None

class FineResponse(BaseModel):
    id : int
    borrowing_id : int
    amount : float 
    is_paid : bool 
    paid_date : date |None=None

    model_config =ConfigDict(from_attributes=True)
    