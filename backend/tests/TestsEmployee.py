import random

from backend.app_classes.Employee import Employee

class TestEmployee:
    def test_one(self):
        employee = Employee(employee_id=1)
        assert employee.id == 1

    def test_create(self):
        email = "test1@test.py" + str(random.randint(1,1000000))
        Employee.create(name=email, password_hash=967,
                        email=email)

        employee = Employee(email=email)
        assert employee.name==email

    def test_get_all(self):
        employees = Employee.get_all()
        assert employees[4].id == 5

    def test_create_unique(self):
        employees = Employee.get_all()
        len_before = len(employees)

        email = "test1@test.py" + str(random.randint(1, 1000000))

        Employee.create(name="Артём", password_hash=967,
                        email=email)

        employees = Employee.get_all()
        assert len_before + 1 == len(employees)

        len_before = len(employees)

        Employee.create(name="Артём", password_hash=967,
                        email=email)

        employees = Employee.get_all()
        assert len_before == len(employees)

    def test_saving(self):
        employees = Employee.get_all()
        if True:
            employee = Employee(employee_id=4)
            employee.password_hash = '123'
            employee.safe()

        employees = Employee.get_all()
        assert employees[3].password_hash == '123'

