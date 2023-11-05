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
- `active_routes`
- `routes_history`
- `account_approved`

### Methods:
- `get_routes_history()` - gets all the finished routes. Returns array of Route objects
- `get_tasks_history()` - gets all the finished tasks. Returns array of Task objects
- `set_route(new_route)` - creates or updates route (and safes to db)

### Constructors:
- `Employee(email)` - gets Employee object from db
- `Employee(id)` - gets Employee object from db
- `Employee(name, email, password_hash)` - creates new Employee object (and safes to db)

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
- `status`
- `employee`

### Methods:
- `get_routes_history()`
- `get_current_route()`
- `set_route(Route)`

### Constructors:
- `Task(type, office)` - creates new task (and safes to db)
- `Task(id)` - gets task from db


## Manager

### Values:
- `id`
- `name`
- `email`
- `password_hash`

### Constructors:
- `Manager(email)` - gets Manager object from db
- `Manager(id)` - gets Manager object from db
- `Manager(name, email, password_hash)` - creates new Manager object (and safes to db)

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
- `employee`
- `tasks`
- `date`
- `status`
- `distance`

### Constructors:
- `Route(id)` - gets Route object from db
- `Route(employee, tasks, date = None, status = 'Не начат', distance=None)` - creates new Route object (and safes to db)

### Methods:

\


