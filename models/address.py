from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, Boolean, TIMESTAMP
from config.db import metadata


addressModal = Table(
    'address', metadata,
    Column('id', String(255), primary_key=True),
    Column('user_id', String(255)),
    Column('city', String(255)),
    Column('pincode', Integer),
    Column('address', String(255)),

)
