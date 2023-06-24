from pydantic import BaseModel


class orderInput(BaseModel):
    address_id: str
    order_amount: int
    payment_method: str
