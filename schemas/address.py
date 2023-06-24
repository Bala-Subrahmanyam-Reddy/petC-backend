from pydantic import BaseModel


class address(BaseModel):
    id: str
    user_id: str
    city: str
    pincode: int
    address: str


class addressInput(BaseModel):
    city: str
    pincode: int
    address: str
