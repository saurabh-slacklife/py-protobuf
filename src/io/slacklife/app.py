import logging
import os

from flask import Flask

from src.io.slacklife.blueprints.user_blueprint import user_bp
from src.io.slacklife.extensions import redis_service


class ManageApp():
    def __init__(self):
        self.logger = logging.getLogger('gunicorn.error')
        self.flask_app: Flask = Flask(__name__, static_folder=None)
        self.flask_app.logger = self.logger
        self.initialize_app()

        self.app_config = self.flask_app.config

    def initialize_app(self):
        self.flask_app = Flask(__name__, static_folder=None)
        self.flask_app.config.from_object(AppConfig())
        self.register_blueprints()
        self.initialize_redis_service()

    def register_blueprints(self):
        self.flask_app.register_blueprint(blueprint=user_bp, url_prefix='/user', options=self.flask_app.config)

    def initialize_redis_service(self):
        redis_service.initialize_service(self.flask_app.config)

    @property
    def get_app(self) -> Flask:
        return self.flask_app


class AppConfig:
    SERVICE_ENV = os.environ.get('SERVICE_ENV', default='development')
    REDIS_HOST = os.environ.get('REDIS_HOST', default='localhost')
    REDIS_PORT = os.environ.get('REDIS_PORT', default=6379)
    REDIS_P = os.environ.get('REDIS_P', default='')
