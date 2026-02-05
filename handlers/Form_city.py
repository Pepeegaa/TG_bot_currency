from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from TG_bot.states.form import Form
from repository import set_user_state, update_city

router = Router()

@router.message(Form.city)
async def process_city(message: Message, state: FSMContext):
    print("FSM HANDLER city WORKED")
    update_city(message.from_user.id, message.text)

    await message.answer("Понял, а какой твой язык программирования?")
    await state.set_state(Form.lang)
    set_user_state(message.from_user.id, "Form.lang")