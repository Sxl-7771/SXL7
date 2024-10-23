import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor
from crud_functions import initiate_db, get_all_products

api = ''

logging.basicConfig(level=logging.INFO)

bot = Bot(token=api)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

initiate_db()


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


def main_menu_keyboard():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton('Рассчитать'), KeyboardButton('Информация'), KeyboardButton('Купить'))
    return markup


def inline_buy_menu():
    inline_markup = InlineKeyboardMarkup(row_width=2)

    products = get_all_products()
    for product in products:
        product_id, title, description, price = product
        inline_markup.add(InlineKeyboardButton(title, callback_data='product_buying'))

    return inline_markup


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer("Привет! Я бот, помогающий твоему здоровью.", reply_markup=main_menu_keyboard())


@dp.message_handler(lambda message: message.text.lower() == 'рассчитать')
async def main_menu(message: types.Message):
    inline_markup = InlineKeyboardMarkup()
    inline_markup.add(InlineKeyboardButton('Рассчитать норму калорий', callback_data='calories'))
    inline_markup.add(InlineKeyboardButton('Формулы расчёта', callback_data='formulas'))
    await message.answer("Выберите опцию:", reply_markup=inline_markup)


@dp.callback_query_handler(lambda call: call.data == 'formulas')
async def get_formulas(call: types.CallbackQuery):
    await call.answer()
    formula_message = (
        "Формула Миффлина-Сан Жеора:\n"
        "Для мужчин: BMR = 10 * вес(кг) + 6.25 * рост(см) - 5 * возраст(лет) + 5\n"
        "Для женщин: BMR = 10 * вес(кг) + 6.25 * рост(см) - 5 * возраст(лет) - 161"
    )
    await call.message.answer(formula_message)


@dp.callback_query_handler(lambda call: call.data == 'calories')
async def set_age(call: types.CallbackQuery):
    await UserState.age.set()
    await call.answer()
    await call.message.answer("Введите свой возраст:", reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler(state=UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)
    await UserState.growth.set()
    await message.answer("Введите свой рост:", reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler(state=UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    await state.update_data(growth=message.text)
    await UserState.weight.set()
    await message.answer("Введите свой вес:", reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler(state=UserState.weight)
async def send_calories(message: types.Message, state: FSMContext):
    await state.update_data(weight=message.text)
    data = await state.get_data()

    age = int(data.get('age', 0))
    growth = int(data.get('growth', 0))
    weight = int(data.get('weight', 0))

    calories = 10 * weight + 6.25 * growth - 5 * age + 5
    await message.answer(f"Ваша норма калорий: {calories} ккал.")
    await state.finish()


@dp.message_handler(lambda message: message.text.lower() == 'купить')
async def get_buying_list(message: types.Message):
    products = get_all_products()

    if not products:
        await message.answer("Нет доступных продуктов.")
        return

    for product in products:
        product_id, title, description, price = product
        with open(f'Photo/{product_id}.jpg', "rb") as img:
            await message.answer_photo(img, f"Название: {title} | Описание: {description} | Цена: {price} руб.")

    await message.answer("Выберите продукт для покупки:", reply_markup=inline_buy_menu())


@dp.callback_query_handler(lambda call: call.data == 'product_buying')
async def send_confirm_message(call: types.CallbackQuery):
    await call.answer()
    await call.message.answer("Вы успешно приобрели продукт!")


@dp.message_handler()
async def fallback(message: types.Message):
    await message.answer('Введите команду /start, чтобы начать общение.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
