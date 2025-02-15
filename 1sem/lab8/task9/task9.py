import asyncio
import json
import random
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage

from lab8.config import BOT_TOKEN

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(storage=MemoryStorage())


class QuizStates(StatesGroup):
    Question = State()
    End = State()


with open("questions.json", "r", encoding="utf-8") as f:
    questions_data = json.load(f)["test"]


@dp.message(Command("start"))
async def start_quiz(message: Message, state: FSMContext):
    random.shuffle(questions_data)
    await state.update_data(questions=questions_data, current=0, correct=0)
    await state.set_state(QuizStates.Question)

    question_text = questions_data[0]["question"]
    await message.answer(f"Первый вопрос:\n{question_text}")


@dp.message()
async def handle_answer(message: Message, state: FSMContext):
    data = await state.get_data()
    questions = data["questions"]
    current = data["current"]
    correct = data["correct"]

    if message.text.strip().lower() == questions[current]["response"].strip().lower():
        correct += 1

    current += 1

    if current < len(questions):
        await state.update_data(current=current, correct=correct)
        question_text = questions[current]["question"]
        await message.answer(f"Следующий вопрос:\n{question_text}")
    else:
        await state.set_state(QuizStates.End)
        await message.answer(
            f"Тест завершён! Вы ответили правильно на {correct} из {len(questions)} вопросов.\n"
            f"Напишите /start, чтобы пройти тест заново.")


@dp.message(Command("stop"))
async def stop_quiz(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("Тест завершён. Напишите /start, чтобы начать заново.")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
