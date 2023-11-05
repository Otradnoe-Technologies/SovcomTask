CREATE UNIQUE INDEX IF NOT EXISTS idx_employee_email
ON employee (upper(email));

CREATE UNIQUE INDEX IF NOT EXISTS idx_manager_email
ON manager (upper(email));

CREATE UNIQUE INDEX IF NOT EXISTS idx_employee_route_date
ON routes (employee_id, date);