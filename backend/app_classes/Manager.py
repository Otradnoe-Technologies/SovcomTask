from backend.config import db_engine, db_meta
import sqlalchemy as db

manager_table = db_meta.tables['manager']

class Manager:

    @staticmethod
    def create(name, email, password_hash):
        conn = db_engine.connect()
        conn.execute("PRAGMA foreign_keys=ON;")
        query = db.insert(manager_table).values(email=email, name=name,
                                                     password_hash=password_hash
                                                ).prefix_with('OR IGNORE')
        conn.execute(query)
        conn.close()

    @staticmethod
    def get_all():
        conn = db_engine.connect()

        query = db.select(manager_table.c["manager_id"])
        output = conn.execute(query).fetchall()

        managers = []
        for manager_id in output:
            managers.append(Manager(manager_id[0]))
        conn.close()
        return managers

    def __init__(self, email=None, manager_id=None):
        conn = db_engine.connect()

        # collect info from manager table
        query = ''
        if manager_id:
            # find by id
            query = db.select(manager_table).where(
                manager_table.columns.manager_id == manager_id)

        elif email:
            # find by email
            query = db.select(manager_table).where(
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


    def safe(self):
        if hasattr(self, 'id') is None:
            return
        # safe to db before quiting
        conn = db_engine.connect()
        conn.execute("PRAGMA foreign_keys=ON;")

        query = db.update(manager_table).where(
            manager_table.c.manager_id == self.id
        ).values(
            name=self.name,
            password_hash=self.password_hash,
            email=self.email,
        )

        conn.execute(query)
        conn.close()

    def __del__(self):
        self.safe()

    def __exit__(self):
        self.safe()