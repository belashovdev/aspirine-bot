import asyncio
from aiogram import executor

from loader import dp, create_db

import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands
from utils.db_api.postgresql import create_db, DBCommands

        


create_db()
contacts = """
📞 *Контакты для связи* 

*Менеджер в тг:* @chernyshev148
*Номер:* +7 (995) 675-75-50
*Официальная страница тг:* @aspirineasic
*Сайт:* [aspirine-ekaterinburg.ru](https://aspirine-ekaterinburg.ru) 
"""

delivery = """
✈️ *Доставка и оплата* 
К оплате доступны следующие способы:
Наличные, перевод на карту, криптой (USDT)

Доставка осуществляется по всему СНГ.
Подробнее про доставку в ваш регион можно спросить у нашего менеджера (раздел "Контакты")

Доставка из Китая - 45 дней, 100% предоплата с заключением договора поставки.
Доставка из Москвы - 5-7 дней, предоплата 20-100%, в зависимости от объема поставки.

"""

DBCommands.add_new_page("", "pricelist", "Страница с актуальным прайс листом")
DBCommands.add_new_page("", "delivery", delivery)
DBCommands.add_new_page("", "contact", contacts)

