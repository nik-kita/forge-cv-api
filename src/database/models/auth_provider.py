from .versions.auth_provider_4451bbbfbdbd import AuthProvider4451bbbfbdbd
from sqlmodel import Enum

AuthProviderRaw = AuthProvider4451bbbfbdbd
AuthProvider = Enum(AuthProvider4451bbbfbdbd)
