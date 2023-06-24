from fastapi import APIRouter
from config.db import database
from models.index import subCategoryModal, categoryModal
from schemas.index import subCategory, category

subCategoryRouter = APIRouter()


@subCategoryRouter.get("/getAllSubCategories")
async def getAllSubCategories():
    query = subCategoryModal.select().where(
        categoryModal.c.id == subCategoryModal.c.cat_id)
    data = await database.fetch_all(query)
    return {"status": 200, "data": data}


@subCategoryRouter.get("/getSubCategoriesById")
async def getSubCategoriesById(category_id: str):
    query = subCategoryModal.select().where(
        subCategoryModal.c.cat_id == category_id)
    data = await database.fetch_all(query)
    return {"status": 200, "data": data}


@subCategoryRouter.get('/getAllSubCategoriesForEachCategory')
async def getAllSubCategoriesForEachCategory():
    query = categoryModal.select()
    categories = await database.fetch_all(query)
    data = []
    if len(categories) > 0:
        for eachCategory in categories:
            sub_query = subCategoryModal.select().where(
                subCategoryModal.c.cat_id == eachCategory.id)
            subCategories = await database.fetch_all(sub_query)
            data.append({"categoryId": eachCategory.id,
                        "categoryName": eachCategory.name,
                         "subCategories": subCategories})
        return {"status": 200, "data": data}
    return {"status": 200, "data": data}
