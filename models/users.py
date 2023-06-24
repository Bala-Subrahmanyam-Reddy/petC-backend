from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, Boolean, TIMESTAMP
from config.db import metadata
from datetime import datetime


userModal = Table(
    'users', metadata,
    Column('id', String(255), primary_key=True),
    Column('name', String(255)),
    Column('email', String(255), unique=True),
    Column('password', String(255)),
    Column('pet_age', String(255)),
    Column('pet_bread', String(255)),
    Column('is_verified', Boolean),
)
