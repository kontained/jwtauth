import unittest
from application.auth.user import User


class TestUser(unittest.TestCase):
    def setUp(self):
        self.target = User(
            id=1,
            username='test',
            password_hash='123456789'
        )

    def test_user_creation(self):
        self.assertIsNotNone(self.target)

    def test_user_repr_method(self):
        self.assertIsNotNone(self.target.__repr__())
