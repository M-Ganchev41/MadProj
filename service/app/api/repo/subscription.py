import pandas

from app.api.models.subscription import (SubscriptionCreate, SubscriptionUpdate, SubscriptionOut)

from app.api.util.db import(subscription, database, engine)

async def add_subscription(payload: SubscriptionCreate):
    query = subscription.insert().values(**payload.dict())
    return await database.execute(query=query)


async def get_all_subscriptions():
    query = subscription.select()
    results = await database.fetch_all(query=query)
    return [
        {
            field: result[field]
            for field in SubscriptionOut.__fields__.keys()
            if field in result
        }
        for result in results
    ]
    #df = pandas.read_sql_query(query, engine)
    #print(df)
    #return df



async def get_subscription(id: int):
    query = subscription.select().where(subscription.c.subscriptionID == id)
    result = await database.fetch_one(query=query)
    if result:
        return {
                field: result[field]
                for field in SubscriptionOut.__fields__.keys()
                if field in result
            }
    return result
    #df = pandas.read_sql_query(query, engine)
    #print(df)
    #return df


async def delete_subscription(id: int):
    query = subscription.delete().where(subscription.c.subscriptionID == id)
    result = await database.execute(query=query)

async def update_subscription(id: int, payload: SubscriptionUpdate):
    query = subscription.update().where(subscription.c.subscriptionID == id).values(**payload.dict())
    await database.execute(query=query)
    return await get_subscription(id)