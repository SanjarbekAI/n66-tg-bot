from asyncio import run

from aiogram import Bot, Dispatcher, types, F
from aiogram.client.default import DefaultBotProperties
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

user_main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Menyu")
        ],
        [
            KeyboardButton(text="Mening buyurtmalarim")
        ],
        [
            KeyboardButton(text="Savat"),
            KeyboardButton(text="Aloqa"),
        ],
    ],
    resize_keyboard=True,
    is_persistent=True
)

user_menu_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="a"),
            KeyboardButton(text="b"),
        ],
    ],
    resize_keyboard=True,
    is_persistent=True
)


async def start_handler(message: types.Message):
    text = (f"Assalomu alaykum, "
            f"{message.from_user.mention_html(f'{message.from_user.full_name}')}")
    await message.answer(text=text, reply_markup=user_main_keyboard)


async def menu_handler(message: types.Message):
    text = "Menyu bosildi"
    await message.answer(text=text, reply_markup=user_menu_keyboard)


async def main():
    bot = Bot(token="7930392265:AAGHQbflfsixVfqGtK_sNHRt7H3jFlsZBqQ", default=DefaultBotProperties(parse_mode='HTML'))
    dp = Dispatcher()
    dp.message.register(start_handler, Command('start'))
    dp.message.register(menu_handler, F.text == "Menyu")

    await dp.start_polling(bot, polling_timeout=0)


if __name__ == '__main__':
    run(main())
