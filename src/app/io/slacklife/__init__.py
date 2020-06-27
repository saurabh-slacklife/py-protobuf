from app.io.slacklife.app import ManageApp
from app.io import logger

app = ManageApp()
flask_app = app.get_app
logger.info(f'Service started with routes: {flask_app.url_map}')
logger.info(f'App config: {flask_app.config}')
