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

    return application
