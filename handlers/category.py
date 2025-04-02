from aiogram import Router
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.fsm.context import FSMContext
from states import CategoryForm

r = Router()


@r.callback_query(CategoryForm.category_choosing)
async def category_chosen(callback: CallbackQuery, state: FSMContext):
    chosen_category = callback.data
    await state.update_data(chosen_category=chosen_category)

    if chosen_category == "ad":
        markup = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="ИП", callback_data="ip")],
            [InlineKeyboardButton(text="Юр. лицо", callback_data="ur")],
            [InlineKeyboardButton(text="Физ. лицо", callback_data="fiz")],
            [InlineKeyboardButton(text="Назад", callback_data="back")],
        ])
        await callback.message.edit_text("Вы ИП, Юр. лицо или Физ. лицо?", reply_markup=markup)
        await state.set_state(CategoryForm.advertiser_type_choosing)
    elif chosen_category == "tickets":
        markup = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Назад", callback_data="back")],
        ])
        instructions = ("Расположите информацию о спектакле в следующем сообщении, как в образце:\n\n"
                        "Название спектакля/мероприятия\n"
                        "Место проведения\n"
                        "Дата и время\n"
                        "Количество билетов, ряд и места\n"
                        "Цена\n"
                        "Номер для связи или ник через @")
        msg = await callback.message.edit_text(instructions, reply_markup=markup)
        await state.update_data(last_bot_message_id=msg.message_id)
        await state.set_state(CategoryForm.tickets)
    elif chosen_category == "other":
        markup = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Назад", callback_data="back")],
        ])
        msg = await callback.message.edit_text("Пожалуйста, напишите Ваше обращение в следующем сообщении.",
                                               reply_markup=markup)
        await state.update_data(last_bot_message_id=msg.message_id)
        await state.set_state(CategoryForm.other_topic)

    await callback.answer()
