from fastapi import FastAPI
from common.config import DB_NAME, SQLALCHEMY_URL, UI_URL
from schemas.user_schema import UserRes
from .routers.user_router import user_router
from .routers.auth_router import auth_router
from .routers.profile_router import profile_router
from contextlib import asynccontextmanager
from os import system
from common.auth import Me_and_Session
from fastapi.middleware.cors import CORSMiddleware


@asynccontextmanager
async def lifespan(app: FastAPI):
    if SQLALCHEMY_URL.startswith("sqlite"):
        system(f"rm {DB_NAME}")
        system("rm -fr migrations/__pycache__ migrations/versions/__pycache__")
        system("alembic upgrade head")
    yield


app = FastAPI(
    lifespan=lifespan,
    swagger_ui_parameters={
        "tryItOutEnabled": True},
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[UI_URL, 'http://localhost:4173'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(profile_router, prefix="/profiles", tags=["profiles"])
app.include_router(user_router, prefix='/user', tags=['user'])


@app.get("/me")
async def get_me(me_and_session: Me_and_Session) -> UserRes:
    me, _ = me_and_session

    return me
