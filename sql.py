import asyncio
import asyncpg
import logging

from utils.db_api.postgresql import create_db


logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.INFO)
        


if __name__ == '__main__':
     loop = asyncio.get_event_loop()
     loop.run_until_complete(create_db())
