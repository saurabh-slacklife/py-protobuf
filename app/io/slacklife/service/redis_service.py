from redis import Redis
from flask import Config


class RedisService:
    def __init__(self):
        self.__redis_connection: Redis = None

    def initialize_service(self, config: Config):
        self.__redis_connection = Redis(host=config.get('REDIS_HOST'),
                                        port=config.get('REDIS_PORT'),
                                        password=config.get('REDIS_P'))

    @property
    def get_redis(self):
        return self.__redis_connection
