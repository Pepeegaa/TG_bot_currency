from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from TG_bot.states.form import Form
from repository import set_user_state, update_phone

router = Router()

@router.message(Form.phone)
async def process_phone(message: Message, state: FSMContext):
    print(print("FSM HANDLER phone WORKED"))
    update_phone(message.from_user.id, message.text)
    await message.answer('Все записал. Спасибо за содействие!')
    await state.clear()
    set_user_state(message.from_user.id, None)