import logging
from asyncio import run

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties

from core.config import TOKEN
from core.table_queries import initializing_tables
from routers import common, register


async def startup(bot: Bot):
    initializing_tables()
    await bot.send_message(text="Bot start to work", chat_id=1358470521)


async def shutdown(bot: Bot):
    await bot.send_message(text="Bot stopped", chat_id=1358470521)


async def main():
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode='HTML'))
    dp = Dispatcher()

    dp.include_router(router=common.router)
    dp.include_router(router=register.router)

    dp.startup.register(startup)
    dp.shutdown.register(shutdown)

    await dp.start_polling(bot, polling_timeout=0)


if __name__ == '__main__':
    logging.basicConfig(
        format="[%(asctime)s] - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.INFO
    )
    logging.getLogger("aiogram.event").setLevel(logging.WARNING)
    run(main())
