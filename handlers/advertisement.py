from aiogram import Router, Bot
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, Message
from aiogram.fsm.context import FSMContext
from aiogram.exceptions import TelegramBadRequest
from config import ADMIN_CHAT_ID
from states import CategoryForm

r = Router()


@r.callback_query(CategoryForm.advertiser_type_choosing)
async def get_advertisement_type(callback: CallbackQuery, state: FSMContext):
    chosen_advertiser_type = callback.data
    if chosen_advertiser_type == "back":
        await state.clear()
        markup = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Размещение рекламы", callback_data="ad")],
            [InlineKeyboardButton(text="Пристрой билетов", callback_data="tickets")],
            [InlineKeyboardButton(text="Другое", callback_data="other")],
        ])
        await callback.message.edit_text(text="Укажите тему обращения:", reply_markup=markup)
        await state.set_state(CategoryForm.category_choosing)
    else:
        markup = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Назад", callback_data="back")],
        ])
        await state.update_data(advertiser_type_choosing=chosen_advertiser_type)
        msg = await callback.message.edit_text("Что именно вам бы хотелось отрекламировать?", reply_markup=markup)
        await state.update_data(last_bot_message_id=msg.message_id)
        await state.set_state(CategoryForm.adv_item_choosing)


@r.message(CategoryForm.adv_item_choosing)
async def get_advertisement_item(message: Message, state: FSMContext, bot: Bot):
    await state.update_data(adv_item_choosing=message.text)
    user_data = await state.get_data()

    advertiser_type_choosing = user_data.get("advertiser_type_choosing")
    if advertiser_type_choosing == "ip":
        advertisement_from = "ИП"
    elif advertiser_type_choosing == "ur":
        advertisement_from = "Юр. лицо"
    else:
        advertisement_from = "Физ. лицо"

    forward_message_text = (
        "#реклама\n\n"
        f"<b>{advertisement_from}</b>\n\n"
        f"<b>Сообщение:</b>\n{user_data.get('adv_item_choosing', 'не указали')}\n\n"
        f"<b>Контакты:</b> {message.from_user.full_name} (@{message.from_user.username})"
    )

    try:
        await bot.send_message(ADMIN_CHAT_ID, forward_message_text)
    except TelegramBadRequest:
        print("Error sending message:", forward_message_text)

    last_bot_message_id = user_data.get("last_bot_message_id")
    if last_bot_message_id:
        try:
            await bot.delete_message(chat_id=message.chat.id, message_id=last_bot_message_id)
        except Exception as e:
            print(f"Error deleting message: {e}")

    await message.answer("Ваш запрос на размещение рекламы был отправлен администратору.")
    await state.clear()


@r.callback_query(CategoryForm.adv_item_choosing)
async def back_to_advertiser_type_choosing(callback: CallbackQuery, state: FSMContext):
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="ИП", callback_data="ip")],
        [InlineKeyboardButton(text="Юр. лицо", callback_data="ur")],
        [InlineKeyboardButton(text="Физ. лицо", callback_data="fiz")],
        [InlineKeyboardButton(text="Назад", callback_data="back")],
    ])
    await callback.message.edit_text("Вы ИП, Юр. лицо или Физ. лицо?", reply_markup=markup)
    await state.set_state(CategoryForm.advertiser_type_choosing)


@r.message(CategoryForm.adv_item_choosing)
async def get_advertisement_item(message: Message, state: FSMContext, bot: Bot):
    await state.update_data(adv_item_choosing=message.text)
    user_data = await state.get_data()

    advertiser_type_choosing = user_data.get("advertiser_type_choosing")
    if advertiser_type_choosing == "ip":
        advertisement_from = "ИП"
    elif advertiser_type_choosing == "ur":
        advertisement_from = "Юр. лицо"
    else:
        advertisement_from = "Физ. лицо"

    forward_message_text = (
        "#реклама\n\n"
        f"<b>{advertisement_from}</b>\n\n"
        f"<b>Сообщение:</b>\n{user_data.get("adv_item_choosing", "не указали")}\n\n"
        f"<b>Контакты:</b> {message.from_user.full_name} (@{message.from_user.username})")

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

    await message.answer("Ваш запрос на размещение рекламы был отправлен администратору.")
    await state.clear()
