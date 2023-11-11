from tasks.models import *

def check_tasks():
    offices = Office.objects.all()
    print(offices[0])

check_tasks()
