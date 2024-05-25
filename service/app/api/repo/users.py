import pandas

from app.api.models.users import (UsersCreate, UsersUpdate, UsersOut)

from app.api.util.db import (users, database, engine)

async def add_user(payload: UsersCreate):
    query = users.insert().values(**payload.dict())
    return await database.execute(query=query)


async def get_all_users():
    query = users.select()
    results = await database.fetch_all(query=query)
    return [
        {
            field: result[field]
            for field in UsersOut.__fields__.keys()
            if field in result
        }
        for result in results
    ]
    #df = pandas.read_sql_query(query, engine)
    #print(df)
    #return df



async def get_user(id: int):
    query = users.select().where(users.c.userID == id)
    result = await database.fetch_one(query=query)
    if result:
        return {
                field: result[field]
                for field in UsersOut.__fields__.keys()
                if field in result
            }
    return result
    #df = pandas.read_sql_query(query, engine)
    #print(df)
    #return df


async def delete_user(id: int):
    query = users.delete().where(users.c.userID == id)
    result = await database.execute(query=query)

async def update_user(id: int, payload: UsersUpdate):
    query = users.update().where(users.c.userID == id).values(**payload.dict())
    await database.execute(query=query)
    return await get_user(id)