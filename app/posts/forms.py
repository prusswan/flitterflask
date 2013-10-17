from flask.ext.wtf import Form, RecaptchaField
from wtforms import TextField, PasswordField, BooleanField, fields, validators
from wtforms.validators import Required, Email, EqualTo

from app.users.models import User
from app import db

class SubmitPostForm(Form):
    body = fields.TextField(validators=[validators.required()])
