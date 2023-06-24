from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, Boolean, TIMESTAMP
from config.db import metadata


orderModal = Table(
    'orders', metadata,
    Column('id', String(255), primary_key=True),
    Column('user_id', String(255)),
    Column('order_amount', Integer),
    Column('payment_method', String(255)),
    Column('payment_status', Boolean),
    Column('address_id', String(255)),
    Column('order_status', Boolean),
    Column('order_date', TIMESTAMP),
    Column('is_delivered', Boolean),
)
