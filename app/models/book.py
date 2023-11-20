from pydantic import BaseModel
from typing import List

class BookBase(BaseModel):
    title: str
    author_id: int

class BookCreate(BookBase):
    pass

class Book(BookBase):
    id: int

    class Config:
        orm_mode = True

class BookList(BaseModel):
    books: List[Book]