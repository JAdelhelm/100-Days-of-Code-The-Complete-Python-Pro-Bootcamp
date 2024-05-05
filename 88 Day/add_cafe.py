from flask_wtf import FlaskForm
from wtforms import PasswordField, EmailField, SubmitField, StringField, URLField, BooleanField
from wtforms.validators import DataRequired, Length, Email

class CafeAdd(FlaskForm):
   name = StringField('Cafe', [Length(min=1, max=150)])
   map_url = URLField('Maps-URL', [Length(min=1, max=150)])
   img_url = URLField('IMG-URL', [Length(min=1, max=150)])
   location = StringField('Location', [Length(min=1, max=150)])
   seats = StringField('Seats', [Length(min=1, max=150)])
   coffee_price = StringField('Coffee-Price', [Length(min=1, max=150)])
   has_wifi = BooleanField('Has Wifi')
   has_toilet = BooleanField('Has toilets')
   has_sockets = BooleanField('Has sockets')
   can_take_calls = BooleanField('Can take calls')
   submit_cafe = SubmitField(label="Add Cafe")

   

# <div class="container">
# {{render_form(form, form_group_classes="mb-1")}}
# </div>