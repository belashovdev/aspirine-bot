import asyncio
import asyncpg
import logging

from utils.db_api.postgresql import Database


logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.INFO)

db = Database()
async def create_db():
   
        await db.create()
        logging.info("Connecting to database...")
        await db.create_table_pricelist()
        logging.info("Table users created")
        await db.add_pricelist("novuy pricelist", "12-12-12")
        await db.update_pricelist()
        #await db.create_table_users()
        


if __name__ == '__main__':
     loop = asyncio.get_event_loop()
     loop.run_until_complete(create_db())
