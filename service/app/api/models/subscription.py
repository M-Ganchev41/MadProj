from pydantic import BaseModel
from typing import Optional
from datetime import date

class SubscriptionBase(BaseModel):
    subscriptionStartDate: date
    subscriptionEndDate: date
    subscriptionDailyPrice: float
    carFK_ID: int
    userFK_ID: int

class SubscriptionCreate(SubscriptionBase):
    pass

class SubscriptionOut(SubscriptionBase):
    subscriptionID: int

    class Config:
        orm_mode = True

class SubscriptionUpdate(BaseModel):
    subscriptionStartDate: Optional[date] = None
    subscriptionEndDate: Optional[date] = None
    subscriptionDailyPrice: Optional[float] = None
    carFK_ID: Optional[int] = None
    userFK_ID: Optional[int] = None

