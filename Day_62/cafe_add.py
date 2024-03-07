from flask_wtf import FlaskForm
from wtforms import StringField, URLField, SelectField, SubmitField, TimeField
from wtforms.validators import DataRequired


class AddCafe(FlaskForm):
    cafe_name = StringField(label="Cafe name", validators=[
                            DataRequired()], render_kw={"style": "margin-bottom: 15px;"})
    cafe_location = URLField(label="Cafe Location on Google Maps (URL)", validators=[
                             DataRequired()], render_kw={"style": "margin-bottom: 15px;"})
    cafe_opening = TimeField(label="Opening Time e.g. 8AM", validators=[
                             DataRequired()], render_kw={"style": "margin-bottom: 15px;"})
    cafe_closing = TimeField(label="Closing Time e.g. 5:30PM", validators=[
                             DataRequired()], render_kw={"style": "margin-bottom: 15px;"})
    coffee_rating = SelectField(label="Coffee Rating", choices=["☕", "☕☕", "☕☕☕", "☕☕☕☕", "☕☕☕☕☕"], validators=[
                                DataRequired()], render_kw={"style": "margin-bottom: 15px;"})
    wifi_rating = SelectField(label="Wifi Strength Rating", choices=["✖️", "💪", "💪💪", "💪💪💪", "💪💪💪💪", "💪💪💪💪💪"
                              ], validators=[DataRequired()], render_kw={"style": "margin-bottom: 15px;"})
    power_socket = SelectField(label="Power Socket Availability", choices=[
                               "✖️", "🔌", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌🔌🔌"], validators=[DataRequired()], render_kw={"style": "margin-bottom: 15px;"})

    submit = SubmitField('Submit')
