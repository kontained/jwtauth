from datetime import datetime, timedelta
import jwt
from flask import current_app
from .user import User


def create_user_token(user):
    payload = {
        'exp': datetime.utcnow() + timedelta(days=1),
        'iat': datetime.utcnow(),
        'sub': user.id
    }

    return jwt.encode(
        payload,
        current_app.config.get('SECRET_KEY'),
        algorithm='HS256'
    )


def validate_user_token(token):
    return jwt.decode(
        token,
        current_app.config.get('SECRET_KEY'),
        algorithms=['HS256'])
