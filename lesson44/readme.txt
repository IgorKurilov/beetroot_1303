Створення проекту та додатку
django-admin startproject notes_project
cd notes_project
django-admin startapp notes

Додати додаток notes до INSTALLED_APPS в notes_project/settings.py:
INSTALLED_APPS = [
    ...
    'notes',
]

Винесення CSS у окремий файл
Створення папки static/notes в папці додатка notes.
Створення файлу styles.css в notes/static/notes/styles.css

Додати django.contrib.staticfiles до INSTALLED_APPS

http://127.0.0.1:8000/ у вашому браузері, щоб побачити головну сторінку з нотатками та застосований CSS.
