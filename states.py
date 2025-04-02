from aiogram.fsm.state import State, StatesGroup


class CategoryForm(StatesGroup):
    category_choosing = State()
    adv_item_choosing = State()
    advertiser_type_choosing = State()
    tickets = State()
    other_topic = State()
