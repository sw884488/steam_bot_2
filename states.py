from aiogram.dispatcher.filters.state import State, StatesGroup

class test(StatesGroup):
    waiting_for_game_name = State()
    waiting_for_game_number = State()