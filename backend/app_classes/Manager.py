from backend.config import db_engine, db_meta
import sqlalchemy as db

manager_table = db_meta.tables.manager

class Manager:

    @staticmethod
    def create(name, email, password_hash):
        conn = db_engine.connect()
        query = db.insert(manager_table).values(email=email, name=name,
                                                     password_hash=password_hash)
        conn.execute(query)
        conn.close()

    @staticmethod
    def get_all():
        conn = db_engine.connect()

        query = manager_table.select("manager_id")
        output = conn.execute(query).fetchall()

        managers = []
        for manager_id in output:
            managers.append(Manager(manager_id))
        conn.close()

    def __init__(self, email=None, id=None):
        conn = db_engine.connect()

        # collect info from manager table
        query = ''
        if id:
            # find by id
            query = manager_table.select().where(
                manager_table.columns.manager_id == id)

        elif email:
            # find by email
            query = manager_table.select().where(
                manager_table.columns.email == email)

        output = conn.execute(query).fetchall()
        conn.close()
        if len(output) == 0:
            # no such manager
            return

        (
            self.id,
            self.name,
            self.password_hash,
            self.email,
        ) = output[0]


    def __del__(self):
        # safe to db before quiting
        conn = db_engine.connect()

        query = db.update(manager_table).where(
            manager_table.c.manager_id == self.id
        ).values(
            name=self.name,
            password_hash=self.password_hash,
            email=self.email,
        )

        conn.execute(query).fetchall()
        conn.close()