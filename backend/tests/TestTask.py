from random import random

from backend.app_classes.Task import Task

class TestTask:
    def test_incorrect_element(self):
        task = Task(100000)
        assert task

    def test_create_and_init(self):
        Task.create(type=1, office_id=1)

        task = Task(task_id=1)
        assert task.id == 1

    def test_create_one(self):
        Task.create(type=1, office_id=1)
        task = Task(1)

        assert task.status == "Не назначена"

    def test_get_all(self):
        tasks = Task.get_all()
        assert tasks[1].id == 2

    def test_create(self):
        tasks = Task.get_all()
        len_before = len(tasks)

        Task.create(type=1, office_id=5)

        tasks = Task.get_all()
        assert len_before + 1 == len(tasks)

        len_before = len(tasks)

        # incorrect input
        Task.create(office_id=1000, type=3)
        Task.create(office_id=10, type=3000)

        tasks = Task.get_all()
        assert len_before == len(tasks)

    def test_saving(self):
        tasks = Task.get_all()
        task = tasks[-1]
        task.type=2
        task.safe()

        task.type = 100000
        task.safe()

        tasks = task.get_all()
        assert tasks[-1].type == 2
