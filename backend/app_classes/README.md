# Classes

----
## Employee

### Values:
- `id`
- `name`
- `default_address`
- `grade`
- `email`
- `password_hash`
- `account_approved`

### Constructors:
- `Employee(email)` - gets Employee object from db
- `Employee(employee_id)` - gets Employee object from db

### Methods:
- @static `get_all()`- returns list of Employee objects
- @static `safe()`- safes to db
- @static `create(name, email, password_hash)` - creates new Employee object and safes to db
- `get_routes_history()` - gets all the finished routes. Returns list of Route objects
- `get_tasks_history()` - gets all the finished tasks. Returns list of Task objects
- `get_current_task()` - Returns Task object
- `get_active_routes()` - Returns list of Route objects



## Task
### Values:
- `id`
- `type`
- `priority`
- `office`
- `title`
- `comment`
- `grade_required`
- `time_required`
- `status` - "Не назначен" / "Назначен" / "Ожидает" / "Начат" / "Выполнен" / "Приостановлен" / "Не выполнен"
- `employee_id`

### Constructors:
- `Task(id)` - gets task from db

### Methods:
- @static `safe()`- safes to db
- @static `get_all()`- returns list of Task objects
- @static `get_active()`- returns list of Task objects
- @static `create(type, office, date=None, status="Не назначена")` - creates new task and safes to db




## Manager

### Values:
- `id`
- `name`
- `email`
- `password_hash`

### Constructors:
- `Manager(email)` - gets Manager object from db
- `Manager(id)` - gets Manager object from db

### Methods:
- @static `safe()`- safes to db
- @static `get_all()`- returns list of Manager objects
- @static `create(name, email, password_hash)` - creates new Manager object (and safes to db)

## Office

### Values:
- `id`
- `address`
- `when_opened`
- `materials_delivered`
- `days_since_last_card`
- `accepted_applications`
- `given_cards`
- `coordinates`
- `tasks`

### Constructors:
- `Office(office_id)` - gets Office object from db

### Methods:
- @static `safe()`- safes to db
- @static `get_all()`- returns list of Office objects
- @static `create(address, when_opened = 'вчера', materials_delivered = 'нет', 
days_since_last_card = 0, accepted_applications = 0, given_cards = 0)` - creates new Office object (and safes to db)

## Route

### Values:
- `id`
- `employee_id`
- `tasks` - list of Task objects
- `date`
- `status` - "Не начат" / "В процессе" / "Закончен" / "Приостановлен" / "Не закончен"
- `distance`

### Constructors:
- `Route(route_id)` - gets Route object from db
- `Route(employee_id, date)` - gets Route object from db

### Methods:
- @static `safe()`- safes to db
- @static `get_all()`- returns list of Route objects
- @static `get_active()`- returns list of Task objects
- @static `create(employee_id, tasks, date, status = 'Не начат', distance=None)` - creates new Route object (and safes to db)


