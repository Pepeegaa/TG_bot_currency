from aiogram import Router
from aiogram.filters import Command
from TG_bot.db_orm.repository.payment_repository import PaymentRepository
from aiogram.types import Message

router = Router()
repo = PaymentRepository()

@router.message(Command("premium"))
async def premium(message: Message):
    if not repo.has_active_payment(message.from_user.id):
        await message.answer("⛔ Доступ только после оплаты")
        return

    await message.answer("✅ Добро пожаловать в премиум!")