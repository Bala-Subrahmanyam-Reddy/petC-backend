from fastapi import APIRouter
from config.db import database
from models.index import productsModal
from sqlalchemy import text

productRouter = APIRouter()


async def getProductsBySubCategoryIdFunction(subCategoryId: str):
    query = text(f"""
        SELECT products.*, GROUP_CONCAT(petbreads.name) AS pet_breadNames,
        subcategories.name AS subCategoryName,categories.name as categoryName FROM products 
        JOIN petbreads ON FIND_IN_SET(petbreads.id, products.pet_breads) > 0 
        JOIN subcategories ON subcategories.id=products.sub_cat_id 
        JOIN categories ON categories.id=products.cat_id WHERE products.sub_cat_id='{subCategoryId}'
        GROUP BY products.id, products.pet_breads;
        """)
    data = await database.fetch_all(query)
    return data


async def getProductsByCategoryIdFunction(categoryId: str):
    query = text(f"""
        SELECT products.*, GROUP_CONCAT(petbreads.name) AS pet_breadNames,
        subcategories.name AS subCategoryName,categories.name as categoryName FROM products 
        JOIN petbreads ON FIND_IN_SET(petbreads.id, products.pet_breads) > 0 
        JOIN subcategories ON subcategories.id=products.sub_cat_id 
        JOIN categories ON categories.id=products.cat_id WHERE products.cat_id='{categoryId}'
        GROUP BY products.id, products.pet_breads;
        """)
    data = await database.fetch_all(query)
    return data


@productRouter.get("/getAllProducts")
async def getAllProducts():
    query = text("""
    SELECT products.*, GROUP_CONCAT(petbreads.name) AS pet_breadNames,
    subcategories.name AS subCategoryName,categories.name as categoryName FROM products 
    JOIN petbreads ON FIND_IN_SET(petbreads.id, products.pet_breads) > 0 
    JOIN subcategories ON subcategories.id=products.sub_cat_id 
    JOIN categories ON categories.id=products.cat_id 
    GROUP BY products.id, products.pet_breads;
    """)
    data = await database.fetch_all(query)
    return {"status": 200, "data": data}


@productRouter.get("/getProductsByCategoryId")
async def getProductsByCategoryId(categoryId: str):
    data = await getProductsByCategoryIdFunction(categoryId)
    return {"status": 200, "data": data}


@productRouter.get("/getProductsBySubCategoryId")
async def getProductsBySubCategoryId(subCategoryId: str):
    data = await getProductsBySubCategoryIdFunction(subCategoryId)
    return {"status": 200, "data": data}


@productRouter.get("/getProductsByCategories")
async def getProductsByCategories():
    query = text(f"""
       SELECT id,name FROM categories
    """)
    categoriesData = await database.fetch_all(query)
    data = []
    for i in range(len(categoriesData)):
        products = await getProductsByCategoryIdFunction(categoriesData[i].id)
        data.append(
            {"categoryId": categoriesData[i].id,
             "categoryName": categoriesData[i].name,
             "products": products}
        )
    return {"status": 200, "data": data}


@productRouter.get("/getProductById")
async def getProductById(productId: str):
    query = text(f"""
    SELECT products.*, GROUP_CONCAT(petbreads.name) AS pet_breadNames,
    subcategories.name AS subCategoryName,categories.name as categoryName FROM products 
    JOIN petbreads ON FIND_IN_SET(petbreads.id, products.pet_breads) > 0 
    JOIN subcategories ON subcategories.id=products.sub_cat_id 
    JOIN categories ON categories.id=products.cat_id WHERE products.id='{productId}'
    GROUP BY products.id, products.pet_breads;
    """)
    data = await database.fetch_all(query)
    return {"status": 200, "data": data}
