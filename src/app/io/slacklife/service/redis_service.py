from flask import Config
from redis import Redis

from app.io import logger


class RedisService:
    def __init__(self):
        self.__redis_connection: Redis = None

    def initialize_service(self, config: Config):
        logger.info(f'''Connection details: {config.get('REDIS_HOST')}:{config.get('REDIS_PORT')}''')
        self.__redis_connection = Redis(host=config.get('REDIS_HOST'),
                                        port=config.get('REDIS_PORT'),
                                        password=config.get('REDIS_P'),
                                        health_check_interval=15)

    @property
    def get_redis(self):
        return self.__redis_connection
