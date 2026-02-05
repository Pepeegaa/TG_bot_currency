from aiogram import Bot, Dispatcher
from TG_bot_currency.db_orm.engine import engine
from TG_bot_currency.db_orm.models import User, Order, Base
import logging
from handlers import start, errors, form_router
from TG_bot_currency.logging_config import setup_logging
import asyncio
import aiohttp
from TG_bot_currency.handlers import payments

from dotenv import load_dotenv
import os

load_dotenv()  # <-- ОБЯЗАТЕЛЬНО первым делом
Base.metadata.create_all(bind=engine)

async def on_startup(dispatcher: Dispatcher):
    dispatcher["session"] = aiohttp.ClientSession(
        timeout=aiohttp.ClientTimeout(total=5)
    )
    logging.info("HTTP session created")


async def on_shutdown(dispatcher: Dispatcher):
    await dispatcher["session"].close()
    logging.info("HTTP session closed")

async def main():
    setup_logging()
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    dp.include_router(start.router)
    dp.include_router(errors.router)
    dp.include_router(form_router.router)
    dp.include_router(payments.router)

    await dp.start_polling(bot)

BOT_TOKEN = os.getenv("BOT_TOKEN")
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
API_KEY_RATE = os.getenv("API_KEY_RATE")
asyncio.run(main())