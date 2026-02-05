# Telegram Bot

### Описание проекта:

Telegram-бот с анкетированием пользователей, сохранением данных в БД, интеграцией внешнего API и системой оплаты через Telegram Stars.
Готов к доработке под определенные задачи и цели.

### Используемые технологии

* Python 3.13
* aiogram 3.x
* FSM (Finite State Machine)
* SQLite + SQLAlchemy (ORM)
* aiohttp (API)
* Telegram Payments (Stars)
* logging
* systemd (production deploy)
* Git / GitHub

### Функциональность

1. регистрация пользователя (пошаговая анкета FSM)
2. хранение состояния в БД (для восстановления диалога после перезапуска)
3. интеграция внешнего API (курс валют, погода и т.п.)
4. платный доступ через Telegram Stars
5. логирование ошибок
6. возможность работе на серверах

### Переменные окружения (.env)
```bash
BOT_TOKEN=your_bot_token
API_KEY_RATE=your_api_key
```

### Запуск локально
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python -m TG_bot.bot
```

### Деплой на сервер (Ubuntu)
```bash
git clone https://github.com/yourname/project.git
cd project
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
systemctl start tg_bot
```