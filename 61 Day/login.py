from flask_wtf import FlaskForm
from wtforms import PasswordField, EmailField, SubmitField
from wtforms.validators import DataRequired, Length, Email


# pip install email_validator
class LoginPage(FlaskForm):
    email = EmailField(label='Email', validators=[DataRequired(),
                                                  Email()], render_kw={'style': 'width: 30ch'})
    password = PasswordField(label='Password', validators=[
                             DataRequired(), Length(min=8)], render_kw={'style': 'width: 30ch'})
    submit = SubmitField(label="Log In", render_kw={'btn-primary': 'True'})
