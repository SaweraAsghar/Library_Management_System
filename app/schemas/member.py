from pydantic import BaseModel, ConfigDict

class MemberCreate(BaseModel):
    name : str
    email : str
    phone : str |None=None
    address : str |None=None

class MemberUpdate(BaseModel):
    name : str |None=None
    email : str |None=None
    phone : str |None=None
    address : str |None=None
    is_active : bool |None=None

class MemberResponse(BaseModel):
    id : int
    name : str
    email : str
    phone : str |None=None
    address : str |None=None
    is_active : bool 

    model_config = ConfigDict(from_attributes=True)


 