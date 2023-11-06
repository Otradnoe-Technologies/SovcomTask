from backend.config import DB_PATH, PROJECT_PATH, db_engine
import sqlalchemy as db
from sqlalchemy import text, MetaData


scripts_path = PROJECT_PATH + "/data/scripts/"
meta_data = db.MetaData(bind=db_engine)
db.MetaData.reflect(meta_data)

def execute_sql_file(filename):
    connection = db_engine.connect()

    with open(scripts_path + filename, 'r') as file:
        queries = file.read().split(";")
        for query in queries:
            connection.execute(text(query))

    connection.close()
