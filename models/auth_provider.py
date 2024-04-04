from sqlmodel import Enum
import enum


class AuthProviderEnum(str, enum.Enum):
    __name__ = "auth_provider"
    "google"


AuthProvider = Enum(AuthProviderEnum)
