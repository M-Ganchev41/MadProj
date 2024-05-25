from typing import List
from fastapi import APIRouter, HTTPException

from app.api.models.make import MakeOut, MakeUpdate, MakeCreate, MakeBase
import app.api.repo.make as makerepo

make = APIRouter()

@make.post('/', response_model=MakeBase, status_code=201)
async def create_make(payload: MakeCreate):
    make_id = await makerepo.add_make(payload)
    response = {'make_id': make_id, **payload.dict()}
    return response

@make.get('/', response_model=List[MakeOut])
async def get_makes():
    return await makerepo.get_all_makes()

@make.get('/{id}/', response_model=MakeOut)
async def get_make(id: int):
    make=await makerepo.get_make(id)
    if not make:
        raise HTTPException(status_code=404, detail="Make not found")
    return make

@make.put('/{id}/', response_model=MakeOut)
async def update_make(id: int, payload: MakeUpdate):
    make = await makerepo.get_make(id)
    if not make:
        raise HTTPException(status_code=404, detail="Make not found")
    return await makerepo.update_make(id, payload)

@make.delete('/{id}/', response_model=None)
async def delete_make(id: int):
    make = await makerepo.get_make(id)
    if not make:
        raise HTTPException(status_code=404, detail="Make not found")
    return await makerepo.delete_make(id)

