from fastapi import APIRouter, Response

import pandas as pd

import app.api.repo.pandasfuncs as pdfunc

pdfnc = APIRouter()


@pdfnc.get('/')
async def filter_pandas(car_power: int):
    #res_data = await (pdfunc.pd_filter())()
    res_data = await pdfunc.pd_filter(car_power)
    #df=pd.DataFrame(res_data)
    return res_data