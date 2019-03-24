import unittest
from unittest import mock
from config import Config
from application import db, create_app
from application.auth.user import User
from application.auth.authentication import Authentication, AuthenticationResponse


class TestAuthentication(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        developmentConfig = Config()
        developmentConfig.FLASK_DEBUG = True
        developmentConfig.SECRET_KEY = '123456789'
        developmentConfig.SQLALCHEMY_DATABASE_URI = 'sqlite://'
        self.app = create_app(developmentConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.target = Authentication()

    def setUp(self):
        User.query.delete()
        db.session.commit()

    @classmethod
    def tearDownClass(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_authentication_creation(self):
        self.assertIsNotNone(self.target)

    def test_authentication_register_user_no_username(self):
        input = {
            'password': 'test'
        }

        with self.assertRaises(Exception):
            self.target.register_user(input)

    def test_authentication_register_user_no_password(self):
        input = {
            'username': 'test'
        }

        with self.assertRaises(Exception):
            self.target.register_user(input)

    @mock.patch('application.auth.authentication.create_user_token')
    def test_authentication_token_factory_raise_exception(self, mock_token_factory):
        input = {
            'username': 'test',
            'password': 'test'
        }

        mock_token_factory.side_effect = ValueError('test')

        with self.assertRaises(Exception):
            self.target.register_user(input)

    def test_authentication_register_user(self):
        input = {
            'username': 'test',
            'password': 'test'
        }

        result = self.target.register_user(input)

        self.assertTrue(isinstance(result, AuthenticationResponse))

    def test_authentication_login_no_username(self):
        input = {
            'password': 'test'
        }

        with self.assertRaises(Exception):
            self.target.login(input)

    def test_authentication_login_no_password(self):
        input = {
            'username': 'test'
        }

        with self.assertRaises(Exception):
            self.target.login(input)

    def test_authentication_login(self):
        input = {
            'username': 'test',
            'password': 'test'
        }

        self.target.register_user(input)
        result = self.target.login(input)

        self.assertTrue(isinstance(result, AuthenticationResponse))
        self.assertTrue(result.success)
