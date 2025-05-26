import random
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode


API_TOKEN = '7876739515:AAETbE5IIDeEcefRfsQHFV8o10qVaBJxihA'


bot = Bot(
    token=API_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)
dp = Dispatcher()


numbers = {}


@dp.message(Command("start"))
async def start(message: types.Message):
    numbers[message.from_user.id] = random.randint(1, 100)
    await message.answer("Я загадал число от 1 до 100. Попробуй угадать!")


@dp.message(lambda message: message.text and message.text.isdigit())
async def guess_number(message: types.Message):
    user_id = message.from_user.id
    if user_id not in numbers:
        await message.answer("Сначала напиши /start")
        return

    guess = int(message.text)
    secret = numbers[user_id]

    if guess < secret:
        await message.answer("Больше!")
    elif guess > secret:
        await message.answer("Меньше!")
    else:
        await message.answer(f"🎉 Правильно! Это было число {secret}!")
        del numbers[user_id]


@dp.message()
async def other_messages(message: types.Message):
    await message.answer("Пожалуйста, вводи только числа или /start для новой игры")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())