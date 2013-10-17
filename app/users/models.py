from app.mixins import CRUDMixin
from flask.ext.login import UserMixin
from app import db, bcrypt
from app.posts.models import Post

class User(UserMixin, CRUDMixin,  db.Model):
    __tablename__ = 'users_user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(120))

    posts = db.relationship('Post', backref='post', lazy='dynamic')

    def __init__(self, name=None, email=None, password=None):
        self.name = name
        self.email = email
        self.password = bcrypt.generate_password_hash(password)

    def __repr__(self):
        return '<User %r>' % (self.name)
