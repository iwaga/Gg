from aiogram.fsm.state import State, StatesGroup

class SosState(StatesGroup):
    question = State()
    submit = State()

class AnswerState(StatesGroup):
    answer = State()
    submit = State()