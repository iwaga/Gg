from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters.callback_data import CallbackData
from loader import db


class ProductCallback(CallbackData, prefix='product'):
    id: int
    action: str
    

# Create product markup
def product_markup(idx='', price=0) -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(f'Добавить в корзину - {price}₽', callback_data=ProductCallback(id=idx, action='add')))
    return markup