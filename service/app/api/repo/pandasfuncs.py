import pandas as pd

from app.api.util.db import (car, make, model, subscription, users, roles, engine)

async def pd_filter(car_power: int):
    query_car = car.select()
    query_make = make.select()
    query_model = model.select()
    df_car_query = pd.read_sql_query(query_car, engine)
    df_make_query = pd.read_sql_query(query_make, engine)
    df_model_query = pd.read_sql_query(query_model, engine)
    df1 = pd.merge(df_car_query, df_make_query, left_on='makeFK_ID', right_on='makeID')
    df2 = pd.merge (df1, df_model_query, left_on='modelFK_ID', right_on='modelID')
    res = pd.DataFrame(df2, columns=["makeName", "modelName", "power", "availability"])
    return (res[res['power'] > car_power]).to_dict(orient='records')


