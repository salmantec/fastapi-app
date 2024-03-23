from fastapi import FastAPI

from . import models as models
from .crud.routes import router
from app.db_connection import engine

# To create table in pointed DB
models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
async def main_route():
    return {"message": "Hey, Its me!!!"}

app.include_router(router)