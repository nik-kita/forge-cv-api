from datetime import timedelta, timezone, datetime
from jose import jwt, JWTError
from fastapi import HTTPException, status


def get_payload_from_token(
    token: str,
    secret: str,
    algorithms: list[str],
):
    try:
        payload = jwt.decode(token, secret, algorithms=algorithms)

        return payload
    except JWTError:
        try:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail=f"""\
Could not validate credentials! \
Untrusted payload: {jwt.get_unverified_claims(token)}\
    """,
                headers={"WWW-Authenticate": "Bearer"},
            )
        except JWTError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate credentials",
                headers={"WWW-Authenticate": "Bearer"},
            )


def create_token(
    data: dict,
    secret: str,
    algorithm: str,
    expires_delta: timedelta,
):

    print(expires_delta)
    print(type(expires_delta))
    print(datetime.now(timezone.utc))
    print(type(datetime.now(timezone.utc)))
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, secret, algorithm=algorithm)

    return encoded_jwt
