from fastapi import FastAPI
from sqlmodel import select
from .config import DB_NAME, SQLALCHEMY_URL
from database.core import Db
from database.models.profile import Profile
from database.models.user import UserRes, User
from .routers.auth import Me, router as auth_router
from .routers.profile import router as profile_router
from contextlib import asynccontextmanager
from os import system


@asynccontextmanager
async def lifespan(app: FastAPI):
    if SQLALCHEMY_URL.startswith("sqlite"):
        system(f"rm {DB_NAME}")
        system("alembic upgrade head")
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(profile_router, prefix="/profile", tags=["profile"])


@app.get("/me", response_model=UserRes)
async def get_me(me: Me):

    return me


@app.get("/all")
async def get_all(me: Me, session: Db):
    users = session.exec(select(User).limit(100)).all()

    return [{"email": u.email} for u in users]
