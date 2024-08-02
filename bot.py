
# pip install python-telegram-bot requests beautifulsoup4

import requests
from bs4 import BeautifulSoup
from telegram import Update, InputFile
from telegram.ext import Updater, CommandHandler, CallbackContext
from io import BytesIO

# Your bot token
TOKEN = '6813338822:AAGoU9J4O-BHs4IrWKN-9L2Q0K2f2_xAVJ4'

# URL and login credentials
LOGIN_URL = 'https://videometrics.asia/login'
DASHBOARD_URL = 'https://videometrics.asia/dashboard'
USERNAME = 'egor_kiev@meta.ua'
PASSWORD = 'Olen55RR!!'

# Function to log in and get the session
def get_session():
    session = requests.Session()
    login_payload = {
        'email': USERNAME,
        'password': PASSWORD
    }
    response = session.post(LOGIN_URL, data=login_payload)
    response.raise_for_status()  # Ensure we catch any login errors
    return session

# Function to parse data
def get_data(session):
    response = session.get(DASHBOARD_URL)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Example: Assuming stats are in a div with class 'stats'
    stats = soup.find('div', class_='stats').get_text()
    
    # Example: Assuming the image is in an img tag with class 'dashboard-image'
    img_tag = soup.find('img', class_='dashboard-image')
    img_url = img_tag['src'] if img_tag else None
    
    return stats, img_url

# Command handler for /start
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hello! I am a bot that shows statistics from VideoMetrics. Use the /stats command to get statistics.')

# Command handler for /stats
def stats(update: Update, context: CallbackContext) -> None:
    session = get_session()
    stats, img_url = get_data(session)
    
    # Sending text with statistics
    update.message.reply_text(f'Statistics: {stats}')
    
    # Sending the photo if found
    if img_url:
        response = requests.get(img_url)
        photo = BytesIO(response.content)
        photo.name = 'dashboard.jpg'
        update.message.reply_photo(photo)

def main():
    # Create the bot and the dispatcher
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    
    # Command handlers
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('stats', stats))
    
    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
