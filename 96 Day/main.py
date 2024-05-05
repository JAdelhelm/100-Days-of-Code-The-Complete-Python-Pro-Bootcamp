"""
Alpha Vantage - Stock News

Build a custom website using an API that you find interesting.
"""

from flask import Flask, render_template, redirect, url_for, request, flash
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float, Boolean, select, update, delete, values, text, insert
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
import json
import pandas as pd
from flask import render_template, request, jsonify
from sqlalchemy import func
import random 
import string


API_KEY = ""


app = Flask(__name__,
            static_folder="./static",
            template_folder="./templates")



app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


@app.route("/chars", methods=["GET","POST"])
def get_characters():
    random_20_chars = [str(random.randint(1,183)) for val in range(20)]
    random_20_chars_str = ','.join(random_20_chars)
    get_chars = requests.get(f"https://rickandmortyapi.com/api/character/{random_20_chars_str}")
    get_chars_json = get_chars.json()
    # print(get_chars_json)

    return render_template('index.html', show_characters= True, list_of_chars=get_chars_json)
    # return render_template("index.html",list_of_characters, show_characters)



@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        # print("POST REQ")
        return redirect(url_for('get_characters'))
            
    return render_template("index.html")




if __name__ == "__main__":
    app.run(debug=True)