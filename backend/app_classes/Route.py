from backend.config import db_engine, db_meta
import sqlalchemy as db
from .Task import Task

route_table = db_meta.tables['route']

class Route:
    @staticmethod
    def create(employee_id, tasks, date, status = 'Не начат', distance=None):
        conn = db_engine.connect()

        # first insert route to route table
        route_table = db_meta.tables.route
        query = db.insert(route_table).values(employee_id=employee_id, status=status,
                                             date=date, distance=distance)
        conn.execute(query)

        route = Route(employee_id, date)
        route.tasks = tasks

        # add route tasks into route_X_task table
        route_x_task = db_meta.tables.route_X_task

        for i, task in route.tasks:
            query = db.insert(route_x_task).values(route_id=route.id, task_id=task.id,
                                                   order_in_route=i)
            conn.execute(query)

        conn.close()

    @staticmethod
    def get_all():
        conn = db_engine.connect()

        query = route_table.select("route_id")
        output = conn.execute(query).fetchall()

        routes = []
        for route_id in output:
            routes.append(Task(route_id))
        conn.close()


    @staticmethod
    def get_active():
        conn = db_engine.connect()

        query = route_table.select("route_id").where(
            route_table.columns.status != "Не закончен"
            and route_table.columns.status != "Закончен"
        )
        output = conn.execute(query).fetchall()

        routes = []
        for route_id in output:
            routes.append(Task(route_id))
        conn.close()


    def __init__(self, route_id=None, employee_id=None, date=None):
        conn = db_engine.connect()
        route_table = db_meta.tables.task
        query = ""
        if route_id:
            query = route_table.select().where(
                route_table.c.route_id == route_id)

        elif employee_id and date:
            query = route_table.select().where(
                route_table.c.employee_id == employee_id
                and route_table.c.date == date
            )

        output = conn.execute(query).fetchall()

        if len(output) == 0:
            # no such route
            conn.close()
            return

        (
            self.id,
            self.employee_id,
            self.date,
            self.distance,
            self.status
        ) = output[0]

        # collect tasks from route_X_task table
        route_x_task = db_meta.tables.route_X_task
        query = route_x_task.select("task_id").where(
            route_table.c.route_id == self.id)
        output = conn.execute(query).fetchall()

        self.tasks = []
        for task_id in output:
            self.tasks.append(Task(task_id))

        conn.close()


    def __del__(self):
        # safe to db before quiting
        conn = db_engine.connect()

        # safe route into route table
        route_table = db_meta.tables.route
        query = db.update(route_table).where(
            route_table.c.route_id == self.id
        ).values(
            employee_id=self.employee_id,
            date=self.date,
            distance=self.distance,
            status=self.status,
        )
        conn.execute(query).fetchall()

        # safe all the corresponding tasks
        route_x_task = db_meta.tables.route_X_task
        for i, task in self.tasks:
            query = db.update(route_x_task).where(
                route_x_task.c.task_id == task.id
            ).values(
                route_id=self.id,
                order_in_route=i
            )
            conn.execute(query).fetchall()

        conn.close()


