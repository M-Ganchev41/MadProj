import pandas

from app.api.models.model import (ModelCreate, ModelUpdate, ModelOut)

from app.api.util.db import(model, database, engine)

async def add_model(payload: ModelCreate):
    query = model.insert().values(**payload.dict())
    return await database.execute(query=query)


async def get_all_models():
    query = model.select()
    results = await database.fetch_all(query=query)
    return [
        {
            field: result[field]
            for field in ModelOut.__fields__.keys()
            if field in result
        }
        for result in results
    ]
    #df = pandas.read_sql_query(query, engine)
    #print(df)
    #return df



async def get_model(id: int):
    query = model.select().where(model.c.modelID == id)
    result = await database.fetch_one(query=query)
    if result:
        return {
                field: result[field]
                for field in ModelOut.__fields__.keys()
                if field in result
            }
    return result
    #df = pandas.read_sql_query(query, engine)
    #print(df)
    #return df


async def delete_model(id: int):
    query = model.delete().where(model.c.modelID == id)
    result = await database.execute(query=query)

async def update_model(id: int, payload: ModelUpdate):
    query = model.update().where(model.c.modelID == id).values(**payload.dict())
    await database.execute(query=query)
    return await get_model(id)