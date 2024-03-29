from fastapi import FastAPI
from .routers.auth import Me, router as auth_router
from .database.db import create_db_and_tables

app = FastAPI()
app.include_router(auth_router, prefix="/auth", tags=["auth"])


@app.get("/me")
async def get_me(me: Me):
    return me

create_db_and_tables()
