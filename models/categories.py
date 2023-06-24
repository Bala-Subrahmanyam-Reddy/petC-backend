from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, Boolean, TIMESTAMP
from config.db import metadata


categoryModal = Table(
    'categories', metadata,
    Column('id', String(255), primary_key=True),
    Column('name', String(255)),
    Column('is_enabled', Boolean),
)
