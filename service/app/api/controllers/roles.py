from typing import List
from fastapi import APIRouter, HTTPException

from app.api.models.roles import RolesOut, RolesUpdate, RolesCreate, RolesBase
import app.api.repo.roles as rolesrepo

role = APIRouter()

@role.post('/', response_model=RolesBase, status_code=201)
async def create_role(payload: RolesCreate):
    role_id = await rolesrepo.add_role(payload)
    response = {'role_id': role_id, **payload.dict()}
    return response

@role.get('/', response_model=List[RolesOut])
async def get_roles():
    return await rolesrepo.get_all_roles()

@role.get('/{id}/', response_model=RolesOut)
async def get_role(id: int):
    role=await rolesrepo.get_role(id)
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")
    return role

@role.put('/{id}/', response_model=RolesOut)
async def update_role(id: int, payload: RolesUpdate):
    role = await rolesrepo.get_role(id)
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")
    return await rolesrepo.update_role(id, payload)

@role.delete('/{id}/', response_model=None)
async def delete_role(id: int):
    role = await rolesrepo.get_role(id)
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")
    return await rolesrepo.delete_role(id)

