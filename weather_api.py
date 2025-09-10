import requests
from config import OPENWEATHERMAP_TOKEN, CITY


class WeatherAPI:
    BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

    def get_weather(self):
        params = {
            'q': CITY,
            'appid': OPENWEATHERMAP_TOKEN,
            'units': 'metric',  # градусы Цельсия
            'lang': 'ru'
        }
        response = requests.get(self.BASE_URL, params=params)
        data = response.json()

        if response.status_code == 200:
            temp = data['main']['temp']
            description = data['weather'][0]['description']
            return f"Погода в городе {CITY}:\nТемпература: {temp}°C\nОписание: {description}"
        else:
            return "Не удалось получить данные о погоде"
