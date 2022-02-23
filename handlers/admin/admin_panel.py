from aiogram import types
from aiogram.types import ReplyKeyboardRemove
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from data import config

from loader import dp, db
from states import Mailing, EditPage
from keyboards.default import menu, admin_menu

@dp.message_handler(user_id=config.ADMINS, commands=['admin'])
async def admin_panel(message: types.Message):
    await message.answer("Панель администратора", reply_markup=admin_menu)


@dp.message_handler(user_id=config.ADMINS, text="💌 Заявки")
async def admin_panel(message: types.Message):
    orders = await db.get_orders()

    all_order = ""
    #[User link](tg://user?id=111111)
    for order in orders:
        user_id = str(order.user_id)
        referral = order.referral
        contact = order.contact
        date  = str(order.date)
        message_order = (f"*Заявка* от [{user_id}](tg://user?id={user_id}) \n"
                         f"{contact} \n"
                         f"_Дата: {date}_ \n\n")
        
        all_order += message_order

    await message.answer(f"Последние 20 заявок: \n\n"
                         f"{all_order}", reply_markup=admin_menu)




