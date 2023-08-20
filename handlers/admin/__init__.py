from aiogram import Router
from aiogram.filters import Command

import states
from filters import IsAdminFilter

from . import menu


def prepare_router() -> Router:
    router = Router()
    router.message.filter(IsAdminFilter)
    
    # register handlers
    router.message.register(menu.menu, Command('menu'))
    
    return router