import databases
import sqlalchemy

DATABASE_URL="mysql+pymysql://root:root@127.0.0.1:3306/petsdb"

database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()
engine = sqlalchemy.create_engine(
    DATABASE_URL
)
