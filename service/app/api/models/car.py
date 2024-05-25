from pydantic import BaseModel
from typing import Optional

class CarBase(BaseModel):
    availability: bool
    colour: str
    power: int
    description: str
    makeFK_ID: int

class CarCreate(CarBase):
    pass

class CarOut(CarBase):
    carID: int

    class Config:
        orm_mode = True

class CarUpdate(BaseModel):
    availability: Optional[bool] = None
    colour: Optional[str] = None
    power: Optional[int] = None
    makeFK_ID: Optional[int] = None
    description: Optional[str] = None

