from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher.filters import Command

from loader import dp
from keyboards.default import menu


@dp.message_handler(CommandStart())
@dp.message_handler(Command("menu"))
async def bot_start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.full_name}!", reply_markup=menu)
