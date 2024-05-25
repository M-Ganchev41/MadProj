from pydantic import BaseModel
from typing import Optional

class UsersBase(BaseModel):
    firstName: str
    lastName: str
    roleFK_ID: int

class UsersCreate(UsersBase):
    pass

class UsersOut(UsersBase):
    userID: int

    class Config:
        orm_mode = True

class UsersUpdate(BaseModel):
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    roleFK_ID: Optional[int] = None