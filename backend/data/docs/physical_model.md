# Физическая модель

---

Таблица `manager`:

| Название        | Описание      | Тип данных | Ограничение   |
|-----------------|---------------|------------|---------------|
| `manager_id`    | Идентификатор | `INTEGER`  | `PRIMARY KEY` |
| `name`          | ФИО           | `TEXT`     | `NOT NULL`    |
| `password_hash` | Хэш пароля    | `TEXT`     | `NOT NULL`    |
| `email`         | Почта         | `TEXT`     | `NOT NULL`    |

Таблица `employee`:

| Название          | Описание      | Тип данных | Ограничение   |
|-------------------|---------------|------------|---------------|
| `employee_id`     | Идентификатор | `INTEGER`  | `PRIMARY KEY` |
| `name`            | ФИО           | `TEXT`     | `NOT NULL`    |
| `default_address` | Адрес локации | `TEXT`     | `NOT NULL`    |
| `grade`           | Грейд         | `TEXT`     | `NOT NULL`    |
| `password_hash`   | Хэш пароля    | `TEXT`     | `NOT NULL`    |
| `email`           | Почта         | `TEXT`     | `NOT NULL`    |

Таблица `route`:

| Название      | Описание                 | Тип данных | Ограничение    |
|---------------|--------------------------|------------|----------------|
| `route_id`    | Идентификатор            | `INTEGER`  | `PRIMARY KEY`  |
| `employee_id` | Идентификатор сотрудника | `TEXT`     | `FOREIGN KEY`  |
| `date`        | Дата                     | `TEXT`     | `NOT NULL`     |
| `distance`    | Расстояние               | `REAL`     | `NOT NULL`     |
| `status`      | Статус маршрута          | `REAL`     | `NOT NULL`     |

Таблица `route_X_task`:

| Название         | Описание             | Тип данных | Ограничение    |
|------------------|----------------------|------------|----------------|
| `route_id`       | Идентификатор        | `INTEGER`  | `FOREIGN KEY`  |
| `task_id`        | Идентификатор задачи | `TEXT`     | `FOREIGN KEY`  |
| `order_in_route` | Порядок в маршруте   | `TEXT`     | `NOT NULL`     |

Таблица `task`:

| Название       | Описание                  | Тип данных | Ограничение    |
|----------------|---------------------------|------------|----------------|
| `task_id`      | Идентификатор             | `INTEGER`  | `PRIMERY KEY`  |
| `task_info_id` | Идентификатор типа задачи | `INTEGER`  | `FOREIGN KEY`  |
| `office_id`    | Идентификатор типа задачи | `INTEGER`  | `FOREIGN KEY`  |
| `task_status`  | Статус задачи             | `TEXT`     | `NOT NULL`     |
| `comment`      | Комментарий к задаче      | `TEXT`     | `NOT NULL`     |

Таблица `office`:

| Название                | Описание                                 | Тип данных | Ограничение   |
|-------------------------|------------------------------------------|------------|---------------|
| `office_id`             | Идентификатор                            | `INTEGER`  | `PRIMERY KEY` |
| `address`               | Адрес                                    | `TEXT`     | `NOT NULL`    |
| `when_opened`           | Когда подключена точка                   | `TEXT`     | `NOT NULL`    |
| `materials_delivered`   | Карты и материалы доставлены             | `TEXT`     | `NOT NULL`    |
| `days_since_last_card`  | Кол-во дней после выдачи последней карты | `TEXT`     | `NOT NULL`    |
| `accepted_applications` | Кол-во одобренных заявок                 | `INTEGER`  | `NOT NULL`    |
| `given cards`           | Кол-во выданных карт                     | `INTEGER`  | `NOT NULL`    |
| `coordinates`           | Координаты                               | `TEXT`     | `NOT NULL`    |

Таблица `task_info`:

| Название         | Описание                     | Тип данных | Ограничение    |
|------------------|------------------------------|------------|----------------|
| `task_info_id`   | Идентификатор                | `INTEGER`  | `PRIMERY KEY`  |
| `title`          | Название задачи              | `TEXT`     | `NOT NULL`     |
| `priority`       | Приоритет                    | `TEXT`     | `NOT NULL`     |
| `time_required`  | Время выполнения (в часах)   | `REAL`     | `NOT NULL`     |
| `grade_required` | Требуемый уровень сотрудника | `TEXT`     | `NOT NULL`     |
| `condition_1 `   | Условие 1                    | `TEXT`     | `NOT NULL`     |
| `condition_2 `   | Условие 2                    | `TEXT`     | `NOT NULL`     |




