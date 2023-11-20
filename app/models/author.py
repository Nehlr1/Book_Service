from pydantic import BaseModel

class AuthorBase(BaseModel):
    full_name: str

class AuthorCreate(AuthorBase):
    pass

class Author(AuthorBase):
    id: int

    class Config:
        orm_mode = True