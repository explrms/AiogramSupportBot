from aiogram.dispatcher.filters.state import StatesGroup, State


class SupportState(StatesGroup):
    send_request = State()
    in_support = State()
