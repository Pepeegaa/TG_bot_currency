from sqlalchemy.orm import sessionmaker
from TG_bot_currency.db_orm.engine import engine

SessionLocal = sessionmaker(bind=engine)