from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import StateFilter, Command

router = Router()

@router.message(StateFilter(None) & ~Command("start", "rate", "premium", "buy") & F.text)
async def free_chat(message: Message):
    await message.answer("Вижу ваше сообщение, но оно не является командой для работы со мной")