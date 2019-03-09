import unittest
from config import Config
from application import create_app
from application.auth.token import create_user_token
from application.auth.user import User


class TestToken(unittest.TestCase):
    def setUp(self):
        developmentConfig = Config()
        developmentConfig.FLASK_DEBUG = True
        developmentConfig.SECRET_KEY = '123456789'
        self.app = create_app(developmentConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_create_user_token_not_user_instance(self):
        with self.assertRaises(AttributeError):
            create_user_token('1')

    def test_create_user_token(self):
        user = User(
            id=1,
            username='test',
            password_hash='test'
        )
        result = create_user_token(user)
        self.assertTrue(isinstance(result, bytes))
