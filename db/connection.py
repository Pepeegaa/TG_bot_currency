import sqlite3
from TG_bot.config import DB_PATH

def get_connection():
    return sqlite3.connect(DB_PATH, timeout=10)

print(DB_PATH)