import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from aiogram.utils import executor
from config import BOT_TOKEN
from db import init_db, add_todo, get_todos, get_todos_by_priority, delete_todo

# Налаштування логування для відслідковування подій
logging.basicConfig(level=logging.INFO)

# Створення об'єкту бота та диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# Обробник команди /start
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Welcome! Use /add to add a new todo, /list to list all todos, /filter to filter todos by priority, and /delete to delete a todo.")

# Обробник команди /add для додавання нової справи
@dp.message_handler(commands=['add'])
async def add_task(message: types.Message):
    # Отримання аргументів команди
    args = message.get_args().split('|')
    if len(args) != 2:
        await message.reply("Usage: /add <description>|<priority>")
        return

    # Розбиття аргументів на опис та пріоритет
    description, priority = args[0].strip(), args[1].strip()
    if not priority.isdigit() or not (1 <= int(priority) <= 10):
        await message.reply("Priority must be an integer between 1 and 10.")
        return

    # Додавання справи до бази даних
    await add_todo(message.from_user.id, description, int(priority))
    await message.reply(f"Added todo: {description} with priority {priority}")

# Обробник команди /list для перегляду списку всіх справ
@dp.message_handler(commands=['list'])
async def list_tasks(message: types.Message):
    # Отримання справ з бази даних
    todos = await get_todos(message.from_user.id)
    if not todos:
        await message.reply("No todos found.")
        return

    # Формування відповіді з усіма справами
    response = "Your todos:\n"
    for todo in todos:
        response += f"{todo[0]}: {todo[1]} (Priority: {todo[2]})\n"
    await message.reply(response, parse_mode=ParseMode.MARKDOWN)

# Обробник команди /filter для фільтрації справ за пріоритетом
@dp.message_handler(commands=['filter'])
async def filter_tasks(message: types.Message):
    # Отримання аргументу команди
    args = message.get_args().strip()
    if not args.isdigit() or not (1 <= int(args) <= 10):
        await message.reply("Priority must be an integer between 1 and 10.")
        return

    # Отримання справ з певним пріоритетом з бази даних
    priority = int(args)
    todos = await get_todos_by_priority(message.from_user.id, priority)
    if not todos:
        await message.reply(f"No todos found with priority {priority}.")
        return

    # Формування відповіді з відфільтрованими справами
    response = f"Your todos with priority {priority}:\n"
    for todo in todos:
        response += f"{todo[0]}: {todo[1]} (Priority: {todo[2]})\n"
    await message.reply(response, parse_mode=ParseMode.MARKDOWN)

# Обробник команди /delete для видалення справи
@dp.message_handler(commands=['delete'])
async def delete_task(message: types.Message):
    # Отримання аргументу команди
    args = message.get_args().strip()
    if not args.isdigit():
        await message.reply("Usage: /delete <todo_id>")
        return

    # Видалення справи з бази даних
    todo_id = int(args)
    await delete_todo(message.from_user.id, todo_id)
    await message.reply(f"Deleted todo with id {todo_id}")

if __name__ == "__main__":
    import asyncio
    # Ініціалізація бази даних та запуск бота
    asyncio.run(init_db())
    executor.start_polling(dp, skip_updates=True)
