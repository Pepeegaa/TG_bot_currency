from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from TG_bot.states.form import Form
from repository import set_user_state, update_language

router = Router()

@router.message(Form.lang)
async def process_lang(message: Message, state: FSMContext):
    print("FSM HANDLER lang WORKED")
    update_language(message.from_user.id, message.text)

    await message.answer("Круто. А какой у тебя номер телефона?")
    await state.set_state(Form.phone)
    set_user_state(message.from_user.id, "Form.phone")