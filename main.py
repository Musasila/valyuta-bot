import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.types import Message
from aiogram.filters import Command
import wikipedia

API_TOKEN = ""
wikipedia.set_lang("uz")

bot = Bot(token=API_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

@dp.message(Command("start"))
async def start_handler(message: Message):
    await message.answer("Salem Wikipedia botina xosh keldiniz!")

@dp.message()
async def wiki_handler(message: Message):
    try:
        result = wikipedia.summary(message.text)
        await message.answer(result)
    except:
        await message.answer("Bu temaga mas ma'lumotlar topilmadi.")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
