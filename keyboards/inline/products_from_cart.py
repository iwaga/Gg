from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters.callback_data import CallbackData


class ProductCallback(CallbackData, prefix='product'):
    id: int
    action: str


# Create products markup
def product_markup(idx, count) -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup()
    back_btn = InlineKeyboardButton('⬅️', callback_data=ProductCallback(id=idx, action='decrease').pack())
    count_btn = InlineKeyboardButton(count, callback_data=ProductCallback(id=idx, action='count').pack())
    next_btn = InlineKeyboardButton('➡️', callback_data=ProductCallback(id=idx, action='increase').pack())
    markup.row(back_btn, count_btn, next_btn)
    return markup