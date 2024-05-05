# This form is only for registration purpose, User and RegistrationForm are two different forms
from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, SubmitField, IntegerField
from wtforms.validators import DataRequired

class RegistrationForm(FlaskForm):
    email = EmailField('email', validators=[DataRequired()])
    name = StringField('name', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    submit = SubmitField('Sign me up!')


class LoginForm(FlaskForm):
    email = EmailField('email', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    submit = SubmitField('Let me in.')