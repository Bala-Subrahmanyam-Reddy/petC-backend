from fastapi import APIRouter, Response
from sqlalchemy import text
from models.index import petBreadsModal
from config.db import database

breadsRouter = APIRouter()


@breadsRouter.get("/getAllBreads")
async def getAllBreads():
    data = await database.fetch_all(petBreadsModal.select())
    return {"status": 200, "data": data}

