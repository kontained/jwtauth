import unittest
from config import Config


class TestDevelopmentConfig(unittest.TestCase):
    def setUp(self):
        self.developmentConfig = Config()
        self.developmentConfig.FLASK_DEBUG = True
        self.developmentConfig.SECRET_KEY = '123456789'

    def test_config_flask_development(self):
        self.assertTrue(self.developmentConfig.FLASK_DEBUG)

    def test_config_secret_key(self):
        self.assertTrue(self.developmentConfig.SECRET_KEY == '123456789')

    def test_config_sqlite_database_uri(self):
        self.assertIsNotNone(self.developmentConfig.SQLALCHEMY_DATABASE_URI)

    def test_config_sqlalchemy_track_modifications(self):
        self.assertFalse(self.developmentConfig.SQLALCHEMY_TRACK_MODIFICATIONS)
