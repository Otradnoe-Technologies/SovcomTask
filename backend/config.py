import os
import sqlalchemy as db

PROJECT_PATH = os.path.dirname(__file__)
DB_PATH = PROJECT_PATH + "/data/app.db"

db_engine = db.create_engine("sqlite:////" + DB_PATH)
db_meta = db.MetaData(bind=db_engine)
db.MetaData.reflect(db_meta)