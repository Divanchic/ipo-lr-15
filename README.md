### Задание 1

Создать простейший веб‑сервис на Flask.

Структура проекта:

```
task_1/
    app/
        __init__.py
        [routes.py]
    [main.py]
    [README.md]
```

В [`routes.py`] реализовать маршруты:

Вариант 3
POST /json — принимает JSON {name, age} и выводит фразу.
GET /multiply/<a>/<b> — возвращает произведение чисел.
