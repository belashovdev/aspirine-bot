from datetime import datetime
from typing import Text
from aiogram import types, Bot
from gino import Gino
from gino.schema import GinoSchemaVisitor
from sqlalchemy import (Column, Integer, BigInteger, String,
                        Sequence, TIMESTAMP, Boolean, JSON, Text)
from sqlalchemy import sql

from data import config

db = Gino()


# Документация
# http://gino.fantix.pro/en/latest/tutorials/tutorial.html

class User(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    user_id = Column(BigInteger)
    username = Column(String(50))
    referral = Column(Integer)
    query: sql.Select

    def __repr__(self):
        return "<User(id='{}', username='{}',referral='{}')>".format(
            self.id, self.username, self.referral)


class Page(db.Model):
    __tablename__ = 'page'
    query: sql.Select

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    key = Column(String(250))
    text = Column(Text())

    def __repr__(self):
        return "<Page(id='{}', text='{}', date='{}', key='{}')>".format(
            self.id, self.text, self.date, self.key)


class Order(db.Model):
    __tablename__ = 'order'
    query: sql.Select

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    user_id = Column(BigInteger)
    referral = Column(Integer)
    contact = Column(String(250))
    date = Column(String(250))

    def __repr__(self):
        return "<Order(id='{}', user_id='{}', contact='{}', date='{}', referral='{}')>".format(
            self.id, self.user_id, self.contact, self.date, self.referral)



class DBCommands:

    async def get_user(self, user_id):
        user = await User.query.where(User.user_id == user_id).gino.first()
        return user

    async def add_new_user(self, referral=None):
        user = types.User.get_current()
        old_user = await self.get_user(user.id)
        if old_user:
            return old_user
        new_user = User()
        new_user.user_id = user.id
        new_user.username = user.username

        if referral:
            new_user.referral = int(referral)
        await new_user.create()
        return new_user

    async def count_users(self) -> int:
        total = await db.func.count(User.id).gino.scalar()
        return total

    async def check_referrals(self):
        bot = Bot.get_current()
        user_id = types.User.get_current().id

        user = await User.query.where(User.user_id == user_id).gino.first()
        referrals = await User.query.where(User.referral == user.id).gino.all()

        return ", ".join([
            f"{num + 1}. " + (await bot.get_chat(referral.user_id)).get_mention(as_html=True)
            for num, referral in enumerate(referrals)
        ])


    async def add_new_order(self, contact):
        new_order = Order()
        new_order.user_id = types.User.get_current()  
        #new_order.referral = referral
        new_order.contact = contact
        
        dt = datetime.now()
        new_order.date = dt.strftime('%m.%d.%Y')
        await new_order.create()
        return new_order

    async def get_orders(self):
        orders = await Order.query.limit(20).order_by(Order.id.desc()).gino.all()
        return orders

    async def add_new_page(self, key, text):
        new_page = Page()
        new_page.key = key
        new_page.text = text

        await new_page.create()
        return new_page

    async def get_page(self, keyword):
        page = await Page.query.where(Page.key == keyword).gino.first()
        return page



async def create_db():
    await db.set_bind(f'postgresql://{config.PGUSER}:{config.PGPASSWORD}@{config.IP}/gino')

    # Create tables
    await db.gino.drop_all()
    await db.gino.create_all()
    await DBCommands.add_new_page("", "pricelist", "Страница с актуальным прайс листом")
    await DBCommands.add_new_page("", "delivery", "Страница с доставка и оплата")
    await DBCommands.add_new_page("", "contact", "Актуальные контакты")


