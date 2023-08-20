from aiogram import Router
from aiogram.filters import CommandStart, StateFilter

import states

from . import start


def prepare_router() -> Router:
    basic_router = Router()
    basic_router.message.register(start.start, CommandStart())
    return basic_router


def prepare_user_router() -> Router:
    user_router = Router()
    return user_router


def prepare_admin_router() -> Router:
    admin_router = Router()
    return admin_router