import logging

from aiogram import Dispatcher

from data.config import ADMINS


async def on_startup_notify(dp: Dispatcher):
    for admin in ADMINS:
        try:
            await dp.bot.send_message(admin, "Бот Запущен")

        except Exception as err:
            logging.exception(err)

async def order_notify(dp: Dispatcher, order):
    for admin in ADMINS:
        try:
            await dp.bot.send_message(admin, str(order))

        except Exception as err:
            logging.exception(err)
