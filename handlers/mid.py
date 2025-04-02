from aiogram import Router
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.fsm.context import FSMContext
from states import CategoryForm

r = Router()


@r.callback_query(CategoryForm.tickets)
@r.callback_query(CategoryForm.other_topic)
async def back_to_category_choosing(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Размещение рекламы", callback_data="ad")],
        [InlineKeyboardButton(text="Пристрой билетов", callback_data="tickets")],
        [InlineKeyboardButton(text="Другое", callback_data="other")],
    ])
    await callback.message.edit_text(text="Укажите тему обращения:", reply_markup=markup)
    await state.set_state(CategoryForm.category_choosing)
