import jwt
import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from application import db
from application.auth.user import User
from application.auth.token import create_user_token


class AuthenticationResponse():
    def __init__(self, success, message=None, token=None):
        self.success = success
        self.message = message
        self.token = token


class Authentication():
    def register_user(self, post_data):
        user = User.query.filter_by(username=post_data.get('username')).first()

        if not user:
            try:
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
            except Exception as e:
                return AuthenticationResponse(
                    False,
                    str(e)
                )
        else:
            return AuthenticationResponse(
                False,
                'An account already exists with that username!'
            )

    def login(self, post_data):
        user = User.query.filter_by(username=post_data.get('username')).first()

        try:
            if user and check_password_hash(user.password, post_data.get('password')):
                pass
            else:
                return AuthenticationResponse(
                    False,
                    'Account could not be authenticated at this time.'
                )
        except Exception as e:
            return AuthenticationResponse(
                False,
                str(e)
            )
