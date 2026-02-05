from sqlalchemy import create_engine

DATABASE_URL = "sqlite:////opt/TG_bot/db_orm/TG_bot_test.db"

engine = create_engine(
    DATABASE_URL,
    echo=False
)