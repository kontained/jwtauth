from flask import Flask


def create_app(config_class):
    application = Flask(__name__)
    application.config.from_object(config_class)

    return application
