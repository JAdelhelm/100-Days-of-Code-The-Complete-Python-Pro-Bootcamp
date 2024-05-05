from flask_wtf import FlaskForm
from flask_ckeditor import CKEditorField
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class PostForm(FlaskForm):
    title = StringField('Blog Post Title')
    subtitle = StringField("Subtitle")
    author = StringField("Your Name")
    img_url = StringField("Blog Image URL")
    # This field (body) is from ckeditor.
    body = CKEditorField('Body') 
    submit = SubmitField('Submit Post')