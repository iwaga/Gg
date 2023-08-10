from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters.callback_data import CallbackData
from loader import db

class CategoryCallback(CallbackData, prefix='category'):
    id: int
    action: str


# Create categories markup
def categories_markup() -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup()
    for idx, title in db.fetchall('SELECT * FROM categories'):
        markup.add(InlineKeyboardButton(title, callback_data=CategoryCallback(id=idx, action='view').pack()))
    return markup
