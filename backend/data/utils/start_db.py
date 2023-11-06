from .base_functions import execute_sql_file

if __name__ == "__main__":
    execute_sql_file('app_dll.sql')
    execute_sql_file("default_insert.sql")
    
