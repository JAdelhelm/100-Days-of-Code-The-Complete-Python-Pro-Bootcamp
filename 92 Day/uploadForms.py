from flask_wtf import FlaskForm
from wtforms import PasswordField, EmailField, SubmitField, StringField,TextAreaField, URLField, BooleanField
from wtforms.validators import DataRequired, Length, Email

class UploadForm(FlaskForm):
   name = StringField('Name of Task', [Length(min=1, max=150)])
   description = TextAreaField('Description', [Length(min=1, max=2000)])
   submit_task = SubmitField(label="Add Task")

