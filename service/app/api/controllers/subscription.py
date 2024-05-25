from typing import List
from fastapi import APIRouter, HTTPException

from app.api.models.subscription import SubscriptionOut, SubscriptionUpdate, SubscriptionCreate, SubscriptionBase
import app.api.repo.subscription as subscriptionrepo

subscription = APIRouter()

@subscription.post('/', response_model=SubscriptionBase, status_code=201)
async def create_subscription(payload: SubscriptionCreate):
    subscription_id = await subscriptionrepo.add_subscription(payload)
    response = {'subscription_id': subscription_id, **payload.dict()}
    return response

@subscription.get('/', response_model=List[SubscriptionOut])
async def get_subscriptions():
    return await subscriptionrepo.get_all_subscriptions()

@subscription.get('/{id}/', response_model=SubscriptionOut)
async def get_subscription(id: int):
    subscription=await subscriptionrepo.get_subscription(id)
    if not subscription:
        raise HTTPException(status_code=404, detail="Subscription not found")
    return subscription

@subscription.put('/{id}/', response_model=SubscriptionOut)
async def update_subscription(id: int, payload: SubscriptionUpdate):
    subscription = await subscriptionrepo.get_subscription(id)
    if not subscription:
        raise HTTPException(status_code=404, detail="Subscription not found")
    return await subscriptionrepo.update_subscription(id, payload)

@subscription.delete('/{id}/', response_model=None)
async def delete_subscription(id: int):
    subscription = await subscriptionrepo.get_subscription(id)
    if not subscription:
        raise HTTPException(status_code=404, detail="Subscription not found")
    return await subscriptionrepo.delete_subscription(id)

