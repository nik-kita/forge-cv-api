from fastapi import FastAPI
from sqlmodel import select

from src.database.db import ActualSession
from src.database.user import User
from .routers.auth import Me, router as auth_router
from contextlib import asynccontextmanager
from os import system


@asynccontextmanager
async def lifespan(app: FastAPI):
    system("alembic upgrade head")
    yield
    print("Shutting down")


app = FastAPI(lifespan=lifespan)
app.include_router(auth_router, prefix="/auth", tags=["auth"])


@app.get("/me")
async def get_me(me: Me):
    return me


@app.get("/all")
async def get_all(me: Me, session: ActualSession):
    users = session.exec(select(User).limit(100)).all()

    return [{"email": u.email} for u in users]
