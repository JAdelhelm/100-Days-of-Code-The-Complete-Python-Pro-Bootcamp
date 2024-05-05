from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired

class MovieForm(FlaskForm):
    rating = FloatField('rating', validators=[DataRequired()])
    review = StringField('review', validators=[DataRequired()])
    done = SubmitField('Done')


class AddMovieForm(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired()])
    add_movie = SubmitField('Add Movie')