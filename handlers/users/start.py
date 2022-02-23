from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher.filters import Command

from loader import dp, db
from keyboards.default import menu


@dp.message_handler(text="⬅️ Главное меню")
@dp.message_handler(CommandStart())
async def register_user(message: types.Message):
    chat_id = message.from_user.id
    referral = message.get_args()
    user = await db.add_new_user(referral=referral)
    # id = user.id
   
    await message.answer(f"Привет, {message.from_user.full_name}!", reply_markup=menu)



