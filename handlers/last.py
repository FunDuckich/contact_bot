from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from config import ADMIN_CHAT_ID

r = Router()


@r.message()
async def start_command(message: Message, state: FSMContext):
    if message.chat.id == ADMIN_CHAT_ID:
        return
    await state.clear()
    await message.answer("Чтобы связаться с администратором, используйте команду /start.\n"
                         "<b>Очень важно, чтобы в вашем профиле показывался ник!</b>")
