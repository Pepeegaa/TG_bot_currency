from repository import add_user, user_exists

def ensure_user(telegram_id, username):
    if not user_exists(telegram_id):
        add_user(telegram_id, username)