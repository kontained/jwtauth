import unittest
from config import Config
from application import db, create_app
from application.auth.authentication import Authentication, AuthenticationResponse


class TestAuthentication(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        developmentConfig = Config()
        developmentConfig.FLASK_DEBUG = True
        developmentConfig.SECRET_KEY = '123456789'
        self.app = create_app(developmentConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.target = Authentication()
        db.create_all()

    @classmethod
    def tearDownClass(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_authentication_creation(self):
        self.assertIsNotNone(self.target)

    def test_authentication_register_user_no_username(self):
        input = {
            'password' : 'test'
        }

        result = self.target.register_user(input)

        self.assertTrue(isinstance(result, AuthenticationResponse))
        self.assertFalse(result.success)
        self.assertIsNotNone(result.message)

    def test_authentication_register_user_no_password(self):
        input = {
            'username' : 'test'
        }

        result = self.target.register_user(input)

        self.assertTrue(isinstance(result, AuthenticationResponse))
        self.assertFalse(result.success)
        self.assertIsNotNone(result.message)

    def test_authentcation_register_user(self):
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

        result = self.target.login(input)

        self.assertTrue(isinstance(result, AuthenticationResponse))
        self.assertFalse(result.success)

    def test_authentication_login_no_password(self):
        input = {
            'username': 'test'
        }

        result = self.target.login(input)

        self.assertTrue(isinstance(result, AuthenticationResponse))
        self.assertFalse(result.success)