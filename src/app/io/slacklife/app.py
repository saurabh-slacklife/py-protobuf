import os

from flask import Flask

from app.io import logger
from app.io.slacklife.blueprints.user_blueprint import user_bp
from app.io.slacklife.extensions import redis_service


class ManageApp():
    def __init__(self):
        self.flask_app: Flask = Flask(__name__, static_folder=None)
        self.initialize_app()

        self.app_config = self.flask_app.config

    def initialize_app(self):
        logger.info(f'App getting initialized')
        self.flask_app = Flask(__name__, static_folder=None)
        self.flask_app.config.from_object(AppConfig())
        # self.flask_app.config.from_envvar('SERVICE_ENV_CONFIG')
        self.register_blueprints()
        self.initialize_redis_service()
        logger.info(f'App getting initialized')

    def register_blueprints(self):
        self.flask_app.register_blueprint(blueprint=user_bp, url_prefix='/user', options=self.flask_app.config)

    def initialize_redis_service(self):
        logger.info(f'Initializing Redis')
        redis_service.initialize_service(self.flask_app.config)
        logger.info(f'Initialized Redis')

    @property
    def get_app(self) -> Flask:
        return self.flask_app


class AppConfig:
    ENV = os.environ.get('SERVICE_ENV', default='development')
    REDIS_HOST = os.environ.get('REDIS_HOST', default='localhost')
    REDIS_PORT = os.environ.get('REDIS_PORT', default=6379)
    REDIS_P = os.environ.get('REDIS_P', default='')
    SERVER_NAME = os.environ.get('SERVER_NAME')
    MAX_CONTENT_LENGTH = os.environ.get('MAX_CONTENT_LENGTH')
