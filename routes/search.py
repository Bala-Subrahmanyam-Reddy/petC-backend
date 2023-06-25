from fastapi import APIRouter
from config.db import database
from models.index import productsModal
from sqlalchemy import text

searchRouter = APIRouter()


@searchRouter.get("/search")
async def search(searchText: str):
    splitWords = searchText.split()
    searchResult = []
    for eachText in splitWords:
        query=text(
            f"""
        SELECT products.*, GROUP_CONCAT(petbreads.name, ',') AS pet_breadNames,
        subcategories.name AS subCategoryName, categories.name AS categoryName
        FROM products
        JOIN petbreads ON instr(',' || products.pet_breads || ',', ',' || cast(petbreads.id as text) || ',') > 0
        JOIN subcategories ON subcategories.id = products.sub_cat_id
        JOIN categories ON categories.id = products.cat_id
        WHERE products.name LIKE '%' || '{eachText}' || '%'
        OR petbreads.name LIKE '%' || '{eachText}' || '%'
        OR products.pet_ages LIKE '%' || '{eachText}' || '%'
        OR products.sold_price <= {int(eachText) if eachText.isnumeric() else 0}
        GROUP BY products.id, products.pet_breads
            """
        )
        data = await database.fetch_all(query)
        if len(data) > 0:
            for eachProduct in data:
                if eachProduct not in searchResult:
                    searchResult.append(eachProduct)
    return {"status": 200, "data": searchResult}
