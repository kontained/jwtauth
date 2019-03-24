import os
import logging
from logging.handlers import TimedRotatingFileHandler
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()


def create_app(config_class=Config):
    application = Flask(__name__)
    application.config.from_object(config_class)
    db.init_app(application)

    # have to import here, so db is importable
    from application.auth import auth_blueprint
    application.register_blueprint(auth_blueprint, url_prefix='/auth')

    from application.errors import errors_blueprint
    application.register_blueprint(errors_blueprint)

    if not os.path.exists('logs'):
        os.mkdir('logs')

    file_handler = TimedRotatingFileHandler(config_class.LOG_FILE, when='D', interval=1)

    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s'
        ' [in %(pathname)s:%(lineno)d'
    ))
    file_handler.setLevel(logging.INFO)

    application.logger.addHandler(file_handler)
    application.logger.setLevel(logging.INFO)
    application.logger.info('Auth API started!')

    return application
