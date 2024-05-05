from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5

from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, SubmitField, EmailField, TextAreaField
from wtforms.validators import DataRequired, Length


class ContactForm(FlaskForm):
    email = EmailField(label="Email:")
    textfield = TextAreaField(label="Enter your message:")
    submit = SubmitField()