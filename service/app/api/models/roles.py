from pydantic import BaseModel
from typing import Optional

class RolesBase(BaseModel):
    roleName: str

class RolesCreate (RolesBase):
    pass

class RolesOut (RolesBase):
    roleID: int

    class Config:
        orm_mode = True

class RolesUpdate (BaseModel):
    roleName: Optional[str] = None