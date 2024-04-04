from datetime import timedelta
from common.config import ACCESS_SECRET_KEY, ACCESS_TOKEN_EXPIRE_MINUTES, ALGORITHM, REFRESH_SECRET_KEY, REFRESH_TOKEN_EXPIRE_DAYS
from utils import jwt_util
import enum


def gen_jwt_res(user_id: int):
    data = {
        "id": user_id,
    }
    access_token = jwt_util.create_token(
        data=data,
        secret=ACCESS_SECRET_KEY,
        algorithm=ALGORITHM,
        expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES),
    )
    refresh_token = jwt_util.create_token(
        data=data,
        secret=REFRESH_SECRET_KEY,
        algorithm=ALGORITHM,
        expires_delta=timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS),
    )

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer",
    }
