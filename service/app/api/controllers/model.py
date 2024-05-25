from typing import List
from fastapi import APIRouter, HTTPException

from app.api.models.model import ModelOut, ModelUpdate, ModelCreate, ModelBase
import app.api.repo.model as modelrepo

model = APIRouter()

@model.post('/', response_model=ModelBase, status_code=201)
async def create_model(payload: ModelCreate):
    model_id = await modelrepo.add_model(payload)
    response = {'model_id': model_id, **payload.dict()}
    return response

@model.get('/', response_model=List[ModelOut])
async def get_models():
    return await modelrepo.get_all_models()

@model.get('/{id}/', response_model=ModelOut)
async def get_model(id: int):
    model=await modelrepo.get_model(id)
    if not model:
        raise HTTPException(status_code=404, detail="Model not found")
    return model

@model.put('/{id}/', response_model=ModelOut)
async def update_model(id: int, payload: ModelUpdate):
    model = await modelrepo.get_model(id)
    if not model:
        raise HTTPException(status_code=404, detail="Model not found")
    return await modelrepo.update_model(id, payload)

@model.delete('/{id}/', response_model=None)
async def delete_model(id: int):
    model = await modelrepo.get_model(id)
    if not model:
        raise HTTPException(status_code=404, detail="Model not found")
    return await modelrepo.delete_model(id)

