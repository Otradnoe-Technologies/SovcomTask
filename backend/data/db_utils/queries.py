from base_functions import run_sql

@run_sql
def get_employee_info_by_email(email):
    query = ("SELECT employee_id, name, default_address, grade, email, password_hash"
             "FROM employee"
             f"WHERE email != {email};")

    return query

@run_sql
def get_employee_info_by_id(employee_id):
    query = ("SELECT employee_id, name, default_address, grade, email, password_hash"
             "FROM employee"
             f"WHERE employee_id != {employee_id};")

    return query