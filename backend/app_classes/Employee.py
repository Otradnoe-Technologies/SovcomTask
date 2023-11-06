from backend.config import db_engine, db_meta
import sqlalchemy as db
import Route
import Task

class Employee:

    @staticmethod
    def create(name, email, password_hash):
        conn = db_engine.connect()
        employee_table = db_meta.tables['employee']
        query = db.insert(employee_table).values(email=email, name=name,
                                                     password_hash=password_hash)
        conn.execute(query)
        conn.close()


    def __init__(self, email=None, id=None):
        conn = db_engine.connect()
        employee_table = db_meta.tables['employee']

        # collect info from employee table
        query = ''
        if id:
            # find by id
            query = employee_table.select().where(
                employee_table.columns.employee_id == id)

        elif email:
            # find by email
            query = employee_table.select().where(
                employee_table.columns.email == email)

        output = conn.execute(query).fetchall()
        if len(output) == 0:
            # no such employee
            return

        (self.id,
         self.name,
         self.default_address,
         self.grade,
         self.password_hash,
         self.email,
         self.account_approved
         ) = output[0]

        conn.close()

    def __del__(self):
        # safe to db before quiting

        conn = db_engine.connect()
        employee_table = db_meta.tables['employee']

        query = db.update(employee_table).where(
                employee_table.c.employee_id == self.id
            ).values(
                name=self.name,
                default_addres=self.default_address,
                grade=self.grade,
                password_hash=self.password_hash,
                email=self.email,
                account_approved=self.account_approved
            )

        conn.execute(query).fetchall()
        conn.close()

    def get_routes_history(self):
        route_table = db_meta.tables.routes
        conn = db_engine.connect()
        query = (route_table.select("route_id")
                 .where(
                    route_table.columns.employee_id == self.id
                ).order_by(
                    route_table.columns.date
                )
        )
        output = conn.execute(query).fetchall()

        routes_history = []
        for route_id in output:
            routes_history.append(Route(route_id))

        conn.close()
        return routes_history


    def get_tasks_history(self):
        routes_history = self.get_routes_history()

        tasks_history = []
        for route in routes_history:
            for task_id in route.task_ids:
                tasks_history.append(Task(task_id))

        return tasks_history


    def get_current_routes(self):
        route_table = db_meta.tables.routes
        conn = db_engine.connect()
        query = (route_table.select("route_id")
            .where(
                route_table.columns.employee_id == self.id
                and route_table.columns.status != "Не закончен"
                and route_table.columns.status != "Закончен"
            ).sort_by(
                route_table.columns.date
            )
        )
        output = conn.execute(query).fetchall()

        current_routes = []
        for route_id in output:
            current_routes.append(Route(route_id))

        conn.close()
        return current_routes

    def get_current_task(self):
        current_routes = self.get_current_routes()

        for route in current_routes:
            for task_id in route.task_ids:
                task = Task(task_id)
                if task.status == "В процессе" or task.status == "Приостановлен":
                    return task

        return None