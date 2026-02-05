from TG_bot.db.connection import get_connection

def add_user(telegram_id, username):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT OR IGNORE INTO tg_users (telegram_id, username)
        VALUES (?, ?)
    """, (telegram_id, username))
    conn.commit()
    conn.close()

def user_exists(telegram_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT 1 FROM tg_users WHERE telegram_id = ?
    """, (telegram_id,))

    result = cursor.fetchone()
    conn.close()

    return result is not None