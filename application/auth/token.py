from datetime import datetime
from application import db


class Token(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, index=True, nullable=False)
    token = db.Column(db.String(500), unique=True, nullable=False)
    time_issued = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    time_expired = db.Column(db.DateTime, index=True)
    time_blacklisted = db.Column(db.DateTime, index=True)

    def __repr__(self):
        return '<id: {} token: {} time_issued: {} time_expired: {} time_blacklisted: {}' \
            .format(self.id, self.token, self.time_issued, self.time_expired, self.time_blacklisted)
