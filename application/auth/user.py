from datetime import datetime
from application import db


class User(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True)

    username = db.Column(
        db.String(64),
        index=True,
        nullable=False,
        unique=True)

    password_hash = db.Column(
        db.String(128),
        nullable=False)

    def __repr__(self):
        return (
            '<id: {} username: {} password_hash: {}>'
            .format(self.id, self.username, self.password_hash)
        )
