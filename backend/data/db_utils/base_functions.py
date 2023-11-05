import sqlite3

base_path = ""
scripts_path = base_path + "scripts/"

def run_sql(func):
    def wrapper():
        connection = sqlite3.connect(base_path + "app.db")
        cursor = connection.cursor()

        query = func()

        answer = cursor.executescript(query)
        connection.commit()
        connection.close()

        return answer


@run_sql
def execute_sql_file(filename):
    with open(scripts_path + filename, 'r') as file:
        query = file.read()

    return query