import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.fsm.storage.memory import MemoryStorage

from lab8.config import BOT_TOKEN

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(storage=MemoryStorage())

start_keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Вход в музей")]
], resize_keyboard=True)

hall1_keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Перейти в зал 2")],
    [KeyboardButton(text="Перейти в зал 3")],
    [KeyboardButton(text="Выход")]
], resize_keyboard=True)

hall2_keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Перейти в зал 1")],
    [KeyboardButton(text="Перейти в зал 4")]
], resize_keyboard=True)

hall3_keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Перейти в зал 1")]
], resize_keyboard=True)

hall4_keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Перейти в зал 2")]
], resize_keyboard=True)


@dp.message(Command(commands=["start"]))
async def start_command(message: Message):
    await message.answer("Добро пожаловать! Пожалуйста, сдайте верхнюю одежду в гардероб!", reply_markup=start_keyboard)


@dp.message(lambda message: message.text == "Вход в музей")
async def enter_museum(message: Message):
    await message.answer("Вы вошли в музей. В данном зале представлено: картина №1. \nВы можете перейти в другие залы.",
                         reply_markup=hall1_keyboard)


# Зал 1
@dp.message(lambda message: message.text == "Перейти в зал 2")
async def to_hall2_from_hall1(message: Message):
    await message.answer("Вы перешли в зал 2. В данном зале представлено: скульптура №1.", reply_markup=hall2_keyboard)


@dp.message(lambda message: message.text == "Перейти в зал 3")
async def to_hall3_from_hall1(message: Message):
    await message.answer("Вы перешли в зал 3. В данном зале представлено: древний артефакт №1.",
                         reply_markup=hall3_keyboard)


@dp.message(lambda message: message.text == "Выход")
async def exit_from_hall1(message: Message):
    await message.answer("Спасибо за посещение музея! Не забудьте забрать верхнюю одежду в гардеробе.",
                         reply_markup=start_keyboard)


# Зал 2
@dp.message(lambda message: message.text == "Перейти в зал 1")
async def to_hall1_from_hall2(message: Message):
    await message.answer("Вы вернулись в зал 1.", reply_markup=hall1_keyboard)


@dp.message(lambda message: message.text == "Перейти в зал 4")
async def to_hall4_from_hall2(message: Message):
    await message.answer("Вы перешли в зал 4. В данном зале представлено: современное искусство №1.",
                         reply_markup=hall4_keyboard)


# Зал 3
@dp.message(lambda message: message.text == "Перейти в зал 1")
async def to_hall1_from_hall3(message: Message):
    await message.answer("Вы вернулись в зал 1.", reply_markup=hall1_keyboard)


# Зал 4
@dp.message(lambda message: message.text == "Перейти в зал 2")
async def to_hall2_from_hall4(message: Message):
    await message.answer("Вы вернулись в зал 2.", reply_markup=hall2_keyboard)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
