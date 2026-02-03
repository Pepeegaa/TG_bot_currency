from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

language_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Python", callback_data="lang:python")],
        [InlineKeyboardButton(text="JS", callback_data="lang:js")]
    ]
)