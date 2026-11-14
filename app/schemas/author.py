from pydantic import BaseModel, ConfigDict

class AuthorCreate(BaseModel):
    name :str
    email : str
    bio : str |None=None

class AuthorUpdate(BaseModel):
    name :str | None=None
    email : str | None=None
    bio : str | None=None

class AuthorResponse(BaseModel):
    id : int
    name :str
    email : str
    bio : str |None=None

    model_config = ConfigDict(from_attributes=True)
    