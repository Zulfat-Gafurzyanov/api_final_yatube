# Проект API для Yatube
Yatube — это платформа для блогов, предполагает возможность зарегистрироваться, создать, отредактировать или удалить собственный пост, прокомментировать пост другого автора и подписаться на него.

## Технологии

- Python
- Django REST Framework
- Simple JWT
- OpenAPI (реализован на Redoc)
  
Документация для API доступна по адресу: http://127.0.0.1:8000/redoc/

## Установка и запуск

### Шаги установки

Клонировать репозиторий и перейти в него в командной строке:

```
https://github.com/Zulfat-Gafurzyanov/api_final_yatube.git
```

```
cd yatube_api
```

Cоздать и активировать виртуальное окружение для Windows:

```
python -m venv venv
```

```
source venv/Scripts/activate
```

Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```
