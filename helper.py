import os
from config import Config
from application import db, create_app


def create_database():
    app = create_app(Config())
    app_context = app.app_context()
    app_context.push()
    db.create_all()


if __name__ == '__main__':
    create_database()
