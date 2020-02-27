import databases
import sqlalchemy

from .envs import DB_HOST, DB_NAME, DB_PASSWORD, DB_PORT, DB_USER

DATABASE_URL = f"mysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# databases
database = databases.Database(DATABASE_URL, min_size=5, max_size=20)

engine = sqlalchemy.create_engine(DATABASE_URL, echo=False)

metadata = sqlalchemy.MetaData()
