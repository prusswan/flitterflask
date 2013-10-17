from flask.ext.wtf import Form, RecaptchaField
from wtforms import TextField, PasswordField, BooleanField, fields, validators
from wtforms.validators import Required, Email, EqualTo

from app.users.models import User
from app import db, bcrypt

class LoginForm(Form):
    name = fields.TextField(validators=[validators.required()])
    password = fields.PasswordField(validators=[validators.required()])

    def validate(self):
        user = self.get_user()

        if user is None:
            raise validators.ValidationError('Invalid user')

        if not bcrypt.check_password_hash(user.password, self.password.data):
            raise validators.ValidationError('Invalid password')

        return True

    def get_user(self):
        print self.name.data, "here"
        return db.session.query(User).filter_by(name=self.name.data).first()

class RegistrationForm(Form):
    name = fields.TextField(validators=[validators.required()])
    email = fields.TextField(validators=[validators.Email()])
    password = fields.PasswordField(validators=[validators.required()])
    confirm_password = fields.PasswordField(validators=[
        validators.required(),
        validators.EqualTo('password', message='Passwords must match')
    ])

    def validate(self):
        if db.session.query(User).filter_by(name=self.name.data).count() > 0:
            raise validators.ValidationError('Duplicate username')

        return True
