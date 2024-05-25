from typing import List
from fastapi import APIRouter, HTTPException

from app.api.models.users import UsersOut, UsersUpdate, UsersCreate, UsersBase
import app.api.repo.users as usersrepo

user = APIRouter()

@user.post('/', response_model=UsersBase, status_code=201)
async def create_user(payload: UsersCreate):
    user_id = await usersrepo.add_user(payload)
    response = {'user_id': user_id, **payload.dict()}
    return response

@user.get('/', response_model=List[UsersOut])
async def get_users():
    return await usersrepo.get_all_users()

@user.get('/{id}/', response_model=UsersOut)
async def get_user(id: int):
    user=await usersrepo.get_user(id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@user.put('/{id}/', response_model=UsersOut)
async def update_user(id: int, payload: UsersUpdate):
    user = await usersrepo.get_user(id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return await usersrepo.update_user(id, payload)

@user.delete('/{id}/', response_model=None)
async def delete_user(id: int):
    user = await usersrepo.get_user(id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return await usersrepo.delete_user(id)

