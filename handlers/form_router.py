from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from TG_bot.states.form import Form
from TG_bot.db_orm.repository.user_repository import UserRepository
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s"
)
logger = logging.getLogger(__name__)

router = Router()
repo = UserRepository()

STATE_MAP = {
    "Form.city": Form.city,
    "Form.lang": Form.lang,
    "Form.phone": Form.phone,
}

@router.message(Form.city)
async def process_city(message: Message, state: FSMContext):
    print("FSM HANDLER city WORKED")

    try:
        repo.update_city(message.from_user.id, message.text)
        logger.info(
            "User %s set city: %s",
            message.from_user.id,
            message.text
        )

        await state.set_state(Form.lang)
        await message.answer("Понял, а какой твой язык программирования?")
        repo.set_user_state(message.from_user.id, "Form.lang")
    except Exception as e:
        logger.exception(f"Ошибка в process_city{e}")
        print(f"[ERROR] start handler: {e}")
        await message.answer("Ошибка. Попробуй ещё раз")

@router.message(Form.lang)
async def process_lang(message: Message, state: FSMContext):
    print("FSM HANDLER lang WORKED")
    try:
        repo.update_language(message.from_user.id, message.text)
        logger.info(
            "User %s set lang: %s",
            message.from_user.id,
            message.text
        )

        await message.answer("Круто. А какой у тебя номер телефона?")
        await state.set_state(Form.phone)
        repo.set_user_state(message.from_user.id, "Form.phone")
    except Exception as e:
        logger.exception(f"Ошибка в process_lang{e}")
        print(f"[ERROR] start handler: {e}")
        await message.answer("Ошибка. Попробуй ещё раз")

@router.message(Form.phone)
async def process_phone(message: Message, state: FSMContext):
    print("FSM HANDLER phone WORKED")
    try:
        repo.update_phone(message.from_user.id, message.text)
        logger.info(
            "User %s set phone: %s",
            message.from_user.id,
            message.text
        )

        await message.answer('Все записал. Спасибо за содействие!')
        await state.clear()
        repo.set_user_state(message.from_user.id, None)
    except Exception as e:
        logger.exception(f"Ошибка в process_phone{e}")
        print(f"[ERROR] start handler: {e}")
        await message.answer("Ошибка. Попробуй ещё раз")

