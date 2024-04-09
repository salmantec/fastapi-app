from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from . import models as models
from .crud.routes import router
from app.db_connection import engine

# To create table in pointed DB
models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def home():
    return """
        <html>
            <head>
                <title>Some HTML in here</title>
            </head>
            <body>
                <h1>Look ma! HTML!</h1>
            </body>
        </html>
        """

@app.get("/api/v1/healthcheck")
async def main_route() -> dict:
    return {"message": "The API is LIVE!!"}


app.include_router(router)
