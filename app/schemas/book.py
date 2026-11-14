from pydantic import BaseModel, ConfigDict

class BookCreate(BaseModel):
    title : str
    author_id : int
    category_id : int
    isbn : str
    price : float
    quantity : int = 0
    description : str |None= None


class BookUpdate(BaseModel):
    title : str |None= None
    author_id : int |None= None
    category_id : int |None= None
    isbn : str |None= None
    price : float |None= None
    quantity : int |None = None
    description : str |None= None

class BookResponse(BaseModel):
    id : int
    title : str
    author_id : int
    category_id : int
    isbn : str
    price : float
    quantity : int 
    description : str | None= None

    model_config = ConfigDict(from_attributes=True)