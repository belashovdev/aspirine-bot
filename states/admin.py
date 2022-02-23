from aiogram.dispatcher.filters.state import StatesGroup, State

class Mailing(StatesGroup):
    Order1 = State()
    Order2 = State()

class EditPage(StatesGroup):
    Order1 = State()
    Order2 = State()