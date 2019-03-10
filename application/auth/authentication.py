import jwt
import traceback
import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from application import db
from application.auth.user import User
from application.auth.token_factory import create_user_token


class AuthenticationResponse():
    def __init__(self, success, message=None, token=None):
        self.success = success
        self.message = message
        self.token = token

    def to_json(self):
        return {
            'success': self.success,
            'message': self.message,
            'token': self.token.decode() if self.token is not None else ''
        }


class Authentication():
    def register_user(self, post_data):
        try:
            user = User.query.filter_by(
                username=post_data.get('username')).first()

            if not user:
                user = User(
                    username=post_data.get('username'),
                    password_hash=generate_password_hash(
                        post_data.get('password'))
                )

                db.session.add(user)
                db.session.commit()

                return AuthenticationResponse(
                    success=True,
                    token=create_user_token(user)
                )
            else:
                return AuthenticationResponse(
                    False,
                    'An account already exists with that username!'
                )
        except Exception as e:
            db.session.rollback()
            return AuthenticationResponse(
                False,
                str(e)
            )

    def login(self, post_data):
        try:
            user = User.query.filter_by(
                username=post_data.get('username')).first()

            if user and check_password_hash(user.password_hash, post_data.get('password')):
                return AuthenticationResponse(
                    success=True,
                    token=create_user_token(user)
                )
            else:
                return AuthenticationResponse(
                    False,
                    'Account could not be authenticated at this time.'
                )
        except Exception as e:
            return AuthenticationResponse(
                False,
                traceback.format_exc()
            )
