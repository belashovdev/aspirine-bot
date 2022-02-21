from typing import Union
from inspect import Parameter
import asyncpg
from asyncpg import Pool

from data import config

class Database:
    def __init__(self):
       self.pool: Union[Pool, None] = None
    
    async def create(self):
        pool = await asyncpg.create_pool(
            user=config.PGUSER,
            password=config.PGPASSWORD,
            host=config.IP,
            database=config.DATABASE
        )
        self.pool=pool
       
    async def create_table_users(self):
        sql = """
        CREATE TABLE IF NOT EXISTS users(
        id INT NOT NULL,
        name VARCHAR(255) NOT NULL,
        contact VARCHAR(255),
        ref VARCHAR(255),
        PRIMARY KEY (id)
        )
        """
        await self.pool.execute(sql)

    async def create_table_pricelist(self):
        sql = """
        CREATE TABLE IF NOT EXISTS pricelist(
        id INT NOT NULL,
        pricelist TEXT NOT NULL,
        date VARCHAR(255),
        PRIMARY KEY (id)
        )
        """
        await self.pool.execute(sql)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ${num}" for num, item in enumerate(parameters, start=1)
        ])
        return sql, tuple(parameters.values())

    async def add_user(self, id: int, name: str, contact: str = None):
        sql = "INSERT INTO users (id, name, contact) VALUES ($1, $2, $3)"
        await self.pool.execute(sql, id, name, contact)

    async def select_all_users(self):
        sql = "SELECT * FROM users"
        return await self.pool.fetch(sql)

    async def select_user (self, **kwargs):
        sql = "SELECT * FROM users WHERE "
        sql, parameters = self.format_args(sql, kwargs)
        return await self.pool.fetchrow(sql, *parameters)

    async def count_users(self):
        return await self.pool.fetchval("SELECT COUNT(*) FROM users")

    async def update_user_contact(self, contact, id):
        sql = "UPDATE users SET contact = $1 WHERE id = $2"
        return await self.pool.execute (sql, contact, id)

    async def delete_users(self):
        await self.pool.execute("DELETE FROM users WHERE True")


    # Методы для работы с прайслистом
    async def add_pricelist(self, pricelist: str, date: str):
        sql = "INSERT INTO pricelist (id, pricelist, date) VALUES (1, $1, $2)"
        return await self.pool.execute(sql, pricelist, date)

    async def select_last_pricelist (self):
        sql = "SELECT * FROM pricelist"
        return await self.pool.fetch(sql)

    async def update_pricelist(self):
        last_pricelist_id = await self.select_last_pricelist()
        print(last_pricelist_id)
        #sql = "UPDATE pricelist SET pricelist = $1, date = $2 WHERE id = $3"
        #return await self.pool.execute (sql, pricelist, date, last_pricelist_id)

    
    
    
