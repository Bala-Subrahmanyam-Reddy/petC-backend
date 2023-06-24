from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, Boolean, TIMESTAMP, JSON
from config.db import metadata


productsModal = Table(
    'products', metadata,
    Column('id', String(255), primary_key=True),
    Column('name', String(255)),
    Column('p_image', String(255)),
    Column('pet_breads', String(255)),
    Column('pet_ages', String(255)),
    Column('original_price', Integer),
    Column('sold_price', Integer),
    Column('cat_id', String(255)),
    Column('sub_cat_id', String(255)),
    Column('is_enabled', Boolean),

)
