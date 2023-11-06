from backend.config import db_engine, db_meta
import sqlalchemy as db

class Task:

    @staticmethod
    def create(type, office_id, date):
        conn = db_engine.connect()
        task_table = db_meta.tables['task_type']
        query = db.insert(task_table).values(type=type, office_id=office_id,
                                                 date=date)
        conn.execute(query)
        conn.close()


    def __init__(self, task_id):
        conn = db_engine.connect()
        task_table = db_meta.tables.task

        # collect main info from the task table
        query = task_table.select().where(
                task_table.columns.task_id == task_id)
        output = conn.execute(query).fetchall()

        if len(output) == 0:
            # no such task
            return

        (self.id,
         self.office_id,
         self.type,
         self.status,
         self.comment,
         self.date,
         ) = output[0]

        # collect additional info from the task_type table
        task_type_table = db_meta.tables.task_type
        query = task_table.select().where(
            task_type_table.columns.type == self.type)
        output = conn.execute(query).fetchall()

        (self.title,
         self.priority,
         self.time_required,
         self.grade_required,
         self.condition_1,
         self.condition_2,
         ) = output[0]

        # getting employee_id if it's defined
        task_x_route = db_meta.tables.task_x_route
        query = task_x_route.select("route_id").where(
            task_type_table.c.task_id == self.id)
        output = conn.execute(query).fetchall()

        if len(output) == 0:
            # no employee doing this task
            self.employee_id = None
            return

        route_id = output[0]

        route_table = db_meta.tables.routes
        query = (route_table.select("employee_id")
            .where(
                route_table.columns.route_id == route_id
            )
        )
        output = conn.execute(query).fetchall()
        self.employee_id = output[0]

        conn.close()

    def __del__(self):
        # safe to db before quiting

        conn = db_engine.connect()
        employee_table = db_meta.tables.task

        query = db.update(employee_table).where(
            employee_table.c.task_id == self.id
        ).values(
            office_id=self.office_id,
            status=self.status,
            comment=self.comment,
        )

        conn.execute(query).fetchall()
        conn.close()
