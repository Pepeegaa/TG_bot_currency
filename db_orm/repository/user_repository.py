from TG_bot_currency.db_orm.session import SessionLocal
from TG_bot_currency.db_orm.models import User
from sqlalchemy.exc import SQLAlchemyError
import logging

logger = logging.getLogger(__name__)

class UserRepository:
    """Репозиторий для работы с пользователями в БД"""

    def __init__(self):
        # Каждая операция создаёт новую сессию
        self.session = SessionLocal()

    # --- CREATE / ENSURE ---
    def ensure_user(self, telegram_id: int, username: str | None) -> User:
        """
        Проверяем есть ли пользователь в БД.
        Если нет — создаём.
        Возвращает объект User.
        """
        try:
            user = self.session.query(User).filter_by(telegram_id=telegram_id).first()
            if not user:
                user = User(telegram_id=telegram_id, username=username)
                self.session.add(user)
                self.session.commit()
                logger.info("Создан новый пользователь %s", telegram_id)
            return user
        except SQLAlchemyError as e:
            logger.exception("Ошибка ensure_user")
            self.session.rollback()
            raise
        finally:
            self.session.close()

    # --- READ ---
    def get_user(self, telegram_id: int) -> User | None:
        try:
            return self.session.query(User).filter_by(telegram_id=telegram_id).first()
        except SQLAlchemyError as e:
            logger.exception("Ошибка get_user")
            raise
        finally:
            self.session.close()

    def get_user_state(self, telegram_id: int) -> str | None:
        user = self.get_user(telegram_id)
        return user.state if user else None

    # --- UPDATE ---
    def set_user_state(self, telegram_id: int, state: str | None):
        try:
            user = self.session.query(User).filter_by(telegram_id=telegram_id).first()
            if user:
                user.state = state
                self.session.commit()
                logger.info("User %s: FSM state -> %s", telegram_id, state)
        except SQLAlchemyError as e:
            logger.exception("Ошибка set_user_state")
            self.session.rollback()
            raise
        finally:
            self.session.close()

    def update_city(self, telegram_id: int, city: str):
        try:
            user = self.session.query(User).filter_by(telegram_id=telegram_id).first()
            if user:
                user.city = city
                self.session.commit()
                logger.info("User %s: обновлен город -> %s", telegram_id, city)
        except SQLAlchemyError as e:
            logger.exception("Ошибка update_city")
            self.session.rollback()
            raise
        finally:
            self.session.close()

    def update_language(self, telegram_id: int, language: str):
        try:
            user = self.session.query(User).filter_by(telegram_id=telegram_id).first()
            if user:
                user.language = language
                self.session.commit()
                logger.info("User %s: обновлен язык -> %s", telegram_id, language)
        except SQLAlchemyError as e:
            logger.exception("Ошибка update_language")
            self.session.rollback()
            raise
        finally:
            self.session.close()

    def update_phone(self, telegram_id: int, phone: str):
        try:
            user = self.session.query(User).filter_by(telegram_id=telegram_id).first()
            if user:
                user.phone = phone
                self.session.commit()
                logger.info("User %s: обновлен телефон", telegram_id)
        except SQLAlchemyError as e:
            logger.exception("Ошибка update_phone")
            self.session.rollback()
            raise
        finally:
            self.session.close()
