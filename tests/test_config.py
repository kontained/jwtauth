import unittest
from application import create_app
from config import Config


class TestDevelopmentConfig(unittest.TestCase):
    def setUp(self):
        developmentConfig = Config()
        developmentConfig.FLASK_DEBUG = True
        developmentConfig.SECRET_KEY = '123456789'
        self.app = create_app(developmentConfig)

    def test_app_is_development(self):
        self.assertTrue(self.app.config['FLASK_DEBUG'])

    def test_app_secret_key(self):
        self.assertTrue(self.app.config['SECRET_KEY'] == '123456789')

    def test_app_sqlite_database_uri(self):
        self.assertIsNotNone(self.app.config['SQLALCHEMY_DATABASE_URI'])

    def test_app_creation(self):
        self.assertIsNotNone(self.app)
