from backend.config import db_engine, db_meta
import sqlalchemy as db
from .Route import Route

employee_table = db_meta.tables['employee']
route_table = db_meta.tables['route']

class Employee:

    @staticmethod
    def create(name, email, password_hash):
        conn = db_engine.connect()
        query = db.insert(employee_table).values(email=email, name=name,
                                                     password_hash=password_hash)
        conn.execute(query)
        conn.close()

    @staticmethod
    def get_all():
        conn = db_engine.connect()

        query = db.select(employee_table.c["employee_id"])
        output = conn.execute(query).fetchall()

        employees = []
        for employee_id in output:
            employees.append(Employee(employee_id=employee_id[0]))

        conn.close()
        return employees

    def __init__(self, email=None, employee_id=None):
        conn = db_engine.connect()

        # collect info from employee table
        query = ''
        if employee_id:
            # find by id
            query = employee_table.select().where(
                employee_table.columns.employee_id == employee_id)

        elif email:
            # find by email
            query = employee_table.select().where(
                employee_table.columns.email == email)

        output = conn.execute(query).fetchall()
        conn.close()
        if len(output) == 0:
            # no such employee
            return

        (
            self.id,
            self.name,
            self.default_address,
            self.grade,
            self.password_hash,
            self.email,
            self.account_approved
        ) = output[0]


    def __del__(self):
        # safe to db before quiting
        conn = db_engine.connect()

        query = db.update(employee_table).where(
            employee_table.c.employee_id == self.id
        ).values(
            name=self.name,
            default_address=self.default_address,
            grade=self.grade,
            password_hash=self.password_hash,
            email=self.email,
            account_approved=self.account_approved
        )

        conn.execute(query)
        conn.close()

    def get_routes_history(self):
        conn = db_engine.connect()
        query = db.select(route_table.c["route_id"]).where(
            route_table.columns.employee_id == self.id
        ).order_by(
            route_table.columns.date
        )

        output = conn.execute(query).fetchall()

        routes_history = []
        for route_id in output:
            route = Route(route_id)
            routes_history.append(route)

        conn.close()
        return routes_history


    def get_tasks_history(self):
        routes_history = self.get_routes_history()

        tasks_history = []
        for route in routes_history:
            for task in route.tasks:
                tasks_history.append(task)

        return tasks_history


    def get_current_routes(self):
        conn = db_engine.connect()
        query = db.select(route_table.c["route_id"]).where(
            route_table.columns.employee_id == self.id
            and route_table.columns.status != "Не закончен"
            and route_table.columns.status != "Закончен"
        ).order_by(
            route_table.columns.date
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
            for task in route.tasks:
                if (task.status == "В процессе"
                        or task.status == "Приостановлен"):
                    return task

        return None