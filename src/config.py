from dotenv import load_dotenv
from os import getenv


print(load_dotenv())

GOOGLE_CLIENT_ID = getenv("GOOGLE_CLIENT_ID")
SWAGGER_HELPER_URL = f"{getenv('SWAGGER_HELPER_URL')}?clientId={GOOGLE_CLIENT_ID}"
ALGORITHM = "HS256"
SECRET_KEY = getenv("SECRET_KEY")
ACCESS_TOKEN_EXPIRE_MINUTES = int(getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))
