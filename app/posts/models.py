from app import db
from app.mixins import CRUDMixin

from datetime import datetime

class Post(CRUDMixin, db.Model):
    __tablename__ = 'post'

    id = db.Column(db.Integer, primary_key=True)

    body = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('users_user.id'))
    created_at = db.Column(db.DateTime)

    def __init__(self, user_id=None, body=None, created_at=None):
        self.user_id = user_id
        self.body = body
        self.created_at = datetime.utcnow()

    def __repr__(self):
        return '<Post %r>' % (self.body)
