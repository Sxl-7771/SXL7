import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import executor

api = ''

logging.basicConfig(level=logging.INFO)

bot = Bot(token=api)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    print('Привет! Я бот помогающий твоему здоровью.')
    await message.answer('Привет! Я бот помогающий твоему здоровью.')


@dp.message_handler(lambda message: message.text and message.text != '/start')
async def all_messages(message: types.Message):
    print('Введите команду /start, чтобы начать общение.')
    await message.answer('Введите команду /start, чтобы начать общение.')

if __name__ == '__main__':
    print("Бот запущен. Ожидание сообщений...")
    executor.start_polling(dp, skip_updates=True)