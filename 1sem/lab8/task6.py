import asyncio
from datetime import datetime

from aiogram import Bot, Dispatcher, Router, types
from aiogram.types import Message
from config import BOT_TOKEN
from aiogram.filters import Command

token = BOT_TOKEN

bot = Bot(token=token)
router = Router()
dp = Dispatcher()

dp.include_router(router)


@router.message(Command(commands=['time']))
async def current_time(message: Message):
    now = datetime.now().strftime("%H:%M:%S")
    await message.answer(f"Текущее время: {now}")
    print(f"{message.message_id} Текущее время: {now}")


@router.message(Command(commands=['date']))
async def current_date(message: Message):
    today = datetime.now().strftime("%Y-%m-%d")
    await message.answer(f"Текущая дата: {today}")
    print(f"{message.message_id} Текущая дата: {today}")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
