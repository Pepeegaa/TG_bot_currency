from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from TG_bot.states.form import Form
from TG_bot.db_orm.repository.user_repository import UserRepository

router = Router()
repo = UserRepository()

STATE_MAP = {"Form.city": Form.city,
             "Form.lang": Form.lang,
             "Form.phone": Form.phone, }

@router.message(Command("start"))
async def start(message: Message, state: FSMContext):
    telegram_id = message.from_user.id
    username = message.from_user.username or message.from_user.first_name

    try:
        # создаём пользователя, если его нет
        repo.ensure_user(telegram_id, username)

        # проверяем сохранённое FSM-состояние
        db_state = repo.get_user_state(telegram_id)
        if db_state:
            await state.set_state(STATE_MAP[db_state])
            await message.answer("Продолжаем с того места, где остановились")
            return

        # если нового пользователя — начинаем с города
        await state.set_state(Form.city)
        repo.set_user_state(telegram_id, "Form.city")
        await message.answer("Привет! В каком ты городе?")
    except Exception as e:
        await message.answer("Произошла ошибка, попробуй позже")
        import traceback
        print(f"[ERROR] start handler: {e}\n{traceback.format_exc()}")