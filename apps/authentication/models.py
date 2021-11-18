from apps import db
from flask_login import UserMixin


class Users(UserMixin, db.Model):
    """  Create the Users"""

    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    abNumber = db.Column(db.String(10), nullable=False, unique=True)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String(200), unique=False,nullable=False)
    last_login = db.Column(db.DateTime, index=False, unique=False, nullable=True)

    def __repr__(self):
        return '<User {}>'.format(self.abNumber)
