import sqlite3
import functools

base_path = ""
scripts_path = base_path + "scripts/"

def run_sql(original_function=None, multiple_queries=False):

    def _decorate(function):

        @functools.wraps(function)
        def wrapped_function(*args, **kwargs):
            connection = sqlite3.connect(base_path + "app.db")
            cursor = connection.cursor()

            query = function(*args, **kwargs)

            if multiple_queries:
                cursor.executescript(query)
            else:
                cursor.execute(query)

            answer = cursor.fetchall()

            connection.commit()
            connection.close()

            return answer

        return wrapped_function

    if callable(original_function):
        return _decorate(original_function)

    return _decorate


@run_sql(multiple_queries=True)
def execute_sql_file(filename):
    with open(scripts_path + filename, 'r') as file:
        query = file.read()

    return query