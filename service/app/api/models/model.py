from pydantic import BaseModel
from typing import Optional

class ModelBase(BaseModel):
    modelName: str

class ModelCreate(ModelBase):
    pass

class ModelOut(ModelBase):
    modelID: int

    class Config:
        orm_mode = True

class ModelUpdate(BaseModel):
    modelName: Optional[str] = None