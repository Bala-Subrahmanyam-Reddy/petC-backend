from fastapi import APIRouter
from config.db import database
from models.index import orderModal
from schemas.index import orderInput
from sqlalchemy import text
from uuid import uuid1
from datetime import datetime


orderRouter = APIRouter()


@orderRouter.post('/createOrder')
async def createOrder(request: orderInput, userId: str):
    orderId = str(uuid1())
    timestamp = datetime.now()
    query = orderModal.insert().values(
        id=orderId,
        user_id=userId,
        order_amount=request.order_amount,
        payment_method=request.payment_method,
        payment_status=1,
        address_id=request.address_id,
        order_status=1,
        order_date=timestamp,
        is_delivered=1
    )
    await database.execute(query)
    return {"status": 201, "msg": "order created", "data": {"id": orderId, **request.dict()}}
