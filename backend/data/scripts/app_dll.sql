CREATE TABLE IF NOT EXISTS manager (
  manager_id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  password_hash TEXT NOT NULL,
  email TEXT UNIQUE
);

CREATE TABLE IF NOT EXISTS employee (
  employee_id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  default_address TEXT NOT NULL,
  grade TEXT NOT NULL,
  password_hash TEXT,
  email TEXT UNIQUE
);

CREATE TABLE IF NOT EXISTS route (
  route_id INTEGER PRIMARY KEY,
  employee_id INTEGER,
  date TEXT NOT NULL,
  distance REAL NOT NULL,
  status TEXT NOT NULL,
  FOREIGN KEY (employee_id) REFERENCES employee(employee_id)
);

CREATE TABLE IF NOT EXISTS route_X_task (
  route_id INTEGER,
  task_id INTEGER,
  order_in_route TEXT NOT NULL,
  FOREIGN KEY (route_id) REFERENCES route(route_id),
  FOREIGN KEY (task_id) REFERENCES task(task_id)
);

CREATE TABLE IF NOT EXISTS task (
  task_id INTEGER PRIMARY KEY,
  task_info_id INTEGER,
  office_id INTEGER,
  task_status TEXT NOT NULL,
  comment TEXT NOT NULL,
  FOREIGN KEY (task_info_id) REFERENCES task_info(task_info_id),
  FOREIGN KEY (office_id) REFERENCES office(office_id)
);

CREATE TABLE IF NOT EXISTS office (
  office_id INTEGER PRIMARY KEY,
  address TEXT NOT NULL,
  when_opened TEXT NOT NULL,
  materials_delivered TEXT NOT NULL,
  days_since_last_card TEXT NOT NULL,
  accepted_applications INTEGER NOT NULL,
  given_cards INTEGER NOT NULL,
  coordinates TEXT
);

CREATE TABLE IF NOT EXISTS task_info (
  task_info_id INTEGER PRIMARY KEY,
  type INTEGER NOT NULL,
  title TEXT NOT NULL,
  priority TEXT NOT NULL,
  time_required REAL NOT NULL,
  grade_required TEXT NOT NULL,
  condition_1 TEXT NOT NULL,
  condition_2 TEXT NOT NULL
); 
