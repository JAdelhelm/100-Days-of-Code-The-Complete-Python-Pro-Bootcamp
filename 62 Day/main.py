from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import csv
import pandas as pd
from cafe_add import AddCafe

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = AddCafe()
    if form.validate_on_submit():
        print("True")

        df_row = pd.DataFrame({'Cafe Name': [request.form.get('cafe_name')],'Location': [request.form.get('cafe_location')], 'Open': [request.form.get('cafe_opening')], 
                               'Close': [request.form.get('cafe_closing')],'Coffee': [request.form.get('coffee_rating')], 
                               'Wifi': [request.form.get('wifi_rating')],'Power': [request.form.get('power_socket')]})
        
        df_conc = pd.read_csv("./cafe-data.csv")
        df_conc = pd.concat([df_conc, df_row], axis=0)
        df_conc.to_csv("./cafe-data.csv", index=False)
        return render_template("add-success.html")


    return render_template('add.html', form=form)


def pandas_handle_cafes():
    df = pd.read_csv("./cafe-data.csv")
    title = list(df.columns)
    content = df.values
    return title, content



@app.route('/cafes')
def cafes():
    title, content = pandas_handle_cafes()
    return render_template('cafes.html', title_columns=title, content=content)


if __name__ == '__main__':
    app.run(debug=True)
