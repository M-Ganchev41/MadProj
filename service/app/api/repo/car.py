import pandas
import json

from app.api.models.car import (CarCreate, CarUpdate, CarOut)

from app.api.util.db import (car, database, engine)

async def add_car(payload: CarCreate):
    query = car.insert().values(**payload.dict())
    return await database.execute(query=query)


async def get_all_cars():
    query = car.select()
    results = await database.fetch_all(query=query)
    return [
        {
            field: result[field]
            for field in CarOut.__fields__.keys()
            if field in result
        }
        for result in results
    ]
    # dfquery = pandas.read_sql_query(query, engine)
    # df = pandas.DataFrame(dfquery, columns=["carID", "availability", "colour", "power", "makeFK_ID", "description"])
    # #print(df)
    # return df


async def get_car(id: int):
    query = car.select().where(car.c.carID == id)
    result = await database.fetch_one(query=query)
    if result:
        return {
                field: result[field]
                for field in CarOut.__fields__.keys()
                if field in result
            }
    return result
    
    #df = pandas.read_sql_query(query, engine)
    #print(df)
    #return df


async def delete_car(id: int):
    query = car.delete().where(car.c.carID == id)
    result = await database.execute(query=query)

async def update_car(id: int, payload: CarUpdate):
    query = car.update().where(car.c.carID == id).values(**payload.dict())
    await database.execute(query=query)
    return await get_car(id)