from pydantic import BaseModel


class category(BaseModel):
    id:str
    name:str
    is_enabled:bool
