import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
OPENWEATHERMAP_TOKEN = os.getenv('OPENWEATHERMAP_TOKEN')
CITY = 'Новосибирск'
