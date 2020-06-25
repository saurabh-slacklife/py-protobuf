from src.io.slacklife.app import ManageApp

app = ManageApp()
logger = app.logger
flask_app = app.get_app
logger.info(f'Service started with routes: {flask_app.url_map}')
logger.info(f'App config: {flask_app.config}')
