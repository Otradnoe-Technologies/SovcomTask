from django.db import models

class Manager(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    account_approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.full_name}"


class Employee(models.Model):
    full_name = models.CharField(max_length=200)
    default_address = models.CharField(max_length=200)
    grade = models.CharField(max_length=200)
    email = models.CharField(max_length=200, blank=False)
    account_approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.full_name}"


class Route(models.Model):
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateTimeField()
    distance = models.FloatField(default=0)
    status = models.CharField(max_length=200, default="Не начат")


class Office(models.Model):
    address = models.CharField(max_length=200)
    when_opened = models.DateTimeField()
    materials_delivered = models.BooleanField()
    last_card_date = models.DateTimeField()
    accepted_applications = models.IntegerField()
    given_cards = models.IntegerField()
    coordinate_x = models.FloatField()
    coordinate_y = models.FloatField()


class TaskType(models.Model):
    type = models.IntegerField()
    priority = models.IntegerField()
    title = models.CharField(max_length=200)
    grade_required = models.IntegerField()
    time_required = models.FloatField()
    condition_1 = models.CharField(max_length=200)
    condition_2 = models.CharField(max_length=200)


class Task(models.Model):
    route = models.ForeignKey(Route, null=True, on_delete=models.CASCADE)
    type = models.ForeignKey(TaskType, on_delete=models.CASCADE)
    office = models.ForeignKey(Office, on_delete=models.CASCADE)
    status = models.CharField(max_length=200, default="Не назначена")
    comment = models.CharField(max_length=200, default="")


