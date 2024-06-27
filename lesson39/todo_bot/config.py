import os
from dotenv import load_dotenv

# Завантаження змінних середовища з .env файлу
load_dotenv()

# Отримання токену бота з середовища
BOT_TOKEN = os.getenv("BOT_TOKEN")
