import logging

from aiogram import Bot, types, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware

import config

bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)

dp = Dispatcher(bot, storage=MemoryStorage())

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

dp.middleware.setup(LoggingMiddleware(logger=logger))
