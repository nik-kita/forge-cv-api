from sqlmodel import Enum
import enum


class AuthProviderEnum(str, enum.Enum):
    __name__ = "auth_provider"
    GOOGLE = "google"


AuthProvider = Enum(AuthProviderEnum)
