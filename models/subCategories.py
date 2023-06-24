from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, Boolean, TIMESTAMP
from config.db import metadata


subCategoryModal = Table(
    'subcategories', metadata,
    Column('id', String(255), primary_key=True),
     Column('cat_id', String(255)),
    Column('name', String(255)),
    Column('is_enabled', Boolean),
)
