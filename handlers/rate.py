from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from TG_bot.services.usd_rate import get_usd_rate

router = Router()

@router.message(Command("rate"))
async def rate_handler(message: Message):
    session = message.bot.dispatcher["session"]

    rate = await get_usd_rate(session)

    if not rate:
        await message.answer("Не удалось получить курс 😢")
        return

    await message.answer(f"💱 1 USD = {rate} RUB")