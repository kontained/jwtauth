from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app(config_class):
    application = Flask(__name__)
    application.config.from_object(config_class)
    db.init_app(application)

    return application
