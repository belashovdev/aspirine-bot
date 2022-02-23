from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

admin_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="💌 Заявки"),
            KeyboardButton(text="📨 Рассылка"),
        ],
        [   
            KeyboardButton(text="📄 Прайс-лист"),
            KeyboardButton(text="🚛 Доставка и оплата"),
            KeyboardButton(text="📞 Контакты"),
        ],
        [
            KeyboardButton(text="⬅️ Главное меню"),
        ],
    ],
    resize_keyboard=True
)

