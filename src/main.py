from fastapi import FastAPI
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
