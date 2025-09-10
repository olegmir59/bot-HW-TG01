import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from weather_api import WeatherAPI
from config import TELEGRAM_TOKEN

# Инициализация бота и диспетчера
bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher()

weather_api = WeatherAPI()

# Обработчики команд
@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("Привет! Я бот прогноза погоды. "
                        "Напиши /weather, чтобы узнать погоду в Новосибирске.")


@dp.message(Command('help'))
async def help(message: Message):
    await message.answer("Доступные команды:\n"
                        "/start - начать работу с ботом\n"
                        "/help - показать это сообщение\n"
                        "/weather - узнать погоду")

@dp.message(Command('weather'))
async def weather(message: types.Message):
    weather_info = weather_api.get_weather()
    await message.answer(weather_info)



# Запуск бота
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

