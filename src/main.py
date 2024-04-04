from fastapi import FastAPI
from sqlmodel import select
from common.config import DB_NAME, SQLALCHEMY_URL
from models.user import UserRes, User
from .routers.auth import router as auth_router
from .routers.profile import router as profile_router
from contextlib import asynccontextmanager
from os import system
from common.auth import Me_and_Session


@asynccontextmanager
async def lifespan(app: FastAPI):
    if SQLALCHEMY_URL.startswith("sqlite"):
        system(f"rm {DB_NAME}")
        system("alembic upgrade head")
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(profile_router, prefix="/profile", tags=["profile"])


@app.get("/me", response_model=UserRes | None)
async def get_me(me_and_session: Me_and_Session):
    me, _ = me_and_session
    print(me)
    return me


@app.get("/all")
async def get_all(me_and_session: Me_and_Session):
    _, session = me_and_session
    users = session.exec(select(User).limit(100)).all()

    return [{"email": u.email} for u in users]
