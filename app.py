import logging

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from data import load_config
import handlers
from aiogram.utils.executor import start_polling

config = load_config(r"config.ini")
async def on_startup(dp):
    # Setup handlers
    handlers.setup(dp)
    logging.warning("Bot started")


async def on_shutdown(dp):
    logging.warning("Shutting down..")
    await dp.bot.session.close()
    await dp.storage.close()
    await dp.storage.wait_closed()
    logging.warning("Bye!")


bot = Bot(config.bot.token)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

def starter():
    start_polling(dp,on_startup= on_startup, on_shutdown= on_shutdown)

if __name__ == "__main__":
    starter()

