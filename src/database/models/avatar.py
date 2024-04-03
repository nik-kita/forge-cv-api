from .versions.avatar_f11abea855d3 import Avatar_f11abea855d3


BaseAvatar = Avatar_f11abea855d3


class Avatar(BaseAvatar, table=True):
    __tablename__ = "avatars"
