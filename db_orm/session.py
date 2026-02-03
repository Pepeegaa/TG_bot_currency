from sqlalchemy.orm import sessionmaker
from TG_bot.db_orm.engine import engine

SessionLocal = sessionmaker(bind=engine)