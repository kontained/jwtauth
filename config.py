import os
baseDirectory = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    FLASK_DEBUG = os.environ.get('FLASK_DEBUG')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(baseDirectory, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    LOG_FILE = 'logs/auth.log'
