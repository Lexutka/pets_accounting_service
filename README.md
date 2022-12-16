Pets Accounting
===========
API-сервис, позволяющий добавлять, просматривать и удалять фотографии и информацию о питомцах, а также выгружать данные через cli-интерфейс.

Технологии:
===========
[![dependencies](https://img.shields.io/static/v1?style=plastic&logo=python&label=python&message=v3.10&color=white)](https://www.python.org/%0A)
[![dependencies](https://img.shields.io/badge/postgesql-1.12-green)](https://www.python.org/%0A)
[![dependencies](https://img.shields.io/badge/django-4.1.4-orange)](https://www.python.org/%0A)

Локальный запуск:
===========

1. Установка зависимостей:
```commandline
$ poetry shell
$ poetry install
```
2. В корневой папке проекта (на уровне с manage.py) создаем и настраиваем файл .env.dev:
```python
DEBUG=0  # 1 для включения дебаг-режима
SECRET_KEY=<django_secret_key>
ALLOWED_HOSTS=localhost 127.0.0.1
API_KEY=token  # Authorization-токен для доступа к API
POSTGRES_ENGINE=django.db.backends.postgresql
POSTGRES_DB=db_name
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_HOST=db_name # при запуске через docker-compose установите значение 'db'
POSTGRES_PORT=5432
```
3. Применяем миграции к БД и запускаем сервер:
```commandline
$ python manage.py migrate
$ python manage.py runserver  
```

Запуск через Docker-Compose:
===========

1. Выполняем пункт 2 предыдущего раздела
2. Собираем и запусксем контейнеры:
```commandline
$ docker-compose up -d --build  
```


Будущие обновления
===========

1. Поддержка полноценого CRUD'а в API
2. Авторизация пользователей
