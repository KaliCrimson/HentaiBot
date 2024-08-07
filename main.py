import asyncio
from aiogram import Bot, Dispatcher

import common, handlers


async def main():

    dp = Dispatcher()
    bot = Bot(token="YOUR_BOT_TOKEN")

    dp.include_router(common.router)
    dp.include_router(handlers.router)

    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
