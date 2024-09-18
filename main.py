from dotenv import load_dotenv
from os import getenv
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

load_dotenv()

BOT_TOKEN = getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start_cmd(message: types.Message) -> None:
    await message.answer("It was command start")

# @dp.message()
# async def echo(message: types.Message) -> None:
#     await message.answer(message.text)

@dp.message()
async def message(message: types.Message, bot: Bot) -> None:
    await message.answer(message.text)
    await bot.send_message(message.from_user.id, "Answer") # Аналог метода выше
    await message.reply(message.text) # Обращается к конкретному пользователю (в нашем случае к нашему)

async def main() -> None:
    await bot.delete_webhook(drop_pending_updates=True) # Пропускаем все данные, полученные во время простоя бота
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())