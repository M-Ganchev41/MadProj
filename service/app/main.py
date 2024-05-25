from app.api.util.db import metadata, database, engine
from app.api.controllers.car import car
from app.api.controllers.make import make
from app.api.controllers.model import model
from app.api.controllers.roles import role
from app.api.controllers.subscription import subscription
from app.api.controllers.users import user
from app.api.controllers.pandasfunc import pdfnc

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from fastapi.encoders import jsonable_encoder
from starlette.exceptions import HTTPException as StarletteHTTPException
from sqlalchemy.exc import SQLAlchemyError

metadata.create_all(engine)
app = FastAPI(openapi_url="/api/v1/service/openapi.json",
               docs_url="/api/v1/service/docs")

@app.exception_handler(SQLAlchemyError)
async def sqlalchemy_exception_handler(request: Request, exc: SQLAlchemyError):
    return JSONResponse(status_code=500,
                        content={"message": "An error occured with the database operation", "detail": str(exc)}
                        )

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=422,
        content={"detail": exc.errors(), "body": exc.body}
    )


@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request: Request, exc: StarletteHTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail}
    )


@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"message": "An internal server error occurred.",
                 "detail": str(exc)},
    )


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

app.include_router(car, prefix='/api/car', tags=['car'])
app.include_router(model, prefix='/api/model', tags=['model'])
app.include_router(make, prefix='/api/make', tags=['make'])
app.include_router(user, prefix='/api/user', tags=['user'])
app.include_router(role, prefix='/api/role', tags=['role'])
app.include_router(subscription, prefix='/api/subscription', tags=['subscription'])
app.include_router(pdfnc, prefix='/api/pdFuncs', tags= ['PandasFuncs'])
