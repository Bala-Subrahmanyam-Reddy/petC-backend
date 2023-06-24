from pydantic import BaseModel


class subCategory(BaseModel):
    id:str
    cat_id:str
    name:str
    is_enabled:bool
