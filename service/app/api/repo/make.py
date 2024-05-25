import pandas

from app.api.models.make import (MakeCreate, MakeUpdate, MakeOut)

from app.api.util.db import (make, database, engine)

async def add_make(payload: MakeCreate):
    query = make.insert().values(**payload.dict())
    return await database.execute(query=query)


async def get_all_makes():
    query = make.select()
    results = await database.fetch_all(query=query)
    return [
        {
            field: result[field]
            for field in MakeOut.__fields__.keys()
            if field in result
        }
        for result in results
    ]
    #df = pandas.read_sql_query(query, engine)
    #print(df)
    #return df



async def get_make(id: int):
    query = make.select().where(make.c.makeID == id)
    result = await database.fetch_one(query=query)
    if result:
        return {
                field: result[field]
                for field in MakeOut.__fields__.keys()
                if field in result
            }
    return result
    #df = pandas.read_sql_query(query, engine)
    #print(df)
    #return df


async def delete_make(id: int):
    query = make.delete().where(make.c.makeID == id)
    result = await database.execute(query=query)

async def update_make(id: int, payload: MakeUpdate):
    query = make.update().where(make.c.makeID == id).values(**payload.dict())
    await database.execute(query=query)
    return await get_make(id)