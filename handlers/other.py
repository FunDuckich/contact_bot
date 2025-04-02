from aiogram import Router, Bot
from aiogram.exceptions import TelegramBadRequest
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from config import ADMIN_CHAT_ID
from states import CategoryForm

r = Router()


@r.message(CategoryForm.other_topic)
async def get_other_topic(message: Message, state: FSMContext, bot: Bot):
    await state.update_data(other_topic=message.text)
    user_data = await state.get_data()
    await state.clear()

    forward_message_text = (
        "#другое\n\n"
        f"<b>Сообщение:</b>\n {user_data.get("other_topic", "не указано")}\n\n"
        f"<b>Контакты:</b> {message.from_user.full_name} (@{message.from_user.username})"
    )

    try:
        await bot.send_message(ADMIN_CHAT_ID, forward_message_text)
    except TelegramBadRequest:
        print(Exception, "\nСообщение:", forward_message_text)

    last_bot_message_id = user_data.get("last_bot_message_id")
    if last_bot_message_id:
        try:
            await bot.delete_message(chat_id=message.chat.id, message_id=last_bot_message_id)
        except Exception as e:
            print(f"Ошибка удаления сообщения: {e}")

    await message.answer("Ваше сообщение отправлено администратору.")
