from typing import List
from fastapi import APIRouter, HTTPException

from app.api.models.car import CarOut, CarUpdate, CarCreate, CarBase
import app.api.repo.car as carrepo

car = APIRouter()

@car.post('/', response_model=CarBase, status_code=201)
async def create_car(payload: CarCreate):
    car_id = await carrepo.add_car(payload)
    response = {'car_id': car_id, **payload.dict()}
    return response

@car.get('/', response_model=List[CarOut])
async def get_cars():
    return await carrepo.get_all_cars()

@car.get('/{id}/', response_model=CarOut)
async def get_car(id: int):
    car=await carrepo.get_car(id)
    if not car:
        raise HTTPException(status_code=404, detail="Car not found")
    return car

@car.put('/{id}/', response_model=CarOut)
async def update_car(id: int, payload: CarUpdate):
    car = await carrepo.get_car(id)
    if not car:
        raise HTTPException(status_code=404, detail="Car not found")
    return await carrepo.update_car(id, payload)

@car.delete('/{id}/', response_model=None)
async def delete_car(id: int):
    car = await carrepo.get_car(id)
    if not car:
        raise HTTPException(status_code=404, detail="Car not found")
    return await carrepo.delete_car(id)

