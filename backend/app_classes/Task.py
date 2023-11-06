from backend.config import db_engine, db_meta
import sqlalchemy as db

task_table = db_meta.tables.task
task_type_table = db_meta.tables.task_type_table
task_x_route = db_meta.tables.task_x_route
route_table = db_meta.tables.routes

class Task:

    @staticmethod
    def create(type, office_id, date):
        conn = db_engine.connect()
        query = db.insert(task_table).values(type=type, office_id=office_id,
                                                 date=date)
        conn.execute(query)
        conn.close()

    @staticmethod
    def get_all():
        conn = db_engine.connect()

        query = task_table.select("task_id")
        output = conn.execute(query).fetchall()

        tasks = []
        for task_id in output:
            tasks.append(Task(task_id))
        conn.close()

    @staticmethod
    def get_active():
        conn = db_engine.connect()

        query = task_table.select("task_id").where(
            task_table.c.status == "В процессе"
            or task_table.c.status == "Приостановлен"
        )
        output = conn.execute(query).fetchall()

        tasks = []
        for task_id in output:
            tasks.append(Task(task_id))

        conn.close()


    def __init__(self, task_id):
        conn = db_engine.connect()

        # collect main info from the task table
        query = task_table.select().where(
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
        query = task_type_table.select().where(
            task_type_table.columns.type == self.type)
        output = conn.execute(query).fetchall()

        (
            self.title,
            self.priority,
            self.time_required,
            self.grade_required,
            self.condition_1,
            self.condition_2
         ) = output[0]

        # getting employee_id if it's defined
        query = task_x_route.select("route_id").where(
            task_x_route.c.task_id == self.id)
        output = conn.execute(query).fetchall()

        if len(output) == 0:
            # no employee doing this task
            self.employee_id = None
            conn.close()
            return

        route_id = output[0]

        query = route_table.select("employee_id").where(
            route_table.columns.route_id == route_id
        )

        output = conn.execute(query).fetchall()
        self.employee_id = output[0]

        conn.close()

    def __del__(self):
        # safe to db before quiting
        conn = db_engine.connect()

        query = db.update(task_table).where(
            task_table.c.task_id == self.id
        ).values(
            office_id=self.office_id,
            status=self.status,
            comment=self.comment,
        )

        conn.execute(query).fetchall()
        conn.close()
