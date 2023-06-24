from fastapi import APIRouter, Response
from sqlalchemy import text
from models.index import categoryModal
from schemas.index import category
from config.db import database

categoryRouter = APIRouter()


@categoryRouter.get("/getAllCategories")
async def getAllCategories():
    data = await database.fetch_all(categoryModal.select())
    return {"status": 200, "data": data}

