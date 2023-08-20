from aiogram import Router
from aiogram.filters import CommandStart

import states

from . import start, user, admin


def prepare_router() -> Router:
    router = Router()
    
    # register handlers
    router.message.register(start.start, CommandStart())
    
    # register routers
    router.include_router(user.prepare_router())
    router.include_router(admin.prepare_router())
    
    return router