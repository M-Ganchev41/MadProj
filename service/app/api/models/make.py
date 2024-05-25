from pydantic import BaseModel
from typing import Optional

class MakeBase(BaseModel):
    makeName: str
    modelFK_ID: int

class MakeCreate(MakeBase):
    pass

class MakeOut(MakeBase):
    makeID: int

    class Config:
        orm_mode = True

class MakeUpdate(BaseModel):
    makeName: Optional[str] = None
    modelFK_ID: Optional[int] = None

