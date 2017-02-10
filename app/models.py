from werkzeug.security import generate_password_hash, check_password_hash
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    name = db.Column(db.String(64), index=True, unique=False)
    initials = db.Column(db.String(2), index=True, unique=False)
    extension = db.Column(db.Integer, index=True, unique=False)
    active = db.Column(db.Integer)

    def __repr__(self):
        return '<Email %r>' % (self.email)

    @property
    def password(selfself):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)