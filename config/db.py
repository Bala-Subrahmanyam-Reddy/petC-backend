import databases
import sqlalchemy

DATABASE_URL="mysql+pymysql://sql12628472:1XdxYgaw3G@sql12.freesqldatabase.com:3306/sql12628472"

database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()
engine = sqlalchemy.create_engine(
    DATABASE_URL
)
