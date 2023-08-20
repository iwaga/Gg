from aiogram import html, types
from aiogram.fsm.context import FSMContext
from states import LanguageState
from data.strings.ru import start_message


async def start(msg: types.Message, state: FSMContext) -> None:
    await msg.answer(start_message)
    await state.set_state(LanguageState.language)