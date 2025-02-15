import asyncio
from aiogram import Bot, Dispatcher, Router, types
from aiogram.types import Message
from config import BOT_TOKEN


bot = Bot(token=BOT_TOKEN)
router = Router()
dp = Dispatcher()

dp.include_router(router)


@router.message()
async def echo_message(message: Message):
    await message.answer(message.text)
    print(message.chat.id, message.text)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
