from flask_wtf import FlaskForm
from wtforms import PasswordField, EmailField, SubmitField, StringField
from wtforms.validators import DataRequired, Length, Email


# pip install email_validator
class LoginForm(FlaskForm):
    username = StringField(label='Username', validators=[DataRequired()], render_kw={'style': 'width: 30ch'})
    password = PasswordField(label='Password', validators=[
                             DataRequired()], render_kw={'style': 'width: 30ch'})
    submit = SubmitField(label="Log In", render_kw={'btn-primary': 'True'})