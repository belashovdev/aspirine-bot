import imp
from aiogram import types
from aiogram.types import ReplyKeyboardRemove
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp, db
from states import Order
from keyboards.default import menu


@dp.message_handler(Command("order"))
async def order(message: types.Message, state: FSMContext):
    await state.reset_state()
    await message.answer(f"*Оставить заявку*\n\n"
                         f"Отправьте боту ваше имя и номер телефона для связи (например: Игорь, 89991232233).\n"
                         f"Мы свяжемся с вами для уточнения деталей\n", reply_markup=ReplyKeyboardRemove())

    await Order.Order1.set()


@dp.message_handler(state=Order.Order1)
async def answer_order(message: types.Message, state: FSMContext):
    contact = message.text
    await db.add_user(message.from_user.id, contact, contact)
    user = await db.select_user(id=message.from_user.id)
    
    await message.answer(f"Ваши данные: {contact}\n"
                         f"Спасибо, мы очень скоро вам перезвоним!\n", reply_markup=menu)

    await state.finish()



