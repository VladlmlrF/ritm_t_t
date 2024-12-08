## Установка проекта:

Клонировать проект из Github командой:
```commandline
https://github.com/VladlmlrF/ritm_t_t.git
```

## Запуск проекта:

1. Создать файл `.env` в котором должны быть следующие записи:
```dotenv
DB_HOST=db
DB_PORT=27017
DB_NAME=formsdb
MONGO_INITDB_ROOT_USERNAME=root
MONGO_INITDB_ROOT_PASSWORD=example
```

2. Непосредственно запустить проект в контейнере командой:
```commandline
docker compose up --build
```

3. Запустить скрипт, который совершает тестовые запросы командой:
```commandline
python -m test_requests.py
```
