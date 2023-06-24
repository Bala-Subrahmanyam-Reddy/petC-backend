from fastapi import APIRouter, Response
from sqlalchemy import text
from models.index import addressModal
from config.db import database
from schemas.index import address, addressInput
from uuid import uuid1

addressRouter = APIRouter()


@addressRouter.get("/getAllAddressesById")
async def getAllAddressesById(userId: str):
    data = await database.fetch_all(addressModal.select().where(addressModal.c.user_id == userId))
    return {"status": 200, "data": data}


@addressRouter.post("/newAddress")
async def newAddress(userId: str, request: addressInput):
    addressId = str(uuid1())
    query = addressModal.insert().values(
        id=addressId,
        user_id=userId,
        city=request.city,
        pincode=request.pincode,
        address=request.address,
    )
    await database.execute(query)
    return {"status": 201, "msg": "address created", "data": {"id": addressId, **request.dict()}}
