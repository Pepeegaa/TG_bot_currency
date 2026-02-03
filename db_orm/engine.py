from sqlalchemy import create_engine

DATABASE_URL = "sqlite:///C:/PyTHoN/Pycharm_proj/TG_bot_test.db"

engine = create_engine(
    DATABASE_URL,
    echo=False
)