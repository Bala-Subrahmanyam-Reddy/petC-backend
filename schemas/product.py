from pydantic import BaseModel


class product(BaseModel):
    id:str
    name:str
    pet_breads:str
    original_price:int
    sold_price:int
    pet_ages:str
    cat_id:str
    sub_cat_id:str
    is_enabled:bool
