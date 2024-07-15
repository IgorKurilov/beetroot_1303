 простой веб-сервис для управления списком дел (To-Do List) с помощью Django
pip install django

django-admin startproject todo_project
cd todo_project

python manage.py startapp todo

Добавьте приложение todo в список установленных приложений (INSTALLED_APPS) в файле todo_project/settings.py:
INSTALLED_APPS = [
    ...
    'todo',
]

Создайте и примените миграции для создания таблицы задач в базе данных:
python manage.py makemigrations
python manage.py migrate

Добавьте маршруты приложения todo в основной файл urls.py вашего проекта:
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todo.urls')),
]

python manage.py runserver

Откройте браузер и перейдите по адресу http://127.0.0.1:8000/ чтобы увидеть ваш To-Do List веб-сервис. 
Вы должны увидеть список задач с возможностью добавления новых, редактирования, просмотра деталей и удаления существующих задач.
