from aiogram import Router
from aiogram.filters import Command

import states
from filters import IsUserFilter

from . import menu


def prepare_router() -> Router:
    router = Router()
    router.message.filter(IsUserFilter)
    
    # register handlers
    router.message.register(menu.menu, Command('menu'))
    
    return router