from backend.config import db_engine, db_meta
import sqlalchemy as db
from Task import Task

office_table = db_meta.tables['office']
task_table = db_meta.tables['task']

class office:

    @staticmethod
    def create(address, when_opened = 'вчера',
               materials_delivered = 'нет', days_since_last_card = 0,
               accepted_applications = 0, given_cards = 0):
        conn = db_engine.connect()
        conn.execute("PRAGMA foreign_keys=ON;")
        query = db.insert(office_table).values(address=address,
                                                when_opened=when_opened,
                                                materials_delivered=materials_delivered,
                                                days_since_last_card=days_since_last_card,
                                                accepted_applications=accepted_applications,
                                                given_cards=given_cards
                                               ).prefix_with('OR IGNORE')
        conn.execute(query)
        conn.close()

    @staticmethod
    def get_all():
        conn = db_engine.connect()

        query = db.select(office_table.c["office_id"])
        output = conn.execute(query).fetchall()

        offices = []
        for office_id in output:
            offices.append(office(office_id[0]))
        conn.close()

        return offices

    def __init__(self, office_id=None):
        conn = db_engine.connect()

        # collect info from office table
        query = db.select(office_table).where(
                office_table.columns.office_id == office_id)

        output = conn.execute(query).fetchall()
        if len(output) == 0:
            # no such office
            return

        (
            self.id,
            self.address,
            self.when_opened,
            self.materials_delivered,
            self.days_since_last_card,
            self.accepted_applications,
            self.given_cards,
            self.coordinates
        ) = output[0]

        query = db.select(task_table.c["task_id"]).where(
            task_table.c.office_id == self.id
        )
        output = conn.execute(query).fetchall()

        tasks = []
        for task_id in output:
            tasks.append(Task(task_id))

        self.tasks = tasks

        conn.close()


    def safe(self):
        if hasattr(self, 'id') is None:
            return
        # safe to db before quiting
        conn = db_engine.connect()
        conn.execute("PRAGMA foreign_keys=ON;")

        query = db.update(office_table).where(
            office_table.c.office_id == self.id
        ).values(
            address=self.address,
            when_opened=self.when_opened,
            materials_delivered=self.materials_delivered,
            days_since_last_card=self.days_since_last_card,
            accepted_applications=self.accepted_applications,
            given_cards=self.given_cards,
            coordinates=self.coordinates
        )

        conn.execute(query).fetchall()
        conn.close()

    def __del__(self):
        self.safe()

    def __exit__(self):
        self.safe()
