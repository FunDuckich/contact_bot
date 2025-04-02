import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from config import BOT_TOKEN
from handlers import (
    first_router,
    category_router,
    adv_router,
    mid_router,
    tickets_router,
    other_router,
    last_router
)


logging.basicConfig(level=logging.INFO)

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN не задан! Проверьте переменные окружения.")


bot = Bot(
    token=BOT_TOKEN,
    default=DefaultBotProperties(parse_mode='HTML')
)

dp = Dispatcher()

dp.include_routers(
    first_router,
    category_router,
    adv_router,
    mid_router,
    tickets_router,
    other_router,
    last_router
)


async def main():
    await dp.start_polling(bot, drop_pending_updates=True)


if __name__ == "__main__":
    asyncio.run(main())
