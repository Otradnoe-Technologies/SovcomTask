from backend.config import db_engine, db_meta
import sqlalchemy as db
from sqlalchemy import exc as sa_exc
from datetime import datetime
import warnings

# Suppress SQLAlchemy warnings
warnings.filterwarnings('ignore', '.*SAWarning.*')

task_table = db_meta.tables['task']
task_type_table = db_meta.tables['task_type']
task_x_route = db_meta.tables['route_X_task']
route_table = db_meta.tables['route']

class Task:

    @staticmethod
    def create(type, office_id, date=None, status="Не назначена"):
        if date is None:
            date = datetime.today().strftime('%Y-%m-%d')

        conn = db_engine.connect()
        conn.execute("PRAGMA foreign_keys=ON;")
        query = db.insert(task_table).values(type=type, office_id=office_id,
                                                 date=date, status=status
                                             ).prefix_with('OR IGNORE')
        try:
            conn.execute(query)
        except sa_exc.SQLAlchemyError:
            pass

        conn.close()


    @staticmethod
    def get_all():
        conn = db_engine.connect()

        query = db.select(task_table.c["task_id"])
        output = conn.execute(query).fetchall()

        tasks = []
        for task_id in output:
            tasks.append(Task(task_id=task_id[0]))

        conn.close()
        return tasks


    @staticmethod
    def get_active():
        conn = db_engine.connect()

        query = db.select(task_table.c["task_id"]).where(
            task_table.c.status == "В процессе"
            or task_table.c.status == "Приостановлен"
        )
        output = conn.execute(query).fetchall()

        tasks = []
        for task_id in output:
            tasks.append(Task(task_id))

        conn.close()
        return tasks


    def __init__(self, task_id):
        if task_id is None:
            return
        conn = db_engine.connect()

        # collect main info from the task table
        query = db.select(task_table).where(
                task_table.columns.task_id == task_id)
        output = conn.execute(query).fetchall()

        if len(output) == 0:
            # no such task
            conn.close()
            return

        (
            self.id,
            self.office_id,
            self.type,
            self.status,
            self.comment,
            self.date,
        ) = output[0]

        # collect additional info from the task_type table
        query = db.select(task_type_table).where(
            task_type_table.columns.type == self.type)
        output = conn.execute(query).fetchall()

        (
            self.type,
            self.title,
            self.priority,
            self.time_required,
            self.grade_required,
            self.condition_1,
            self.condition_2
         ) = output[0]

        # getting employee_id if it's defined
        query = db.select(task_x_route.c["route_id"]).where(
            task_x_route.c.task_id == self.id)
        output = conn.execute(query).fetchall()

        if len(output) == 0:
            # no employee doing this task
            self.employee_id = None
            conn.close()
            return

        route_id = output[0]

        query = db.select(route_table.c["employee_id"]).where(
            route_table.columns.route_id == route_id
        )

        output = conn.execute(query).fetchall()
        self.employee_id = output[0]

        conn.close()


    def safe(self):
        if not hasattr(self, 'id'):
            return
        # safe to db
        conn = db_engine.connect()
        conn.execute("PRAGMA foreign_keys=ON;")

        query = db.update(task_table).where(
            task_table.c.task_id == self.id
        ).values(
            type=self.type,
            office_id=self.office_id,
            status=self.status,
            comment=self.comment,
        )

        try:
            conn.execute(query)
        except sa_exc.SQLAlchemyError:
            pass

        conn.close()


    def __del__(self):
        self.safe()

    def __exit__(self):
        self.safe()
