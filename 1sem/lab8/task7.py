import asyncio
from aiogram import Bot, Dispatcher, Router, types
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import Command
import random

from lab8.config import BOT_TOKEN

bot = Bot(token=BOT_TOKEN)
router = Router()
dp = Dispatcher()

dp.include_router(router)

sleep_event = asyncio.Event()
user_tasks = {}

start_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="/dice"), KeyboardButton(text="/timer")]
    ],
    resize_keyboard=True
)

dice_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Кинуть один шестигранный кубик"),
            KeyboardButton(text="Кинуть 2 шестигранных кубика одновременно")
        ],
        [
            KeyboardButton(text="Кинуть 20-гранный кубик"),
            KeyboardButton(text="Вернуться назад")
        ]
    ],
    resize_keyboard=True
)

timer_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="30 секунд"),
            KeyboardButton(text="1 минута")
        ],
        [
            KeyboardButton(text="5 минут"),
            KeyboardButton(text="Вернуться назад"),
            KeyboardButton(text="/cancel")
        ]
    ],
    resize_keyboard=True
)

close_keyboard = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="/close")]], resize_keyboard=True
)


@router.message(Command(commands=['start']))
async def start_command(message: Message):
    await message.answer("Выберите действие:", reply_markup=start_keyboard)


@router.message(lambda msg: msg.text == "/dice")
async def dice_command(message: Message):
    await message.answer("Выберите кубик для броска:", reply_markup=dice_keyboard)


@router.message(lambda msg: msg.text == "Кинуть один шестигранный кубик")
async def roll_one_dice(message: Message):
    result = random.randint(1, 6)
    await message.answer(f"Выпало число: {result}")
    print(f"{message.chat.id} Выпало число: {result}")


@router.message(lambda msg: msg.text == "Кинуть 2 шестигранных кубика одновременно")
async def roll_two_dice(message: Message):
    result1 = random.randint(1, 6)
    result2 = random.randint(1, 6)
    await message.answer(f"Выпали числа: {result1} и {result2}")
    print(f"{message.chat.id} Выпали числа: {result1} и {result2}")


@router.message(lambda msg: msg.text == "Кинуть 20-гранный кубик")
async def roll_d20(message: Message):
    result = random.randint(1, 20)
    await message.answer(f"Выпало число: {result}")
    print(f"{message.chat.id} Выпало число: {result}")


@router.message(lambda msg: msg.text == "Вернуться назад")
async def back_to_start(message: Message):
    await message.answer("Выберите действие:", reply_markup=start_keyboard)


async def timer_task(chat_id: int, duration: int):
    try:
        for remaining in range(duration, 0, -1):
            await bot.send_message(chat_id, f"Осталось времени: {remaining} секунд")
            await asyncio.sleep(1)
        await bot.send_message(chat_id, "Таймер завершён!")
    except asyncio.CancelledError:
        raise


@router.message(Command(commands=['timer']))
async def start_timer(message: Message):
    chat_id = message.chat.id

    if chat_id in user_tasks:
        await message.reply("Таймер уже запущен. Отмените его командой /cancel, чтобы запустить новый.")
        return

    await message.reply("Выберите время для таймера:", reply_markup=timer_keyboard)


@router.message(lambda message: message.text in ["30 секунд", "1 минута", "5 минут"])
async def handle_timer_selection(message: Message):
    chat_id = message.chat.id

    time_mapping = {
        "30 секунд": 30,
        "1 минута": 60,
        "5 минут": 300
    }
    duration = time_mapping.get(message.text)

    await message.reply(f"Таймер на {duration} секунд запущен!", reply_markup=timer_keyboard)
    task = asyncio.create_task(timer_task(chat_id, duration))
    user_tasks[chat_id] = task


@router.message(Command(commands=['cancel']))
async def cancel_timer(message: Message):
    chat_id = message.chat.id

    if chat_id not in user_tasks:
        await message.reply("Нет запущенного таймера, который можно отменить.")
        return

    task = user_tasks.pop(chat_id)
    task.cancel()
    await message.reply("Таймер отменён!", reply_markup=start_keyboard)


@router.message(lambda message: message.text == "Вернуться назад")
async def handle_back_button(message: Message):
    await message.reply("Вы вернулись назад.", reply_markup=start_keyboard)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
