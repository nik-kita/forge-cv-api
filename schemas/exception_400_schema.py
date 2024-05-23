from pydantic import BaseModel


class Exception_400(BaseModel):
    message: str
    beauty_message: None | str = None
