from aiogram import Router
from aiogram.types import Message
from aiogram.filters import StateFilter

router = Router()

@router.message(StateFilter(None))
async def free_chat(message: Message):
    await message.answer(message.text)