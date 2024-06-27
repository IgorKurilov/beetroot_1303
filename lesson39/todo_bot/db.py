import aiosqlite

# Назва бази даних
DATABASE = 'todo.db'

# Функція для ініціалізації бази даних
async def init_db():
    async with aiosqlite.connect(DATABASE) as db:
        # Створення таблиці для зберігання справ, якщо вона ще не існує
        await db.execute('''
            CREATE TABLE IF NOT EXISTS todos (
                id INTEGER PRIMARY KEY,
                user_id INTEGER NOT NULL,
                description TEXT NOT NULL,
                priority INTEGER NOT NULL
            )
        ''')
        await db.commit()

# Функція для додавання нової справи
async def add_todo(user_id, description, priority):
    async with aiosqlite.connect(DATABASE) as db:
        await db.execute('''
            INSERT INTO todos (user_id, description, priority)
            VALUES (?, ?, ?)
        ''', (user_id, description, priority))
        await db.commit()

# Функція для отримання всіх справ користувача
async def get_todos(user_id):
    async with aiosqlite.connect(DATABASE) as db:
        async with db.execute('''
            SELECT id, description, priority FROM todos
            WHERE user_id = ?
            ORDER BY priority
        ''', (user_id,)) as cursor:
            return await cursor.fetchall()

# Функція для отримання справ користувача з певним пріоритетом
async def get_todos_by_priority(user_id, priority):
    async with aiosqlite.connect(DATABASE) as db:
        async with db.execute('''
            SELECT id, description, priority FROM todos
            WHERE user_id = ? AND priority = ?
            ORDER BY priority
        ''', (user_id, priority)) as cursor:
            return await cursor.fetchall()

# Функція для видалення справи за її ID
async def delete_todo(user_id, todo_id):
    async with aiosqlite.connect(DATABASE) as db:
        await db.execute('''
            DELETE FROM todos
            WHERE user_id = ? AND id = ?
        ''', (user_id, todo_id))
        await db.commit()
