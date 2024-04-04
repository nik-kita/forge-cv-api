from datetime import timedelta
from common.config import ACCESS_SECRET_KEY, ACCESS_TOKEN_EXPIRE_MINUTES, ALGORITHM, REFRESH_SECRET_KEY, REFRESH_TOKEN_EXPIRE_DAYS
from utils.jwt import create_token
import enum


class JwtTypeEnum(str, enum.Enum):
    ACCESS = 'access',
    REFRESH = 'refresh'


def gen_jwt_res(user_id: int, jwt_type: JwtTypeEnum):
    data = {
        "id": user_id,
    }
    secret, expires_delta = (
        ACCESS_SECRET_KEY,
        ACCESS_TOKEN_EXPIRE_MINUTES,
    ) if jwt_type == JwtTypeEnum.ACCESS else (
        REFRESH_SECRET_KEY,
        REFRESH_TOKEN_EXPIRE_DAYS,
    )
    access_token = create_token(
        data=data,
        secret=secret,
        algorithm=ALGORITHM,
        expires_delta=expires_delta,
    )
    refresh_token = create_token(
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
