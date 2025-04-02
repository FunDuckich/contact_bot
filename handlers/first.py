from aiogram import Router
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from aiogram.fsm.context import FSMContext
from config import ADMIN_CHAT_ID
from states import CategoryForm
from aiogram.filters.command import Command

r = Router()


# @r.message()
# async def get_chat_id(message: Message):
#     print(f"Chat ID: {message.chat.id}")
#     await message.answer("Всё, я получил id чатика)")


@r.message(Command("start"))
async def contact_command(message: Message, state: FSMContext):
    if message.chat.id == ADMIN_CHAT_ID:
        return
    await state.clear()
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Размещение рекламы", callback_data="ad")],
        [InlineKeyboardButton(text="Пристрой билетов", callback_data="tickets")],
        [InlineKeyboardButton(text="Другое", callback_data="other")],
    ])
    await message.answer("Укажите тему обращения:", reply_markup=markup)
    await state.set_state(CategoryForm.category_choosing)
