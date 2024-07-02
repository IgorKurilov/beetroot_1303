Перехід на PostgreSQL
1: Встановіть PostgreSQL та бібліотеку psycopg2
pip install psycopg2-binary

2: Оновіть налаштування бази даних settings.py

3: Створіть базу даних PostgreSQL
psql
# Увійдіть в інтерфейс PostgreSQL

CREATE DATABASE your_db_name;
CREATE USER your_db_user WITH PASSWORD 'your_db_password';
ALTER ROLE your_db_user SET client_encoding TO 'utf8';
ALTER ROLE your_db_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE your_db_user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE your_db_name TO your_db_user;

4: Запустіть міграції для PostgreSQL
python manage.py migrate
