from aiogram import Router
from aiogram.filters import Command
from TG_bot.db_orm.repository.payment_repository import PaymentRepository
from aiogram.types import PreCheckoutQuery, Message, LabeledPrice, CallbackQuery
from aiogram import F
import uuid
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

pay_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Оплатить ⭐ 0",
                callback_data="pay_stars"
            )
        ]
    ])

router = Router()
repo = PaymentRepository()


@router.message(Command("buy"))
async def buy_handler(message: Message):
    await message.answer(
        "Оплатить доступ:",
        reply_markup=pay_kb
    )


@router.callback_query(F.data == "pay_stars")
async def send_invoice(callback: CallbackQuery):
    await callback.bot.send_invoice(
        chat_id=callback.from_user.id,
        title="Доступ к боту",
        description="Полный доступ к функционалу",
        payload="order_1",
        provider_token="",  # ⭐ ВАЖНО: пусто
        currency="XTR",     # ⭐ Telegram Stars
        prices=[
            LabeledPrice(label="Доступ", amount=0)
        ]
    )

@router.pre_checkout_query(F.invoice_payload)
async def pre_checkout(pre_checkout_query: PreCheckoutQuery):
    try:
        await pre_checkout_query.answer(ok=True)
    except Exception:
        await pre_checkout_query.answer(
            ok=False,
            error_message="Ошибка при оплате"
        )
@router.message(F.successful_payment)
async def successful_payment_handler(message: Message):
    payment = message.successful_payment

    repo.creat_order(
        user_id=message.from_user.id,
        payment=payment
    )

    await message.answer("🎉 Оплата успешна! Доступ открыт.")


