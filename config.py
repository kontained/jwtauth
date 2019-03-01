import os


class Config(object):
    FLASK_DEBUG = os.environ.get('FLASK_DEBUG')
