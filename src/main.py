from fastapi import FastAPI
from common.config import DB_NAME, SQLALCHEMY_URL
from schemas.user import UserRes
from .routers.auth_router import auth_router
from .routers.profile_router import profile_router
from contextlib import asynccontextmanager
from os import system
from common.auth import Me_and_Session


@asynccontextmanager
async def lifespan(app: FastAPI):
    if SQLALCHEMY_URL.startswith("sqlite"):
        system(f"rm {DB_NAME}")
        system("alembic upgrade head")
    yield


app = FastAPI(
    lifespan=lifespan,
    swagger_ui_parameters={
        "tryItOutEnabled": True},
)
app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(profile_router, prefix="/profile", tags=["profile"])


@app.get("/me", response_model=UserRes | None)
async def get_me(me_and_session: Me_and_Session):
    me, _ = me_and_session

    return me
