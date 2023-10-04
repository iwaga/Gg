import asyncio
import logging
from aiogram import Bot, Dispatcher
from data import config
import handlers

logging.basicConfig(level=logging.INFO)
bot = Bot(token=config.BOT_TOKEN, parse_mode='HTML')
dp = Dispatcher()


def setup_handlers(dp: Dispatcher) -> None:
    dp.include_router(handlers.prepare_router())


async def main():
    setup_handlers(dp)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())