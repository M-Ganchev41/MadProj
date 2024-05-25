import pandas

from app.api.models.roles import (RolesUpdate, RolesCreate, RolesOut)

from app.api.util.db import(roles, database, engine)

async def add_role(payload: RolesCreate):
    query = roles.insert().values(**payload.dict())
    return await database.execute(query=query)


async def get_all_roles():
    query = roles.select()
    results = await database.fetch_all(query=query)
    return [
        {
            field: result[field]
            for field in RolesOut.__fields__.keys()
            if field in result
        }
        for result in results
    ]
    #df = pandas.read_sql_query(query, engine)
    #print(df)
    #return df



async def get_role(id: int):
    query = roles.select().where(roles.c.roleID == id)
    result = await database.fetch_one(query=query)
    if result:
        return {
                field: result[field]
                for field in RolesOut.__fields__.keys()
                if field in result
            }
    return result
    #df = pandas.read_sql_query(query, engine)
    #print(df)
    #return df


async def delete_role(id: int):
    query = roles.delete().where(roles.c.roleID == id)
    result = await database.execute(query=query)

async def update_role(id: int, payload: RolesUpdate):
    query = roles.update().where(roles.c.roleID == id).values(**payload.dict())
    await database.execute(query=query)
    return await get_role(id)