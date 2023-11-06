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
- `active_routes_ids`
- `account_approved`

### Constructors:
- `Employee(email)` - gets Employee object from db
- `Employee(id)` - gets Employee object from db

### Methods:
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

- @static `create(type, office)` - creates new task and safes to db




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
- @static `create(name, email, password_hash)` - creates new Manager object (and safes to db)

## Office

### Values:
- `id`
- `address`
- `when_opened`
- `materials_delivered`
- `days_since_last_card`
- `accepted_applications`
- `given cards`
- `coordinates`
- `tasks`

### Constructors:
- `Office(id)` - gets Office object from db
- `Office(address, when_opened = 'вчера', materials_delivered = 'нет', 
days_since_last_card = 0, accepted_applications = 0, given_cards = 0)` - creates new Office object (and safes to db)

### Methods:
- `check_tasks_conditions()` - if conditions are met, adds task to db

## Route

### Values:
- `id`
- `employee_id`
- `task_ids`
- `date`
- `status` - "Не начат" / "В процессе" / "Закончен" / "Приостановлен" / "Не закончен"
- `distance`

### Constructors:
- `Route(id)` - gets Route object from db
- `Route(employee_id, date)` - gets Route object from db

### Methods:
@static `create(employee_id, tasks, date, status = 'Не начат', distance=None)` - creates new Route object (and safes to db)


