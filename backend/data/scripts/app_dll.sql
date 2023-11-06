CREATE TABLE IF NOT EXISTS manager (
  manager_id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  password_hash TEXT NOT NULL,
  email TEXT UNIQUE,
  UNIQUE (email COLLATE NOCASE)
);

CREATE TABLE IF NOT EXISTS employee (
  employee_id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  default_address TEXT,
  grade TEXT,
  password_hash TEXT,
  email TEXT UNIQUE,
  account_approved INTEGER,
  UNIQUE (email COLLATE NOCASE)
);

CREATE TABLE IF NOT EXISTS route (
  route_id INTEGER PRIMARY KEY,
  employee_id INTEGER NOT NULL,
  date TEXT NOT NULL,
  distance REAL NOT NULL,
  status TEXT NOT NULL,
  FOREIGN KEY (employee_id) REFERENCES employee(employee_id),
  CONSTRAINT unq UNIQUE (date, employee_id)
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

CREATE TABLE IF NOT EXISTS task_type (
  type INTEGER PRIMARY KEY,
  title TEXT NOT NULL,
  priority TEXT NOT NULL,
  time_required REAL NOT NULL,
  grade_required TEXT NOT NULL,
  condition_1 TEXT NOT NULL,
  condition_2 TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS task (
  task_id INTEGER PRIMARY KEY,
  office_id INTEGER NOT NULL,
  type INTEGER NOT NULL,
  status TEXT NOT NULL,
  comment TEXT,
  date TEXT NOT NULL,
  FOREIGN KEY (type) REFERENCES task_type(type),
  FOREIGN KEY (office_id) REFERENCES office(office_id)
);

CREATE TABLE IF NOT EXISTS route_X_task (
  task_id INTEGER PRIMARY KEY,
  route_id INTEGER NOT NULL,
  order_in_route INTEGER NOT NULL,
  FOREIGN KEY (route_id) REFERENCES route(route_id),
  FOREIGN KEY (task_id) REFERENCES task(task_id)
);


