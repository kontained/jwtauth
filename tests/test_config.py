import unittest
from application import create_app
from config import Config


class TestDevelopmentConfig(unittest.TestCase):
    def create_test_app(self):
        developmentConfig = Config()
        developmentConfig.FLASK_DEBUG = True
        return create_app(developmentConfig)

    def test_app_is_development(self):
        app = self.create_test_app()
        self.assertTrue(app.config['FLASK_DEBUG'])
