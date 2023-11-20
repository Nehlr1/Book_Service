from pydantic import BaseModel

class ClientBase(BaseModel):
    full_name: str

class ClientCreate(ClientBase):
    pass

class Client(ClientBase):
    id: int

    class Config:
        orm_mode = True