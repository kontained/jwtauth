import unittest
from unittest import mock
from jwt import ExpiredSignatureError, DecodeError
from datetime import datetime
from config import Config
from application import create_app
from application.auth.token_factory import create_user_token, validate_user_token
from application.auth.user import User


class TestToken(unittest.TestCase):
    def setUp(self):
        developmentConfig = Config()
        developmentConfig.FLASK_DEBUG = True
        developmentConfig.SECRET_KEY = '123456789'
        developmentConfig.SQLALCHEMY_DATABASE_URI = 'sqlite://'
        self.app = create_app(developmentConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def build_user(self):
        return User(
            id=1,
            username='test',
            password_hash='test'
        )

    def test_create_user_token_not_user_instance(self):
        with self.assertRaises(AttributeError):
            create_user_token('1')

    def test_create_user_token(self):
        result = create_user_token(self.build_user())
        self.assertTrue(isinstance(result, bytes))

    def test_decode_token(self):
        token = create_user_token(self.build_user())
        result = validate_user_token(token)
        self.assertIsNotNone(result)

    @mock.patch('application.auth.token_factory.datetime')
    def test_decode_expired_token(self, mock_datetime):
        mock_datetime.utcnow = mock.Mock(return_value=datetime(2010, 1, 1))
        token = create_user_token(self.build_user())
        with self.assertRaises(ExpiredSignatureError):
            validate_user_token(token)

    def test_decode_modified_token(self):
        token = create_user_token(self.build_user())
        test = bytearray(token)
        test[0] = 100
        with self.assertRaises(DecodeError):
            validate_user_token(bytes(test))
